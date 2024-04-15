# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
from dateutil import parser

dbname = get_database()

user = dbname['User']
print(user)


user_one = {'User ID' : 10007 ,'User Name' :  'hb' ,'User Email' :'hb.gmail.com'  ,'User Age' :7}
result = user.insert_one(user_one) 
print(result) 