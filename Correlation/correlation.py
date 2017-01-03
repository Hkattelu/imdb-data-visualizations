import numpy as numpy
import csv

#Load in the dataset as a 2d array for convenience
data = [];
file = open('correlations.csv');
for line in file:
	data.append(line.strip().split(','));

for row in data:
	val = 0;
	for col in row:
		val += float(col);
	print(val);
