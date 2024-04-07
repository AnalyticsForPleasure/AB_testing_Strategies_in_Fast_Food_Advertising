from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Scenario
# A fast-food chain plans to add a new item to its menu. However, they are still undecided between three possible marketing campaigns for promoting the new product.
# In order to determine which promotion has the greatest effect on sales, the new item is introduced at locations in several randomly selected markets. A different
# promotion is used at each location, and the weekly sales of the new item are recorded for the first four weeks.
#
# Goal
# Evaluate A/B testing results and decide which marketing strategy works the best.



# MarketID: unique identifier for market
# MarketSize: size of market area by sales
# LocationID: unique identifier for store location
# AgeOfStore: age of store in years
# Promotion: one of three promotions that were tested
# week: one of four weeks when the promotions were run
# SalesInThousands: sales amount for a specific LocationID, Promotion, and week



if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/AB_testing_Strategies_in_Fast_Food_Advertising/Data/WA_Marketing-Campaign.csv')
    print('*')
    column_headers = list(df.columns.values)
    print("The Column Header :", column_headers)

    MarketSize_values = pd.unique(df['MarketSize'])# 'Medium', 'Small'.'Large'
    LocationID_values = pd.unique(df['LocationID'])
    Age_of_Store_values = pd.unique(df['AgeOfStore']) # range of years : 1 - 23 years.
    Promotion_values = pd.unique(df['Promotion']) # [3,2,1]
    Week_values = pd.unique(df['week']) # [1,2,3,4]
    print('*')
