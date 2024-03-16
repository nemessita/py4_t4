# Static bir password yaradin. Daxil edilen parolun 3 dəfə səhv yazılma şansı olsun və hər səhv 
# yazıldıqda 1 şansınız azaldı mesajı versin. Əgər şanslar bitərsə block olundunuz mesajı verilsin. 
# For-dan istifadə edin

password = "root"
chans = 3

for i in range(3):
    admin = input("password: ") 
    if admin == password:
        print("YOU WIN")
        break
    else:
        chans -= 1
        print("wrong", chans, "times")
        if chans == 0:
            print("YOU LOSE")
            break
        
        