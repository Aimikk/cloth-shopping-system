from project.tools.logger import *
from project.view.component import *
from project.da.cloth_da import *
from project.entity.cloth import *
from tkinter import ttk, Tk, Label, Entry, Button, messagebox

# Main class
class Cloth_Shop(Tk):
    def __init__(self):
        super().__init__()
        self.title("Cloth Shop Management System")
        self.geometry("800x600")

        # Database connection
        self.db_connection = create_connection()
        if not self.db_connection:
            self.destroy()
            return

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        # Add Cloth Tab
        self.add_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.add_tab, text="Add Cloth")

        Label(self.add_tab, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = Entry(self.add_tab)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(self.add_tab, text="Size:").grid(row=1, column=0, padx=10, pady=5)
        self.size_entry = Entry(self.add_tab)
        self.size_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(self.add_tab, text="Price:").grid(row=2, column=0, padx=10, pady=5)
        self.price_entry = Entry(self.add_tab)
        self.price_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(self.add_tab, text="Quantity:").grid(row=3, column=0, padx=10, pady=5)
        self.quantity_entry = Entry(self.add_tab)
        self.quantity_entry.grid(row=3, column=1, padx=10, pady=5)

        Button(self.add_tab, text="Add Cloth", command=self.on_add_cloth).grid(row=4, columnspan=2, pady=10)

        # Show Cart Tab
        self.cart_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.cart_tab, text="Show Cart")
        self.cart_text = Text(self.cart_tab, height=15, width=70)
        self.cart_text.pack(side="left", fill="y")
        cart_scrollbar = ttk.Scrollbar(self.cart_tab, command=self.cart_text.yview)
        cart_scrollbar.pack(side="right", fill="y")
        self.cart_text['yscrollcommand'] = cart_scrollbar.set
        Button(self.cart_tab, text="Refresh Cart", command=self.on_show_cart).pack(pady=10)

        self.cart = []

        # Calculate Total Price Tab
        self.total_price_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.total_price_tab, text="Total Price")
        Button(self.total_price_tab, text="Total Price", command=self.calculate_total_price).pack(pady=10)

        # View Cloths Tab
        self.view_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.view_tab, text="View Cloths")
        self.cloths_text = Text(self.view_tab, height=15, width=70)
        self.cloths_text.pack(side="left", fill="y")
        scrollbar = ttk.Scrollbar(self.view_tab, command=self.cloths_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.cloths_text['yscrollcommand'] = scrollbar.set
        Button(self.view_tab, text="Refresh List", command=self.on_view_cloths).pack(pady=10)

        # Buy Cloth Tab
        self.buy_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.buy_tab, text="Buy Cloth")
        Label(self.buy_tab, text="Cloth ID:").grid(row=0, column=0, padx=10, pady=5)
        self.buy_id_entry = Entry(self.buy_tab)
        self.buy_id_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(self.buy_tab, text="Quantity:").grid(row=1, column=0, padx=10, pady=5)
        self.buy_quantity_entry = Entry(self.buy_tab)
        self.buy_quantity_entry.grid(row=1, column=1, padx=10, pady=5)

        Button(self.buy_tab, text="Buy Cloth", command=self.on_buy_cloth).grid(row=2, columnspan=2, pady=10)

        # Remove Cloth Tab
        self.remove_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.remove_tab, text="Remove Cloth")
        Label(self.remove_tab, text="Cloth ID:").grid(row=0, column=0, padx=10, pady=5)
        self.remove_id_entry = Entry(self.remove_tab)
        self.remove_id_entry.grid(row=0, column=1, padx=10, pady=5)

        Button(self.remove_tab, text="Remove Cloth", command=self.on_remove_cloth).grid(row=1, columnspan=2, pady=10)


    # Creat Total Price Calculator

    def calculate_total_price(self):
        total_price = 0
        for item in self.cart:
            cloth_id, quantity = item
            price = get_cloth_price(self.db_connection, cloth_id)
            total_price += price * quantity
        messagebox.showinfo("Total Price", f"The total price is: {total_price}")

    # Handling errors
    def on_add_cloth(self):
        name = self.name_entry.get()
        size = self.size_entry.get()
        logging.info("Data saved")
        try:
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Price and quantity must be numbers.")
            return
        add_cloth(self.db_connection, name, size, price, quantity)

    def on_view_cloths(self):
        view_cloths(self.db_connection, self.cloths_text)

    def on_buy_cloth(self):
        try:
            cloth_id = int(self.buy_id_entry.get())
            quantity = int(self.buy_quantity_entry.get())
            self.cart.append((cloth_id, quantity))
            messagebox.showinfo("Success", "Cloth added to cart!")
            logging.info("Data Bought")
        except ValueError:
            messagebox.showerror("Error", "Cloth ID and quantity must be integers.")
            return
        buy_cloth(self.db_connection, cloth_id, quantity)

    def on_show_cart(self):
        self.cart_text.delete(1.0, tk.END)
        for item in self.cart:
            self.cart_text.insert(tk.END, f"Cloth ID: {item[0]}, Quantity: {item[1]}\n")

    def on_remove_cloth(self):
        try:
            cloth_id = int(self.remove_id_entry.get())
            logging.info("Item removed")
        except ValueError:
            messagebox.showerror("Error", "Cloth ID must be an integer.")
            return
        remove_cloth(self.db_connection, cloth_id)



# Creat App (YOU CAN RUN FROM HERE):

if __name__ == "__main__":
    app = Cloth_Shop()
    app.mainloop()
