# Sodoku Solver Utility Functions
import csv

def csv2puzzle(fname):
	f = open(fname, 'r')
	reader = csv.reader(f)
	
	puzzle = []
	for row in reader:
		puzzle.append(row)
	f.close()
	
	return puzzle
		
		
def puzzle2csv(puzzle, fname):
	pass
