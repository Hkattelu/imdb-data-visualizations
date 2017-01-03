import pandas as pandas
from sklearn import manifold
import numpy

data = pandas.read_csv("../final_reduced_data.csv");

mds = manifold.MDS(n_components = 2)

transformed_data = mds.fit(data).embedding_

numpy.savetxt("mds_data.csv",transformed_data,'%5.2f',delimiter=',')

