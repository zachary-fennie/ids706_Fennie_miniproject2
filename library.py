"""
LIBRARY
"""

# Required packages
import pandas as pd
import matplotlib.pyplot as plt


def add(x, y):
    """function adds two varibales serves"""
    return x + y


def data_read(input_csv):
    """function reads in a csv to return a df"""
    output_df = pd.read_csv(input_csv)
    return output_df


def data_preview(input_preview):
    """function reads in a df to return the summary statistics"""
    output_preview = input_preview.head()
    return output_preview


def data_column_names(input_column_names):
    """function reads in a df to return the summary statistics"""
    output_columns_names = input_column_names.columns
    return output_columns_names


def data_summary_stats(input_stats):
    """function reads in a df to return the summary statistics"""
    output_stats = input_stats.describe
    return output_stats


def data_visualization(input_viz):
    """function creates a basic data visualization"""
    plt.style.use("seaborn-v0_8-darkgrid")
    plt.plot(input_viz["day"], input_viz["tank"])
    plt.plot(input_viz["day"], input_viz["APC"])
    plt.plot(input_viz["day"], input_viz["field artillery"])
    plt.title("Russian Equipment Losses in the Russian Ukraine War")
    plt.xlabel("Days (Since Invasion Began)")
    plt.ylabel("Equipment Losses")
    plt.legend(["Tanks", "APCs", "Field Artillery"])
    plt.show()
    plt.savefig("main_ground_losses.png")
    plt.close()


def report_run(input_csv):
    """Pandas Descriptive Report"""
    # read CSV
    report_data = data_read(input_csv)
    # Generate a preview
    preview = data_preview(report_data)
    print(preview)
    # Generate full column name list
    col_names = data_column_names(report_data)
    print(col_names)
    # Generate summary statistics
    summary_stats = data_summary_stats(report_data)
    print(summary_stats)
    # Generate data visualization
    data_visualization(report_data)
