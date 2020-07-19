from modules import coderun

runclass = coderun.coderun()

print("welcome use getstart0.0.1.020")

while True:
    inputs = input(">>>")
    if inputs == "exitmain;":
        break
    runclass.runcode(inputs)

print("exit...")