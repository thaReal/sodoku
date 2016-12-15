from Tkinter import *
import ui_puzzle
import ui_interface
import util
import solver

class App(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title("Sodoku Solver")
		self.initialize()
		
		
	def initialize(self):
		self.puzzleframe = ui_puzzle.PuzzleFrame(self)
		self.controlframe = ui_interface.ControlFrame(self)
		self.controlframe.pack(expand=1, fill=BOTH, anchor='s')
		self.controlframe.solve_btn["command"] = self.solvePuzzle
		
		self.filemenu = ui_interface.FileMenu(self)
		self.config(menu=self.filemenu)
	
		self.mainloop()
		
	def loadPuzzle(self, puzzle):
		self.puzzleframe.inputPuzzle(puzzle)

	def solvePuzzle(self):
		puzzle = self.puzzleframe.extractPuzzle()
		self.solver = solver.Solver(puzzle)
		self.solver.check_puzzle()
		
		box = self.solver.boxes[0]
		solver.runBFSB(box)
				
	
if __name__=='__main__':
	app = App()
