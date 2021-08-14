#!/usr/bin/python

# Author: Emmanuel A. Hernandez <@snipa.v1>

""" This script will cleanup logs based on paths in the config.yml file
    or add a single file path with the --p flag"""

import argparse
import os

import yaml

CFG = 'config.yml'

parser = argparse.ArgumentParser()
parser.add_argument("--p",
                    dest="path",
                    help="Root path to cleanup",
                    action='store')
parser.add_argument("--all",
                    dest="all",
                    help="Set this flag to delete all files in specified path.",
                    action='store_true')
args = parser.parse_args()
path = args.path if args.path else None
all = args.all if args.all else None


def cleanup_logs(path):
    """
    Function takes in a file path and removes only .log files by default
    If '--all' is set in CLI, it will delete 'ALL' files(all extension types) in the specified path

    Args:
        path ([String]): Filepath to target directory that contains files to delete
    """
    print('[.] Removing logs in: "{}"'.format(path))
    files = os.listdir(path)
    if files:
        c = 0
        for file in files:
            if all:
                print(f'\t- Removing all files: {file}')
                os.remove(path + file)
                c += 1
            elif '.log' in file:
                print(f'\t- Removing logs: {file}')
                os.remove(path + file)
                c += 1
            else:
                pass
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
