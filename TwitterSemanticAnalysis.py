"""
    -----------------------------------
    TwitterSemanticAnalysis.py
    -----------------------------------
    This application is made to easily do some semantic analysis making use of the
    Twitter API (used w/ R).
    -----------------------------------
"""
import sys
import rpy2.robjects as ro
import os

# global variables
version = sys.version

# global R functions
r_source = ro.r["source"]

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
root.minsize(width=866, height=533)

# running Ranalytics
curr_dir = os.path.dirname(__file__)
ranalytics = r_source(curr_dir+"/ranalytics/ranalytics.R")
do_analysis = ranalytics[0]
do_analysis("AI", number=1000)

# run
root.mainloop()
