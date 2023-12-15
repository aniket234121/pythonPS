list=[[1,2,3],[45,454,65],[12,76,45]]
for i in range(len(list)):
    for j in range(len(list[i])):
        list[i].reverse()
        print(list[i][j],end=" ")
    print()