# ==========================
#   Find Reference Address
# ==========================
# Non Primitive Data Types are also called Reference Data Types

userList = ["Hussain", "Suleman", "Zaryab"]
print(hex(id(userList))) # reference address
print(type(userList))
print(userList)

languages = {"Python", "JavaScript", "Nodejs"}
print(hex(id(languages))) # reference address
print(type(languages))
print(languages)

colors = (255, 255, 255)
print(hex(id(colors))) # reference address
print(type(colors))
print(colors)

student = {"name": "Hussain", "age": 21}
print(hex(id(student))) # reference address
print(type(student))
print(student)