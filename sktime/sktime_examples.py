"""
sktime - python toolbox for time series: how to implement your own estimator

sktime is a widely used scikit-learn compatible library for learning with time
 series. sktime is easily extensible by anyone, and interoperable with the
 pydata/numfocus stack. This tutorial explains how to write your own sktime
 estimator, e.g., forecaster, classifier, transformer, by using sktime’s
 extension templates and testing framework. A custom estimator can live in any
  local code base, and will be compatible with sktime pipelines, or
  scikit-learn. A continuation of the sktime introductory tutorial at pydata

https://www.sktime.net/en/latest/

https://london2022.pydata.org/cfp/talk/AHH8FE/

https://github.com/sktime/sktime-tutorial-pydata-london-2023
"""
import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sktime.alignment.dtw_python import AlignerDTW
from sktime.classification.distance_based import KNeighborsTimeSeriesClassifier
from sktime.clustering.dbscan import TimeSeriesDBSCAN
from sktime.datasets import load_airline, load_osuleaf, load_basic_motions, \
    load_covid_3month
from sktime.datatypes import check_is_mtype
from sktime.dists_kernels import AggrDist, ScipyDist
from sktime.dists_kernels.compose_from_align import DistFromAligner
from sktime.forecasting.naive import NaiveForecaster
from sktime.regression.distance_based import KNeighborsTimeSeriesRegressor
from sktime.transformations.series.detrend import Detrender
from sktime.utils.plotting import plot_series

data = datasets.load_diabetes()

RandomForestClassifier()

y = load_airline()

# regression example
fh = np.arange(1, 37)
forecaster = NaiveForecaster(strategy="last", sp=12)
forecaster.fit(y)
y_pred = forecaster.predict(fh)

# classification
x_train, y_train = load_osuleaf(split="test", return_type="numpy3D")
x_new, _ = load_osuleaf(split="test", return_type="numpy3D")

mean_eucl_dist = AggrDist(ScipyDist())
clf = KNeighborsTimeSeriesClassifier(n_neighbors=3, distance=mean_eucl_dist)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_new)

# panel data - sktime data formats
# pandas Dataframe with 2-level MultiIndex
# numpy 3D darray with index

"""
sklearn tabular data

sktime time series data

sktime supports and recongises mutliple data formats - dask, xarray or
abstract data type scitype 

https://github.com/sktime/sktime-tutorial-pydata-london-2023/blob/main/notebooks/02_panel_tasks.ipynb
"""
x, _ = load_osuleaf(return_type="numpy3D")
X, _ = load_basic_motions(return_type="numpy3D")
x_pd, _ = load_osuleaf(return_type="pd-multiindex")

valid, error_msg, metadata = check_is_mtype(x_pd, "pd-multiindex",
                                            return_metadata=True)
valid, error_msg, metadata = check_is_mtype(x_pd, "numpy3D",
                                            return_metadata=True)
"""
Distance based algorithims for different time series models
"""
x_train, y_train = load_osuleaf(split="train", return_type="numpy3D")
x_test, y_test = load_osuleaf(split="test", return_type="numpy3D")
x_test = x_test[:2]
y_test = y_test[:2]

mean_eucl_dist = AggrDist(ScipyDist())
clf = KNeighborsTimeSeriesClassifier(n_neighbors=3, distance=mean_eucl_dist)
clf.fit(x_train, y_train)
y_pred = clf.fit(x_test)

accuracy_score(y_test, y_pred)

# Time Series Regression - basic vignettes
X_train, y_train = load_covid_3month(split="train")
y_train = y_train.astype("float")
X_new, _ = load_covid_3month(split="test")
X_new = X_new.loc[:2]  # smaller dataset for faster notebook runtime

clf = KNeighborsTimeSeriesRegressor(n_neighbors=3, distance=mean_eucl_dist)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_new)


# Time Series Clustering - basic vignettes
X, _ = load_osuleaf(split="train", return_type="numpy3D")
X = X[:10]
mean_eucl_dist = AggrDist(ScipyDist())
clst = TimeSeriesDBSCAN(distance=mean_eucl_dist)
clst.fit(X)
clst.get_fitted_params()

# Primer on sktime transformers for feature extraction
X, _ = load_osuleaf(return_type="pd-multiindex")
detrender = Detrender()
X_detrended = detrender.fit_transform(X)
X_detrended.head()

#  Distances, kernels - general interface
x, _ = load_osuleaf(return_type="numpy3d")
x1 = x[:3]
x2 = x[5:10]

mean_euc_dist = AggrDist.create_test_instance()
distmat = mean_euc_dist(x1, x2)

# alternatively, via the transform method
distmat = mean_euc_dist.transform(x1, x2)
distmat_symm = mean_euc_dist.transform(x1)



# Time series distances, kernels - composition
x, _ = load_basic_motions(return_type="numpy3d")
x = x[:3]
x.shape

# aligners - general interface
aligner = AlignerDTW()
aligner.fit([x1, x2])
aligner.get_alignment()
x1_al, x2_al = aligner.get_aligned()

plot_series(x1_al.reset_index(drop=True), x2_al.reset_index(drop=True), labels=["leaf_1", "leaf_2"])
