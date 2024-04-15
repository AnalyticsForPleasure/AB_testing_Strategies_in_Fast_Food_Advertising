from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

#For this project, we will be working to understand the results of an A/B test run by an e-commerce website.
# we goal is to work through this notebook to help the company understand.

#Below is a description of this data set
# Campaign Name: Target campaign type for ad landing page.
# Spend [USD]: The amount of money spent on advertising in the campaign.
# of Impressions: The number of people who viewed the ad in the campaign (contains repeated viewing of the same person for the ad).
# Reach: The number of unique people who saw the ad in the campaign.
# of Website Clicks: The number of users who clicked on the website link in the campaign's advertisement.
# of Searches: The number of users who performed a search on the website.
# of View Content: Number of users who have viewed product details.
# of Add to Cart: The number of users who have added the product to the cart.
# of Purchase: The number of users who have purchased the product.

# **************************************************************************************************************
# Function  name: presenting_the_number_of_people_reach_campaign
# input:
# return value:
# ***************************************************************************************************************
def presenting_the_number_of_people_reach_campaign(new_df):
    # The number of people to see the ad in the campaign: (What is the total number for reach of each campaign?)
    total_result = new_df.groupby(["Campaign Name"])["Reach"].sum()
    sns.set_style("white")
    fig, ax = plt.subplots(1, 1, figsize=(16, 5), sharex=False)
    # Use custom colors
    c = sns.color_palette(["royalblue", "lightblue"])
    # Plot the total reach for each campaign
    total_result.plot(kind="bar",
                      rot=0,
                      width=0.93,
                      alpha=1,
                      fontsize=12,
                      color=c,
                      ax=ax)
    # Annotate the bars with the total reach values
    for i, g in enumerate(total_result):
        ax.text(i + 0.10, g - 180000, "{:0,.0f}".format(g), color='white',
                fontsize=19, fontweight="bold", ha="center", va='center')
    # Set plot title, labels, and aesthetics
    ax.set_title("Total Number who reach to the campaign", fontsize=18, color="blue", pad=38)
    ax.set_xlabel('')
    ax.set_xticklabels(labels=["Control", "Test"], fontsize=14)
    ax.set_yticks([])
    sns.despine(left=True)
    plt.savefig('output_chart.jpg', dpi=250, bbox_inches='tight')
    plt.show()

# **************************************************************************************************************
# Function  name: reviewing_click_through_rate_for_each_campaign
# input:
# return value:
# ***************************************************************************************************************
def reviewing_click_through_rate_for_each_campaign(new_df):
    sns.set_style("whitegrid")
    c = sns.color_palette(["royalblue", "lightblue"])
    fig, ax = plt.subplots(1, 3, figsize=(16, 4), sharex=False)
    sns.ecdfplot(x="Reach",
                 data=new_df,
                 hue="Campaign Name",
                 palette="deep", ax=ax[0])
    ax[0].set_title("Empirical Cumulative Distribution Function\nof Campaign Reach Counts", fontsize=13, color="k", pad=20,fontweight="bold")
    ax[0].set_xlabel("Reach Number", fontsize=12,fontweight="bold")
    ax[0].set_ylabel("Empirical Cumulative Distribution Function", fontsize=12, color="k",fontweight="bold")
    sns.ecdfplot(x="# of Website Clicks",
                 data=new_df,
                 hue="Campaign Name",
                 palette="deep", ax=ax[1])
    ax[1].set_title("Empirical Cumulative Distribution Function\nof Campaign Click Counts", fontsize=13, color="k", pad=20,fontweight="bold")
    ax[1].set_xlabel("Number of Clicks to the Website", fontsize=12,fontweight="bold")
    ax[1].set_ylabel("Empirical Cumulative Distribution Function", fontsize=12, color="c",fontweight="bold")
    sns.set_style("white")
    CTR = new_df.groupby(["Campaign Name"])["# of Website Clicks"].sum() / new_df.groupby(["Campaign Name"])[
        "Reach"].sum() * 100
    CTR.plot(kind="bar",
             rot=0,
             width=0.80,
             alpha=0.9,
             fontsize=12,
             color=c, ax=ax[2])

    for i, g in enumerate(CTR):
        ax[2].text(i, g - 3, "{0:.{digits}f}%".format(g, digits=2), color='white',fontweight="bold",
                   fontsize=15, ha="center", va='center')
    ax[2].set_title("CTR per campaign", fontsize=14, color="k", pad=20,fontweight="bold")
    ax[2].set_xlabel("Campaign Name", fontsize=12, fontweight="bold")
    ax[2].set_ylabel("CTR", fontsize=15, color="k")
    ax[2].set_xticklabels(labels=["Control", "Test"], fontsize=12);

    plt.savefig('output_chart_2.jpg', dpi=250, bbox_inches='tight')
    plt.show()

if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    #df = pd.read_csv('/home/shay_diy/PycharmProjects/AB_testing_Strategies_in_Fast_Food_Advertising/Data/WA_Marketing-Campaign.csv')
    df_control_group = pd.read_csv('/home/shay_diy/PycharmProjects/AB_testing_Strategies_in_Fast_Food_Advertising/Data/control_group.csv', sep = ";")
    df_test_group = pd.read_csv('/home/shay_diy/PycharmProjects/AB_testing_Strategies_in_Fast_Food_Advertising/Data/test_group.csv', sep = ";")


    #Let's merge the two sets of data, so that one data set is placed below the other data set, as follows:
    new_df = df_control_group.merge(df_test_group, how='outer')#.sort_values(['date']).reset_index(drop=True)
    new_df.head()

    new_df.sort_values(['Date']).reset_index(drop=True)
    print('*')

    res = new_df.isnull().sum()
    print('*')

    #presenting_the_number_of_people_reach_campaign(new_df)
    print('*')

    reviewing_click_through_rate_for_each_campaign(new_df)
    print('*')
