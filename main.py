import library as lib

if __name__ == "__main__":
    """
    Pandas Descriptive Statistics Report
    """

    # import required libraries
    import pandas as pd
    import matplotlib.pyplot as plt

    # Source - Kaggle: Russia Ukraine War 2022
    # URL: https://www.kaggle.com/datasets/piterfm/2022-ukraine-russian-war?select=russia_losses_equipment.csv
    rus_data = pd.read_csv(
        "/Users/zacharyfennie/Desktop/mids/2024_FALL/IDS_706/ids706_Fennie_miniproject2/russia_losses_equipment.csv"
    )

    # preview the data and confirm successful upload
    preview = rus_data.head()
    print(preview)

    # display the column names
    col_names = rus_data.columns
    print(col_names)

    # produce summary statistics
    summary_stats = rus_data.describe()
    print(summary_stats)

    # create visualization
    plt.style.use("seaborn-v0_8-darkgrid")
    plt.plot(rus_data["day"], rus_data["tank"])
    plt.plot(rus_data["day"], rus_data["APC"])
    plt.plot(rus_data["day"], rus_data["field artillery"])
    plt.title("Russian Equipment Losses in the Russian Ukraine War")
    plt.xlabel("Days (Since Invasion Began)")
    plt.ylabel("Equipment Losses")
    plt.legend(["Tanks", "APCs", "Field Artillery"])

    plt.show()
    plt.savefig("main_ground_losses.png")
    plt.close()
