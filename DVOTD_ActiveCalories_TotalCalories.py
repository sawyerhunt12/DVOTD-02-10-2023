# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 08:47:08 2023

@author: HuntS2
"""

import pandas as pd
import plotly_express as px
import plotly.io as pio
pio.renderers.default = "browser"

df = pd.read_csv(r"C:\Users\Hunts2\OneDrive - AECOM\Documents\Data Science Projects\Other Projects\2023-02-10\2023 Workouts - January.csv")


fig = px.scatter(df, 
                  x = "Active Calories",
                  y = "Total Calories",
                  color = "Avg Heart Rate (bpm)",
                  hover_data = ["Workout"],
                  trendline = "ols",
                  title = "January 2023 Workouts Active Calories vs. Total Calories Burned")
fig.show()