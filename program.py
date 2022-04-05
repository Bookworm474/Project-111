import pandas as pd
import statistics as st
import random
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = st.mean(data)
mean_of_samples = []

for x in range(0,100):
    temp = []
    for x in range(0,30):
        temp.append(data[random.randint(0, (len(data)-1))])
    mean_of_samples.append(st.mean(temp))
mean = st.mean(mean_of_samples)
stdev = st.stdev(mean_of_samples)

zscore = (mean - population_mean)/stdev

first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - (2 * stdev), mean + (2 * stdev)
third_stdev_start, third_stdev_end = mean - (3 * stdev), mean + (3 * stdev)

fig = ff.create_distplot([mean_of_samples], ["Mean Reading Time"], show_hist=False)
fig.show()