# pydata_london_2023

The London PyData Conference June 2023

# sktime - python toolbox for time series: how to implement your own estimator
06-17, 09:00–10:30 (Europe/London), Tower Suite 1
sktime is a widely used scikit-learn compatible library for learning with time series. sktime is easily extensible by anyone, and interoperable with the pydata/numfocus stack. This tutorial explains how to write your own sktime estimator, e.g., forecaster, classifier, transformer, by using sktime’s extension templates and testing framework. A custom estimator can live in any local code base, and will be compatible with sktime pipelines, or scikit-learn. A continuation of the sktime introductory tutorial at pydata [link]

Writing sktime compatible estimators is meant to be easy.

This tutorial will explain: • sktime base class and estimator architecture • basic software design patterns used in extension • how to use the extension templates • how to validate your custom estimator • testing in third party extensions and packages

Users can write sktime compatible estimators without a full developer setup, or any need to contribute the estimator to the sktime codebase. The custom estimator can be used with any tuning, pipeline, composition, or reduction functionality in sktime, and will be compatible with scikit-learn, too. This philosophy enables interoperability with third projects, proprietary code bases, or custom extension packages to sktime.

How this works technically: sktime ensures that all estimators of a certain type, e.g., forecasters, adhere to the same interface contracts, by using the base class and strategy patterns.

Separate to this user sided contract is the extension contract, which "extenders", users implementing their own estimators, have to satisfy. This is based on the template pattern which keeps boilerplate from the extension contract, and clearly defined "fill in your code" instructions in sktime´s extension templates.

The extension templates are python files with gaps that the extender is meant to fill in with the logic of a new estimator, with clear instructions in comments, and without any boilerplate. Finally, the sktime test suite provides few-line-validation for any custom estimator.

A full developer setup is typically not required to implement a custom estimator compatible with sktime.
