import time
import random
def buyonestock(stockname = '001'):
    n=random.random()
    if n>0.5:
        return
    else:
        raise ValueError("value error")

max_try=5
try_num=0
while True:

    try:
        buyonestock()
    except Exception as e:
        print (e,"wrong when transaction"),
        try_num +=1
        #time.sleep(1)
        if try_num <=max_try:
            continue
        else:
            break
        # if try_num>max_try:
        #     print ("not buy")
        #     break
    else:
        print ("well done")
        break

