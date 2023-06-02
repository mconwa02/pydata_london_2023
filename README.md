# PyData London June 2023

The London PyData Conference June 2023

# sktime - python toolbox for time series: how to implement your own estimator
06-17, 09:00–10:30 (Europe/London), Tower Suite 1

https://github.com/sktime/sktime-tutorial-pydata-london-2023/tree/main

sktime is a widely used scikit-learn compatible library for learning with time series. sktime is easily extensible by anyone, and interoperable with the pydata/numfocus stack. This tutorial explains how to write your own sktime estimator, e.g., forecaster, classifier, transformer, by using sktime’s extension templates and testing framework. A custom estimator can live in any local code base, and will be compatible with sktime pipelines, or scikit-learn. A continuation of the sktime introductory tutorial at pydata [link]

Writing sktime compatible estimators is meant to be easy.

This tutorial will explain: • sktime base class and estimator architecture • basic software design patterns used in extension • how to use the extension templates • how to validate your custom estimator • testing in third party extensions and packages

Users can write sktime compatible estimators without a full developer setup, or any need to contribute the estimator to the sktime codebase. The custom estimator can be used with any tuning, pipeline, composition, or reduction functionality in sktime, and will be compatible with scikit-learn, too. This philosophy enables interoperability with third projects, proprietary code bases, or custom extension packages to sktime.

How this works technically: sktime ensures that all estimators of a certain type, e.g., forecasters, adhere to the same interface contracts, by using the base class and strategy patterns.

Separate to this user sided contract is the extension contract, which "extenders", users implementing their own estimators, have to satisfy. This is based on the template pattern which keeps boilerplate from the extension contract, and clearly defined "fill in your code" instructions in sktime´s extension templates.

The extension templates are python files with gaps that the extender is meant to fill in with the logic of a new estimator, with clear instructions in comments, and without any boilerplate. Finally, the sktime test suite provides few-line-validation for any custom estimator.

A full developer setup is typically not required to implement a custom estimator compatible with sktime.

# An Introduction to Polars

06-02, 11:00–12:30 (Europe/London), Minories

https://tinyurl.com/pydatapolars

Uses Rust terms
Polars is a next generation data-frame library which aims to be fast, efficient, composable and lazy! This introductory tutorial will take you through the basics of getting started with polars in Python. We will demonstrate the out the box multi-core efficiencies, by composing advanced filters and joins, before comparing with the traditional pandas workflows. As a finale we will look at some lazy processing when applying polars to large scale data-sets.

### Background
The tutorial targets intermediate data-scientists who use pandas as a part of their existing data science tool-kit.
The central premise of the tutorial is that polars is faster and more composable resulting in a cleaner and more productive work flows.

The ultimate aim of this tutorial is to "convert" pandas users to polars :) !

### Introduction
Installation - basic installation using pip
Data type basics - column types and coalescing
Interop with pandas/numpy - how this relates to the traditional numpy dtypes
File reading basics - the standard operations to read data into a dataframe from a host of different formats

### Standard Workflow

Accessing columns
Filtering - filtering is composed quite nicely in polars, so we will go through a few examples
Grouping - grouping is again nicely multicore

### Joining

Row based operations
Advanced Workflow
A note about multicore - polars is Rust under the hood and the correctness allows for a clean multicore processing capacity. We will spend five minutes demonstrating this on a large data-set.
Case study, lazy geospatial processing: The final part of the tutorial will be a case study example of efficient geospatial lazy processing. In this we will go through the efficiency gains of using the lazy interface to filter a large collection of geospatial data in a multicore way, to find points within defined polygonal shapes. We will show that large amounts of data can be processed efficiently even on relative small setup, and complex filters can be applied to disk backed data.


# Bring best practices to your messy data science team!

06-02, 13:30–15:00 (Europe/London), Minories

This session's header image
If part of your job is to constantly poke your fellow data scientist to isolate projects environments, updating requirements, cleaning code, writing consistent docstrings, etc., then you should definitely join us for this very hands-on tutorial with reproducibility, compliance, and consistency in mind

We will be covering:
- What is pipx and why using it
- Managing virtual environments and dependencies using pyproject.toml, venv, and pip-tools
- Running pre-commit hooks (black, ruff, isort, pydocstyle, sqlfluff, and a few more!)
- Automating commands using Make with a Makefile
- Bonus: VSCode integration

Code and slides: https://github.com/DrGabrielHarris/pydata-london-2023

https://www.gnu.org/home.en.html

Website: https://12ft.io/

Not using in Poetry instead using pip-tools

https://pip-tools.readthedocs.io/en/latest/

https://www.pydocstyle.org/en/stable/