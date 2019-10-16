phone  = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
var = input("Phone: ")
output = ""
for ch in var:
    output += phone.get(ch, ch) + " "
print(output)