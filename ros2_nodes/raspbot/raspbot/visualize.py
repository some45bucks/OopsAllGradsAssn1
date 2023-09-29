import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize


df = pd.read_csv(f'../pathlogs/logs_run{1}.csv')

df.columns = ['x', 'y','orientation', 'timestamp']

colormap = 'viridis' 

norm = Normalize(vmin=df['timestamp'].min(), vmax=df['timestamp'].max())

plt.figure(figsize=(8, 6))
ax = plt.gca()

scatter = ax.scatter(df['x'], df['y'], c=df['timestamp'], cmap=colormap, s=100, marker=(3, 0, df['orientation']), linestyle='None')

cbar = plt.colorbar(scatter)
cbar.set_label('Timestamp (seconds)')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.title('Scatter Plot with Gradient-Colored Points')

plt.show()
