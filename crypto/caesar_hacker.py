import string

msg = 'Zfbi,!tif!xpvme!qspcbcmz!fbu!nfA'
SYMBOLS = string.ascii_uppercase + string.ascii_lowercase + '1234567890' + ' !?.'

for key in range(len(SYMBOLS)):
    translated = ''
    for c in msg:
        if c in SYMBOLS:
            index = SYMBOLS.find(c)
            translatedIndex = index - key
            if translatedIndex < 0:
                translatedIndex += len(SYMBOLS)
            translated += SYMBOLS[translatedIndex]
        else:
            translated += c
    print(f'Klucz #{key}: {translated}')
