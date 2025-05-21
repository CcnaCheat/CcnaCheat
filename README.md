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



