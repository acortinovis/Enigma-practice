
messages=['hi','how are you','nice to meet you','bye']
sent_messages=[]
def send_messages(messages: list):
    global sent_messages
    while messages:
        message=messages.pop(0)
        print(message)
        sent_messages.append(message)
print('new list:')
send_messages(messages)
print(f'old list: {messages}')

#3. Write a function that accepts a list of items a person wants on a sandwich.
#  The function should have one parameter that collects as many items as the function call provides and it should print a summary of the sandwich that's being ordered.
#  Call the function three times using a different number of arguments each time.

def sand_maker(items: list):
    print('here there are your sandwich items: ')
    for item in items:
        print(item)

sand_maker(items=['cheese'])
sand_maker(items=['cheese,lettuce'])
sand_maker(items=['cheese,lettuce,tomatoes,ham']) 