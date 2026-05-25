import socket

def test_smtp_connection(server, port=25, timeout=10):
    """Test basic SMTP connectivity and display server response."""
    print(f"Attempting to connect to {server}:{port}...")
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((server, port))
        
        # Receive server greeting banner
        response = sock.recv(1024).decode().strip()
        print(f"{response}")
        
        if response.startswith("220"):
            # Send EHLO to see what the server supports
            sock.send(b"EHLO test\r\n")
            ehlo_response = sock.recv(1024).decode().strip()
            print(f"\nEHLO response:\n{ehlo_response}")
            
            # MAIL FROM
            S_email = input("MAIL FROM: ")
            sock.send(f"MAIL FROM: <{S_email}>\r\n".encode())
            S_email_response = sock.recv(1024).decode().strip()
            
            if S_email_response.startswith("250"):
                print(f"{S_email_response}")
                
                # RCPT TO
                R_email = input("RCPT TO: ")
                sock.send(f"RCPT TO: <{R_email}>\r\n".encode())
                R_email_response = sock.recv(1024).decode().strip()
                
                if R_email_response.startswith("250"):
                    print(f"{R_email_response}")
                    
                    # DATA command
                    sock.send(b"DATA\r\n")
                    D_Response = sock.recv(1024).decode().strip()
                    
                    if D_Response.startswith("354"):
                        print(f"{D_Response}")
                        print("Enter email content (headers + body).")
                        print("Type a single '.' on a new line when done:\n")
                        
                        # Build the email content
                        email_lines = []
                        
                        # Get user input line by line
                        while True:
                            line = input()
                            if line == ".":
                                break
                            email_lines.append(line)
                        
                        # Join all lines with CRLF and add the terminating sequence
                        email_content = "\r\n".join(email_lines) + "\r\n.\r\n"
                        
                        # Send the email content
                        sock.send(email_content.encode())
                        
                        # Get server response after sending email
                        send_response = sock.recv(1024).decode().strip()
                        print(f"\nServer response: {send_response}")
                        
                        if send_response.startswith("250"):
                            print("[✓] Email sent successfully!")
                        else:
                            print(f"[!] Unexpected response: {send_response}")
                    
                    else:
                        print(f"[!] DATA command failed: {D_Response}")
                
                else:
                    print(f"[!] RCPT TO failed: {R_email_response}")
            
            else:
                print(f"[!] MAIL FROM failed: {S_email_response}")
            
            # Always QUIT properly
            sock.send(b"QUIT\r\n")
            quit_response = sock.recv(1024).decode().strip()
            print(f"QUIT response: {quit_response}")
            sock.close()
        
        else:
            print(f"[!] Connected but unexpected response (not 220)")
        
    except socket.gaierror:
        print(f"[✗] DNS resolution failed — check the server name: {server}")
    except socket.timeout:
        print(f"[✗] Connection timed out — port {port} may be blocked")
    except ConnectionRefusedError:
        print(f"[✗] Connection refused — server not accepting on port {port}")
    except Exception as e:
        print(f"[✗] Connection failed: {e}")

test_smtp_connection("mail.uma.ac.ir")