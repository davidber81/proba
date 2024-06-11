

# Использование %:
team1_num = 5
print("В команде Мастера кода участников: %s!" %team1_num)
#
team1_num = 5
team2_num = 6
print("Итого сегодня в командах участников: %s и %s!" %(team1_num, team2_num))

# Использование format():
score_2 = 42
print("Команда Волшебники данных решила задач: {}!".format(score_2))
#
team1_time = 18015.2
print("Волшебники данных решили задачи за {} с !".format(team1_time))

# Использование f-строк:
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')
#

team1_num = 'Мастера кода!'
team2_num = 'Волшебники Данных!'
score1 = int(input())
score2 = int(input())
team1_time = float(input())
team2_time = float(input())
if score_1 > score_2 and team1_time > team2_time:
    print(f'Результат битвы: победа команды {team1_num}')
elif score_1 < score_2 and team1_time < team2_time:
    print(f'Результат битвы: победа команды {team2_num}')
else:
    print('Ничья!')
#
tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')
