import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../Code/regression/data/clean.csv')
atts = ['acousticness', 'danceability', 'duration_ms', 'energy', 'explicit', 'instrumentalness',
        'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo', 'valence']

df = df[atts]

pop = df[df['popularity'] >= 60]


# plt.hist(df['loudness'],  density=True, label='all', alpha=0.5)
# plt.hist(pop['loudness'],  density=True, label='popular', alpha=0.5)
# plt.savefig(f'hist_acousticness.png')
# plt.xlabel(str.capitalize('loudness'))
# plt.ylabel('Frequency (normalized)')
# plt.legend()
# plt.show()

colors = ['green', 'mediumblue']
for att in atts:
    y1 = df[att]
    y2 = pop[att]
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.hist([y1, y2], color=colors)
    n, bins, patches = ax1.hist([y1, y2])
    ax1.cla()  # clear the axis

    # plots the histogram data
    width = (bins[1] - bins[0]) * 0.4
    bins_shifted = bins + width
    ax1.bar(bins[:-1], n[0], width, align='edge', color=colors[0])
    ax2.bar(bins_shifted[:-1], n[1], width, align='edge', color=colors[1])

    # finishes the plot
    ax1.set_ylabel("Count (all)", color=colors[0])
    ax2.set_ylabel("Count (popular)", color=colors[1])
    ax1.tick_params('y', colors=colors[0])
    ax2.tick_params('y', colors=colors[1])
    ax1.set_xlabel(str.capitalize(att))
    plt.tight_layout()
    plt.savefig(f'hist_{att}.png')
    plt.show()


# for att in atts:
