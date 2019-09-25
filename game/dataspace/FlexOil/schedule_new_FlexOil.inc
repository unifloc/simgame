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






--Строительство скважины PS9--
WELSPECS
-- WELLNAME GRPNAME I J BHPREF TYPE(PHASE) /
  PS9     G1   69 69 1*        OIL /
/
COMPDAT
-- WELLNAME I J K1 K2 STATUS SATNUM  CF  RW(DIAM) KH SKIN  /
   PS9   2*   1 2  SHUT     2*      0.2  1*  10 /
/


DATES
2 JUL 2020  1:0:0/
/
--Строительство скважины PS8--
WELSPECS
-- WELLNAME GRPNAME I J BHPREF TYPE(PHASE) /
  PS8     G1   38 69 1*        WATER /
/
COMPDAT
-- WELLNAME I J K1 K2 STATUS SATNUM  CF  RW(DIAM) KH SKIN  /
   PS8   2*   1 2  SHUT     2*      0.2  1*  10 /
/


DATES
3 JUL 2020  1:0:0/
/
--Реперфорация скважины PS9--
COMPDAT
-- WELLNAME I J K1 K2 STATUS SATNUM  CF  RW(DIAM) KH SKIN  /
   PS9   2*   11 15  OPEN     2*        1*    1*  10 /
/


DATES
4 JUL 2020  1:0:0/
/
--Реперфорация скважины PS8--
COMPDAT
-- WELLNAME I J K1 K2 STATUS SATNUM  CF  RW(DIAM) KH SKIN  /
   PS8   2*   11 15  OPEN     2*        1*    1*  10 /
/


DATES
5 JUL 2020  1:0:0/
/
--Смена ГНО на скважине PS9--


DATES
7 JUL 2020  1:0:0/
/
--Запуск скважины PS9--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   PS9    OPEN  BHP           3*          1*        1*   150.0 /
/


DATES
8 JUL 2020  1:0:0/
/
--Запуск скважины PS8--
WCONINJE
-- WELLNAME FLUID STATUS CONTROL RATE RESV BHP /
   PS8   WATER  OPEN  BHP     100.0        1*   200.0 /
/


DATES
9 JUL 2020  1:0:0/
/
--Запуск скважины P1--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   P1    OPEN  BHP           3*          1*        1*   200.0 /
/


DATES
10 JUL 2020  1:0:0/
/
--Остановка скважины P3--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   P3    STOP  BHP           3*          10        1*   50 /
/


DATES
11 JUL 2020  1:0:0/
/
--Запуск скважины P3--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   P3    OPEN  LRAT           3*          100.0        1*   200 /
/


DATES
12 JUL 2020  1:0:0/
/
--Строительство скважины PS10--
WELSPECS
-- WELLNAME GRPNAME I J BHPREF TYPE(PHASE) /
  PS10     G1   73 15 1*        OIL /
/
COMPDAT
-- WELLNAME I J K1 K2 STATUS SATNUM  CF  RW(DIAM) KH SKIN  /
   PS10   2*   1 2  SHUT     2*      0.2  1*  10 /
/


DATES
13 JUL 2020  1:0:0/
/
--Реперфорация скважины PS10--
COMPDAT
-- WELLNAME I J K1 K2 STATUS SATNUM  CF  RW(DIAM) KH SKIN  /
   PS10   2*   11 15  OPEN     2*        1*    1*  10 /
/


--big step--0
DATES
31 JUL 2020  0:0:0/
/


DATES
14 AUG 2020  1:0:0/
/
--Смена ГНО на скважине PS10--


--big step--1
DATES
31 AUG 2020  0:0:0/
/


DATES
14 SEP 2020  2:0:0/
/
--Запуск скважины PS10--
WCONPROD
-- WELLNAME STATUS CONTROL ORATE WRATE GRATE LRATE RESV BHP /
   PS10    OPEN  BHP           3*          1*        1*   150.0 /
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


