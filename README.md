# Bigram-Model

A simple character-level bigram language model trained from scratch using PyTorch.  

# Description

This project implements a tiny bigram-based language model, similar to the first steps in building a GPT-style tokenizer and neural network.  
It loads a text file, builds a character-level vocabulary, encodes the training data, and trains a single-layer embedding model that predicts the next character based solely on the previous one.  
A small sampling loop then generates new text using the learned probabilities.  
