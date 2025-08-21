import joblib
import streamlit as st

model = joblib.load(open("C:/Users/DELL/Desktop/Data Science/BREAST CANCER/Breast_Cancer_Diagnosis.pkl", 'rb'))

def main():
    st.title('BREAST CANCER DIAGNOSIS')

    #input variables
    radius_mean = st.number_input('Radius Mean')
    texture_mean = st.number_input('Texture Mean')
    smoothness_mean = st.number_input('Smoothness Mean')
    compactness_mean = st.number_input('Compactness Mean')
    symmetry_mean = st.number_input('Symmetry Mean')
    fractal_dimension_mean = st.number_input('Fractal Dimension Mean')
    radius_se = st.number_input('Radius Standard Error')
    texture_se = st.number_input('Texture Standard Error')
    smoothness_se = st.number_input('Smoothness Standard Error')
    compactness_se = st.number_input('Compactness Standard Error')
    symmetry_se = st.number_input('Symmetry Standard Error')
    symmetry_worst = st.number_input('Symmetry Worst')

    #Prediction code
    if st.button('Diagnose'):
        makediagnosis= model.predict([[radius_mean,texture_mean,smoothness_mean,compactness_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,smoothness_se,compactness_se,symmetry_se,symmetry_worst]])
        st.write("Diagnosis:", makediagnosis[0])
if __name__=='__main__':
    main()