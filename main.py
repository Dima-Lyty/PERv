import random
def greet():
    greetings = ["Привіт!","Добрий день!","Привіт!"]
     print(random.choice (greetings))

def respond(user_input):
    if"Як справи"in user_input.lower():
       responses = ["У меня все добре!","У меня ): 89 все добре, дякую!", "Чудово!"]
     print(random.choice(responses))
    elif"погoдa"in user_input.lower():
       responses=["Сьогодні сонячно і тепло.","Очікуеттся дощова погода.", "Температура 25 градусов."]
     print(random.choice(responses))
    else:
     print("Пробачте я не розумію вас")

greet()
while True:
    user_input = input("Ваше питання")
    respond(user_input)
