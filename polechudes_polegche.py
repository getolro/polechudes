print("Здравствуйте, если вы прочитали описание то вы уже понимаете зачем вы тут, а если вы не поняли это не мои проблемы, закройте приложение и делайте что хотите,а я работу выполнил")
print("для начала игры выберите слово от 1 до 30 включительно")
listword = ["информатика", "водогрязеторфопарафинолечение", "рыбка", "итерация", "близнецы", "календарь", "любовь", "фортнайт", "лимон", "кратность", "инициализация", "аутентификация", "жизнь", "лампа", "пистолет", "рисунок", "гиперболический", "параболоид", "стакан", "лошадь", "риск", "вайб", "блокнот", "сикуляризация", "звук", "пуля", "козерог", "спарта"]
print("вводить буквы по одной с маленького регистра, если хотите ввести все слово, то можно сыграть во все или ничего, отгадываете то честь и слава, не отгадываете унижение и грусть")
print("если хотите сыграть по-крупному введите 'храбрость', даже если вы проиграете то будете запомнены как храбрецы")
print("сдаваться нельзя, я верю в тебя, ты сильный, а если не получилось отгадать слово то пробуй еще раз и еще раз")
word = listword[int(input()) - 1]
lettersword = list()
for i in range(len(word)):
    lettersword.append(word[i])
spaseword = list()
for i in range(len(lettersword)):
    spaseword.append("_ ")
schet = len(word) + 5
setletter = []
while 1:
    if schet != 0:
        letter = input()
        if letter not in word or letter in setletter:
            schet -= 1
        if len(letter) == 1 and letter != "храбрость":
            for i in range(len(lettersword)):
                if letter == lettersword[i] and letter not in setletter:
                    spaseword[i] = letter
                print(spaseword[i], end=" ")
            if "_ " in spaseword:
                print(f"количество попыток {schet}, введите букву")
            else:
                print(f"победа!!!!!, молодец попыток осталось {schet}")
                break
        elif len(letter) != 1 and letter != "храбрость":
            print("следуйте правилам")
        elif letter == "храбрость":
            print("введите полностью слово")
            if "".join(lettersword) == input():
                print("ты легенда!!!!!!!!!!!!!ты выиграл!!!!!!!!!!")
        setletter.append(letter)
        if schet == 0:
            print("ты проиграл, не отчаивайся попробуй еще раз")
            break
