import tkinter as tk
from tkinter import ttk

# Function to handle the search button click
def search_cars():
    # Get the values from the search fields
    make = make_var.get()
    model = model_var.get()
    year = year_var.get()
    price_min = price_min_var.get()
    price_max = price_max_var.get()
    mileage_min = mileage_min_var.get()
    mileage_max = mileage_max_var.get()
    
    # Display the search criteria for now (mockup behavior)
    results_text.set(f"Search Results for:\nMake: {make}, Model: {model}, Year: {year}, Price: {price_min}-{price_max}, Mileage: {mileage_min}-{mileage_max}")

# Main application window
root = tk.Tk()
root.title("Car Information Hub")
root.geometry("800x600")

# Search Bar
search_frame = ttk.Frame(root)
search_frame.pack(pady=10)

search_label = ttk.Label(search_frame, text="Search for cars:")
search_label.pack(side=tk.LEFT, padx=5)

search_entry = ttk.Entry(search_frame, width=50)
search_entry.pack(side=tk.LEFT, padx=5)

search_button = ttk.Button(search_frame, text="Search", command=search_cars)
search_button.pack(side=tk.LEFT, padx=5)

# Advanced Search Options
advanced_frame = ttk.LabelFrame(root, text="Advanced Search Options")
advanced_frame.pack(padx=10, pady=10, fill="x")

# Make
make_label = ttk.Label(advanced_frame, text="Make:")
make_label.grid(row=0, column=0, padx=5, pady=5)
make_var = tk.StringVar()
make_entry = ttk.Entry(advanced_frame, textvariable=make_var)
make_entry.grid(row=0, column=1, padx=5, pady=5)

# Model
model_label = ttk.Label(advanced_frame, text="Model:")
model_label.grid(row=0, column=2, padx=5, pady=5)
model_var = tk.StringVar()
model_entry = ttk.Entry(advanced_frame, textvariable=model_var)
model_entry.grid(row=0, column=3, padx=5, pady=5)

# Year
year_label = ttk.Label(advanced_frame, text="Year:")
year_label.grid(row=1, column=0, padx=5, pady=5)
year_var = tk.StringVar()
year_entry = ttk.Entry(advanced_frame, textvariable=year_var)
year_entry.grid(row=1, column=1, padx=5, pady=5)

# Price Range
price_label = ttk.Label(advanced_frame, text="Price Range:")
price_label.grid(row=1, column=2, padx=5, pady=5)
price_min_var = tk.StringVar()
price_max_var = tk.StringVar()
price_min_entry = ttk.Entry(advanced_frame, textvariable=price_min_var, width=10)
price_max_entry = ttk.Entry(advanced_frame, textvariable=price_max_var, width=10)
price_min_entry.grid(row=1, column=3, padx=5, pady=5, sticky="w")
price_max_entry.grid(row=1, column=3, padx=5, pady=5, sticky="e")

# Mileage Range
mileage_label = ttk.Label(advanced_frame, text="Mileage Range:")
mileage_label.grid(row=2, column=0, padx=5, pady=5)
mileage_min_var = tk.StringVar()
mileage_max_var = tk.StringVar()
mileage_min_entry = ttk.Entry(advanced_frame, textvariable=mileage_min_var, width=10)
mileage_max_entry = ttk.Entry(advanced_frame, textvariable=mileage_max_var, width=10)
mileage_min_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
mileage_max_entry.grid(row=2, column=1, padx=5, pady=5, sticky="e")

# Search Results
results_frame = ttk.LabelFrame(root, text="Search Results")
results_frame.pack(padx=10, pady=10, fill="both", expand=True)

results_text = tk.StringVar()
results_label = ttk.Label(results_frame, textvariable=results_text, anchor="nw", justify="left")
results_label.pack(padx=10, pady=10, fill="both", expand=True)

# Run the application
root.mainloop()
