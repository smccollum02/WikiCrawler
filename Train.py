import pandas as pd
import numpy as np
import tensorflow as tf
import nltk
from matplotlib import pyplot as plt
from nltk.corpus import stopwords, words
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import SimpleRNN, Embedding, Dense, Dropout, LSTM, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences