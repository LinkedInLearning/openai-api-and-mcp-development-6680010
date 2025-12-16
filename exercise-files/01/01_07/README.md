# 2. Learning the Core and Start Building 
[Documentation](https://platform.openai.com/docs/guides/evals?api-mode=responses)

Improve model outputs through evaluations to ensure AI responses meet your style and expectations.
---

**openai**: [OpenAI](https://openai.com/): OpenAI library for Python to build applications with GPT-3.
**streamlit**: [Streamlit](https://streamlit.io/): Streamlit is an open-source Python library that makes it easy to build beautiful custom web-apps for machine learning and data science.
**streamlit-chat**: [Streamlit Chat](https://pypi.org/project/streamlit-chat/): Streamlit Chat is a Streamlit component that allows you to add a chatbot to your Streamlit app. It uses OpenAI's GPT-3 to generate responses to user input.
**python-dotenv**: [Python Dotenv](https://pypi.org/project/python-dotenv/): Reads the key-value pair from .env file and adds them to environment variable. It is great for managing app settings during development and in production using 12-factor principles.
**pillow**: [Pillow](https://pypi.org/project/Pillow/): Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.
---

[1]- Python installation
[2]- Create and activate a virtual Environment
[3]- Install packages
[4]- Create API keys & set the environment variables 

### [1]-Python installation (recommended: python3.11)

#### macOS
1. **Check if Python is already installed**
   ```sh
   python3 --version
   ```
   If Python is not installed, proceed with the steps below.

2. **Install Homebrew (if not installed)**
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Install Python**
   ```sh
   brew install python3
   ```

4. **Check Python Version**
   ```sh
   python3 --version
   ```

#### Windows
1. **Download Python** from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Run the installer** and check the box **"Add Python to PATH"** before proceeding with the installation.

3. **Check Python Version**
   ```sh
   python --version
   ```

---

### [2]-Create and activate a virtual environment - [venv](https://docs.python.org/3/library/venv.html)

#### macOS
1. **Navigate to your project directory**
   ```sh
   cd /path/to/your/project
   ```

2. **Create a virtual environment**
   ```sh
   python3 -m venv .venv
   python3.11 -m venv .venv
   ```

3. **Activate the virtual environment**
   ```sh
   source .venv/bin/activate
   ```

4. **Verify that the virtual environment is active** (you should see `(venv)` in the terminal prompt).

#### Windows
1. **Navigate to your project directory**
   ```sh
   cd C:\path\to\your\project
   ```

2. **Create a virtual environment**
   ```sh
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   ```sh
   .venv\Scripts\activate
   ```

4. **Verify that the virtual environment is active** (Command Prompt should show `(venv)` before the directory path).

---

## Deactivating the Virtual Environment
For both macOS and Windows, deactivate the virtual environment by running:
```sh
 deactivate
```

---

### [3]-Install packages
(Mac)
```sh
pip3 install -r requirements.txt

```

(Windows)
```sh
pip install -r requirements.txt
```


#### On Windows:

Download the executable from the [official FFmpeg site](https://ffmpeg.org/download.html)


---

## Exiting the Virtual Environment
Simply run:
```sh
deactivate
```

### [4]-Create API keys & set the environment variables 

1. Create an OpenAI Account[OpenAI's API Keys page](https://platform.openai.com/signup/),
2. Go to [OpenAI's API Keys page](https://platform.openai.com/settings/organization/api-keys),
3. Click **Create new secret key** and copy it, 
4. You will need to add your billing information (MANAGE > Settings > Billing).  


#### Set environment variables 

##### macOS & Linux  
You can store the key in your shell configuration file:  

```sh
echo 'export OPENAI_API_KEY="your-secret-key"' >> ~/.bashrc
source ~/.bashrc
````

or add to `.env` file

```sh
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

```

### -Start the app

`streamlit run app.py`



