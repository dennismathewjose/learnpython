#new windows
import time
import curses
from curses import wrapper

def main(stdscr):
	stdscr.clear()
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
	curses.init_pair(2,curses.COLOR_BLACK, curses.COLOR_WHITE)

	#this is a method used to create a new window on top of the existing window
	#syntax; curses.newwin(height, width, x-cord, y-cord)
	new_window=curses.newwin(4,100,10,10)


	stdscr.addstr("This is the old window")
	stdscr.refresh()
	i=0


	while(i!=100):

		new_window.clear() #here instead of stdscr we use the new_window
		color=curses.color_pair(2)
		new_window.border()

		if i%2 == 0:
			color=curses.color_pair(1) #if i is divisible by two color changes to white and red

		new_window.addstr(1,1,"this is in new window")

		new_window.addstr(2,1,f"\nCount : {i}",color) #formatted output or f string
		new_window.refresh() #to clear the screen after every output
		time.sleep(0.1)
		i=i+1

		
	
	stdscr.getch()


wrapper(main)