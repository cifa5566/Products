#讀取檔案
products = []

with open('products.csv', 'r', encoding = 'utf-8') as f:  # encoding =編碼 讀取寫入需相同
	for line in f:
		name, price = line.strip().split(',') # strip()=去除/n , split(',')=用逗號分割資料 
		products.append([name, price])

print(products)



while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break;
	price = input('請輸入商品價格: ')
	price = int(price)

	products.append([name, price]) #二維清單 清單中含有清單

print(products)

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n') #加入標題
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')

	
