from urllib import parse
from constants import RETURN_URL, URL_FOR_OAUTH, URL_FOR_TOKEN, STATE

API_KEY = input('1) Введите идентификатор клиента:')

values = {'response_type': 'code',
          'client_id': API_KEY,
          'redirect_uri': RETURN_URL,
          'state': STATE,
          'scope': 'r_basicprofile'}

data = parse.urlencode(values)
myURL = URL_FOR_OAUTH + str(data)

print(f'2) Перейдите по ссылке ниже:\n{myURL}')

CODE = input('3) Войдите на сайт, если он того требует, или сразу же в адресной строке браузера\n'
             'скопируйте значение "code" ("code=" то,что надо скопировать "&state")'
             'и вставьте сюда:')

API_SECRET = input('4) Введите секретный ключ клиента:')

values2 = {'grant_type': 'authorization_code',
           'code': CODE,
           'redirect_uri': RETURN_URL,
           'client_id': API_KEY,
           'client_secret': API_SECRET}

data2 = parse.urlencode(values2)
myURL2 = str(data2)

print(f'5) Скопируйте строку ниже и запустите ее в терминале:\n'
      f'curl {URL_FOR_TOKEN} -d "{myURL2}"\n'
      f'Вы должны получить "access_token".')

