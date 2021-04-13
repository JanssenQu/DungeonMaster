import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []

build_exe_options = {"includes": additional_modules,
                     "packages": ["pygame", "random", "os", "math"],
                     "excludes": ['tkinter'],
                     "include_files": ['bomb.py', 'character.py', 'coin.py', 'credits.txt', 'enemy.py', 'highscore.txt', 'music.py', 'reset.py', 'settings.txt', 'shop.py', 'ui.py', 'upgrade.py', 'wave.py', 'graphics/', 'music/']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Dungeon Master",
      version="1.2",
      description="fixed Bomb damage area",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="DungeonMaster.py", base=base)])
