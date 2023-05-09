#Written by Shiven Desai
import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create a Label widget containing the text "Hello World!"
        self.label = tkinter.Label(self.main_window, text='Hello World!')
        self.label.pack()

        # Create labels for last name, first name, and age
        self.last_name_label = tkinter.Label(self.main_window, text='Last Name:')
        self.first_name_label = tkinter.Label(self.main_window, text='First Name:')
        self.age_label = tkinter.Label(self.main_window, text='Age:')

        # Pack the labels onto the window
        self.last_name_label.pack()
        self.first_name_label.pack()
        self.age_label.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    gui = MyGUI()
