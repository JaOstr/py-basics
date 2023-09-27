import string

msg = 'This is my secret message.'
#msg = "To jest moja tajna wiadomość."
#msg = 'g2Jwr67Jz2wnJ7nw1nJ0vnq2z2śćM'
#msg = 'Kv?uqwpfu?rncwukdng?gpqwijB'
key = 8
mode = 'encrypt'

SYMBOLS = string.ascii_uppercase + string.ascii_lowercase + '1234567890' + ' !?.'
translated = ''

for c in msg:
    if c in SYMBOLS:
        index = SYMBOLS.find(c)
        if mode == 'encrypt':
            translatedIndex = index + key
        elif mode == 'decrypt':
            translatedIndex = index - key
        
        if translatedIndex >= len(SYMBOLS):
            translatedIndex -= len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex += len(SYMBOLS)
        
        translated += SYMBOLS[translatedIndex]
    else:
        translated += c
    
print(translated)
