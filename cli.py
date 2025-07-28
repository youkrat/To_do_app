"""

"""
import sys 
import argparse


if len(sys.argv) == 1:
    print(
        "Usage: type cli.py -h/--help")
    
else:
    parser = argparse.ArgumentParser(description ="Task Management system")
    parser.add_argument("-a", help = "Add task")
    parser.add_argument("-r", help = "Lists all pending tasks")
    args = parser.parse_args()

    if args.a:
        task = args.a
        with open("tasks.txt", "a") as file:
                file.write(f'{task}\n')
    elif args.r:
        with open("tasks.txt", "r") as file:
                for line in file:
                    print(f"Current remaining tasks: {line}", end ="")