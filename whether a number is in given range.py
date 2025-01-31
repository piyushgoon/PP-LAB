def in_range(num, start, end):
    return start <= num <= end

num = int(input("Enter a number: "))
start = int(input("Enter range start: "))
end = int(input("Enter range end: "))

print("In range" if in_range(num, start, end) else "Out of range")
