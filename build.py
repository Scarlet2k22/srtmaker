import os
import platform
import subprocess
import sys

def build_windows():
    print("Building for Windows...")
    subprocess.run(["pyinstaller", "--onefile", "--windowed", "--add-data", "icon.ico;.", "--icon=icon.ico", "--name=SRTMaker", "srtmaker.py"], check=True)
    print("Windows build completed. SRTMaker.exe is in the dist directory.")

def build_mac():
    print("Building for Mac...")
    subprocess.run(["pyinstaller", "--windowed", "--onefile", "--add-data", "icon.ico:.", "--icon=icon.ico", "--name=SRTMaker", "srtmaker.py"], check=True)
    os.rename("dist/SRTMaker.app", "SRTMaker.app")
    print("Mac build completed. SRTMaker.app is in the current directory.")

def build_linux():
    print("Building for Linux...")
    subprocess.run(["pyinstaller", "--onefile", "--add-data", "icon.ico:.", "--name=SRTMaker", "srtmaker.py"], check=True)
    print("Linux build completed. SRTMaker is in the dist directory.")

def main():
    # Remove old build and dist directories
    for dir in ['build', 'dist']:
        if os.path.exists(dir):
            for root, dirs, files in os.walk(dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(dir)

    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = platform.system()

    if target == "Windows":
        build_windows()
    elif target == "Darwin":  # macOS
        build_mac()
    elif target == "Linux":
        build_linux()
    else:
        print(f"Unsupported target: {target}")

if __name__ == "__main__":
    main()
