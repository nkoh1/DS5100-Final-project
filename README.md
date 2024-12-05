# Monte Carlo Package

This is a recreation of the Monte Carlo simulation which involves rolling dice, tossing coins, and analyzing text. The following methods and classes were used in the creating of this project:

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

Parameters: None

Errors Raised: None


## Game Class Methods Descriptions and Parameters

`__init__(self, n_sides =6)`:
The initializer for the Game class takes n_sides as a parameter. It creates a die object of 6 sides.

Parameter `n_sides=6`: Number of sides on a die.

`play_game(self, rolls)`:
The play_game method rolls performs dice rolls and its values are stored in a dataframe.

Parameter `rolls`: The number of rolls a die will perform.

`recent_play(self, view = "wide")`:
The recent_play method will store the rolled values in a dataframe and allow the user to view the dataframe either narrow or wide.

Errors Raised:
`ValueError` will return if user input is not either narrow or wide.


## Analyzer Class Methods Descriptions and Parameters

`__init__(self,game_result)`:
Takes Game object as input parameter.

Parameter: `game_result` is the game object.

Errors Raised:
`ValueError` if not a Game object.

`jackpot_results (self)`:
The jackpot_results method checks to see if the rolled Die objects land on the same face. If so, it will record the number of times each number (n=1,...,6) have been rolled and output that as an integer.

Parameters: None

Errors Raised: None

`count_sides_rolled(self)`:
The count_sides_rolled method counts how many times a given face was rolled. A dataframe is then returned with its results.

Parameters: None

Errors Raised: None

`combo_count(self)`:
The combo_count method computes the distinct combinations of the die faces rolled and returns a dataframe with its results.

No parameters.

Parameters: None

Errors Raised: None

`permutation_counter(self)`:
The permutation_counter method computes the total number of permutations based on the die faces rolled and returns a dataframe with the total permutations as an integer.

Parameters: None

Errors Raised: None

# Installation:

`pip install .`

# Importing:

`import demo as montecarlo`


# Creating Die object:
## Creating a Die object called `die`
- `die = Die(n_sides,weight)`
## Change the weight of a side
-  `roll = self.die.weight_change(5,3)`
## Rolling the die
-  `result = self.die.roll_dice(5)`

# Playing a Game
## Creating a Game object `game`
- `play = Game(6)`
## Rolling the dice
-  `play_df = play.play_game(10)`
## Recent Results
- `play_wide_df = play.recent_play(view = 'wide')`

# Creating Analyzer object:
## Creating jackpot method
- `play_results = Analyzer(play)`

## Finding total jackpots
- `play_results.jackpot_results()`
## Simulating a dice roll for count_sides_rolled()
- `throw_results = {i:0 for i in range(1,7)}`
## Finding the total number of times each dice sidde is rolled
- `throw_results_df = pd.Series(throw_results).sort_index()`
## Finding total permutations of faces rolled
- `play_results.perm_counter()` 
