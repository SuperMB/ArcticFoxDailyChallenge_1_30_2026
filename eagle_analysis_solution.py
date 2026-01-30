 
import pandas as pd
import numpy as np
import arcticfox  
arcticfox.projectpath('eagle_analysis_solution.py')  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 



### Kits that willl be helpful - Data, View, ColumnOp, RowSort
### The focus of this challenge is doing column based computations

## We will compute the GOLDEN EAGLE RATIO!!! 
## To determine the Eagle with the highest flight altitue.

## The GOLDEN EAGLE RATIO is:
##     Wingspan * Average Talon / Beak Size

## Why is this the equation? Nobody knows...



# Load the eagle_measurements.csv
#> Data eagle_measurements.csv 
eagle_measurementsDf = pd.read_csv('eagle_measurements.csv') 

# Compute the wingspan
#> ColumnOp _Wingspan_ = _LeftWingLength_cm_ + _RightWingLength_cm_ 
eagle_measurementsDf['Wingspan'] = eagle_measurementsDf['LeftWingLength_cm'] + eagle_measurementsDf['RightWingLength_cm'] 

# Compute the average talon size
#> ColumnOp _AverageTalon_ = (_LeftTalonLength_cm_ + _RightTalonLength_cm_) / 2 
eagle_measurementsDf['AverageTalon'] = (eagle_measurementsDf['LeftTalonLength_cm'] + eagle_measurementsDf['RightTalonLength_cm']) / 2 

# Compute the GOLDEN EAGLE RATIO!
#> ColumnOp _EagleMeasure_ = _Wingspan_ * _AverageTalon_ / _BeakLength_cm_ 
eagle_measurementsDf['EagleMeasure'] = eagle_measurementsDf['Wingspan'] * eagle_measurementsDf['AverageTalon'] / eagle_measurementsDf['BeakLength_cm'] 

# Get the Eagle with the largest GOLDEN EAGLE RATIO 
# and submit its name!

#> RowSort EagleMeasure--descending 
eagle_measurementsDf.sort_values(by='EagleMeasure', ascending=False, inplace=True) 

#> View 
print(eagle_measurementsDf.astype(str).fillna('').head()) #)1 
##***        EagleName LeftWingLength_cm RightWingLength_cm LeftTalonLength_cm RightTalonLength_cm BeakLength_cm            Wingspan       AverageTalon        EagleMeasure
##*** 212   AspenBluff             67.55              66.52               8.28                8.76          6.27              134.07               8.52  182.18124401913877
##*** 2    IronThermal             65.01               65.0               7.96                8.01          6.11              130.01  7.984999999999999   169.9066857610474
##*** 49   SummitSpire             69.04              69.56               7.24                7.51          6.05  138.60000000000002              7.375   168.9545454545455
##*** 21    SunFeather             62.04              61.49               8.18                8.38          6.14              123.53  8.280000000000001  166.58442996742673
##*** 71    BeaconVale             67.91              68.22               8.36                8.69           7.0              136.13  8.524999999999999  165.78689285714285
