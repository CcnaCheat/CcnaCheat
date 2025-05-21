Here's a clear guide on **how to download and install Python** on Windows:

---

## 🐍 **How to Download & Install Python**

### ✅ Step 1: Download Python

Go to the official Python website:
🔗 [https://www.python.org/downloads/](https://www.python.org/downloads/)

It will automatically suggest the right version for your OS.

---

## 💻 **Windows**

### 🔹 1. Download the Installer:

* Go to: [https://www.python.org/downloads/windows](https://www.python.org/downloads/windows)
* Click the **“Download Python”** button (e.g., `Python 3.12.x`)

### 🔹 2. Run the Installer:

* ✅ Important: **Check the box** that says:

  ```
  [✓] Add Python to PATH
  ```
* Click **Install Now**
* Wait for installation to complete.

### 🔹 3. Verify Installation:

Open Command Prompt and run:

```cmd
python --version
```

or

```cmd
python3 --version
```

You should see something like:

```
Python 3.12.x
```










To run your Python script successfully, you need to install several packages. You can install all the required packages using `pip`. Here are the **commands to set up the packages**:

### ✅ 1. Install Required Python Packages

Open a terminal or command prompt and run:

```bash
pip install pyautogui pytesseract pillow keyboard requests
```

> You might need to use `pip3` instead of `pip` depending on your system.

---

### ✅ 2. Install Tesseract OCR Engine

The `pytesseract` library is a Python wrapper, but you still need to install **Tesseract** itself:

#### 🔹 Windows:

Download the installer from:
[https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

Make sure to note the installation path (e.g., `C:\Program Files\Tesseract-OCR\tesseract.exe`) and update it in your script:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

To add your **Groq API key** from [https://console.groq.com](https://console.groq.com), follow these steps:

---

### ✅ **1. Get Your API Key from Groq**

1. Go to: [https://console.groq.com/keys](https://console.groq.com/keys)
2. Log in and click **“Create API Key”**
3. Copy the key (e.g., `gsk_live_...`)

---

### ✅ **2. Paste it into Your Script**

Open your `sika.py` and **replace this line**:

```python
GROQ_API_KEY = "replace"  # Replace with your Groq API key
```



> ⚠️ Make sure to **keep the key in quotes** and do **not** share it publicly.

---





To run your Python file `sika.py`, follow these steps based on your operating system:

---

### ✅ **Step-by-Step: Run `sika.py`**

#### 🔹 **Windows / Ubuntu / macOS (Terminal or Command Prompt)**

Navigate to the folder where `sika.py` is located. Use:

```bash
cd path/to/your/script
```

Then run:

```bash
python sika.py
```

> If `python` doesn't work, try:
>
> ```bash
> python3 sika.py
> ```

---

### 🛠️ **Example** (Windows)

If your script is on the desktop:

```bash
cd Desktop
python sika.py
```

---

### ⚠️ **Make sure:**

1. You installed the required packages (`pyautogui`, `pytesseract`, etc.).
2. Tesseract is installed and the path is correctly set in your script.
3. You're running the command from the same environment where the packages were installed.

---



