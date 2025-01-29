import os
import time

def run_client():
    os.system("python client.py")
def run_host():
    os.system("python host.py")
def run_ports():
    os.system("python ports.py")
    

def main():
    while True:
        print("\nchoose what you want :")
        print("1. check the host is online or not ")
        print("2. check the ports and response time ")
        print("3. get or post method")
        print("0. exit")

        choice = input("enter your choice: ")

        if choice == "1":
            run_host()
        elif choice == "2":
            run_ports()
        elif choice == "3":
            run_client()
        elif choice == "0":
            print(" exit .")
            break
        else:
            print(" TRY AGAIN.")

if __name__ == "__main__":
    main()
