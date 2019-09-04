# format 이용
food_list = ['apple','pear']
place = 'gachon'
formatting_str = "i eat {food}, and i will go {place}"
for i in food_list:
    print(formatting_str.format(food=i, place=place))


# cron : 정기적으로 crawling할 때 사용
## 형식 : (분) (시) (일) (월) (요일) <실행할 명령어의 경로>
