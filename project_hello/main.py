def dl_index():
    print('''

  dl_p1a: matrix multiplication and finding eigen vectors
  dl_p1b: Random Matrix
  dl_p2:  Solving XOR problem using deep feed forward network
  dl_p3:  Implementing deep neural network for performing binary classification task.
  dl_p4a: Using Feed Forward Network with multiple hidden layers for performing multiclass classification and predicting the class.
  dl_p4b: Using a deep feed forward network with two hidden layers for performing classification and predicting the probability of class.
  dl_p5a: Evaluating feed forward deep network for regression using KFold cross validation.
  dl_p5b: Evaluating feed forward deep network for multiclass Classification using KFold cross-validation.
  dl_p6a: Implement 12 regularization with alpha=0.001
  dl_p6b: Evaluating feed forward deep network for multiclass Classification using KFold cross-validation.
  dl_p6c: Replace 12 regularization with l1 regularization.
  dl_p7:  Demonstrate recurrent neural network that learns to perform sequence analysis for stock price.
  dl_p8:  Performing encoding and decoding of images using deep autoencoder.
  dl_p9:  Implementation of convolutional neural network to predict numbers from number
  dl_p10: Denoising of images using autoencoder.

  ''')


def dl_p1a():
    print('''
import tensorflow as tf
print("Matrix Multiplication Demo")
x=tf.constant([1,2,3,4,5,6],shape=[2,3])
print(x)
y=tf.constant([7,8,9,10,11,12],shape=[3,2])
print(y)
z=tf.matmul(x,y)
print("Product:",z)
e_matrix_A=tf.random.uniform([2,2],minval=3,maxval=10,dtype=tf.float32,name="matrixA")
print("Matrix A:\\n{}\\n\\n".format(e_matrix_A))
eigen_values_A,eigen_vectors_A=tf.linalg.eigh(e_matrix_A)
print("Eigen Vectors:\\n{}\\n\\nEigen Values:\\n{}\\n".format(eigen_vectors_A,eigen_values_A))
''')


def dl_p1b():
    print('''
import tensorflow as tf
random_matrix = tf.random.uniform(shape=[3, 3], minval=1, maxval=10)
eigenvalues, eigenvectors = tf.linalg.eigh(random_matrix)
# Print the results
print("Random Matrix:\\n", random_matrix.numpy())
print("\\nEigenvalues:\\n", eigenvalues.numpy())
print("\\nEigenvectors:\\n", eigenvectors.numpy())
''')


def dl_p2():
    print('''
import numpy as np
from keras.layers import Dense
from keras.models import Sequential
model=Sequential()
model.add(Dense(units=2,activation='relu',input_dim=2))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
print(model.summary())
print(model.get_weights())
X=np.array([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
Y=np.array([0.,1.,1.,0.])
model.fit(X,Y,epochs=1000,batch_size=4)
print(model.get_weights())
print(model.predict(X,batch_size=4))
''')


def dl_p3():
    print('''
#!pip install keras
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
names =["No. of pregnancies","Glucose level","Blood Pressure","skin thickness","Insulin","BMI","Diabetes pedigree","Age","Class"]
df=pd.read_csv("pima-indians-diabetes.data.csv",names = names)
print(df.head(3))
binaryc = Sequential()
from tensorflow.tools.docs.doc_controls import doc_in_current_and_subclasses
binaryc.add(Dense(units=10,activation='relu',input_dim=8))
binaryc.add(Dense(units=8,activation='relu'))
binaryc.add(Dense(units=1,activation='sigmoid'))
binaryc.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
X =df.iloc[:,:-1]
y = df.iloc[:,-1]
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(X,y,test_size = 0.25, random_state=1)
xtrain.shape
ytrain.shape
binaryc.fit(xtrain,ytrain,epochs=200,batch_size=20)
predictions=binaryc.predict(xtest)
predictions.shape
class_labels=[]
for i in predictions:
    if(i>0.5):
        class_labels.append(1)
    else:
        class_labels.append(0)
class_labels
from sklearn.metrics import accuracy_score
print('Accuracy Score', accuracy_score(ytest,class_labels))
''')


def dl_p4a():
    print('''
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
df=pd.read_csv("flowers.csv")
print(df.head())
X =df.iloc[:,:-1].astype(float)
y = df.iloc[:,-1]
print(X.shape) ##print not necessary
print(y.shape) ##print not necessary
from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
y = lb.fit_transform(y)
print(y)
##print not necessary
from tensorflow.keras.utils import to_categorical
encoded_Y = to_categorical(y)
print(encoded_Y) ##print not necessary
model = Sequential()
model.add(Dense(8,activation='relu',input_dim=4))
model.add(Dense(6,activation='relu'))
model.add(Dense(3,activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
odel.fit(X,encoded_Y,epochs=100,batch_size=10)
predictions = model.predict(X)
for i in range(35,130,3):
    print(predictions[i],encoded_Y[i])
import numpy as np
a =[]
for i in range(0,150):
    a.append(np.argmax(predictions[i]))
newdf = pd.DataFrame(list(zip(a,y)),columns = ['Predicted','True Label'])
print(newdf)
''')


def dl_p4b():
    print('''
from keras.models import Sequential
from keras.layers import Dense,InputLayer
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
X, Y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)
# Normalize data
scaler = MinMaxScaler()
scaler.fit(X)
X =scaler.transform(X)
# Create model
model = Sequential()
model.add(InputLayer(input_shape=(2,)))
model.add(Dense(4, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model with binary crossentropy loss
model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(X, Y, epochs=500)
Xnew, Yreal = make_blobs(n_samples=3, centers=2, n_features=2, random_state=1)
Xnew = scaler.transform(Xnew)
Ynew = model.predict(Xnew)
# Convert to class predictions
Yclass = (Ynew > 0.5).astype(int)
print(Yclass)
for i in range(len(Xnew)):
    print(f"X={Xnew[i]},Predicted_probability={Ynew[i]},Predicted_class={Yclass[i]}")
''')


def dl_p5a():
    print('''
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from keras.models import Sequential
from keras.layers import Dense
from scikeras.wrappers import KerasRegressor
# Load the dataset correctly, skipping the first row (header)
dataframe = pd.read_csv("housing.csv", sep=',', header=0)
print("Shape of dataset:", dataframe.shape)
print("First few rows of dataset:")
print(dataframe.head())
# Extract features (X) and target variable (Y)
X =dataframe.drop(columns=['MEDV']).values
# Features (all columns except 'MEDV')
Y =dataframe['MEDV'].values
#Target variable ('MEDV')
# Check the shape of X (number of features)
print("Shape of X (features):", X.shape)
# Define the wider model function
def wider_model():
    model = Sequential()
    model.add(Dense(15,input_dim=X.shape[1], kernel_initializer='normal' , activation='relu'))
    model.add(Dense(13, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model
#Create pipeline with standardization and Keras model
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp',KerasRegressor(build_fn=wider_model, epochs=10, batch_size=5)))
pipeline = Pipeline(estimators)
# Define KFold cross-validation
kfold = KFold(n_splits=10, shuffle=True, random_state=42)
try:
    # Evaluate pipeline using cross-validation
    results = cross_val_score(pipeline, X, Y, cv=kfold)
    print("Wider: %.2f (%.2f) MSE" % (results.mean(), results.std()))
except ValueError as e:
    print("Error during cross-validation:", e)
''')


def dl_p5b():
    print('''
from sklearn.datasets import make_classification
from sklearn.model_selection import KFold
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn.metrics import accuracy_score
# Generate a random multiclass classification dataset
X, y = make_classification(n_samples=100,
n_features=20,
n_informative=2,
n_redundant=0,
n_classes=2,
n_clusters_per_class=2,
random_state=42)
# Convert the target variable to categorical format
y = to_categorical(y)
# Define the k-fold cross-validator
n_splits = 5
kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
# Define the feed-forward deep network model
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# Perform k-fold cross-validation
fold_accuracies = []
for train_index, val_index in kf.split(X):
    X_train, X_val = X[train_index], X[val_index]
    y_train, y_val = y[train_index], y[val_index]
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))
    y_pred_prob = model.predict(X_val)
    y_pred = y_pred_prob.argmax(axis=1) # Get the predicted class index with highest probability
    accuracy = accuracy_score(y_val.argmax(axis=1), y_pred)
    fold_accuracies.append(accuracy)
# Calculate the mean accuracy across all folds
mean_accuracy = sum(fold_accuracies) / len(fold_accuracies)
print(f'Mean accuracy: {mean_accuracy:.2f}')
''')


def dl_p6a():
    print('''
from matplotlib import pyplot
from sklearn.datasets import make_moons
from keras.models import Sequential
from keras.layers import Dense
X,Y=make_moons(n_samples=100,noise=0.2,random_state=1)
n_train=30
trainX,testX=X[:n_train,:],X[n_train:]
trainY,testY=Y[:n_train],Y[n_train:]
#print(trainX)
#print(trainY)
#print(testX)
#print(testY)
model=Sequential()
model.add(Dense(500,input_dim=2,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
history=model.fit(trainX,trainY,validation_data=(testX,testY),epochs=4000)
pyplot.plot(history.history['accuracy'],label='train')
pyplot.plot(history.history['val_accuracy'],label='test')
pyplot.legend()
pyplot.show()
''')


def dl_p6b():
    print('''
from matplotlib import pyplot
from sklearn.datasets import make_moons
from keras.models import Sequential
from keras.layers import Dense
from keras.regularizers import l2
X,Y=make_moons(n_samples=100,noise=0.2,random_state=1)
n_train=30
trainX,testX=X[:n_train,:],X[n_train:]
trainY,testY=Y[:n_train],Y[n_train:]
#print(trainX)
#print(trainY)
#print(testX)
#print(testY)
model=Sequential()
model.add(Dense(500,input_dim=2,activation='relu',kernel_regularizer=l2(0.001)))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
history=model.fit(trainX,trainY,validation_data=(testX,testY),epochs=4000)
pyplot.plot(history.history['accuracy'],label='train')
pyplot.plot(history.history['val_accuracy'],label='test')
pyplot.legend()
pyplot.show()
''')


def dl_p6c():
    print('''
from matplotlib import pyplot
from sklearn.datasets import make_moons
from keras.models import Sequential
from keras.layers import Dense
from keras.regularizers import l1_l2
X,Y=make_moons(n_samples=100,noise=0.2,random_state=1)
n_train=30
trainX,testX=X[:n_train,:],X[n_train:]
trainY,testY=Y[:n_train],Y[n_train:]
#print(trainX)
#print(trainY)
#print(testX)
#print(testY)
model=Sequential()
model.add(Dense(500,input_dim=2,activation='relu',kernel_regularizer=l1_l2(l1=0.001,l2=0.001)
))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
history=model.fit(trainX,trainY,validation_data=(testX,testY),epochs=4000)
pyplot.plot(history.history['accuracy'],label='train')
pyplot.plot(history.history['val_accuracy'],label='test')
pyplot.legend()
pyplot.show()
''')


def dl_p7():
    print('''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from sklearn.preprocessing import MinMaxScaler
# Importing the training dataset
dataset_train = pd.read_csv('C:/Users/HP/Downloads/Google_Stock_Price_Train.csv')
training_set = dataset_train.iloc[:, 1:2].values
# Scaling the training set
sc = MinMaxScaler(feature_range=(0, 1))
training_set_scaled = sc.fit_transform(training_set)
X_train = []
Y_train = []
for i in range(60, 1258):
    X_train.append(training_set_scaled[i-60:i, 0])
    Y_train.append(training_set_scaled[i, 0])
X_train, Y_train = np.array(X_train), np.array(Y_train)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
# Building the LSTM model
regressor = Sequential()
regressor.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=50))
regressor.add(Dropout(0.2))
regressor.add(Dense(units=1))
# Compiling the model
regressor.compile(optimizer='adam', loss='mean_squared_error')
# Fitting the model to the training set
regressor.fit(X_train, Y_train, epochs=100, batch_size=32)
# Predicting the stock prices
dataset_test = pd.read_csv('C:/Users/HP/Downloads/Google_Stock_Price_Test.csv')
real_stock_price = dataset_test.iloc[:, 1:2].values
dataset_total = pd.concat((dataset_train['Open'], dataset_test['Open']), axis=0)
inputs = dataset_total[len(dataset_total)- len(dataset_test)- 60:].values
inputs = inputs.reshape(-1, 1)
inputs = sc.transform(inputs)
X_test = []
for i in range(60, 80):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_stock_price = regressor.predict(X_test)
# Inverse scaling for predicted prices
predicted_stock_price = sc.inverse_transform(predicted_stock_price)
plt.plot(real_stock_price, color='red', label='Real Google Stock Price')
plt.plot(predicted_stock_price, color='blue', label='Predicted Stock Price')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')
plt.legend()
plt.show()
''')


def dl_p8():
    print('''
import keras
from keras import layers
from keras.datasets import mnist
import numpy as np
encoding_dim = 32
input_img = keras.Input(shape=(784,))
#Input image
# "encoded" is the encoded representation of the input
encoded = layers.Dense(encoding_dim, activation='relu')(input_img)
# "decoded" is the lossy reconstruction of the input
decoded = layers.Dense(784, activation='sigmoid')(encoded)
# Creating autoencoder model
autoencoder = keras.Model(input_img, decoded)
encoder = keras.Model(input_img, encoded) #Create the encoder model
encoded_input = keras.Input(shape=(encoding_dim,))
# Retrieve the last layer of the autoencoder model
decoder_layer = autoencoder.layers[-1]
# Create the decoder model
decoder = keras.Model(encoded_input, decoder_layer(encoded_input))
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
# Scale and make train and test dataset
(X_train, _), (X_test, _) = mnist.load_data()
X_train = X_train.astype('float32') / 255.
X_test = X_test.astype('float32') / 255.
X_train = X_train.reshape((len(X_train), np.prod(X_train.shape[1:])))
X_test = X_test.reshape((len(X_test), np.prod(X_test.shape[1:])))
print(X_train.shape)
print(X_test.shape)
# Train autoencoder with training dataset
autoencoder.fit(X_train, X_train,
epochs=50,
batch_size=256,
shuffle=True,
validation_data=(X_test, X_test))
encoded_imgs = encoder.predict(X_test)
decoded_imgs = decoder.predict(encoded_imgs)
import matplotlib.pyplot as plt
n =10
plt.figure(figsize=(40, 4))
for i in range(10):
# Howmanydigits we will display
    ax = plt.subplot(3, 20, i + 1)
    plt.imshow(X_test[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax = plt.subplot(3, 20, i + 1 + 20)
    # Display original
    # Display encoded image
    plt.imshow(encoded_imgs[i].reshape(8, 4)) # Adjust shape if necessary
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax = plt.subplot(3, 20, 2 * 20 + i + 1)
    # Display reconstruction
    plt.imshow(decoded_imgs[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()
''')


def dl_p9():
    print('''
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense,Conv2D,Flatten
import matplotlib.pyplot as plt
#download mnist data and split into train and test sets
(X_train,Y_train),(X_test,Y_test)=mnist.load_data()
#plot the first image in the dataset
plt.imshow(X_train[0])
plt.show()
print(X_train[0].shape)
X_train=X_train.reshape(60000,28,28,1)
X_test=X_test.reshape(10000,28,28,1)
Y_train=to_categorical(Y_train)
Y_test=to_categorical(Y_test)
Y_train[0]
print(Y_train[0])
model=Sequential()
#add model layers
#learn image features
model.add(Conv2D(64,kernel_size=3,activation='relu',input_shape=(28,28,1)))
model.add(Conv2D(32,kernel_size=3,activation='relu'))
model.add(Flatten())
model.add(Dense(10,activation='softmax'))
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
#train
model.fit(X_train,Y_train,validation_data=(X_test,Y_test),epochs=3)
print(model.predict(X_test[:4]))
#actual results for 1st 4 images in the test set
print(Y_test[:4])

''')


def dl_p10():
    print('''
import keras
from keras.datasets import mnist
from keras import layers
import numpy as np
from keras.callbacks import TensorBoard
import matplotlib.pyplot as plt
(X_train, _), (X_test, _) = mnist.load_data()
X_train = X_train.astype('float32') / 255.
X_test = X_test.astype('float32') / 255.
X_train = np.reshape(X_train, (len(X_train), 28, 28, 1))
X_test = np.reshape(X_test, (len(X_test), 28, 28, 1))
noise_factor = 0.5
X_train_noisy = X_train + noise_factor * np.random.normal(loc=0.0, scale=1.0,
size=X_train.shape)
X_test_noisy = X_test + noise_factor * np.random.normal(loc=0.0, scale=1.0,
size=X_test.shape)
X_train_noisy = np.clip(X_train_noisy, 0., 1.)
X_test_noisy = np.clip(X_test_noisy, 0., 1.)
n =10
plt.figure(figsize=(20, 2))
for i in range(1, n + 1):
    ax = plt.subplot(1, n, i)
    plt.imshow(X_test_noisy[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()
input_img = keras.Input(shape=(28, 28, 1))
x =layers.Conv2D(32, (3, 3), activation='relu', padding='same')(input_img)
x =layers.MaxPooling2D((2, 2), padding='same')(x)
x =layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
encoded = layers.MaxPooling2D((2, 2), padding='same')(x)
x =layers.Conv2D(32, (3, 3), activation='relu', padding='same')(encoded)
x =layers.UpSampling2D((2, 2))(x)
x =layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x =layers.UpSampling2D((2, 2))(x)
decoded = layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)
autoencoder = keras.Model(input_img, decoded)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
autoencoder.fit(X_train_noisy, X_train,
    epochs=3,
    batch_size=128,
    shuffle=True,
    validation_data=(X_test_noisy, X_test),
    callbacks=[TensorBoard(log_dir='/tmo/tb', histogram_freq=0, write_graph=False)])
predictions = autoencoder.predict(X_test_noisy)
m=10
plt.figure(figsize=(20, 2))
for i in range(1, m + 1):
    ax = plt.subplot(1, m, i)
    plt.imshow(predictions[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()
''')


def nlp_index():
    print('''
  nlp_p1b: Install NLTK packages.
  nlp_p1c: Convert the given text into speech.
  nlp_p1d: Convert the audio file into speech.
  nlp_p2a:  Study of various corpus– Brown, Inaugural, Reuters, udhr with various methods like fields, raw, words, sents, categories.
  nlp_p2b:  Create and use your own corpora (plaintext, categorical).
  nlp_p2c:  Study conditional frequency distribution.
  nlp_p2d: Study of tagged corpora with methods like tagged_sents, tagged_words.
  nlp_p2e: Write a program to find the most frequent noun tags.
  nlp_p2f: Mapwords to the properties using Python Dictionaries.
  nlp_p2g:  Defaulttagger,  Regular Expression Tagger,  Unigram Tagger
  nlp_p2h: Find different words from a given plaintext without any spaces by comparing this text with a given corpus of words. Also find the score of words.
  nlp_p3a: Study of Wordnet Dictionary with methods as synsets, definitions, examples, antonyms.
  nlp_p3b:  Study lemmas, hyponyms, hypernyms, entailments.
  nlp_p3c:  Write a program using python to find synonym and antonym of word "active" using Wordnet.
  nlp_p3d: Compare two nouns.
  nlp_p3e: Handling stopword - Using nltk, add or remove stop words in NLTK's Default stop word list. ,  Using Gensim, add or remove stop words in Default Gensim stop words List. , Using SpaCy, , add or remove Stop Words in Default SpaCy stop words List.
  nlp_p4a: Tokenization using Python’s split() function.
  nlp_p4b: Tokenization using Regular Expression (RegEx).
  nlp_p4c: Tokenization using NLTK.
  nlp_p4d:  Tokenization using spaCy library
  nlp_p4e:  Tokenization using Keras.
  nlp_p4f:  Tokenization using Gensim.
  nlp_p5a:   Wordtokenization in Hindi
  nlp_p5b:  Generate similar sentences from a given Hindi text input
  nlp_p5c:   Identify the Indian language from the given text.
  nlp_p6a:   Part of speech Tagging and chunking of user defined text.
  nlp_p6b:  NamedEntity recognition of user defined text.
  nlp_p6c:  NamedEntity recognition with diagram using NLTK corpus– treebank.
  nlp_p7a:   Define grammar using nltk. Analyse a sentence using the same.
  nlp_p7b:  Accept the input string with Regular expression of FA: 101+
  nlp_p7c:  Accept the input string with Regular expression of FA:(a+b)*bba
  nlp_p7d:   Implementation of Deductive Chart Parsing using context free grammar and a given sentence.
  nlp_p8a:   Study PorterStemmer, LancasterStemmer, RegexpStemmer, SnowballStemmer.
  nlp_p8b:  Study WordNet Lemmatizer.
  nlp_p9:   Implement Naive Bayes classifier
  nlp_p10a:   Speech Tagging.
  nlp_p10b:  Statistical Parsing
  nlp_p10c:  Parse a sentence and draw a tree using malt parsing. 
  nlp_p11a:   Multiword Expressions in NLP
  nlp_p11b:   Normalized Web Distance and Word Similarity
  nlp_p11c:   WordSense Disambiguation.

  ''')


def nlp_p1b():
    print('''
!pip install nltk
      ''')


def nlp_p1c():
    print('''
# text to speech 
# pip install gtts 
# pip install playsound 
from playsound import playsound
# import required for text to speech conversion 
from gtts import gTTS
mytext = "Welcome to Practical 1: Natural Language programming, Harshad" 
language = "en" 
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("myfile.mp3") 
playsound("myfile.mp3") 
print("Text converted into speech succesfully")
      ''')


def nlp_p1d():
    print('''
#pip3 install SpeechRecognition pydub 
import speech_recognition as sr
filename = "Harshad.wav" 
# initialize the recognizer 
r = sr.Recognizer() 
# open the file 
with sr.AudioFile(filename) as source: 
# listen for the data (load audio to memory) 
    audio_data = r.record(source) 
# recognize (convert from speech to text) 
    text = r.recognize_google(audio_data) 
    print(text)
      ''')


def nlp_p2a():
    print('''
 import nltk
 nltk.download('brown')
 from nltk.corpus import brown
 print ('File ids of brown corpus',brown.fileids())
 'Let’s pick out the first of these texts — Emma by Jane Austen — and give it a short
 name, emma, then find out how many words it contains:'
 ca01 = brown.words('ca01')
 # display first few words
 print('ca01 has following words:',ca01)
 #Total number of words in ca01
 print('ca01 has',len(ca01),'words')
 #categories or files
 print ('Categories or file in brown corpus:\n')
 print (brown.categories())
 'display other information about each text, by looping over all the values of fileid
 corresponding to the brown file identifiers listed earlier and then computing statistics
 for each text.'
 print ('\n\nStatistics for each text:\n')
 print('AvgWordLen\tAvgSentenceLen\tno.ofTimesEachWordAppearsOnAvg\t\tFileName')
 for fileid in brown.fileids():
 num_chars = len(brown.raw(fileid))
 num_words = len(brown.words(fileid))
 num_sents = len(brown.sents(fileid))
 num_vocab = len(set([w.lower() for w in brown.words(fileid)]))
 print (int(num_chars/num_words),'\\t\\t\\t', int(num_words/num_sents),'\\t',
 int(num_words/num_vocab),'\\t\\t\\t', fileid)
      ''')


def nlp_p2b():
    print('''
import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'D:\\MSCIT\\SEM 4\\2 Natural Language Processing\\Practicals\\Practical 2'  # Use a raw string for the path
filelist = PlaintextCorpusReader(corpus_root, '.*')
print('\\n File list: \\n')
print(filelist.fileids())
print(filelist.root)
# Display other information about each text
print('\\n\\nStatistics for each text:\\n')
print('AvgWordLen\\tAvgSentenceLen\\tno.ofTimesEachWordAppearsOnAvg\\tFileName')
for fileid in filelist.fileids():
    num_chars = len(filelist.raw(fileid))
    num_words = len(filelist.words(fileid))
    num_sents = len(filelist.sents(fileid))
    num_vocab = len(set([w.lower() for w in filelist.words(fileid)]))

    print(int(num_chars / num_words), '\\t\\t\\t', int(num_words / num_sents), '\\t\\t\\t', int(num_words / num_vocab), '\\t\\t', fileid)
      ''')


def nlp_p2c():
    print('''
# Process a sequence of pairs
text = ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
pairs = [('news', 'The'), ('news', 'Fulton'), ('news', 'County'), ...]
import nltk
from nltk.corpus import brown
fd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)
genre_word = [
    (genre, word)
    for genre in ['news', 'romance']
    for word in brown.words(categories=genre)
]
print(len(genre_word))
print(genre_word[:4])
print(genre_word[-4:])
cfd = nltk.ConditionalFreqDist(genre_word)
print(cfd)
print(cfd.conditions())
print(cfd['news'])
print(cfd['romance'])
print(list(cfd['romance']))
from nltk.corpus import inaugural
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target)
)
from nltk.corpus import udhr
languages = [
    'Chickasaw', 'English', 'German_Deutsch',
    'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik'
]
cfd = nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1')
)
cfd.tabulate(conditions=['English', 'German_Deutsch'], samples=range(10), cumulative=True)
      ''')


def nlp_p2d():
    print('''
import nltk
from nltk import tokenize
nltk.download('punkt')
nltk.download('words')
para = "Hello! My name is Harshad Patil. Today we will be learning NLTK."
sents = tokenize.sent_tokenize(para)
print("\nsentence tokenization\n===================\n",sents)
# word tokenization
print("\nword tokenization\n===================\n")
for index in range(len(sents)):
 words = tokenize.word_tokenize(sents[index])
 print(words)
      ''')


def nlp_p2e():
    print('''
import nltk
from collections import defaultdict
text = nltk.word_tokenize("Harshad likes to play cricket. Harshad does not like to play with hearts.")
tagged = nltk.pos_tag(text)
print(tagged)
# Checking if it is a noun or not
addNounWords = []
count = 0
for words in tagged:
    val = tagged[count][1]
    if val in ('NN', 'NNS', 'NNPS', 'NNP'):
        addNounWords.append(tagged[count][0])
    count += 1
print(addNounWords)
temp = defaultdict(int)
# Memoizing count
for sub in addNounWords:
    for wrd in sub.split():
        temp[wrd] += 1
# Getting max frequency
res = max(temp, key=temp.get)
# Printing result
print("Word with maximum frequency: " + str(res))

      ''')


def nlp_p2f():
    print('''
#creating and printing a dictionay by mapping word with its properties
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))
      ''')


def nlp_p2g():
    print('''
import nltk
from nltk.tag import DefaultTagger
exptagger = DefaultTagger('NN')
from nltk.corpus import treebank
testsentences = treebank.tagged_sents()[1000:]
print(exptagger.evaluate(testsentences))
# Tagging a list of sentences
import nltk
from nltk.tag import DefaultTagger
exptagger = DefaultTagger('NN')
print(exptagger.tag_sents([['Hi', ','], ['How', 'are', 'you', '?']]))

#Regular Expression Tagger
from nltk.corpus import brown 
from nltk.tag import RegexpTagger 
test_sent = brown.sents(categories='news')[0] 
regexp_tagger = RegexpTagger( 
[(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal numbers 
(r'(The|the|A|a|An|an)$', 'AT'),   # articles 
(r'.*able$', 'JJ'),                # adjectives 
(r'.*ness$', 'NN'),   # nouns formed from adjectives      
(r'.*ly$', 'RB'),     # adverbs        
(r'.*s$', 'NNS'),         # plural nouns   
(r'.*ing$', 'VBG'),   # gerunds              
(r'.*ed$', 'VBD'),  # past tense verbs 
(r'.*', 'NN')    # nouns (default)                    
]) 
print(regexp_tagger) 
print(regexp_tagger.tag(test_sent)) 
#UniTagger
from nltk.tag import UnigramTagger
from nltk.corpus import treebank
train_sents = treebank.tagged_sents()[:10]
tagger = UnigramTagger(train_sents) # Initializing 
print(treebank.sents()[0])
print('\n',tagger.tag(treebank.sents()[0]))
tagger.tag(treebank.sents()[0])
tagger = UnigramTagger(model ={'Pierre': 'NN'}) #Overriding the context model 
print('\n',tagger.tag(treebank.sents()[0]))
      ''')


def nlp_p2h():
    print('''
from __future__ import with_statement
import re
words = []
testword = []
ans = []
print("MENU")
print("-----------")
print("1. Hash tag segmentation")
print("2. URL segmentation")
print("Enter the input choice for performing word segmentation:")
choice = int(input())
if choice == 1:
    text = "#whatismyname"
    print("input with HashTag", text)
    pattern = re.compile("[^\\w']")
    a = pattern.sub('', text)
elif choice == 2:
    text = "www.whatismyname.com"
    print("input with URL", text)
    a = re.split(r'\\s|(?<!\\d)[,.](?!\\d)', text)
    splitwords = ["www", "com", "in"]
    a = "".join([each for each in a if each not in splitwords])
else:
    print("Wrong choice...try again")
    a = ''
if a:
    print(a)
    for each in a:
        testword.append(each)

    test_length = len(testword)
    try:
        with open(r"words.txt", 'r') as f:
            lines = f.readlines()
            words = [(e.strip()) for e in lines]
    except FileNotFoundError:
        print("The word list file was not found. Please check the file path.")
        exit()
    def Seg(a, length):
        ans = []
        for k in range(0, length + 1):
            if a[0:k] in words:
                print(a[0:k], "-appears in the corpus")
                ans.append(a[0:k])
                break
        if ans:
            g = max(ans, key=len)
            return g
        return ''
    test_tot_itr = 0
    answer = []
    N = 37
    while test_tot_itr < test_length:
        ans_words = Seg(a, test_length)
        if ans_words:
            test_itr = len(ans_words)
            answer.append(ans_words)
            a = a[test_itr:test_length]
            test_tot_itr += test_itr
    Aft_Seg = " ".join([each for each in answer])
    print("Output:")
    print("---------")
    print("After segmentation:", Aft_Seg)
    C = len(answer)
    score = C * N / N
    print("Score:", score)
      ''')


def nlp_p3a():
    print('''
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
print(wordnet.synsets("sunrise"))
print("My word is Sunrise:- \\n", "Definition:", wordnet.synset("sunrise.n.01").definition())
print("Examples:", wordnet.synset("sunrise.n.01").examples())
anto = wordnet.lemma('sunrise.n.01.sunrise')
print("\\nAntonym of word Sell (Noun):", anto.antonyms())
      ''')


def nlp_p3b():
    print('''
import nltk
from nltk.corpus import wordnet
print(wordnet.synsets("computer"))
print(wordnet.synset("computer.n.01").lemma_names())
# All lemmas for each synset.
for e in wordnet.synsets("computer"):
    print(f'{e} --> {e.lemma_names()}')
# Print all lemmas for a given synset
print(wordnet.synset('computer.n.01').lemmas())
# Get the synset corresponding to lemma
print(wordnet.lemma('computer.n.01.computing_device').synset())
# Get the name of the lemma
print(wordnet.lemma('computer.n.01.computing_device').name())
# Hyponyms give abstract concepts of the word that are much more specific
# The list of hyponyms words of the computer
syn = wordnet.synset('computer.n.01')
print(syn.hyponyms())
print([lemma.name() for synset in syn.hyponyms() for lemma in synset.lemmas()])
# The semantic similarity in WordNet
vehicle = wordnet.synset('vehicle.n.01')
car = wordnet.synset('car.n.01')
print(car.lowest_common_hypernyms(vehicle))
      ''')


def nlp_p3c():
    print('''
from nltk.corpus import wordnet 
print( wordnet.synsets("active")) 
print(wordnet.lemma('active.a.01.active').antonyms())
      ''')


def nlp_p3d():
    print('''
import nltk 
from nltk.corpus import wordnet 
syn1 = wordnet.synsets('football') 
syn2 = wordnet.synsets('soccer') 
# A word may have multiple synsets, so need to compare each synset of word1 with synset of word2 
for s1 in syn1:
    for s2 in syn2:
        print("Path similarity of: ")
        print(s1, '(', s1.pos(), ')', '[', s1.definition(), ']')
        print(s2, '(', s2.pos(), ')', '[', s2.definition(), ']')
        print("   is", s1.path_similarity(s2))
        print()
      ''')


def nlp_p3e():
    print('''
#Using nltk, add or remove stop words in NLTK's Default stop word list.
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
text = "Harshad likes to play cricket, however he is not too fond of basketball."
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
print(tokens_without_sw)
# Add the word 'play' to the NLTK stop word collection
all_stopwords = stopwords.words('english')
all_stopwords.append('play')
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)
# Remove ‘not’ from stop word collection
all_stopwords.remove('not')
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)
# Using Gensim, add or remove stop words in Default Gensim stop words List.
# pip install gensim nltk
import gensim
from gensim.parsing.preprocessing import remove_stopwords, STOPWORDS
import nltk
from nltk.tokenize import word_tokenize
# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
text = "Harshad likes to play cricket, however he is not too fond of basketball."
filtered_sentence = remove_stopwords(text)
print(filtered_sentence)
all_stopwords = gensim.parsing.preprocessing.STOPWORDS
print(all_stopwords)
# The following script adds 'likes' and 'play' to the list of stop words in Gensim:
all_stopwords_gensim = STOPWORDS.union(set(['likes', 'play']))
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
print(tokens_without_sw)
# Output:
# ['Harshad', 'cricket', ',', 'fond', 'basketball', '.']
# The following script removes the word "not" from the set of stop words in Gensim:
sw_list = {"not"}
all_stopwords_gensim = STOPWORDS.difference(sw_list)
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
print(tokens_without_sw)
# Using SpaCy, , add or remove Stop Words in Default SpaCy stop words List.
#pip install spacy 
#python -m spacy download en_core_web_sm 
#python -m spacy download en 
import spacy 
import nltk 
from nltk.tokenize import word_tokenize 
sp = spacy.load('en_core_web_sm') 
#add the word play to the NLTK stop word collection 
all_stopwords = sp.Defaults.stop_words 
all_stopwords.add("play") 
text = "Harshad likes to play cricket, however he is not too fond of basketball." 
text_tokens = word_tokenize(text) 
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords] 
print(tokens_without_sw) 
#remove 'not' from stop word collection 
all_stopwords.remove('not') 
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords] 
print(tokens_without_sw) 
      ''')


def nlp_p4a():
    print('''
 text = """ This tool is an a beta stage
 Electric cars are running petrol cars raw and rough experience.It also supports custom battery
 model, prebuilt charging model, and the Autonomous Driving API
 You can use this tool for creation of monitors, alarms, and dashboards that spotlight changes.
 The release of these three tools will enable developers to create visual rich experiences for
 Electric cars with advanced infotainment systems. Electric car manufacturers describes these
 tools as the collection of tech and tools for creating visually rich and interactive driving
 experiences"""
 data = text.split('.')
 for i in data:
    print(i.strip())
      ''')


def nlp_p4b():
    print('''
import nltk
# import RegexpTokenizer() method from nltk
from nltk.tokenize import RegexpTokenizer
# Create a reference variable for Class RegexpTokenizer
tk = RegexpTokenizer('\\s+', gaps = True)
# Create a string input
str = "winner winner chicken dinner"
tokens = tk.tokenize(str) # Use tokenize method

print(tokens)
      ''')


def nlp_p4c():
    print('''
import nltk
from nltk.tokenize import RegexpTokenizer

# Create a reference variable for Class RegexpTokenizer
tk = RegexpTokenizer('\\s+', gaps = True)

# Create a string input
str = "There will only one winner, let's go!! "

tokens = tk.tokenize(str)		# Use tokenize method
print(tokens)
      ''')


def nlp_p4d():
    print('''
import spacy
nlp = spacy.blank("en")
str = "Mayday! Mayday! Officer prince reporting enemey artilary heading towards north"		#string input
# Create an instance of document, doc object is a container for a sequence of Token objects.
doc = nlp(str)

words = [word.text for word in doc]	# Read & words
print(words)
      ''')


def nlp_p4e():
    print('''
#pip install keras
#pip install tensorflow
import keras
from keras_preprocessing.text import text_to_word_sequence
# Create a string input
str = "Tokenization using Keras and Tensorflow"
tokens = text_to_word_sequence(str)     
# tokenizing the text
print(tokens)
      ''')


def nlp_p4f():
    print('''
from gensim.utils import tokenize

# Create a string input
input_str = "Players unknown battlegrounds ready to launch"

tokens = list(tokenize(input_str)) # Tokenize the text

print(tokens)
      ''')


def nlp_p5a():
    print('''
import sys
from indicnlp import common
# The path to the local git repo for Indic NLP library
INDIC_NLP_LIB_HOME=r"indic_nlp_library"
# The path to the local git repo for Indic NLP Resources
INDIC_NLP_RESOURCES=r"indic_nlp_resources"
# Add library to Python path
sys.path.append(r'{}\\src'.format(INDIC_NLP_LIB_HOME))
# Set environment variable for resources folder
common.set_resources_path(INDIC_NLP_RESOURCES)
from indicnlp.tokenize import indic_tokenize
indic_string='सुनो, कुछ आवाज़ आ रही है। फोन?'
print('Input String: {}'.format(indic_string))
print('Tokens: ')
for t in indic_tokenize.trivial_tokenize(indic_string):
    print(t)
      ''')


def nlp_p5b():
    print('''
synonyms = {
    "खुश": ["प्रसन्न", "आनंदित", "खुशी"],
    "बहुत": ["अधिक", "बहुत ज्यादा", "काफी"]
}

# Function to generate similar sentences by replacing some words with synonyms
def generate_similar_sentences(input_sentence, num_sentences=5):
    similar_sentences = []

    # Replace some words with synonyms 
    for word, word_synonyms in synonyms.items():
        for synonym in word_synonyms:
            modified_sentence = input_sentence.replace(word, synonym)
            similar_sentences.append(modified_sentence)
    return similar_sentences[:num_sentences]

input_sentence = "मैं आज बहुत खुश हूँ।"
similar_sentences = generate_similar_sentences(input_sentence)
print("Original sentence:", input_sentence)
print("Similar sentences:")
for sentence in similar_sentences:
    print("-", sentence)
      ''')


def nlp_p5c():
    print('''
import nltk
import langid

# Download necessary NLTK data
nltk.download('punkt')

def identify_language(text):
    lang, _ = langid.classify(text)
    return lang

# Identify the Indian Language from the given text
language = identify_language("नमस्ते, आप कैसे हैं?")
print("Identified language:", language)
      ''')


def nlp_p6a():
    print('''
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk import tokenize
from nltk import tag
from nltk import chunk
para = "Natural language processing (NLP) is a machine learning technology that gives computers the ability to interpret, manipulate, and comprehend human language."
sents = tokenize.sent_tokenize(para)
print("\\nsentence tokenization\\n===================\\n",sents)
# word tokenization
print("\\nword tokenization\\n===================\\n")
for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index])
    print(words)
# POS Tagging
tagged_words = []
for index in range(len(sents)):
    tagged_words.append(tag.pos_tag(words))
print("\\nPOS Tagging\\n===========\\n",tagged_words)
# chunking
tree = []
for index in range(len(sents)):
    tree.append(chunk.ne_chunk(tagged_words[index]))
print("\\nchunking\\n========\\n")
print("Tree: ",tree)
      ''')


def nlp_p6b():
    print('''
#pip install -U spacy
#python -m spacy download en_core_web_sm
import spacy
# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")
# Process whole documents
text = ("Natural language processing (NLP) is an interdisciplinary subfield of computer science and information retrieval. It is primarily concerned with giving computers the ability to support and manipulate human language. It involves processing natural language datasets, such as text corpora or speech corpora, using either rule-based or probabilistic machine learning approaches.")
print("Original text: ", text, "\\n")
doc = nlp(text)
# Analyse syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
      ''')


def nlp_p6c():
    print('''
import nltk 
nltk.download('treebank') 
from nltk.corpus import treebank_chunk 
treebank_chunk.tagged_sents()[0] 
treebank_chunk.chunked_sents()[0] 
treebank_chunk.chunked_sents()[0].draw() 
      ''')


def nlp_p7a():
    print('''
import nltk
from nltk import tokenize
grammar1 = nltk.CFG.fromstring("""
S -> VP
VP -> VP NP
NP -> Det NP
Det -> 'that'
NP -> 'flight'
VP -> 'Book'
""")
sentence = "Book that flight"
all_tokens = tokenize.word_tokenize(sentence)
print(all_tokens)
parser = nltk.ChartParser(grammar1)
for tree in parser.parse(all_tokens):
    print(tree)
    tree.draw()
      ''')


def nlp_p7b():
    print('''
def FA(s):
    # if the length is less than 3 then it can't be accepted, Therefore end the process.
    if len(s) < 3:
        return "Rejected"
    if s[0] == '1':
        if s[1] == '0':
            if s[2] == '1':
                for i in range(3, len(s)):
                    if s[i] != '1':
                        return "Rejected"
                return "Accepted"  # if all 4 nested if true
            return "Rejected"  # else of 3rd if
        return "Rejected"  # else of 2nd if
    return "Rejected"  # else of 1st if
inputs = ['1', '10101', '101', '10111', '01010', '100', '', '10111101', '1011111']
for i in inputs:
    print(FA(i))
      ''')


def nlp_p7c():
    print('''
def FA(s):
  size=0
#scan complete string and make sure that it contains only 'a' & 'b'
  for i in s:
    if i=='a' or i=='b':
      size+=1
    else:
      return "Rejected"
#After checking that it contains only 'a' & 'b'
#check it's length it should be 3 atleast
  if size>=3:
#check the last 3 elements
    if s[size-3]=='b':
      if s[size-2]=='b':
        if s[size-1]=='a':
          return "Accepted" # if all 4 if true
        return "Rejected" # else of 4th if
      return "Rejected" # else of 3rd if
    return "Rejected" # else of 2nd if
  return "Rejected" # else of 1st if
inputs=['bba', 'ababbba', 'abba','abb', 'baba','bbb','']
for i in inputs:
  print(FA(i))
      ''')


def nlp_p7d():
    print('''
#!pip install nltk
#nltk.download('punkt')
import nltk
from nltk import tokenize
grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  PP -> P NP
  NP -> Det N | Det N PP | 'I'
  VP -> V NP | VP PP
  Det -> 'a' | 'my'
  N -> 'bird' | 'balcony'
  V -> 'saw'
  P -> 'in'
  """)
sentence = "I saw a bird in my balcony"
for index in range(len(sentence)):
  all_tokens = tokenize.word_tokenize(sentence)
print(all_tokens)
# all_tokens = ['I', 'saw', 'a', 'bird', 'in', 'my', 'balcony']
parser = nltk.ChartParser(grammar1)
for tree in parser.parse(all_tokens):
  print(tree)
  tree.pretty_print()
      ''')


def nlp_p8a():
    print('''
# PorterStemmer 
import nltk
from nltk.stem import PorterStemmer
word_stemmer = PorterStemmer()
print(word_stemmer.stem('writing'))
#LancasterStemmer 
import nltk
from nltk.stem import LancasterStemmer
Lanc_stemmer = LancasterStemmer()
print(Lanc_stemmer.stem('writing'))
#RegexpStemmer 
import nltk
from nltk.stem import RegexpStemmer
Reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)
print(Reg_stemmer.stem('writing'))
#SnowballStemmer 
import nltk
from nltk.stem import SnowballStemmer
english_stemmer = SnowballStemmer('english')
print(english_stemmer.stem ('writing'))
      ''')


def nlp_p8b():
    print('''
#WordNetLemmatizer
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print("word :\\tlemma") 
print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))

# a denotes adjective in "pos"
print("better :", lemmatizer.lemmatize("better", pos ="a"))
      ''')


def nlp_p9():
    print('''
#pip install pandas







          Expand Down





          Expand Up

    @@ -1753,7 +1763,7 @@ def print_node(t, width):

#pip install sklearn
import pandas as pd
import numpy as np
import re
import nltk
nltk.download('stopwords')
# Load the data
sms_data = pd.read_csv("C:/Users/hp/AppData/Local/Programs/Python/Python310/spam.csv", encoding='latin-1')
# Rename columns if necessary
sms_data.rename(columns={'v1': 'Category', 'v2': 'Message'}, inplace=True)
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
stemming = PorterStemmer()
corpus = []
for i in range(len(sms_data)):
    s1 = re.sub('[^a-zA-Z]', ' ', sms_data['Message'][i])
    s1 = s1.lower()
    s1 = s1.split()
    s1 = [stemming.stem(word) for word in s1 if word not in set(stopwords.words('english'))]
    s1 = ' '.join(s1)
    corpus.append(s1)
from sklearn.feature_extraction.text import CountVectorizer
countvectorizer = CountVectorizer()
x = countvectorizer.fit_transform(corpus).toarray()
print(x)
y = sms_data['Category'].values
print(y)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, stratify=y, random_state=2)
# Multinomial Naïve Bayes.
from sklearn.naive_bayes import MultinomialNB
multinomialnb = MultinomialNB()
multinomialnb.fit(x_train, y_train)
# Predicting on test data:
y_pred = multinomialnb.predict(x_test)
print(y_pred)
# Results of our Models
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(classification_report(y_test, y_pred))
print("accuracy_score: ", accuracy_score(y_test, y_pred))
      ''')


def nlp_p10a():
    print('''
#Speech Tagging using spaCy
import spacy #pip install spacy #python-m spacy download en
nlp = spacy.load("en_core_web_sm") #python-m spacy download en_core_web_sm
sp = spacy.load('en_core_web_sm')
sen = sp(u"I like to play cricket. I hated it in my childhood though")
print(sen.text)
print(sen[7].pos_)
print(sen[7].tag_)
print(spacy.explain(sen[7].tag_))
for word in sen:
    print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')
sen = sp(u'Can you google it?')
word = sen[2]
print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')
sen = sp(u'Can you search it on google?')
word = sen[5]
print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')
# Finding the Number of POS Tags
sen = sp(u"I like to play football. I hated it in my childhood though")
num_pos = sen.count_by(spacy.attrs.POS)
for k, v in sorted(num_pos.items()):
    print(f'{k}. {sen.vocab[k].text:{8}}: {v}')
# Visualizing Parts of Speech Tags
from spacy import displacy
sen = sp(u"I like to play football. I hated it in my childhood though")
displacy.serve(sen, style='dep', options={'distance': 120})
# 2  Speech tagging using nktl
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
# Create our training and testing data:
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
# Train the Punkt tokenizer:
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
# Tokenize:
tokenized = custom_sent_tokenizer.tokenize(sample_text)
def process_content():
    try:
        for i in tokenized[:2]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))
        process_content()
process_content()
    ''')


def nlp_p10b():
    print('''
# Usage of "Give" and "Gave" in the Penn Treebank sample
import nltk
def give(t):
    return t.label() == 'VP' and len(t) > 2 and t[1].label() == 'NP' \
           and (t[2].label() == 'PP-DTV' or t[2].label() == 'NP') \
           and ('give' in t[0].leaves() or 'gave' in t[0].leaves())
def sent(t):
    return ' '.join(token for token in t.leaves() if token[0] not in '*-0')
def print_node(t, width):
    output = "%s %s: %s / %s: %s" % \
             (sent(t[0]), t[1].label(), sent(t[1]), t[2].label(), sent(t[2]))
    if len(output) > width:
        output = output[:width] + "..."
    print(output)
for tree in nltk.corpus.treebank.parsed_sents():
    for t in tree.subtrees(give):
        print_node(t, 72)
## Probabilistic parser
import nltk
from nltk import PCFG
grammar = PCFG.fromstring("""
NP -> NNS [0.5] | JJ NNS [0.3] | NP CC NP [0.2]
NNS -> "men" [0.1] | "women" [0.2] | "children" [0.3] | NNS CC NNS [0.4]
JJ -> "old" [0.4] | "young" [0.6]
CC -> "and" [0.9] | "or" [0.1]
""")
print(grammar)
viterbi_parser = nltk.ViterbiParser(grammar)
token = "old men and women".split()
obj = viterbi_parser.parse(token)
print("Output:")
for x in obj:
    print(x)
    ''')


def nlp_p10c():
    print('''
#Steps







          Expand Down





          Expand Up

    @@ -1784,57 +1794,36 @@ def nlp_p11a():

 Parse a sentence and draw a tree using malt parsing.
 1. Java should be installed. (system till jdk and path till bin)
 2. maltparser-1.7.2 (https://maltparser.org/dist/maltparser-1.7.2.zip) zip file should be copied in
 C:\\Users\\AppData\\Local\\Programs\\Python\\Python39 folder and should be
 extracted in the same folder.
 3. engmalt.linear-1.7.mco (https://www.maltparser.org/mco/english_parser/engmalt.linear-1.7.mco) & engmalt.poly-1.7.mco (https://www.maltparser.org/mco/english_parser/engmalt.poly-1.7.mco) file should be copied to
 C:\\Users\\ AppData\\Local\\Programs\\Python\\Python39 folde
    ''')


def nlp_p11a():
    print('''
# Multiword Expressions in NLP
from nltk.tokenize import MWETokenizer
from nltk import sent_tokenize, word_tokenize
s = """Good cake cost Rs.1500\\kg in Mumbai. Please buy me one of them.\\n\\nThanks."""
mwe = MWETokenizer([('New', 'York'), ('Hong', 'Kong')], separator='_')
for sent in sent_tokenize(s):
 print(mwe.tokenize(word_tokenize(sent)))
    ''')


def nlp_p11b():
    print('''
import numpy as np
import re
import textdistance  
from sklearn.cluster import AgglomerativeClustering
texts = ['Reliance supermarket', 'Reliance hypermarket', 'Reliance', 'Reliance', 'Reliance downtown', 'Reliance market','Mumbai', 'Mumbai Hyper', 'Mumbai dxb', 'mumbai airport','k.m trading', 'KM Trading', 'KM trade', 'K.M. Trading', 'KM.Trading']
def normalize(text):
    """ Keep only lower-cased text and numbers"""
    return re.sub('[^a-z0-9]+', ' ', text.lower())

def group_texts(texts, threshold=0.4):
    """ Replace each text with the representative of its cluster"""
    normalized_texts = np.array([normalize(text) for text in texts])
    distances = 1 - np.array([
        [textdistance.jaro_winkler(one, another) for one in normalized_texts]
        for another in normalized_texts])
    clustering = AgglomerativeClustering(
        distance_threshold=threshold,
        metric="precomputed",  # Updated parameter name
        linkage="complete",
        n_clusters=None
    ).fit(distances)
    centers = dict()
    for cluster_id in set(clustering.labels_):
        index = clustering.labels_ == cluster_id
        centrality = distances[:, index][index].sum(axis=1)
        centers[cluster_id] = normalized_texts[index][centrality.argmin()]
    return [centers[i] for i in clustering.labels_]

print(group_texts(texts))







          Expand Down



    ''')


def nlp_p11c():
    print('''
#Word Sense Disambiguation
from nltk.corpus import wordnet as wn
def get_first_sense(word, pos=None):
    if pos:
        synsets = wn.synsets(word,pos)
    else:
        synsets = wn.synsets(word)
    return synsets[0]
best_synset = get_first_sense('bank')
print ('%s: %s' % (best_synset.name, best_synset.definition))
best_synset = get_first_sense('set','n')
print ('%s: %s' % (best_synset.name, best_synset.definition))
best_synset = get_first_sense('set','v')
print ('%s: %s' % (best_synset.name, best_synset.definition))
    ''')
