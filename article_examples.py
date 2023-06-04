
from taipy import Gui

Gui(page="# Getting started with *Taipy*").run() # use_reloader=True

from sktime.datasets import load_osuleaf

# load an example time series panel in pd-multiindex mtype
X, _ = load_osuleaf(return_type="pd-multiindex")

# steps 1, 2 - prepare osuleaf dataset (train and new)
from sktime.datasets import load_osuleaf

X_train, y_train = load_osuleaf(split="train", return_type="numpy3D")
X_new, _ = load_osuleaf(split="test", return_type="numpy3D")

# step 3 - specify the classifier
from sktime.classification.distance_based import KNeighborsTimeSeriesClassifier

# example 1 - 3-NN with simple dynamic time warping distance (requires numba)
clf = KNeighborsTimeSeriesClassifier(n_neighbors=3)
# all classifiers is scikit-learn / scikit-base compatible!
# nested parameter interface via get_params, set_params
clf.get_params()
# step 4 - fit/train the classifier
clf.fit(X_train, y_train)
# step 5 - predict labels on new data
y_pred = clf.predict(X_new)

import pandas as pd


"
from dowhy import CausalModel
import dowhy.datasets

kidney_df = dowhy.datasets.linear_dataset()

model = CausalModel(
    data=kidney_df,
    graph=kidney_df['gml_graph'],
    treament='treatment',
    outcome='success'
)

identified_estimand = model.identify_effect()

estimate = model.estimate_effect(
    identified_estimand,
    method_name="backdoor.linear_regression",
    target_units='ate'
)


# IV. Refute the obtained estimate using multiple robustness checks.
refute_results = model.refute_estimate(
    estimand,
    estimate,
    method_name="random_common_cause")
