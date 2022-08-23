from . import __version__
import common_lib_pypi
import dep_of_common_lib


def main() -> None:
    print(__package__, __version__)
    print(common_lib_pypi.__name__, common_lib_pypi.__version__)
    print(dep_of_common_lib.__name__, dep_of_common_lib.__version__)


if __name__ == "__main__":
    main()
