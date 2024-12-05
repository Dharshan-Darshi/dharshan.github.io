import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class HotelManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1024x768")  # Adjust for a desktop-sized window
        self.root.configure(bg="#e8f4f8")  # Light blue background

        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Hotel Management System", font=("Arial", 24, "bold"), bg="#003333", fg="white")
        title.pack(side="top", fill="x")

        # Customer Info Frame
        frame_customer = tk.Frame(self.root, bd=3, relief="groove", bg="#e8f9f9")
        frame_customer.place(x=10, y=50, width=500, height=350)

        tk.Label(frame_customer, text="Customer Details", font=("Arial", 16, "bold"), bg="#003333", fg="white").grid(row=0, columnspan=2, pady=10, sticky="w")

        tk.Label(frame_customer, text="Name:", bg="#e8f9f9", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_name = tk.Entry(frame_customer, font=("Arial", 12))
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame_customer, text="Phone Number:", bg="#e8f9f9", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_phone = tk.Entry(frame_customer, font=("Arial", 12))
        self.entry_phone.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame_customer, text="Email:", bg="#e8f9f9", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_email = tk.Entry(frame_customer, font=("Arial", 12))
        self.entry_email.grid(row=3, column=1, padx=10, pady=5)

        # Room Preferences Frame
        frame_room = tk.Frame(self.root, bd=3, relief="groove", bg="#e8f9f9")
        frame_room.place(x=10, y=420, width=500, height=300)

        tk.Label(frame_room, text="Room Preferences", font=("Arial", 16, "bold"), bg="#003333", fg="white").grid(row=0, columnspan=2, pady=10, sticky="w")

        tk.Label(frame_room, text="Number of Guests:", bg="#e8f9f9", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.combo_guests = ttk.Combobox(frame_room, font=("Arial", 12), state="readonly", width=17)
        self.combo_guests['values'] = ("1 Person", "2 Persons", "Family")
        self.combo_guests.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame_room, text="Room Type:", bg="#e8f9f9", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.combo_room = ttk.Combobox(frame_room, font=("Arial", 12), state="readonly", width=17)
        self.combo_room['values'] = ("AC", "Non-AC")
        self.combo_room.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame_room, text="Check-In Date (YYYY-MM-DD):", bg="#e8f9f9", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_checkin = tk.Entry(frame_room, font=("Arial", 12))
        self.entry_checkin.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(frame_room, text="Check-Out Date (YYYY-MM-DD):", bg="#e8f9f9", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entry_checkout = tk.Entry(frame_room, font=("Arial", 12))
        self.entry_checkout.grid(row=4, column=1, padx=10, pady=5)

        # Buttons
        button_frame = tk.Frame(self.root, bd=2, relief="groove", bg="#e8f4f8")
        button_frame.place(x=10, y=730, width=500, height=50)

        tk.Button(button_frame, text="Submit", font=("Arial", 14, "bold"), bg="#00796b", fg="white", command=self.submit).pack(side="left", padx=10, pady=5)
        tk.Button(button_frame, text="Clear All", font=("Arial", 14, "bold"), bg="#d32f2f", fg="white", command=self.clear_all).pack(side="right", padx=10, pady=5)

        # Data Display Frame
        frame_display = tk.Frame(self.root, bd=3, relief="groove", bg="#ffffff")
        frame_display.place(x=520, y=50, width=490, height=730)

        tk.Label(frame_display, text="Submitted Bookings", font=("Arial", 16, "bold"), bg="#003333", fg="white").pack(side="top", fill="x")

        self.text_display = tk.Text(frame_display, font=("Arial", 12), bg="#f8f9fa", fg="#333333")
        self.text_display.pack(fill="both", expand=True)

    def validate_input(self):
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()
        email = self.entry_email.get().strip()
        guests = self.combo_guests.get()
        room = self.combo_room.get()
        checkin = self.entry_checkin.get().strip()
        checkout = self.entry_checkout.get().strip()

        if not name or not phone or not email or not guests or not room or not checkin or not checkout:
            return "All fields must be filled!"

        if not phone.isdigit() or len(phone) < 10:
            return "Invalid phone number!"

        if "@" not in email or "." not in email:
            return "Invalid email address!"

        try:
            checkin_date = datetime.strptime(checkin, "%Y-%m-%d")
            checkout_date = datetime.strptime(checkout, "%Y-%m-%d")
            if checkin_date >= checkout_date:
                return "Check-out date must be later than check-in date!"
        except ValueError:
            return "Dates must be in YYYY-MM-DD format!"

        return None

    def submit(self):
        error = self.validate_input()
        if error:
            messagebox.showerror("Validation Error", error)
            return

        data = (
            f"Name: {self.entry_name.get()}\n"
            f"Phone: {self.entry_phone.get()}\n"
            f"Email: {self.entry_email.get()}\n"
            f"Guests: {self.combo_guests.get()}\n"
            f"Room Type: {self.combo_room.get()}\n"
            f"Check-In: {self.entry_checkin.get()}\n"
            f"Check-Out: {self.entry_checkout.get()}\n"
            "-" * 50 + "\n"
        )
        self.text_display.insert("end", data)
        messagebox.showinfo("Success", "Booking submitted successfully!")
        self.clear_entries()

    def clear_entries(self):
        self.entry_name.delete(0, "end")
        self.entry_phone.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.combo_guests.set("")
        self.combo_room.set("")
        self.entry_checkin.delete(0, "end")
        self.entry_checkout.delete(0, "end")

    def clear_all(self):
        self.text_display.delete("1.0", "end")
        self.clear_entries()


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementApp(root)
    root.mainloop()
