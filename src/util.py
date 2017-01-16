# Sodoku Solver Utility Functions

import csv
import time
import os

puzzledir = "./puzzles/"

def csv2puzzle(fname):
	fname2 = puzzledir + fname
	f = open(fname2, 'r')
	reader = csv.reader(f)
	
	puzzle = []
	for row in reader:
		puzzle.append(row)
	f.close()
	
	return puzzle
		
		
def puzzle2csv(puzzle):
	name = generate_fname()
	fname = puzzledir + name + ".csv"
	f = open(fname, 'w')
	
	csv_writer = csv.writer(f)
	for row in puzzle:
		csv_writer.writerow(row)
		
	f.close()
	print "%s sucessfully saved!" % fname
	
	
def generate_fname():
	# For now just going to use the time so at least each filename should be unique
	t = time.ctime()
	tlist = t.split(' ')
	fname = tlist[1] + '-' + tlist[3] + '-' + tlist[5] + '-' + tlist[4]
	return fname
	

def list_puzzles():
	cwd = os.getcwd()
	puzzledir = cwd + '/puzzles/'
	puzzle_list = os.listdir(puzzledir)
	
	return puzzle_list
	
	
