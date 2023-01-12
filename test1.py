import requests as r

num = input('원하시는 회차를 입력해 주세요 : ')

url='https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=' + num

a= r.get(url).json()

a1=a['drwNo']

nums=[]
for i in range(1,7):
    key='drwtNo'+str(i)
    nums.append(a[key])

s=''
for i in nums:
    if i == nums[5]:
        s = s + str(i)
    else:
        s = s + str(i) + ','

a8=a['bnusNo']


print('{}회차의 당첨번호는 {} 보너스번호는 {}입니다.'.format(a1,s,a8))