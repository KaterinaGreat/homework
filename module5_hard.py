from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self):
        return self.nickname == self.current_user

    def get_info(self):
        print(f'Имя: {self.nickname}')
        print(f'Пароль: {self.password}')
        print(f'Возраст: {self.age}')

    def hash_password(self, password):
        return hash(password)

class Video:
    # title = (str)
    # duration = (int)ration

    def __init__(self, title=str, duration=int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return print(f"Видео(Название={self.title}, продолжительность={self.duration}, ограничение по возрасту={self.adult_mode})")
class UrTube:
    def __init__(self, current_user=None):
        self.users = []
        self.videos = []
        self.current_user = current_user

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.hash_password == hash(password):
                self.current_user = user
                return

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        for user in self.users:
            if user.nickname == nickname and user.hash_password == hash(password):
                return f"Пользователь {user.nickname} уже существует"
            else:
                self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            is_found = False
            for vi in self.videos:
                if vi.title == video.title:
                    is_found = True
                    break
            if not is_found:
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word_lower = search_word.lower()
        for video in self.videos:
            if search_word_lower in video.title.lower():
                return video.title

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = None
        for vi in self.videos:
            if vi.title == title:
                break
            if not video:
                print("Видео не найдено")
                return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for second in range(video.time_now, video.duration):
            print(f"Секунда: {second + 1}")
            sleep(1)

        video.time_now = 0
        print("Конец видео")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')