#!/usr/bin/python3.4m
from clean_extract import load_data
from train_test import train,cross_validation,predict
from sklearn.model_selection import train_test_splits

def train_new_model():
    (train_data,author_frame,domain_frame,subreddit_frame) = load_data(path)
    (trained_model,cross_validation_frame,test_frame) = train(train_frame,author_frame,domain_frame,subreddit_frame)
    if cross_valid==1:
        cross_validation(cross_validation)
    test(trained_model,test_frame)

# def predict():
