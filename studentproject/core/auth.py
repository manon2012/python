def login():
    name = input("name:")
    passwd = input("passwd:")
    with open('userinfo') as f:
        for line in f:
            #print (line)
            user,pwd,ident=line.strip().split("|")
            if user==name and pwd==passwd:
                print ("login ok")
                #print (user,ident)
                return (user,ident)

