class User:
    def __init__(self, user_id, username):
        print("new user created")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    


user_1 = User("001", "aasi")

# user_1.id = "001"
# user_1.username = "aasi"


user_2 = User("002", "lehmä")


user_2.follow(user_1)

print(f"user_1 followers = {user_1.followers}")
print(f"user_2 following = {user_2.following}")


# user_2.id = "002"
# user_2.username = "lehmä"

