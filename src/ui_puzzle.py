from Tkinter import *

class PuzzleFrame(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, bg="#555753")
		self.parent = parent
		self.cells = {}
		self.boxes = []
		
		self.initialize()
		self.pack(expand=1, fill=BOTH)
	
		
	def initialize(self):
		for x in range(3):
			for y in range(3):
				self.makeBox(x, y)
	
	
	def makeBox(self, c, r):
		boxframe = Frame(self)
		for x in range(3):
			for y in range(3):
				value = StringVar()
				cell = Entry(boxframe, textvar=value, width=2)
				cell.grid(column=x, row=y, padx=1, pady=1)
				cell.bind('<KeyRelease>', self.checkInput)
				self.cells[cell] = value
				
		boxframe.grid(column=c, row=r, padx=2, pady=2)
		self.boxes.append(boxframe)		
					
	def checkInput(self, event):
		textvar = self.cells[event.widget]
		value  = textvar.get()
			
		if len(value) > 1:
			c = value[-1]
			textvar.set(c)
		
		# TODO: Add error checking for char vs. num input
		
	def extractPuzzle(self):
		puzzle = []
		for i in range(9):
			blank_row = []
			for j in range(9):
				blank_row.append('')
			puzzle.append(blank_row)
				
		for cell in self.cells.keys():
			c_mult = cell.grid_info()['in'].grid_info()['column']
			r_mult = cell.grid_info()['in'].grid_info()['row']
			c = cell.grid_info()['column']
			r = cell.grid_info()['row']
			
			row = (r_mult*3) + r
			col = (c_mult*3) + c 
			
			value = self.cells[cell].get()
			
			if value != '':
				puzzle[int(row)][int(col)] = value
				# print "%s, %s - %s" % (row, col, value) # DEBUG
				
		return puzzle
		
		
	def clearPuzzle(self):
		for cell in self.cells.keys():
			self.cells[cell].set('')
			
		
	def inputPuzzle(self, puzzle):
		self.clearPuzzle()
		i = 0
		for row in puzzle:
			j = 0
			for val in row:
				if val != '':
					outer_row = int(i/3)
					outer_col = int(j/3)
					inner_row = i % 3
					inner_col = j % 3
					
					box = self.grid_slaves(outer_row, outer_col)
					cell = box[0].grid_slaves(inner_row, inner_col)
					#print cell
					self.cells[cell[0]].set(str(val))
				j += 1
			i += 1
			
			
			
if __name__=='__main__':
	root = Tk()
	root.title("Sodoku Solver")
	app = PuzzleFrame(root)
	app.mainloop()
