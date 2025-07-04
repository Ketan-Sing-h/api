import requests
import pandas as pd

pd.set_option('display.max_columns', None)

url = 'https://dummyjson.com/products/'
response = requests.get(url, verify=False)

data = response.json()
products = data["products"]

for product in products:
    dimensions = product["dimensions"]
    product["width"] = dimensions["width"]
    product["height"] = dimensions["height"]
    product["depth"] = dimensions["depth"]

products_df = pd.DataFrame(data['products'], columns=["id", "title", "category", "price", "discountPercentage", "rating", "stock", "brand", "width", "height", "depth"])
# print(products_df)

reviews = []
for product in products:
    for review in product["reviews"]:
        reviews.append({
            "rating": review["rating"],
            "comment": review["comment"],
            "date": review["date"],
            "reviewerName": review["reviewerName"],
            "reviewerEmail": review["reviewerEmail"]
        })
reviews_df = pd.DataFrame(reviews, columns = ["rating", "comment", "date", "reviewerName", "reviewerEmail"])         

reviews_df["date"] = reviews_df["date"].apply(pd.to_datetime).dt.date
# print(reviews_df)
# reviews_df.info()