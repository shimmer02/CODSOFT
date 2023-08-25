import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('spam_model.sav', 'rb'))
feature_extraction = pickle.load(open('feature_extraction.sav', 'rb'))

def predict(input):
    input_features = feature_extraction.transform(input)
    prediction = loaded_model.predict(input_features)

    if prediction == 0:
        st.error('SMS is spam :thumbsdown:')
    else:
        st.success('SMS is not spam :thumbsup:')
def main():

    st.title('SMS Spam Detector')

    sms = st.text_input('Enter SMS message', placeholder='SMS')

    result = ''

    if st.button('Detect'):
        result = predict([sms])
if __name__ == '__main__':
    main()