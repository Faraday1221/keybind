import argparse
from keybind.keybind import interactive_loop


parser = argparse.ArgumentParser(description="randomly prompt keybindigs")
# parser.add_argument('nrounds', type=list, default=list("1234qwerasdf"))
# parser.add_argument('keys', type=int, default=50)
parser.add_argument('keys', action='store_const', const=list("1234qwerasdf"))
parser.add_argument('nrounds', action='store_const', const=50)

args = parser.parse_args()

def main():
    interactive_loop(sourcekeys=args.keys, nrounds=args.nrounds)
    pass


main()