from app import add
import time

for _ in range(16):
    time.sleep(0.5)
    add.s(1, 2).apply_async()
