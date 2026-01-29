users = {}        # usernames will go here
posts = []        # every post you create gets added here
post_id = 0       # each post gets its own number

def main_menu():
    print ("MAIN MENU:")
    print ("1. Create a user")
    print ("2. Write a post")
    print ("3. View the feed")
    print ("4. Like a post")
    print ("5. Exit")

    choice = input("Choose an option (numbers only)")
    return choice
def make_user():
    username = input("username: ")
    bio = input("bio: ")
    if username in users:
        print("That username already exists.")
        return
    users[username] = {"bio": bio, "followers": 0}
    print("User created:", username)
def make_post():
    global post_id
    user = input ("What user is posting this: ")
    if user not in users:
        print("Please input an active user: ")
        return
    text = input("Type your post: ")
    post_id = post_id + 1
    posts.append ({
    "id": post_id,
    "user": user,
    "text": text,
    "likes": 0
})
    print("Post created")
def look_feed():
    for post in posts:
        print("Post ID:", post["id"])
        print("User:", post["user"])
        print("Text:", post["text"])
        print("Likes:", post["likes"])
def like_post():
    post_id_input = input("Put the post id of the post you want to like: ")
    post_id_input = int(post_id_input)
    for post in posts:
        if post["id"] == post_id_input:
            post["likes"] += 1
            print ("Post liked. Total likes:", post ["likes"])
            return
    print ("Post does not exist")
def exit_twitter():
    print("Bye bye")
while True:
    choice = main_menu()

    if choice == "1":
        make_user()
    elif choice == "2":
        make_post()
    elif choice == "3":
        look_feed()
    elif choice == "4":
        like_post()
    elif choice == "5":
        exit_twitter()

        break
