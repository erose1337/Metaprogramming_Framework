import os
import sys

PACKAGE_DIR = os.path.split(os.path.abspath(__file__))[0]

def main(package_dir=PACKAGE_DIR):
    command = "python -m pride.main {} {}"
    command = command.format(os.path.join(package_dir, "mediaplayer.py"),
                             ' '.join(sys.argv[1:]))
    print command
    os.system(command)

if __name__ == "__main__":
    main()
