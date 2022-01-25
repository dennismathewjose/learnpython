#miscellaneous Examples

import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

	curses.echo() # to see the keys typing

     # the block of code which fall under the attribute on and off will follow the specified attributes
	stdscr.attron(curses.color_pair(2))
	#border() function is used to create a border along the screen. We can adjust the size of the border
	stdscr.border()
	stdscr.attroff(curses.color_pair(2))

	stdscr.attron(curses.color_pair(1))

	row,col = stdscr.getmaxyx()# to get the maximum number of rows and columns
	stdscr.addstr(1,1,f'{row},{col}')
	stdscr.addstr(row//2,col//2,"Middle")# to print in the middle row and column

	rectangle(stdscr, 2,2,5,18)
	stdscr.addstr(15,1, "End of Today's session")
	stdscr.attroff(curses.color_pair(1))

	stdscr.move(20,1)#to move the cursor to a particular point in the screen

	while True:
		stdscr.attron(curses.color_pair(1))
		key = stdscr.getkey()
		if ord(key) == 27:
			break

	stdscr.attroff(curses.color_pair(1))
	stdscr.refresh()


wrapper(main)