import os
import schedule_read
import subprocess
import time
import API
import data_extractor as de

current_dir = os.getcwd()

team_names = API.import_teamnames()
print(team_names)
#team_names = [['Образец']]
run_sim_option = True
if run_sim_option:
    for this_team_name in team_names:

        if not os.path.isdir(f"dataspace/{this_team_name[0]}"):
             os.mkdir(f"dataspace/{this_team_name[0]}")
     
        print("---Импорт решений " + this_team_name[0] + '---')
        API.create_table_and_import(this_team_name[0], current_dir)
        schedule_read.create_schedule_for_team(this_team_name[0])

        print("---Перемешsение сгенерированной schedule секции для команды " + this_team_name[0] + '---')
        path_to_generated_schedule = "dataspace/" + this_team_name[0] + '/'
        new_schedule_file_name = "schedule_new_" + this_team_name[0] + ".inc"
        abs_path_to_new_schedule = path_to_generated_schedule + new_schedule_file_name
        subprocess.call(["cp", "-r" , abs_path_to_new_schedule, 'workspace/spe1_SCH.INC'])

        print("---Запуск симулятора для команды " + this_team_name[0] + '---')
        path_to_opm_data = current_dir+ "/workspace"
        os.chdir(path_to_opm_data)
        result = os.system("mpirun -np 2 flow spe1.DATA")

        print("---Запуск скрипта на python3.8 для извлечения результатов команды " + this_team_name[0] + '---')
        os.chdir(current_dir)
        os.system("python3.8 data_extractor.py")

        print("---Перенос результатов в папку команды " + this_team_name[0] + '---')
        if not os.path.isdir(f"resultspace/{this_team_name[0]}"):
             os.mkdir(f"resultspace/{this_team_name[0]}")
        command_to_move_results = "mv -f ./sim_result.csv ./resultspace/" + this_team_name[0] + '/'
        os.system(command_to_move_results)
        
        print("---Экспорт решений в гугл таблицу  " + this_team_name[0] + '---')
        de.export_to_csv(current_dir, this_team_name[0])
        time.sleep(2)
        API.export_to_GT(current_dir,this_team_name[0])
        API.export_snapshots(this_team_name[0])