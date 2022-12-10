t=int(input())
for i in range(t):
    n=int(input())
    given_list= [int(x) for x in input().split()]
    count_value = 0
    for i in given_list:
        if given_list.count(i)>2:
            count_value = 1
            print ('NO')
            break
    if count_value == 0:
        print('YES')