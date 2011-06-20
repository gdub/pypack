"""
Functions for console scripts.
"""

from optparse import OptionParser
 
import pypack


def pypack_command():
    usage = "%prog [options] package_name"
    version = "pypack, version %s, %s" % (pypack.__version__, pypack.__url__)
    parser = OptionParser(usage=usage, version=version)
#    parser.add_option("-l", "--license",  dest="license",
#                      default="placeholder",
#                      help="Specify a license to use.")
#    parser.add_option("-t", "--tests",  action="store_true", dest="test_dir",
#                      default=False,
#                      help="create a 'tests' directory with a stub unittest.")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("Incorrect number of arguments")
    builder = pypack.PackageBuilder(args[0])
    builder.make_package()


if __name__ == "__main__":
    pypack_command()
