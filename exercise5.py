#Written by Shiven Desai
import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create two frames to group widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the top frame.
        self.prompt_label = tkinter.Label(self.top_frame,
                                           text='Enter a distance in kilometers:')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        # Pack the top frame's widgets.
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # Create the button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame,
                                           text='Convert',
                                           command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                           text='Quit',
                                           command=self.main_window.destroy)

        # Add three buttons for positive quotes
        self.quote1_button = tkinter.Button(self.bottom_frame,
                                            text='Quote 1',
                                            command=self.display_quote1)
        self.quote2_button = tkinter.Button(self.bottom_frame,
                                            text='Quote 2',
                                            command=self.display_quote2)
        self.quote3_button = tkinter.Button(self.bottom_frame,
                                            text='Quote 3',
                                            command=self.display_quote3)

        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.quote1_button.pack(side='left')
        self.quote2_button.pack(side='left')
        self.quote3_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The convert method is a callback function for the Calculate button.
    def convert(self):
        # Get the value entered by the user into the kilo_entry widget.
        kilo = float(self.kilo_entry.get())

        # Convert kilometers to miles.
        miles = kilo * 0.6214

        # Display the results in an info dialog box.
        tkinter.messagebox.showinfo('Results',
                                    str(kilo) +
                                    ' kilometers is equal to ' +
                                    str(miles) + ' miles.')

    # Define three callback functions for displaying positive quotes.
    def display_quote1(self):
        tkinter.messagebox.showinfo('Positive Quote', 'The only way to do great work is to love what you do. - Steve Jobs')

    def display_quote2(self):
        tkinter.messagebox.showinfo('Positive Quote', 'You are never too old to set another goal or to dream a new dream. - C.S. Lewis')

    def display_quote3(self):
        tkinter.messagebox.showinfo('Positive Quote', 'Believe you can and you are halfway there. - Theodore Roosevelt')

# Create an instance of the KiloConverterGUI class.
if __name__ == '__main__':
    kilo_conv = KiloConverterGUI()
