# Monte Carlo Project

This is a recreation of the Monte Carlo project that involves the simulation of rolling dice, flipping coins, and analyzing text. The following methods and classes were used in the creating of this project:

Classes and Descriptions:

# Die
The die class creates a Die object (or coin) to use for the duration of the program. It will have a default weight of 1 so the chance of a die hitting any number is equally likely.

# Methods:
__init__(self,n_sides):
This initializer takes on a parameter called n_sides. It is an array that also includes if certain sides are weighted more than the others.

Parameters:
n_sides: integer

weight_change(self, weight, die_face):
The weight_change method allows the user to change the weight of a side of any given dice so that one side, or sides, weigh more than the others. This results in the dice being more likely to land on one side than the rest.

Parameters:
weight: integer

die_face: string or integer

roll_dice(self, n_rolls=1):
The roll_dice method allows any number of rolls with the default number of throws being 1 and default weight also being 1. This is then saved into a dataframe.

Parameters:
n_rolls: integer

roll_state(self):
The roll_state method will return the last roll occurred.

No parameters.


# Game
A game consists of rolling of one or more similar dice (Die objects) one or more times. Similar dice are represented as objects with the same number of sides (in this case, a regular 6-sided die) but sides can be weighted if chosen to be.

# Methods
__init__(self, tot_dice):
The initializer for the Game class contains a single parameter which is a list of already instantiated dice.

Parameters:
tot_dice: integer


# Analyzer
Based on the results found within the Game class, the Analyzer class provides statistical details regarding the results through visualizations.

