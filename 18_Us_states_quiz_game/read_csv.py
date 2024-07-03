import pandas

# adding data form 50_states.csv file to pandas data frame
df = pandas.read_csv("50_states.csv")
# make list of state name & transform state name to lowercase
all_state_list = df.state.to_list()
# all_state_list = df.state.str.lower().to_list()
# print(all_state_list)
