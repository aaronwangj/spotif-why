import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn import metrics
import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense


df = pd.read_csv('./data/big_combined.csv')
df.drop_duplicates(subset=['id'], inplace=True)
df = df.sort_values('popularity', ascending=False).drop_duplicates(subset=['Track Name', 'Artist']).sort_index()

df = df[["danceability", "energy", "loudness", "mode", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "popularity"]]

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_df = scaler.fit_transform(df)

scaled_df = pd.DataFrame(scaled_df, columns=["danceability", "energy", "loudness", "mode", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "popularity"])

X = scaled_df.drop('popularity', axis=1).values
Y = scaled_df[['popularity']].values


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=42)
print(len(X_train), len(X_test))
leaky_relu = tf.keras.layers.LeakyReLU(alpha = 0.2)

model = Sequential()
model.add(Dense(250, activation = leaky_relu))
model.add(Dense(300, activation = leaky_relu))
model.add(Dense(200, activation = leaky_relu))
model.add(Dense(10, activation = leaky_relu))
model.add(Dense(50, activation = leaky_relu))
model.add(Dense(1))

opt = keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0001)

model.compile(loss='mean_squared_error', optimizer=opt , metrics = ["MeanAbsoluteError"])


model.fit(x=X_train,y=y_train,
          validation_data=(X_test,y_test),
          batch_size=256,
          epochs=20)

model.summary()

y_pred = model.predict(X_test)

print('MSE:', metrics.mean_squared_error(y_test, y_pred))  
df = pd.DataFrame(data={"expected": list(y_test), "predicted": list(y_pred)})
df.to_csv("../../Visualizations/nn_results.csv")