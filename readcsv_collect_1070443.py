#pure python
# with open('C:\homework\機器學習\第三周\data_with_classes.csv','r') as csvfile:
#     next(csvfile)
#     matclass=[[]for _ in range(3)]
#     print(matclass)
#     for row in csvfile:
#         row=row.strip()
#         row=row.split(',')
#         print(row[5])
        
#         index=int(row[5])-1
#         matclass[index].append(row[:5])
#     # print(matclass[0])
#     matclass1=matclass[0]
#     matclass2=matclass[1]
#     matclass3=matclass[2]
#     print(matclass1)

        

#用pandas
# import pandas as pd
# csvfile = pd.read_csv('C:\homework\機器學習\第三周\data_with_classes.csv')
# print(csvfile)
# group =csvfile.groupby('Class')
# group_lst=list(group) #group:[tuple[Scalar, DataFrame]]
# matclass1=group_lst[0][1]
# matclass2=group_lst[1][1]
# matclass3=group_lst[2][1]
# matclass1=matclass1.values.tolist()
# matclass2=matclass2.values.tolist()
# matclass3=matclass3.values.tolist()#將dataframe轉list
# print(matclass1)
# print(type(matclass1))

import pandas as pd
csvfile=pd.read_csv(r'C:\homework\機器學習\第三周\data_with_classes.csv')
row_n,col_n=csvfile.shape
columns_lst=csvfile.columns
matclass=[]
for i in range(1,4):#第一次將class=1分成一組,...
    n=(csvfile['Class']==i)
    data=pd.DataFrame(csvfile[n],columns=columns_lst[:-1])#把class排除掉
    data=data.values.tolist()
    matclass.append(data)
matclass1=matclass[0]
matclass2=matclass[1]
matclass3=matclass[2]
print(matclass1)
print(matclass2)
print(matclass3)



