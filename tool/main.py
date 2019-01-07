#!/usr/bin/env python3

#~ import argparse
import click
import infer

"""
Main script to run tool from 
"""

# argparse
#~ parser = argparse.ArgumentParser()
#~ parser.add_argument("input", help="path to input file in FAST5 format")
#~ args = parser.parse_args()

# 1. Get input from user:
#       * fast5 file
#       * output file name
#       * specify some options?
#       * specify some output?

# 2. Infer signal

# 3. Save to file

# 4. Give output message

# TODO: change in infer length of raw!!
@click.command()
@click.option("--input-file", "-i", help="Path to input file in FAST5 format")
@click.option("--output-file", "-o", help="Name of output file")
def main(input_file, output_file):
    """
    A tool with a neural network as basis to predict the presence of 
    homopolymers in the raw signal from a MinION sequencer. 
    """
    predictions = infer.main(input_file)                                       # predictions is scores
    with open(output_file + ".txt", "w") as dest:
        dest.write("{}\n".format(predictions))
    
    print("Finished class predictions.")
    
    return None
    
if __name__ == "__main__":
    main()
    




