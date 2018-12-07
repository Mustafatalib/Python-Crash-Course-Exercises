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

    


