T = int(input())

for i in range(1,T+1):
    
        str_list = list(str(i))
        count = 0 

        count = str_list.count('3') + str_list.count('6') + str_list.count('9')

        if count == 0:
            print(i,end=' ')      

        else:         
            print('-'*count,end=' ')
   

