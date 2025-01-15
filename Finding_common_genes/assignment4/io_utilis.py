"""
Opening the file handle in read or write mode
"""
import sys


def get_filehandle(file, mode):
    """
    filehandle : get_filehandle(infile,"r")
    Takes: 2 arguments, file name and mode
    :param file: The file to be opened
    :param mode: The way to open the file.(Read or write)
    :return: filehandle
    """

    try:
        f_handle = open(file, mode)
        return f_handle
    except OSError:
        print(f"Could not open the file: {file} for type'{mode}'", file=sys.stderr)
        raise
    except ValueError:
        print(f"Could not open the file: {file} for type'{mode}'", file=sys.stderr)
        raise
