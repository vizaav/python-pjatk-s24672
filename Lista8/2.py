import os
import platform


class FolderManager:
    def __init__(self):
        self.system = platform.system()

    def utworz_folder(self, sciezka):
        try:
            os.makedirs(sciezka, exist_ok=True)
            print(f"Utworzono folder: {sciezka}")
        except OSError:
            print(f"Wystąpił błąd podczas tworzenia folderu: {sciezka}")

    def usun_folder(self, sciezka):
        try:
            os.rmdir(sciezka)
            print(f"Usunięto folder: {sciezka}")
        except OSError:
            print(f"Wystąpił błąd podczas usuwania folderu: {sciezka}")

    def wyswietl_strukture(self, sciezka):
        print("Struktura folderów:")
        for folder, podfoldery, pliki in os.walk(sciezka):
            poziom = folder.replace(sciezka, '').count(os.sep)
            indent = ' ' * 4 * poziom
            print(f"{indent}{os.path.basename(folder)}/")
            for plik in pliki:
                print(f"{indent}    {plik}")


# Tworzenie instancji FolderManager
folder_manager = FolderManager()

# Przykład użycia
if folder_manager.system == "Windows":
    sciezka_glowna = "C:\\MojeFoldery"
else:
    sciezka_glowna = "/home/user/MojeFoldery"

# Utworzenie struktury folderów
folder_manager.utworz_folder(sciezka_glowna)
folder_manager.utworz_folder(os.path.join(sciezka_glowna, "Folder1"))
folder_manager.utworz_folder(os.path.join(sciezka_glowna, "Folder1", "Podfolder1"))
folder_manager.utworz_folder(os.path.join(sciezka_glowna, "Folder2"))
folder_manager.utworz_folder(os.path.join(sciezka_glowna, "Folder2", "Podfolder2"))

# Wyświetlenie struktury folderów
folder_manager.wyswietl_strukture(sciezka_glowna)

# Usunięcie folderów
folder_manager.usun_folder(os.path.join(sciezka_glowna, "Folder1", "Podfolder1"))
folder_manager.usun_folder(os.path.join(sciezka_glowna, "Folder1"))
folder_manager.usun_folder(os.path.join(sciezka_glowna, "Folder2", "Podfolder2"))
folder_manager.usun_folder(os.path.join(sciezka_glowna, "Folder2"))
folder_manager.usun_folder(sciezka_glowna)
