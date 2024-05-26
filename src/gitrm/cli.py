import typer
import os
import shutil
import git
from rich import print

app = typer.Typer()
root = f"{os.path.expanduser("~")}/.gitrm"

@app.callback()
def callback():
    """
    Manage and install git repositories with caching, and more all within your terminal
    Source Code: https://github.com/hyerland/git-rm
    """
    if not os.path.exists(f"{os.path.expanduser("~")}/.gitrm"):
        os.mkdir(f"{os.path.expanduser("~")}/.gitrm") #* 'Root' of the configuration directory
        os.mkdir(f"{os.path.expanduser("~")}/.gitrm/cache") #* Cache for cloned projects.

        #* Create a README for configuration directory
        with open(f"{root}/notice.txt", 'w') as readme:
            readme.write("Hey there!\nFor general use cases we don't recommend " 
                         "you messing with the `.gitrm` directory as "
                         "it may cause unexpected consequences.\nPlease refer "
                         "to the documentation when configuring here.")
    else:
        pass
    
@app.command()
def clone(url: str, branch: str = 'main', override: bool = False):
    """
    Grabs a git URL and clones the repository then caches for future usage.
    """
    formatted_url = url.replace("https://github.com/", "").replace('/', "-").replace('.git', "")
    directory = f"{root}/cache/{formatted_url}"

    if override:
            os.system('rmdir /S /Q "{}"'.format(directory))
    try:
        git.Repo.clone_from(url=url, to_path=directory, branch=branch)
    except git.GitCommandError:
        print("[red]Repository has already been cloned! Use the flag, [bold]`--override`[/bold] to do a fresh install.")

@app.command()
def load():
    """
    Load the portal gun
    """
    typer.echo("Loading portal gun")