
import joblib
import streamlit as st
model = joblib.load('flowerClassifier.pkl')

st.title('My app')

st.write ('Enter flower measurement to predict the iris species')

sepal_length = st.number_input('Enter sepal length')
sepal_width = st.number_input('Enter sepal width')
petal_length = st.number_input('Enter a petal length')
petal_width = st.number_input('Enter a petal width')

if st.button ('Predict'):
    newData = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict (newData)

    if prediction == 0:
        st.success ('The predicted class is Setosa')
    elif prediction == 1:
        st.success('The predicted class is Versicolo')
    else:
        st.success('The predicted class is Virginica')

