# -*- coding: utf-8 -*-
"""GPT-3 Chatbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lbfi1lt5Oj87oDMfvmqjpTHPA8Hu-wld
"""

!pip install openai
!pip install dotenv

#!pip uninstall dotenv
#!pip uninstall python-dotenv
#!pip install python-dotenv

import pandas as pd
import numpy as np
from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"
completion = openai.Completion()

start_sequence = "\nA:"
restart_sequence = "\n\nQ:"
session_prompt = prompt="Welcome to Innodatatics AI chatbot! I'm here to answer your questions related to Data science. let's go! \"Unknown\".\n\nQ:What is the Central Limit Theorem and why is it important? \nA:“Suppose that we are interested in estimating the average height among all people. Collecting data for  every person in the world is impossible. While we can’t obtain a height measurement from everyone in the  population, we can still sample some people. The question now becomes, what can we say about the  average height of the entire population given a single sample. The Central Limit Theorem addresses this  question exactly.”\n\nQ: What is sampling? How many sampling methods do you know? \nA: “Data sampling is a statistical analysis technique used to select, manipulate and analyze a representative \nsubset of data points to identify patterns and trends in the larger data set being examined.”\n\nQ: What is the difference between type I vs type II error?\nA: “A type I error occurs when the null hypothesis is true, but is rejected. A type II error occurs when the null hypothesis is false, but erroneously fails to be rejected.” \n\nQ: What is linear regression?\nA: A linear regression is a good tool for quick predictive analysis: for example, the price of a house depends on a myriad of factors, such as its size or its location. In order to see the relationship between these variables, we need to build a linear regression, which predicts the line of best fit between them and can help conclude whether or not these two factors have a positive or negative relationship\n\nQ: . What is Data Science? \nA: Data Science is a blend of various tools, algorithms, and machine learning principles with the goal to discover hidden patterns from the raw data.\n\nQ: What is a confusion matrix?\nA: The confusion matrix is a 2X2 table that contains 4 outputs provided by the binary classifier. Various measures, such as error-rate, accuracy, specificity, sensitivity, precision and recall are derived from it\n\nQ:What is a Probability Distribution? \nA:Probability distribution is a statistical function, that gives the probability of each value of random variable.\n\nQ:Define evaluationn metrics \nA:An evaluation metric quantifies the performance of a predictive model. This typically involves training a model on a dataset, using the model to make predictions on a holdout dataset not used during training, then comparing the predictions to the expected values in the holdout dataset. \n\nQ:what do you mean by tensorflow? \nA:tensorflow is a free and open source software library for machine learning and artificial intelligence \n\nQ:who invented keras? \nA:francois chollet invented keras and he is currently working as an ai researcher at google.",

def ask(question, chat_log =None):
  prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
  response = openai.Completion.create(
      model="text-davinci-002",
      prompt=prompt_text,
      temperature=0.85,
      max_tokens=100,
      top_p=1,
      frquency_penalty=0,
      presence_penalty=0,
      stop=["\n"]
      )
  story = response['choices'][0]['text']
  return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
      chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

