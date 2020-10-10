import datetime


def log(key, com):
    d1 = datetime.datetime.now()
    file = open('logs.txt', 'a')
    file.write('{}---{}---{}\n'.format(key, d1.strftime("%d/%m/%Y %H:%M:%S"), com))
    file.close()
