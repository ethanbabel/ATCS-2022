from models import *
from database import init_db, db_session
from datetime import datetime

class Twitter:

    def __init__(self):
        self.current_user = None
    

    """
    The menu to print once a user has logged in
    """
    def print_menu(self):
        print("\nPlease select a menu option:")
        print("1. View Feed")
        print("2. View My Tweets")
        print("3. Search by Tag")
        print("4. Search by User")
        print("5. Tweet")
        print("6. Follow")
        print("7. Unfollow")
        print("0. Logout")
    
    """
    Prints the provided list of tweets.
    """
    def print_tweets(self, tweets):
        for tweet in tweets:
            print("==============================")
            print(tweet)
        print("==============================")

    """
    Should be run at the end of the program
    """
    def end(self):
        print("Thanks for visiting!")
        db_session.remove()
    
    """
    Registers a new user. The user
    is guaranteed to be logged in after this function.
    """
    def register_user(self):
        usernames = db_session.query(User.username).all()
        usernames = [r for (r, ) in usernames]
        while True:
            uname = input("What will your twitter handle be?")
            pass1 = input("Enter a password. ")
            pass2 = input("Re-enter your password")
            if not(pass1 == pass2):
                print("Those passwords don't match. Try again.\n")
            elif uname in usernames:
                print("That username is already taken. Try again.\n")
            else:
                print("\nWelcome " + uname + "!")
                self.current_user = User(username=uname, password=pass1)
                db_session.add(self.current_user)
                db_session.commit()
                break


    """
    Logs the user in. The user
    is guaranteed to be logged in after this function.
    """
    def login(self):
        usernames = db_session.query(User.username).all()
        usernames = [r for(r, ) in usernames]
        while True:
            uname = input("Uername: ")
            p = input("Password: ")
            user_password = db_session.query(User.password).where(User.username == uname).first()[0]
            if(uname not in usernames) or (user_password!=p):
                print("Invalid username or password. ")
            else:
                print("\nWelcome " + uname + "!")
                self.current_user = db_session.query(User).where(User.username == uname).first()
                break


    
    def logout(self):
        self.current_user = None
        print("You've been logged out. ")

    """
    Allows the user to login,  
    register, or exit.
    """
    def startup(self):
        print("Please select a menu option: ")
        print("1. Login ")
        print("2. Register User ")
        print("0. Exit ")
        option = int(input(""))

        if option==1:
            self.login()
        elif option ==2:
            self.register_user()
        elif option==0:
            self.end()

    def follow(self):
        acc_to_follow = input("Who would you like to follow?\n")
        alr_following = False
        following = self.current_user.following
        for a in following:
            if acc_to_follow == a.username:
                alr_following = True
        if alr_following:
            print ("You already follow " + acc_to_follow)
        else:
            acc = db_session.query(User).where(User.username == acc_to_follow).first()
            self.current_user.following.append(acc)
            db_session.commit()
            print("You are now following " + acc_to_follow)

    def unfollow(self):
        acc_to_unfollow = input("Who would you like to unfollow?\n")
        alr_following = False
        following = self.current_user.following
        for a in following:
            if acc_to_unfollow == a.username:
                alr_following = True
        if not alr_following:
            print("You don't follow " + acc_to_unfollow)
        else:
            acc = db_session.query(User).where(User.username == acc_to_unfollow).first()
            self.current_user.following.remove(acc)
            db_session.commit()
            print("You no longer follow " + acc_to_unfollow)

    def tweet(self):
        tweet_content = input("Create Tweet: ")
        tags = input("Enter your tags seperated by spaces: ").split()
        existing_tags = db_session.query(Tag.content).all()
        existing_tags = [r for (r, ) in existing_tags]
        tag_objects = []
        for t in tags:
            if t not in existing_tags:
                new_tag = Tag(content = t)
                db_session.add(new_tag)
                db_session.commit()
                tag_objects.append(new_tag)
            else:
                old_tag = db_session.query(Tag).where(Tag.content == t).first()
                tag_objects.append(old_tag)
        new_tweet = Tweet(content= tweet_content, timestamp=datetime.now(), username=self.current_user.username, tags=tag_objects)
        db_session.add(new_tweet)
        db_session.commit()

    
    def view_my_tweets(self):
        my_tweets = db_session.query(Tweet).where(Tweet.username == self.current_user.username).all()
        self.print_tweets(my_tweets)
    
    """
    Prints the 5 most recent tweets of the 
    people the user follows
    """
    def view_feed(self):
        unames = []
        following = self.current_user.following
        for acc in following:
            unames.append(acc.username)
        my_feed = db_session.query(Tweet).filter(Tweet.username.in_(unames)).order_by(Tweet.timestamp.desc()).limit(5).all()
        self.print_tweets(my_feed)


    def search_by_user(self):
        uname = input("Enter the username you want to search by: ")
        unames = db_session.query(User.username).all()
        unames = [r for (r, ) in unames]
        if uname not in unames:
            print("There is no user by that name. ")
        else:
            tweets = db_session.query(Tweet).where(Tweet.username == uname).all()
            self.print_tweets(tweets)

    def search_by_tag(self):
        t = input("Enter the tag you want to search by: ")
        tags = db_session.query(Tag.content).all()
        tags = [r for (r, ) in tags]
        if t not in tags:
            print("There are no tweets with this tag. ")
        else:
            tag_content = db_session.query(Tag).where(Tag.content == t).first()
            tweets = db_session.query(Tweet) .where(Tweet.tags.contains(tag_content)).all()
            self.print_tweets(tweets)

    """
    Allows the user to select from the 
    ATCS Twitter Menu
    """
    def run(self):
        init_db()

        print("Welcome to ATCS Twitter!")
        self.startup()

        run = True
        while run:
            self.print_menu()
            option = int(input(""))

            if option == 1:
                self.view_feed()
            elif option == 2:
                self.view_my_tweets()
            elif option == 3:
                self.search_by_tag()
            elif option == 4:
                self.search_by_user()
            elif option == 5:
                self.tweet()
            elif option == 6:
                self.follow()
            elif option == 7:
                self.unfollow()
            else:
                self.logout()
                run = False
        
        self.end()


