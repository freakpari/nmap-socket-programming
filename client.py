import socket

#THIS FUNCTION CONNECTED TO THE SERVER.PY
def main():
    host = 'localhost'
    port = 8080

    try:
        while True:
            request = input('enter your request:')
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((host, port))
                client_socket.sendall(request.encode())
                response = client_socket.recv(1024).decode()
                
                if not response:
                    print("No response from server, closing connection.")
                    break
                
                print("Response from server:")
                print(response)


    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
