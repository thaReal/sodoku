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
			print "[-] Failed raw puzzle check"
			return
		
		self.populate()
		
		if check_puzzle(self) != True:
			self.valid = False
			print "[-] Failed global puzzle check"
			return
		
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
			i_row = []
			for i in row:
				try:
					i_row.append(int(i))
				except:
					i_row.append(i)
					
			self.rows.append(i_row)
		
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
	
	def repopulate(self):
		self.columns = []
		for i in range(9):
			col = []
			for row in self.rows:
				col.append(row[i])
			self.columns.append(col)
		
		self.boxes = []
		for j in range(3):
			for i in range(3):
				box = []
				for k in range(9):
					x = (k % 3) + (i * 3)
					y = int(k / 3) + (j * 3)
					cell = self.rows[y][x]
					box.append(cell)
				self.boxes.append(box)
	
	# Maybe...?
	def regenerate(self, i):
		x0 = (i % 3) * 3
		y0 = int(i / 3) * 3
		n = 0
		for j in range(3):
			x = x0 + j
			for k in range(3):
				y = y0 + k
				self.rows[y][x] = self.boxes[i][n]
				self.columns[x][y] = self.boxes[i][n]
				n += 1
		self.debugPrint()
	
	# This class needs to be updated - either just print the rows (so it looks like a 
	# regular puzzle, or use __str__  / __repr()__ 
	
	def debugPrint(self):
		for r in self.rows:
			print r
		print ''
		
		'''
		for c in self.columns:
			print c
		print ""
		
		for b in self.boxes:
			print b
		print ""
		'''
		
class Guess:
	def __init__(self, row):
		self.row = row
		self.numbers = [1,2,3,4,5,6,7,8,9]
		self.create_pnumbers()
		self.generate_permutations()
		
	def create_pnumbers(self):
		for i in self.row:
			try:
				index = self.numbers.index(int(i))
				self.numbers.pop(index)
								
			except:
				pass		

	def generate_permutations(self):
		l = len(self.numbers)
		self.p = permutations(self.numbers, l)

	def get_permutation(self):
		try:
			iteration = self.p.next()
			return iteration
		except:
			return None

	def get_possibilities(self):
		l = len(self.numbers)
		n = factorial(l)
		return n			

	def make_attempt(self, p):
		row = []
		count = 0
		for i in self.row:
			if i == '':
				value = p[count]
				count += 1
				row.append(value)
			else:
				row.append(i)
				
		return row
#-----
		
class Box:
	def __init__(self, box):
		self.box = box
		self.numbers = [1,2,3,4,5,6,7,8,9]
		self.create_pnumbers()
		self.generate_permutations()	
			
	def create_pnumbers(self):
		for i in self.box:
			try:
				index = self.numbers.index(int(i))
				self.numbers.pop(index)
								
			except:
				pass
				
	def get_possibilities(self):
		l = len(self.numbers)
		n = factorial(l)
		return n
	
	def generate_permutations(self):
		l = len(self.numbers)
		self.p = permutations(self.numbers, l)
		

	def get_permutation(self):
		try:
			iteration = self.p.next()
			return iteration
			
		except:
			return None
			
	def fill_box(self, p):
		box = []
		count = 0
		for i in self.box:
			if i == '':
				value = p[count]
				count += 1
				box.append(value)
			else:
				box.append(i)
				
		return box
				
		
		
class Solver:
	def __init__(self, puzzle):
		self.puzzle = puzzle
	
	def count_perms(self):
		n = 0
		for i in range(9):
			box = Box(self.puzzle.boxes[i])
			if n == 0:
				n += box.get_possibilities()
			else:
				n *= box.get_possibilities()
		print "  > %s total possibilities" % n

	# This is gonna be a little rocky for a while...
	def generate_solution_space(self):
			puzzle = self.puzzle
			i = 0
			n = 0
			boxes = []
			for x in range(9):
				box = Box(self.puzzle.boxes[x])
				boxes.append(box)
			# print boxes[0].get_possibilities()
			
			while i < 8:
				p = boxes[i].get_permutation()
				if p == None:
					if i == 0:
						break
					else:
						i -= 1
				
				else:
					print boxes[i].fill_box(p)
					puzzle.boxes[i] = boxes[i].fill_box(p)
					puzzle.regenerate(i)
					result = check_puzzle(puzzle)
					print result
					
					if check_puzzle(puzzle) == True:
						i += 1
						print " >> i = %s" % i
						n += 1
			
					else:
						print "Iteration %s, INVALID" % n
						puzzle.boxes[i] = self.puzzle.boxes[i]
						n += 1
			
			
class StepSolver:
	def __init__(self, rawpuzzle):
		self.puzzle = Puzzle(rawpuzzle)
		self.initialize()
		
	def initialize(self):
		self.pSolution = Puzzle(self.puzzle.rows)
		self.i = 0
		self.n = 0
		self.guesses = []
		for x in range(9):
			guess = Guess(self.puzzle.rows[x])
			self.guesses.append(guess)
		
	def step(self):
		print "step fired"
		if self.i < 8:
				p = self.guesses[self.i].get_permutation()
				if p == None:
					if i == 0:
						print "No guesses.."
						return
					else:
						i -= 1
				
				else:
					# Here's where (at least I know) code is breaking down
					
					self.pSolution.rows[self.i] = self.guesses[self.i].make_attempt(p)
					self.pSolution.repopulate()
					
					# DEBUG
					# result = check_puzzle(self.pSolution)
					# print result
					
					if check_puzzle(self.pSolution) == True:
						self.i += 1
						print "Iteration %s, VALID" % self.n
						print " >> i = %s" % self.i
						self.n += 1
			
					else:
						print "Iteration %s, INVALID" % self.n
						self.pSolution.rows[self.i] = self.puzzle.rows[self.i]
						self.pSolution.repopulate()
						self.n += 1
		else:
			return

def check_puzzle(puzzle):
	for row in puzzle.rows:
		nrow = clean_blanks(row)
		if len(nrow) != 0:
			if len(nrow) != len(set(nrow)):	
				print ">>> Row check failed"
				print nrow
				print "%s : %s" % (len(nrow), len(set(nrow)))
				return False
			
	for col in puzzle.columns:
		ncol = clean_blanks(col)
		if len(ncol) != 0:
			if len(ncol) != len(set(ncol)):
				print ">>> Column check failed"
				return False
			
	for box in puzzle.boxes:
		nbox = clean_blanks(box)
		if len(nbox) != 0:
			if len(nbox) != len(set(nbox)):
				print ">>> Box check failed"
				return False
				
	return True
				
				
def clean_blanks(plist):
	clean_list = []
	for x in plist:
		 if x != '':
		 	clean_list.append(x)
		
	return clean_list
	
	
	
if __name__=='__main__':
	pass
