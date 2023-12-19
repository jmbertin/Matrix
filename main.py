import subprocess
import os

def main():
    """
    Main function to test all exercises
    """
    scripts = ["ex00.py", "ex01.py", "ex02.py", "ex03.py", "ex04.py", "ex05.py", "ex06.py", "ex07.py", "ex08.py", "ex09.py", "ex10.py", "ex11.py", "ex12.py", "ex13.py"]

    for script in scripts:
        print()
        input("Press key to launch '{}'...".format(script))
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Running '{}'...".format(script))
        print()
        subprocess.run(["python", script])

if __name__ == "__main__":
    main()
