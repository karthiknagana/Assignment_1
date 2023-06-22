import pandas as pd

# Read the data into a DataFrame
url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/hate-crimes/hate_crimes.csv"
data = pd.read_csv(url)

# Display the first few rows of the DataFrame
print(data.head())

import matplotlib.pyplot as plt

def plot_line_graph(data, x_column, y_columns, title, xlabel, ylabel):
    """
    Plot a line graph with multiple lines.

    Args:
        data (pd.DataFrame): The DataFrame containing the data.
        x_column (str): The name of the column to use for the x-axis.
        y_columns (list): A list of column names to use for the y-axis.
        title (str): The title of the graph.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
    """
    plt.figure(figsize=(10, 6))

    x_values = range(len(data))
    for column in y_columns:
        plt.plot(x_values, data[column], marker="o", label=column)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(x_values, data[x_column], rotation=90)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
plot_line_graph(
    data,
    x_column="state",
    y_columns=["median_household_income", "hate_crimes_per_100k_splc"],
    title="Hate Crimes and Household Income by State",
    xlabel="State",
    ylabel="Value",
)

def plot_bar_chart(data, x_column, y_column, title, xlabel, ylabel):
    """
    Plot a bar chart.

    Args:
        data (pd.DataFrame): The DataFrame containing the data.
        x_column (str): The name of the column to use for the x-axis.
        y_column (str): The name of the column to use for the y-axis.
        title (str): The title of the graph.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(data[x_column], data[y_column])

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.show()

plot_bar_chart(
    data,
    x_column="state",
    y_column="hate_crimes_per_100k_splc",
    title="Hate Crimes per 100k Population by State",
    xlabel="State",
    ylabel="Hate Crimes per 100k Population",
)

def plot_scatter_plot(data, x_column, y_column, title, xlabel, ylabel):
    """
    Plot a scatter plot.

    Args:
        data (pd.DataFrame): The DataFrame containing the data.
        x_column (str): The name of the column to use for the x-axis.
        y_column (str): The name of the column to use for the y-axis.
        title (str): The title of the graph.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_column], data[y_column])

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# Plot 3: Share of Non-White Population vs. Share of Non-Citizen Population
plot_scatter_plot(
    data,
    x_column="share_non_white",
    y_column="share_non_citizen",
    title="Share of Non-White Population vs. Share of Non-Citizen Population",
    xlabel="Share of Non-White Population",
    ylabel="Share of Non-Citizen Population",
)