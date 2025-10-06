# lst = [1,2,3]
# my_str = "mlops"
# my_int = 155

#print(type(my_str))

# lst.clear()
# print(lst)

# my_str = my_str.capitalize()
# print(my_str)

# a = 'x'
# b = 'y'
# print(a+b)

from oops_proj import chatbook
user1 = chatbook()
print(user1.id)

chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)


#getter and setter
# user1 = chatbook()
# print(user1.get_name())
# user1.set_name("Agent Z")
# print(user1.get_name())


# #function
# lst = [1,2,3]
# a1 = len(lst)
# print(a1)

# #method
# user1 = chatbook()
# user1.sendmsg()
