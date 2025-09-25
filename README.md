# Pig dice game
Welcome to our Pig dice game. It's an basic old game but can still be pretty fun!
### Two players

### Goal is to reach 100 points first

### Rules
1. The first player (or computer) chooses to roll their dice.
2. After every roll you may choose to continue the round or hold and save your points.
3. If you roll a 1 you lose all your points you have gathered in that round.
4. Then after the player have rolled a 1 or choose to hold. it's the next players (or computers) turn
5. This continues on until someone reaches 100 points first

# Computer intelligence
We have made the intelligence in such a way that the computer always wants to roll if they haven't rolled a total of 10 in the current round. 
There are also three different difficulties, which goes from Normal, Hard, Extreme. The higher difficulty you choose, the more values it gets on its die.
So in normal mode, the computer gets a regular die that goes from 1-6. In hard mode it gets a die with numbers 1-12, and in extreme mode it gets a die with 1-18.
The player always only has one single die.

# Clone and install the project
Clone the repository by typing this in your console in your directory of your choice

    git clone https://github.com/isander94/DiceGame.git


## Create and activate venv

Create a venv by typing:

    python -m venv .venv

Then you can activate it in different way depending if you're on Windows or Mac/Linux

Windows:
    . .venv/Scripts/activate

Mac/Linux:
    . .venv/bin/activate

## Install packages

To install required packages from the project into your venv type this:
    pip install -r requirements.txt