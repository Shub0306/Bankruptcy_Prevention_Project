import streamlit as st
import pandas as pd
import pickle


#level = [0.0,0.5,1.0]
#st.title('Bankruptcy Prevention System')

#selected_movie_name = st.selectbox(
#'Select The Financial Flexibility',level)
#selected_movie_name = st.selectbox(
#'Select The Credibility',level)
#selected_movie_name = st.selectbox(
##'Select The Competitiveness',level)



model = pickle.load(open('bank.pkl', 'rb'))
def predict( financial_flexibility, competitiveness, credibility):
    data = {' financial_flexibility': [ financial_flexibility], ' competitiveness': [ competitiveness], ' credibility': [ credibility]}
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    prediction = 'NON-BANKRUPT' if prediction[0] == 1 else 'BAKRUPT'
    return prediction

def main():
    # Set the app title
    st.title('Bankruptcy Prevention System')

    # Add inputs for user to enter values
    Flexibility = st.selectbox('Select value for Financial flexibility', [0.00,0.50,1.00])
    Competitiveness = st.selectbox('Select value for Competitiveness', [0.00,0.50,1.00])
    Credibility = st.selectbox('Select value for Credibility', [0.00,0.50,1.00])

    # Call the prediction function when the user clicks the 'Predict' button
    if st.button('Predict'):
        prediction = predict(Flexibility, Credibility, Competitiveness)
        st.write(f'The prediction is: {prediction}')

# Run the app
if __name__ == '__main__':
    main()




