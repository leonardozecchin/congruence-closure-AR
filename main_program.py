import time
import sys
sys.path.insert(0, './code')
from cca import start_program

filename = "/home/leonardo/Scrivania/Uni/automatedReasoning/congruence-closure-AR/input/input.txt"
fin = open(filename, "r")
fout = open("output/output.txt", "w")
lines = fin.readlines()

for i,line in enumerate(lines):

    print("\n*********************")
    print(f"Formula {i+1}: {line.strip()}")
    start_time = time.time()
    satisfiability = start_program(line.strip())
    if satisfiability:
        print(f"{line.strip()} --> SATISFIABLE. Time: {time.time()-start_time}", file=fout)
    else:
        print(f"{line.strip()} --> UNSATISFIABLE. Time: {time.time() - start_time}", file=fout)
fout.close()
    
