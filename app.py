import streamlit as st
import pandas as pd
import numpy as np


df=pd.read_csv('file.csv')
print(df.value_counts())