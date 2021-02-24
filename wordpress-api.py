from woocommerce import API
import json
from bs4 import BeautifulSoup

wcapi = API(
    url="http://localhost/wordpress/index.php",
    consumer_key="ck_29901a34af6f71014b011c6059849c2460573c8e",
    consumer_secret="cs_eef1dac2b22a089bd176ec54f09cb01fb30a137c",
    version="wc/v3"
)

# Force delete example.
# print(wcapi.delete("products/100", params={"force": True}).json())

# Query example.
# print(wcapi.get("products", params={"per_page": 20}).json())
# print(wcapi.get("products").json())

#########################################
# api_product_insert_example = {
#     "name": "Premium Quality",
#     "type": "simple",
#     "regular_price": "21.99",
#     "sale_price": "121.99",
#     "description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.",
#     "short_description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
#     "categories": [
#         {
#             "id": 9
#         },
#         {
#             "id": 14
#         }
#     ],
#     "images": [
#         {
#             "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_front.jpg"
#         },
#         {
#             "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_back.jpg"
#         }
#     ]
# }
#########################################

"""Inserta un producto en la BD"""
# wcapi.post("products", data).json()

"""

premiun = wcapi.get("products/1241").json()
for key,value in premiun.items():
	print(key,":",value)

print()
print("-------Categories------")
categories = wcapi.get("products/categories").json()

for i in categories:
	print(i)
"""


# data = {
#     "name": "Ropa",
#     "image": {
#         "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_front.jpg"
#     }
# }

# print(wcapi.post("products/categories", data).json())

# data = {
# 	"price": "21.54",
# 	"regular_price": "11.99",	#el regular price es el que cambia el precio
# 	"sale_price": "33",		  	#el precio rebajado 
# 	"manage_stock": "True",		#Activa Gestion de inventario True o False
# 	"stock_quantity": 33,		#Determina la cantidad en inventario
# }

test = {}
sku = ''
name = "Testeando"
type = "simple"
description = "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo."
short_description = "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas."
categories = [{"id": 17},{"id": 23}]
regular_price = "28"
sale_price = "33"
manage_stock = "True"
stock_quantity = "35"
images =  [
		    {"src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_front.jpg"}
		    ,
			{"src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_back.jpg"}
    	  ]

test['sku'] = sku
test['name'] = name
test['type'] = type
test['description'] = description
test['short_description'] = short_description
test['categories'] = categories
test['regular_price'] = regular_price
test['sale_price'] = sale_price
test['manage_stock'] = manage_stock
test['stock_quantity'] = stock_quantity
test['images'] = images


# print()
# print()
# print(data)

# print()
# print()
# print(test)


# wcapi.post("products", test).json()
# print()
# print('imprime las lista de las categorias')
# categories_list = wcapi.get("products/categories").json()
# for categorie in categories_list:
# 	print(categorie)
# 	print()

data = {}
regular_price = "11.54"
categories = [{"id": 17},{"id": 23}]

data['regular_price']=regular_price
data['categories']=categories

# wcapi.put("products/1253", data).json()

print()
print()
# info = wcapi.get("products?X-WP-TotalPages&X-WP-TotalPages").json()
# print(info)
print()
print()
print()

#########################################
### Configuracion de la conexion al servidor SQL ###
import pyodbc 
server = 'dbalcodesa.mssql.somee.com'
database = 'dbAlcodesa'
username = 'Camess_SQLLogin_1'
password = 'pelh6u7v1n'
cnxn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.7.so.1.1};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
######

cursor.execute('SELECT * FROM artAlco')
for row in cursor:
	print(row)
	test['sku'] = row[0]
	test['name'] = row[1]
	test['regular_price'] = str(row[3])
	if row[2] == 'INFANTIL':
		test['categories'] = [{"id": 24}]
	if row[2] == 'UNISEX':
		test['categories'] = [{"id": 25}]
	if row[2] == 'JUVENIL 	':
		test['categories'] = [{"id": 26}]

	if row[2] == '04 02 MEDICAMENTOS':
		test['categories'] = [{"id": 27}]
	if row[2] == '04 12 EQ P/MANEJO ANIMALES':
			test['categories'] = [{"id": 28}]
	if row[2] == '04 08 INST. VETERINARIO':
			test['categories'] = [{"id": 29}]
	if row[2] == '04 01 ALIMENTOS':
			test['categories'] = [{"id": 30}]

	test['manage_stock'] = True
	test['stock_quantity'] = row[4]
	test['images'] = images
	### La linea siguiente hace el insert en la API de Woocomerce de los datos captados de la BD
	wcapi.post("products", test).json()
	print(
			test['sku'],
			test['name'],
			test['regular_price'],
			test['categories'],
			test['manage_stock'],
			test['stock_quantity'],
			)
# print()
# print()
# cursor.execute('SELECT * FROM artAlco')
# for row in cursor:
# 	print(row)
# print()
# print("-------Categories------")
# categories = wcapi.get("products/categories").json()

# for i in categories:
# 	print(i)
# 	print("-------------------")
# cursor.execute('SELECT * FROM cteAlco')
# for row in cursor:
#     print(row)

#########################################
# api_customers_insert_example = {
#     "email": "john.doe@example.com",
#     "first_name": "John",
#     "last_name": "Doe",
#     "username": "john.doe",
#     "billing": {
#         "first_name": "John",
#         "last_name": "Doe",
#         "company": "",
#         "address_1": "969 Market",
#         "address_2": "",
#         "city": "San Francisco",
#         "state": "CA",
#         "postcode": "94103",
#         "country": "US",
#         "email": "john.doe@example.com",
#         "phone": "(555) 555-5555"
#     },
#     "shipping": {
#         "first_name": "John",
#         "last_name": "Doe",
#         "company": "",
#         "address_1": "969 Market",
#         "address_2": "",
#         "city": "San Francisco",
#         "state": "CA",
#         "postcode": "94103",
#         "country": "US"
#     }
# }
#########################################
customers_insert = {}
email 			= 'alejandro@sharingan.com'
first_name 		= 'Alejandro'
last_name 		= 'Mestre Argudin'
username 		= 'alejo'
company			= 'Rutabikes'
address_1		= 'San Rafael 807'
address_2		= 'Belascoain 905'
city			= 'La Habana'
state			= 'HA'
postcode		= '10400'
country			= 'CU'
phone			= '(555) 555-5555'
billing 		= {}
shipping 		= {}

customers_insert['email'] = email
customers_insert['first_name'] = first_name
customers_insert['last_name'] = last_name
customers_insert['username'] = username
customers_insert['billing'] =  {
								"first_name": first_name,
								"last_name": last_name,
								"company": company,
								"address_1": address_1,
						        "address_2": address_2,
						        "city": city,
						        "state": state,
						        "postcode": postcode,
						        "country": country,
						        "email": email,
						        "phone": phone
						        }
							
customers_insert['shipping'] = {
								"first_name": first_name,
								"last_name": last_name,
								"company": company,
								"address_1": address_1,
						        "address_2": address_2,
						        "city": city,
						        "state": state,
						        "postcode": postcode
						        }
### Borrar un usuario por el ID
# wcapi.delete("customers/13", params={"force": True}).json()
###

### Inserta un CUSTOMER a partir de un arreglo
# wcapi.post("customers", customers_insert).json()
###

# customers = wcapi.get('customers').json()
# for i in customers:
# 	for key,value in i.items():
# 		print(key,value)
# 		print()
# 	print('------------------------------------------------------------------------------------------------------------')

# print()
# print(customers_insert)
# print()

# print('CUSTOMERS')
# print()
# customers = wcapi.get('customers').json()
# for i in customers:
# 	for key,value in i.items():
# 		print(key,':',value)
# 		print()
# 	print('------------------------------------------------------------------------------------------------------------')

#########################################
# api_order_insert_example
order = {
    "payment_method": "bacs",
    "payment_method_title": "Direct Bank Transfer",
    "set_paid": True,
    "billing": {
        "first_name": "John",
        "last_name": "Doe",
        "address_1": "969 Market",
        "address_2": "",
        "city": "San Francisco",
        "state": "CA",
        "postcode": "94103",
        "country": "US",
        "email": "john.doe@example.com",
        "phone": "(555) 555-5555"
    },
    "shipping": {
        "first_name": "John",
        "last_name": "Doe",
        "address_1": "969 Market",
        "address_2": "",
        "city": "San Francisco",
        "state": "CA",
        "postcode": "94103",
        "country": "US"
    },
    "line_items": [
        {
            "product_id": 1378,
            "quantity": 2
        },
        {
            "product_id": 1377,
            "variation_id": 23,
            "quantity": 1
        }
    ],
    "shipping_lines": [
        {
            "method_id": "flat_rate",
            "method_title": "Flat Rate",
            "total": "10.00"
        }
    ]
}
#########################################
# wcapi.post("orders", order).json()

order_insert		 	= {}
payment_method 			= 'bacs'
payment_method_title	= "Direct Bank Transfer"
set_paid 				= True
billing			 		= {}
shipping 				= {}
line_items				= [
					        {"product_id": 1378,
					         "quantity": 2},
        					
        					{"product_id": 1377,
						     "variation_id": 23,
						     "quantity": 1}
						   ]
shipping_lines			= [
					        {
					        "method_id": "flat_rate",
				            "method_title": "Flat Rate",
				            "total": "10.00"
					        }
						   ]

order_insert['payment_method'] 		 = payment_method
order_insert['payment_method_title'] = payment_method_title
order_insert['set_paid'] 			 = set_paid
order_insert['billing'] 			 =  {
										"first_name": first_name,
										"last_name": last_name,
										"company": company,
										"address_1": address_1,
									    "address_2": address_2,
									    "city": city,
									    "state": state,
									    "postcode": postcode,
									    "country": country,
									    "email": email,
									    "phone": phone
									    }
							
order_insert['shipping'] 			= {
										"first_name": first_name,
										"last_name": last_name,
										"company": company,
										"address_1": address_1,
									    "address_2": address_2,
									    "city": city,
									    "state": state,
									    "postcode": postcode
									    }
order_insert['line_items'] 			= line_items
order_insert['shipping_lines']  	= shipping_lines

# wcapi.post("orders", order_insert).json()
# wcapi.post("orders", order).json()

# print('ORDERS')
# print()
# orders = wcapi.get('orders').json()
# for i in orders:
# 	for key,value in i.items():
# 		print(key,value)
# 		print()
# 	print('------------------------------------------------------------------------------------------------------------')

# print()
# for key,value in order_insert.items():
# 	print(key,value)
# print()
