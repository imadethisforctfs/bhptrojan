import os

def run(**args):
    print("[*] In deirlister module.")
    files = os.listdir(".")
    return str(files)
    