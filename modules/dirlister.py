import os

def run(**args):
    print("[*] In dirlinster modules.")
    files = os.listdir(".")

    return str(files)
