#Использование %
team2_num = 6
print("В команде Мастера кода участников: %s ! " %5)
print("Итого сегодня в командах участников: %s и %s !" %(5, 6))

#Использование format():
score_2 = 42 #количество задач решённых командой 2
print("Команда Волшебники данных решила задач: {} !".format(score_2))
team1_time = 18015.2 #время за которое команда 2 решила задачи
print(" Волшебники данных решили задачи за {} с !".format(team1_time))

#Использование f-строк:
score_1 = 40
print(f"Команды решили {score_1} и {score_2} задач.")
team2_time = 2153.31451
def challenge_result(result):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
        return print(f"Результат битвы: {result}")

tasks_total = 82
time_avg = (team1_time + team2_time)/ 2
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")