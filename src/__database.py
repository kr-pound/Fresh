#firebase import
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class database:
    username = None
    password = None

    product_name = None
    product_price = 0
    product_detail = None
    product_sold_status = None

    #store category
    product_veg = None
    product_fruit = None
    product_daily_product = None
    product_otop = None

    product_category = None

    def __init__(self):
        #path in local pc and database
        self.service_account_path = "C:/Users/krita/Documents/GitHub/SEP-Project/UI Design/Protocol - Coding/serviceAccountKey.json"
        self.database_url_path = "https://fresh-python-default-rtdb.asia-southeast1.firebasedatabase.app"
        self.cred = credentials.Certificate(self.service_account_path)
        self.default_app = firebase_admin.initialize_app(self.cred, {'databaseURL': self.database_url_path} )

        #set ref to the root of database
        self.ref = db.reference('/')

    #push data to database via ref
    def push_users(self, db_directory = '/users'):
        data = {'username' : self.username, 'password' : self.password}

        self.ref = db.reference(db_directory)
        self.ref.push(data)

        #implementation
        #database().push({'username' : 'AB', 'password' : '123456'}, 'sub_dir_name')

    def push_product(self, db_directory = '/product'):
        if (self.product_veg == True):
            self.product_category = "veg"
        if (self.product_fruit == True):
            self.product_category = "fruit"
        if (self.product_daily_product == True):
            self.product_category = "product"
        if (self.product_otop == True):
            self.product_category = "otop"

        data = {'name' : self.product_name, 'detail' : self.product_detail,
                'price' : self.product_price, 'category' : self.product_category, 'sold': 'no'}

        self.ref = db.reference(db_directory)
        self.ref.push(data)

    #return the data reference in database
    def __get_data(self, key, value, db_directory = '/'):
        ref = db.reference(db_directory)
        search_data = ref.order_by_child(key).equal_to(value).get()

        #for the first key found, return value
        for key, val in search_data.items():
                return val
            
    def is_visible(self, key, value, db_directory = '/'):
        self.ref = db.reference(db_directory)

        #check if the data is visible
        if self.__get_data(key, value, db_directory) != None:
            return True
        else:
            return False
        
        #implementation
        #print(database().is_visible('username', 'ABC', '/users'))
    
    def get_password(self, user_key, user_value, db_directory = '/users'):
        val = self.__get_data(self, user_key, user_value, db_directory)

        self.username = None
        self.password = None

        #set username & password receive from __get_data()
        if val != None:
            self.username = val["username"]
            self.password = val["password"]

        #implementation
        #print(database().get_username_password('username', 'ABC'))

    def get_product(self, db_directory = '/product'):
        ref = db.reference(db_directory)
        product_data = ref.get()

        product_list = []

        #put all product in the list
        for key, val in product_data.items():
            product_list.append(val)

        return product_list

        #implementation
        #print(database().get_product())

    
    def update_node(self, child_key, key_set, value_set, db_directory = '/'):
        self.ref = db.reference(db_directory)
        key = self.ref.child('-MbjVvSyo0fcBG85whjb').get()
        #print(key)
        #return self.ref.child('-MbjVvSyo0fcBG85whjb').child(key).remove()

        return self.ref.child('product').child('-MbjVvSyo0fcBG85whjb').update({'name': 'a'})

    #print all the list in directory
    def show_list(self, db_directory = '/', print_data = True):
        self.ref = db.reference(db_directory)
        data = self.ref.get()

        #determine when to print the data
        if (print_data):
            print(data)

        #implementation
        #print(database().show_list('/users'))


#print(database().delete_node())
