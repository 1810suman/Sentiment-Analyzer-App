# Sentiment-Analyzer-App
Sentiment Analysis App using Python's tkinter library for the graphical interface and TextBlob for sentiment analysis. The app consists of a main window titled "Sentiment Analysis App" with a violet background. At the top, there's a bold heading labeled "SENTIMENT ANALYZER" to indicate the purpose of the application. Below the heading, a text box is provided for users to input their message, and an "Analyze Sentiment" button is available. When the button is clicked, the analyze_sentiment() function is triggered. This function retrieves the text from the input box, checks if it's empty, and displays an error message if necessary. Then, it calls the get_sentiment() function, which uses TextBlob to analyze the sentiment of the message. The sentiment result (Positive, Neutral, or Negative) is displayed in a label below the button. The app runs in a continuous loop (root.mainloop()) to handle user interactions, ensuring the application remains responsive until the user closes the window. Overall, the app provides a simple and intuitive interface for users to analyze the sentiment of their input text.







