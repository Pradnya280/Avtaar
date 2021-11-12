user_name=input("enter your name::")
print("hi,",user_name,"!")

# random id using uuid1()

import uuid

# Printing random id using uuid1()
print ("The random id using uuid1() is : ",end="")
print (uuid.uuid1())


from datetime import datetime
now=datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
