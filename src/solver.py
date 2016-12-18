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
		#self.debugPrint()
		print "[+] Puzzle valid & populated!"
		
		
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


class Box:
	def __init__(self, box):
		self.box = box
		self.numbers = [1,2,3,4,5,6,7,8,9]
		self.create_pnumbers()
		
	def create_pnumbers(self):
		for i in self.box:
			try:
				index = self.numbers.index(int(i))
				value = self.numbers.pop(index)
								
			except:
				pass
				
	def get_possibilities(self):
		l = len(self.numbers)
		n = factorial(l)
		return n
		
		
class Solver:
	def __init__(self, puzzle):
		self.puzzle = puzzle
	
	def count_perms(self):
		n = 0
		for i in range(9):
			box = Box(self.puzzle.boxes[i])
			# print box.get_possibilities()
			if n == 0:
				n += box.get_possibilities()
			else:
				n *= box.get_possibilities()
		
		print "  > %s total possibilities" % n

			
def check_puzzle(puzzle):
	for row in puzzle.rows:
		if len(row) != len(set(row)):
			return False
			
	for col in puzzle.columns:
		if len(col) != len(set(col)):
			return False
			
	for box in puzzle.boxes:
		if len(box) != len(set(box)):
			return False
				
	return True
				

'''
	# Reference
	def count_permutations(self):
		l = len(self.numbers)
		print "[+] %s unknown numbers" % l
		
		p = permutations(self.numbers, l)
		count = 0
		plist = []
		
		while True:
			try:
				iteration = p.next()
				count += 1
				plist.append(iteration)
				
			except:
				break
		
		return plist
	'''
	
	
	
if __name__=='__main__':
	pass
