import pickle
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D,Dropout
import matplotlib.pyplot as plt

def loadtrainingdata(pathX, pathy):
    X = pickle.load(open(pathX, "rb"))
    y = pickle.load(open(pathy, "rb"))
    return X, y


def trainmodel(X, y):
    X = X / 255.0

    model = Sequential()

    model.add(Conv2D(32, (2, 2), input_shape=X.shape[1:]))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (2, 2)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))

    model.add(Conv2D(128, (2, 2)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.3))

    model.add(Conv2D(256, (2, 2)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.4))

    model.add(Flatten())

    model.add(Dense(128))
    model.add(Activation("relu"))
    model.add(Dropout(0.45))

    model.add(Dense(7))
    model.add(Activation("softmax"))

    model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=['accuracy'])
    #model.fit(X, y, batch_size=16, epochs=60, validation_split=0.1)
    history = model.fit(X, y, batch_size=16, epochs=70, validation_split=0.1)

    # Plot training & validation accuracy values
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()

    # Plot training & validation loss values
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()
    model.summary()

    return model


def savemodel(model, modelsavepathandname):
    model.save(modelsavepathandname)


X, y = loadtrainingdata("CNN/Trainingdata/XX", "CNN/Trainingdata/yy")
model = trainmodel(X, y)
savemodel(model, "CNN/Models/model2904")
