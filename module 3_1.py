
calls = 0

def count_calls():# подсчитывает вызовы остальных фвункций
    global calls
    calls +=1

def string_info(string):
    count_calls()
    a = (len(string))
    b = string.upper()
    c = string.lower()
    return a,b,c


def is_contains(string,list_to_search):
    count_calls()
    for i in list_to_search:
        if string in i:
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Capybara', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)










#print string_info(string,list_to_search)
#print(calls)
#a = (len('calls'))
#b = 'calls'.upper()
#c = 'calls'.lower()
#print(string_info())
#print(a,b,c)

#def is_contains():




#a = 5
#b = 6

#def printer():
    #a = 'str'
    #b = 'str2'
    #c = 15
    #d = 20
    #print(c, d, 'local')
    #print(a, b, 'global')
#print(a, b)
#printer()
#print(a, b)


