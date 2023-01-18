import requests as r

url = 'https://api.agify.io/?name=seongmin'

b = r.get(url).json()
name=b['name']
age=b['age']

print('{}의 나이는 {}짤! 응애!\n{}은 무거워서 놓고다녀욧!'.format(name,age%10,(age//10)*10))

print('a')