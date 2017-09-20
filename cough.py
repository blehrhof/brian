def main():
    cough(3)
    sneeze(3)

def cough(n):
    say("cough",n)

def sneeze(n):
    say("achoo",n)

def say(word,n):
    for i in range(n):
        print(word)

main()

for i in range(65, 65 + 26):
    print("{} is {}".format(chr(i), i))
