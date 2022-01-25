#curses basics
import curses
from curses import wrapper

def main(stdscr):  #stdscr => standard output screen.

	stdscr.clear() # command to clear the cmd prompt to get clean output
    
    #similar to print statement, the first two arguments are to specify the position of the cursor.
       #the screen acts like a coordinate system.
	stdscr.addstr(10,50,"My first curses program!!") 

	#lets see how to overwrite a text!!
       #to overwrite a certian text place the cursor on the position where you want to overwrite and print the required text in that position.
	stdscr.addstr(10,45, "Overwritten text ")

	#Curses attributes and colors
	stdscr.addstr(0,0,"I'am Dennis Mathew Jose", curses.A_UNDERLINE)
	stdscr.addstr(1,0,"Blink text",curses.A_BLINK) #blink mode
	stdscr.addstr(4,0,"Reverse mode", curses.A_REVERSE) #reverse background and foreground colors

    #the first argument of the function is the id, 2nd argument is the foreground color and 3rd argument is background color
	curses.init_pair(1, curses.COLOR_RED,curses.COLOR_GREEN)
	curses.init_pair(2, curses.COLOR_GREEN,curses.COLOR_BLUE)

	#blue and yellow is a variable which denote the color scheme directed to id 1
	red_and_green = curses.color_pair(1)
	stdscr.addstr(6,0,"Color mode on", red_and_green)
	stdscr.addstr(8,0,"blue on green", curses.color_pair(2)) 

	#attributes and colors working simultaneously
	stdscr.addstr("\nThis is a sample program", red_and_green|curses.A_UNDERLINE) #any atributes can be given similarly
	stdscr.addstr("\n\nReversing the colors",curses.color_pair(2)|curses.A_REVERSE)
	stdscr.refresh() #we have to refresh the screen after clearing the previous contents
	stdscr.getch() # wait until the user press a key 

wrapper(main)