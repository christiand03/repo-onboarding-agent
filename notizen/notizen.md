# Vision
Unsere Vision ist es, die mühsame Einarbeitung in unbekannte Repositories in einen automatisierten, mühelosen Prozess zu verwandeln. Der Repo-Onboarding-Agent ermöglicht es Entwicklern, schneller produktiv zu werden, indem er autonom eine umfassende technische Übersicht für jedes beliebige GitHub-Repository generiert.



# Core Workflow
1. User Prompt: "Create a technical onboarding guide for the repository at https://github.com/user/repo."
2. Agent Action:  Klont das angegebene Repository und durchleuchtet dessen Inhalt (Welche Tools brauchen wir dafür?)
3. Agent Action:  Analysiert die Verzeichnisstruktur, erkennt das verwendete Framework, die Programmiersprache und listet alle kritischen Abhängigkeiten auf -> + Tree View erstellen
4. Agent Action: Projekttyp erkennen (Python Web App, Java Backend Application etc) 
5. Agent Action: Wichtigste Dokumente erkennen
6. Agent Action: Abstract Syntax Tree erstellen
7. LLM: Informationen zu einem Report zusammenführen
8. Agent Action: Report (lokal?) abspeichern oder ausgeben





# Tech Stack
- Gemini API / OpenAI API / Anthropic API / lokal open source für development um Kosten zu sparen
- Huggingface
- Ollama
- LangChain mit vorkonfiguriertem Agent starten + LLM konfigurieren  
- Mermaid.js für Diagramme? https://github.com/mermaid-js/mermaid (eher nicht)
    - Alternativ: Graphviz oder PlantUML -> lieber PlantUML 




# Key Components
- Agent -> LangChain, LlamaIndex
    - Agent State Management
    - Tool execution -> MCP Server?
- Python Functions die der Agent verwenden kann
    - Repo Documents bekommen
    - Repo structure analysieren
    - Abstract Syntax Tree & Tree View erstellen
    - Report abspeichern
- UI / Frontend -> Streamlit
- System Prompts -> Langfuse 
- Guardrails -> Guardrail Agent Stichwort Multi Agent System?

# Agent
- Zentrale Steuerungseinheit die User Prompt entgegen nimmt, in einen Ablaufplan zerlegt, entscheidet welche Werkzeuge wann eingesetzt werden, ruft diese auf und verarbeitet das Ergebnis

- LangChain oder LlamaIndex

# LLM
- Aus dem gegebenen Ziel den Plan formulieren
- Ergebnisse der Werkzeuge interpretieren
- Alle gesammelten Informationen zu einem Report zusammenführen

- OpenAI API / Gemini API / Anthropic API / open source

# Werkzeuge
- GitPython für git clone Befehl
- Tool um Metadaten auszulesen
- ast Modul oder slimit für AST Erstellung von jeder Datei
    - ast.ClassDef, ast.FunctionDef, ast.Import, ast.ImportFrom extrahieren
    - Call Graph erstellen für jede Function mit ast.Call -> Welche Funktionen werden von anderen Funktionen aufgerufen (ast + pycg + networkx)
    - Klassenstruktur und Vererbung mit ast.ClassDef "bases" Attribut und FunctionDef für jede Funktion der Klasse
    - mit ast.get_docstring() die Docstrings aus den Methoden auslesen
    -  

# Frontend
- Wird benötigt damit der Nutzer seinen Prompt eingeben kann und den fertigen Report angezeigt bekommen 
-> Streamlit

# Hosting?
- Kann der Code vollständig lokal laufen oder muss dieser / Teile davon irgendwo gehosted werden?



# Projektablauf
- Phase 1: Proof of Concept erstellen:
    - Agent kann Repo klonen
    - Dateistruktur auslesen, Tech Stack identifizieren
- Phase 2: LLM integrieren
    - LLM API einrichten + System Prompts / Guardrails
    - Frontend für Nutzereingaben einrichten (Streamlit?)
    - Eine einzelne Datei erklären lassen
    -> Beweist das wir Code an KI senden können und Erklärung zurückbekommen
- Phase 3: Automatisierung und Verfeinerung:
    - Hauptdateien identifizieren
    - Code in Blöcke zerlegen
    - AST erstellen
    - Gesamtprozess zusammenführen
- Phase 4: Erweiterung
    - Weitere Modularitäten einfügen wenn noch Zeit vorhanden 
    - Fragen zu dem Repo beantworten?
    - Code Qualität überprüfen und Verbesserungen vorschlagen?
    - Datenbank anbinden wo genererierte Docs gespeichert werden
    - Bewertungsfeature einführen, positiv = in Datenbank speichern, negativ = speichern + neu generieren -> Erstellt gleichzeitig Labels für einen Datensatz von guten und schlechten Outputs
    - Guardrail Agent
    - Code embedden um semantisch ähnliche Bereiche als Kontext bei der Doc Erstellung hinzuzufügen


# Warum brauchen wir einen AI Agent?
- Mit einem linearen Ablauf der Toolcalls würde kein Agent gebraucht werden
-> Repos bestehen nicht nur aus einer Programmiersprache, die Tools müssen in mehreren Sprachen verfügbar sein und der Agent wählt je nach Sprache aus
- Tools können fehlschlagen
-> Agent adaptiert wenn ein Tool fehlschlägt damit der Nutzer keine Error message bekommt
- Repos können sehr groß werden, es ist unmöglich alles auf einmal zu analysieren
-> Agent kann eigenständig die relevantesten Dokumente auswählen und analysieren (benötigt Heuristic / Strategie zum Auswählen)
- Sobald die Anzahl oder Komplexität der zur Verfügung stehenden Tools größer wird, steigt der Nutzen des Agents