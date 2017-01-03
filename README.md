# imdb-data-visualizations
A series of data visualizations a created with the kaggle imdb dataset

### Visualizations 

I created the following visualizations using python and javascript. For javascript I used d3.js (version 3),
and for python I used pandas, numpy, and sci-kit-learn:

- Bivariate Scatterplot
- Correlation Matrix
- 5x5 Scatterplot Matrix
- Parallel Coordinates
- PCA plot (and associated scree plot)
- Biplot
- MDS display of the data points
- MDS display of the data attributes

### Viewing the data

Due to google chrome's cross-origin policy, viewing the visualizations is slightly
harder than just downloading them and opening in chrome. However, if you have python installed,
it is still easy. Simply open up a terminal and type in the following:

If you are on windows,

```
python -m http.server 8000
```

on linux,

```
python -m SimpleHTTPServer 8000
```

Then, check your localhost:8000 and the visualizations should be there.

