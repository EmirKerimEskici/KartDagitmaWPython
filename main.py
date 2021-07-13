import random
import time

renkler=['Karo','Maça','Sinek','Kupa']
sayilarimiz=[1,2,3,4,5,6,7,8,9,10,'jilet','Kız','Papaz']
kagitlar=[]
a=[]
b=[]
c=[]
d=[]

for i in renkler:
	for renk in sayilarimiz:
		kagitlar.append(i+' '+str(renk))

i=52
while i!=39:
	r=random.choice(kagitlar)
	time.sleep(0.5)
	a.append(r)
	kagitlar.remove(r)
	i=i-1


while i!=26:
	r=random.choice(kagitlar)
	time.sleep(0.4)
	b.append(r)
	kagitlar.remove(r)
	i=i-1

while i!=13:
	r=random.choice(kagitlar)
	time.sleep(0.3)
	c.append(r)
	kagitlar.remove(r)
	i=i-1

while i!=0:
	r=random.choice(kagitlar)
	time.sleep(0.2)
	d.append(r)
	kagitlar.remove(r)
	i=i-1

print("KEREM'İN ELİ 1:")
for l in a:
	print(l)

print('#######')

print("YUNUS'UN ELİ 2:")
for l in b:
	print(l)

print('########')

print("ATAKAN'IN ELİ 3:")
for l in c:
	print(l)

print('########')

print("BERKAN'IN ELİ 4:")
for l in d:
	print(l)


print('BOL ŞANSLAR BEYLER')