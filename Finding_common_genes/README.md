**Open file handle in read or write mode : io_utilis.py**
This script provides a function get_filehandle which returns a file handle object for a given file name and mode.

**Usage**
filehandle = get_filehandle(file, mode)

file: a string representing the name of the file to be opened.
mode: a string representing the mode in which to open the file. It should be either "r" for read mode or "w" for write mode.
The function returns a file handle object that can be used to read from or write to the file.

**Exceptions**
If the function is unable to open the file, it will raise an OSError or a ValueError. The error message will be printed to stderr.


**Gene Description Lookup** - **gene_names_from_chr21.py**
This script allows the user to search for a gene by symbol and retrieves its description from the 'chr21_genes.txt' file. The user can interactively enter a gene name of interest and the corresponding description will be displayed.

**Prerequisites**
Python 3
argparse module
'chr21_genes.txt' file

**Installation and Usage**
Navigate to the directory containing the script.
Run the script using the command python gene_description_lookup.py
When prompted, enter the gene symbol of interest. To exit, type "quit".

*Command Line Options*
The following command line options are available:

-i, --infile: path to the input file (default: 'chr21_genes.txt').

**Output**
The script will output the gene description corresponding to the gene name entered by the user.
If the gene name is not found, a message indicating that the name is not valid will be displayed. 
If the user enters 'quit', the script will terminate.

**Gene Category Counter** - **find_common_cats.py**
The program counts how many genes are in each category (1.1, 1.2, etc.) based on data from the chr21_genes.txt file. 
This program prints the results so that categories are arranged in ascending order to an output file.

**Dependencies**
This program requires the following dependencies:
argparse
io_utils module which is included in the assignment4 package.

**Usage**
usage: gene_category_counter.py [-h] [-i1 INFILE1] [-i2 INFILE2]

Combine on gene name and count the category occurrence

To run the program, use the following command:
python3 find_common_cats.py -i1 [gene_description_file] -i2 [gene_category_file]
The program will output a file called categories.txt to the OUTPUT directory with the gene categories and their respective counts arranged in ascending order.

**Input Files**
This program takes in two input files:

*Gene description file* (default: /chr21_genes.txt): 
This file contains the description of each gene, with the gene name in the first column and the description in the second column.

*Gene category file* (default: /chr21_genes_categories.txt): 
This file contains the gene category for each gene, with the gene name in the first column and the category in the second column.

**Output File**
The program outputs a file called categories.txt to the OUTPUT directory.
This file contains the gene categories and their respective counts arranged in ascending order, with the category description included. 
The file has the following format:
Category    Occurrence  Description
[category]  [count]     [description]
...

**Gene Intersection Finder** - **intersection_of_genes.py**
This program finds all gene symbols that appear both in the chr21_genes.txt file and in the HUGO_genes.txt file. 
The gene symbols are printed to a file in alphabetical order.

**Requirements**
Python 3
argparse module

**Usage**
Run the following command in the terminal to execute the program:
python gene_intersection.py [-h] [-i1 INFILE1] [-i2 INFILE2]

**Output**
The program outputs the following information to the terminal:

The number of unique gene names in chr21_genes.txt
The number of unique gene names in HUGO_genes.txt
The number of common gene symbols found
The output file path where the list of common gene symbols is stored
The list of common gene symbols is stored in the OUTPUT/intersection_output.txt file.

**Implementation**
The program reads two input files and converts them into sets. It then calculates the intersection of the two sets 
and writes the common gene symbols into a file. Finally, it prints the number of unique gene names in each file, 
the number of common gene symbols found, and the output file path where the list of common gene symbols is stored.