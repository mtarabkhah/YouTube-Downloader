from pytube import YouTube
import csv
from tkinter import *
from tkinter.filedialog import askopenfilename

# Main function to download a video from the provided <link>
def Download(link):
    print(f'\nDownloading "{link}"')
    try: # Using exception handling to avoid runtime errلهفors such as incorrect link
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download()
        print("Download is completed successfully")
    except:
        print("An error has occurred")

# Changing the text of a entry widget to a new text
def set_text(e,text):
    e.delete(0,END)  # Deleting previous text
    e.insert(0,text) # Setting new text
    return

# Clearing all the user input values
def clearButtonClick():
   # choice = None
   set_text(linkEntry,"")
   set_text(fileEntry,"")
   # downloadButton['state'] = DISABLED

def selectButtonClick():
   filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
   set_text(fileEntry,filename)
   # choice = "File"
   # downloadButton['state'] = NORMAL

def downloadButtonClick():
    if linkEntry.get(): # choice == "Link":
        Download(linkEntry.get())
    elif fileEntry.get(): # choice == "File":
        filename = fileEntry.get()
        with open(filename, 'r') as file:
            csvreader = csv.reader(file)
            for link in csvreader:
                Download(link[0])
            file.close()

# choice = None
root = Tk()
# root.geometry("450x90")

# Creating Lable Widgets
linkLabel = Label(root,text="Video Link")
linkLabel.grid(row=0,column=0)

fileLabel = Label(root,text="Links' File")
fileLabel.grid(row=1,column=0)

# Creating Button Widgets
clearButton = Button(root,text="Clear Form",command=clearButtonClick)
clearButton.grid(row=2,column=0)

selectButton = Button(root,text="Select File",command=selectButtonClick)
selectButton.grid(row=1,column=2)

downloadButton = Button(root,text="Download",command=downloadButtonClick) # ,state=DISABLED)
downloadButton.grid(row=2,column=2)

# Creating Entry Widgets
linkEntry = Entry(root,width=50)
linkEntry.grid(row=0,column=1)

fileEntry = Entry(root,width=50)
fileEntry.grid(row=1,column=1)

root.mainloop()