import numpy as np 
import pickle
import streamlit as st

loaded_model = pickle.load(open(r'C:\Users\Rapid IT World\Desktop\New folder\Project\Diabetes prediction\trained_model.sav', 'rb'))

#create a function for prediction

def diabeties_prediction(input_data):
    #convert input data into the numpy array
    input_data_to_np = np.asarray(input_data)

    #reshaping the array
    reshaped_arr = input_data_to_np.reshape(1, -1)

    #prediction of model based on the user input
    prediction = loaded_model.predict(reshaped_arr)
    print(prediction)

    if (prediction[0] == 0):
        return "The Person is not diabetic"
    else:
        return "The Person is diabetic"

def main():
    #Giving a title
    st.title('Diabetes Prediction Web App')  

    #input data that user gives
    # Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('BloodPressure value')
    SkinThickness = st.text_input('SkinThickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMIs value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    Age = st.text_input('Age of the person')

    #a empty variable to store the prediction vaues
    diagnosis = ''
    
    # abutton for checking the prediction values
    if st.button('Diabetes Test Result'):
        diagnosis = diabeties_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

    st.success(diagnosis)

if __name__ == '__main__':
    main()