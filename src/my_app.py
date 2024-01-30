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


def get_credentials(site: str) -> dict:
    with open(r"C:\Users\karme\Sentiment_Analysis\credentials.yaml",'r') as f:
        credentials = yaml.load(f,Loader=yaml.FullLoader)
        cred = credentials[site]
        return cred 


if __name__ == '__main__':
    df = pd.read_csv(r"C:\Users\karme\Sentiment_Analysis\data\test\BBCA.JK new.csv")
    display(df)
    