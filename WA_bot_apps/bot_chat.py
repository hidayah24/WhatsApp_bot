def response(input_pesan):
    message = input_pesan.lower()

    if message == 'nice':
        return 'Very nice'
    elif message == 'hello':
        return 'Hello there'
    else:
        return 'Cool!'