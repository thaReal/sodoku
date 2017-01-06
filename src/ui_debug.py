from Tkinter import *

class DebugWindow(Toplevel):
	def __init__(self, parent):
		Toplevel.__init__(self, parent, bg="#204a87")
		self.parent = parent
		self.title("Debug")
		self.initialize()

		
	def initialize(self):
		self.validate_btn = Button(self, text="Validate")
		self.validate_btn.grid(column=0, row=0, padx=5, pady=5, sticky="W")
		
		self.stepsolve_btn = Button(self, text="Initialize")
		self.stepsolve_btn.grid(column=0, row=1, columnspan=2, padx=5, pady=5,
		sticky="W")
		
		seperator = Frame(self, height=2, bg="black")
		seperator.grid(column=0, row=2, columnspan=3, sticky="WE")
		
		step_lbl = Label(self, text="Step Options:", justify='center')
		step_lbl.grid(column=0, row=3, columnspan=3, padx=5, pady=5, sticky="W")
		
		self.step_btn = Button(self, text="1x", state="disabled")
		self.step_btn.grid(column=0, row=4, padx=5, pady=5, sticky="W")
		
		self.mstep_btn = Button(self, text="100x", state="disabled")
		self.mstep_btn.grid(column=0, row=5, padx=5, pady=5, sticky="W")
		
		self.mstep2_btn = Button(self, text="1000x", state="disabled")
		self.mstep2_btn.grid(column=0, row=6, padx=5, pady=5, sticky="W")
		
		seperator = Frame(self, height=2, bg="black")
		seperator.grid(column=0, row=7, columnspan=3, sticky="WE")
		
		self.display_btn = Button(self, text="Display", state="disabled")
		self.display_btn.grid(column=0, row=8, padx=5, pady=5, sticky="W")
		
		self.run_btn = Button(self, text="Run", state="disabled")
		self.run_btn.grid(column=0, row=9, padx=5, pady=5, sticky="W")
		
		self.calc_btn = Button(self, text="Calculate", state="disabled")
		self.calc_btn.grid(column=0, row=10, padx=5, pady=5, sticky="W")
		
		
	def step_solver_init(self):
		self.step_btn['state'] = 'normal'
		self.step_btn['command'] = self.parent.step
		
		self.display_btn['state'] = 'normal'
		self.display_btn['command'] = self.parent.stepsolver.pSolution.debugPrint
		
		self.mstep_btn['state'] = 'normal'
		self.mstep_btn['command'] = self.parent.multistep
		
		self.mstep2_btn['state'] = 'normal'
		self.mstep2_btn['command'] = self.parent.multistep2
		
		self.run_btn['state'] = 'normal'
		self.run_btn['command'] = self.parent.run
		
		self.calc_btn['state'] = 'normal'
		self.calc_btn['command'] = self.parent.calc_possibilities
		

