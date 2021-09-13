n = int(input())

piece_composer = {}
piece_key = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    piece_composer[piece] = composer
    piece_key[piece] = key

command = input()

while not command == "Stop":
    current_command = command.split("|")
    to_do = current_command[0]
    if to_do == "Add":
        piece = current_command[1]
        composer = current_command[2]
        key = current_command[3]
        if piece in piece_composer:
            print(f"{piece} is already in the collection!")
        else:
            piece_composer[piece] = composer
            piece_key[piece] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif to_do == "Remove":
        piece = current_command[1]
        if piece in piece_composer:
            del piece_composer[piece]
            piece_key.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif to_do == "ChangeKey":
        piece = current_command[1]
        new_key = current_command[2]
        if piece in piece_composer:
            piece_key[piece] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

piece_composer = sorted(piece_composer.items(), key=lambda kvp: (kvp[0], kvp[1]))
for key, value in piece_composer:
    print(f"{key} -> Composer: {value}, Key: {piece_key[key]}")