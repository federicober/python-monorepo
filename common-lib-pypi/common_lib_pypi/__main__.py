from . import __version__
import dep_of_common_lib

def main():
    print(__package__, __version__)
    print(dep_of_common_lib.__name__, dep_of_common_lib.__version__)

if __name__ == "__main__":
    main()