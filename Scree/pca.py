import numpy as numpy
import pandas as pandas
from sklearn.decomposition import PCA
import csv as csv


data = pandas.read_csv("../final_reduced_data.csv");
pca = PCA()
pca.fit(data)

explained_variance = pca.explained_variance_ratio_

eigenvalues = open("eigenvalues.csv",'w')
writer_1 = csv.writer(eigenvalues)
writer_1.writerow(explained_variance)

pca_top2 = PCA(n_components = 2)
rotated_points = pca_top2.fit_transform(data)

components = open("components.csv",'w')
writer_2 = csv.writer(components)
for row in rotated_points:
	writer_2.writerow(row)
