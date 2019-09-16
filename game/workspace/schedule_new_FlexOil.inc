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
--P3 2*  1 1 OPEN 2* 0.2 1* 10/
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
--P3 OPEN LRAT 3* 60 1* 80 /
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
  4*30/

-- change data at some point
COMPDAT
P1 2*  1 2 OPEN 2* 0.2 1* 11/
--P3 2*  1 1 OPEN 2* 0.2 1* 12/
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
--P3 OPEN LRAT 3* 70 1* 80 /
PS1 OPEN BHP 3* 160 1* 182 /
PS2 OPEN BHP 3* 160 1* 194 /
P4 OPEN BHP 3* 200 1* 150 /
P5 OPEN BHP 3* 200 1* 170 /
P6 OPEN BHP 3* 200 1* 190 /
/




TSTEP  
  4*30/

-- change data at some point
COMPDAT
P1 2*  1 2 OPEN 2* 0.2 1* 12/
--P3 2*  1 1 OPEN 2* 0.2 1* 13/
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
--P3 OPEN LRAT 3* 75 1* 80 /
PS1 OPEN BHP 3* 160 1* 180 /
PS2 OPEN BHP 3* 160 1* 190 /
P4 OPEN BHP 3* 200 1* 160 /
P5 OPEN BHP 3* 200 1* 160 /
P6 OPEN BHP 3* 200 1* 180 /
/


TSTEP  
  3*30/

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
  2*30/






WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   PS1    STOP  BHP           3*          10        1*   50 /
/
TSTEP
 5*0.1
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   PS1    OPEN  BHP           3*          1*        1*   200.0 /
/
TSTEP
 25*0.1
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   PS2    STOP  BHP           3*          10        1*   50 /
/
TSTEP
 5*0.1
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   PS2    OPEN  BHP           3*          1*        1*   200.0 /
/
TSTEP
 5*0.1
/
COMPDAT
-- name x y z1 z2 perf table  CF  diam KH skin  /
   P1   2*    1*   1*   OPEN     2*        1*    1*  7.5 /
/
TSTEP
 10*0.1
/
TSTEP
 20*0.1
/
TSTEP
 19*0.1
/
TSTEP
 20*0.1
/
TSTEP
 10*0.1
/
WELSPECS
-- name group x y pwf_depth phase /
  PS9     G1   69 69 1*        OIL /
/
COMPDAT
-- name x y z1 z2 perf table  CF  diam KH skin  /
   PS9   2*   1 2  SHUT     2*      0.2  1*  10 /
/
WELSPECS
-- name group x y pwf_depth phase /
  PS8     G1   38 69 1*        OIL /
/
COMPDAT
-- name x y z1 z2 perf table  CF  diam KH skin  /
   PS8   2*   1 2  SHUT     2*      0.2  1*  10 /
/
COMPDAT
-- name x y z1 z2 perf table  CF  diam KH skin  /
   PS9   2*   11 15  OPEN     2*        1*    1*  10 /
/
COMPDAT
-- name x y z1 z2 perf table  CF  diam KH skin  /
   PS8   2*   11 15  OPEN     2*        1*    1*  10 /
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   P1    STOP  BHP           3*          10        1*   50 /
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   PS9    OPEN  BHP           3*          1*        1*   150.0 /
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   PS8    OPEN  BHP           3*          1*        1*   150.0 /
/
TSTEP
 9*0.1
/
TSTEP
 15*0.1
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   P1    OPEN  BHP           3*          1*        1*   200.0 /
/
TSTEP
 5*0.1
/
TSTEP
 1*0.1
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   P3    STOP  BHP           3*          10        1*   50 /
/
TSTEP
 19*0.1
/
TSTEP
 10*0.1
/
WELSPECS
-- name group x y pwf_depth phase /
  P7     G1   50 85 1*        OIL /
/
COMPDAT
-- name x y z1 z2 perf table  CF  diam KH skin  /
   P7   2*   1 2  SHUT     2*      0.2  1*  10 /
/
COMPDAT
-- name x y z1 z2 perf table  CF  diam KH skin  /
   P7   2*   11 15  OPEN     2*        1*    1*  10 /
/
TSTEP
 37*0.1
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   P3    OPEN  BHP           3*          1*        1*   200.0 /
/
TSTEP
 2*0.1
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   P4    STOP  BHP           3*          10        1*   50 /
/
TSTEP
 17*0.1
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   P4    OPEN  BHP           3*          1*        1*   200.0 /
/
TSTEP
 2*0.1
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   P5    STOP  BHP           3*          10        1*   50 /
/
TSTEP
 19*0.1
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   P5    OPEN  BHP           3*          1*        1*   190 /
/
TSTEP
 1*0.1
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   P6    STOP  BHP           3*          10        1*   50 /
/
TSTEP
 18*0.1
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   P6    OPEN  BHP           3*          1*        1*   190 /
/
TSTEP
 220*0.1
/
TSTEP
 10*0.1
/
WCONPROD
-- name status control orate wrate grate lrate lrateres bhp /
   P7    OPEN  BHP           3*          1*        1*   190 /
/
TSTEP
 10*0.1
/
WELSPECS
-- name group x y pwf_depth phase /
  I22     G1   55 53 1*        WATER /
/
COMPDAT
-- name x y z1 z2 perf table  CF  diam KH skin  /
   I22   2*   1 2  SHUT     2*      0.2  1*  10 /
/
TSTEP
 10*0.1
/
COMPDAT
-- name x y z1 z2 perf table  CF  diam KH skin  /
   I22   2*   11 15  OPEN     2*        1*    1*  10 /
/
TSTEP
 10*0.1
/
WCONINJE
-- name fluid status control lrate lrateres bhp /
   I22   WATER  OPEN  BHP     1*        1*   400 /
/
TSTEP
 10*0.1
/
