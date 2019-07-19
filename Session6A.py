def applyPromoCode(promocode, amount):
    if promocode == "FLAT50":
        return amount * 50//100
    elif promocode == "FLAT30":
        return amount * 30//100
    else:
        return amount * 10//100

total = 1000
#discount = applyPromoCode("FLAT30", total)
#print("Please pay: \u20b9",total-discount)

print("Please pay: \u20b9",total-applyPromoCode("FLAT30", total))

print("applyPromoCode is:",applyPromoCode)

# Reference Copy (Abstraction)
fun = applyPromoCode

print("fun is:",fun)

print("Please pay: \u20b9",total-fun("FLAT50", total))

del fun

print("Please Pay: \u20b9",total-fun("FLAT50", total))
print("Please Pay: \u20b9",total-applyPromoCode("FLAT30", total))

# HW: Create a function which applies promoCode on the basis of these conditions:
# 1. FLAT50 promoCode can work only if user has total amount > 1000
# 2. FLAT30 promoCode can work only if user has total amount > 500 and <1000
# 3. We can propose use to apply a promoCode which is more benficial for him/her
# Make sure of various test cases