from html import generate_page
import shutil
import os

def main():
    print(r"""
 ____  _             _                _        ____  _ _          ____                           _             
|  _ \(_)_ __   __ _| |    ___   __ _(_) ___  / ___|(_) |_ ___   / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |_) | | '_ \ / _` | |   / _ \ / _` | |/ __| \___ \| | __/ _ \ | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
|  _ <| | | | | (_| | |__| (_) | (_| | | (__   ___) | | ||  __/ | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
|_| \_\_|_| |_|\__, |_____\___/ \__, |_|\___| |____/|_|\__\___|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
               |___/            |___/                                                                          
""")

    print("Creating any required folders")
    init()

    print("Deleting content of public site")
    clean()

    print("Copying content of ./static/ into ./public/")
    copy_static()

    print("Generate html pages from markdown in ./content/ and ./template.html")
    generate()

def init():
    os.makedirs("static", exist_ok=True)
    os.makedirs("public", exist_ok=True)
    os.makedirs("content", exist_ok=True)

def clean():
    shutil.rmtree("./public")
    os.mkdir("./public")

def copy_static():
    recurse_copy("./static/", "./public/")

def recurse_copy(source, destination):
    with os.scandir(source) as entries:
        for entry in entries:
            if entry.is_dir():
                os.mkdir(os.path.join(destination, entry.name))
                recurse_copy(os.path.join(source, entry.name), os.path.join(destination, entry.name))
            else:
                shutil.copy(os.path.join(source, entry.name), destination)
                print(">", os.path.join(destination, entry.name))

def generate():
    recurse_generate("./content/", "./public/")

def recurse_generate(source, destination):
    with os.scandir(source) as entries:
        for entry in entries:
            if entry.is_dir():
                os.mkdir(os.path.join(destination, entry.name))
                recurse_generate(os.path.join(source, entry.name), os.path.join(destination, entry.name))
            else:
                markdown_file = os.path.join(source, entry.name)
                html_file = os.path.join(destination, entry.name.replace(".md", ".html"))
                print(">", html_file)
                generate_page(markdown_file, "./template.html", html_file)

if __name__ == "__main__":
    main()
