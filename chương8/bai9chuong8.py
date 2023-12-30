import time

def count_down(n):
    while n > 0:
        print(f"Countdown: {n} seconds")
        time.sleep(1)  # Dừng 1 giây
        n -= 1
    print("Time's up!")

# Nhập số nguyên n bạn muốn đếm ngược
n = int(input("Nhập một số nguyên n để đếm ngược: "))

count_down(n)