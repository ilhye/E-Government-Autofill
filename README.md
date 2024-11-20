# E-Government Autofill
E-Government Autofill is a Python-based tool that automates the process of filling out government forms by pre-populating the required fields with user data. 

## Prerequisites
- Python 3.7 or later
- Google Chrome (latest version)
- ChromeDriver (compatible with your Chrome version)

### Step 1: Clone the repository
1. Clone the repository to your local machine:

    ```bash 
    git clone https://github.com/ilhye/E-Government-Autofill.git
    ```

### Step 2: Set Up a Virtual Environment
1. Navigate to the project directory:

    ```bash
    cd E-Government-Autofill
    ```
2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```
    
### Step 3: Install Dependencies
1. Install the required Python libraries:

    ```bash
    pip install selenium
    ```
2. Download and install ChromeDriver:
    - Check your version of Google Chrome and download the matching version of ChromeDriver from: ChromeDriver Downloads
    - Extract the chromedriver executable and place it in a directory included in your system's PATH, or specify the path directly in your code when initializing the WebDriver.

### Step 4: Running the Application
1. Once everything is set up, run the Python script to launch the tool:

    ```bash
    python Pagibig.py
    ```