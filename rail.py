def encryption(text, key):
    encry_dic = []
    index = 0
    direction = True
    for i in range(len(text)):
        
        if len(encry_dic) < index+1:
            encry_dic.append("")

        encry_dic[index] += text[i]

        if index == 0:
            direction = True
        elif index == key - 1:
            direction = False

        if direction:
            index += 1
        else:
            index -= 1

    result = ""
    for i in range(3):
        result += encry_dic[i]
    
    print(result)

# def decryption(text, key):
def decrypt_rail_fence(ciphertext, num_rails):
    rail_lengths = [0 for i in range(num_rails)]
    rail_index = 0
    direction = 1

    # Calculate the length of each rail
    for i in range(len(ciphertext)):
        rail_lengths[rail_index] += 1

        if rail_index == num_rails - 1:
            direction = -1
        elif rail_index == 0:
            direction = 1

        rail_index += direction

    # Create a nested list to represent the rails and populate it with the ciphertext
    rails = [[] for i in range(num_rails)]
    rail_index = 0
    for i in range(len(ciphertext)):
        rails[rail_index].append(ciphertext[i])

        if len(rails[rail_index]) == rail_lengths[rail_index]:
            rail_index += 1

    # Read off the plaintext from the rails
    plaintext = ''
    rail_index = 0
    direction = 1

    for i in range(len(ciphertext)):
        plaintext += rails[rail_index].pop(0)

        if rail_index == num_rails - 1:
            direction = -1
        elif rail_index == 0:
            direction = 1

        rail_index += direction

    print(plaintext)
    return plaintext

encryption("GeeksforGeeks", 3)
decrypt_rail_fence("GsGsekfrekeoe", 3)
