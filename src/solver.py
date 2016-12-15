#Sodoku Solver Engine
from math import factorial
from itertools import permutations

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
			
		for j in range(3):
			for i in range(3):
				box = []
				for k in range(9):
					x = (k % 3) + (i * 3)
					y = int(k / 3) + (j * 3)
					cell = self.rows[y][x]
					box.append(cell)
				self.boxes.append(box)
			
		self.debugPrint()
		
		
	def debugPrint(self):
		print "Rows:"
		for r in self.rows:
			print r
		
		print "\nColumns:"
		for c in self.columns:
			print c	

		print "\nBoxes:"
		for b in self.boxes:
			print b
			
		print "\nBrute force # of possibilites: %s\n" % self.calc_possibilities()


	def calc_possibilities(self):
		n = 0
		p = 0
		for box in self.boxes:
			for cell in box:
				if cell != '':
					n += 1
			if p == 0:
				p += factorial(n)
			else:
				p = p * factorial(n)
			n = 0
		
		return p


class BFSB_Engine:
	def __init__(self, box):
		self.box = box
		self.numbers = [1,2,3,4,5,6,7,8,9]
		self.given = {}

		self.create_pnumbers()
		self.count_permutations()

	def create_pnumbers(self):
		for i in self.box:
			try:
				index = self.numbers.index(i)
				value = self.numbers.pop(index)
				self.given[index] = value
			except:
				pass
				
	def count_permutations(self):
		p = permutations(self.numbers, 9)
		count = 0
		while True:
			try:
				iteration = p.next()
				count += 1
			except:
				break
		
		if count % 1000 == 0:
			print " > %s permutations generated" % count

		print "[+] %s total permuations generated" % count
		
		
def runBFSB(box):
	bfsb = BFSB_Engine(box)

if __name__=='__main__':
	pass
