import tkinter as tk
import random

# Strings to display
strings = [
    "Lo är smart!",
    "Lo är stark!",
    "Var är mina julklappar?",
    "Mjau!",
    "Tokigt!",
    "Ge mig godis!",
    "Lo är en igelkott",
    "Nu är det jul!",
    "Dansa upp-och-ner!",
    "Låt som en dinosaurie!",
]


def change_button_text():
    """Change the button text to a random string."""
    button.config(text=random.choice(strings))


# Create the main window
root = tk.Tk()
root.attributes("-fullscreen", True)  # Set fullscreen
root.configure(bg="blue")  # Set background color

# Create a button
button = tk.Button(
    root,
    text="Tryck här!",
    font=("Arial", 60),
    bg="green",
    fg="white",
    activebackground="orange",  # Background color when pressed
    activeforeground="white",  # Text color when pressed
    relief="flat",  # Removes border-style change
    command=change_button_text,
)

# Center the button in the window
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Run the application
root.mainloop()
