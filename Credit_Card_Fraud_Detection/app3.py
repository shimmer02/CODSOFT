import pickle 
import streamlit as st
import numpy as np

loaded_model = pickle.load(open('fraud_model.sav', 'rb'))

def predict(input):
    npin = np.asarray(input)
    rs = npin.reshape(1, -1)
    fraud_pred = loaded_model.predict(rs)

    if fraud_pred == [0]:
        st.success('The Transaction was not a fraudulent :thumbsup:')
    else:
        st.error('The transaction was fraudulent :thumbsdown:')
def main():
    
    st.title('FRAUDULENT CREDIT CARD TRANSACTION DETECTION')

    cc_num = st.number_input('Enter Credit Card Number')
    amt = st.number_input('Enter Amount of Transaction')
    gender = st.selectbox('Pick Gender', options=['Male', 'Female'])
    zip = st.number_input('Enter ZIP code')
    lat = st.number_input('Location: Enter Latitude')
    long = st.number_input('Location: Enter Longitude')
    dob = st.date_input( 'Enter Date (YYYY/MM/DD)', format='YYYY/MM/DD' )
    cpop = st.number_input('Enter City Population')
    unix = st.number_input('Enter Unix Time Stamp')
    mlat = st.number_input('Merchant Location: Enter Latitude')
    mlong = st.number_input('Merchant Location: Enter Longitude')
    

    result = ''

  
    date_time = dob.strftime("%Y/%m/%d")
    dobnum = date_time.replace('/', '')
    numdob = int(dobnum)
    
    if gender == 'Male':
        gen = 1
    else:
        gen = 0
    if st.button('Predict'):
        result = predict([0, cc_num, amt, gen, zip, lat, long, cpop, numdob, unix, mlat, mlong ])

if __name__ == '__main__':
    main()