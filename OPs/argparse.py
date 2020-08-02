import argparse

parser = argparse.ArgumentParser()

# Add a required, positional argument for the input data file name,
# and open in 'read' mode
parser.add_argument('infile', type=argparse.FileType('r'))

# Add an optional argument for the output file,
# open in 'write' mode and and specify encoding
parser.add_argument('--output', type=argparse.FileType('w', encoding='UTF-8'))

args = parser.parse_args()

# Read a CSV file,  sum the values in the second column,
# and optionally write to file
sum = 0
with args.infile as infile:
    for line in infile:
        value = int(line.split(',')[1])
        sum += value
        print(sum)

        if args.output is not None:
            args.output.writelines(f'{sum}\n')
