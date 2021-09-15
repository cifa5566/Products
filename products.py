import os # operating system
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:  # encoding =編碼 讀取寫入需相同
			for line in f:
				if '商品,價格' in line:
					continue  #跳過標題 繼續迴圈
				name, price = line.strip().split(',') # strip()=去除/n , split(',')=用逗號分割資料 
				products.append([name, price])	
	return products  #把讀完的資料存起來

def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break;
		price = input('請輸入商品價格: ')
		price = int(price)
		products.append([name, price]) #二維清單 清單中含有清單
	print(products)
	return products

def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n') #加入標題
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main(): #主要執行程式碼
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('Yes')
		products = read_file(filename)
	else:
		print('找不到檔案')
	products = user_input(products) #透過user_input函式更新products資料
	print_products(products)
	write_file('products.csv', products)

main()

