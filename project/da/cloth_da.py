import mysql.connector
import tkinter as tk
from tkinter import messagebox
def create_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="clothing_shop_db"
        )
    except mysql.connector.Error as e:
        messagebox.showerror("Database Connection Error", str(e))
        return None


def add_cloth(db_connection, name, size, price, quantity):
    cursor = db_connection.cursor()
    query = "INSERT INTO cloths (name, size, price, quantity) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, size, price, quantity))
    db_connection.commit()
    cursor.close()
    messagebox.showinfo("Success", "Cloth added successfully.")


# Function to display all cloths in the database
def view_cloths(db_connection, text_widget):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM cloths")
    rows = cursor.fetchall()
    cursor.close()

    text_widget.delete('1.0', tk.END)  # Clear the text widget first
    text_widget.insert(tk.END, "{:<5} {:<30} {:<10} {:<10} {:<10}\n".format('ID', 'Name', 'Size', 'Price', 'Quantity'))
    for row in rows:
        text_widget.insert(tk.END, "{:<5} {:<30} {:<10} {:<10} {:<10}\n".format(*row))


# Function to allow a user to buy a cloth
def buy_cloth(db_connection, cloth_id, quantity):
    cursor = db_connection.cursor()
    cursor.execute("SELECT quantity FROM cloths WHERE id = %s", (cloth_id,))
    result = cursor.fetchone()

    if result and result[0] >= quantity:
        new_quantity = result[0] - quantity
        update_query = "UPDATE cloths SET quantity = %s WHERE id = %s"
        cursor.execute(update_query, (new_quantity, cloth_id))
        db_connection.commit()
        messagebox.showinfo("Success", f"You bought {quantity} of cloth ID {cloth_id}.")
    else:
        messagebox.showerror("Error", "Not enough stock or cloth not found.")
    cursor.close()


# Function to remove a cloth from the database
def remove_cloth(db_connection, cloth_id):
    cursor = db_connection.cursor()
    query = "DELETE FROM cloths WHERE id = %s"
    cursor.execute(query, (cloth_id,))
    db_connection.commit()
    cursor.close()
    messagebox.showinfo("Success", "Cloth removed successfully.")

    # cloth_da.py
def get_cloth_by_id(connection, cloth_id):
        cursor = connection.cursor()
        query = "SELECT * FROM cloths WHERE id = %s"
        cursor.execute(query, (cloth_id,))
        result = cursor.fetchone()
        cursor.close()
        return result
# Function to get price of the clothes
def get_cloth_price(db_connection, cloth_id):
    cursor = db_connection.cursor()
    query = "SELECT price FROM cloths WHERE id = %s"
    cursor.execute(query, (cloth_id,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else 0
