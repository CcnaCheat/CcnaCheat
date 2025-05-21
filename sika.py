import tkinter as tk
import pyautogui
import unicodedata
import re
from PIL import Image
import pytesseract
import os
import requests
import json
import keyboard

# --- Tesseract Path Configuration ---
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows
# Uncomment for macOS/Linux:
# pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'  # macOS
# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'        # Linux

# --- Check Tesseract Availability ---
try:
    pytesseract.get_tesseract_version()
    print("✅ Tesseract is installed and accessible.")
except Exception as e:
    print(f"❌ Tesseract is not installed or path is incorrect: {e}")
    print("Please install Tesseract from https://github.com/UB-Mannheim/tesseract/wiki (Windows)")
    print("or use 'brew install tesseract' (macOS) or 'sudo apt-get install tesseract-ocr' (Linux).")
    exit(1)

# --- Groq API Configuration ---
GROQ_API_KEY = "replace"  # Replace with your Groq API key
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {GROQ_API_KEY}"
}

# --- Load Questions and Answers from answers.txt ---
def load_qa_from_file(file_path="answers.txt"):
    qa_dict = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            current_question = None
            for line in lines:
                line = line.strip()
                if line.startswith('Q:'):
                    current_question = line[2:].strip()
                elif line.startswith('A:') and current_question:
                    qa_dict[current_question] = line[2:].strip()
                    current_question = None
        print(f"✅ Loaded {len(qa_dict)} question-answer pairs from {file_path}.")
        return qa_dict
    except FileNotFoundError:
        print(f"❌ File {file_path} not found. Falling back to Groq API for answers.")
        return {}
    except Exception as e:
        print(f"⚠️ Error reading {file_path}: {e}")
        return {}

# --- Call Groq API for Matching and Answering ---
def get_ai_answer(extracted_text, qa_dict):
    if not extracted_text:
        return "No valid text provided."
    
    try:
        # Prepare the prompt
        if qa_dict:
            # If answers.txt exists, ask the AI to match the extracted text to a question
            questions = list(qa_dict.keys())
            prompt = (
                f"The following text was extracted from a screenshot:\n\n'{extracted_text}'\n\n"
                f"Below is a list of questions with their answers:\n\n"
                + "\n".join([f"Q: {q}\nA: {qa_dict[q]}" for q in questions]) +
                f"\n\nTask: Determine which question from the list above is most relevant to the extracted text. "
                f"Return only the answer corresponding to the most relevant question. "
                f"If no question is relevant, provide a concise answer to the extracted text."
            )
        else:
            # If no answers.txt, answer the extracted text directly
            prompt = f"Answer the following question: {extracted_text}"

        payload = {
            "model": "meta-llama/llama-4-scout-17b-16e-instruct",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 150
        }
        response = requests.post(GROQ_API_URL, headers=HEADERS, data=json.dumps(payload))
        response.raise_for_status()
        result = response.json()
        answer = result.get("choices", [{}])[0].get("message", {}).get("content", "No answer generated.").strip()
        return answer if answer else "No answer generated."
    except Exception as e:
        return f"Error calling Groq API: {str(e)}"

# --- Normalize Text for AI Input ---
def normalize(text):
    text = text.lower()
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    text = re.sub(r'[^a-z0-9? ]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# --- Show Tooltip ---
def show_tooltip(answer, x, y):
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    
    tooltip_text = answer if answer else "No answer found."
    
    label = tk.Label(root, text=tooltip_text, bg='white', fg='black',
                     font=('Segoe UI', 9, 'bold'), bd=1, relief='solid',
                     wraplength=400, justify='left')
    label.pack(ipadx=10, ipady=6)
    root.geometry(f'+{x}+{y}')
    
    root.bind_all('<Button-1>', lambda e: root.destroy())
    root.after(5000, root.destroy)
    root.mainloop()

# --- Screenshot and Analyze Text ---
def handle_screenshot():
    print("📸 Capturing screen...")
    try:
        screenshot = pyautogui.screenshot()
        temp_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp_screen.png')
        screenshot.save(temp_file)

        extracted_text = pytesseract.image_to_string(Image.open(temp_file), config='--psm 3').strip()
        if not extracted_text:
            print("❌ No text extracted from screenshot.")
            show_tooltip("No text extracted.", pyautogui.position()[0] + 20, pyautogui.position()[1])
            return

        print("✅ Extracted Text:")
        print(extracted_text)

        # Load Q&A from answers.txt
        qa_dict = load_qa_from_file()

        # Get answer from Groq API
        print("🔍 Sending to Groq API for matching and answering...")
        cursor_x, cursor_y = pyautogui.position()
        answer = get_ai_answer(extracted_text, qa_dict)
        print(f"\nAI Answer: {answer}")
        show_tooltip(answer, cursor_x + 20, cursor_y)

    except Exception as e:
        print(f"⚠️ Error during screenshot processing: {e}")
        show_tooltip(f"Error: {str(e)}", pyautogui.position()[0] + 20, pyautogui.position()[1])
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

# --- Main Program ---
if __name__ == "__main__":
    print("🔹 Press Ctrl+X to capture and scan.")
    print("🔹 Press ESC to quit.")
    try:
        keyboard.add_hotkey('ctrl+x', handle_screenshot)
        keyboard.wait('esc')
    except Exception as e:
        print(f"⚠️ Error setting up hotkeys: {e}")
        print("Try running as administrator or check keyboard library installation.")