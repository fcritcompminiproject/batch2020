import os
os.chdir("/Ker/")
from keras.preprocessing.image import ImageDataGenerator as idg
from keras.models import Sequential as seq
from keras.layers import Conv2D
from keras.layers import MaxPooling2D as MaxP2D
from keras.layers import Dense, Flatten, Dropout
import os

image_width, image_height = 128,128
rescl = 1. / 255
training_dir = 'data/train'
testing_dir = 'data/validation'
training_samples = 7463
testing_samples = 3411
epoch = 50

model = seq()
model.add(Conv2D(32,[3,3],strides=1,padding='valid',activation='relu',
                        input_shape=(image_width, image_height, 1)))
model.add(Conv2D(32,[3,3],strides=1,padding='valid',activation='relu'))
model.add(MaxP2D(pool_size=(2,2)))

model.add(Conv2D(64,[3,3],strides=1,padding='valid',activation='relu'))
model.add(Conv2D(64,[3,3],strides=1,padding='valid',activation='relu'))
model.add(MaxP2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(9, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='Adam',
              metrics=['accuracy'])


train_datagen = idg(
    rescale=rescl,
    shear_range=0.2,
    zoom_range=0.2,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True)


test_datagen = idg(
    rescale=rescl,
    shear_range=0.2,
    zoom_range=0.2,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True)

model.summary()

train_generator = train_datagen.flow_from_directory(
    training_dir,
    target_size=(image_width, image_height),
    batch_size=32,
    color_mode="grayscale",
    class_mode='categorical')

test_generator = test_datagen.flow_from_directory(
    testing_dir,
    target_size=(image_width, image_height),
    batch_size=32,
    color_mode="grayscale",
    class_mode='categorical')

history= model.fit_generator(
    train_generator,
    steps_per_epoch=training_samples//32,
    epochs=epoch,
    validation_data=test_generator,
    validation_steps=testing_samples//32)

model.save_weights('cnn_weights.h5')
model.save('cnn_model.h5')

