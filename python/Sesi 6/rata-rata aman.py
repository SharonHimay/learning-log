def rata_rata_aman(data):
    try:
        return sum(data) / len(data)
    except ZeroDivisionError:
        return None

print(rata_rata_aman([]))       # None
print(rata_rata_aman([2, 4]))   # 3.0