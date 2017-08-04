import os
from os.path import expanduser
home_path = expanduser("~")
import csv 

class CaseWriter(object):
	def write_test_case(self, filename):
		with open(filename+'.csv', 'wb') as writecsv:
    		writer = csv.writer(writecsv)
    		writer.writerow(["Test case id", "Test cases", "Priority", "Preconditions", "Input test data", "Steps to be executed", "Expected results", "Actual results", "Pass/Fail", "Comments"])
    		writer.writeheader()
