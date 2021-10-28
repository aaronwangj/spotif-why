import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../nn/nn_results.csv', index_col=0)
df['expected'] = df['expected'].str[1:-1]
df['predicted'] = df['predicted'].str[1:-1]
df['expected'] = pd.to_numeric(df.expected)
df['predicted'] = pd.to_numeric(df.predicted)


df['residual'] = df['predicted'] - df['expected']


fig, ax = plt.subplots()

ax.plot(df.predicted, df.residual, 'ro', markersize=0.2)
ax.set_ylabel('Residual', fontsize=20)
ax.set_xlabel('Predicted Popularity', fontsize=20)
ax.set_title('Neural Network Residuals', fontsize=30)

# lims = [
#     np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
#     np.max([ax.get_xlim(), ax.get_ylim()]),  # max of both axes
# ]

# # now plot both limits against eachother
# ax.plot(lims, lims, 'k-', alpha=0.75, zorder=1)
# ax.set_aspect('equal')
# ax.set_xlim(lims)
# ax.set_ylim(lims)

plt.show()
fig.savefig('nn_residuals.png')


df = pd.read_csv('../regression/regression_results.csv', index_col=0)
df['residual'] = df['predicted'] - df['expected']

fig, ax = plt.subplots()

ax.plot(df.predicted, df.residual, 'ro', markersize=0.2)
ax.set_ylabel('Residual', fontsize=20)
ax.set_xlabel('Predicted Popularity', fontsize=20)
ax.set_title('Regression Residuals', fontsize=30)

# lims = [
#     np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
#     np.max([ax.get_xlim(), ax.get_ylim()]),  # max of both axes
# ]

# # now plot both limits against eachother
# ax.plot(lims, lims, 'k-', alpha=0.75, zorder=1)
# ax.set_aspect('equal')
# ax.set_xlim(lims)
# ax.set_ylim(lims)

plt.show()
fig.savefig('regression_residuals.png')
