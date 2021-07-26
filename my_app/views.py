from django.shortcuts import render,redirect
from.models import *
import tensorflow
import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
import re
import numpy as np
from keras.models import load_model
model=load_model('spam_data.h5') # this is my trained model with 0.9997% Accuracy


def text_preprocessing(text): # preprocess text data
    tokenizer = Tokenizer(num_words=500, split='')
    tokenizer.fit_on_texts(text)
    text = text.lower()
    new_text = re.sub('[^a-zA-z0-9\s]', '', text)
    new_text = re.sub('rt', '', new_text)
    return new_text
def Pipeline(text):
    text_new=text_preprocessing(text)
    tok = tokenizer.texts_to_sequences(text_new)
    tok = sequence.pad_sequences(tok)
    return tok
def prediction():
    clean_text=Pipeline(text)
    model=model.predict(clean_text).mean()
    if model==0:
        return 'ham'
    else:
        return 'spam'

def home(request):
    ab=mode.objects.all()
    if request.method=="POST":
        text_data=request.POST['text_data']
        text=mode(des=text_data)
        text.save()
        pred_text=text_preprocessing(text=text)
        return request(request,'home.html',{'pred':pred_text})
    return render(request,'home.html',{"ab":ab})
def delelte(request,id):
    if request.method=="POST":
        fm=mode.objects.get(id=id)
        fm.delete()
        return redirect('home')
