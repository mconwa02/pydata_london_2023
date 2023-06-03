# ✨ fastAPI facts we wish we'd known beforehand. 

Spoiler: It's not about getting started.

06-03, 11:45–12:25 (Europe/London), Salisbury

An exchange of views on fastAPI in practice.

FastAPI has become an integral part of the PyData ecosytem. FastAPI is great, it helps many engineers create REST APIs based on the OpenAPI standard and run them asynchronously. It has a thriving community and educational documentation.

FastAPI does a great job of getting people started with APIs quickly.

This talk will point out some obstacles and dark spots that I wish we had known about before. In this talk we want to highlight solutions based on experience building a data hub in asset management.

An exchange of views on fastAPI in practice.

FastAPI is great, it helps many developers create REST APIs based on the OpenAPI standard and run them asynchronously. It has a thriving community and educational documentation.

FastAPI does a great job of getting people started with APIs quickly.

This talk will point out some obstacles and dark spots that I wish we had known about before. In this talk we want to highlight solutions.

This talk will include the following:

### pydantic

fastAPI is built on the shoulders of giants I: pydantic
FastAPI makes extensive use of [pydantic. pydantic]!(https://docs.pydantic.dev/) parses data, can 
validate (and transform) data, and has built-in interfaces to export OpenAPI definitions among many other features.


### starlette

fastAPI is built on the shoulders of giants I: [starlette]!(https://www.starlette.io/)
Routes and middleware are managed by starlette. In this section we will explore how to create custom middleware and what we learned along the way.

fastAPI has tutorials, but is this documentation?
The fastAPI page provides a good introduction. The more we worked with fastAPI, the harder it was to find accurate documentation. Looking at the source code, we really missed DocStrings! Introspection to the rescue - will probably include a rant about missing DocStrings!

### pydantic

DRY ("Don't repeat yourself") with pydantic
For our use case, we decided to use strict models to validate our data structures, as we work in a highly regulated industry where no mistakes are allowed to happen. Setting up the REST API was much easier than developing consistent models that generalise well. We follow the "single source of truth" paradigm, entering redundant definitions is an absolute no-go.
In this section we show how to create highly reusable pydantic model pools with inheritance for use in fastAPI. For testing, we also created models from metadata!

"The road not taken": pydantic Depends()!
API routes often consist of a request model and a response model. But what about cases where the models alone don't work and a model and e.g. query parameters need to be mixed?
Apart from flake8 complaining about having callables in the signature, this can be quite a difficult use case. Strategies for resolving model/parameter conflicts.

Bonus - if time:

Integrating fastAPI with Sphinx.
Demonstrate how to integrate OpenAPI with your Sphinx documentation.

Based on experience building a data hub in asset management, the talk will show how fastAPI is built and how well introspection can help you understand what is going on under the hood and which library is actually doing the heavy lifting where.

## Why Fast API

High performance web framework

instead of flask

custom python package interface to 


FASTAPI current version 

259 classes
6022 lines of code
more docstrings