from Tkinter import *
import ui_puzzle
import ui_interface
import util

class App(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title("Sodoku Solver")
		self.initialize()
		
	def initialize(self):
		self.puzzleframe = ui_puzzle.PuzzleFrame(self)
		self.controlframe = ui_interface.ControlFrame(self)
		self.controlframe.pack(expand=1, fill=BOTH, anchor='s')
		self.controlframe.solve_btn["command"] = self.puzzleframe.extractPuzzle
		
		self.filemenu = ui_interface.FileMenu(self)
		self.config(menu=self.filemenu)
	
		self.mainloop()
		

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
	app = App()
