
# 03 Bring best practices to your messy data science team!

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

https://github.com/charliermarsh/ruff

Questions for talk https://www.canva.com/presentation/join

### Package *squatting*

*Typo-squatting* occurs when a malicious package is uploaded with a name 
similar to a common package ex `pip install panda` instead of `pip install 
pandas`