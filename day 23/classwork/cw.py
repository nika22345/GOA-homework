v = 'აეიოუ'
s = input("შეიყვანე ტექსტი: ")
while len(s) == 0 or s[0] in v or s[-1] in v:
    s = input("თავიდან სცადე: ")
print("მართებული ინფუთი:", s)