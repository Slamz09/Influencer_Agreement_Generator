
---

## ✅ 1. **Install Python and Visual Studio Code (VS Code) or Notepad ++ ** *(Optional but recommended)**

🔹 On Windows:
1. Go to: [https://www.python.org/downloads](https://www.python.org/downloads)
2. Click "Download Python 3.x.x"
3. Open the installer:
   * **IMPORTANT**: Check the box that says **"Add Python to PATH"**
   * Click **"Install Now"**

To check it's installed:
* Open the **Command Prompt** (type `cmd` in Start Menu)
* Type:
  ``power shell
   ```
  python --version
  ```
  You should see something like: `Python 3.12.x`
---

## ✅ 2. **Create Your Project Folder and Project Files**

1. Create the project folder, e.g.:

   ```
   C:\Users\YourName\Documents\Influencer_Agreement_Generator

2. Create the project files:

```
| File Name                            | Purpose                                |
| ------------------------------------ | -------------------------------------- |
| `app.py`                             | Your main Python Flask app             |
| `Influencer_Agreement_Template.docx` | Your Word template with placeholders   |
| `templates/form.html` *(optional)*   | HTML form (if not using inline string) |
---
```

## ✅ 3. **Activate it**

* On Windows:

  ```powershell
  cd C:\Users\slamb\PythonProjects\Influencer_Agreement_Generator
  python .\influencer_app.py

