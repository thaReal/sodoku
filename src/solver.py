#Sodoku Solver Engine

from math import factorial
from itertools import permutations

class Puzzle:
	def __init__(self, raw_puzzle):
		self.raw_puzzle = raw_puzzle
		self.rows = []
		self.columns = []
		self.boxes = []
		self.valid = True
		
		if self.check_raw_puzzle() != True:
			self.valid = False
			return
		
		self.populate()
		self.debugPrint()

		
	def check_raw_puzzle(self):
		if len(self.raw_puzzle) != 9:
			return False
		
		for row in self.raw_puzzle:
			if len(row) != 9:
				return False
		
		return True
		
		
	def populate(self):
		for row in self.raw_puzzle:
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
		
		
		
class Solver:
	def __init__(self, puzzle):
		self.puzzle = puzzle
		
		

class SB_Perm_Gen:
	def __init__(self, box):
		self.box = box
		self.numbers = [1,2,3,4,5,6,7,8,9]
		self.given = {}

		self.create_pnumbers()
		self.count_permutations()

	def create_pnumbers(self):
		for i in self.box:
			try:
				index = self.numbers.index(int(i))
				value = self.numbers.pop(index)
				self.given[index] = value
				
			except:
				pass
				
	def count_permutations(self):
		l = len(self.numbers)
		print "[+] %s unknown numbers" % l
		
		p = permutations(self.numbers, l)
		count = 0
		while True:
			try:
				iteration = p.next()
				count += 1
				if count % 1000 == 0:
					print " > %s permutations generated" % count
		
			except:
				break
		
		print "[+] %s total permuations generated" % count
		
		
		
def run(puzzle):
	pass



if __name__=='__main__':
	pass
