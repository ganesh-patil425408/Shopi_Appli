import tkinter as tk
from tkinter import ttk, messagebox


# PRODUCT DATA
products = {
    "Grocery": {
        "Rice": 60,
        "Wheat": 50,
        "Sugar": 45,
        "Oil": 120,
        "Milk": 30
    },

    "Electronics": {
        "Mobile": 12000,
        "Laptop": 55000,
        "Headphones": 1500,
        "Keyboard": 800,
        "Mouse": 500
    },

    "Clothing": {
        "T-Shirt": 500,
        "Jeans": 1200,
        "Shirt": 900,
        "Jacket": 2000,
        "Shoes": 1500
    }
}

# MAIN WINDOW
root = tk.Tk()

root.title("Shopi Application")
root.geometry("800x750")
root.config(bg="light blue")
root.resizable(False, False)

# VARIABLES

grand_total = 0

# TITLE

title = tk.Label(
    root,
    text="SHOPI APPLICATION",
    font=("Arial", 24, "bold"),
    bg="light blue",
    fg="dark blue"
)

title.pack(pady=10)

# PRODUCT SELECTION FRAME


selection_frame = tk.LabelFrame(
    root,
    text="Product Selection",
    font=("Arial", 13, "bold"),
    bg="white",
    fg="dark blue"
)

selection_frame.pack(
    padx=20,
    pady=5,
    fill="x"
)


# CATEGORY
tk.Label(
    selection_frame,
    text="Category:",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=7,
    sticky="w"
)


category_box = ttk.Combobox(
    selection_frame,
    values=list(products.keys()),
    state="readonly",
    width=25
)

category_box.grid(
    row=0,
    column=1,
    padx=10,
    pady=7
)

# PRODUCT

tk.Label(
    selection_frame,
    text="Product:",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=7,
    sticky="w"
)


product_box = ttk.Combobox(
    selection_frame,
    state="readonly",
    width=25
)

product_box.grid(
    row=1,
    column=1,
    padx=10,
    pady=7
)

# QUANTITY

tk.Label(
    selection_frame,
    text="Quantity:",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=7,
    sticky="w"
)


quantity_entry = tk.Entry(
    selection_frame,
    width=28
)

quantity_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=7
)


# PRICE
tk.Label(
    selection_frame,
    text="Price:",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(
    row=0,
    column=2,
    padx=10,
    pady=7
)


price_value = tk.Label(
    selection_frame,
    text="₹0",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="green"
)

price_value.grid(
    row=0,
    column=3,
    padx=10,
    pady=7
)

# PRODUCT TOTAL

tk.Label(
    selection_frame,
    text="Product Total:",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(
    row=1,
    column=2,
    padx=10,
    pady=7
)


product_total_value = tk.Label(
    selection_frame,
    text="₹0",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="blue"
)

product_total_value.grid(
    row=1,
    column=3,
    padx=10,
    pady=7
)

# CATEGORY FUNCTION

def change_category(event=None):

    category = category_box.get()

    if category:

        product_box["values"] = list(
            products[category].keys()
        )

        product_box.set("")

        price_value.config(text="₹0")

        product_total_value.config(
            text="₹0"
        )


category_box.bind(
    "<<ComboboxSelected>>",
    change_category
)

# PRODUCT PRICE FUNCTION

def show_price(event=None):

    category = category_box.get()
    product = product_box.get()

    if category and product:

        price = products[category][product]

        price_value.config(
            text=f"₹{price}"
        )

        product_total_value.config(
            text="₹0"
        )


product_box.bind(
    "<<ComboboxSelected>>",
    show_price
)

# CALCULATE PRODUCT PRICE


def calculate_price():

    category = category_box.get()
    product = product_box.get()
    quantity = quantity_entry.get()

    if category == "":
        messagebox.showwarning(
            "Warning",
            "Please select a category."
        )
        return

    if product == "":
        messagebox.showwarning(
            "Warning",
            "Please select a product."
        )
        return

    if quantity == "":
        messagebox.showwarning(
            "Warning",
            "Please enter quantity."
        )
        return

    if not quantity.isdigit():

        messagebox.showerror(
            "Error",
            "Quantity must contain numbers only."
        )

        return

    quantity = int(quantity)

    if quantity <= 0:

        messagebox.showerror(
            "Error",
            "Quantity must be greater than 0."
        )

        return

    price = products[category][product]

    total = price * quantity

    product_total_value.config(
        text=f"₹{total}"
    )

# BUTTON FRAME

button_frame = tk.Frame(
    root,
    bg="light blue"
)

button_frame.pack(
    pady=7
)
# CALCULATE PRICE BUTTON

calculate_button = tk.Button(
    button_frame,
    text="CALCULATE PRICE",
    font=("Arial", 10, "bold"),
    bg="orange",
    fg="black",
    width=18,
    height=2,
    command=calculate_price
)

calculate_button.grid(
    row=0,
    column=0,
    padx=8
)

# PURCHASE PRODUCT

def purchase_product():

    category = category_box.get()
    product = product_box.get()
    quantity = quantity_entry.get()

    if category == "":
        messagebox.showwarning(
            "Warning",
            "Please select a category."
        )
        return

    if product == "":
        messagebox.showwarning(
            "Warning",
            "Please select a product."
        )
        return

    if quantity == "":
        messagebox.showwarning(
            "Warning",
            "Please enter quantity."
        )
        return

    if not quantity.isdigit():

        messagebox.showerror(
            "Error",
            "Quantity must contain numbers only."
        )

        return

    quantity = int(quantity)

    if quantity <= 0:

        messagebox.showerror(
            "Error",
            "Quantity must be greater than 0."
        )

        return

    price = products[category][product]

    total = price * quantity

    bill_table.insert(
        "",
        "end",
        values=(
            product,
            quantity,
            f"₹{price}",
            f"₹{total}"
        )
    )

    # Clear input

    category_box.set("")
    product_box.set("")

    quantity_entry.delete(
        0,
        tk.END
    )

    price_value.config(
        text="₹0"
    )

    product_total_value.config(
        text="₹0"
    )


purchase_button = tk.Button(
    button_frame,
    text="PURCHASE PRODUCT",
    font=("Arial", 10, "bold"),
    bg="green",
    fg="white",
    width=20,
    height=2,
    command=purchase_product
)

purchase_button.grid(
    row=0,
    column=1,
    padx=8
)

# PURCHASED PRODUCTS

bill_frame = tk.LabelFrame(
    root,
    text="Purchased Products",
    font=("Arial", 13, "bold"),
    bg="white",
    fg="dark blue"
)

bill_frame.pack(
    padx=20,
    pady=5,
    fill="x"
)

# TABLE

columns = (
    "Product",
    "Quantity",
    "Price",
    "Total"
)


bill_table = ttk.Treeview(
    bill_frame,
    columns=columns,
    show="headings",
    height=6
)


bill_table.heading(
    "Product",
    text="Product"
)

bill_table.heading(
    "Quantity",
    text="Quantity"
)

bill_table.heading(
    "Price",
    text="Price"
)

bill_table.heading(
    "Total",
    text="Total"
)


bill_table.column(
    "Product",
    width=230
)

bill_table.column(
    "Quantity",
    width=130,
    anchor="center"
)

bill_table.column(
    "Price",
    width=150,
    anchor="center"
)

bill_table.column(
    "Total",
    width=150,
    anchor="center"
)


bill_table.pack(
    padx=5,
    pady=5
)

# CALCULATE ALL PRODUCTS

def calculate_all_price():

    global grand_total

    items = bill_table.get_children()

    if not items:

        messagebox.showwarning(
            "Warning",
            "Please purchase at least one product."
        )

        return

    grand_total = 0

    for item in items:

        values = bill_table.item(item)["values"]

        total = values[3]

        total = int(
            str(total).replace("₹", "")
        )

        grand_total += total

    grand_total_value.config(
        text=f"₹{grand_total}"
    )
# CALCULATE ALL PRICE BUTTON

calculate_all_button = tk.Button(
    root,
    text="CALCULATE ALL PRICE",
    font=("Arial", 11, "bold"),
    bg="purple",
    fg="white",
    width=25,
    height=2,
    command=calculate_all_price
)

calculate_all_button.pack(
    pady=7
)
# TOTAL BILL

total_frame = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="groove"
)

total_frame.pack(
    padx=20,
    pady=5,
    fill="x"
)


tk.Label(
    total_frame,
    text="TOTAL BILL:",
    font=("Arial", 16, "bold"),
    bg="white"
).pack(
    side="left",
    padx=20,
    pady=10
)


grand_total_value = tk.Label(
    total_frame,
    text="₹0",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="green"
)

grand_total_value.pack(
    side="right",
    padx=20,
    pady=10
)

# PREPARE BILL

def prepare_bill():

    if not bill_table.get_children():

        messagebox.showwarning(
            "Warning",
            "Please purchase products first."
        )

        return

    if grand_total == 0:

        calculate_all_price()

    bill_text = "SHOPI BILL\n"
    bill_text += "=" * 40 + "\n"

    for item in bill_table.get_children():

        values = bill_table.item(item)["values"]

        product = values[0]
        quantity = values[1]
        price = values[2]
        total = values[3]

        bill_text += (
            f"{product}  x{quantity}  "
            f"{price}  {total}\n"
        )

    bill_text += "=" * 40 + "\n"

    bill_text += f"TOTAL BILL: ₹{grand_total}"

    messagebox.showinfo(
        "FINAL BILL",
        bill_text
    )

    # Disable buttons after bill preparation

    calculate_button.config(
        state="disabled"
    )

    purchase_button.config(
        state="disabled"
    )

    calculate_all_button.config(
        state="disabled"
    )

    prepare_button.config(
        state="disabled"
    )

    category_box.config(
        state="disabled"
    )

    product_box.config(
        state="disabled"
    )

    quantity_entry.config(
        state="disabled"
    )

    # Show EXIT button

    exit_button.pack(
        pady=7
    )

# PREPARE BILL BUTTON
prepare_button = tk.Button(
    root,
    text="PREPARE BILL",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    width=25,
    height=2,
    command=prepare_bill
)

prepare_button.pack(
    pady=7
)

# EXIT BUTTON

def exit_application():

    root.destroy()


exit_button = tk.Button(
    root,
    text="EXIT",
    font=("Arial", 11, "bold"),
    bg="red",
    fg="white",
    width=15,
    height=2,
    command=exit_application
)

# EXIT is NOT displayed initially.

# START APPLICATION

root.mainloop()
