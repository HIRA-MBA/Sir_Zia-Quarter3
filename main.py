import streamlit as st
import pandas as pd
import os
from io import BytesIO
import openpyxl
print(openpyxl.__version__)



st.set_page_config(page_title="Data sweeper ", layout='wide')
st.title("DAta sweeper")
st.write("transform your file between CSV and Excel Format")
uploaded_file = st.file_uploader("upload your file (csv or excel ):",type=["csv","xlsv"],accept_multiple_files=True)

if uploaded_file:
    for file in uploaded_file:
        file_ext=os.path.splitext(file.name)[-1].lower()

        if file_ext==".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xls":
            df = pd.read_excel(file)
        else: 
            st.error(f"unsupported file type :{file_ext}")
            continue

        st.write(f"file name {file.name}")
        st.write(f"file size: {file.size/1024}")
        st.write("review the head of data frame")
        st.dataframe(df.head())

        st.subheader("data cleaning options")
        if st.checkbox(f"clean data for {file.name}") :
            col1 , col2 = st.columns(2)

            with col1:
                if st.button(f' remove duplicates from {file.name}'):
                  df.drop_duplicates(inplace=True)
                  st.write("Duplicates Removed!")

            with col2:
                if st.button(f"fill missing values for {file.name}"):
                    numeric_cols=df.select_dtypes(include=['number']).columns
                    df[numeric_cols]=df[numeric_cols].fillna(df[numeric_cols]).mean

                    st.write("missing number are filled")

# choose specific column to keep or convert

st.subheader("select columns to convert")
columns= st.multiselect(f"choose columns  for {file.name}",df.columns,default=df.columns)
df=df[columns]

# create some visualization

st.subheader(f"data visualization")
if st.checkbox(f"show visualization for {file.name}"):
    st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])

# convert the file -> csv to excel
st.subheader(F" conversion options")
conversion_type= st.radio(f"convert {file.name} to:", ["CSV","Excel"],key=file.name)
if st.button(f"convert {file.name}"):
    buffer=BytesIO()
    if conversion_type== "CSV":
        df.to_csv(buffer,index=False)
        file_name=file.name.replace(file_ext,".csv")
        mime_type= "text/csv"

    elif conversion_type == "Excel" :
        df.to_excel(buffer,index=False)
        file_name=file.name.replace(file_ext,".xlsx")
        mime_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    buffer.seek(0)

    # Download button
    st.download_button(
        label=f" Download {file_name} as {conversion_type}",
        data=buffer,
        file_name=file_name,
        mime=mime_type
    )

st.success(" All files Processed")