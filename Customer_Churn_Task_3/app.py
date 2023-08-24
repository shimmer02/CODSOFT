import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('churn_model.sav', 'rb'))

def predict(input):
    npin = np.asarray(input)
    rs = npin.reshape(1, -1)
    churn_pred = loaded_model.predict(rs)

    if churn_pred == [0]:
        st.success('Customer will not exit :thumbsup:')
    else:
        st.error('Customer will exit :thumbsdown:')
def main():
    
    st.title('CUSTOMER CHURN PREDICTION')

    credit_score = st.number_input('Enter Credit Score', 600)
    gender = st.select_slider('Select Gender [1 : Male, 0 : Female]', [1, 0])
    age = st.slider('Enter Age', 18,92)
    tenure = st.slider('Select Tenure', 0,10)
    balance = st.number_input('Enter Balance', 000)
    numofproducts = st.slider('Select number of products', 1,4)
    hascrcard = st.select_slider('Select if user has credit card or not [1 : Yes, 0 : No]', [1, 0])
    isactivemember = st.select_slider('Select if use is an active member [1 : Yes, 0 : No]', [1, 0])
    estimatedsalary = st.number_input('Enter Salary (estimated)', 000000)

    result = ''

    if st.button('Predict'):
        result = predict([credit_score/850, gender, age/92, tenure/10, balance/250898.09, numofproducts, hascrcard, isactivemember, estimatedsalary/199992.480000])

if __name__ == '__main__':
    main()