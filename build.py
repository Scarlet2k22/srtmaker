import os
import platform
import subprocess
import sys

def build_windows():
    print("Building for Windows...")
    cmd = ["pyinstaller", "--onefile", "--windowed", "--name=SRTMaker", "srtmaker.py"]
    if os.path.exists("icon.ico"):
        cmd.extend(["--add-data", "icon.ico;.", "--icon=icon.ico"])
    subprocess.run(cmd, check=True)
    print("Windows build completed. SRTMaker.exe is in the dist directory.")

def build_mac():
    print("Building for Mac...")
    cmd = ["pyinstaller", "--onefile", "--name=SRTMaker", "srtmaker.py"]
    subprocess.run(cmd, check=True)
    if os.path.exists("dist/SRTMaker"):
        os.rename("dist/SRTMaker", "SRTMaker")
        print("Mac build completed. SRTMaker is in the current directory.")
    else:
        print("Mac build completed, but the output file was not found in the expected location.")

def build_linux():
    print("Building for Linux...")
    cmd = ["pyinstaller", "--onefile", "--name=SRTMaker", "srtmaker.py"]
    subprocess.run(cmd, check=True)
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
