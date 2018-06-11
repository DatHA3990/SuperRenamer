# By Dat HA copyrights 2017

# library to navigate files
import os

# library for user interface
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import IntVar


# function to rename files
def rename():
    # get text prefix
    textPrefix = prefixEntry.get()

    # if no names were inputed
    if nameText.get("1.0", "end-1c") == "":
        messagebox.showinfo("Renaming status", "Error, no new file names were found.")
        return

    # if there is no directory
    if directoryName == "":
        messagebox.showinfo("Renaming status", "Error, directory not found.")
        return

    # get name list from user
    name = nameText.get("1.0", "end-1c").split('\n')
    name = [i for i in name if i]

    # get all the files that are going to be renamed
    files = [i.split('\\')[1] for i in
             [os.path.join("files", f) for root, dirs, files in os.walk(directoryName) for f in files]]

    # file number
    num = 0 if isZero.get() else 1

    # if there is the same number of names and files. made to prevent errors
    if len(name) == len(files):

        # going through the files
        for i in range(len(files)):
            # rename the files
            os.rename(directoryName + '\\' + files[i],
                      directoryName + '\\' + textPrefix + [" - ", ""][textPrefix == ""] + (
                          "%s - " % (str(num)) if isNumbered.get() else "") + name[i].replace('\t', '_') + '.' +
                      files[i].split('.')[1])

            # increment number
            num += 1

        # indicate to user that renaming was sucessfusl
        messagebox.showinfo("Renaming status", "Sucess, files have been renamed.")
        return

    else:
        # indicate to user that there was an error during remaing
        messagebox.showinfo("Renaming status", "Error, files quantity and name quantity do not match.")
        return


def setDirectory():
    global directoryName
    directoryName = filedialog.askdirectory()
    directoryName = directoryName.replace("/", "\\")


# create window
window = tk.Tk()
# set window title
window.title("Super ReNameR")

# directory name
directoryName = ""
isNumbered = tk.IntVar(window)
isZero = tk.IntVar(window)

# text prefix variable
textPrefix = ""

# thing so that stuff stick to all sides
stick = tk.N + tk.S + tk.E + tk.W

# display renaming instructions to user
instructionLabel1 = tk.Label(window, text="Enter new file names here")
instructionLabel1.grid(row=0, columnspan=2, sticky=stick)

# create text location
nameText = tk.Text(window, width=45)
nameText.grid(row=1, column=0, columnspan=2, sticky=stick)

# are files going to be numbered
numberedCheck = tk.Checkbutton(window, text="Number files", variable=isNumbered)
numberedCheck.grid(row=2, column=0, sticky=stick)

# start numbering on 0
zeroCheck = tk.Checkbutton(window, text="Start on 0", variable=isZero)
zeroCheck.grid(row=2, column=1, sticky=stick)

# add text prefix label
prefixLabel = tk.Label(window, text="Enter prefix for file naming")
prefixLabel.grid(row=3, columnspan=1, sticky=stick)

# add text prefix input
prefixEntry = tk.Entry(window, textvariable=textPrefix)
prefixEntry.grid(row=3, column=1, sticky=stick)

# get directory
directoryButton = tk.Button(window, text="Choose directory", command=setDirectory)
directoryButton.grid(row=4, column=0, sticky=stick)

# create out rename button
renameButton = tk.Button(window, text="Rename", command=rename)
renameButton.grid(row=4, column=1, sticky=stick)

# run the ui
window.mainloop()
