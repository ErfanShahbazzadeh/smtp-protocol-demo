import socket
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading

class SMTPClientGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SMTP Client - Email Sender")
        self.root.geometry("700x650")
        self.root.resizable(True, True)
        
        # Color scheme
        self.bg_dark = "#1a1a1a"       # Soft black background
        self.bg_medium = "#2d2d2d"     # Slightly lighter black
        self.bg_input = "#3a3a3a"      # Input field background
        self.fg_white = "#e0e0e0"      # Soft white text
        self.fg_green = "#4ade80"      # Soft green accent
        self.fg_green_dark = "#22c55e" # Darker green for buttons
        self.fg_red = "#ef4444"        # Red for errors
        self.border_color = "#404040"  # Subtle border
        
        self.root.configure(bg=self.bg_dark)
        self.sock = None
        
        self.setup_ui()
    
    def setup_ui(self):
        # Style configuration
        style = ttk.Style()
        style.theme_use("clam")
        
        # Configure styles
        style.configure("TFrame", background=self.bg_dark)
        style.configure("TLabel", 
                       background=self.bg_dark, 
                       foreground=self.fg_white,
                       font=("Segoe UI", 10))
        style.configure("Title.TLabel", 
                       background=self.bg_dark, 
                       foreground=self.fg_green,
                       font=("Segoe UI", 16, "bold"))
        style.configure("Status.TLabel", 
                       background=self.bg_dark, 
                       foreground=self.fg_green,
                       font=("Segoe UI", 9))
        style.configure("TButton", 
                       background=self.fg_green_dark,
                       foreground=self.bg_dark,
                       font=("Segoe UI", 10, "bold"),
                       borderwidth=0,
                       padding=10)
        style.map("TButton",
                 background=[("active", self.fg_green)],
                 foreground=[("active", self.bg_dark)])
        
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="✉ SMTP Email Client", style="Title.TLabel")
        title_label.pack(pady=(0, 20))
        
        # Server settings frame
        server_frame = ttk.Frame(main_frame)
        server_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Server row
        ttk.Label(server_frame, text="Server:").pack(side=tk.LEFT, padx=(0, 5))
        self.server_entry = tk.Entry(server_frame, 
                                     bg=self.bg_input, 
                                     fg=self.fg_white,
                                     insertbackground=self.fg_green,
                                     relief=tk.FLAT,
                                     font=("Consolas", 10))
        self.server_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.server_entry.insert(0, "Your mail server (e.g., smtp.example.com)")
        
        ttk.Label(server_frame, text="Port:").pack(side=tk.LEFT, padx=(0, 5))
        self.port_entry = tk.Entry(server_frame, 
                                   bg=self.bg_input, 
                                   fg=self.fg_white,
                                   insertbackground=self.fg_green,
                                   relief=tk.FLAT,
                                   font=("Consolas", 10),
                                   width=6)
        self.port_entry.pack(side=tk.LEFT)
        self.port_entry.insert(0, "25")
        
        # Connect button
        self.connect_btn = tk.Button(server_frame,
                                     text="Connect",
                                     bg=self.fg_green_dark,
                                     fg=self.bg_dark,
                                     font=("Segoe UI", 10, "bold"),
                                     relief=tk.FLAT,
                                     padx=15,
                                     pady=5,
                                     cursor="hand2",
                                     command=self.connect_to_server)
        self.connect_btn.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Separator
        separator1 = tk.Frame(main_frame, height=1, bg=self.border_color)
        separator1.pack(fill=tk.X, pady=15)
        
        # Email details frame
        email_frame = ttk.Frame(main_frame)
        email_frame.pack(fill=tk.X, pady=(0, 10))
        
        # From field
        ttk.Label(email_frame, text="From:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.from_entry = tk.Entry(email_frame,
                                   bg=self.bg_input,
                                   fg=self.fg_white,
                                   insertbackground=self.fg_green,
                                   relief=tk.FLAT,
                                   font=("Consolas", 10))
        self.from_entry.grid(row=0, column=1, sticky=tk.EW, pady=5, padx=(10, 0))
        
        # To field
        ttk.Label(email_frame, text="To:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.to_entry = tk.Entry(email_frame,
                                 bg=self.bg_input,
                                 fg=self.fg_white,
                                 insertbackground=self.fg_green,
                                 relief=tk.FLAT,
                                 font=("Consolas", 10))
        self.to_entry.grid(row=1, column=1, sticky=tk.EW, pady=5, padx=(10, 0))
        
        # Subject field
        ttk.Label(email_frame, text="Subject:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.subject_entry = tk.Entry(email_frame,
                                      bg=self.bg_input,
                                      fg=self.fg_white,
                                      insertbackground=self.fg_green,
                                      relief=tk.FLAT,
                                      font=("Consolas", 10))
        self.subject_entry.grid(row=2, column=1, sticky=tk.EW, pady=5, padx=(10, 0))
        
        email_frame.columnconfigure(1, weight=1)
        
        # Message body
        ttk.Label(main_frame, text="Message Body:").pack(anchor=tk.W, pady=(10, 5))
        self.body_text = scrolledtext.ScrolledText(main_frame,
                                                   height=10,
                                                   bg=self.bg_input,
                                                   fg=self.fg_white,
                                                   insertbackground=self.fg_green,
                                                   relief=tk.FLAT,
                                                   font=("Consolas", 10),
                                                   wrap=tk.WORD)
        self.body_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Send button
        self.send_btn = tk.Button(main_frame,
                                  text="Send Email",
                                  bg=self.fg_green_dark,
                                  fg=self.bg_dark,
                                  font=("Segoe UI", 11, "bold"),
                                  relief=tk.FLAT,
                                  padx=20,
                                  pady=8,
                                  cursor="hand2",
                                  state=tk.DISABLED,
                                  command=self.send_email)
        self.send_btn.pack(pady=(0, 10))
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="Not connected", style="Status.TLabel")
        self.status_label.pack()
        
        # Log output
        ttk.Label(main_frame, text="Connection Log:").pack(anchor=tk.W, pady=(10, 5))
        self.log_text = scrolledtext.ScrolledText(main_frame,
                                                  height=6,
                                                  bg=self.bg_medium,
                                                  fg=self.fg_green,
                                                  relief=tk.FLAT,
                                                  font=("Consolas", 9),
                                                  state=tk.DISABLED,
                                                  wrap=tk.WORD)
        self.log_text.pack(fill=tk.X, pady=(0, 5))
    
    def log(self, message, error=False):
        """Add message to log"""
        self.log_text.configure(state=tk.NORMAL)
        if error:
            self.log_text.insert(tk.END, f"[ERROR] {message}\n", "error")
        else:
            self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.log_text.configure(state=tk.DISABLED)
        
        # Configure error tag color
        self.log_text.tag_config("error", foreground=self.fg_red)
    
    def update_status(self, message, is_error=False):
        """Update status label"""
        self.status_label.configure(text=message)
        if is_error:
            self.status_label.configure(foreground=self.fg_red)
        else:
            self.status_label.configure(foreground=self.fg_green)
    
    def connect_to_server(self):
        """Connect to SMTP server in a separate thread"""
        server = self.server_entry.get().strip()
        port = int(self.port_entry.get().strip())
        
        self.connect_btn.configure(state=tk.DISABLED, text="Connecting...")
        self.update_status("Connecting...")
        
        def connect():
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.settimeout(10)
                self.sock.connect((server, port))
                
                response = self.sock.recv(1024).decode().strip()
                self.root.after(0, self.log, f"Server: {response}")
                
                if response.startswith("220"):
                    self.sock.send(b"EHLO test\r\n")
                    ehlo = self.sock.recv(1024).decode().strip()
                    self.root.after(0, self.log, f"EHLO: {ehlo[:100]}...")
                    
                    self.root.after(0, self.on_connected)
                else:
                    self.root.after(0, self.on_connection_failed, f"Unexpected response: {response}")
                    
            except Exception as e:
                self.root.after(0, self.on_connection_failed, str(e))
        
        threading.Thread(target=connect, daemon=True).start()
    
    def on_connected(self):
        """Called when connection is successful"""
        self.connect_btn.configure(state=tk.DISABLED, text="Connected.", bg=self.fg_green)
        self.send_btn.configure(state=tk.NORMAL)
        self.update_status("Connected to server")
        self.log("Successfully connected and authenticated!")
    
    def on_connection_failed(self, error_msg):
        """Called when connection fails"""
        self.connect_btn.configure(state=tk.NORMAL, text="Connect", bg=self.fg_green_dark)
        self.send_btn.configure(state=tk.DISABLED)
        self.update_status(f"Connection failed: {error_msg}", True)
        self.log(f"Connection failed: {error_msg}", True)
        self.sock = None
    
    def send_email(self):
        """Send email in a separate thread"""
        if not self.sock:
            messagebox.showerror("Error", "Not connected to server")
            return
        
        from_addr = self.from_entry.get().strip()
        to_addr = self.to_entry.get().strip()
        subject = self.subject_entry.get().strip()
        body = self.body_text.get("1.0", tk.END).strip()
        
        if not all([from_addr, to_addr, body]):
            messagebox.showwarning("Incomplete", "Please fill in all fields (From, To, and Message Body)")
            return
        
        self.send_btn.configure(state=tk.DISABLED, text="Sending...")
        self.update_status("Sending email...")
        
        # Build email with headers
        email_content = f"From: {from_addr}\r\n"
        email_content += f"To: {to_addr}\r\n"
        email_content += f"Subject: {subject}\r\n"
        email_content += "\r\n"  # Blank line between headers and body
        email_content += body
        email_content += "\r\n.\r\n"
        
        def send():
            try:
                # MAIL FROM
                self.sock.send(f"MAIL FROM: <{from_addr}>\r\n".encode())
                response = self.sock.recv(1024).decode().strip()
                self.root.after(0, self.log, f"MAIL FROM: {response}")
                
                if not response.startswith("250"):
                    self.root.after(0, self.on_send_failed, f"MAIL FROM failed: {response}")
                    return
                
                # RCPT TO
                self.sock.send(f"RCPT TO: <{to_addr}>\r\n".encode())
                response = self.sock.recv(1024).decode().strip()
                self.root.after(0, self.log, f"RCPT TO: {response}")
                
                if not response.startswith("250"):
                    self.root.after(0, self.on_send_failed, f"RCPT TO failed: {response}")
                    return
                
                # DATA
                self.sock.send(b"DATA\r\n")
                response = self.sock.recv(1024).decode().strip()
                self.root.after(0, self.log, f"DATA: {response}")
                
                if not response.startswith("354"):
                    self.root.after(0, self.on_send_failed, f"DATA failed: {response}")
                    return
                
                # Send email content
                self.sock.send(email_content.encode())
                response = self.sock.recv(1024).decode().strip()
                self.root.after(0, self.log, f"Send: {response}")
                
                if response.startswith("250"):
                    self.root.after(0, self.on_send_success)
                else:
                    self.root.after(0, self.on_send_failed, f"Send failed: {response}")
                
                # QUIT
                self.sock.send(b"QUIT\r\n")
                quit_response = self.sock.recv(1024).decode().strip()
                self.root.after(0, self.log, f"QUIT: {quit_response}")
                self.sock.close()
                self.sock = None
                
            except Exception as e:
                self.root.after(0, self.on_send_failed, str(e))
        
        threading.Thread(target=send, daemon=True).start()
    
    def on_send_success(self):
        """Called when email is sent successfully"""
        self.send_btn.configure(state=tk.DISABLED, text="Sent.", bg=self.fg_green)
        self.connect_btn.configure(state=tk.NORMAL, text="Connect", bg=self.fg_green_dark)
        self.update_status("Email sent successfully!")
        self.log("Email sent successfully!")
        messagebox.showinfo("Success", "Email sent successfully!")
    
    def on_send_failed(self, error_msg):
        """Called when sending fails"""
        self.send_btn.configure(state=tk.NORMAL, text="Send Email", bg=self.fg_green_dark)
        self.update_status(f"Sending failed: {error_msg}", True)
        self.log(f"Sending failed: {error_msg}", True)
        messagebox.showerror("Error", f"Failed to send email:\n{error_msg}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SMTPClientGUI(root)
    root.mainloop()