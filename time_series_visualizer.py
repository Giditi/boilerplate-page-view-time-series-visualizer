import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col="date" , parse_dates=True)

# Clean data
months= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
flt_top25= df['value'] >= df['value'].quantile(0.975)
flt_bot25= df['value'] <= df['value'].quantile(0.025)
df_clean = df.loc[(~flt_top25 & ~flt_bot25)]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12,6))
    #fig=df_clean.plot.line()
    fig=sns.lineplot(data=df_clean, legend="brief")

    fig.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig.set_xlabel('Date')
    fig.set_ylabel('Page views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar= df.copy()
    df_bar.reset_index(inplace=True)
    df_bar["year"] = df.index.year.values
    df_bar["month"] = df.index.month_name()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15,5))
    ax = sns.barplot(x="year", hue="month", y="value", data=df_bar, hue_order = months, errorbar=None )
    ax.set(title='Month', xlabel='Years', ylabel='Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2, figsize=(25,10))
    sns.boxplot(x="year", hue="year", y="value", data=df_box,ax = ax[0])
    ax[0].set(title='Year-wise Box Plot (Trend)',xlabel='Years', ylabel='Page Views')

    sns.boxplot(x="month", hue="month", y="value", data=df_box, hue_order = months,ax = ax[1])
    ax[1].set(title='Month-wise Box Plot (Seasonality)',xlabel='Month', ylabel='Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
