## PyData London June 2023

The London PyData Conference June 2023

## PyData Bristol
https://www.meetup.com/pydata-bristol/events/293860053/

Thursday, June 15, 2023 at 6:00 PM to 8:30 PM BST
Cookpad, 1 Broad Plain, Bristol

## 01 sktime - python toolbox for time series: how to implement your own 

https://github.com/sktime/sktime-tutorial-pydata-london-2023/tree/main
sktime is a widely used scikit-learn compatible library for learning with time series. sktime is easily extensible by anyone, and interoperable with the pydata/numfocus stack. This tutorial explains how to write your own sktime estimator, e.g., forecaster, classifier, transformer, by using sktime’s extension templates and testing framework. A custom estimator can live in any local code base, and will be compatible with sktime pipelines, or scikit-learn. A continuation of the sktime introductory tutorial at pydata [link]

Writing sktime compatible estimators is meant to be easy.

This tutorial will explain: • sktime base class and estimator architecture • basic software design patterns used in extension • how to use the extension templates • how to validate your custom estimator • testing in third party extensions and packages

## 02 An Introduction to Polars

https://tinyurl.com/pydatapolars

Uses Rust terms
Polars is a next generation data-frame library which aims to be fast, efficient, composable and lazy! This introductory tutorial will take you through the basics of getting started with polars in Python. We will demonstrate the out the box multi-core efficiencies, by composing advanced filters and joins, before comparing with the traditional pandas workflows. As a finale we will look at some lazy processing when applying polars to large scale data-sets.

## 03 Bring best practices to your messy data science team!

Code and slides: https://github.com/DrGabrielHarris/pydata-london-2023

https://www.gnu.org/home.en.html

Website: https://12ft.io/

Not using in Poetry instead using pip-tools

[pip tools]!(https://pip-tools.readthedocs.io/en/latest/)

[py doc style]!(https://www.pydocstyle.org/en/stable/)

[ruff]!(https://github.com/charliermarsh/ruff)

Questions for talk [canva]!(https://www.canva.com/presentation/join)

## 04 Delta Lake 101: How many water metaphors does it take to describe data?

Delta Lake is an open-source storage framework that enables the creation of a 
Lakehouse architecture using a variety of compute engines such as Spark,
PrestoDB, Flink, Trino, and Hive from Python. Its high data reliability and 
optimized query performance make it an ideal solution for supporting big data 
use cases, including batch and streaming data ingestion, fast interactive 
queries, and machine learning.

[delta]!(https://github.com/delta-io/delta)

## 05 Keynote: Large Language Models: From Prototype to Production

Ines Montani is a developer specializing in tools for AI and NLP technology.
She’s the co-founder and CEO of Explosion and a core developer of spaCy, a 
popular open-source library for Natural Language Processing in Python, and
Prodigy, a modern annotation tool for creating training data for machine
learning models.

## 06 The Opinionated Python Stack 

I chose for my Company’s ML Projects and how I bundled it in a Project Generator

Have you ever struggled with choosing the right tools for your Machine Learning projects? As a Lead Data Scientist in a consulting firm, I faced this challenge repeatedly and finally converged to a small set of technologies which allow to build reliable and scalable projects with a great DX (Developer Experience). In this talk, I will share the key components of my ML stack, including DVC, Streamlit, FastAPI, Terraform and other powerful tools to streamline the development and experimentation processes. Through a live demo, I will finally show you the Project Generator I’ve built to encourage adoption of these technologies and to help Data Scientists focus on the ML itself rather than the "plumbing" around it. Attendees should have a basic understanding of Python and Machine Learning concepts.

## 07 Executives at PyData

Executives at PyData is a facilitated discussion session for executives and leaders to discuss challenges around designing and delivering successful data projects, organizational communication, product management and design, hiring, and team growth.

## 08✨ fastAPI facts we wish we'd known beforehand. 

Spoiler: It's not about getting started.

An exchange of views on fastAPI in practice.

## 09 Pandas 2, Dask or Polars?

Quickly tackling larger data on a single machine

Pandas 2 brings new Arrow data types, faster calculations and better scalability. Dask scales Pandas across cores. Polars is a new competitor to Pandas designed around Arrow with native multicore support. Which should you choose for modern research workflows? We'll solve a "just about fits in ram" data task using the 3 solutions, talking about the pros and cons so you can make the best choice for your research workflow. You'll leave with a clear idea of whether Pandas 2, Dask or Polars is the tool for your team to invest in.

## 10 New Developments in Pandas and Dask Dataframes

We're in a new era of dataframe development. Libraries like Arrow, Polars, DuckDB, Vaex, Modin, and others stretch the bounds of performance on what we think can be done with tabular data in Python. These systems have great benchmarking results and generate significant buzz on social media.

Matthew Rocklin is an open source software developer in the numeric Python ecosystem

## 11 From correlations to causality in machine learning– a gentle guide to 

Learning about causal inference

Today most conventional ML systems look to exploit correlations in data in order to draw inferences. However as we learned back in school Statistics class, correlation is not causation. So when you need to know the ‘why’ behind a particular prediction, or why A outperforms B in an experiment, then relying on correlations is insufficient. Furthermore some ML models are build purely for explainability and insight purposes rather than predictions, in order to understand how the world works so we could potentially make some kind of policy change, e.g. What if we had chosen a different strategy or tactic – would the outcome have been different, and if so, by how much? To answer these kinds of questions, you need to delve into the world of causality.

## # How to build stunning Data Science Web applications in Python

The new low-code Python package that allows you to 
create complete Data Science applications, including graphical visualization and managing algorithms, pipelines, and scenarios.

It is composed of two main independent components:

* Taipy Core

* Taipy GUI.

![taipy website](https://www.taipy.io/)

Taipy GUI to create an interactive and powerful user interface in a few lines of code.

Taipy Core to create scenarios, use models, retrieve metrics easily, version control their application configuration,

Taipy Studio, a brand-new pipeline graphical editor inside VS Code also that facilitates the creation of scenarios and pipelines.

With Taipy, the Python developer can transform simple pilots into production-ready end-user applications. Taipy GUI goes way beyond the capabilities of the standard graphical stack: Gradio, Streamlit, Dash, etc.

This could be useful for Savings UI instead of using 