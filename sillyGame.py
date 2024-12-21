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
    "Simma som en fisk!",
    "Hej Hallsberg!",
]

# List of fun colors for background
colors = ["blue", "red", "yellow", "green", "purple", "orange", "pink", "cyan"]

# Initialize score
score = 0


def change_button_text_and_move():
    """Change the button text, move it to a random position, and update the score."""
    global score
    # Change button text to a random string
    button.config(text=random.choice(strings))
    # Move the button to a random position
    button.place(relx=random.uniform(0.1, 0.9), rely=random.uniform(0.1, 0.9))
    # Change the background to a random color
    root.configure(bg=random.choice(colors))
    # Update the score
    score += 1
    score_label.config(text=f"Score: {score}")


# Create the main window
root = tk.Tk()
root.attributes("-fullscreen", True)  # Set fullscreen
root.configure(bg="blue")  # Initial background color

# Create a score label
score_label = tk.Label(
    root, text=f"Poäng: {score}", font=("Arial", 40), bg="blue", fg="white"
)
score_label.pack(pady=20)

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
    command=change_button_text_and_move,
)

# Place the button initially at the center
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Run the application
root.mainloop()
