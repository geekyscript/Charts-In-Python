import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 15, 8, 12, 20]
})

# Seaborn lineplot
sns.lineplot(data=df, x='x', y='y', color='blue')

# Fill under the curve using Matplotlib
plt.fill_between(df['x'], df['y'], color='skyblue', alpha=0.4)

# Titles and labels
plt.title('Area Chart with Seaborn')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.show()
