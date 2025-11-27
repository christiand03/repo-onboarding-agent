# Repo Onboarding Agent 🚀

**Repo Onboarding Agent** is an AI-powered tool designed to streamline the process of onboarding developers to new codebases.

## 🌟 Features

*   **Automated Code Analysis**: Scans the repository to understand file structures, dependencies, and logic.
*   **Automated Documentation Generation**: After analyzing the Repository a comprehensive Documentation is generated.
*   **Full-Stack Architecture**:
    *   **Backend**: Handles all the Logic and LLM interaction.
    *   **Frontend**: User interface for easy interaction with the agent. Hosted on the Streamlit Cloud for convenient access.
    *   **Database**: Persistent storage for analysis results and metadata.

## 🏃 Usage
1. Go to https://aistudio.google.com
2. In the bottom left corner 'get your API Key'
3. Create a Project & your API Key
4. Head on over to https://repo-agent.streamlit.app
5. Register as a User
6. Set your API Key
7. Choose the AI Models
8. Copy a Github Repository URL into the Chat
9. Wait for your Documentation to be generated! (it will take a while)
10. It would be appreciated if you leave Feedback on how to improve the provided Documentation

---

## Or if you want to work locally:

## 🛠️ Prerequisites

*   **Python** 
*   **Github Account** with Repos to be analyzed

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/christiand03/repo-onboarding-agent.git
cd repo-onboarding-agent
```

### 2. Configure Environment Variables
Copy the example environment file and configure your Gemini API key or Ollama Base URL.

```bash
cp .env.example .env
```
*Open `.env` in your editor and fill in the required Keys.*

### 3. Install Dependencies
Create a virtual environment and install the required packages using:

```bash
pip install -r requirements.txt
```

### 4. Start Streamlit
```bash
streamlit run frontend/Frontend.py
```


