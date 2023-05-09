#Written by Shiven Desai
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create three Button widgets.
        self.button1 = tkinter.Button(self.main_window,
                                      text='Click for a positive quote!',
                                      command=lambda: self.show_quote('You are capable of amazing things!'))
        self.button2 = tkinter.Button(self.main_window,
                                      text='Click for a positive quote!',
                                      command=lambda: self.show_quote('Believe in yourself and all that you are.'))
        self.button3 = tkinter.Button(self.main_window,
                                      text='Click for a positive quote!',
                                      command=lambda: self.show_quote('The best way to predict your future is to create it.'))

        # Pack the Buttons.
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The show_quote method is a callback function for the Button widgets.
    def show_quote(self, quote):
        # Display an info dialog box with the provided quote.
        tkinter.messagebox.showinfo('Positive Quote', quote)

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()
