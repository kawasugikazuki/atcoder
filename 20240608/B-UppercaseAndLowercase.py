s=input()
small=0
large=0
for i in range(len(s)):
  if s[i].isupper():
    large+=1
  else:
    small+=1

if large>small:
  s=s.upper()
else:
  s=s.lower()

print(s)