import argparse
import h2o
import time
import socket
from pprint import pprint


seed = 1314
all_models = ['ln', 'lg', 'rf', 'gb', 'nn']

parser = argparse.ArgumentParser()
parser.add_argument('models', help='A list of models to run', type=str, nargs='+', choices=['all'] + all_models)
parser.add_argument('-f', '--file', help='A path or URL from which H2O will import the data set', type=str, default='')
parser.add_argument('-i', '--imputed', help='A path or URL from which H2O will import a pre-imputed data set', type=str, default='')
parser.add_argument('-p', '--port', help='Port number on which H2O is listening', type=int, default=0)
parser.add_argument('-o', '--host', help='Host name or IP address on which H2O is listening', type=int, default=0)

# Parse arguments
args = parser.parse_args()
port = args.port
host = args.host
path = args.file
im_path = args.imputed
models = set(args.models)