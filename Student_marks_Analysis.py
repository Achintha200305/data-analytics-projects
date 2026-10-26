import numpy as np
import pandas as pd
Student_data=np.array([[85, 78, 90, 92, 88],
                       [65, 70, 68, 75, 80],
                       [45, 52, 48, 60, 55],
                       [92, 88, 95, 98, 90],
                      [30, 42, 35, 50, 45]])
row_names=["STU001","STU002","STU003","STU004","STU005"]
col_name=["Maths","Statistics","Physics","Programming","English"]
df=pd.DataFrame(Student_data,columns=col_name,index=row_names)
print(df)

df["Total_h"]=np.sum(Student_data,axis=1)
df["Average_of_Std"]=np.mean(Student_data,axis=1)

df["student_Ave_v"]=np.mean(Student_data,axis=1)
subject_array = np.array(col_name)
max_indices = np.argmax(Student_data, axis=1)
df["Top_Subject"] = subject_array[max_indices]

df["Highest_Mark"]=np.max(Student_data,axis=0)
print(df)

