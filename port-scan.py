import socket

def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)
                    print(f"\033[32mPort {port} is open\033[0m")
                else:
                    print(f"\033[91mPort {port} is closed\033[0m")
        except KeyboardInterrupt:
            print("\nScan aborted by user.")
            return open_ports
        except socket.gaierror:
            print("Hostname could not be resolved. Exiting.")
            return open_ports
        except socket.error:
            print("Couldn't connect to server.")
            return open_ports
    return open_ports

def main():
    print("\tPort scan by linux")
    host = input("Enter the target host/IP address: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    print(f"\nScanning ports {start_port} to {end_port} on {host}...\n")
    open_ports = scan_ports(host, start_port, end_port)

    if open_ports:
        print("\n\033[32mOpen ports:\033[0m")
        for port in open_ports:
            print(port)
    else:
        print("\n\033[91mNo open ports found\033[0m")

if __name__ == "__main__":
    main()