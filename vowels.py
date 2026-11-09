# soz ve cumle daxil et5mek
text = input("Bir soz ve ya cumle daxil edin: ")

# saitler
vowels = "a, e, ə, ı, i, o, ö, u, ü"
count = 0
for letter in text:
    if letter in vowels:
        count = count + 1

# netice
print(f"count of vowels: {count}")