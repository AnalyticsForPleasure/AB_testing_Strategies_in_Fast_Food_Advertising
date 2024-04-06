from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns



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