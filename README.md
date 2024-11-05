# Optimal Cost Factor Analysis

This repository contains Python code to calculate the optimal cost factor for the bcrypt password hashing algorithm. The cost factor significantly impacts the security and performance of the password hashing process, making it crucial to find the right balance.

## Table of Contents
1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Analysis](#analysis)
   - [Average Hash Time vs. Cost Factor](#1-average-hash-time-vs-cost-factor)
   - [Cost Factor vs. Time to Brute Force the Password](#2-cost-factor-vs-time-to-brute-force-the-password)
4. [Results](#results)
5. [Conclusion](#conclusion)
6. [License](#license)

## Overview

The repository includes scripts that:
1. Calculate the average hash time for various cost factors.
2. Estimate the time required to brute force a password for different cost factors.

These calculations help determine the optimal cost factor that provides a secure yet performant hashing process for production environments.

## Requirements

- Python 3.x
- bcrypt
- time
- random
- string
- matplotlib.pyplot

You can install the required dependencies using:

```bash
pip install bcrypt matplotlib
```

## Analysis

### 1. Cost Factor vs Average Hash and Validation Time for different Passoword Lengths

![Average Hash Time vs. Cost Factor for Varying Password Lengths](./Cost%20Factor%20vs%20Hash%20Times%20for%20different%20lengths%20of%20password.png)

For each password length, ranging from 8 to 13 characters, the hashing and verification times were measured while incrementally increasing the bcrypt cost factor. As shown in Figure 1, both the hashing and verification times increased consistently with the cost factor, reflecting bcrypt's computational design. Notably, the results indicate that password length had a minimal impact on hashing and verification times. This suggests that bcrypt’s performance is largely determined by the cost factor rather than the password length, as bcrypt's work factor (cost) dominates its processing time.

### 2. Average Hash Time vs. Cost Factor

![Average Hash Time vs. Cost Factor](./Avg%20hash%20verify%20vs%20cost%20factor.png)

This graph illustrates the trends in average hash times for various cost factors, ranging from 8 to 14. It highlights how the hash time increases as the cost factor rises, indicating a direct relationship between the cost factor and processing time.

### 3. Cost Factor vs. Time to Brute Force the Password

![Cost Factor vs. Time to Brute Force](./Cost%20Factor%20vs%20Time%20to%20Brute%20Force.png)

This graph shows the relationship between cost factors (ranging from 10 to 14) and the time required to brute force a password, measured in years. As the cost factor increases, the time to brute force a password escalates dramatically, demonstrating the enhanced security provided by higher cost factors.

## Results

According to the system requirements, the Average Hashing Time and Average Verification time was set to 0.2 seconds. Accordingly, the optimal value for the cost factor was found to be 12, which would take around 6 months to brute force the password. The impractical time required to crack the password supports the claim that the considered cost factor is efficient for the given threshold time for hashing and verification.

## Conclusion

By using this repository, you can identify the optimal bcrypt cost factor that provides a strong balance between security and performance for your password hashing needs. The provided graphs and calculations will guide you in making informed decisions when deploying bcrypt in production environments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
