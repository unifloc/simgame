RPTRST
'BASIC=3' 'FREQ=1' 'FLOWS' /

RPTSCHED
'FIP=3' 'SUMMARY=3' 'WELSPECS' /

WELSPECS
  P1 G1 19 19 1* OIL /
  P3 G1 85 85 1* OIL /
  PS1 G1 15 85 1* OIL /
  PS2 G1 85 15 1* OIL /
  P4 G1 29 29 1* OIL /
  P5 G1 19 29 1* OIL /
  P6 G1 29 19 1* OIL /
  I1 G1 24 24 1* WATER /
  I2 G1 51 51 1* WATER /
  I3 G1 14 24 1* WATER /
  I4 G1 24 14 1* WATER /
  I5 G1 24 34 1* WATER /
  I6 G1 34 24 1* WATER /
/

-- all wells with positive skin at start
COMPDAT
P1 2*  1 2 OPEN 2* 0.2 1* 10/
P3 2*  1 1 OPEN 2* 0.2 1* 10/
P4 2*  1 5 OPEN 2* 0.2 1* 10/
P5 2*  1 5 OPEN 2* 0.2 1* 10/
P6 2*  1 5 OPEN 2* 0.2 1* 10/
I1 2*  1 15 OPEN 2* 0.2 1* 10/
I2 2*  1 12 OPEN 2* 0.2 1* 10/
I3 2*  1 15 OPEN 2* 0.2 1* 10/
I4 2*  1 15 OPEN 2* 0.2 1* 10/
I5 2*  1 12 OPEN 2* 0.2 1* 10/
I6 2*  1 12 OPEN 2* 0.2 1* 10/
PS1 2*  1 12 OPEN 2* 0.2 1* 10/
PS2 2*  1 5 OPEN 2* 0.2 1* 10/
/

WCONPROD
P1 OPEN BHP 3* 200 1* 180 /
P3 OPEN LRAT 3* 60 1* 80 /
PS1 OPEN BHP 3* 160 1* 185 /
PS2 OPEN BHP 3* 160 1* 190 /
P4 OPEN BHP 3* 200 1* 170 /
P5 OPEN BHP 3* 200 1* 175 /
P6 OPEN BHP 3* 200 1* 210 /
/


WCONINJE
I2  WATER OPEN BHP 400 1* 400 /
I1  WATER OPEN BHP 400 1* 400 /
I3  WATER OPEN BHP 400 1* 400 /
I4  WATER OPEN BHP 400 1* 400 /
I5  WATER OPEN BHP 400 1* 400 /
I6  WATER OPEN BHP 400 1* 400 /
/

TSTEP  
  1*1/

-- change data at some point
COMPDAT
P1 2*  1 2 OPEN 2* 0.2 1* 11/
P3 2*  1 1 OPEN 2* 0.2 1* 12/
P4 2*  1 5 OPEN 2* 0.2 1* 10/
P5 2*  1 5 OPEN 2* 0.2 1* 12/
P6 2*  1 5 OPEN 2* 0.2 1* 11/
I1 2*  1 15 OPEN 2* 0.2 1* 8/
I2 2*  1 12 OPEN 2* 0.2 1* 7/
I3 2*  1 15 OPEN 2* 0.2 1* 8/
I4 2*  1 15 OPEN 2* 0.2 1* 10/
I5 2*  1 12 OPEN 2* 0.2 1* 7/
I6 2*  1 12 OPEN 2* 0.2 1* 9/
PS1 2*  1 12 OPEN 2* 0.2 1* 12/
PS2 2*  1 5 OPEN 2* 0.2 1* 13/
/

WCONPROD
P1 OPEN BHP 3* 200 1* 170 /
P3 OPEN LRAT 3* 70 1* 80 /
PS1 OPEN BHP 3* 160 1* 182 /
PS2 OPEN BHP 3* 160 1* 194 /
P4 OPEN BHP 3* 200 1* 150 /
P5 OPEN BHP 3* 200 1* 170 /
P6 OPEN BHP 3* 200 1* 190 /
/




TSTEP  
  1*1/

-- change data at some point
COMPDAT
P1 2*  1 2 OPEN 2* 0.2 1* 12/
P3 2*  1 1 OPEN 2* 0.2 1* 13/
P4 2*  1 5 OPEN 2* 0.2 1* 12/
P5 2*  1 5 OPEN 2* 0.2 1* 15/
P6 2*  1 5 OPEN 2* 0.2 1* 12/
I1 2*  1 15 OPEN 2* 0.2 1* 8/
I2 2*  1 12 OPEN 2* 0.2 1* 7/
I3 2*  1 15 OPEN 2* 0.2 1* 8/
I4 2*  1 15 OPEN 2* 0.2 1* 10/
I5 2*  1 12 OPEN 2* 0.2 1* 7/
I6 2*  1 12 OPEN 2* 0.2 1* 9/
PS1 2*  1 12 OPEN 2* 0.2 1* 13/
PS2 2*  1 5 OPEN 2* 0.2 1* 14/
/

WCONPROD
P1 OPEN BHP 3* 200 1* 174 /
P3 OPEN LRAT 3* 75 1* 80 /
PS1 OPEN BHP 3* 160 1* 180 /
PS2 OPEN BHP 3* 160 1* 190 /
P4 OPEN BHP 3* 200 1* 160 /
P5 OPEN BHP 3* 200 1* 160 /
P6 OPEN BHP 3* 200 1* 180 /
/


TSTEP  
  1*1/

-- change data at some point
COMPDAT
P1 2*  1 2 OPEN 2* 0.2 1* 15/
P3 2*  1 1 OPEN 2* 0.2 1* 18/
P4 2*  1 5 OPEN 2* 0.2 1* 12/
P5 2*  1 5 OPEN 2* 0.2 1* 16/
P6 2*  1 5 OPEN 2* 0.2 1* 13/
I1 2*  1 15 OPEN 2* 0.2 1* 7/
I2 2*  1 12 OPEN 2* 0.2 1* 6/
I3 2*  1 15 OPEN 2* 0.2 1* 4/
I4 2*  1 15 OPEN 2* 0.2 1* 10/
I5 2*  1 12 OPEN 2* 0.2 1* 7/
I6 2*  1 12 OPEN 2* 0.2 1* 9/
PS1 2*  1 12 OPEN 2* 0.2 1* 13/
PS2 2*  1 5 OPEN 2* 0.2 1* 17/
/

WCONPROD
P1 OPEN BHP 3* 200 1* 164 /
P3 OPEN LRAT 3* 95 1* 170 /
PS1 OPEN BHP 3* 160 1* 170 /
PS2 OPEN BHP 3* 160 1* 182 /
P4 OPEN BHP 3* 200 1* 163 /
P5 OPEN BHP 3* 200 1* 155 /
P6 OPEN BHP 3* 200 1* 140 /
/

TSTEP  
  1*1/






--Строительство скважины F1--
WELSPECS
-- WELLNAME GRPNAME I J BHPREF TYPE(PHASE) /
  F1     G1   33 68 1*        OIL /
/
COMPDAT
-- WELLNAME I J K1 K2 STATUS SATNUM  CF  RW(DIAM) KH SKIN  /
   F1   2*   1 13  OPEN     2*      0.2  1*  10 /
/
--Строительство скважины F2--
WELSPECS
-- WELLNAME GRPNAME I J BHPREF TYPE(PHASE) /
  F2     G1   51 85 1*        OIL /
/
COMPDAT
-- WELLNAME I J K1 K2 STATUS SATNUM  CF  RW(DIAM) KH SKIN  /
   F2   2*   1 13  OPEN     2*      0.2  1*  10 /
/
--Смена ГНО на скважине P6--
--Смена ГНО на скважине PS2--
--Смена ГНО на скважине PS1--
--Смена ГНО на скважине F1--
--Смена ГНО на скважине F2--
--Реперфорация скважины P1--
COMPDAT
-- WELLNAME I J K1 K2 STATUS SATNUM  CF  RW(DIAM) KH SKIN  /
   P1   2*   1 11  OPEN     2*        1*    1*  10 /
/
--Запуск скважины F1--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   F1    OPEN  BHP           3*          1*        1*   210 /
/
--Запуск скважины F2--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   F2    OPEN  BHP           3*          1*        1*   200 /
/
DATES
2 JUL 2020  0:0:0/
/
--Запуск скважины P5--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   P5    OPEN  BHP           3*          1*        1*   200.0 /
/
DATES
11 JUL 2020  0:0:0/
/
--Остановка скважины P1--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   P1    STOP  BHP           3*          10        1*   50 /
/
DATES
14 JUL 2020  0:0:0/
/
--Запуск скважины P1--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   P1    OPEN  BHP           3*          1*        1*   200.0 /
/
DATES
15 JUL 2020  0:0:0/
/
--Остановка скважины P3--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   P3    STOP  BHP           3*          10        1*   50 /
/
DATES
18 JUL 2020  0:0:0/
/
--Запуск скважины P3--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   P3    OPEN  BHP           3*          1*        1*   200.0 /
/
DATES
19 JUL 2020  0:0:0/
/
--Остановка скважины P6--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   P6    STOP  BHP           3*          10        1*   50 /
/
DATES
21 JUL 2020  0:0:0/
/
--Запуск скважины P6--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   P6    OPEN  BHP           3*          1*        1*   163.3 /
/
DATES
22 JUL 2020  0:0:0/
/
--Остановка скважины PS1--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   PS1    STOP  BHP           3*          10        1*   50 /
/
DATES
24 JUL 2020  0:0:0/
/
--Запуск скважины PS1--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   PS1    OPEN  BHP           3*          1*        1*   223.46 /
/
DATES
25 JUL 2020  0:0:0/
/
--Остановка скважины P4--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   P4    STOP  BHP           3*          10        1*   50 /
/
DATES
27 JUL 2020  0:0:0/
/
--Запуск скважины P4--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   P4    OPEN  BHP           3*          1*        1*   200.0 /
/
DATES
28 JUL 2020  0:0:0/
/
--Остановка скважины PS2--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   PS2    STOP  BHP           3*          10        1*   50 /
/
DATES
30 JUL 2020  0:0:0/
/
--Запуск скважины PS2--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   PS2    OPEN  BHP           3*          1*        1*   223.3 /
/
DATES
31 JUL 2020  0:0:0/
/
--Остановка скважины P5--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   P5    STOP  BHP           3*          10        1*   50 /
/
--big step in end--
DATES
31 JUL 2020  0:0:0/
/
--big step in end--
DATES
31 AUG 2020  0:0:0/
/
--big step in end--
DATES
30 SEP 2020  0:0:0/
/
--big step in end--
DATES
31 OCT 2020  0:0:0/
/
--big step in end--
DATES
30 NOV 2020  0:0:0/
/
