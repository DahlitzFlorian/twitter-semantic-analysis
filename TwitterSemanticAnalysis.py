"""
    -----------------------------------
    TwitterSemanticAnalysis.py
    -----------------------------------
    This application is made to easily do some semantic analysis making use of the
    Twitter API (used w/ R).
    -----------------------------------
"""
import sys

# global variables
version = sys.version

# importing libs based on Python version
if "2.7" in version:
    from Tkinter import *
    import tkFileDialog as filedialog
elif "3.3" in version or "3.4" in version:
    from tkinter import *
    from tkinter import filedialog

# setting up window
root = Tk("Twitter Semantic Analysis")
root.title("Twitter Semantic Analysis")

# run
root.mainloop()
