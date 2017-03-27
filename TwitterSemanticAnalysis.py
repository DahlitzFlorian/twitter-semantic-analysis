"""
    -----------------------------------
    TwitterSemanticAnalysis.py
    -----------------------------------
    This application is made to easily do some semantic analysis making use of the
    Twitter API (used w/ R).
    -----------------------------------
"""
import rpy2.robjects as ro
import os
from tkinter import *
from tkinter import filedialog


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.term = Entry(self)
        self.number = Entry(self)
        self.button = Button(self, text="Get", command=self.click_submit)
        self.term_label = Label(self, text="Term to search")
        self.number_label = Label(self, text="Number of tweets")
        self.button.pack()
        self.term_label.pack()
        self.term.pack()
        self.number_label.pack()
        self.number.pack()

    def check_empty(self, term, number):
        if len(term) == 0:
            term = "Twitter"
        if len(number) == 0:
            number = 100
        return {1: term, 2: number}

    def click_submit(self):
        values = self.check_empty(term=self.term.get(), number=self.number.get())
        r_source = ro.r["source"]
        curr_dir = os.path.dirname(__file__)
        ranalytics = r_source(curr_dir + "/ranalytics/ranalytics.R")
        do_analysis = ranalytics[0]
        do_analysis(values[1], number=values[2])

root = App()
root.title("Twitter Semantic Analysis")
root.minsize(width=866, height=533)

# run
root.mainloop()
