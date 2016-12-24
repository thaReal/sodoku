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
		self.controlframe.pack(expand=1, fill=BOTH)
		
		self.controlframe.solve_btn["command"] = self.solvePuzzle
		self.controlframe.validate_btn["command"] = self.debugValidate
		self.controlframe.stepsolve_btn["command"] = self.stepSolverInit
		
		self.statusbar = ui_interface.StatusBar(self)
		self.statusbar.pack(expand=1, fill=X, anchor='s')
		
		self.filemenu = ui_interface.FileMenu(self)
		self.config(menu=self.filemenu)
	
		self.mainloop()
		
	def loadPuzzle(self, puzzle):
		self.puzzleframe.inputPuzzle(puzzle)

	def solvePuzzle(self):
		raw_puzzle = self.puzzleframe.extractPuzzle()
		print "[+] Solver Starting"
		
		#puzzle = solver.Puzzle(raw_puzzle)
		#sl = solver.Solver(puzzle)
		#sl.generate_solution_space()
		
		print "[+] Solver Finished"

	def stepSolverInit(self):
		raw_puzzle = self.puzzleframe.extractPuzzle()
		self.stepsolver = solver.StepSolver(raw_puzzle)
		
		self.controlframe.step_btn['state'] = 'normal'
		self.controlframe.step_btn['command'] = self.stepsolver.step
		
		self.controlframe.display_btn['state'] = 'normal'
		self.controlframe.display_btn['command'] = self.stepsolver.pSolution.debugPrint
		
		self.controlframe.mstep_btn['state'] = 'normal'
		self.controlframe.mstep_btn['command'] = self.multistep
		
		self.controlframe.mstep2_btn['state'] = 'normal'
		self.controlframe.mstep2_btn['command'] = self.multistep2
		
		self.controlframe.run_btn['state'] = 'normal'
		self.controlframe.run_btn['command'] = self.run
		
	def debugValidate(self):
		raw_puzzle = self.puzzleframe.extractPuzzle()
		puzzle = solver.Puzzle(raw_puzzle)
		puzzle.debugPrint()
		print "[+] Done!"
		
	def multistep(self):
		self.stepsolver.multistep(100)
		
	def multistep2(self):
		self.stepsolver.multistep(1000)
		
	def run(self):
		self.stepsolver.run()
	
if __name__=='__main__':
	app = App()
