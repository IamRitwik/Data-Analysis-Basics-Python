import streamlit as st
import glob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pathlib import Path
import plotly.express as px

st.title("Mood Analyzer")
filepaths = glob.glob("diary/*.txt")
filepaths = sorted(filepaths)
analyzer = SentimentIntensityAnalyzer()
dates = []
pos = []
negs = []

for filepath in filepaths:
    path = Path(filepath).stem
    with open(filepath, "r") as file:
        text = file.read()
    score = analyzer.polarity_scores(text)
    dates.append(path)
    pos.append(score["pos"])
    negs.append(score["neg"])

figure = px.line(x=dates, y=pos, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)

figure = px.line(x=dates, y=negs, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure)