import streamlit as st
import pandas as pd
import yaml


def printing() -> str:
    return 'Hello World'

def display(df: pd.DataFrame) -> None:
    st.dataframe(df)
    #st.table(data.iloc[0:10])
    st.json({'foo':'bar','fu':'ba'})
    st.metric(label="Temp", value="273 K", delta="1.2 K")

if __name__ == '__main__':
    with open("credentials.yaml",'r') as f:
        credentials = yaml.load(f)
        print(credentials)