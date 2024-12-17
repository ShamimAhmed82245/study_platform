from main_app.models import User
def run():
    password = "123"
    username="rana123"
    first_name="Joual"
    last_name ="Rana" 
    email = "abc@gmail.com"
    role = "student"
    User.objects.create(
        username=username,
        password=password,
        first_name=first_name,
        last_name = last_name,
        email=email,
        role=role
    )
