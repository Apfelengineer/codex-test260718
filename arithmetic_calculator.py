first_number = float(input("1つ目の数を入力してください: "))
second_number = float(input("2つ目の数を入力してください: "))

print(f"加算: {first_number + second_number}")
print(f"減算: {first_number - second_number}")
print(f"乗算: {first_number * second_number}")

if second_number == 0:
    print("除算: 0では割れません")
else:
    print(f"除算: {first_number / second_number}")
