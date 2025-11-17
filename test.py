with open('input.txt', 'r', encoding='utf-8') as FILE:
    raw_text = FILE.read()

characters = set('\ ,!?.\n0123456789abcdefghijklmnopqrstuvwxyz')
raw_text = ''.join('none' if char.lower() not in characters else char for char in raw_text)

chars = sorted(set(raw_text))
vocab_size = len(chars)

print(chars )
print(vocab_size)