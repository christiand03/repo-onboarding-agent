- einleitungsfolie
- motivation:
    - herausforderung des onboardings hervorheben
    - "jeder kennt das problem bla bla"
    - kurz problem beschreiben
- Vision / Ziel darstellen
- Wie kommen wir zu diesem Ziel?
- Key Components
    - Agent
    - LLM
    - Frontend
    - Tools
    - Sonstiges (System Prompts, Guardrails)
- Agent Workflow vorstellen
- Wie sieht unser MVP aus?
- Tech Stack
- Umsetzung / Roadmap
    - Bis Weihnachten sollte MVP stehen
    - Januar für Erweiterungen
- Risiken & Gegenmaßnahmen
    - ein/zwei Erweiterungen ansprechen, aber sagen das wir da noch keinen Fokus drauf legen wollen



Projektziele:
- User Interface als Web Application hosten
- Agent der autonom eine Documentation erstellen kann
- Der Nutzer ist mit der Documentation nach der ersten Generierung zufrieden
- Der Nutzer kann Feedback geben ob ihm die Documentation gefällt


MVP:
- Agent der reine Python Repos analysieren und dokumentieren kann, Dokumentationsinhalt sind die beschriebenen Bestandteile aus doc_bestandteile.md


Key Componentes:
- Was ist das Component?
- Welchen Zweck erfüllt es?
- Welche Technologien könnten wir dafür verwenden?

Welche Fähigkeiten soll der Agent besitzen?
- Github klonen
- code analysieren / interpretieren (an das LLM weitergeben)
- Allgemeine Projektdetails extrahieren
- Tech Stack erstellen
- Dependencies dokumentieren (und als requirements.txt festhalten?)
- Quick Start Guide
- Wichtigsten Anwendungsfälle
- Auflistung verfügbarer Befehle
- Erklärung der Funktionen/Methoden
    - Signatur (Name, Parameter, Typhinweise)
    - Kurzbeschreibung
    - Parameterbeschreibung
    - Rückgabewerte
- Architektur
    - Projektstruktur (Tree View)
    - Diagramme:
        - Komponentendiagramm
        - Klassendiagramm
        - Ablaufdiagramm
        - Datenbankschema
        - AST Diagramm
- wichtigste Dokumente erkennen 


# Milestones
- Heute 
- Tools erstellt (3 Wochen)
- System Prompts schreiben +
- LLM einbauen +
- Frontend bauen (1 Woche)
- Agent erstellen (2 Wochen)
- Zwischenpräsentation erstellen (1 Woche)
- Weihnachten
- (Guardrails)

# Projektrisiken
- Zu ambitionierte Ziele (wir haben zu wenig Zeit um das Projekt umzusetzen)
- Wir fokussieren uns zu sehr auf die Zukunft / Vision (was könnte man noch alles geiles Einfügen?) -> Fokus auf den MVP
- Repositories können aus vielen verschiedenen Sprachen bestehen -> Vorerst auf Python Repositories fokussieren, code parser als austauschbares modul schreiben um später mehrere Sprachen zu unterstützen
- Große Repositories / Dokumente verbrauchen viel Context Window -> Code Chunken in sinnvolle Blöcke um diese besser verarbeiten zu können 
- LLM kann halluzinieren -> detaillierte System Prompts, Guardrails