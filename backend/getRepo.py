import tempfile
from git import Repo, GitCommandError
import logging
import os


class RepoFile:
    """
    Repräsentiert eine einzelne Datei in einem Git-Repository.
    
    Der Inhalt der Datei wird "lazy" geladen, d.h. erst bei tatsächlichem Zugriff.
    """
    def __init__(self, file_path, commit_tree):
        """
        Initialisiert das RepoFile-Objekt.

        Args:
            file_path (str): Der Pfad zur Datei innerhalb des Repositories.
            commit_tree (git.Tree): Das Tree-Objekt des Commits, aus dem die Datei stammt.
        """
        self.path = file_path
        self._tree = commit_tree
        

        self._blob = None
        self._content = None
        self._size = None

    @property
    def blob(self):
        """Lazy-lädt das Git-Blob-Objekt."""
        if self._blob is None:
            try:
                self._blob = self._tree[self.path]
            except KeyError:
                raise FileNotFoundError(f"Datei '{self.path}' konnte im Commit-Tree nicht gefunden werden.")
        return self._blob

    @property
    def content(self):
        """Lazy-lädt und gibt den dekodierten Inhalt der Datei zurück."""
        if self._content is None:
            self._content = self.blob.data_stream.read().decode('utf-8', errors='ignore')
        return self._content

    @property
    def size(self):
        """Lazy-lädt und gibt die Größe der Datei in Bytes zurück."""
        if self._size is None:
            self._size = self.blob.size
        return self._size
        
    def analyze_word_count(self):
        """
        Eine Beispiel-Analyse-Methode. Zählt die Wörter im Dateiinhalt.
        """
        return len(self.content.split())

    def __repr__(self):
        """Gibt eine nützliche String-Repräsentation des Objekts zurück."""
        return f"<RepoFile(path='{self.path}')>"
    
    def to_dict(self, include_content=False):
        data = {
            "path": self.path,
            "name": os.path.basename(self.path),
            "size": self.size,
            "type": "file"
        }
        if include_content:
            data["content"] = self.content
        return data





class GitRepository:
    """
    Verwaltet ein Git-Repository, einschließlich Klonen in ein temporäres
    Verzeichnis und Bereitstellung von RepoFile-Objekten.
    """
    def __init__(self, repo_url):
        self.repo_url = repo_url
        self.temp_dir = tempfile.mkdtemp()
        self.repo = None

        self.files = []
        
        try:
            logging.info(f"Clone Repository {self.repo_url}...")
            self.repo = Repo.clone_from(self.repo_url, self.temp_dir)
            self.latest_commit = self.repo.head.commit
            self.commit_tree = self.latest_commit.tree
            logging.info("Cloning successful.")
        except GitCommandError as e:
            self.close()
            raise RuntimeError(f"Error cloning repository: {e}") from e

    def get_all_files(self):
        """
        Gibt eine Liste aller Dateien im Repository als RepoFile-Objekte zurück.

        Returns:
            list[RepoFile]: Eine Liste von RepoFile-Instanzen.
        """
        file_paths = self.repo.git.ls_files().split('\n')
        self.files = [RepoFile(path, self.commit_tree) for path in file_paths if path]
        return self.files

    def close(self):
        """Löscht das temporäre Verzeichnis und dessen Inhalt."""
        if self.temp_dir:
            print(f"\nLösche temporäres Verzeichnis: {self.temp_dir}")
            self.temp_dir = None
            
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def get_file_tree(self, include_content=False):

        if not self.files:
            self.get_all_files()

        tree = {"name": "root", "type": "directory", "children": []}

        for file_obj in self.files:
            parts = file_obj.path.split('/')
            current_level = tree["children"]
            
            # Iteriere durch die Ordnerstruktur
            for part in parts[:-1]:
                # Suche, ob Ordner schon existiert
                found = next((item for item in current_level if item["name"] == part and item["type"] == "directory"), None)
                if not found:
                    new_dir = {"name": part, "type": "directory", "children": []}
                    current_level.append(new_dir)
                    current_level = new_dir["children"]
                else:
                    current_level = found["children"]
            
            # Datei am Ende hinzufügen
            current_level.append(file_obj.to_dict(include_content=include_content))

        return tree

