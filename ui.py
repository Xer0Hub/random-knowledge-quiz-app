from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     font=("Ariel", 20, "italic"),
                                                     text="Some question text",
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # IMAGE LIBRARY
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        #BUTTONS
        self.true = Button(image=true_image, highlightthickness=0)
        self.true.grid(row=2, column=0
                       )
        self.false = Button(image=false_image, highlightthickness=0)
        self.false.grid(row=2, column=1)

        self.window.mainloop()