# Created by y2mulyana
# Morse data are from Wikipedia

data_morse = {
    'A' : '• –',
    'B' : '– • • •',
    'C' : '– • – •',
    'D' : '– • •',
    'E' : '•',
    'F' : '• • – •',
    'G' : '– – •',
    'H' : '• • • •',
    'I' : '• •',
    'J' : '• – – –',
    'K' : '– • –',
    'L' : '• – • •',
    'M' : '– –',
    'N' : '– •',
    'O' : '– – –',
    'P' : '• – – •',
    'Q' : '– – • –',
    'R' : '• – •',
    'S' : '• • •',
    'T' : '–',
    'U' : '• • –',
    'V' : '• • • –',
    'W' : '• – –',
    'X' : '– • • –',
    'Y' : '– • – –',
    'Z' : '– – • •',
    '1' : '• – – – –',
    '2' : '• • – – –',
    '3' : '• • • – –',
    '4' : '• • • • –',
    '5' : '• • • • •',
    '6' : '– • • • •',
    '7' : '– – • • •',
    '8' : '– – – • •',
    '9' : '– – – – •',
    '0' : '– – – – –',
    '.' : '• – • – • –',
    ',' : '– – • • – –',
    ':' : '– – – • • •',
    '-' : '– • • • • –',
    '/' : '– • • – •',
    ' ' : '/',
    }

# While loop control
def check_repeat():
    repeat = input('\nTry with other text ? (Y/N)')
    if repeat.upper() == 'Y':
        return True
    else:
        return False
        
cont = True
while cont:
    teks = input('Input your text > ').upper()
    
    # Finding unlisted character in database
    not_in_database = []
    for i in teks:
        if i not in data_morse:
            not_in_database.append(i)

    if len(not_in_database) > 0:
        # Display unlisted character in database
        print(f"{', '.join(not_in_database)} characters(s) not found in our database")
        cont = check_repeat()
    else:
        # Convert to Morse
        morse =[]
        for i in teks:
            morse.append(data_morse[i]+'  ')
        print('\n" / " for space or word separator')
        print(f"Enjoy your morse below : \n{''.join(morse)}")
        cont = check_repeat()

