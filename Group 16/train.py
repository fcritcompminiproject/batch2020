from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.optimizers import SGD

class Train:
	def train():
		# Initializing the CNN
		classifier = Sequential()

		# First convolution layer and pooling
		classifier.add(Convolution2D(64, (3, 3), input_shape=(128, 128, 1), activation='relu'))
		classifier.add(MaxPooling2D(pool_size=(2, 2)))

		# Second convolution layer and pooling
		classifier.add(Convolution2D(32, (3, 3), activation='relu'))
		classifier.add(MaxPooling2D(pool_size=(2, 2)))

		# Flattening the layers
		classifier.add(Flatten())

		# Adding a fully connected layer
		classifier.add(Dense(units=1024,activation='relu'))
		classifier.add(Dropout(0.5))
		classifier.add(Dense(units=512,activation='relu'))
		classifier.add(Dropout(0.5))
		classifier.add(Dense(units=28, activation='softmax')) # softmax for more than 2


		SGD(lr=0.01, decay=0.0005, momentum=0.9, nesterov=True)

		# Compiling the CNN
		classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) # categorical_crossentropy for more than 2


		# Step 2 - Preparing the train/test data and training the model


		from keras.preprocessing.image import ImageDataGenerator

		train_datagen = ImageDataGenerator(
				rescale=1./255,
				shear_range=0.2,
				zoom_range=0.2,
				horizontal_flip=False)

		test_datagen = ImageDataGenerator(rescale=1./255)

		training_set = train_datagen.flow_from_directory('data/train',
														 target_size=(128, 128),
														 batch_size=20,
														 color_mode='grayscale',
														 class_mode='categorical')

		test_set = test_datagen.flow_from_directory('data/test',
													target_size=(128, 128),
													batch_size=20,
													color_mode='grayscale',
													class_mode='categorical') 
		classifier.fit_generator(
				training_set,
				steps_per_epoch=2000*28/5, # No of images in training set
				epochs=5,
				validation_data=test_set,
				validation_steps=500*28/5,# No of images in test set
				shuffle=True)



		#saving
		model_json=classifier.to_json()
		with open("model-bw.json","w")as json_file:
			json_file.write(model_json)
		classifier.save_weights('model-bw.h5')