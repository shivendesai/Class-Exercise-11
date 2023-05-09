#Written by Shiven Desai
import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()
        # Set the window dimensions.
        self.main_window.geometry('400x200')
        # Display a title.
        self.main_window.title('My First GUI')
        # Enter the tkinter main loop.
        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()
