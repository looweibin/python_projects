import random
import string

purpose = input('Do you want to encrypt[E] or decrypt?[D]\n')

letter_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)
shuffled_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)

if purpose.lower() == 'e':
    input_message = list(input('\nPlease input message to be ecrypted.\n'))
    seed = int(input('\nPlease input encrypt seed.\n'))
    random.Random(seed).shuffle(shuffled_list)
    encode_dict = dict(zip(letter_list, shuffled_list))

    encode_list = []
    for i in input_message:
        if i in letter_list:
            encode_list.append(encode_dict[i])
        else:
            encode_list.append(i)

    encrypted_message = ''.join(encode_list)
    print(f'\nThe encrypted message is:\n{encrypted_message}')

else:
    input_message = list(input('\nPlease input message to be decrypted.\n'))
    seed = int(input('\nPlease input dencrypt seed.\n'))
    random.Random(seed).shuffle(shuffled_list)
    decode_dict = dict(zip(shuffled_list, letter_list))

    decode_list = []
    for i in input_message:
        if i in letter_list:
            decode_list.append(decode_dict[i])
        else:
            decode_list.append(i)

    decrypted_message = ''.join(decode_list)
    print(f'\nThe message is:\n{decrypted_message}')
