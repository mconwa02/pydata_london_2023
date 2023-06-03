# The Opinionated Python Stack 

I chose for my Company’s ML Projects and how I bundled it in a Project Generator
06-03, 10:15–10:55 (Europe/London), Salisbury

Have you ever struggled with choosing the right tools for your Machine Learning projects? As a Lead Data Scientist in a consulting firm, I faced this challenge repeatedly and finally converged to a small set of technologies which allow to build reliable and scalable projects with a great DX (Developer Experience). In this talk, I will share the key components of my ML stack, including DVC, Streamlit, FastAPI, Terraform and other powerful tools to streamline the development and experimentation processes. Through a live demo, I will finally show you the Project Generator I’ve built to encourage adoption of these technologies and to help Data Scientists focus on the ML itself rather than the "plumbing" around it. Attendees should have a basic understanding of Python and Machine Learning concepts.

The world of Data Science is constantly evolving, with new tools and techniques frequently emerging. As a result, building a reliable and efficient Machine Learning stack can be a daunting task. To succeed, companies must navigate a complex landscape of technologies and identify the ones that best meet their unique needs and challenges.

As a Lead Data Scientist for a consulting firm, I have gained experience with various projects and have developed my own idea of such a Machine Learning stack, putting together the technologies I've found to be sufficiently mature and flexible.

In this talk, I'll walk you through this stack, which includes:
- Standard Python developing tools (Poetry, linters, continuous integration, pre-commit, etc.) to ensure a high-quality code base
- DVC for data versioning
- Streamlit to explore data and analyse experimentation results
- FastAPI to serve the model
- Terraform for infrastructure as code

I'll explain how each component fits into the larger picture and discuss the benefits and trade-offs of using these tools together.

To facilitate the adoption of the stack at my company, I've built a Project Generator that allows to quickly and easily scaffold out a new ML project with all of the necessary tools and architecture already in place. This generator helps data scientists focus on the ML itself rather than the "plumbing" around it. After a live demo of the tool, I will briefly explain how I built the generator itself.

This talk is intended for Data Scientists and ML engineers who want to streamline their work and learn about efficient tools for building reliable and scalable ML projects. Attendees should have a basic understanding of Python and Machine Learning concepts.

## Talk Notes

*Quality Checks*
- black (code formatting)
- pytest (unit tests)
- mypy (type checking)
- Ruff (linting)
- 
pip-tools 


Code version with Git
Data Version Control with DVC

Git-like CLI

Data Pipeline

Write DAGs in YSML syntax
Efficient Caching

Streamlit 
wed apps few lines of code 

https://github.com/sicara/sicarator

