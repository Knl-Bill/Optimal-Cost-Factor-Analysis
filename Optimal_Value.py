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
optimal_cost_factor = None
performance_threshold = 0.2  # Set your acceptable threshold (e.g., 0.2 seconds)

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
    avg_hash_time = total_hash_time / 13.0
    avg_verify_time = total_verify_time / 13.0
    hash_times.append(avg_hash_time)
    verify_times.append(avg_verify_time)
    
    # Check if both times are within the performance threshold
    if avg_hash_time <= performance_threshold and avg_verify_time <= performance_threshold:
        optimal_cost_factor = j

plt.figure(figsize=(10, 5))
plt.plot(cf, hash_times, label='Average Hashing Time', marker='o')
plt.plot(cf, verify_times, label='Average Verification Time', marker='x')
plt.xlabel('Cost Factor')
plt.ylabel('Time (seconds)')
plt.title('Cost Factor vs Average Hashing & Verification Times')
plt.legend()
plt.grid(True)
plt.show()

if optimal_cost_factor:
    print(f"The optimal cost factor is: {optimal_cost_factor}")
else:
    print("No cost factor within the acceptable performance threshold.")
