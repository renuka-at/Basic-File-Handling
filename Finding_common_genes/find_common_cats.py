"""
This program counts how many genes are in each category (1.1, 1.2, etc.) based on data from the chr21_genes.txt file.
This program prints the results so that categories are arranged in ascending order to an output file
"""
import argparse
from assignment4.io_utilis import get_filehandle


def main():
    """Business Logic"""

    args = get_args()
    inp_file1 = args.infile1
    inp_file2 = args.infile2
    fh_in1 = get_filehandle(inp_file1, "r")  # opening the file in read mode infile 1
    final_dict1 = dict_inp(fh_in1, index=2)  # converting to a dict
    fh_in2 = get_filehandle(inp_file2, "r")  # opening the file in read mode infile 1
    final_dict2 = dict_inp(fh_in2, index=1)

    o_file = 'OUTPUT/categories.txt'
    fh_out = get_filehandle(o_file, "w")
    # counting gene categories
    counts = dict()
    to_count = list(final_dict1.values())
    for value in to_count:
        counts[value] = counts.get(value, 0) + 1
    fh_out.write(f"\nCategory\tOccurrence\tDescription\n")
    for key, val in final_dict2.items():
        for cat, occ in counts.items():
            if key == cat:
                fh_out.write(f"{cat}\t\t{occ}\t\t{val}\n")

    fh_out.close()
    fh_in1.close()
    fh_in2.close()


def get_args():
    """
    Command line options using argparse
    :return: Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Combine on gene name and count the category occurrence')
    parser.add_argument('-i1', '--infile1', metavar='INFILE1', type=str,
                        help='Path to the gene description file to open', default='/chr21_genes.txt')
    parser.add_argument('-i2', '--infile2', metavar='INFILE2', type=str, help='Path to the gene category to open',
                        default='/chr21_genes_categories.txt')
    return parser.parse_args()


def dict_inp(infile, index):
    """
    Takes an input file and converts it into a list.
    The index[0] and index[index] of the list are updated as key value pairs in a dictionary
    :param infile: The input file provided from the command line
    :param index: the value index of for dictionary creation
    :return: a dictionary
    """
    dict_ = {}

    for line in infile:
        in_line = line.split('\t')
        in_list = [element.rstrip() for element in in_line]
        dict_.update({in_list[0]: in_list[index]})
    return dict_


if __name__ == '__main__':
    main()
