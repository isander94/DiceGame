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

exec:
	@printf "Using executable: $(PYTHON)\n"

# Create a virtual environment
venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv

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
uml:
	pyreverse src/player.py
	dot -Tpng classes.dot -o doc/uml/playerdiagram.png
	pyreverse src/dice.py
	dot -Tpng classes.dot -o doc/uml/dicediagram.png
	pyreverse src/game.py
	dot -Tpng classes.dot -o doc/uml/gamediagram.png
	pyreverse src/highscore.py
	dot -Tpng classes.dot -o doc/uml/highscorediagram.png
	pyreverse src/main.py
	dot -Tpng classes.dot -o doc/uml/maindiagram.png
	@printf "Diagrams created at doc/uml\n"

