guests = ['Uncle', 'Aunty', 'Sister in law']
print("You're cordially invited " + guests[0] + ".")
print("You're cordially invited " + guests[1] + ".")
print("You're cordially invited " + guests[2] + ".")
print("So I got a new big table for our dinner.")
guests.insert(0, 'frnd1')
guests.insert(2, 'frnd2')
guests.append('bestfrnd')
for i in guests:
    print(i.title() + " You're cordially invited.")
print("The dinner table is delayed so I can only invite 2 people.")
rem1 = guests.pop(0)
print(rem1 + " Sorry you cant come.")
rem2 = guests.pop(0)
print(rem2 + " Sorry you cant come.")
rem3 = guests.pop(0)
print(rem3 + " Sorry you cant come.")
print(guests)
rem4 = guests.pop(0)
print(rem4 + " Sorry you cant come.")
print(guests[0] + " Congrats. Here you come. ")
print(guests[1] + " Congrats. Here you come. ")
print(guests)
del guests[1]
del guests[0]
print(guests)

 