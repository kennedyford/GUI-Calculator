from tkinter import *

class MainGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg = "white")
        master.attributes("-fullscreen", False)
        self.setupGUI()

    # sets up the GUI to display
    def setupGUI(self):
        self.display = Label(self, text = "", anchor = E, bg = "white",\
                             height = 1, font = ("TexGyreAdventor", 45))
        self.display.grid(row = 0, column = 0, columnspan = 4, sticky = N+W+E+S)
        self.pack(fill = BOTH, expand = 1)

        for row in range(6):
            Grid.rowconfigure(self, row, weight = 1)

        for col in range(4):
            Grid.columnconfigure(self, col, weight = 1)

        # ( ) AC <-
        # 7 8 9  /
        # 4 5 6  *
        # 1 2 3  -
        # 0 .    +
        #  =  ** %

        ############### FIRST ROW ##################
        
        img = PhotoImage(file = "images/lpr.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("("))
        button.image = img
        button.grid(row = 1, column = 0, sticky = N+W+E+S)

        # )
        img = PhotoImage(file = "images/rpr.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process(")"))
        button.image = img
        button.grid(row = 1, column = 1, sticky = N+W+E+S)

        # AC
        img = PhotoImage(file = "images/clr.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("AC"))
        button.image = img
        button.grid(row = 1, column = 2, sticky = N+W+E+S)

        # <-
        img = PhotoImage(file = "images/bak.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("backspace"))
        button.image = img
        button.grid(row = 1, column = 3, sticky = N+W+E+S)

        ############### SECOND ROW ####################
        # 7
        img = PhotoImage(file = "images/7.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("7"))
        button.image = img
        button.grid(row = 2, column = 0, sticky = N+W+E+S)

        # 8
        img = PhotoImage(file = "images/8.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("8"))
        button.image = img
        button.grid(row = 2, column = 1, sticky = N+W+E+S)

        # 9
        img = PhotoImage(file = "images/9.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("9"))
        button.image = img
        button.grid(row = 2, column = 2, sticky = N+W+E+S)

        # /
        img = PhotoImage(file = "images/div.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("/"))
        button.image = img
        button.grid(row = 2, column = 3, sticky = N+W+E+S)

        ################ THIRD ROW #######################
        # 4
        img = PhotoImage(file = "images/4.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("4"))
        button.image = img
        button.grid(row = 3, column = 0, sticky = N+W+E+S)

        # 5
        img = PhotoImage(file = "images/5.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("5"))
        button.image = img
        button.grid(row = 3, column = 1, sticky = N+W+E+S)

        # 6
        img = PhotoImage(file = "images/6.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("6"))
        button.image = img
        button.grid(row = 3, column = 2, sticky = N+W+E+S)

        # *
        img = PhotoImage(file = "images/mul.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("*"))
        button.image = img
        button.grid(row = 3, column = 3, sticky = N+W+E+S)

        ################ FORTH ROW #######################
        # 1
        img = PhotoImage(file = "images/1.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("1"))
        button.image = img
        button.grid(row = 4, column = 0, sticky = N+W+E+S)

        # 2
        img = PhotoImage(file = "images/2.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("2"))
        button.image = img
        button.grid(row = 4, column = 1, sticky = N+W+E+S)

        # 3
        img = PhotoImage(file = "images/3.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("3"))
        button.image = img
        button.grid(row = 4, column = 2, sticky = N+W+E+S)

        # -
        img = PhotoImage(file = "images/sub.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("-"))
        button.image = img
        button.grid(row = 4, column = 3, sticky = N+W+E+S)

        ################ FIFTH ROW #######################
        # 0
        img = PhotoImage(file = "images/0.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("0"))
        button.image = img
        button.grid(row = 5, column = 0, sticky = N+W+E+S)

        # .
        img = PhotoImage(file = "images/dot.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("."))
        button.image = img
        button.grid(row = 5, column = 1, sticky = N+W+E+S)

        # +
        img = PhotoImage(file = "images/add.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("+"))
        button.image = img
        button.grid(row = 5, column = 3, sticky = N+W+E+S)

        ################ SIXTH ROW #######################

        # =
        img = PhotoImage(file = "images/eql-wide.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("="))
        button.image = img
        button.grid(row = 6, column = 0, columnspan = 2, sticky = N+W+E+S)

        # **
        img = PhotoImage(file = "images/pow.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("**"))
        button.image = img
        button.grid(row = 6, column = 2, sticky = N+W+E+S)

        # %
        img = PhotoImage(file = "images/mod.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command = lambda: self.process("%"))
        button.image = img
        button.grid(row = 6, column = 3, sticky = N+W+E+S)

    # gives the buttons an action
    def process(self, button):

        # clears the screen
        if (button == "AC"):
            self.display["text"] = ""

        # evaluates something mathematically when "=" button is pressed
        elif (button == "="):
            expr = self.display["text"]

            try:
                result = str(eval(expr))

                # restricts the result to 14 or less characters
                if (len(result) > 13):
                    result_short = result[0:11]
                    self.display["text"] = result_short + "..."
                    
                else:
                    self.display["text"] = str(result)

            except:
                self.display["text"] = "ERROR"

        # if "ERROR" is displayed, clears the screen when a new button is pushed
        elif (self.display["text"] == "ERROR"):
            self.display["text"] = ""

        # sets up the backspace button
        elif (button == "backspace"):
            new_expr = self.display["text"][:-1]
            self.display["text"] = new_expr

        # restricts the screen to 14 or less characters
        elif (len(self.display["text"]) > 13):
            pass

        # displays any other buttons on the screen (integers, math sumbols, etc.)
        else:
            self.display["text"] += button
            

        

################################## M A I N ####################################

# create window
window = Tk()

# set the window title
window.title("The Reckoning")

# generate the gui
p = MainGUI(window)

# display and wait for user interaction
window.mainloop()
