import unicodedata

a = unicodedata.lookup('LATIN SMALL LETTER A')
print(a)

for chr in ['가', '쀍', 'ㄱ', '1', 'A', 'a', '☆', '김', '석', '근']:
    print(unicodedata.name(chr))