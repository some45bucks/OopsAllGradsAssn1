import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import Normalize, to_rgba
from matplotlib.cm import ScalarMappable

df = pd.read_csv('../pathlogs/logs.csv')
df.columns = ['x', 'y', 'orientation', 'timestamp']
colormap = 'plasma'

timestamp_min = df['timestamp'].min()
timestamp_max = df['timestamp'].max()

norm = Normalize(vmin=timestamp_min, vmax=timestamp_max)

sm = ScalarMappable(cmap=colormap, norm=norm)
sm.set_array([])  

f, ax = plt.subplots(figsize=(8, 6))
for index, row in df.iterrows():
    color = sm.to_rgba(row['timestamp'])  
    ax.scatter(row['x'], row['y'], c=[color], s=100, marker=(3, 0, row['orientation'] - 90), linestyle='None')

cb = f.colorbar(sm, ax=ax, label='Timestamp (seconds)')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.title('Scatter Plot with Gradient-Colored Points')

plt.show()
