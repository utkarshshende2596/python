try:
    f = open("sample",'r')
    if f.name == ('sample'):
        raise Exception     #manually throw exceptiom
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('sad')
else: #when exception is not thrown
    for line in f:
        print(line,end='')
finally:    # run weather it excecutes successfully or not
    print('asd')