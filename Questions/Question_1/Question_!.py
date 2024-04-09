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
# magine you own a fast-food chain and are planning to add a new dish to the menu. This dish is your grandmother's secret
# recipe and tastes amazing(Yum yum!). But you want others to know that as well. Up until now, you have come up with
# three feasible marketing campaigns for promoting the new dish. In order to determine which campaign is bringing in
# more sales, you introduce the dish at 137 different locations in 10 different markets. You come with a brilliant idea
# to run all 3 campaigns at the locations - with a different campaign at each location and finally record the weekly
# sales of the new dish over the first four weeks.


# Goal
# Evaluate A/B testing results and decide which marketing strategy works the best.



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

    presenting_the_number_of_people_reach_campaign(new_df)
    print('*')