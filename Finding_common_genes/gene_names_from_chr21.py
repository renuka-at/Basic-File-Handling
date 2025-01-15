"""
This script asks the user to enter a gene symbol and then prints the description for that gene based
on data from the chr21_genes.txt file.
"""
import argparse

from assignment4.io_utilis import get_filehandle


def main():
    """Business Logic"""
    args = get_args()  # getting cli -args
    inp_file = args.infile
    fh_in = get_filehandle(inp_file, "r")  # opening the file in read mode
    final_dict = dict_inp(fh_in)  # converting input file to dictionary

    flag_gene_name = 0
    while flag_gene_name == 0:
        # gene_name is the key and d_script in the description accessed using the gene name
        gene_name = input("Enter gene name of interest.Type quit to exit:\t")
        if gene_name.lower() == "quit":
            print("Thanks for querying the data")
            flag_gene_name = 1
        elif gene_name in final_dict:
            d_script = final_dict[gene_name]
            print(f"{gene_name} found! Here is the description:\n {d_script}")
        else:
            print("Not a valid gene name")


def dict_inp(infile):
    """
    Takes an input file and converts it into a list.
    The index[0] and index[1] of the list are updated as key value pairs in a dictionary
    :param infile: input file from the command line
    :return: a dictionary
    """
    dict_ = {}

    for line in infile:
        in_line = line.split('\t')
        in_list = [element.rstrip() for element in in_line]
        dict_.update({in_list[0]: in_list[1]})
    return dict_


def get_args():
    """
    Command line options using argparse
    :return: Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Open chr21_genes.txt and ask user for a gene name')
    parser.add_argument('-i', '--infile', type=str, help='Path to the file to open', default='/chr21_genes.txt')
    return parser.parse_args()


if __name__ == '__main__':
    main()
