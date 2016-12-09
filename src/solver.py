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
			
		# Still need to populate boxes...
		
		return True

	def debugPrint(self):
		print "Rows:"
		for r in self.rows:
			print r
		print "\nColumns:"
		for c in self.columns:
			print c	

if __name__=='__main__'
	pass
