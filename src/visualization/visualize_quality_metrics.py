# Visualize fabric quality metrics and defect rates
import seaborn as sns
import matplotlib.pyplot as plt
def plot_quality_distribution(df):
    sns.histplot(df['quality_score'], kde=True)
    plt.show()
