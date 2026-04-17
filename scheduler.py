import time

task = input("Enter task: ")
seconds = int(input("Enter delay in seconds: "))

print(f"\nTask scheduled. Reminder in {seconds} seconds...\n")

time.sleep(seconds)

print(f"Reminder: {task}")
