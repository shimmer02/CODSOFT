import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('movie_model.sav', 'rb'))
feature_extraction = pickle.load(open('feature_extraction.sav', 'rb'))

def predict(input):
    input_features = feature_extraction.transform(input)
    prediction = loaded_model.predict(input_features)
    disp = 'The movie is of the '+ prediction +' genre'
    brackets = ['[',',',']']
    Without_brackets = ""
    for character in disp:
        if character not in brackets:
            Without_brackets += character
    st.success(Without_brackets)
    
def main():

    st.title('Know Your Show :movie_camera:')

    name = st.text_input('Enter Movie Name', placeholder='Movie')
    year = st.text_input('Enter Year of Release', placeholder='Year')
    desc = st.text_input('Enter Brief Description', placeholder='Synopsis')
    check_quotes = ["'", '"']
    Without_quotes = ""
    for character in desc:
        if character not in check_quotes:
            Without_quotes += character
    y = '('+  year + ')'
    mov = name + y + ' ' + Without_quotes

    if st.button('Predict Genre'):
        predict([mov])
if __name__ == '__main__':
    main()