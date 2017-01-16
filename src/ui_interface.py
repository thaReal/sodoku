from Tkinter import *
import util

class ControlFrame(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initialize()
		
	def initialize(self):
		self.solve_btn = Button(self, text="Solve")
		self.solve_btn.grid(column=0, row=0, padx=5, pady=5)
		
		self.clear_btn = Button(self, text="Clear", command=self.clearPuzzle)
		self.clear_btn.grid(column=1, row=0, padx=5, pady=5)
		
		self.quit_btn = Button(self, text="Quit", command=self.parent.destroy)
		self.quit_btn.grid(column=2, row=0, padx=5, pady=5)
		
	def clearPuzzle(self):
		self.parent.puzzleframe.clearPuzzle()
		
		
		
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
		
		
		
class FileMenu(Menu):
	def __init__(self, parent):
		Menu.__init__(self, parent)
		self.parent = parent
		self.initialize()
		
	def initialize(self):
		self.filemenu = Menu(self, tearoff=0)	
		self.filemenu.add_command(label="Settings", command=self.settingsDialog)
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

	def settingsDialog(self):
		self.settings = SettingsWindow(self.parent)



class LoadWindow(Toplevel):
	def __init__(self, parent):
		Toplevel.__init__(self, parent)
		self.parent = parent
		self.title("Load Puzzle")
		self.initialize()
		
	def initialize(self):
		self.mainframe = Frame(self)
		self.mainframe.pack()
		
		lbl = Label(self.mainframe, text="Select file to load:", justify=LEFT)
		lbl.pack(expand=1, fill=X)
		
		scrollbar = Scrollbar(self.mainframe)
		scrollbar.pack(side=RIGHT, fill=Y)
		
		self.puzzle_list = util.list_puzzles()
		self.puzzle_box = Listbox(self.mainframe)
		for  f in self.puzzle_list:
			self.puzzle_box.insert(0, f)
		self.puzzle_box.pack(expand=1, fill=Y)
		
		scrollbar.config(command=self.puzzle_box.yview)
		
		self.ok_btn = Button(self.mainframe, text="Ok", command=self.loadFile)
		self.ok_btn.pack(padx=5, pady=5, side=LEFT)
		
		self.rename_btn = Button(self.mainframe, text="Rename",
		command=self.rename_file)
		
		self.cancel_btn = Button(self.mainframe, text="Cancel", 
		command=self.destroy)
		self.cancel_btn.pack(padx=5, pady=5, side=LEFT)
		
	def rename_file(self):
		pass
		
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
		self.text.set("Ready")
		self.initialize()
	
	def initialize(self):
		lbl = Label(self, text="<Status>: ")
		lbl.grid(column=0, row=0, sticky='w', padx=5) 
		
		self.status_label = Label(self, textvar=self.text, fg="Green")
		self.status_label.grid(column=1, row=0, sticky='w')


	def set_status_running(self):
		self.text.set("Running...")
		

class SettingsWindow(Toplevel):
	def __init__(self, parent):
		Toplevel.__init__(self, parent)
		self.parent = parent
		self.debugMode = IntVar()
		self.autosave = IntVar()
		self.debug_on = False
		
		self.initialize()
		
	def initialize(self):
		self.frame = Frame(self, bg="#204a87")
		self.frame.pack(expand=1, fill=BOTH)
		
		title_lbl = Label(self.frame, text="Settings", justify='center', relief=RAISED,
		borderwidth=3)
		title_lbl.grid(column=0, row=0, columnspan=3, padx=5, pady=5, ipadx=5, 
		sticky="NWE")
		
		debug_lbl = Label(self.frame, text="Debug Mode: ")
		debug_lbl.grid(column=0, row=1, padx=5, pady=5, sticky="NW")
		
		debug_on = Radiobutton(self.frame, text="On", variable=self.debugMode,
		value=1)
		debug_on.grid(column=1, row=1, padx=2, pady=5, sticky="NW")
		
		debug_off = Radiobutton(self.frame, text="Off", variable=self.debugMode,
		value=0)
		debug_off.grid(column=2, row=1, padx=2, pady=5, sticky="NW")
		
		autosave_lbl = Label(self.frame, text="Autosave\nSolution: ")
		autosave_lbl.grid(column=0, row=2, padx=5, pady=5, sticky="NW")
		
		autosave_on = Radiobutton(self.frame, text="On", variable=self.autosave,
		value=1, command=self.select_autosave)
		autosave_on.grid(column=1, row=2, padx=2, pady=5, sticky="NW")
		
		autosave_off = Radiobutton(self.frame, text="Off", variable=self.autosave,
		value=0, command=self.select_autosave)
		autosave_off.grid(column=2, row=2, padx=2, pady=5, sticky="NW")
		
		buttonframe = Frame(self.frame)
		buttonframe.grid(column=0, row=3, columnspan=3, sticky="SWE")
		
		ok_btn = Button(buttonframe, text="Ok", command=self.ok_press)
		ok_btn.grid(column=0, row=0, padx=5)
		
		cancel_btn = Button(buttonframe, text="Cancel", command=self.cancel_press)
		cancel_btn.grid(column=1, row=0, padx=5)
		
	def select_autosave(self):
		pass
				
	def ok_press(self):
		if self.debug_on == False and self.debugMode.get() == 1:
			print "Launch Debug Window"
			self.debug_on = True
			self.parent.launch_debug()
			self.destroy()
			
		elif self.debug_on == True and self.debugMode.get() == 0:
			print "Destroy debug window"
			self.debug_on = False
			# code to destroy window here
			self.destroy()
		
		else:
			self.destroy()
		
	def cancel_press(self):
		self.destroy()
		
	def launch_debug(self):
		pass
		
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
