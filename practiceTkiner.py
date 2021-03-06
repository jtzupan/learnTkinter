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
#can also add height and width parameters to arguments

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
#button can also take a parameter called 'command'
button1 = Button(topFrame, text='Some text', fg='red')

##########################################################
#how to bind a function to a widget
##this is just one of many ways to do this
#as an optional parameter to the button, add 'command = function here'
#ex.
buttonWithFunction = Button(root, text = 'print my name', command = somefunction)

#another way to do this
#pass an event as an input to the function
## in the function definition
#use bind method to bind the event to a user action
buttonEvent.bind(<button>, example_function)

#can bind multiple events to a single widget
#different button clicks are different actions

#################################################################
# how to use tkinter with classes
#can pass the frame when the object is initialized
#frame.quit is the built in quitting function, breaks main loop

###################################################################
#how to make a drop down menu (9)
#create basic function before the root call
#create the menu using the tkinter command
menu = Menu(root)
#configure the menu
root.config(menu = menu)

#create the dropdown options
#build a new menu and place it within the existing menu
submenu = Menu(menu)
#cascade adds the drop down and menu places the menu in the drop down
menu.add_casdcade(label = 'File', menu = submenu)
#add submenus for every line of the drop down
submenu.add_command(label = 'new project', command= python command here)
submenu1.add_command(label = 'new project', command= python command here)
#seperator adds lines between drop down menu options
submenu.add.seperator()

###################################################################
#creating a toolbar
toolbar = Frame(root, bg = 'some color'
insertToolbar = Button(toolbar, text = 'some text', command = doNothing)
insertToolbar.pack(side = LEFT, padx = 2, pady = 2)
printButton = Button(toolbar, text = 'some other text', command = doNothing)
printButton.pack(side = LEFT)

toolbar.pack(side = TOP, fill = x)

####################################################################
#toolbar continues
status = Label(root, text = 'some text', bd = 1, relief = SUNKEN, anchor = W
status.pack(side = BOTTOM, fill = X)

####################################################################
#display window continuously, should always be present
root.mainloop()

























