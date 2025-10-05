# Program to display ASCII values of alphabets

# Uppercase letters
print("Uppercase Letters and their ASCII values:")
for ch in range(ord('A'), ord('Z') + 1):
    print(f"{chr(ch)} : {ch}")

print("\nLowercase Letters and their ASCII values:")
# Lowercase letters
for ch in range(ord('a'), ord('z') + 1):
    print(f"{chr(ch)} : {ch}")
