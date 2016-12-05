from Tkinter import *

class ControlFrame(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initialize()
		
	def initialize(self):
		self.solve_btn = Button(self, text="Solve")
		self.solve_btn.grid(column=0, row=0, padx=5, pady=5, sticky="NW")
		
		self.quit_btn = Button(self, text="Quit", command=self.parent.destroy)
		self.quit_btn.grid(column=1, row=0, padx=5, pady=5, sticky="NE")
		
		
class FileMenu(Menu):
	def __init__(self, parent):
		Menu.__init__(self, parent)
		self.parent = parent
		self.initialize()
		
	def initialize(self):
		self.filemenu = Menu(self, tearoff=0)	
		self.filemenu.add_command(label="Settings", command=self.dummy)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Save Puzzle", command=self.dummy)
		self.filemenu.add_command(label="Load Puzzle", command=self.dummy)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Quit", command=self.parent.quit)
		self.add_cascade(label="File", menu=self.filemenu)
		
		self.helpmenu = Menu(self, tearoff=0)
		self.helpmenu.add_command(label="About", command=self.dummy)
		self.add_cascade(label="Help", menu = self.helpmenu)
		
		
	def dummy(self):
		pass
		
		
class AboutDialog(Tk):
	def __init__(self, parent):
		Tk.__init__(self, parent)
		self.parent = parent
		self.initialize()
		
	def initialize(self):
		pass
		
		

if __name__=='__main__':
	root = Tk()
	app = ControlFrame(root)
	app.pack(expand=1, fill=BOTH)
	app.mainloop()
