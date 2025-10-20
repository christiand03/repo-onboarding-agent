### Local Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/repo-onboarding-agent.git
```

2. Create and activate a virtual environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. create .gitignore
```bash
# Virtuelle Umgebung ignorieren
venv/
__pycache__/

# Datei für Umgebungsvariablen (für später)
.env

# VS Code spezifische Dateien
.vscode/
```

5. create .env
```bash
GOOGLE_API_KEY='XXX'
```