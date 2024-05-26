import pickle
import streamlit as st
from PIL import Image
import numpy as np
pickle_in=open("Model.pkl","rb")
model=pickle.load(pickle_in)
@st.cache_data
def predict_cancer(Clubbing_of_Finger_Nails,Age,Smoking,Wheezing,Fatigue,Passive_Smoker,Dust_Alcohol):
    input=np.array([[Clubbing_of_Finger_Nails,Age,Smoking,Wheezing,Fatigue,Passive_Smoker,Dust_Alcohol]])
    prediction=model.predict(input)
    return prediction
def main():
    st.title("Lung Cancer Prediction")
    image_path="E:\\DataScience\\Cancer\\cancerimage.jpg"
 
    # Load the image using PIL
    image = Image.open(image_path)
    
    # Display the image in Streamlit
    st.image(image, caption='Lung Cancer', use_column_width=True)
    
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Lung Cancer Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    Name=st.text_input('Enter Patient Name')
    Gender=st.selectbox('Gender',("Male","Female"))
    Clubbing_of_Finger_Nails=st.slider("Enter Patient Clubbing_of_Finger_Nails",0,10,0)
    Age=st.slider('Enter Patient Age',0,100,25)
    Smoking=st.slider('Enter Patient smoking status',0,10,0)
    Wheezing=st.slider('Enter Patient wheezing status',0,10,0)
    Fatigue=st.slider('Enter Patient fatigue status',0,10,0)
    Passive_Smoker=st.slider('Enter Patient Passive smoking status',0,10,0)
    Dust_Alcohol=st.slider('Enter Patient Dust Allergy status',0,10,0)
    output=""
    text=""
    safe_html ="""  
    <div style="background-color:#80ff80; padding:10px >
    <h2 style="color:white;text-align:center;"> The Abalone is young</h2>
    </div>
    """
    if st.button("Predict"):
        output=predict_cancer(Clubbing_of_Finger_Nails,Age,Smoking,Wheezing,Fatigue,Passive_Smoker,Dust_Alcohol)
        if output==0:
            text='Low'
        elif output==1:
            text='Medium'
        else:
            text='High'
    st.success(f"Patient {Name} has {text} Cancer {output}")
if __name__=='__main__':
    main()
