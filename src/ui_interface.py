from Tkinter import *
import util

class ControlFrame(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initialize()
		
	def initialize(self):
		self.solve_btn = Button(self, text="Solve")
		self.solve_btn.grid(column=0, row=0, padx=5, pady=5, sticky="W")
		
		self.clear_btn = Button(self, text="Clear", command=self.clearPuzzle)
		self.clear_btn.grid(column=1, row=0, padx=5, pady=5, sticky="W")
		
		self.quit_btn = Button(self, text="Quit", command=self.parent.destroy)
		self.quit_btn.grid(column=2, row=0, padx=5, pady=5, sticky="W")
		
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
		print fname
		
		self.destroy()

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
