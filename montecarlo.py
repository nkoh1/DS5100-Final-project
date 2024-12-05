# A code block with your classes.
import numpy as np
import pandas as pd
import random

class Die: 
    """
    The Die class takes a NumPy array to act as a face of the object. In this case, it will be either a 6-sided die or a coin which has 2 sides.
    The data type of the array may be either strings or numbers with all values being distinct from each other. By default, a die or a coin will have the same weight for each side.
    
    Attributes:
    -----------
    n_sides : NumPy.ndarray that represents the sides of dice with the defaut being 6 sides, excluding 0.
    weight : NumPy.ndarray that determines the weight of a dice's side. This can be changed as needed.
    _side_wt: The private dataframe that keeps all results using n_sides and weight.
    """
    def __init__ (self, n_sides: np.ndarray, weight: np.ndarray):
        """
        __init__ parameters: sides (type: NumPy array)
        ==============================================
        """
        if not isinstance(n_sides, np.ndarray):
            raise TypeError("n_sides must be NumPy array")

        if len(n_sides) != len(set(n_sides)):
            raise ValueError("Values in this array are not unique")
        
        self.n_sides = n_sides
        
        if weight is None:
            self.weight = np.ones(len(n_sides))
        
        
        self.weight = weight

        self._side_wt = pd.DataFrame({"Sides":self.n_sides, 'Die': self.weight})
        
    def weight_change(self, weight, die_face): #weight default 1
        """
        weight_change parameters: weight, die_face (type: string or integer)
        
        Raised Errors:
        =================================
        IndexError - Error will raise when die_face is less than 1 or die_face has more than 6 sides. Must be strictly positive.
        
        ValueError - Error will raise when the weight chosen is less than 1. Must be strictly positive.
        =================================
        weight_change() will allow the user to change the weight of one side of a die. All dice faces are weighted 1 by default.
        
        """
        if not isinstance (weight, int) or weight <=0:
            raise TypeError("The weight is not a valid type.")
        if die_face not in self.n_sides:
            raise IndexError(f"{die_face} is not a valid index")

         
        index = np.where(self.n_sides ==die_face)[0][0]
        self.weight[index]= weight #updates weight
        
        self._side_wt['Die'] = self._side_wt.apply(lambda row: weight if row['Sides'] == die_face else row['Die'], axis=1)


        
    def roll_dice(self, n_rolls=1): #defaulted to 1 roll
        """
        roll_dice parameters: n_rolls (type: integer)
        
        roll_dice will simulate the action of rolling dice labeled as throw and put them in a list.
        """
        throw = np.random.choice(self.n_sides, size = n_rolls, p = self.weight / np.sum(self.weight)) #np.random.choice from python doc; useful for probability
        return throw.tolist() #returns all thrown values as a list; tolist()
    
    
    def roll_state(self):
        """
        roll_state parameters: None
        
        roll_state will show the latest result of the die roll
        """
        
        return self._side_wt.copy()

class Game: 
    """
    The Game class consists of rolling one or more dice (dice objects) multiple times. All dice in this scenario have 6 sides but weights can be changed.
    The latest result of the last game played will be kept.
    
    """
    def __init__(self, n_sides =6):
        """
        __init__ parameters: n_sides (type: integer)
        ===============================================
        """   
        if not isinstance(n_sides, int):
            raise TypeError("The value entered is not an integer.")
            
        self.die = Die(np.arange(1, n_sides+1), np.ones(n_sides)) #calls Die class and specifies sides
        self._side_wt = pd.DataFrame() #initializing pd.dataFrame
 
    def play_game(self, rolls):
        """
        play_game parameters: rolls (type: integer)
        
        play_game will perform dice rolls and store the results in a dataframe 
        """
        roll_results = self.die.roll_dice(rolls)
        
        rr_big = np.array(roll_results).reshape(1,rolls)
        
        dice_df = pd.DataFrame(rr_big, columns = [f'Roll # {i+1}'
                                                        for i in range(rolls)])
        
        self._side_wt = pd.concat([self._side_wt, dice_df], axis=1)
        
        return self._side_wt
        
    
    def recent_play(self, view = "wide"): #form = wide, defaults to wide view. also shows last play
        """
        recent_play parameters: view (takes a user inputted string that is either wide or narrow
        Determines if the dataframe should be visualized as narrow (long) or wide (transposed)
        ===============================================
        """
        if view == "wide":
            return self._side_wt
        elif view =="narrow":
            return self._side_wt.melt(var_name= "Die",value_name = "Side")
        else:
            raise ValueError("Invalid input. Dataframe must be either wide or narrow")


class Analyzer:
    """
    The Analyzer class the results of a single game and outputs various statistical properties about it.
    
    """
    def __init__(self,game_result):
        """
        __init__ parameters: games (type: object; part of class Game)
        Raised Errors:
        ========================================================
        ValueError: checks to see if the games object is part of the Game class. If not, throws error        
        """

        if not isinstance(game_result,Game):
            raise ValueError("This is not a Game object.")
            
        self.game_result = game_result
        self.output = self.game_result.play_game(5)
        
    
    def jackpot_results (self): #jackpot method   
        """
        jackpot_results parameters: None
    
        Returns the number of times a jackpot is hit. That is, the number of arbitrary dice land on the same side.
        """
        jpot_check = self.game_result._side_wt.values
        
        jpot_ct =0
        
        for i in jpot_check.T:
            if len(set(i)) == 1:
                jpot_ct+=1
        return jpot_ct

    def count_sides_rolled(self):
        """
        count_sides_rolled parameters: None
    
        Returns the number of times each face is landed upon after rolling a number of times. Results in a dataframe.
        """
        if self.output is not None:
            throw_results = {i:0 for i in range(1,7)} #since n_sides =6
            
            for i in self.output.columns:
                roll_sides = self.output[i].values
                
            for j in roll_sides:
                if j in throw_results:
                    throw_results[j] +=1
                
            throw_results_df = pd.Series(throw_results).sort_index()
            return throw_results_df

                    
                    


        
    def perm_counter(self):
        """
        perm_coutner parameters: None
    
        Returns the total number of permutations from the number of rolls and outputs a dataframe with them. Also includes the total number of permutations.
        """
        throw_results = self.output.values.flatten()

        perm_list = np.array(list(np.random.permutation(throw_results) for i in range(len(throw_results))))
        
        final_perm_df = pd.DataFrame(perm_list, [f'Roll # {i+1}'
                                                        for i in range(len(throw_results))])
        
        perm_total = len(final_perm_df)
        return perm_total, final_perm_df

