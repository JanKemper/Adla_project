import adla

while True:
    text = input('adla > ')
    result, error = adla.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)