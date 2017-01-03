import pandas as pandas
from sklearn import manifold
import numpy

data = pandas.read_csv("corr_distance.csv");

mds = manifold.MDS(n_components = 2,dissimilarity="precomputed");

transformed_data = mds.fit(data).embedding_

numpy.savetxt("mds_attributes.csv",transformed_data,'%5.2f',delimiter=',')