# 02 An Introduction to Polars

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


