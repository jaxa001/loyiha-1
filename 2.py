# son = int(input("son kirit "))

# if 100 <= son <= 999:
#     birinchi = son // 100
#     oxirgi = son % 10

#     if birinchi > oxirgi:
#         print(f"Birinchi raqam ({birinchi}) oxirgi raqamdan ({oxirgi}) katta — kamayish")
#     elif birinchi < oxirgi:
#         print(f"Birinchi raqam ({birinchi}) oxirgi raqamdan ({oxirgi}) kichik — kopayish")
#     else:
#         print(f"({birinchi}) — bir xil")
# else:
#     print("xato faqat uch xonali son!")

a = int(input("son kirit "))
b = int(input("2 - son kirit "))
c = int(input("3 - son kirit "))

if a < b and a < c:
    print(f"Eng yaqin shahar {a} km")
elif b < c and b < a:
    print(f"Eng yaqin shahar {b} km")
else:
    print(f"Eng yaqin shahar {c} km")