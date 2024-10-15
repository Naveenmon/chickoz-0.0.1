import pymongo
from bson import ObjectId
from datetime import date, timedelta
import os
import shutil
import torch.nn as nn


# date and time
def dates():
    t = date.today()
    t = t.strftime("%d, %b %Y")
    return t


#User details
from pymongo import MongoClient


class userdetails:
    __user = {}

    def __init__(self, name, email, mobnum, password, role):
        self.__user['username'] = name
        self.__user['email'] = email
        self.__user['mobilenumber'] = mobnum
        self.__user['password'] = password
        self.__user['role'] = role
        self.__user['cart'] = []
        self.__user['address'] = {}

    def getuser(self):
        return self.__user


#Orders
class Orders:
    __order = {}

    def __init__(self, id, name, details, cart, order_date, status, total):
        self.__order['userid'] = id
        self.__order['username'] = name

    __order = {}

    def __init__(self, userid, name, details, cart, order_date, status, total):
        self.__order['userid'] = userid
        self.__order['username'] = name
        self.__order['details'] = details
        self.__order['cart'] = cart
        self.__order['order_date'] = order_date
        self.__order['status'] = status
        self.__order['total'] = total


'''class menu:
    def getorder(self):
        return self.__order'''


#Menu
class menu:
    __food = {}

    def __init__(self, foodname, category, price, stock, image):
        self.__food['foodname'] = foodname
        self.__food['category'] = category
        self.__food['price'] = price
        self.__food['stock'] = stock
        self.__food['image'] = image

    def getmenu(self):
        return self.__food


class model():
    __mongo = MongoClient('mongodb://localhost:27017')
    _db = "chickoz"

    __mongo = pymongo.MongoClient('mongodb://localhost:27017')
    __mongo = __mongo["chickoz"]

    #fetch
    def fetch(r):
        l = []
        for i in r:
            l.append(i)
        return l

    #register

    def register(self,username, email, mobnum, password, role):
        res = self.__mongo['user'].find({'email': email, 'password': password})
        result = self.fetch(res)
        if len(result)<=0:
            s = userdetails(username, email, mobnum, password, role)
            self.__mongo[self._db]['user'].insert_one(s.getuser())
            del s
            return True
        else:
            return False

    #login
    def login(email, password):
        res = model.__mongo[model._db]['user'].find({'email': email, 'password': password})
        result = model.fetch(res)

    def login(self, email, password):
        res = self.__mongo['user'].find({'email': email, 'password': password})
        result = self.fetch(res)
        return result

    #Cart Check
    def cartcheck(self, session):
        res = self.__mongo['user'].find({"_id": ObjectId(session['id'])}, {"_id": 0, "cart": 1})
        r = self.fetch(res)
        r = r[0]
        return r

    #Add cart
    def addcart(self, id, session, qnt):
        res = self.__mongo['menu'].find({"_id": ObjectId(id)}, {"_id": 0, "product_name": 1, "img": 1, "price": 1})
        r = self.fetch(res)
        r = r[0]
        one = {"product_id": ObjectId(id), "product_name": r['product_name'], "qnt": qnt, "price": r['price'],
               "img": r['img']}
        self.__mongo['user'].update_one({"_id": ObjectId(session.get("id"))}, {"$push": {"cart": one}})

    #Remove cart
    def removecart(self, id, session):
        r = self.cartcheck(session)
        r = r['cart']
        self.__mongo['user'].update_one({"_id": ObjectId(session.get("id"))},
                                         {"$pull": {"cart": {"product_id": ObjectId(id)}}})

    #Add category
    def addcategory(self, name):
        self.__mongo.create_collection(name)
        os.mkdir("./static/" + name)

    # remove category
    def removecategory(self, name):
        self.__mongo.drop_collection(name)
        shutil.rmtree("./static/" + name)

    def menu(self):
        res = self.__mongo['menu'].find({})
        result = self.fetch(res)
        return result


class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        # no activation and no softmax at the end
        return out



