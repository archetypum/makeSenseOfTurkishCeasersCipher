turkish = []
for i in range(97,123):
  if(chr(i) == 'c'):
    turkish.append(chr(i))
    turkish.append('ç')
    continue
  if(chr(i) == 'g'):
    turkish.append(chr(i))
    turkish.append('ğ')
    continue
  if(chr(i) == 'i'):
    turkish.append(chr(i))
    turkish.append('ı')
    continue
  if(chr(i) == 'o'):
    turkish.append(chr(i))
    turkish.append('ö')
    continue
  if(chr(i) == 'q'):
    continue
  if(chr(i) == 's'):
    turkish.append(chr(i))
    turkish.append('ş')
    continue
  if(chr(i) == 'u'):
    turkish.append(chr(i))
    turkish.append('ü')
    continue
  if(chr(i) == 'w'):
    continue
  if(chr(i) == 'x'):
    continue
  else:
    turkish.append(chr(i))
print(turkish)
print(len(turkish))


def encrypt(string, shift):
 
  cipher = ''
  for chr in string: 
    if chr == ' ':
      cipher = cipher + chr
    else:
      cipher = cipher + turkish[(turkish.index(chr) + shift) % 29]
  
  return cipher

 
text = input("enter string: ")

print("original string: ", text)
for i in range(26):
  print("after encryption: ", encrypt(text, i))