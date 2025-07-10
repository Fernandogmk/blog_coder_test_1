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