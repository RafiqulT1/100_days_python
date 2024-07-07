import pandas

# adding data form 50_states.csv file to pandas data frame
df = pandas.read_csv("./data_files/50_states.csv")
# make list of state name & transform state name to lowercase
all_states = df.state.to_list()

