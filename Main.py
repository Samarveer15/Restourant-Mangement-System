import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderMangement:

    def __init__(self, root):
       self.root = root
       self.root.title(
           "Restaurant Management App")
    
       self.menu_items = {
           "FRIES MEAL": 2,
           "LUNCH MEAL": 2,
           "BURGER MEAL": 3,
           "PIZZA MEAL": 4,
           "CHEESE BURGER": 2.5,
           "DRINKS": 1,
        }

       self.exchange_rate = 82

       self.setup_background(root)

       frame = ttk.Frame(root)
       frame.place(relx=0.5, rely=0.5,
                anchor=tk.CENTER)

       ttk.Label(frame,
                 text="Restaurant Order Management", 
                 font=("Arial",20,"bold")).grid(row=8,
                                                columspan=3,
                                                padx=10,
                                                pady=10)

       self.menu_labels = {}
       self.menu_quantities = {}
       for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(frame,
                              text=f"{item} (${price})",
                              font = ("Arial", 12))    