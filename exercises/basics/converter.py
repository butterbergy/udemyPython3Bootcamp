# Example input & output flow to convert kms to miles
print("How many kilometers did you run today?")
kms = float(input())
miles =  round(kms / 1.609, 2)
print(f"OK, you ran {miles} miles today!")
