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
    try:
        for i in range(100):  # You can change this value for speed of animation
            time.sleep(0.1)
            sys.stdout.write("\r" + text[i % len(text)])
            sys.stdout.flush()
    except KeyboardInterrupt:
        sys.stdout.write("\r" + " " * len(text) + "\r")
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

# Function to install OS
def install_os(script_url, script_name):
    try:
        os.system("pkg update -y && pkg install wget curl proot tar -y")
        os.system(f"wget {script_url} -O {script_name}")
        os.system(f"chmod +x {script_name}")
        os.system(f"bash {script_name}")
        print(Fore.GREEN + f"{script_name.split('-')[0].title()} installed successfully!")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

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
        install_os("https://offs.ec/2MceZWr", "install-nethunter-termux")
    elif choice == "2":
        install_os("https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu22/ubuntu22-xfce.sh", "ubuntu22-xfce.sh")
    elif choice == "3":
        install_os("https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-xfce.sh", "debian-xfce.sh")
    elif choice == "4":
        install_os("https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-xfce.sh", "arch-xfce.sh")
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

    # Start the animation
    animation()

if __name__ == "__main__":
    main()
            
