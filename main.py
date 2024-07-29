import os
import time
import sys
import subprocess
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

# Animation function
def animation():
    text = "|/-\\"
    for i in range(100):                                                                                                                                                                                                                                                                                          time.sleep(0.1)  # You can change this value for speed of animation
        sys.stdout.write("\r" + text[i % len(text)])
        sys.stdout.flush()

# Clear terminal function
def clear():
    os.system("clear" if os.name == "posix" else "cls")

# Credits animation function
def animated_credits():
    credit_text = [
        "Author  : LocalHost.07",
        "Program : Python",
        "",
        "Tool is for Installing Rootless OS for Your Android Device Easily.",
        "",
        "Made With Love [❤️]"
    ]
    for line in credit_text:
        for char in line:
            sys.stdout.write(Fore.MAGENTA + char)
            sys.stdout.flush()
            time.sleep(0.05)
        sys.stdout.write("\n")
        time.sleep(0.5)

# Main function
def main():
    clear()

    # ASCII banner
    banner = pyfiglet.figlet_format("LH Os-Installer", font="slant")
    print(Fore.WHITE + banner)
    print(Fore.RED + "Author : LocalHost.07")
    print()
    print(Fore.WHITE + "Please select your OS to Install (rootless):")
    print()

    options = [
        "1. Kali Linux",
        "2. Ubuntu",
        "3. Desbian",
        "4. ArcLinux",
        "5. Update",
        "6. Credits",
        "7. Exit"
    ]

    for option in options:
        print(Fore.CYAN + option)

    print()

    choice = input(Fore.WHITE + "Enter your choice : ")

    if choice == "1":
        os.system("pkg update -y && pkg install wget curl proot tar -y")
        os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
        os.system("chmod +x install-nethunter-termux")
        os.system("./install-nethunter-termux")
        print(Fore.GREEN + "Kali Linux installed successfully!")
    elif choice == "2":
        os.system("pkg update -y && pkg install wget curl proot tar -y")
        os.system("wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu22/ubuntu22-xfce.sh -O ubuntu22-xfce.sh")
        os.system("chmod +x ubuntu22-xfce.sh")
        os.system("bash ubuntu22-xfce.sh")
        print(Fore.GREEN + "Ubuntu installed successfully!")
    elif choice == "3":
        os.system("pkg update -y && pkg install wget curl proot tar -y")
        os.system("wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-xfce.sh -O debian-xfce.sh")
        os.system("chmod +x debian-xfce.sh")
        os.system("bash debian-xfce.sh")
        print(Fore.GREEN + "Desbian installed successfully!")
    elif choice == "4":
        os.system("pkg update -y && pkg install wget curl proot tar -y")
        os.system("wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-xfce.sh -O arch-xfce.sh")
        os.system("chmod +x arch-xfce.sh")
        os.system("bash arch-xfce.sh")
        print(Fore.GREEN + "ArcLinux installed successfully!")
    elif choice == "5":
        os.system("apt update -y")
        print(Fore.GREEN + "System updated successfully!")
    elif choice == "6":
        print()
        animated_credits()
    elif choice == "7":
        clear()
        sys.exit()
    else:
        print(Fore.RED + "Invalid choice!")
        main()

    animation()

if __name__ == "__main__":
    main()



