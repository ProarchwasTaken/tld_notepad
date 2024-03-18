from tkinter import Tk, Label, Button
import tkinter.filedialog as fd
from tkinter.constants import BOTTOM, END, LEFT, N, W
from tkinter.scrolledtext import ScrolledText
from backend import saveFile, getCurrentPath, setCurrentPath


class Application:
    """Notepad clone capable of opening and saving files."""
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Tyler's Notepad")
        self.root.geometry("600x400")
        self.root.resizable(width=False, height=False)

        self.setupWidgit()
        self.root.mainloop()

    def setupWidgit(self):
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
            font=text_font,
            command=self.clearBuffer,
            width=10,
            height=1,
            borderwidth=5
        )
        open_file = Button(
            master=self.root,
            text="Open File",
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
        if getCurrentPath() == "" or new_path:
            save_path: str = fd.asksaveasfilename()
            setCurrentPath(save_path)

        saveFile(self.buffer.get("1.0", END))

    def clearBuffer(self):
        self.buffer.delete("1.0", END)


if __name__ == "__main__":
    Application()

