
# Secure Coding Task – CodeAlpha Cyber Security Internship

##  Intern Details
- **Name**: Bongani Funzo
- **Student ID**: CA/JU1/27523
- **Domain**: Cyber Security

---

## Task Overview
This task demonstrates how to identify and fix security vulnerabilities in Python code.

### Vulnerable Code: [`vulnerable_script.py`](./vulnerable_script.py)
The original script had the following critical issues:
1. **Hardcoded credentials** — Exposes sensitive data in plain text.
2. **Use of `eval()`** — Allows execution of arbitrary Python code.
3. **Unvalidated file access** — Could lead to directory traversal attacks.
4. **Unrestricted `os.system()`** — Vulnerable to command injection.

---

## Fixed Version: [`secure_script.py`](./secure_script.py)
All vulnerabilities have been addressed:
| Issue                 | Fix                                                   |
|-----------------------|-------------------------------------------------------|
| Hardcoded credentials | Replaced with secure input using `getpass`            |
| `eval()` usage        | Replaced with `ast.literal_eval()` and numeric checks |
| File access           | Restricted to a safe folder with filename validation  |
| Command injection     | Used `subprocess.run()` with command whitelist        |

---

## How to Use
1. Clone the repo or download the files.
2. Create a folder called `files` and place `.txt` files for testing file access.
3. Run `secure_script.py` and follow the prompts.

---

## Social Submission
Check out my LinkedIn post: [🔗 LinkedIn Task 3 Post](#)
> #SecureCoding #CyberSecurity #CodeAlpha #Python #Internship #InfoSec

---

## 📌 Notes
This task was part of the CodeAlpha Cyber Security Internship (July–August 2025).
