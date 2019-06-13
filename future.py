from __future__ import print_function

name = input('Please tell me your name:- ')
rawAge = input('Please tell me your age:- ')
age = int(rawAge)


if age>=19:
		print (name,'You are allowed in')
		print('What would like to have in drinks')
		drinks=["Whiskey(1)","Rum(2)","Beer(3)"]
		for drink in drinks:
				print (drink)
		asddrink = input('Please select the number of your drink:- ')
		finaldrinks = int(asddrink)
				
if age>=19:
	if finaldrinks ==1:
		print('Please selct your brand from our stock')
		drinks=["McDowells","Officers Choice","Royal Stag","teachers"]
		for drink in drinks:
				print (drink)
		drinker = input('Please select the preference of your brand:- ')
		
	if finaldrinks ==2:
		print('Please selct your brand from our stock')
		drinks=["Havana Club","Captain Morgan","Bacardi"]
		for drink in drinks:
				print (drink)
		drinker = input('Please select the preference of your brand:- ')

	if finaldrinks ==3:
		print('Please selct your brand from our stock')
		drinks=["Tuborg","Budweiser","Corona"]
		for drink in drinks:
				print (drink)
		drinker = input('Please select the preference of your brand:- ')
		
if age<=18:
			print(name,'You are allowed in but no drinks for you')
			drinker=('None')
			
if age<=200:
		items = ('1 for Veg Chinese', '2 for Non-Veg Chinese','3 for Non-Veg Starters','4 for Indian','5 for Italian')
		for item in items:
			print(item)
		Menu = input()
		Chinese = float(Menu)
		
	
if age>=19:
	if Chinese==1:
		chinese=['Hakka Noodles','Schezwan Noodles','Manchurian Dry','Manchurian Gravy','Fried Rice','Triple Schezwan Rice','Triple Schezwan Noodles']
		for china in chinese:
			print(china)
		CFood = input('Please Enter The Food from the above menu:- ')
		print(name,'Your order is',CFood,'and your drink is',drinker)
		
	if Chinese==2:
		chinese=['Chicken Hakka Noodles','Chicken Schezwan Noodles','Chicken Triple Rice','Chicken Lollipop','Chicken Fried Rice','Chicken Singapuri Noodles']
		for china in chinese:
			print(china)
		CFood = input('Please Enter The Food from the above menu:- ')
		print(name,'Your order is',CFood,'and your drink is',drinker)
		
	if Chinese==4:
		chinese=['Paneer Tikka Masala','Paneer Butter Masala','Mushroom Masala','Palak Paneer','Veg Jaffrezi','Dal Makhani','Dal Tadka','Dal Fry','Veg Kadai','Dum Aloo','Mix Veg','Paneer Bhurji','Jira Aloo','Aloo Muttar','Aloo Gobi']
		for china in chinese:
			print(china)
		CFood = input('Please Enter The Food from the above menu:- ')
		
		print('Please Enter Indian Bread from the above menu:- ')
		chinese=['Roti','Naan','Kulcha']
		for china in chinese:
			print(china)
		Roti = input('Here:- ')
		print(name,'Your order is',CFood,'with',Roti,'and your drink is',drinker)
	
	if Chinese==5:
		chinese=['Pasta in white sauce','Pasta in Red Sauce','Pizza','Cheese Pizza']
		for china in chinese:
			print(china)
		CFood = input('Please Enter The Food from the above menu:- ')
		print(name,'Your order is',CFood,'and your drink is',drinker)
	
	if Chinese==3:
		chinese=['Chicken Tandooei','Chicken Tikka','Reshami Chicken Tikka','Angari Chicken Tikka','Malai Chicken Tikka','Chicken Kheema with Bread']
		for china in chinese:
			print(china)
		CFood = input('Please Enter The Food from the above menu:- ')
		print(name,'Your order is',CFood,'and your drink is',drinker)

if age<=18:
	if Chinese==1:
		chinese=['Hakka Noodles','Schezwan Noodles','Manchurian Dry','Manchurian Gravy','Fried Rice','Triple Schezwan Rice','Triple Schezwan Noodles']
		for china in chinese:
			print(china)
		CFood = input('Please Enter The Food from the above menu:- ')
		print(name,'Your Order is',CFood)

	if Chinese==2:
		chinese=['Chicken Hakka Noodles','Chicken Schezwan Noodles','Chicken Triple Rice','Chicken Lollipop','Chicken Fried Rice','Chicken Singapuri Noodles']
		for china in chinese:
			print(china)
		CFood = input('Please Enter The Food from the above menu:- ')
		print(name,'Your Order is',CFood)
		
	if Chinese==4:
		chinese=['Paneer Tikka Masala','Paneer Butter Masala','Mushroom Masala','Palak Paneer','Veg Jaffrezi','Dal Makhani','Dal Tadka','Dal Fry','Veg Kadai','Dum Aloo','Mix Veg','Paneer Bhurji','Jira Aloo','Aloo Muttar','Aloo Gobi']
		for china in chinese:
			print(china)
		CFood = input('Please Enter The Food from the above menu:- ')
		print('Please Enter Indian Bread from the above menu:- ')
		chinese=['Roti','Naan','Kulcha']
		for china in chinese:
			print(china)
		Roti = input('Here:- ')
		print(name,'Your order is',CFood,'with',Roti)
	
	if Chinese==5:
		chinese=['Pasta in white sauce','Pasta in Red Sauce','Pizza','Cheese Pizza']
		for china in chinese:
			print(china)
		CFood = input('Please Enter The Food from the above menu:- ')
		print(name,'Your Order is',CFood)
	
	if Chinese==3:
		chinese=['Chicken Tandooei','Chicken Tikka','Reshami Chicken Tikka','Angari Chicken Tikka','Malai Chicken Tikka','Chicken Kheema with Bread']
		for china in chinese:
			print(china)
		CFood = input('Please Enter The Food from the above menu:- ')
		print(name,'Your Order is',CFood)
