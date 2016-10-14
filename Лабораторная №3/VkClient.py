import BaseClient
import requests
import json
import datetime

class VkClient(BaseClient.BaseClient):
    def __init__ (self, method):
        self.BASE_URL = 'https://api.vk.com/method/'
        self.method = method
        self.http_method = 'get'
        
        
    def get_json(self):
        pass
        
        
    def get_dict_data(self):
        dict_data = json.loads(self.execute())
        return dict_data

        
    def _get_data(self, method, http_method):
        response = None
        if http_method == 'get':
            response = requests.get(self.generate_url(method))
        return self.response_handler(response)
        
        
    def response_handler(self,response):
        dict_data = ""
        dict_data = json.loads(response.text)
        if "error" in dict_data.keys():
            raise Exception
        return response.text

        
def create_args(args):
    return "&".join("%s=%s" % (key, value) for key, value in args.items())
        
        
def check_bdatt(obj):
    return ("bdate" in obj.keys()) and (len(obj["bdate"].split('.')) == 3)

    
if __name__ == "__main__" :
    name = input("Введите ID>")
    try:
        vk_name = VkClient('users.get?user_ids=' + name)
        name = vk_name.get_dict_data()
        if (name is None) or (not 'uid' in name['response'][0]):
            raise Exception
    except Exception:
        print('Вы ввели некорректную информацию')
        exit()
        
    # Для точности выведем немного информации о том, кого мы нашли
    print('Имя пользователя VK: ' + name['response'][0]['first_name'] + ' ' + name['response'][0]['last_name'])
    
    # Сегодняшняя дата (для вычисления возраста)
    now = datetime.date.today()
    # Словарь для кол-ва людей определенного возраста
    old_arr = {}
    
    # Аргументы для выборки друзей
    args = {
        "user_id":name['response'][0]['uid'], 
        "fields":"bdate", 
        "v":"5.57"
    }
    
    
    try:
        vk = VkClient('friends.get?' + create_args(args))
        tmp = vk.get_dict_data()["response"]["items"]
    except Exception:
        print('Что-то произошло при попытке получить пользователя')
        exit()

    for x in tmp:
        if check_bdatt(x):
            bdate_arr = x["bdate"].split('.')
            bdate = datetime.date(
                    int(bdate_arr[2]), 
                    int(bdate_arr[1]), 
                    int(bdate_arr[0])
                    )
            diff = int((now - bdate).days / 365)
            if not diff in old_arr.keys():
                old_arr[diff] = 0
            old_arr[diff] = old_arr[diff]+ 1
        
    
    # Выведем в более менее приличном формате
    for key in sorted(old_arr):
        print(str(key) + ' ' + '#'.join('' for i in range(old_arr[key]+1)))
    