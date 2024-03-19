from tkinter import Tk, Label, Button
import tkinter.filedialog as fd
from tkinter.constants import BOTTOM, END, LEFT, N, W
from tkinter.scrolledtext import ScrolledText
from backend import (saveFile, getCurrentPath, setCurrentPath, 
    getFileContents)


class Application:
    """Notepad clone capable of opening and saving files. Not gonna lie,
    I had a good time building this program, and I learned a lot of stuff
    from it."""
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Tyler's Notepad")
        self.root.geometry("600x400")
        self.root.resizable(width=False, height=False)

        self.setupWidgits()

        print("Everything is good to go! Now beginning main loop.")
        self.root.mainloop()
        print("Cya next time!")

    def setupWidgits(self):
        self.buffer = ScrolledText(
            self.root,
            width=70, 
            height=20,                         
            borderwidth=10
        )

        txt_credits = Label(
            self.root, 
            text="Application written by: Tyler Dillard"
        )

        text_font = ("Arial", 10, "bold")

        new_file = Button(
            master=self.root,
            text="New File",
            command=self.clearBuffer,
            font=text_font,
            width=10,
            height=1,
            borderwidth=5
        )
        open_file = Button(
            master=self.root,
            text="Open File",
            command=self.openFile,
            font=text_font,
            width=10,
            height=1,
            borderwidth=5
        )
        save = Button(
            master=self.root,
            text="Save",
            command=self.saveBuffer,
            font=text_font,
            width=10,
            height=1,
            borderwidth=5
        )
        save_as = Button(
            master=self.root,
            text="Save As",
            command=lambda: self.saveBuffer(new_path=True),
            font=text_font,
            width=10,
            height=1,
            borderwidth=5
        )

        self.buffer.place(x=0, y=32)
        txt_credits.pack(side=BOTTOM, anchor=W)

        new_file.pack(side=LEFT, anchor=N)
        open_file.pack(side=LEFT, anchor=N)
        save.pack(side=LEFT, anchor=N)
        save_as.pack(side=LEFT, anchor=N)

    def saveBuffer(self, new_path: bool = False):
        """For saving the current buffer as an usable file. This is done
        by calling a function from the backend. File dialog only opens
        if the current path is empty, or the user clicks the 'Save As'
        button."""

        if getCurrentPath() == "" or new_path:
            save_path: str = fd.asksaveasfilename()
            setCurrentPath(save_path)

        saveFile(self.buffer.get("1.0", END))

    def openFile(self):
        """For loading up a given file and inserting it's contents into
        the buffer. Not before clearing it though."""

        file: str = fd.askopenfilename()
        setCurrentPath(file)
        file_contents: str = getFileContents()

        self.clearBuffer(clear_path=False)
        self.buffer.insert("1.0", file_contents)

    def clearBuffer(self, clear_path: bool = True):
        """It's self explanatory. It also clears the current path by
        default unless specified otherwise."""

        if clear_path:
            setCurrentPath("", force=True)
        self.buffer.delete("1.0", END)


if __name__ == "__main__":
    Application()

