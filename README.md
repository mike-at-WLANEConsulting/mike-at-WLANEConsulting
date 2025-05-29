
## Python Project Setup Steps

Based on the project structure, here are the detailed steps followed to set up this Python project from scratch. These instructions are designed for junior engineers new to Python:

### 1. **Initialize Git Repository**
   - Created a new repository on GitHub or locally
   - Set up initial README.md file to document the project
   - **What this does:** Version control tracks changes to your code over time

### 2. **Create Project Structure**
   - Created `src/` directory for source code
   - Added Python scripts (e.g., `get-location-tree.py`)
   - **Why this matters:** Organizing code in folders makes projects easier to navigate and maintain

### 3. **Set Up Environment Management**
   - Created `.env` file for environment variables (storing sensitive data like API tokens)
   - Added `python-dotenv` dependency to load environment variables
   - **Security note:** Never commit `.env` files to version control - they contain secrets!
   - **Example `.env` file:**
     ```
     ACCESS_TOKEN=your_api_token_here
     ```

### 4. **Configure Dependencies**
   - Created `requirements.txt` file with project dependencies:
     - `requests>=2.31.0` for HTTP API calls
     - `python-dotenv>=1.0.0` for environment variable management
   - **What this does:** Lists all external libraries your project needs to run
   - **Why it's important:** Other developers can install the same versions you used

### 5. **Set Up Version Control**
   - Created comprehensive `.gitignore` file to exclude:
     - Environment files (`.env`) - keeps secrets safe
     - Python cache files (`__pycache__/`, `*.pyc`) - temporary files Python creates
     - Virtual environment directories - these are recreated locally
     - IDE-specific files (`.vscode/`, etc.) - personal editor settings
     - OS-specific files (`.DS_Store`, `Thumbs.db`) - system files
   - **What this does:** Prevents unnecessary or sensitive files from being tracked in Git

### 6. **Implement Core Functionality**
   - Developed API integration scripts
   - Used environment variables for secure credential management
   - Implemented proper error handling and response validation
   - **Best practices used:**
     - Check response status codes
     - Validate JSON responses before processing
     - Use meaningful variable names

### **Getting Started (For New Developers):**

#### Prerequisites:
- Install Python 3.7+ from [python.org](https://python.org)
- Install Git from [git-scm.com](https://git-scm.com)

#### Setup Steps:
1. **Clone this repository:**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
   *What this does: Creates an isolated Python environment for this project*

3. **Activate the virtual environment:**
   - **Windows:** `venv\Scripts\activate`
   - **Mac/Linux:** `source venv/bin/activate`
   *You'll see (venv) in your terminal prompt when active*

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *This installs all the libraries listed in requirements.txt*

5. **Set up environment variables:**
   - Copy `.env.example` to `.env` (if provided)
   - Or create a new `.env` file with your API credentials:
     ```
     ACCESS_TOKEN=your_actual_token_here
     ```

6. **Run the script:**
   ```bash
   python src/get-location-tree.py
   ```

#### **Important Notes for Beginners:**
- Always activate your virtual environment before working on the project
- Never commit your `.env` file - it contains secrets
- Use `pip freeze > requirements.txt` to update dependencies
- Deactivate virtual environment with `deactivate` command when done

