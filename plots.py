import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt # plotting

# Load your data

def pair_plot(df):

    # Create a Seaborn pairplot
    return sns.pairplot(df)

    # # Display the plot in Streamlit
    # st.pyplot(plot.fig)


def daily_usage_bar_plot(daily_usage_df):
    daily_usage_by_weekday = daily_usage_df.groupby('weekday')['Total Units'].sum().reset_index()

    # Map weekday number to name for better readability
    weekday_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    daily_usage_by_weekday['weekday_name'] = daily_usage_by_weekday['weekday'].map(weekday_map)

    # Sort by weekday order
    daily_usage_by_weekday = daily_usage_by_weekday.sort_values('weekday')

    # Create the bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weekday_name', y='Total Units', data=daily_usage_by_weekday)
    plt.xlabel('Day of Week')
    plt.ylabel('Total Units')
    plt.title('Total Units by Day of Week')
    return plt