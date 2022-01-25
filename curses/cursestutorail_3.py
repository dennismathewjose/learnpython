
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

def main(stdscr):
	x,y = 0,0
	stdscr.nodelay(True)
	xpos = 0
	while True:
		try:
			key = stdscr.getkey()
		except:
			key=None
		
		if key == "KEY_UP":
			y-=1
		elif key == "KEY_DOWN":
			y+=1
		elif key == "KEY_LEFT":
			x-=1
		elif key == "KEY_RIGHT":
			x+=1

		stdscr.clear()
		xpos+=1
		stdscr.addstr(0, xpos//50,"Moving Text")
		stdscr.addstr(y,x,"-")
		stdscr.refresh()

		#How to draw a rectangle in curses.
		rectangle(stdscr, 1, 1, 5, 10)


wrapper(main)