""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser
try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root


if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)

    import os

    parser = ArgumentParser(description='This programme writes the data from the input file to the output file after applying a standard scale transform..')
    parser.add_argument('infile', help='provide input file path', nargs='?')
    parser.add_argument('outfile', help='provide output file path', nargs='?')
    args = parser.parse_args()
    input_data = np.loadtxt(args.infile)
    normalized = (input_data - input_data.mean(axis=0) / input_data.std(axis=0))
    processed = normalized
    root_dir = get_repository_root()
    os.makedirs(root_dir / "outputs", exist_ok=True)
    np.savetxt(args.outfile, processed, fmt='%.2e')
