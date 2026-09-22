import subprocess

while True:
    print("")
    file = input("Drag APK file into the terminal and press enter ")

    try:
        subprocess.run(["adb", "install", file])
        print("")
        exit = input("Install another APK? (y/n) ")
        if exit == "n":
            break
    except subprocess.CalledProcessError as e:
        print("")
        print("Error code: ", e.stderr)
        print("")
        exit = input("Try Again? (y/n) ")
        if exit == "n":
            break