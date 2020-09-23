import os
import schedule_read
import subprocess
import time
import API
import data_extractor as de

current_dir = os.getcwd()

team_names = API.import_teamnames()[0]

run_sim_option = True
if run_sim_option:
    for this_team_name in team_names:

        if not os.path.isdir(f"dataspace/{this_team_name}"):
             os.mkdir(f"dataspace/{this_team_name}")
     
        print("---Импорт решений " + this_team_name + '---')
        API.create_table_and_import(this_team_name, current_dir)
        schedule_read.create_schedule_for_team(this_team_name)

        print("---Перемешsение сгенерированной schedule секции для команды " + this_team_name + '---')
        path_to_generated_schedule = "dataspace/" + this_team_name + '/'
        new_schedule_file_name = "schedule_new_" + this_team_name + ".inc"
        abs_path_to_new_schedule = path_to_generated_schedule + new_schedule_file_name
        subprocess.call(["cp", "-r" , abs_path_to_new_schedule, 'workspace/spe1_SCH.INC'])

        print("---Запуск симулятора для команды " + this_team_name + '---')
        path_to_opm_data = current_dir+ "/workspace"
        os.chdir(path_to_opm_data)
        result = os.system("mpirun -np 2 flow spe1.DATA")

        print("---Запуск скрипта на python3.8 для извлечения результатов команды " + this_team_name + '---')
        os.chdir(current_dir)
        os.system("python3.8 data_extractor.py")

        print("---Перенос результатов в папку команды " + this_team_name + '---')
        command_to_move_results = "mv -f ./sim_result.csv ./resultspace/" + this_team_name + '/'
        os.system(command_to_move_results)
        
        print("---Экспорт решений в гугл таблицу  " + this_team_name + '---')
        de.export_to_csv(current_dir, this_team_name)
        API.export_to_GT(current_dir,this_team_name)
        API.export_snapshots(this_team_name)