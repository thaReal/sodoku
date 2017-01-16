from math import factorial
from itertools import permutations
import multiprocessing

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
	
	def debugPrint(self):
		for r in self.rows:
			print r
		print ''


class MultiSolver:
	def __init__(self, puzzle):
		self.puzzle = puzzle
		self.valid_possibilities = []
		self.initialize()
		
	def initialize(self):
		pass
	
	def check_row_1(self, row):
		guess = row_guesses.get_permutation()
		while guess != None:
			row_guesses.make_attempt(guess)
		
		
	
