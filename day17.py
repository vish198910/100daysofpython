class User:
    def __init__(self,user_id):
        self.id = user_id


user1 = User("Vishnu")
user1._id = "801"
user1.username = "angela"

print(user1.id)
print(user1.__dict__)