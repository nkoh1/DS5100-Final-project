# Monte Carlo Project

This is a recreation of the Monte Carlo project that involves the simulation of rolling dice, flipping coins, and analyzing text. The following methods and classes were used in the creating of this project:

## Classes and Descriptions:

### Die
The die class creates a Die object (or coin) to use for the duration of the program. It will have a default weight of 1 so the chance of a die hitting any number is equally likely.

### Game
A game consists of rolling of one or more similar dice (Die objects) one or more times. Similar dice are represented as objects with the same number of sides (in this case, a regular 6-sided die) but sides can be weighted if chosen to be.

### Analyzer
An Analyzer object takes the results of a single game and computes various descriptive statistical properties about it.

## Die Class Methods Descriptions and Parameters:

`__init__(self,n_sides)`:
This initializer takes on a parameter called n_sides. It is an array that also includes if certain sides are weighted more than the others.

Parameter `n_sides`: integer

Errors Raised:
`TypeError` raised if input is not a NumPy array.
`ValueError` raised if values are not distinct.

`weight_change(self, weight, die_face)`:
The weight_change method allows the user to change the weight of a side of any given dice so that one side, or sides, weigh more than the others. This results in the dice being more likely to land on one side than the rest.

Parameter `weight`: integer
Parameter `die_face`: string or integer

Errors Raised:
`IndexError`: raised if the checked value is not within boundaries of the Die object.
`TypeError`: raised if the weight value is not of correct type

`roll_dice(self, n_rolls=1)`:
The roll_dice method allows any number of rolls with the default number of throws being 1 and default weight also being 1. This is then saved into a dataframe.

Parameter `n_rolls`: integer

`roll_state(self)`:
The roll_state method will return the last roll occurred.

No parameters.


## Game Class Methods Descriptions and Parameters

`__init__(self, n_sides =6)`:
The initializer for the Game class takes n_sides as a parameter. It creates a die object of 6 sides.

Parameter `n_sides=6`: Number of sides on a die.

`play_game(self, rolls)`:
The play_game method rolls performs dice rolls and its values are stored in a dataframe.

Parameter `rolls`: The number of rolls a die will perform.

`narrow_wide(self, form = "wide")`:
The narrow_wide method will store the rolled values in a dataframe and allow the user to view the dataframe either narrow or wide.

Errors Raised:
`ValueError` returns if the user input is not narrow or wide


## Analyzer Class Methods Descriptions and Parameters

`__init__(self,game_result)`:
Takes Game object as input parameter.

Parameter: `game_result` is the game object.

Errors Raised:
`ValueError` if not a Game object.

`jackpot_results (self)`:
The jackpot_results method checks to see if the rolled Die objects land on the same face. If so, it will record the number of times each number (n=1,...,6) have been rolled and output that as an integer.

No parameters.

`count_sides_rolled(self)`:
The count_sides_rolled method counts how many times a given face was rolled. A dataframe is then returned with its results.

No parameters.

`combo_count(self)`:
The combo_count method computes the distinct combinations of the die faces rolled and returns a dataframe with its results.

No parameters.

`permutation_counter(self)`:
The permutation_counter method computes the total number of permutations based on the die faces rolled and returns a dataframe with the total permutations as an integer.

No parameters.

# Installation:

`pip install -e .`

# Importing:

`import montecarlo
from montecarlo import montecarlo`


# Creating Die object:
## Creating a Die object called `die`
- `die = Die(6)`
## Change the weight of a side
-  `die.weight_change(2,4)`
## Rolling the die
-  `die.roll_dice(5)`

# Playing a Game
## creating a Game object `game`
- `game = Game(tot_dice=5)`
- `tot_dice` is the number of dice involved in a roll
## rolling the dice

- 
