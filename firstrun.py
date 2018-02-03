import subprocess
import tkinter
import tkinter.messagebox
from git import Repo


def prereq():
    reqPackage = ["nvidia-cuda-dev", "nvidia-cuda-toolkit", "libcurl4-openssl-dev", "libssl-dev", "libjansson-dev", "automake", "autotools-dev"]
    installPackages = []
    for package in reqPackage:
        result = subprocess.run(['dpkg-query', '-l', package], stdout=subprocess.PIPE)
        rc = result.returncode
        print(rc)
        if(rc == 1):
            installPackages.append(package)

    for installation in installPackages:
        subprocess.run(["sudo apt-get -y install", installation])

    Repo.clone_from("https://github.com/tpruvot/ccminer.git", "ccminer")
    subprocess.run("cd ccminer")
    subprocess.run("git checkout linux")
    subprocess.run("./build.sh")
