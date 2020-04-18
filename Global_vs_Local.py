spam="Global Spam"

print("Outside Spam")

def test_func(test):
    global spam
    print(test)
    spam="Local Spam".capitalize
    return spam

testvariable =test_func(spam)
print(f"Value of test variable {testvariable}")