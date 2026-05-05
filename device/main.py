import time
import random

print("Starting IoT intrusion system...")

while True:
    temp = round(random.uniform(18, 30), 1)
    motion = random.choice([True, False])

    print(f"Temp: {temp}°C | Motion: {motion}")

    if motion:
        print("🚨 Motion detected!")

    time.sleep(3)
