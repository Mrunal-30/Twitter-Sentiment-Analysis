from tkinter import *
from PIL import ImageTk
import tkinter
# Create GUI window
root = Tk()
root.title("Twitter Sentiment Analysis")
# root.configure(bg="#1da1f2")
root.geometry('1920x1080+0+0')
# root.resizable(False,False)

bgimage=ImageTk.PhotoImage(file='960x01.jpg')
bglabel=Label(root,image=bgimage)
bglabel.place(x=0,y=0)

# Logo
# Frame
LogoFrame=Frame(root,bg="#1da1f2")
LogoFrame.place(x=400,y=150)

LogoImage=ImageTk.PhotoImage(file='logo.jpeg')

LOgoLabel=Label(LogoFrame,image=LogoImage)
LOgoLabel.grid(row=0,column=1,columnspan=2,pady=50)

# Create input field for tweet
entry_label =Label(LogoFrame,text="Enter the tweet:", fg="black", bg="#1da1f2", font=("Helvetica", 15, "bold"))
entry_label.place()
entry_label.grid(row=1,column=0,pady=10,padx=20 )
entry = Entry(LogoFrame, width=50,bd=5,fg="black",font=("Helvetica",10))
entry.grid(row=1,column=1,pady=10,padx=10)

# Function to analyze sentiment on button click
def analyze():
    tweet = entry.get()
    sentiment = analyze_sentiment(tweet)
    result_label.config(text=f"Sentiment: {sentiment}", fg=sentiment_colors[sentiment])
    
# Create button to perform sentiment analysis
analyze_button = Button(LogoFrame, text="Analyze", command=analyze,bd=5,width=15,font=('times new roman',14,"bold"))
analyze_button.grid(row=2,column=1,padx=10,pady=10)

def reset():
    reset_button=Button(text="")
# Create button to reset sentiment analysis
reset_button = Button(LogoFrame, text="Reset", command=reset,width=15,bd=5,font=('times new roman',14,"bold"))
reset_button.grid(row=3,column=1,padx=10,pady=20)
    
# Label to display sentiment result
result_label = Label(LogoFrame, text="",fg="Black",bd=10,width=20, bg="white", font=("Helvetica", 12, "bold"))
result_label.grid(row=5,column=1,pady=10)


# Define sentiment colors
sentiment_colors = {"Positive": "green", "Neutral": "orange", "Negative": "red"}

# Function to perform sentiment analysis
def analyze_sentiment(tweet):
    # Pre-defined positive and negative words
    positive_words = ["happy","good", "great", "excellent", "awesome", "nice","love", "hope", "joy", "gratitude", "kindness", "optimism", "success", "inspiration", "confidence", "harmony", "enjoy","laughter", "appreciation"]
    negative_words = ["bad", "poor", "terrible", "hate", "awful"]

    # Tokenize the tweet
    words = tweet.split()

    # Count positive and negative words in the tweet
    positive_count = sum(1 for word in words if word.lower() in positive_words)
    negative_count = sum(1 for word in words if word.lower() in negative_words)

    # Determine sentiment based on word counts
    if positive_count > negative_count:
        return "Positive"
    elif positive_count == negative_count:
        return "Neutral"
    else:
        return "Negative"






# Calculate the center position of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_x = int((screen_width - window_width) / 2)
position_y = int((screen_height - window_height) / 2)
root.geometry("+{}+{}".format(position_x, position_y))

# Run the GUI application
root.mainloop()