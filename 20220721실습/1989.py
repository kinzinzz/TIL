T = int(input())

for i in range(1,T+1):
    str = input()
    
    if len(str) % 2 == 0:
        center_index = int(((len(str)) / 2))
        str_list = list(str)
        
        left_list = str_list[:center_index]
        right_list = str_list[center_index:]
                        
        if left_list != list(reversed(right_list)):
            print(f'#{i}', 0, end ='')
            print('')
            
        elif left_list == list(reversed(right_list)):
            print(f'#{i}', 1, end ='')
            print('')
                       
        
    else :
        center_index = int((len(str)-1) / 2)
        str_list = list(str)
        
        left_list = str_list[:center_index]
        right_list = str_list[center_index+1:]
                        
        if left_list != list(reversed(right_list)):
            print(f'#{i}', 0, end ='')
            print('')
            
        elif left_list == list(reversed(right_list)):
            print(f'#{i}', 1, end ='')
            print('') 
            