from app import add
import time

while True:
    time.sleep(0.5)
    add.s(1, 2).apply_async()
