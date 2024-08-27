import bcrypt
import time
import random
import string
import matplotlib.pyplot as plt

def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def analyze(psw, cf):
    start_time = time.time()
    hashed_password = bcrypt.hashpw(psw.encode(), bcrypt.gensalt(cf))
    hash_time = time.time() - start_time
    start_time = time.time()
    result = bcrypt.checkpw(psw.encode(), hashed_password)
    verify_time = time.time() - start_time
    return hash_time, verify_time

hash_times = []
verify_times = []
cf = []
for j in range(8, 15):
    base = 8
    cf.append(j)
    total_hash_time = 0
    total_verify_time = 0
    for i in range(13):
        password = generate_random_string(base + i)
        ht, vt = analyze(password, j)
        total_hash_time += ht
        total_verify_time += vt
        base += 1
    hash_times.append(total_hash_time / 13.0)
    verify_times.append(total_verify_time / 13.0)

plt.figure(figsize=(10, 5))
plt.plot(cf, hash_times, label='Average Hashing Time', marker='o')
plt.plot(cf, verify_times, label='Average Verification Time', marker='x')
plt.xlabel('Cost Factor')
plt.ylabel('Time (seconds)')
plt.title('Cost Factor vs Average Hashing & Verification Times')
plt.legend()
plt.grid(True)
plt.show()
