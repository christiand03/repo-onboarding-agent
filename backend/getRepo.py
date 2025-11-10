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

    def get_file_tree(self):
        """
        Extrahiert die Verzeichnisstruktur (Tree View) des Repositories als
        verschachteltes Dictionary.
        
        Die Schlüssel sind Datei- oder Verzeichnisnamen.
        Die Werte für Dateien sind RepoFile-Objekte.
        Die Werte für Verzeichnisse sind weitere Dictionaries.

        Returns:
            dict: Eine verschachtelte Dictionary-Repräsentation der Dateistruktur.
        """
        if not self.commit_tree:
            return {}
        return self._traverse_tree(self.commit_tree, "")

    def _traverse_tree(self, tree, current_path):
        """
        Rekursive Hilfsfunktion, die ein git.Tree-Objekt durchläuft und
        eine Dictionary-Struktur aufbaut.

        Args:
            tree (git.Tree): Das aktuell zu durchlaufende Tree-Objekt.
            current_path (str): Der Pfad zum aktuellen Tree vom Repository-Root aus.

        Returns:
            dict: Die Dictionary-Struktur für den aktuellen Tree.
        """
        file_structure = {}
        
        # 1. Dateien (Blobs) auf der aktuellen Ebene verarbeiten
        for blob in tree.blobs:
            # Den vollständigen Pfad für das RepoFile-Objekt erstellen
            full_path = f"{current_path}/{blob.name}" if current_path else blob.name
            file_structure[blob.name] = RepoFile(full_path, self.commit_tree)

        # 2. Unterverzeichnisse (Trees) rekursiv verarbeiten
        for subtree in tree.trees:
            # Den Pfad für die nächste Rekursionsstufe erweitern
            full_path = f"{current_path}/{subtree.name}" if current_path else subtree.name
            # Rekursiver Aufruf für das Unterverzeichnis
            file_structure[subtree.name] = self._traverse_tree(subtree, full_path)
            
        return file_structure

