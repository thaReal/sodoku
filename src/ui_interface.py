from Tkinter import *
import util

class ControlFrame(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initialize()
		
		self.init_debug()
		
	def initialize(self):
		self.solve_btn = Button(self, text="Solve")
		self.solve_btn.grid(column=0, row=0, padx=5, pady=5)
		
		self.clear_btn = Button(self, text="Clear", command=self.clearPuzzle)
		self.clear_btn.grid(column=1, row=0, padx=5, pady=5)
		
		self.quit_btn = Button(self, text="Quit", command=self.parent.destroy)
		self.quit_btn.grid(column=2, row=0, padx=5, pady=5)
		
		
	def init_debug(self):
		self.seperator = Frame(self, height=2, bg="black")
		self.seperator.grid(column=0, row=1, columnspan=3, sticky="WE")
		
		self.validate_btn = Button(self, text="Validate")
		self.validate_btn.grid(column=0, row=2, padx=5, pady=5)
		
		self.stepsolve_btn = Button(self, text="Initialize Ssolver")
		self.stepsolve_btn.grid(column=1, row=2, columnspan=2, padx=5, pady=5)
		
		step_lbl = Label(self, text="Step Options:", justify='center')
		step_lbl.grid(column=0, row=3, columnspan=3)
		
		self.step_btn = Button(self, text="1x", state="disabled")
		self.step_btn.grid(column=0, row=4, padx=5, pady=5)
		
		self.mstep_btn = Button(self, text="100x", state="disabled")
		self.mstep_btn.grid(column=1, row=4, padx=5, pady=5)
		
		self.mstep2_btn = Button(self, text="1000x", state="disabled")
		self.mstep2_btn.grid(column=2, row=4, padx=5, pady=5)
		
		self.display_btn = Button(self, text="Display", state="disabled")
		self.display_btn.grid(column=0, row=5, padx=5, pady=5)
		
		self.run_btn = Button(self, text="Run", state="disabled")
		self.run_btn.grid(column=2, row=5, padx=5, pady=5)
		
		
	def clearPuzzle(self):
		self.parent.puzzleframe.clearPuzzle()
		
		
class FileMenu(Menu):
	def __init__(self, parent):
		Menu.__init__(self, parent)
		self.parent = parent
		self.initialize()
		
	def initialize(self):
		self.filemenu = Menu(self, tearoff=0)	
		self.filemenu.add_command(label="Settings", command=self.dummy)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Save Puzzle", command=self.savePuzzle)
		self.filemenu.add_command(label="Load Puzzle", command=self.loadPuzzle)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Quit", command=self.parent.quit)
		self.add_cascade(label="File", menu=self.filemenu)
		
		self.helpmenu = Menu(self, tearoff=0)
		self.helpmenu.add_command(label="About", command=self.aboutDialog)
		self.add_cascade(label="Help", menu = self.helpmenu)
		
		
	def dummy(self):
		pass
		
	def savePuzzle(self):
		puzzle = self.parent.puzzleframe.extractPuzzle()
		util.puzzle2csv(puzzle)
		
	def loadPuzzle(self):
		loadwindow = LoadWindow(self.parent)
		
	def aboutDialog(self):
		self.about = AboutDialog(self.parent)


class LoadWindow(Toplevel):
	def __init__(self, parent):
		Toplevel.__init__(self, parent)
		self.parent = parent
		self.initialize()
		
	def initialize(self):
		self.mainframe = Frame(self)
		self.mainframe.pack()
		
		lbl = Label(self.mainframe, text="Select file to load:", justify=LEFT)
		lbl.pack(expand=1, fill=X)
		
		self.puzzle_list = util.list_puzzles()
		self.puzzle_box = Listbox(self.mainframe)
		for  f in self.puzzle_list:
			self.puzzle_box.insert(0, f)
		self.puzzle_box.pack(expand=1, fill=X)
		
		self.ok_btn = Button(self.mainframe, text="Ok", command=self.loadFile)
		self.ok_btn.pack(padx=5, pady=5, side=LEFT)
		
		self.cancel_btn = Button(self.mainframe, text="Cancel", 
		command=self.destroy)
		self.cancel_btn.pack(padx=5, pady=5, side=LEFT)
		
		
	def loadFile(self):
		findex = self.puzzle_box.curselection()
		if len(findex) == 0:
			return
		
		fname = self.puzzle_box.get(findex)
		puzzle = util.csv2puzzle(fname)
		self.parent.loadPuzzle(puzzle)
			
		self.destroy()
		
		
class StatusBar(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, relief=SUNKEN, borderwidth=2)
		self.parent = parent
		self.text = StringVar()
		self.text.set("waiting for input...")
		self.initialize()
	
	def initialize(self):
		lbl = Label(self, text="<Status>: ")
		lbl.grid(column=0, row=0, sticky='w', padx=5) 
		
		self.status_label = Label(self, textvar=self.text, fg="Green")
		self.status_label.grid(column=1, row=0, sticky='w')

#------		
		
class AboutDialog(Toplevel):
	def __init__(self, parent):
		Toplevel.__init__(self, parent)
		self.parent = parent
		self.initialize()
		
	def initialize(self):
		self.bgframe = Frame(self, width=300, height=200, bg="green")
		self.bgframe.pack()
		

if __name__=='__main__':
	root = Tk()
	app = ControlFrame(root)
	app.pack(expand=1, fill=BOTH)
	app.mainloop()
