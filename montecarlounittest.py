import pandas as pd
import montecarlo
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer
import unittest
import numpy as np
import itertools

class MonteCarloTesting(unittest.TestCase):
    def test_init_function(self):
        n_sides = np.array([1,2,3,4,5,6])
        weight = np.array([1,1,1,2,3,1])
        
        die = Die(n_sides,weight)
        
        np.testing.assert_array_equal(die.n_sides, n_sides)
        np.testing.assert_array_equal(die.weight, weight)

        
    def test_weight_change(self):
        n_sides = np.array([1,2,3,4,5,6])
        weight = np.array([1,1,1,2,3,1])
        
        self.die = Die(n_sides, weight)
        
        self.die.weight_change(5,3)
        self.assertEqual(self.die.weight[2],5)
        self.assertEqual(self.die._side_wt.loc[self.die._side_wt['Sides']==3, 'Die'].values[0],5)

    def test_roll_dice(self):
        
        n_sides = np.array([1,2,3,4,5,6])
        weight = np.array([1,1,1,2,3,1])
        
        self.die = Die(n_sides, weight)
        result = self.die.roll_dice(5)
        
        
        
        for r in result:
            self.assertIn(r, self.die.n_sides)
            
        self.die.weight_change(5,3) #increases weight of 3 5x

        result = self.die.roll_dice(5)
        roll1 = result.count(3)
        roll2 = result.count(2)
        
          
    def test_roll_state(self):
        n_sides = np.array([1,2,3,4,5,6])
        weight = np.array([1,1,1,2,3,1])
       
        self.die = Die(n_sides, weight)
        
        first = self.die.roll_state()
        
        self.assertTrue(isinstance(first, pd.DataFrame))
        self.assertEqual(first.shape, (6,2))
        self.assertTrue('Sides' in first.columns)
        self.assertTrue('Die' in first.columns)
        
        self.die.weight_change(5,2) #modifying weight after initializing
        
        last = self.die.roll_state()
        #checking die state
        self.assertEqual(last.loc[last['Sides']==2, 'Die'].values[0],5)
        

        
    def test_game_init(self):
       # n_sides = np.array([1,2,3,4,5,6])
       ## weight = np.array([1,1,1,2,3,1])
        #self.die = Die(n_sides, weight)
        play = Game(6) #standard 6 sided die
        
        self.assertIsInstance(play.die, Die)
        
        play_init = isinstance(play._side_wt, pd.DataFrame)
        
        self.assertTrue(play_init)
        
    def test_play_game(self):
        play = Game(6)
        play_df = play.play_game(10) #10 rolls
        self.assertIsInstance(play_df, pd.DataFrame)
        
        self.assertIsInstance(play._side_wt, pd.DataFrame)
        
        
        
    def test_recent_play(self):
        play = Game(6)
        play_df = play.play_game(10) #10 rolls
        play_wide_df = play.recent_play(view = 'wide')
        self.assertIsInstance(play_wide_df, pd.DataFrame)
        self.assertEqual(play_wide_df.shape[1],10) #checking to see if the dataframe shows as wide for 10 rolls
        
        play_narrow_df = play.recent_play(view='narrow')
        self.assertIsInstance(play_narrow_df, pd.DataFrame)
        self.assertTrue(play_narrow_df.shape[1] ==2) #checking for narrow view where there are only 2 columns in index 1
    
    
    def test_jackpot_results(self):
        play = Game(6)
        play_results = Analyzer(play)
        
        jpot_ct = play_results.jackpot_results()
        analyzer_ct = self.assertIsInstance(jpot_ct, int)
        
    def test_count_sides_rolled(self):
        play = Game(6)
        play_results = Analyzer(play)
        
        roll_results = play_results.count_sides_rolled()
        
    def test_perm_counter(self):
        play = Game(6)
        play_results = Analyzer(play)
        
        total, perm_df = play_results.perm_counter()
        #perm_df = play_results.perm_counter()
        
        self.assertIsInstance(perm_df, pd.DataFrame)

        
        
        
if __name__ == '__main__':
    unittest.main(verbosity=3)