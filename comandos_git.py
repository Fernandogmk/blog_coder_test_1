class ComandosGit:
    def __init__(self):
        self.comandos = {
            "init": "git init",
            "clone": "git clone <url>",
            "add": "git add <archivo>",
            "commit": "git commit -m '<mensaje>'",
            "push": "git push <remoto> <rama>",
            "pull": "git pull <remoto> <rama>",
            "status": "git status",
            "log": "git log",
            "branch": "git branch",
            "checkout": "git checkout <rama>"
        }

    def mostrar_comandos(self):
        for nombre, comando in self.comandos.items():
            print(f"{nombre}: {comando}")

git = ComandosGit()
git.mostrar_comandos()


# Comandos para configurar nuestra identidad:
# git config --global user.name "nombre apellido"
# git config --global user.email "nombre@example.com"
# git init  Se usa una sola vez (crea capeta .git)

# Se usan cuando nosotros queramos:
# git status  Muestra el estado del repo (archivos modificados, no agregados, etc.)
# git log  Muestra el historial de commits
# Se repiten siempre que haya cambios:
# git add .  Agrega todos los archivos al repo
# git commit -m "mensaje"  Crea un commit con los archivos agregados (etiqueta de info)
# git push origin main  Sube los cambios al repositorio remoto (GitHub, GitLab, etc.)
# ramas:
# crear y movernos a rama nueva:
# git checkout -b "funciones-nuevas"
# movernos a rama existente:
# git checkout "main"
# ver ramas:
# git branch
# juntar ramas en main:
# git merge "funciones-nuevas"