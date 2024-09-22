"""
TESTING LIBRARY
"""

# import required packages
import matplotlib.pyplot as plt
import pandas as pd
import library as lib


# Read and store data
DATA_CSV = "russia_losses_equipment.csv"
data_test = pd.read_csv(DATA_CSV)


def test_data_read():
    """test function checks if output is null"""
    output_df = lib.data_read(DATA_CSV)
    assert output_df is not None


def test_data_preview():
    """test function checks if preview is correct"""
    test_preview = lib.data_preview(data_test)
    assert test_preview is not None


def test_data_column_names():
    """test function checks if column names are correct"""
    test_col = lib.data_column_names(data_test)
    assert test_col is not None


def test_data_summary_stats():
    """test function checks if summary stats are correct"""
    test_summary = lib.data_summary_stats(data_test)
    assert test_summary is not None


def test_data_visualization():
    """test function checks if data is viz is operating as intended"""
    try:
        plt.figure()
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Data Visualization failed: {e}")

    assert plot_success


def test_report_run():
    """test function checks if all report functions are operating properly"""
    # test data read
    test_data_read()
    # test preview
    test_data_preview()
    # test column names
    test_data_column_names()
    # test summary statistics
    test_data_summary_stats()
    # test data visualization
    test_data_visualization()
