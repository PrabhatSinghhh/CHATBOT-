import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import random

# Dictionary of Q&A responses
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! What can I do for you?",
    "hey": "Hey! Need any assistance?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "i am fine": "Glad to hear that! How can I assist you today?",
    "fine": "That's good to know! What would you like to talk about?",
    "i am good": "That's great! How can I help you today?",
    "what's up": "Not much, just here to assist you! What about you?",
    "how can i help you": "You can ask me questions or seek assistance with various topics.",
    "help": "Sure! What do you need help with?",
    "what is your purpose": "My purpose is to assist you with information and answer your questions.",
    "who are you": "I am SmartBot, your virtual assistant created to help you with information.",
    "what is your function": "I can chat with you, answer questions, and provide information on various topics.",
    "what is your name": "I'm SmartBot, your virtual assistant.",
    "who created you": "I was created by Prabhat using Python.",
    "what can you do": "I can chat with you and answer basic questions.",
    "tell me a joke": lambda: random.choice([
        "Why do Python programmers wear glasses? Because they can't C!",
        "Why was the JavaScript developer sad? Because he didn't 'null' his feelings.",
        "Why did the computer get cold? Because it forgot to close Windows!"
    ]),
    "bye": "Goodbye! Have a nice day!",
    "thank you": "You're welcome!",
    "what is python": "Python is a high-level, interpreted programming language known for its readability.",
    "what is tkinter": "Tkinter is Python's standard GUI library.",
    "who is the prime minister of india": "Narendra Modi is the current Prime Minister of India.",
    "what is ai": "AI stands for Artificial Intelligence, a field that simulates human intelligence in machines.",
    "what is machine learning": "Machine Learning is a branch of AI that focuses on allowing machines to learn from data.",
    "tell me the time": lambda: f"Current time is {datetime.now().strftime('%H:%M:%S')}",
    "tell me the date": lambda: f"Today's date is {datetime.now().strftime('%Y-%m-%d')}",
    "how old are you": "I'm timeless! I exist only when you run me.",
    "can you help me": "Sure! Ask me anything related to general knowledge, programming, or tech.",
    "what is your purpose": "I'm here to make your life easier by answering your questions.",
    "open google": "I can't open sites directly, but you can visit https://www.google.com",
    "what is cloud computing": "Cloud computing is delivery of computing services over the internet.",
    "what is github": "GitHub is a platform for hosting and collaborating on code projects.",
    "what is html": "HTML stands for HyperText Markup Language, used to create web pages.",
    "what is css": "CSS stands for Cascading Style Sheets, used to style HTML content.",
    "what is javascript": "JavaScript is a programming language used to make web pages interactive.",
    "what is mysql": "MySQL is an open-source relational database management system.",
    "what is sql": "SQL is a language for managing and manipulating relational databases.",
    "what is data structure": "Data structures are ways of organizing data for efficient access and modification.",
    "what is algorithm": "An algorithm is a step-by-step procedure to solve a problem.",
    "what is dsa": "DSA stands for Data Structures and Algorithms.",
    "what is oop": "OOP stands for Object-Oriented Programming. It uses objects and classes in programming.",
    "what is inheritance": "Inheritance allows a class to acquire the properties and methods of another class.",
    "what is encapsulation": "Encapsulation means binding data and functions into a single unit (class).",
    "what is polymorphism": "Polymorphism allows methods to do different things based on the object it is acting upon.",
    "what is abstraction": "Abstraction hides internal implementation and shows only the necessary details.",
    "what is recursion": "Recursion is a function that calls itself to solve smaller instances of a problem.",
    "what is array": "An array is a collection of items stored at contiguous memory locations.",
    "what is loop": "A loop is used to repeat a block of code multiple times.",
    "what is function": "A function is a block of code that performs a specific task and can be reused.",
    "what is variable": "A variable is a named storage location in memory that can hold a value.",
    "what is constant": "A constant is a value that cannot be changed during the execution of a program.",
    "what is exception": "An exception is an error that occurs during the execution of a program.",
    "are you human": "No, I'm just a computer program designed to assist you.",
    "do you have feelings": "I don't have feelings, but I'm here to help you!",
    "can you learn": "I can provide information based on pre-defined responses, but I don't learn like humans do.",
    "capital of india": "The capital of India is New Delhi.",
    "largest country": "Russia is the largest country in the world by land area.",
    "smallest country": "Vatican City is the smallest country in the world.",
    "highest mountain": "Mount Everest is the highest mountain in the world.",
    "longest river": "The Nile is often considered the longest river in the world.",
    "most spoken language": "Mandarin Chinese is the most spoken language in the world.",
    "what is the meaning of life": "The meaning of life is a philosophical question that varies for each individual.",
    "tell me about yourself": "I'm SmartBot, created to assist you with information and answer your questions.",
    "whether right now": "I can't check the weather directly, but you can use a weather app or website.",
    "tell me a fact": lambda: random.choice([
        "Did you know honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible.",
        "Bananas are berries, but strawberries aren't! In botanical terms, a berry is a fruit produced from the ovary of a single flower with seeds embedded in the flesh.",
        "Octopuses have three hearts and blue blood. Two hearts pump blood to the gills, while the third pumps it to the rest of the body."
    ]),
    "tell me a quote": lambda: random.choice([
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
        "In the middle of every difficulty lies opportunity. - Albert Einstein",
        "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll"
    ]),
    "Galgotias": "Galgotias University is a private university located in Greater Noida, Uttar Pradesh, India.",
    "about galgotias": "Galgotias University offers a wide range of undergraduate and postgraduate programs in various fields including engineering, management, law, and more.",
    "galgotias university": "Galgotias University is known for its quality education and has been ranked among the top universities in India.",
    "galgotias college": "Galgotias College of Engineering and Technology is affiliated with Galgotias University and offers engineering programs.",
    "galgotias campus": "The Galgotias campus is equipped with modern facilities, libraries, and laboratories to support student learning.",
    "galgotias admission": "Admissions to Galgotias University are based on entrance exams like JEE Main, GALGOTIAS Entrance Exam, and other criteria depending on the program.",
    "galgotias placements": "Galgotias University has a dedicated placement cell that helps students secure internships and job placements in various industries.",
    "galgotias events": "Galgotias University hosts various cultural, technical, and sports events throughout the year to engage students.",
    "galgotias fest": "Galgotias Fest is an annual cultural festival that showcases talent from students across the university.",
    "galgotias sports": "Galgotias University encourages sports and has facilities for various sports including cricket, football, basketball, and more.",
    "galgotias faculty": "Galgotias University has a team of experienced faculty members who are dedicated to providing quality education.",
    "galgotias library": "The Galgotias library is well-stocked with books, journals, and digital resources to support student research and learning.",
    "galgotias hostel": "Galgotias University provides hostel facilities for students with all necessary amenities for a comfortable stay.",
    "galgotias campus life": "Campus life at Galgotias University is vibrant with various clubs, societies, and extracurricular activities.",
    "galgotias alumni": "Galgotias University has a strong alumni network that supports current students through mentorship and career guidance.",
    "galgotias research": "Galgotias University promotes research and innovation among students and faculty, encouraging them to publish papers and participate in conferences.",
    "who is prabhat": "Prabhat is a student at Galgotias University, known for his interest in programming and technology.",
    "tell me about prabhat": "Prabhat is a dedicated student at Galgotias University, passionate about learning and technology.",
    "prabhat's hobbies": "Prabhat enjoys coding, reading tech blogs, and participating in hackathons.",
    "prabhat's interests": "Prabhat is interested in artificial intelligence, machine learning, and software development.",
    "prabhat's achievements": "Prabhat has participated in various coding competitions and has won accolades for his innovative projects.",
    "prabhat's future plans": "Prabhat aims to work in the field of software development and contribute to innovative tech solutions.",
    "prabhat's favorite programming language": "Prabhat's favorite programming language is Python due to its simplicity and versatility.",
    "prabhat's favorite subject": "Prabhat's favorite subject is Computer Science, particularly programming and algorithms.",
    "prabhat's favorite book": "Prabhat enjoys reading books on technology and programming, especially those that enhance his coding skills.",
    "prabhat's favorite movie": "Prabhat loves movies that inspire innovation and creativity, especially those related to technology.",
    "prabhat's favorite music": "Prabhat enjoys listening to music that helps him focus while coding, often instrumental or electronic.",
    "prabhat's favorite food": "Prabhat enjoys a variety of cuisines, but he particularly loves Indian and Italian food.",
    "prabhat's favorite sport": "Prabhat enjoys playing cricket and football during his free time.",
    "prabhat's favorite hobby": "Prabhat's favorite hobby is coding and exploring new technologies.",
    "prabhat's favorite quote": "Prabhat believes in the quote, 'The only way to do great work is to love what you do.' - Steve Jobs",
    "prabhat's favorite quote about learning": "Prabhat often quotes, 'Live as if you were to die tomorrow. Learn as if you were to live forever.' - Mahatma Gandhi",
    "prabhat's favorite quote about success": "Prabhat believes in the quote, 'Success is not the key to happiness. Happiness is the key to success.' - Albert Schweitzer",
    "prabhat's favorite quote about technology": "Prabhat often says, 'Technology is best when it brings people together.' - Matt Mullenweg",
    "prabhat's favorite quote about life": "Prabhat believes in the quote, 'Life is what happens when you're busy making other plans.' - John Lennon",
    "prabhat's favorite quote about challenges": "Prabhat often quotes, 'Challenges are what make life interesting; overcoming them is what makes life meaningful.' - Joshua J. Marine",
}

# Create chatbot response function
def get_response(user_input):
    user_input = user_input.lower().strip()
    for key in responses:
        if key in user_input:
            response = responses[key]
            return response() if callable(response) else response
    return "I'm not sure how to respond to that. Try asking something else."

# GUI
root = tk.Tk()
root.title("SmartBot - Python Chatbot")
root.geometry("500x600")
root.config(bg="#f0f0f0")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_window.place(x=20, y=20, width=460, height=450)
chat_window.insert(tk.END, "Bot: Hello! I am SmartBot. Type 'bye' to exit.\n")
chat_window.config(state='disabled')

user_input = tk.StringVar()
entry_box = tk.Entry(root, textvariable=user_input, font=("Arial", 14))
entry_box.place(x=20, y=490, width=380, height=40)

# Listbox for suggestions
suggestion_box = tk.Listbox(root, font=("Arial", 12), height=5)
suggestion_box.place(x=20, y=530, width=460)
suggestion_box.bind("<<ListboxSelect>>", lambda event: fill_suggestion())

# Hide suggestion box initially
suggestion_box.place_forget()

def update_suggestions(event=None):
    typed = user_input.get().lower()
    suggestion_box.delete(0, tk.END)

    if typed == "":
        suggestion_box.place_forget()
        return

    # Find keys that start with the typed text
    suggestions = [key for key in responses.keys() if key.startswith(typed)]

    if suggestions:
        for s in suggestions:
            suggestion_box.insert(tk.END, s)
        suggestion_box.place(x=20, y=530, width=460)
    else:
        suggestion_box.place_forget()

def fill_suggestion():
    if suggestion_box.curselection():
        index = suggestion_box.curselection()[0]
        value = suggestion_box.get(index)
        user_input.set(value)
        suggestion_box.place_forget()
        entry_box.icursor(tk.END)  # Move cursor to end

# Bind key release event to update suggestions while typing
entry_box.bind("<KeyRelease>", update_suggestions)

# Send button functionality
def send():
    message = user_input.get()
    if message.strip():
        suggestion_box.place_forget()  # Hide suggestions on send
        chat_window.config(state='normal')
        chat_window.insert(tk.END, f"You: {message}\n")
        response = get_response(message)
        chat_window.insert(tk.END, f"Bot: {response}\n\n")
        chat_window.config(state='disabled')
        chat_window.see(tk.END)
        user_input.set("")

send_btn = tk.Button(root, text="Send", command=send, font=("Arial", 12), bg="#4caf50", fg="white")
send_btn.place(x=410, y=490, width=70, height=40)

# Bind Enter key to send
entry_box.bind("<Return>", lambda event: send())

root.mainloop()
# This code creates a simple chatbot application using Tkinter in Python.