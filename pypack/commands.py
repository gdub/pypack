"""
Functions for console scripts.
"""

from optparse import OptionParser

import pypack


def pypack_command():
    usage = "%prog [options] package_name"
    version = "pypack, version %s, %s" % (pypack.__version__, pypack.__url__)
    parser = OptionParser(usage=usage, version=version)
    parser.add_option("-a", "--author", dest="author", default="",
                      help="The author name to use for the created package.")
    parser.add_option("-d", "--desc", dest="desc", default="",
                      help="A short description for the created package.")
    parser.add_option("-e", "--email", dest="email", default='',
                      help=("The author e-mail address to use for the created"
                            " package."))
    parser.add_option("--initial-version", dest="version", default="0.1",
                      help=("The initial version number to use for the created"
                            " package, e.g. 0.2, 1.0, 1.0-rc1, etc."))
    parser.add_option("-t", "--target", dest="target", default=None,
                      help=("Specify a target directory to place the package"
                            " skeleton files in (the directory must not"
                            " already exist).  If not given, then new package"
                            " contents will be placed in the current"
                            " directory."))
    parser.add_option("-u", "--url", dest="url", default="",
                      help=("The URL to use for the created package."))
#    parser.add_option("-l", "--license",  dest="license",
#                      default="placeholder",
#                      help="Specify a license to use.")
#    parser.add_option("-t", "--tests",  action="store_true", dest="test_dir",
#                      default=False,
#                      help="create a 'tests' directory with a stub unittest.")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("Incorrect number of arguments")
    builder = pypack.PackageBuilder(args[0], options)
    builder.make_package()


if __name__ == "__main__":
    pypack_command()
