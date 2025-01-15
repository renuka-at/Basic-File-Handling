"""
This program finds all gene symbols that appear both in the chr21_genes.txt file and in the HUGO_genes.txt file.
These gene symbols are printed to a file in alphabetical order
"""
import argparse

from assignment4.io_utilis import get_filehandle


def main():
    """Business Logic"""

    args = get_args()  # getting cli -args
    inp_file1 = args.infile1
    inp_file2 = args.infile2
    fh_in1 = get_filehandle(inp_file1, "r")  # opening the file in read mode
    fh_in2 = get_filehandle(inp_file2, "r")
    set_1 = set_in(fh_in1)
    set_2 = set_in(fh_in2)
    intersect, c_val, s1_val, s2_val = all_calc(set_1, set_2)
    # write into the output file
    o_file = 'OUTPUT/intersection_output.txt'
    fh_out = get_filehandle(o_file, "w")
    output = (out_file_sort(intersect))
    # converting list to string and adding a \n after every element
    to_write = '\n'.join(output)
    fh_out.write(to_write)

    # print results
    print(f"\nNumber of unique gene names in {inp_file1}: {s1_val}\n"
          f"Number of unique gene names in {inp_file2}: {s2_val}\n"
          f"Number of common gene symbols found: {c_val}\n"
          f"Output stored in OUTPUT/intersection_output.txt\n")

    fh_out.close()
    fh_in1.close()
    fh_in2.close()


def out_file_sort(intersect_set):
    """
    :param intersect_set: created from the intersection of set1 and set2
    :return: a sorted list in ascending order
    """

    # convert to lists
    intersect_list = list(intersect_set)
    # sorts in alphabetical order
    sorted_list = sorted(intersect_list)
    return sorted_list


def all_calc(set1, set2):
    """
    :param set1: set 1 created from input file 1
    :param set2: set 2 created from input file 2
    :return: length of the intersection of the 2 sets, length of set 1,
             length of set 2
    """

    u_set1 = _remove_dupl(set1)
    u_set2 = _remove_dupl(set2)
    # common gene symbols between two sets
    com = u_set1.intersection(u_set2)
    # number of genes in each
    common, unq_set1, unq_set2 = len(com), len(u_set1), len(u_set2)
    return com, common, unq_set1, unq_set2


def _remove_dupl(inp_set):
    # to remove duplicates
    n_set = set(inp_set)
    return n_set


def set_in(infile):
    """
    The file is read and its headers are seperated and the rest of
    the file is converted to a list and then to a set
    :param infile: input filehandle provided from the command-line
    :return: a set
    """
    new_list = []
    infile.readline()
    for line in infile:
        in_line = line.split('\t')
        in_list = in_line[0].rstrip('\n')
        new_list.append(in_list)
    return set(new_list)


def get_args():
    """
        Command line options using argparse
        :return: Instance of argparse arguments
        """
    parser = argparse.ArgumentParser(description=' Provide two gene list (ignore header line), find intersection')
    parser.add_argument('-i1', '--infile1', metavar='INFILE1', type=str,
                        help='Gene list 1 to open',
                        default='/chr21_genes.txt')
    parser.add_argument('-i2', '--infile2', metavar='INFILE2', type=str, help='Gene list 2 to open',
                        default='/HUGO_genes.txt')
    return parser.parse_args()


if __name__ == '__main__':
    main()
