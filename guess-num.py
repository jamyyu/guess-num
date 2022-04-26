#產生一個隨機整數1~100(不要印出來)
#讓使用者重複輸入數字去猜
#猜對印出“終於答對了！”
#猜錯要告訴他 比答案大／小

import random
start = input('請決定隨機數字範圍開始值：')
end = input('請決定隨機數字範圍結束值：')
start =int(start)
end = int(end)

r = random.randint (start, end)
count = 0 #加入1個計數功能
while True:
    count += 1 #count = count + 1 快寫法
    num = input('請猜數字：')
    num = int(num)
    if num == r:
        print('終於猜對了！')
        print('這是你猜的第', count, '次')
        break
    elif num > r:
    	print('比答案大')
    else:
    	print('比答案小')
    print('這是你猜的第', count, '次') #印3樣東西，字串 整數 字串，用逗點隔開

