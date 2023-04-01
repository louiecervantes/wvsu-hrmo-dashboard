#Input the relevant libraries
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from scipy.stats import chi2_contingency
from PIL import Image

def filterBy(df, college):
    filtered_df = df[df['COLLEGE'] == college]  
    return filtered_df

def loadcsvfile(campus):
    csvfile = 'employee_cleaned.csv'
    df = pd.read_csv(csvfile, dtype='str', header=0, sep = ",", encoding='latin')
    st.dataframe(df, width=800, height=400)
    st.write("Properties of the dataset")
    desc = df.describe().T
    st.write(desc) 
        
    else:
        st.write('No data to process!')   
    return df
    
# Define the Streamlit app
def app():
    
    # Load image from file
    img = Image.open("wvsu_logo.png")
    new_size = (200, 200)
    img = img.resize(new_size)
 
    # Create a container element and center it vertically
    container = st.container()
    container.horizontal_alignment = "center"

    # Display the image inside the container element and align it to the center
    with container:
        st.image(img)
        st.title("Welcome to the WVSU Human Resource Dashboard")
        
    st.subheader("(c) 2023 WVSU Management Information System")
                 
    st.write("This dashboard is managed by: \nAgustin C. Cabahug, Jr. \nSAO, WVSU Human Resource Office \nhrmo@wvsu.edu.ph")
                 
    st.write("A Human Resource Management (HRM) dashboard is a tool that provides a comprehensive visual representation of key HR metrics and data in real-time. It is used by HR professionals to monitor and analyze important HR information, such as employee turnover rates, performance metrics, and workforce demographics. The dashboard can display graphs, charts, tables, and other visual elements that help HR professionals quickly and easily understand the data and identify trends and patterns.")

    #create a dataframe
    df = pd.DataFrame()
    
    st.subheader("Employee Demographics")
    campus = 'Main'
    options = ['Main', 'Calinog', 'Himamaylan', 'Janiuay', 'Lambunao', 'Pototan','All']
    selected_option = st.selectbox('Select the campus', options)
    if selected_option=='Main':
        campus = selected_option
        df = loadcsvfile(campus)
    else:
        campus = selected_option
        df = loadcsvfile(campus)
    

    if st.button('By Gender'):
        if hasData==True:
            #Gender
            st.write("Distribution by gender")
            scounts=df['GENDER'].value_counts()
            labels = list(scounts.index)
            sizes = list(scounts.values)
            custom_colours = ['#ff7675', '#74b9ff']
            fig = plt.figure(figsize=(12, 4))
            plt.subplot(1, 2, 1)
            plt.pie(sizes, labels = labels, textprops={'fontsize': 10}, startangle=140, autopct='%1.0f%%', colors=custom_colours)
            plt.subplot(1, 2, 2)
            sns.barplot(x = scounts.index, y = scounts.values, palette= 'viridis')
            st.pyplot(fig)
        else:
            st.write("No data to process!")
            
            
    st.subheader('Alumni engangement')
    st.write('Under development')
    st.subheader('Contact Information')
    st.write('Under development')
            
#run the app
if __name__ == "__main__":
    app()
