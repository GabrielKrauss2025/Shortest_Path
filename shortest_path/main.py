from pathlib import Path
import runpy

pasta = Path(__file__).resolve().parent

for nome in ["parte_1.py", "parte_2.py", "parte_3.py", "parte_6.py", "parte_7.py"]:
    print(f"\n--- {nome}---")
    runpy.run_path(str(pasta / nome), run_name="__main__")