#Sodoku Solver Engine

class Solver:
	def __init__(self, puzzle):
		self.puzzle = puzzle
		self.rows = []
		self.columns = []
		self.boxes = []
		
	def check_puzzle(self):
		if len(self.puzzle) != 9:
			return False
		
		for row in self.puzzle:
			if len(row) != 9:
				return False
			self.rows.append(row)
			
		for i in range(9):
			col = []
			for row in self.rows:
				col.append(row[i])
			self.columns.append(col)
			
		for j in range(9):
			i = 0
			box = []
			for n in range(9):
				if i == 3:
					j += 1
					i = 0
				val = self.rows[j][i]
				box.append(val)
			self.boxes.append(box)			 
			
		self.debugPrint()
		return True

	def debugPrint(self):
		print "Rows:"
		for r in self.rows:
			print r
		print "\nColumns:"
		for c in self.columns:
			print c	


if __name__=='__main__':
	pass
