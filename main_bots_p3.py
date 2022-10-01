import subprocess

# Iterable con las rutas de los scripts
scripts_paths = ("./bots/youtube.py", "./bots/twitter.py", "./bots/tiktok.py", "./bots/google.py")

# Creamos cada proceso    
ps = [subprocess.Popen(["python3", script]) for script in scripts_paths]
exit_codes = [p.wait() for p in ps]


if not any(exit_codes):
    print("Todos los procesos terminaron con éxito")
else:
    print("Algunos procesos terminaron de forma inesperada.")