import seaborn as sns
import matplotlib.pyplot as plt

def df_barplot(df):
    
     # Step 1: Calculate null counts
    none_counts = df.isnull().sum()
    none_counts = none_counts[none_counts > 0]

    # Check if there are any null values
    if none_counts.empty:
        print("No columns with null values.")
        return

    # Step 2: Prepare data for plotting
    plot_data = none_counts.reset_index()
    plot_data.columns = ['Column', 'None Counts']

    # Step 3: Create the bar plot
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data = plot_data, x = "Column", y = "None Counts", hue = "Column", palette = "Set2")
    ax.set_ylabel("Count of None Values")
    ax.set_title("None Value Counts by Column")
    plt.xticks(rotation=90)
    plt.show()
    
    return ax