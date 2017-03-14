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
        self.entry = Entry(self)
        self.button = Button(self, text="Get", command=self.click_submit)
        self.button.pack()
        self.entry.pack()

    def click_submit(self):
        r_source = ro.r["source"]
        curr_dir = os.path.dirname(__file__)
        ranalytics = r_source(curr_dir + "/ranalytics/ranalytics.R")
        do_analysis = ranalytics[0]
        do_analysis(self.entry.get(), number=1000)

root = App()
root.title("Twitter Semantic Analysis")
root.minsize(width=866, height=533)

# run
root.mainloop()
