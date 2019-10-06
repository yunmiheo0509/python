dayofweekli = [2, 5, 5, 1, 3, 6, 1, 4, 0, 2, 5, 0]  # 달의 시작 요일 리스트(0일요일,6토요일)
dayofweek=0
d_30 = [4, 6, 9, 11] #30일로 끝나는 달
d_31 = [1, 2, 3, 5, 7, 8, 10, 12] #31일로 끝나는 달
d_28 = 2 #2월달 28일
date = 0 #달의 끝나는 날짜 넣는 변수

month_input = int(input('월을 입력하세요(1-12):'))

dayofweek = dayofweekli[month_input-1] #달의 시작요일 넣는 변수
if month_input == d_28:
    date = 28
for i in d_30:
    if month_input == i:
        date = 30
date=31


print("           2019")
print('sun mon tue wed thr fri sat')
print('---------------------------')
j=1
i=1
while i<=date:
    if i == 1:
        while j <=dayofweek:
            print(end="    ")
            j=j+1
    if i < 10:
        print(end=" ")
    print(i,end="  ")
    if (dayofweek+1) % 7==0:
        print("")
    dayofweek=dayofweek+1
    i = i+1
print("")
print('-------------------------')
