import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

#bitcoin prices sourced from Yahoo Finance with the value of the Close price taken
#times taken were from Jan. 01, 2018 to Jan, 01, 2022
bitcoin = [13657.20, 3843.52, 7200.17, 29374.15, 47686.81]
current_std = np.std(bitcoin)
print(current_std)

#calculating IRR for 10 bitcoins mined from the year 2018-2022 assuming an initial investment of $500K
current_irr_array = [-500000, 10 * bitcoin[0], 10 * bitcoin[1], 10 * bitcoin[2], 10 * bitcoin[3], 10 * bitcoin[4]]
current_irr_res = npf.irr(current_irr_array)
print(current_irr_res)

#calculating the worth of investment at the end of each year assuming an investment of $1K in 2018
multiplier = 1000 / (10 * bitcoin[0])
values_array = np.multiply(bitcoin, multiplier)

#charting out the value of the investment for each year from 2018 to 2022
years_array = [2018, 2019, 2020, 2021, 2022]
plt.plot(years_array, values_array)
plt.savefig("investment_value_graph.png")