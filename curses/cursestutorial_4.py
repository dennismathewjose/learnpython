#textboxes
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

def main(stdscr):
	stdscr.clear()
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

	win = curses.newwin(3, 18, 2, 2) #we create a new window which is of the size of the rectangle
	t_box = Textbox(win, curses.color_pair(1)) #now we made this new window as our textbox

	#rectangle is created using the function rectangle of curses module
	rectangle(stdscr, 1, 1, 5, 20) #the first argument is the std o/p screen, 
	#the 2nd and 3rd arg is the top left corner (x,y) of rectangle and 4th & 5th argument is the bottom right corner (x,y)

	stdscr.refresh()

	#this helps the user to write text in the textbox
	t_box.edit() # use ctrl+G to get out of the textbox
	
     # gather() function is used to retrieve the text from the textbox.
	text = t_box.gather()

	text2 = t_box.gather().replace("\n","")

	stdscr.addstr(10,0, text)
	stdscr.addstr(15,0, text2)
	stdscr.getch()

wrapper(main)