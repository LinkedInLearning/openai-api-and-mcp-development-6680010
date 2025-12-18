**Automate your project with Github Models and Actions**
======================================================

\[1\] - **Python Installation**  
\[2\] - **Create and Activate a Virtual Environment**  
\[3\] - **Install Package**  
\[4\] - **Setting up OpenAI Secret Key**  
\[5\] - **Integrate GitHub Models**

* * *

### \[1\] - Python Installation

#### macOS

1.  **Check if Python is already installed**
    
    shCopy code
    
    `python3 --version`
    
    If Python is not installed, proceed with the following steps.
    
2.  **Install Homebrew (if not installed)**
    
    shCopy code
    
    `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    
3.  **Install Python**
    
    shCopy code
    
    `brew install python3`
    
4.  **Check Python Version**
    
    shCopy code
    
    `python3 --version`
    

#### Windows

1.  **Download Python** from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/ "https://www.python.org/downloads/")
    
2.  **Run the installer** and check the box **"Add Python to PATH"** before proceeding with the installation.
    
3.  **Check Python Version**
    
    shCopy code
    
    `python --version`
    

* * *

### \[2\] - Create and Activate a Virtual Environment - [venv](https://docs.python.org/3/library/venv.html "https://docs.python.org/3/library/venv.html")

#### macOS

1.  **Navigate to your project directory**
    
    shCopy code
    
    `cd /path/to/your/project`
    
2.  **Create a virtual environment**
    
    shCopy code
    
    `python3 -m venv .venv`
    
3.  **Activate the virtual environment**
    
    shCopy code
    
    `source .venv/bin/activate`
    
4.  **Verify that the virtual environment is active** (you should see `(venv)` in the terminal prompt).
    

#### Windows

1.  **Navigate to your project directory**
    
    shCopy code
    
    `cd C:\path\to\your\project`
    
2.  **Create a virtual environment**
    
    shCopy code
    
    `python -m venv .venv`
    
3.  **Activate the virtual environment**
    
    shCopy code
    
    `.venv\Scripts\activate`
    
4.  **Verify that the virtual environment is active** (Command Prompt should show `(venv)` before the directory path).
    

* * *

**Deactivating the Virtual Environment**
----------------------------------------

For both macOS and Windows, deactivate the virtual environment by running:

shCopy code

 `deactivate`

* * *

### \[3\] - Install Packages

#### (macOS)

shCopy code

`pip3 install -r requirements.txt  export PYTHONPATH=$PYTHONPATH:/path/to/autogen_agentchat`

#### (Windows)

shCopy code

`pip install -r requirements.txt`

* * *

**Exiting the Virtual Environment**
-----------------------------------

Simply run:

shCopy code

`deactivate`

* * *

### \[4\] - Setting Up OpenAI Secret Key

1.  Create an OpenAI Account: [OpenAI's API Keys page](https://platform.openai.com/signup/ "https://platform.openai.com/signup/")
2.  Go to [OpenAI's API Keys page](https://platform.openai.com/settings/organization/api-keys "https://platform.openai.com/settings/organization/api-keys")
3.  Click **Create new secret key** and copy it.
4.  You will need to add your billing information (MANAGE > Settings > Billing).

* * *

#### **Set Environment Variables**

##### macOS & Linux

You can store the key in your shell configuration file:

shCopy code

`echo 'export OPENAI_API_KEY="your-secret-key"' >> ~/.bashrc source ~/.bashrc`

Or add to `.env` file:

shCopy code

`OPENAI_API_KEY="YOUR_OPENAI_API_KEY" GITHUB_TOKEN="YOUR_GITHUB_TOKEN"`

* * *

### \[5\] - Integrating GitHub Models

#### \*5.1 - Personal GitHub Account - [Authenticate](https://github.com/login "https://github.com/login")

#### \*5.2 - Create a Personal Access Token (PAT) or Fine-grained PAT - [Developer Settings](https://github.com/settings/personal-access-tokens "https://github.com/settings/personal-access-tokens")

#### \*5.3 - Install the required modules and SDKs

#### \*5.4 - Make an API Call - [**Quickstart Guide**](https://docs.github.com/fr/github-models/quickstart "https://docs.github.com/fr/github-models/quickstart")

shCopy code

`echo 'export GITHUB_TOKEN="your-secret-key"' >> ~/.bashrc source ~/.bashrc`

bashCopy code

`curl -s \   -X GET "https://models.github.ai/catalog/models" \   -H "Accept: application/vnd.github+json" \   -H "Authorization: Bearer $GITHUB_TOKEN" \ | jq`

#### \*5.5 - Models CLI

*   [GitHub Models Extension](https://github.com/github/gh-models "https://github.com/github/gh-models")
*   Install: `gh extension install https://github.com/github/gh-models`

#### (macOS)

shCopy code

`brew install gh`

#### (Windows)

shCopy code

`winget install GitHub.cli`

*   **Run Tests**:

bashCopy code

`gh models run openai/gpt-4o-mini "what is 1 + 1"`

* * *

### **Start the app**

#### (macOS)

shCopy code

`python3 main.py`

#### (Windows)

shCopy code

`python main.py`

