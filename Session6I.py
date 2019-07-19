def applyPromoCode(promocode, amount):
    if amount >= 1000 and promocode == "FLAT50":
        return amount * 50 // 100
    elif 500 < amount < 1000 and promocode == "FLAT30":
        return amount * 30 // 100
    else:
        print("Not Valid !!")

total = int(input("Enter Amount:"))
print("Please pay: \u20b9",total-applyPromoCode("FLAT50", total))