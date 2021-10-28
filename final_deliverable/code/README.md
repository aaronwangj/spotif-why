# Code README

### Design Decisions ###
We used three models: Multiple Linear Regression, Support Vector Regression, and a Neural Net. 
The first and the last work on our bigger dataset, while the second (SVR) only works on the smaller dataset (as explained in the [abstract](../abstract.pdf)).

### Instructions ###
All three models can be run by simply giving the following command from this directory: "python [filename]".
The first and the third models produce visualizations that need to be closed to continue running.

### Bugs ###
There are no know bugs per se. Running the linear regression throws a multicollinearity warning. However, using our correlation [heatmap](../visualizations/heatmap/features_heatmap.png) we have already chosen independent variables such that they are not highly correlated to each other.
The other issue is with the running of SVR as described in [abstract](../abstract.pdf).
