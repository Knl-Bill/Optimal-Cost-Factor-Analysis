import bcrypt
import time
import string
import random
import matplotlib.pyplot as plt

characters = string.ascii_letters + string.digits
password = ''.join(random.choice(characters) for _ in range(10))
cost_factor = 11
cf = list()
Time = list()
for cost_factor in range(10,15):
    start_time = time.time()
    bcrypt.hashpw(password.encode(), bcrypt.gensalt(cost_factor))
    cf.append(cost_factor)
    hash_time = time.time() - start_time
    password_length = 10
    character_set_size = 62  # assuming a-z, A-Z, 0-9
    total_passwords = character_set_size ** password_length
    brute_force_time = hash_time * total_passwords
    brute_force_time_years = brute_force_time / (60 * 60 * 24 * 365)
    Time.append(brute_force_time_years)

plt.figure(figsize=(10, 5))
plt.plot(cf, Time, marker='o', color='b', linestyle='-', label='Brute Force Time (years)')
plt.xlabel('Cost Factor')
plt.ylabel('Brute Force Time (years)')
plt.title('Cost Factor vs Brute Force Time')
plt.grid(True)
plt.legend()
plt.show()
 