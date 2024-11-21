def format_list(items):
    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return items[0] + ' and ' + items[1]
    else:
        result = ''
        for i in range(len(items) - 1):
            result += items[i] + ', '
        result += 'and ' + items[-1]
        return result

spam = ['apples', 'bananas', 'tofu', 'cats']
result = format_list(spam)
print(result)  # Output: apples, bananas, tofu, and cats
