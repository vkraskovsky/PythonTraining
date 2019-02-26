# Задача 2
# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу.

student_results_file = '/home/slava/dev/Temp/H08_Task02/student_results.txt'
with open(student_results_file, 'r') as student_results:
    results = student_results.readlines()
    print(results)
    rate_count = 0
    rate_sum = 0
    for i in results:
        j = i.rstrip().split()
        rate_sum += int(j[2])
        rate_count += 1
        if j[2] in ('0', '1', '2', '3'):
            print('Low Performer:', *j)
    print('Average rate', round(rate_sum/rate_count, 2))
