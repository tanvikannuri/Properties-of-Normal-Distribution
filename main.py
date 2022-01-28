import statistics
import pandas as pd 
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("studentsPerformance.csv")
data = df["reading score"].tolist()

mean = statistics.mean(data)
mode = statistics.mode(data)
median = statistics.median(data)
std_deviation = statistics.stdev(data)

print("Mean, Median, Mode, Std Deviation of data is {}, {}, {}and {} respectively".format(mean, median, mode, std_deviation))

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

fig= ff.create_distplot([data],["Reading Score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))

fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="Std.Deviation1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="Std.Deviation2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="Std.Deviation3"))

fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="Std.Deviation1(end)"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="Std.Deviation2(end)"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="Std.Deviation3(end)"))


fig.show()

list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))