#this is a practice file
#basic idea of tkinter is to make a window and add widgets to this window


#import module
import tkinter

#build the basic window
root = Tk()

#add a label
#can also change backgound color (bg), and foreground color (fg)
label1 = Label(root, text = 'some text')

#different ways to give the objects a location in window
########################################################

#pack places label in window whereever it fits
label1.pack()
#pack can have a placement parameter, default is to stack things on top of one another
#ex label.pack(side=BOTTOM, TOP, LEFT, RIGHT)
#pack has parameter (fill = X) to set object as wide as parent window

# a frame as in invisible container that can be places in a window, this creates frame, still needs to be placed
topFrame = Frame(root)

#########################################################
#use entry to allow for user input/blank fields
entryExample = Entry(root,)

########################################################
# can use grids to organize widgets
#column default is 0
#can align within container using 'sticky' = N, E, W, S (north, east, south, west)
widg1.grid(row=0)
widg2.grid(row=0, column=1)
widg3.grid(row=1)
widg4.grid(row=1, column=1)

#########################################################
#to get a checkbox
exampleCheck = Checkbutton(root, text='example text')
#how to make a widget span multiple cells
exampleCheck.grid(columnspan=2)

##########################################################
#buttons
#button1 = Button(where to put it, text of button, color of button)
button1 = Button(topFrame, text='Some text', fg='red')


#display window continuously, should always be present
root.mainloop()
