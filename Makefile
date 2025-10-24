# Variable that can be changed to your respective python command
PYTHON ?= python

# Default action if no argument is passed
all: help

# List availible commands
help:
	@printf "Commands:\n"
	@printf "exec - See which executable is being used\n"
	@printf "venv - Create a virtual environment\n"
	@printf "install - Install required packages\n"
	@printf "installed - View installed packages\n"
	@printf "test - Run unit tests and generate reports\n"
	@printf "uml - Create UML diagrams for the classes\n"
	@printf "docs - Generate documentation for the classes\n"
	@printf "pylint - Perform linting with pylint on the project\n"
	@printf "flake - Perform linting with flake8 on the project\n"
	@printf "clean - Remove coverage files, cache and html reports\n"
	@printf "clean-doc - Remove generated documentation\n"

exec:
	@printf "Using executable: $(PYTHON)\n"

# Create a virtual environment
venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "To activate the virtual environment perform the following command:\n"
	@printf "Windows:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Mac/Linux:\n"
	@printf "venv/bin/activate\n"
	@printf "To deactivate, enter deactivate\n"

# Install packages
install:
	$(PYTHON) -m pip install -r requirements.txt
	@printf "Packages successfully installed!\n"

# See installed packages
installed:
	$(PYTHON) -m pip list

# Run unit tests and generate reports
test:
	coverage run -m unittest discover src
	coverage report -m
	coverage html

# Create UML class diagrams


# Generate documentation about the classes
docs:
	cd src && pdoc --output-dir ../doc/pdoc *.py

# Perform linting
# Pylint
pylint:
	@for file in src/*.py; do \
		pylint $$file; \
	done

# Flake8
flake:
	@for file in src/*.py; do \
		flake8 $$file; \
	done

lint: pylint flake

# Cleanup
# Remove coverage reports, cache and html reports
clean:
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

# Remove generated documentation
clean-doc:
	rm -rf doc/pdoc
