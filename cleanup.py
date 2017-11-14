#!/usr/bin/python

# Author: Emmanuel A. Hernandez <@snipa.v1>

""" This script will cleanup logs based on paths in the config.yml file
    or add a single file path with the --p flag"""

import os
import yaml
import argparse

CFG = 'config.yml'

parser = argparse.ArgumentParser()
parser.add_argument("--p",
                    dest="path",
                    help="Root path to cleanup",
                    action='store')
args = parser.parse_args()
path = args.path if args.path else None


def cleanup_logs(path):
    print('[.] Removing logs in: "{}"'.format(path))
    files = os.listdir(path)
    if files:
        c = 0
        for file in files:
            print('\t- Removing: {}'.format(file))
            os.remove(path + file)
            c += 1
        print("\n\t* Files removed: {}\n\n".format(str(c)))

    else:
        print("[!] No files to remove\n\n")


def main(path=path):
    with open(CFG, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    paths = (cfg['paths'])

    if path:
        cleanup_logs(path)
    else:

        for path in paths:
            cleanup_logs(path)

    print('\n[%] Done')


if __name__ == '__main__':
    try:
        main(path=path)
    except KeyboardInterrupt:
        print('\n[!] KeyboardInterrupt Detected.')
        print('[%] Exiting...')
        exit(0)
