import numpy as np
import numpy_financial as npf

#bitcoin prices sourced from Yahoo Finance with the value of the Close price taken
#times taken were from Jan. 01, 2018 to Jan, 01, 2022
bitcoin = [13657.20, 3843.52, 7200.17, 29374.15, 47686.81]
current_std = np.std(bitcoin)
print(current_std)