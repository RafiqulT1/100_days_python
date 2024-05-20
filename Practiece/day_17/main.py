class User:
    def __init__(self, user_id, username):
        print("new user begin created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
        
        
        

    
user_1 = User("001", "killeRoo")
user_2 = User("002", "Racoon")


user_1.follow(user_2)

print(f"{user_1.id} = {user_1.following}")
print(f"{user_1.id} = {user_1.followers}")
print(f"{user_2.id} = {user_1.followers}")
print(f"{user_2.id} = {user_1.following}")