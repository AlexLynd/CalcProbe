# calculator-source
This project is for hacking standard six function calculators for subtle programmability, ability to store variables and so forth.  This project is still in developing stage, and this is a temporary repository.
For now, some of this is irrelevant.
## How it Works
calc_source.py is the main source code, used for calling programs.  It calls them from the programs listed in calc_modules, written as functions.  The program_config text file holds the names of the programs you want on the calculator, from the list of programs defined in calc_modules.
    
## How to Use
Fork this repository, and change calc_modules to have whatever programs you want.  Use config.txt to save be able to call them within calc_source.  