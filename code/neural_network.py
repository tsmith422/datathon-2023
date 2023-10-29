import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt


def data_preprocessing(df):
    col_to_keep = ['death', 'timeknown', 'cost', 'age', 'blood', 'reflex', 'bloodchem1', 'glucose', 'psych2', 'bloodchem3',
                   'totalcost', 'psych4', 'urine', 'bloodchem6', 'information', 'psych6', 'temperature']
    df = df[col_to_keep]

    df.drop_duplicates()
    
    for col in col_to_keep:
      median = df[col].median()
      df[col].fillna(median, inplace = True)

    df.replace('', 0, inplace=True)
    df.fillna(0, inplace=True)
    return df


def split_feature_label(df):
    y = df['death']
    X = df.drop(columns=['death'])
    return y, X


def standardize(X):
    scaler = StandardScaler()
    X_numeric = scaler.fit_transform(X.select_dtypes(include=['float64']))
    X[X.select_dtypes(include=['float64']).columns] = X_numeric
    return X


def train_model(X, y):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_val, y_val, test_size=.3, random_state=42)

    model = keras.Sequential([
        layers.Input(shape=(X_train.shape[1],)),
        layers.Dense(128, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_val, y_val))

    test_loss, test_accuracy = model.evaluate(X_test, y_test)

    model.save('example.h5')

    print(f'Test accuracy: {test_accuracy}')

    import matplotlib.pyplot as plt

    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['val_accuracy'], label='val_accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0, 1])
    plt.legend(loc='lower right')
    plt.show()


if __name__ == "__main__":
    data_path = './TD_HOSPITAL_TRAIN.csv'
    df = pd.read_csv(data_path)
    cleaned_data = data_preprocessing(df)
    y, X = split_feature_label(cleaned_data)
    X = standardize(X)
    train_model(X, y)


