from email.header import Header
from sqlite3 import ProgrammingError
import owlready2

owl_path_new = r"http://test.org/onto.owl"
onto = owlready2.get_ontology(owl_path_new)

with onto:
    #-------------------
    # экземпляры класса
    # музыка
    class Music(owlready2.Thing):
        pass
    class Title(Music):
        pass
    class Genre(Music):
        pass
    class Executor(Music):
        pass
    class Tutor(Music):
        pass

    class Playlist(Music):
        pass
    class Playlist_by_user(Playlist):
        pass
    class Playlist_recommended(Playlist):
        pass
    class Playlist_recommended_by_algorithm(Playlist_recommended):
        pass
    class Playlist_recommended_by_editor(Playlist_recommended):
        pass


    #подкаст
    class Podcast(owlready2.Thing):
            pass
    class Title_Podcast(Podcast):
        pass
    class Author(Podcast):
        pass
    class Theme(Podcast):
        pass
    class Chart(Podcast):
        pass

    #подписка
    class Subscription(owlready2.Thing):
            pass
    class Duration(Subscription): #продолжительность подписки
            pass

    class Type(Subscription):
            pass
    class Family_Subscription(Type):
            pass
    class Standart_Subscription(Type):
            pass

    #разработчик
    class Developer(owlready2.Thing):
            pass

    #слушатель
    class Listener(owlready2.Thing):
            pass

    #-------------------
    # Свойства
    # выступает в жанре
    class performs_in_the_genre(Executor >> Genre, owlready2.AsymmetricProperty, owlready2.IrreflexiveProperty):
        pass
    # жанр выступления
    class genre_of_performance (Genre >> Executor, owlready2.AsymmetricProperty, owlready2.IrreflexiveProperty):
        pass
    # добавил
    class added (Genre >> Playlist, owlready2.SymmetricProperty): #
        pass
    # исполняет произведение
    class performs_the_work (Executor >> Title , owlready2.AsymmetricProperty, owlready2.IrreflexiveProperty):
        pass

    #слушатель оформляет подписку (причем 1 слушатель может оформить 1 подписку, функциональное св-во)
    class listener_subscribes(owlready2.ObjectProperty,owlready2.FunctionalProperty):
        domain = [Listener]
        range = [Subscription]

    # подписка оформляется слушателем (обратное свойство к "слушатель оформляет подписку ")
    class subscription_is_being_issued(owlready2.ObjectProperty):
        domain = [Subscription]
        range =  [Listener]
        inverse_property = listener_subscribes

    # создает подкаст по теме
    class creates_by_theme (Author>> Theme, owlready2.AsymmetricProperty, owlready2.IrreflexiveProperty):
        pass
    #-------------------
    # свойства данных
    # почта слушателя
    class Listener_mail(owlready2.DataProperty, owlready2.FunctionalProperty):
        domain = [Listener]
        range = [str]

    # идентификатор слушателя в БД сервиса
    class Listener_ID(owlready2.DataProperty, owlready2.FunctionalProperty):
        domain = [Listener]
        range = [int]

    # идентификатор исполнителя в БД сервиса
    class Executor_ID(owlready2.DataProperty, owlready2.FunctionalProperty):
        domain = [Executor]
        range = [int]

    # прибыль исполнителя
    class Executor_profit(owlready2.DataProperty, owlready2.FunctionalProperty):
        domain = [Executor]
        range = [float]

    # прибыль автора подкаста
    class Author_profit(owlready2.DataProperty, owlready2.FunctionalProperty):
        domain = [Author]
        range = [float]



#-------------------
# экземпляры класса
jazz = Genre ("Джаз")
classical_music = Genre ("Классическая музыка")
pop = Genre ("Поп")
rock = Genre ("Рок")
hip_hop = Genre ("Хип-хоп")
electronic_music = Genre ("Электронная музыка")
rap = Genre ("Рэп")
# исполнители музыки
Egor_Krid = Executor("Егор Крид", Executor_ID = 1, Executor_profit = 1000)
Maxim = Executor("Мак$им", Executor_ID = 2, Executor_profit = 2000)
Amy_Winehouse = Executor("Amy Winehouse", Executor_ID = 3, Executor_profit = 3000)
Arctic_Monkeys = Executor("Arctic Monkeys", Executor_ID = 4, Executor_profit = 4000)
Lana_del_Rey = Executor("Lana del Rey", Executor_ID = 5, Executor_profit = 5000)
Ludovico_Einaudi = Executor("Ludovico Einaudi", Executor_ID = 6, Executor_profit = 6000)
Hans_Zimmer = Executor("Hans Zimmer", Executor_ID = 7, Executor_profit = 7000)
Daft_Punk = Executor("Daft Punk", Executor_ID = 8, Executor_profit = 8000)
Eminem = Executor("Eminem", Executor_ID = 9, Executor_profit = 9000)
# авторы подкастов
Mamenko = Author("Маменко", Author_profit = 5000)
Yuzefovich= Author("Юзефович", Author_profit = 7000)
# темы подкастов
Humor = Theme("Юмор")
Science_and_education= Theme("Наука и образование")
# слушатели
Abramov = Listener("Абрамов", Listener_ID = 1, Listener_mail = "abramov2000@mail.ru")
Bychkov = Listener("Бычков", Listener_ID = 2, Listener_mail = "bychkov@mail.ru")
Vasnetsova = Listener("Васнецова", Listener_ID = 3, Listener_mail = "fan_of_Sergey_Lazarev@mail.ru")
Ryan_Goslingova = Listener("Райан-Гослингова", Listener_ID = 4, Listener_mail = "real_ryan_goslings_wife@mail.ru")
# разработчики
Razrabotchikov = Developer("Разработчиков")
Yandexov = Developer("Яндексов")
# плейлисты
Autumn_playlist = Playlist_recommended_by_editor("Осенний плейлист")
Tik_tok_top = Playlist_recommended_by_editor("Тик-ток топ")
# тип подписки
standart_1_month = Subscription("Стандартная подписка на 1 месяц")
family_1_month = Family_Subscription("Семейная подписка на 1 месяц")


Egor_Krid = Executor("Егор Крид", Executor_ID = 1, Executor_profit = 1000)
Maxim = Executor("Мак$им", Executor_ID = 2, Executor_profit = 2000)
Amy_Winehouse = Executor("Amy Winehouse", Executor_ID = 3, Executor_profit = 3000)
Arctic_Monkeys = Executor("Arctic Monkeys", Executor_ID = 4, Executor_profit = 4000)
Lana_del_Rey = Executor("Lana del Rey", Executor_ID = 5, Executor_profit = 5000)
Ludovico_Einaudi = Executor("Ludovico Einaudi", Executor_ID = 6, Executor_profit = 6000)
Hans_Zimmer = Executor("Hans Zimmer", Executor_ID = 7, Executor_profit = 7000)
Daft_Punk = Executor("Daft Punk", Executor_ID = 8, Executor_profit = 8000)
Eminem = Executor("Eminem", Executor_ID = 9, Executor_profit = 9000)

Otpyskay = Title("Отпускаю")
October_song = Title("October_song")
Rap_god = Title ("Rap god")
Fluorescent_Adolescent = Title ("Fluorescent Adolescent")
Dark_Paradise = Title ("Dark_Paradise")
Radio = Title ("Radio")
Experience = Title ("Experience")
STAY = Title ("S.T.A.Y.")
Get_lucky = Title ("Get_lucky")

# жанр выступления
jazz.genre_of_performance = [Amy_Winehouse]
classical_music.genre_of_performance = [Ludovico_Einaudi, Hans_Zimmer]
pop.genre_of_performance = [Egor_Krid, Lana_del_Rey, Maxim]
rock.genre_of_performance = [Arctic_Monkeys, Lana_del_Rey]
electronic_music.genre_of_performance = [Daft_Punk]
rap.genre_of_performance = [Eminem]

# выступает в
Egor_Krid.performs_in_the_genre =[pop, rap]
Maxim.performs_in_the_genre =[pop]
Amy_Winehouse.performs_in_the_genre =[jazz]
Arctic_Monkeys.performs_in_the_genre =[rock]
Lana_del_Rey.performs_in_the_genre =[pop, rock]
Ludovico_Einaudi.performs_in_the_genre =[classical_music]
Hans_Zimmer.performs_in_the_genre =[classical_music]
Daft_Punk.performs_in_the_genre =[electronic_music]
Eminem.performs_in_the_genre =[rap]

# добавил (симметричное)
Razrabotchikov.added = [Autumn_playlist]
Yandexov.added = [Tik_tok_top]

# исполняет
Egor_Krid.performs_the_work = [Otpyskay]
Maxim.performs_the_work = [Otpyskay]
Amy_Winehouse.performs_the_work = [October_song]
Arctic_Monkeys.performs_the_work = [Fluorescent_Adolescent]
Lana_del_Rey.performs_the_work = [Dark_Paradise, Radio]
Ludovico_Einaudi.performs_the_work = [Experience]
Hans_Zimmer.performs_the_work = [STAY]
Daft_Punk.performs_the_work = [Get_lucky]
Eminem.performs_the_work = [Rap_god]

# оформляет
Abramov.listener_subscribes = standart_1_month
Bychkov.listener_subscribes = standart_1_month
Vasnetsova.listener_subscribes =standart_1_month
Ryan_Goslingova.listener_subscribes = family_1_month

# оформляется - обратно к оформляет

# создает по теме
Mamenko.creates_by_theme = [Humor]
Yuzefovich.creates_by_theme = [Science_and_education]

#-------------------
# запросы
# жанр выступления
print("1. Жанр выступления Ханса Циммера:", onto.search(genre_of_performance = Hans_Zimmer))
print("2. Жанр выступления Daft Punk:", onto.search(genre_of_performance = Daft_Punk))
# выступает в
print("3. Кто выступает в жанре поп c прибылью 1000:", onto.search(performs_in_the_genre = pop, Executor_profit = 1000))
print("4. Кто выступает в жанре поп:", onto.search(performs_in_the_genre = pop))
# добавил(симметричное)
print("5. Добавил осенний плейлист:", onto.search(added= Autumn_playlist))
print("6. Тик-ток топ добавил: ", onto.search(added = Tik_tok_top))
# исполняет
print("7. Кто исполняет S.T.A.Y.: ", onto.search(performs_the_work = STAY))
print("8. Кто исполняет Отпускаю: ", onto.search(performs_the_work = Otpyskay))
# оформляет
print("9. Кто оформляет стандартную подписку на месяц: ", onto.search(listener_subscribes = standart_1_month))
print("10. Кто оформляет семейную подписку на месяц: ", onto.search(listener_subscribes = family_1_month))
# оформляется
print("11. Какую подписку оформляет Райан-Гослингова: ", onto.search(subscription_is_being_issued = Ryan_Goslingova))
print("12. Какую подписку оформляет Разработчиков: ", onto.search(subscription_is_being_issued = Bychkov))
# создает по теме
print("13. Кто создает подкасты по теме юмор: ", onto.search(creates_by_theme = Humor))
print("14. Кто создает подкасты по теме наука и образование: ", onto.search(creates_by_theme = Science_and_education))

onto.save(file = "Abrosimova_LR_2.owl")
print("")

print("Список классов онтологии:")
for item in list(onto.classes()):
    print(item)

print("")
print("Список свойств онтологии:")
for item in list(onto.properties()):
    print(item)

print("")
print("Список экземпляров онтологии:")
for item in list(onto.individuals()):
    print(item)

input('Press ENTER to exit')
