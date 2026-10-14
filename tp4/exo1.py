class Product : 
    code = 1234
    name = "Simon"
    priceET = 12
    tax = 0.2
    def get_price_it(self):
        return self.priceET + (self.tax * self.priceET)
print(Product().get_price_it())

import random
n=int(input("Saisissez le nombre de produits que vous achetez : "))
for i in range(n):
    product = Product()
    product.code = random.randint(1000,9999)
    product.name = input("Saisissez le nom du produit : ")
    product.priceET = float(input("Saisissez le prix du produit : "))
    print(f"{product.code} - {product.name} - {product.get_price_it()}€")