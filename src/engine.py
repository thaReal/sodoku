from Tkinter import *
import ui_puzzle
import ui_interface

def main():
	root = Tk()
	root.title("Sodoku Solver")
	
	puzzleframe = ui_puzzle.PuzzleFrame(root)
	controlframe = ui_interface.ControlFrame(root)
	controlframe.pack(expand=1, fill=BOTH, anchor='s')
	controlframe.solve_btn["command"] = puzzleframe.extractPuzzle
	
	filemenu = ui_interface.FileMenu(root)
	root.config(menu=filemenu)
	
	root.mainloop()	
	
	
if __name__=='__main__':
	main()
