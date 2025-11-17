import re
import os
import tomllib

from typing import List, Dict, Any, Optional


class ProjektInfoExtractor:
    """
    Extrahiert grundlegende Projektinformationen aus gängigen Projektdateien
    wie README, pyproject.toml und requirements.txt.
    """
    def __init__(self):
        self.INFO_NICHT_GEFUNDEN = "Information not found"
        # Initialisiert die Struktur mit Platzhaltern
        self.info = {
            "projekt_uebersicht": {
                "titel": self.INFO_NICHT_GEFUNDEN,
                "beschreibung": self.INFO_NICHT_GEFUNDEN,
                "aktueller_status": self.INFO_NICHT_GEFUNDEN,
                "key_features": self.INFO_NICHT_GEFUNDEN,
                "tech_stack": self.INFO_NICHT_GEFUNDEN,
            },
            "installation": {
                "dependencies": self.INFO_NICHT_GEFUNDEN,
                "setup_anleitung": self.INFO_NICHT_GEFUNDEN,
                "quick_start_guide": self.INFO_NICHT_GEFUNDEN,
            }
        }

    def _finde_datei(self, patterns: List[str], dateien: List[Any]) -> Optional[Any]:
        """Sucht case-insensitiv nach einer Datei, die einem der Muster entspricht."""
        for datei in dateien:
            for pattern in patterns:
                if datei.path.lower().endswith(pattern.lower()):
                    return datei
        return None

    def _extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: List[str]) -> Optional[str]:
        """
        Extrahiert den Text unter einer Markdown-Überschrift (##).
        
        Args:
            inhalt (str): Der gesamte Markdown-Text.
            keywords (list): Eine Liste von alternativen Schlüsselwörtern für den Titel 
                             der Sektion (z.B. ["Installation", "Setup"]).
        
        Returns:
            str: Der extrahierte Textabschnitt oder None.
        """
        # Erstellt ein Regex-Pattern, das auf jedes der Schlüsselwörter reagiert
        keyword_pattern = "|".join(re.escape(k) for k in keywords)
        
        # Sucht nach "## Schlüsselwort" und erfasst alles bis zur nächsten "##" oder dem Dateiende
        pattern = re.compile(
            rf"##\s*({keyword_pattern})\s*\n(.*?)(?=\n##|\Z)",
            re.IGNORECASE | re.DOTALL
        )
        match = pattern.search(inhalt)
        if match:
            return match.group(2).strip()
        return None

    def _parse_readme(self, inhalt: str):
        """Parst den Inhalt einer README-Datei."""
        if self.info["projekt_uebersicht"]["titel"] == self.INFO_NICHT_GEFUNDEN:
            title_match = re.search(r"^\s*#\s*(.*)", inhalt)
            if title_match:
                self.info["projekt_uebersicht"]["titel"] = title_match.group(1).strip()

        # Beschreibung (Fallback)
        # Nimmt den Text nach dem Titel bis zur nächsten Überschrift
        if self.info["projekt_uebersicht"]["beschreibung"] == self.INFO_NICHT_GEFUNDEN:
            desc_match = re.search(r"^\s*#\s*.*\n+([^#\n].*)", inhalt, re.DOTALL)
            if desc_match:
                 self.info["projekt_uebersicht"]["beschreibung"] = desc_match.group(1).strip().split('\n\n')[0]


        # Key Features
        features = self._extrahiere_sektion_aus_markdown(inhalt, ["Features", "Key Features", "Merkmale"])
        if features:
            self.info["projekt_uebersicht"]["key_features"] = features
            
        # Tech Stack
        tech_stack = self._extrahiere_sektion_aus_markdown(inhalt, ["Tech Stack", "Technology", "Technologien"])
        if tech_stack:
            self.info["projekt_uebersicht"]["tech_stack"] = tech_stack
            
        # Status
        status = self._extrahiere_sektion_aus_markdown(inhalt, ["Status", "Current Status"])
        if status:
            self.info["projekt_uebersicht"]["aktueller_status"] = status

        # Setup-Anleitung
        setup = self._extrahiere_sektion_aus_markdown(inhalt, ["Installation", "Setup", "Getting Started"])
        if setup:
            self.info["installation"]["setup_anleitung"] = setup
            
        # Quick Start
        quick_start = self._extrahiere_sektion_aus_markdown(inhalt, ["Quick Start", "Schnellstart"])
        if quick_start:
            self.info["installation"]["quick_start_guide"] = quick_start

    def _parse_toml(self, inhalt: str):
        """Parst den Inhalt einer pyproject.toml-Datei."""
        if not tomllib:
            print("Warnung: 'tomli' ist nicht installiert. pyproject.toml kann nicht analysiert werden.")
            return
            
        try:
            data = tomllib.loads(inhalt)
            project_data = data.get("project", {})
            
            if "name" in project_data:
                self.info["projekt_uebersicht"]["titel"] = project_data["name"]
            if "description" in project_data:
                self.info["projekt_uebersicht"]["beschreibung"] = project_data["description"]
            if "dependencies" in project_data:
                # Überschreibt 'dependencies' immer, da toml als primäre Quelle gilt
                self.info["installation"]["dependencies"] = project_data["dependencies"]
        except tomllib.TOMLDecodeError as e:
            print(f"Warnung: Fehler beim Parsen der pyproject.toml: {e}")

    def _parse_requirements(self, inhalt: str):
        """Parst den Inhalt einer requirements.txt-Datei."""
        # Nur füllen, wenn noch keine Dependencies aus toml gefunden wurden
        if self.info["installation"]["dependencies"] == self.INFO_NICHT_GEFUNDEN:
            lines = inhalt.splitlines()
            dependencies = [
                line.strip() for line in lines 
                if line.strip() and not line.strip().startswith('#')
            ]
            if dependencies:
                self.info["installation"]["dependencies"] = dependencies

    def extrahiere_info(self, dateien: List[Any], repo_url: str) -> Dict[str, Any]:
        """
        Orchestriert die Extraktion von Informationen aus einer Liste von RepoFile-Objekten.
        
        Die Reihenfolge der Verarbeitung ist wichtig, um Prioritäten zu setzen:
        1. pyproject.toml (höchste Priorität für Metadaten)
        2. requirements.txt (Fallback für Dependencies)
        3. README (für beschreibende Texte und als Fallback)
        4. Titel wird am Ende basierend auf der URL überschrieben.
        """
        # 1. Relevante Dateien finden
        readme_datei = self._finde_datei(["readme.md", "readme.rst", "readme.txt", "readme"], dateien)
        toml_datei = self._finde_datei(["pyproject.toml"], dateien)
        req_datei = self._finde_datei(["requirements.txt"], dateien)

        # 2. Dateien parsen (mit Priorisierung)
        if toml_datei:
            self._parse_toml(toml_datei.content)

        if req_datei:
            self._parse_requirements(req_datei.content)
            
        if readme_datei:
            self._parse_readme(readme_datei.content)
            
        # 3. Finale Formatierung der Dependencies
        deps = self.info["installation"]["dependencies"]
        if isinstance(deps, list):
            if not deps:
                self.info["installation"]["dependencies"] = self.INFO_NICHT_GEFUNDEN
            else:
                self.info["installation"]["dependencies"] = "\n".join(f"- {dep}" for dep in deps)
        
        repo_name = os.path.basename(repo_url.removesuffix('.git'))
        self.info["projekt_uebersicht"]["titel"] = f"{repo_name} documentation"

        return self.info