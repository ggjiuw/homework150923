
with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as file:
    for line in file.readlines():
        data = line.split(';')
        if data[5] == 'UA': # in order to change the country, instead of UA, enter the country you need, for example US
            print(data[2])
