#step 3-4
guests = ["Musk", "Blud", "Goga"]
print("Dear, " + guests[0] + ", welcome back!")
print("Dear, " + guests[1] + ", welcome home!")
print("Dear, " + guests[2] + ", welcome!")

#step 3-5
cant_come = guests.pop()
print(cant_come + " не сможет прийти.")
guests.append("Ваня")
print("Dear, " + guests[0] + ", welcome back!")
print("Dear, " + guests[1] + ", welcome home!")
print("Dear, " + guests[2] + ", welcome!")

#step 3-6
print("Будет больше гостей, список расширяется")
guests.insert(0, "Михаил")
guests.insert(2, "Роман")
guests.append("Кирил")
print("Welcome, " + guests[0] + "!")
print("Welcome, " + guests[1] + "!")
print("Welcome, " + guests[2] + "!")
print("Welcome, " + guests[3] + "!")
print("Welcome, " + guests[4] + "!")
print("Welcome, " + guests[5] + "!")

#step 3-7
print("На обед приглашаются всего 2 гостя.")
print("Приглашение отменено, " + guests.pop())
print("Приглашение отменено, " + guests.pop())
print("Приглашение отменено, " + guests.pop())
print("Приглашение отменено, " + guests.pop())
print("Приглашение остается в силе, " + guests[0])
print("Приглашение остается в силе, " + guests[1])
del guests[0]
del guests[0]
print(guests)