import requests
from django.conf import settings

class Fetch:

    def __init__(self,path="/",method="GET",token=None,data={},params={}):
        self._path = path
        self._url = f'{settings.URL_SERVICE}/{path}'
        self._method = method
        self._data = data
        self._token = token
        self._params = params
        self._headers = headers = {
                'Content-Type': 'application/json; charset=utf-8',
                'Authorization': f'Bearer {settings.KEY_API}'
            }

    def getToken(self):
        data={
              "usuario": "1113.jmonroy",
              "password": "radlt"
             }
        try:
            response = requests.post(
                url= f'{settings.URL_SERVICE}/authentication/login', 
                headers= {"Content-Type": "application/json; charset=utf-8"}, 
                json= data)
            if response.status_code == 200:
                return response.json()
            else:
                print("Error en el status")
                return None
        except Exception as e:
            print(e)
            return None

    def strParams(self):
        for key in self._params:
            return'&'.join(f'{key}={value[0]}' for key, value in self._params.items())

    def send(self):
        count = 1
        try:
            if self._method.upper() == "GET":
                response = requests.get( url=self._url, params=self._params, headers=self._headers )
                if response.status_code == 200:
                    return response.json()
                else:
                    return { 'message': response.json() }
        except Exception as e:
            count = count + 1
            if count <=3:
                return self.send()
            else:
                return {'message': f'Intento fallido al realizar la peticion :: {count}'}
        