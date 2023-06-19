# Congruence closure Algoritm with DAG
Implementation of the congruence closure algorithm with DAG. Automated Reasoning's project.

## Structure of the Repository
The repository has two main programs: **mainProgram.py** and **theParser.py**.
1. The *mainProgram* program implements the algorithm by reading an input file that contains formulas in normal form, e.g. ***f(a,b)=a and f(f(a,b),b)!=a***
2. The *theParser.py* program implements the algorithm by reading an input file that contains the formulas that need to be brought into DNF form and then brought to normal form, e.g *and(eq(f(a,b),a),dis(f(f(a,b),b),a))* becomes *f(a,b)=a and f(f(a,b),b)!=a*; or *imply(eq(x,g(y,z)),eq(f(x),f(g(y,z))))* becomes and(eq(x,g(y,z)),dis(f(x),f(g(y,z)))) and after ***x=g(y,z) and f(x)!=f(g(y,z))***

Within the ***code*** folder are the codes that are used by the main programs, in particular *cca* is used for the **Congruence Closure Algorithm**, while the other programs were used during implementation.

Inside the ***classes*** folder, you will find two important classes: *dag* and *node*, which are utilized by the algorithm.

In the ***input*** and ***output*** folders there are two types of files:
1. ***input.txt*** and ***output.txt*** : the former contains the formulas in the normal form and in the latter you will find the algorithm's resulting outcomes.
2. ***inputToParser.txt*** and ***outputToParser.txt*** : the former containsFormulas that must be parsed and in the latter you will find the algorithm's resulting outcomes.

## How to run the code
---------------
Use the following terminal commands within the folder: 
> python3 mainProgram.py 

> python3 theParser.py

### *Libraries*
1. queue
2. sys
3. time

They come with Python’s standard utility module, so there is no need to install it externally.

### OBS:
You may need to modify the file paths in certain parts of the programs or adjust the path for importing functions from one program to a different directory.