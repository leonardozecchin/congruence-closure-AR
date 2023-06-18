from cca import start_program
import time

filename = "/Users/leonardozecchin/uni/automatedReasoning/congruence-closure-AR/input/input.txt"
fin = open(filename, "r")
fout = open("output/output.txt", "w")
lines = fin.readlines()

for line in lines:
    start_time = time.time()
    satisfiability = start_program(line.strip())
    if satisfiability:
        print(f"{line.strip()} --> SATISFIABLE. Time: {time.time()-start_time}", file=fout)
    else:
        print(f"{line.strip()} --> UNSATISFIABLE. Time: {time.time() - start_time}", file=fout)
fout.close()
    
