import random as rd
otp = rd.randrange(10000)     # Returns a random number between the given range
print("OTP is:",otp)

otp = rd.randrange(2000, 6000, 10)
print("OTP Now is:",otp)

otp = rd.randint(1000, 9000)    # Returns a random number between the given range
print("OTP Lastly is:",otp)

# DOUBT??
print(rd.seed(10))    # Initialize the random number generator