import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

## import data

my_csv = '../final_reduced_data.csv' ## path to your dataset

dat = pd.read_csv(my_csv, index_col=0)
# if no row or column titles in your csv, pass 'header=None' into read_csv
# and delete 'index_col=0' -- but your biplot will be clearer with row/col names

## perform PCA

n = len(dat.columns)

pca = PCA(n_components = n)
# defaults number of PCs to number of columns in imported data (ie number of
# features), but can be set to any integer less than or equal to that value

pca.fit(dat)

## project data into PC space

# 0,1 denote PC1 and PC2; change values for other PCs
xvector = pca.components_[0] # see 'prcomp(my_data)$rotation' in R
yvector = pca.components_[1]

xs = pca.transform(dat)[:,0] # see 'prcomp(my_data)$x' in R
ys = pca.transform(dat)[:,1]

vectors = [];

for i in range(len(xvector)):
	vectors.append([xvector[i] * max(xs),yvector[i]*max(ys)]);

points = [];

for i in range(len(xs)):
    points.append([xs[i], ys[i]]);

labels = list(dat.columns.values)

np.savetxt("biplot_points.csv",points,'%5.2f',delimiter=',')
np.savetxt("biplot_vectors.csv",vectors,'%5.2f',delimiter=',')
np.savetxt("component_labels.csv",labels,'%s',delimiter=',')