import json
from pymongo import MongoClient


class CreateMongoDB:
    def __init__(self,data):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['recipe_database']
        self.collection = self.db['recipes']
        self.data = data

    def insert_data(self):
        self.collection.insert_many(self.data)


    def avg_of_ingredients(self):
        sum= 0
        count = 0
        for i in self.collection.find():
            x=len(i["ingredients"])
            sum+=x
            count+=1
        return f"რეცეპტს საშუალოდ სჭირდება {sum/count} ინგრედიენტი."

    def avg_of_steps(self):
        sum = 0
        count = 0
        for i in self.collection.find():
            x=len(i["steps"])
            sum+=x
            count+=1
        return f"რეცეპტს საშუალოდ აქვს {sum/count} მომზადების ეტაპი."

    def most_portion(self):

        max_portion_doc = self.collection.find_one(sort=[("portion", -1)])

        if max_portion_doc:
            return f"ყველაზე მეტი ულუფა აქვს:, {max_portion_doc['portion']}, URL:  {max_portion_doc['receipt_url']}"
        else:
            return "ასეთი რეცეპტი ვერ მოიძებნა"


    def find_author(self):
        pipeline = [
            {
                "$group": {
                    "_id": "$author",  
                    "count": {"$sum": 1}  
                }
            },
            {
                "$sort": {
                    "count": -1  
                }
            },
            {
                "$limit": 1  
            }
        ]

        
        result = list(self.collection.aggregate(pipeline))

       
        if result:
            most_frequent_author = result[0]['_id']
            author_count = result[0]['count']
            return f"ყველაზე მეტი რეცეპტი განთავსებული აქვს {most_frequent_author}-ს. {author_count} რეცეპტი."
        else:
            return "ავტორი ვერ მოიძებნა."


