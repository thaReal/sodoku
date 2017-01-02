from Tkinter import *

class DebugWindow(Toplevel):
	def __init__(self, parent):
		Toplevel.__init__(self, parent)
		self.parent = parent
		self.frame = Frame(self, bg="#5c3566")
		self.initialize()
		
	def initialize(self):
		#self.seperator = Frame(self, height=2, bg="black")
		#self.seperator.grid(column=0, row=1, columnspan=3, sticky="WE")
		
		self.validate_btn = Button(self, text="Validate")
		self.validate_btn.grid(column=0, row=0, padx=5, pady=5)
		
		self.stepsolve_btn = Button(self, text="Initialize Ssolver")
		self.stepsolve_btn.grid(column=0, row=1, columnspan=2, padx=5, pady=5)
		
		step_lbl = Label(self, text="Step Options:", justify='center')
		step_lbl.grid(column=0, row=2, columnspan=3)
		
		self.step_btn = Button(self, text="1x", state="disabled")
		self.step_btn.grid(column=0, row=3, padx=5, pady=5)
		
		self.mstep_btn = Button(self, text="100x", state="disabled")
		self.mstep_btn.grid(column=0, row=4, padx=5, pady=5)
		
		self.mstep2_btn = Button(self, text="1000x", state="disabled")
		self.mstep2_btn.grid(column=0, row=5, padx=5, pady=5)
		
		self.display_btn = Button(self, text="Display", state="disabled")
		self.display_btn.grid(column=0, row=6, padx=5, pady=5)
		
		self.run_btn = Button(self, text="Run", state="disabled")
		self.run_btn.grid(column=0, row=7, padx=5, pady=5)
		
		
	def step_solver_init(self):
		self.step_btn['state'] = 'normal'
		self.step_btn['command'] = self.parent.step
		
		self.display_btn['state'] = 'normal'
		self.display_btn['command'] = self.parent.stepsolver.pSolution.debugPrint
		
		self.debug_window.mstep_btn['state'] = 'normal'
		self.debug_window.mstep_btn['command'] = self.parent.multistep
		
		self.debug_window.mstep2_btn['state'] = 'normal'
		self.debug_window.mstep2_btn['command'] = self.parent.multistep2
		
		self.debug_window.run_btn['state'] = 'normal'
		self.debug_window.run_btn['command'] = self.parent.run
		

