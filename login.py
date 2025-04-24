import tkinter as tk
from tkinter import messagebox

# Sample usernames and passwords
SAMPLE_USERNAMES = ["Abcde", "kymn12"]
SAMPLE_PASSWORDS = ["mySWUST", "helloSW"]

class TriangleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Triangle Checker")
        self.root.geometry("400x300")
        self.login_screen()

    def login_screen(self):
        """Create the login screen."""
        for widget in self.root.winfo_children():
            widget.destroy()  # Clear the window

        tk.Label(self.root, text="Login", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.check_login).pack(pady=10)

    def check_login(self):
        """Validate login credentials."""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username in SAMPLE_USERNAMES and password in SAMPLE_PASSWORDS:
            messagebox.showinfo("Login", "Login successful!")
            self.triangle_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    def triangle_screen(self):
        """Create the triangle checker screen."""
        for widget in self.root.winfo_children():
            widget.destroy()  # Clear the window

        tk.Label(self.root, text="Triangle Checker", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Enter three positive numbers:").pack()

        self.entry_a = tk.Entry(self.root)
        self.entry_a.pack()
        self.entry_b = tk.Entry(self.root)
        self.entry_b.pack()
        self.entry_c = tk.Entry(self.root)
        self.entry_c.pack()

        tk.Button(self.root, text="Check Triangle", command=self.check_triangle).pack(pady=10)

    def is_triangular(self, a, b, c):
        """Check if three numbers form a triangle."""
        return a + b > c and a + c > b and b + c > a

    def check_triangle(self):
        """Check the validity of triangle sides and restart on invalid input."""
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            c = float(self.entry_c.get())

            if a <= 0 or b <= 0 or c <= 0:
                messagebox.showerror("Invalid Input", "Numbers must be greater than zero.\nThe program will restart.")
                self.triangle_screen()  # Restart the triangle input screen
                return

            if self.is_triangular(a, b, c):
                messagebox.showinfo("Result", "The numbers form a valid triangle!")
            else:
                messagebox.showwarning("Result", "The numbers do NOT form a triangle.")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers.\nThe program will restart.")
            self.triangle_screen()  # Restart the triangle input screen

if __name__ == "__main__":
    root = tk.Tk()
    app = TriangleApp(root)
    root.mainloop()
