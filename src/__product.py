from __database import database

#product store in class
class CartProductClass():
    product = [None] * 5
    product_list = None

    #buying product list
    buy_list = [None] * 6
    #total_price calculated
    total_price = 0

    #product information
    productLabel1 = None
    productLabel2 = None
    productLabel3 = None
    productLabel4 = None
    productLabel5 = None

    buyingButton1 = None
    buyingButton2 = None
    buyingButton3 = None
    buyingButton4 = None
    buyingButton5 = None

    productDescription1 = None
    productDescription2 = None
    productDescription3 = None
    productDescription4 = None
    productDescription5 = None

    productAmount1 = ""
    productAmount2 = ""
    productAmount3 = ""
    productAmount4 = ""
    productAmount5 = ""

    productPicture1 = ""
    productPicture2 = ""
    productPicture3 = ""
    productPicture4 = ""
    productPicture5 = ""

    productTick1 = ""
    productTick2 = ""
    productTick3 = ""
    productTick4 = ""
    productTick5 = ""

    productSoldStatus1 = None
    productSoldStatus2 = None
    productSoldStatus3 = None
    productSoldStatus4 = None
    productSoldStatus5 = None

    def __init__(self):
        self.db = database()
        self.load_product_data()

    def load_product_data(self):
        #receive product dictionary from database
        self.product_list = database.get_product('/product')
        #create list of each product object in page
        while(len(self.product) < len(self.product_list)):
            self.product += [None] * 5
        
        #store product objects in the list
        id_count = 0
        for product in self.product_list:
            #get any data from dictionary
            name = self.product[id_count] = product["name"]
            price = self.product[id_count] = product["price"]
            detail = self.product[id_count] = product["detail"]
            picture = self.product[id_count] = product["category"] + ".png"
            status = self.product[id_count] = product["sold"]

            #store the object within a list
            self.product[id_count] = ProductClass(name, price, detail, picture, status)
            id_count += 1

        print("\nProduct Data: ", end="")
        print(self.product)

    def update_status(self):
        #id_count = 0
        #print(self.product_list)
        #for product in self.product_list:
            #print(product)
            #if (self.product[id_count] == 'yes'):
                #print("This product is sold")
        pass

    #generate product information
    def label_product_detail(self, current_page, amount_per_page, product_list):
        page_index = current_page - 1

        if (product_list[0 + (amount_per_page * page_index)] != None):
            self.productLabel1 = product_list[0 + (amount_per_page * page_index)].name
            self.buyingButton1 = str(product_list[0 + (amount_per_page * page_index)].price) + " Baht"
            self.productDescription1 = "   " + product_list[0 + (amount_per_page * page_index)].detail
            self.productAmount1 = "Buy: " + str(product_list[0 + (amount_per_page * page_index)].buy_amount)
            self.productPicture1 = str(product_list[0 + (amount_per_page * page_index)].picture)
            if (product_list[0 + (amount_per_page * page_index)].buy_amount > 0):
                self.productTick1 = "red tick.png"
            else:
                self.productTick1 = ""

        if (product_list[1 + (amount_per_page * page_index)] != None):
            self.productLabel2 = product_list[1 + (amount_per_page * page_index)].name
            self.buyingButton2 = str(product_list[1 + (amount_per_page * page_index)].price) + " Baht"
            self.productDescription2 = "   " + product_list[1 + (amount_per_page * page_index)].detail
            self.productAmount2 = "Buy: " + str(product_list[1 + (amount_per_page * page_index)].buy_amount)
            self.productPicture2 = str(product_list[1 + (amount_per_page * page_index)].picture)
            if (product_list[1 + (amount_per_page * page_index)].buy_amount > 0):
                self.productTick2 = "red tick.png"
            else:
                self.productTick2 = ""

        if (product_list[2 + (amount_per_page * page_index)] != None):
            self.productLabel3 = product_list[2 + (amount_per_page * page_index)].name
            self.buyingButton3 = str(product_list[2 + (amount_per_page * page_index)].price) + " Baht"
            self.productDescription3 = "   " + product_list[2 + (amount_per_page * page_index)].detail
            self.productAmount3 = "Buy: " + str(product_list[2 + (amount_per_page * page_index)].buy_amount)
            self.productPicture3 = str(product_list[2 + (amount_per_page * page_index)].picture)
            if (product_list[2 + (amount_per_page * page_index)].buy_amount > 0):
                self.productTick3 = "red tick.png"
            else:
                self.productTick3 = ""

        if (product_list[3 + (amount_per_page * page_index)] != None):
            self.productLabel4 = product_list[3 + (amount_per_page * page_index)].name
            self.buyingButton4 = str(product_list[3 + (amount_per_page * page_index)].price) + " Baht"
            self.productDescription4 = "   " + product_list[3 + (amount_per_page * page_index)].detail
            self.productAmount4 = "Buy: " + str(product_list[3 + (amount_per_page * page_index)].buy_amount)
            self.productPicture4 = str(product_list[3 + (amount_per_page * page_index)].picture)
            if (product_list[3 + (amount_per_page * page_index)].buy_amount > 0):
                self.productTick4 = "red tick.png"
            else:
                self.productTick4 = ""

        if (product_list[4 + (amount_per_page * page_index)] != None):
            self.productLabel5 = product_list[4 + (amount_per_page * page_index)].name
            self.buyingButton5 = str(product_list[4 + (amount_per_page * page_index)].price) + " Baht"
            self.productDescription5 = "   " + product_list[4 + (amount_per_page * page_index)].detail
            self.productAmount5 = "Buy: " + str(product_list[4 + (amount_per_page * page_index)].buy_amount)
            self.productPicture5 = str(product_list[4 + (amount_per_page * page_index)].picture)
            if (product_list[4 + (amount_per_page * page_index)].buy_amount > 0):
                self.productTick5 = "red tick.png"
            else:
                self.productTick5 = ""


    #clear any product show
    def clear_label_product_detail(self):
        lebel_cleared = ""
        buying_button_cleaed = ""
        description_cleared = ""
        product_amount_cleared = ""
        product_picture_cleared = ""

        self.productLabel1 = lebel_cleared
        self.productLabel2 = lebel_cleared
        self.productLabel3 = lebel_cleared
        self.productLabel4 = lebel_cleared
        self.productLabel5 = lebel_cleared

        self.buyingButton1 = buying_button_cleaed
        self.buyingButton2 = buying_button_cleaed
        self.buyingButton3 = buying_button_cleaed
        self.buyingButton4 = buying_button_cleaed
        self.buyingButton5 = buying_button_cleaed

        self.productDescription1 = description_cleared
        self.productDescription2 = description_cleared
        self.productDescription3 = description_cleared
        self.productDescription4 = description_cleared
        self.productDescription5 = description_cleared

        self.productAmount1 = product_amount_cleared
        self.productAmount2 = product_amount_cleared
        self.productAmount3 = product_amount_cleared
        self.productAmount4 = product_amount_cleared
        self.productAmount5 = product_amount_cleared

        self.productPicture1 = product_picture_cleared
        self.productPicture2 = product_picture_cleared
        self.productPicture3 = product_picture_cleared
        self.productPicture4 = product_picture_cleared
        self.productPicture5 = product_picture_cleared

        self.productTick1 = product_picture_cleared
        self.productTick2 = product_picture_cleared
        self.productTick3 = product_picture_cleared
        self.productTick4 = product_picture_cleared
        self.productTick5 = product_picture_cleared

    def set_product_sold_out(self):
        pass

#class of each product info
class ProductClass():
    name = None
    price = None
    detail = None
    status = None

    buy_amount = 0
    picture = 0

    def __init__(self, name, price, detail, picture, status):
        self.name = name
        self.price = price
        self.detail = detail

        self.picture = picture
        self.status = status




