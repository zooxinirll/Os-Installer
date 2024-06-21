import os
import time
import sys
import subprocess
from colorama import Fore, Back, Style

# Animation function
def animation():
    text = "|/-\\"

    for i in range(100):
        time.sleep(0.1)  # You can change this value for speed of animation
        sys.stdout.write("\r" + text[i % len(text)])
        sys.stdout.flush()

# Clear terminal function
def clear():
    os.system("clear" if os.name == "posix" else "cls")

# Main function
def main():
    clear()

    print("**********************************")
    print("* Welcome to LH-07 Os Installer  *")
    print("*                                *")
    print("* Author : LocalHost.07          *")
    print("*                                *")
    print("**********************************")
    print(Fore.YELLOW+"Please select your OS to Install (rootless):")
    print()
    print(Fore.CYAN+"1. Kali Linux")
    print("2. Ubuntu")
    print("3. Desbian")
    print("4. ArcLinux")
    print("5. Update ")
    print("6. Credits")
    print()

    choice = input(Fore.WHITE+"Enter your choice (1/2/3/4/5): ")

    if __name__ == "__main__":
        if choice == "1":
            os.system("pkg update -y && pkg install wget curl proot tar -y ")
            os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
            os.system("chmod +x install-nethunter-termux")
            os.system("./install-nethunter-termux")
            print("Kali Linux installed successfully!")


        elif choice == "2":
            os.system("pkg update -y && pkg install wget curl proot tar -y")
            os.system("wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu22/ubuntu22-xfce.sh -O ubuntu22-xfce.sh")
            os.system("chmod +x ubuntu22-xfce.sh ")
            os.system("bash ubuntu22-xfce.sh")
            print("Ubuntu installed successfully!")


        elif choice == "3":
            os.system("pkg update -y && pkg install wget curl proot tar -y")
            os.system("wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-xfce.sh -O debian-xfce.sh ")
            os.system("chmod +x debian-xfce.sh ")
            os.system("bash debian-xfce.sh")
            print("Desbian installed successfully!")


        elif choice == "4":
            os.system("pkg update -y && pkg install wget curl proot tar -y ")
            os.system("wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-xfce.sh -O arch-xfce.sh")
            os.system("chmod +x arch-xfce.sh")
            os.system("bash arch-xfce.sh")
            print("ArcLinux installed successfully!")

        elif choice == "5":
            os.system("apt update -y")

        elif choice == "6":
            print()
            print("Author  : LocalHost.07 ")
            print("Program : Python")
            print()
            print("Tool is for Installing Rootless Os for Your Android Device Easily .")
            print()
            print("Made With Love [❤️]")

        else:
            print("Invalid choice!")
            main()

    animation()

if __name__ == "__main__":
    main()
