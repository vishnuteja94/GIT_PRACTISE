import streamlit as st
import pandas as np
import numpy as np

df=pd.read_csv('file.csv')
print(df.value_counts())