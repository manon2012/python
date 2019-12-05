import requests
import json

# url = 'http://account/login'
# data = {
#     "username":"01",
#     "password":"password",
# }
# res=requests.post(url,data).json()
# print(res)


# def send_post(url,data):
#     result = requests.post(url, data).json()
#     res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
#     print (res)
#
# if __name__ == '__main__':
#     url = 'http://account/login'
#     data = {
#         "username":"01",
#         "password":"password",
#     }
#
#     ress=send_post(url,data)


class Runmain:
    def send_post(self,url,data):
        result = requests.post(url, data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        print (res)

    def send_get(self,url,data):
        result = requests.get(url, data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        print (res)

    def run_main(self,method,url,data):
        result =None
        if method == "post":
            result = self.send_post(url,data)
        elif method =="get":
            result = self.send_get()
        else:
            print ("wrong method")
        return result

if __name__ == '__main__':
    url = 'http://account/login'
    data = {
        "username":"01",
        "password":"password",
    }

    run=Runmain()
    res =run.run_main("post",url,data)
    print (res)

