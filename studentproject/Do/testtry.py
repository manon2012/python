
def testtry():
    sum=0
    count =0
    numlist=[]
    while True:

        number = input("please input number:")
        try:
            number = int(number)
            numlist.append(number)
        except Exception as e:
            print (e)
            continue
        sum +=number
        count+=1
        try:
            ret= sum/count
            if len(numlist)==5:
                print ("5 day average price is %s"% ret)
            elif len(numlist) == 10:
                print ("10 day %s"%ret)
            else:
                print(ret)
        except Exception as e:
            print ("lll,",e)


testtry()