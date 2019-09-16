import os
import schedule_read
import subprocess
import importlib.util
import pandas as pd

current_dir = os.getcwd()

# TODO сделать сохранения результатов в папку команд  smspec egrid
# TODO понять, почему не генерит SMSPEC

print(current_dir)

team_names = ['ФОН', 'FlexOil']

schedule_read.create_schedules_for_all_teams(team_names)

run_sim_option = True
if run_sim_option:
    for this_team_name in team_names:

        print("---Перемежение сгенерированной schedule секции для команды " + this_team_name + '---')
        path_to_generated_schedule = "/home/khabibullinra/GitHub/simrun2.7/dataspace/" + this_team_name + '/'
        new_schedule_file_name = "schedule_new_" + this_team_name + ".inc"
        abs_path_to_new_schedule = path_to_generated_schedule + new_schedule_file_name
        #command_to_copy_schedule = "cp -f " + abs_path_to_new_schedule + ' ./workspace/spe1_SCH.INC'
        #os.system(command_to_copy_schedule)
        subprocess.call(["cp", "-f" , abs_path_to_new_schedule, './workspace/spe1_SCH.INC'])

        print("---Запуск симулятора для команды " + this_team_name + '---')
        path_to_opm_data = "/home/khabibullinra/GitHub/simrun2.7/workspace"
        os.chdir(path_to_opm_data)
        result = os.system("mpirun -np 2 flow spe1.DATA")
        #subprocess.call(["mpirun", "-np", '2', 'flow', 'spe1.DATA'])

        print("---Запуск скрипта на python2.7 для извлечения результатов команды " + this_team_name + '---')
        os.chdir(current_dir)
        os.system("python2.7 data_extractor.py")

        print("---Перенос результатов в папку команды " + this_team_name + '---')
        command_to_move_results = "mv -f ./sim_result.csv ./resultspace/" + this_team_name + '/'
        os.system(command_to_move_results)
        command_to_move_results = "mv -f ./workspace/SPE1.EGRID ./resultspace/" + this_team_name + '/'
        os.system(command_to_move_results)



spec = importlib.util.spec_from_file_location("plotly_workflow.py",
                                         "/home/khabibullinra/GitHub/unifloc/uniflocpy/uTools/plotly_workflow.py")
pwf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pwf)

for this_team_name in team_names:
    path_to_file = "/home/khabibullinra/GitHub/simrun2.7/resultspace/" + this_team_name + "/"
    file_name = "sim_result.csv"
    file = path_to_file + file_name
    result = pd.read_csv(file, index_col="time")
    result.index = pd.to_datetime(result.index)

    traces = pwf.create_traces_list_for_all_columms(result, chosen_mode="lines+markers")
    data = traces
    plot_name = "Результат построения графиков команды " + this_team_name
    pwf.plot_func(data, plot_name, path_to_file + plot_name+".html")