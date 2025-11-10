#pip install winshell
import winshell

try:
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)

    print("Recycle bin is emptied Now")
except:
    print("Recycle bin is already empty!")