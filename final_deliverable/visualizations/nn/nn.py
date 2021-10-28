import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from scipy.ndimage.filters import gaussian_filter

df = pd.read_csv('nn_results.csv', index_col=0)
df['expected'] = df['expected'].str[1:-1]
df['predicted'] = df['predicted'].str[1:-1]
df['expected'] = pd.to_numeric(df.expected)
df['predicted'] = pd.to_numeric(df.predicted)
print(df.head())

fig, ax = plt.subplots()

ax.plot(df.expected, df.predicted, 'ro', markersize=0.2)
ax.set_ylabel('Predicted Popularity')
ax.set_xlabel('Expected Popularity')
ax.set_title('Predicted Popularity vs Expected Popularity')

lims = [
    np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
    np.max([ax.get_xlim(), ax.get_ylim()]),  # max of both axes
]

# now plot both limits against eachother
ax.plot(lims, lims, 'k-', alpha=0.75, zorder=1)
ax.set_aspect('equal')
ax.set_xlim(lims)
ax.set_ylim(lims)

plt.show()
fig.savefig('predicted_scatter.png')

fig, ax = plt.subplots()
extent = lims + lims
hb = ax.hexbin(df.expected, df.predicted, gridsize=50,
               cmap=cm.jet, extent=extent)
ax.set_title("Predicted vs Expected using Hexbin")
cb = fig.colorbar(hb, ax=ax)
cb.set_label('counts')
ax.set_ylabel('Predicted Popularity')
ax.set_xlabel('Expected Popularity')

ax.plot(lims, lims, 'w', alpha=0.75, zorder=1, linestyle='dotted')

plt.show()
fig.savefig('predicted_nn_hexbin.png')


def scatter_heatmap(x, y, s):
    heatmap, _, _ = np.histogram2d(
        x, y, bins=1000, range=[lims, lims])
    heatmap = gaussian_filter(heatmap, sigma=s)
    return heatmap.T


fig, axs = plt.subplots(2, 2)
sigmas = [0, 10, 20, 40]

for ax, s in zip(axs.flatten(), sigmas):
    if s == 0:
        ax.plot(df.expected, df.predicted, 'ro', markersize=0.2)
        ax.plot(lims, lims, 'k-', alpha=0.75,
                zorder=1)
        ax.set_title("Predicted vs Expected")
        ax.set_aspect('equal')
        ax.set_xlim(lims)
        ax.xaxis.set_ticks(np.arange(0, 1.01, .2))
        ax.set_ylim(lims)
    else:
        hm = scatter_heatmap(df.expected, df.predicted, s)
        ax.set_xlim(lims)
        ax.xaxis.set_ticks(np.arange(0, 1.01, .2))
        ax.set_ylim(lims)
        ax.imshow(hm, extent=extent, origin='lower',
                  cmap=cm.jet)

        ax.plot(lims, lims, 'w', alpha=0.75,
                zorder=1, linestyle="dotted")
        ax.set_title(
            "Smoothed $\sigma$ = %d" % s)

plt.tight_layout()
plt.show()
fig.savefig('predicted_nn_smoothed.png')
