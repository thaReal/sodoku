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
		
		self.statusbar = ui_interface.StatusBar(self)
		self.statusbar.pack(expand=1, fill=X, anchor='s')
		
		self.filemenu = ui_interface.FileMenu(self)
		self.config(menu=self.filemenu)
	
		self.mainloop()
		
	def loadPuzzle(self, puzzle):
		self.puzzleframe.inputPuzzle(puzzle)

	def solvePuzzle(self):
		raw_puzzle = self.puzzleframe.extractPuzzle()

	def stepSolverInit(self):
		raw_puzzle = self.puzzleframe.extractPuzzle()
		self.stepsolver = solver.StepSolver(raw_puzzle)
		
		self.debug_window.step_btn['state'] = 'normal'
		self.debug_window.step_btn['command'] = self.stepsolver.step
		
		self.debug_window.display_btn['state'] = 'normal'
		self.debug_window.display_btn['command'] = self.stepsolver.pSolution.debugPrint
		
		self.debug_window.mstep_btn['state'] = 'normal'
		self.debug_window.mstep_btn['command'] = self.multistep
		
		self.debug_window.mstep2_btn['state'] = 'normal'
		self.debug_window.mstep2_btn['command'] = self.multistep2
		
		self.debug_window.run_btn['state'] = 'normal'
		self.debug_window.run_btn['command'] = self.run
		
	def debugValidate(self):
		raw_puzzle = self.puzzleframe.extractPuzzle()
		puzzle = solver.Puzzle(raw_puzzle)
		puzzle.debugPrint()
		print "[+] Done!"
		
	def step(self):
		self.stepsolver.step()
		
	def multistep(self):
		self.stepsolver.multistep(100)
		
	def multistep2(self):
		self.stepsolver.multistep(1000)
		
	def run(self):
		self.stepsolver.run()

	def launch_debug(self):
		self.debug_window = ui_interface.DebugWindow(self)
		self.debug_window.validate_btn["command"] = self.debugValidate
		self.debug_window.stepsolve_btn["command"] = self.stepSolverInit
	
if __name__=='__main__':
	app = App()
