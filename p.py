import tkinter as tk
from tkinter import ttk
from textblob import TextBlob

# Function to analyze sentiment of the given message
def get_sentiment(message):
    """
    Function to analyze sentiment of the given message.
    Returns 'positive', 'neutral', or 'negative'.
    """
    blob = TextBlob(message)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        return "Positive"
    elif sentiment == 0:
        return "Neutral"
    else:
        return "Negative"

# Function to analyze the sentiment of the input message and display the result
def analyze_sentiment():
    """
    Function to analyze the sentiment of the input message
    and display the result in a label.
    """
    message = input_text.get("1.0", tk.END).strip()

    if not message:
        sentiment_label.config(text="Please enter a message", fg="red")
        return

    sentiment = get_sentiment(message)
    result_text = f"Sentiment: {sentiment}"
    
    sentiment_label.config(text=result_text, fg="dark blue")

# Create main window
root = tk.Tk()
root.title("Sentiment Analysis App")

# Customize the main window
root.geometry("600x400")  # Set the size of the window
root.configure(bg="violet")  # Set background color to lavender

# Create heading label
heading_label = tk.Label(root, text="SENTIMENT ANALYZER", font=("Segoe UI", 24, "bold"), fg="black", bg="violet")
heading_label.pack(pady=20)

# Create input text box
input_text = tk.Text(root, height=10, width=50, font=("Arial", 16), bg="white", fg="#333333")  # Set font and colors
input_text.pack(padx=20, pady=20)

# Create analyze button
analyze_button = ttk.Button(root, text="Analyze Sentiment", command=analyze_sentiment, style="TButton")
analyze_button.pack()

# Add some padding to the button
analyze_button.pack(pady=(0, 20))

# Create label to display sentiment result
sentiment_label = tk.Label(root, text="", font=("Arial", 21), bg="violet")
sentiment_label.pack()

# Run the Tkinter event loop
root.mainloop()
