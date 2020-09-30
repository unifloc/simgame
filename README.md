# SimGame2020 
## Authors:
* Rinat Khabibullin
* Alexey Vodopyan
* Oleg Kobzar 
* Evgeny Svoykin
* Dmitry Lubnikov
* Vladislav Dormenev
* Dmitry Antropov

Репозиторий для развития учебного проекта для изучения разработки нефтяных и газовых проектов с помощью открытого симулятора Open Porous Media.

Структура проекта (будет перерабатываться в дальнейшем):
* dataspace - исходные данные команд для управления месторождением;
* workspace - данные симулятора, рабочая директория в которой ведется расчет OPM;
* resultspace - результаты расчетов в сыром и обработанном виде;
* guides - гайды и инструкции по провоедению игры, установке и работе с необходимым софтом.

Дополнительно:
* .py файлики в корне проекта - для запуска всех необходимых действий;
* simgame_run.py - основной скрипт для запуска на расчёт;
* API.py - скрипт для работы с импортом и экспортом из гугл таблицы;
В паре идёт файл creds.json. Подробнее с работой API.py можно поссмотреть по [сылке](https://www.youtube.com/watch?v=Bf8KHZtcxnA&ab_channel=%D0%94%D0%B8%D0%B4%D0%B6%D0%B8%D1%82%D0%B0%D0%BB%D0%B8%D0%B7%D0%B8%D1%80%D1%83%D0%B9%21);
* schedule_read.py - скрипт для чтения решения команды и создания .inс файла, необходимого для запуска на расчет в opm;
* data_extractor.py - скрипт для чтения результатов расчета opm.

# [Мануал по игре](https://docs.google.com/document/d/1-QevtR_6TomRk5jX3PCB7LC9chd18N2i2_e7WbmRB4A/edit)

## [Пример оформления гугл таблицы WIP](https://docs.google.com/spreadsheets/d/17O_GghnChsKLxtdRGGWG8W9aOMx411DRHKszuMPflMo/edit#gid=0)
