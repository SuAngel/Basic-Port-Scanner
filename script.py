
import socket

def scan_ports(target_ip, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            sock.connect((target_ip, port))
            open_ports.append(port)
            print(f"Port {port} is open")
        except socket.error:
            pass
        finally:
            sock.close()

    return open_ports

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    open_ports = scan_ports(target_ip, start_port, end_port)

    if open_ports:
        print("Open ports: ", open_ports)
    else:
        print("No open ports found.")
