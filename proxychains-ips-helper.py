def append_proxy_addresses(protocol, file_path):
    try:
        # Open the file containing IP addresses
        with open(file_path, 'r') as file:
            addresses = file.readlines()

            # Open proxychains.conf in append mode
            with open('/etc/proxychains.conf', 'a') as proxychains_conf:
                for address in addresses:
                    # Split IP address and port
                    ip, port = address.strip().split(':')
                    
                    # Write to proxychains.conf in the required format
                    proxychains_conf.write(f"{protocol} {ip} {port}\n")

        print("Proxy addresses appended successfully to proxychains.conf")
    except FileNotFoundError:
        print("File not found or cannot be opened.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Take inputs: protocol choice and file path
    protocol_choice = input("Enter the protocol choice (http/socks4/socks5): ").strip().lower()
    file_path = input("Enter the path to the text file containing IP addresses: ").strip()

    # Call function to append addresses to proxychains.conf
    append_proxy_addresses(protocol_choice, file_path)
