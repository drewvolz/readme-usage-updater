from typing import List, Optional
import sys
import argparse


def main(sys_args: Optional[List[str]] = None) -> int:
    if not sys_args:
        sys_args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog='readmeUsageUpdater',
        description='Update README usage as soon as the help is changed.')

    # Play around!
    # 1. Uncomment lines 19-23,
    # 2. run `make` or `python3 ./script/update-usage.py`
    # 3. then run `git diff README.md` to see the changes
    #
    # parser.add_argument('-o',
    #                     '--options',
    #                     required=False,
    #                     action='append',
    #                     help='the options to pass to the program')

    args = parser.parse_args(sys_args)

    print(f'readmeUsageUpdater example')
    print(f'argparse found these args: {args}')

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        pass
