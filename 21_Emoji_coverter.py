def emoji_converter(message):
    words = message.split(' ')
    emoji = {
        ':)': '😀',
        ':(': '☹️'
    }
    # print(words)
    op = ''
    for w in words:
        op += emoji.get(w, w) + ' '
    return op
message = input(">>")
result=emoji_converter(message)
print(result)