import tempfile
import shutil
from git import Repo, GitCommandError

# ==============================================================================
# Klasse 1: Das Datenobjekt, das eine einzelne Datei repräsentiert
# ==============================================================================
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
        
        # Attribute für Lazy Loading (werden erst bei Bedarf gefüllt)
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


# ==============================================================================
# Klasse 2: Der Manager für das gesamte Git-Repository
# ==============================================================================
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
            print(f"Klone Repository von {self.repo_url}...")
            self.repo = Repo.clone_from(self.repo_url, self.temp_dir)
            self.latest_commit = self.repo.head.commit
            self.commit_tree = self.latest_commit.tree
            print("Klonen erfolgreich.")
        except GitCommandError as e:
            self.close()
            raise RuntimeError(f"Fehler beim Klonen des Repositories: {e}") from e

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
            #shutil.rmtree(self.temp_dir)
            self.temp_dir = None
            
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


