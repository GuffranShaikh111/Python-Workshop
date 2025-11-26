from unicodedata import category


class Application:
    def __init__(self,application_name,category,company,app_size,no_of_users,ratings):
        self.application_name=application_name
        self.category=category
        self.app_size=app_size
        self.company=company
        self.no_of_users=no_of_users
        self.ratings=ratings

    def signup(self):
        print(f"SignUp Done,{self.application_name}")
    def login(self):
        print(f"Welcome to Application,{self.application_name}")
    def logout(self):
        print(f"Thank you for using {self.application_name}")
    def info(self):
        print(f"Name:{self.application_name}\n"
              f"category: {self.category}\n"
              f"Company:{self.company}\n"
              f"app size: {self.app_size}\n"
              f"Number of users:{self.no_of_users}\n"
              f"Ratings:{self.ratings}\n")

app1=Application("Instagram","Social Media","meta","42.47",10000,4.4)
app2=Application("Facebook","Social Media","meta","44.47",8000,4.2)
app3=Application("Snapchat","Social Media","meta","41.47",9000,4.3)
app1.info()