# Pig dice game
Welcome to our Pig dice game. It's an basic old game but can still be pretty fun!
### Two players

### Goal is to reach 100 points first

### Rules
1. The first player (or computer) chooses to roll their dice.
2. After every roll you may choose to continue the round or hold and save your points.
3. If you roll a 1 you lose all your points you have gathered in that round.
4. Then after the player have rolled a 1 or choose to hold, it's the next players (or computers) turn
5. This continues on until someone reaches 100 points first

# Game difficulty
When playing against the computer, you may choose between four different difficulties. Each difficulty
allows the computer to roll higher values and therefore having the potential of accumulating high scores quickly.
The difficulty levels changes the potential outcomes when rolling the die accordingly:
* Normal: 1-6 points
* Medium: 1-12 points
* Hard: 1-24 points
* Very hard: 1-48 points
To ensure a feeling of high risk - high reward, the computer will always be able to roll a 1 and lose all the points
for that turn.
However, the player can only roll 1-6 regardless of difficulty level.

# Installing the game
Clone the repository by typing this in your console in your directory of your choice

    git clone https://github.com/isander94/DiceGame.git

# Makefile
This project uses a makefile to simplify installation and running tests and generating documentation.
    If you're using Windows you will need to install the Chocolatey package manager from the link below
    https://chocolatey.org/install

If you're using a Mac or Linux system, makefiles should already work for you.

## Create and activate a virtual environment (venv)

Create a venv by typing:

    make venv

Then you can activate it in different way depending if you're on Windows or Mac/Linux

Windows:

    . .venv/Scripts/activate

Mac/Linux:

    . .venv/bin/activate

## Packages
# Install packages
To install required packages from the project into your venv type this:

    make install

# View installed packages

If you would like to inspect what packages the project is using, simple run the following command:

    make installed

## Run tests and get coverage report

To run the test suite for the project, enter the following command:

    make test

This will run the tests for all of the classes and also generate a coverage reports.
The first report can be seen in the terminal after the tests have passed. The second report is an HTML report and is located
in the htmlcov directory after the tests are finished.

## Documentation
This project allows you to easily generate documentation. Both written documentation that shows you the code in the browser
but also a UML diagram that shows the classes and the packages.

# Generating documentation

To generate documentation that can be seen in the browser, run the following program:

    make docs

This will create HTML-files based on the classes of the project and will be located in the doc/pdoc directory.

# Generating UML diagrams

If you'd like to create UML-diagrams instead, run this command:

    make uml

The diagrams will be located in the doc/uml directory.

# Linting and code consistency
There are three commands for performing linting of the code of the project:

    make pylint
    make flake
    make lint

The first command will run pylint on all files, and flake will instead run flake8. If you prefer to run them both in sequence,
use the third command which will run them both.

# Cleaning up after generating documents and diagrams
Should you want to clean up the project after experimenting with documentation, diagrams and coverage reports you can easily do so.

This command removes the coverage report file and compiled python bytecode.

    clean

To clean the generated documentation, run the following command:

    make clean-doc

This will remove the HTML-documentation located in the doc/pdoc directory.

The UML diagrams can also be cleaned. Run the following command:

    make clean-uml

Additionally, you can run one command for a complete sweep:

    make clean-all

## Need a reminder?
To find all availible commands, simply run this short command:

    make help

It will list all commands and a brief explanation.

## Running the game
Navigate to the src folder with the following command:

    cd src

We can now run the main file:

    python main.py

You will be presented with the main menu and the game will wait for your input.


