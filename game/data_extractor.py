from ecl.summary import EclSum
import pandas as pd

path_to_sim_dir = "./workspace/"
model_data_file_name = "spe1.DATA"

file_name = path_to_sim_dir + model_data_file_name
summary = EclSum(file_name)
dates = summary.dates

shape = len(dates)
result_df = pd.DataFrame({"test": list(range(shape))})

nedeed_keys = ["WOPR:*", "WWPR:*", "WLPR:*", "WGPR:*", "WWIR:*" ,
               "WGOR:*", "WBHP:*",
               "WOPT:*", "WWPT:*", "WLPT:*", "WGPT:*", "WWIT:*",
               "FOPT", "FWPT", "FLPT", "FGPT", "FWIT"]

#  all_keys = summary.keys("*")
#  print all_keys
for i in nedeed_keys:
    keys_by_wells = summary.keys(i)
    for j in keys_by_wells:
        this_parameter_values = summary.numpy_vector(j)
        one_parameter_df = pd.DataFrame({j: this_parameter_values})
        result_df = result_df.join(one_parameter_df)

time_parameter_column = pd.DataFrame({"time": dates})
result_df = result_df.join(time_parameter_column)
result_df = result_df.set_index("time")
del result_df['test']

result_df.to_csv("sim_result.csv")

