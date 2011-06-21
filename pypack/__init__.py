import datetime
import os
from string import Template


__version__ = '0.8'
__url__ = 'http://pypi.python.org/pypi/python-package-template/'


class PypackError(Exception): pass
class PathExists(PypackError): pass


class FSNode(object):
    """
    Base class for file system node types, e.g. File and Directory.
    """

    def __init__(self, path):
        self.path = path


class File(FSNode):
    """
    Represents a file who's content is based on a template.
    """

    template_dir = os.path.join(__path__[0], 'templates')

    def __init__(self, path, template=None, substitutions=True):
        super(File, self).__init__(path)
        self.template = template

    @property
    def template_path(self):
        # If no template file was given, use the same name as the path.
        if self.template:
            path = self.template
        else:
            path = self.path
        return os.path.join(self.template_dir, path)

    def copy_to(self, dir, context):
        file_path = os.path.join(dir, self.path)
        with open(file_path, 'w') as f:
            with open(self.template_path) as template_file:
                template = Template(template_file.read())
                f.write(template.substitute(**context))


class Directory(FSNode):
    """
    Represents a directory.
    """

    def copy_to(self, dir, context):
        file_path = os.path.join(dir, self.path)
        os.mkdir(file_path)


class PackageBuilder(object):
    """
    Defines package contents and how that content gets created.
    """

    def __init__(self, name, options, contents=None):
        self.name = self.check_name(name)
        if not options.target:
            options.target = os.path.join(os.getcwd(), name)
        self.target_dir = options.target
        self.pkg_dir = os.path.join(options.target, name)
        self.options = options
        if contents is None:
            self.contents = [
                File('CHANGES.txt', 'changes.txt'),
                File('distribute_setup.py', substitutions=False),
                File('LICENSE.txt', 'license.txt'),
                File('MANIFEST.in', 'manifest.txt'),
                File('README.txt', 'readme.txt'),
                File('setup.py', 'setup.txt'),
                Directory(self.name),
                    File(os.path.join(self.name, '__init__.py'), 'empty.txt'),
            ]
        else:
            self.contents = contents

    def build_context(self, name, options):
        """
        Build and return a context dictionary, using passed name and options.
        """
        context = {
            'author': options.author,
            'author_email': options.email,
            'name': name,
            'description': options.desc,
            'url': options.url,
            'date': datetime.date.today().strftime('%B %d, %Y'),
            'version': options.version,
            'manifest_items': """\
include *.txt
recursive-include docs *.txt""",
        }
        context['dashes'] = '=' * len(context['name'])
        context['version_and_date'] = '%s - %s' % (context['version'],
                                                   context['date'])
        context['version_and_date_dashes'] = '=' * len(context['version_and_date'])
        return context

    @staticmethod
    def check_name(name):
        """
        Ensure that given name is a valid Python package name.
        """
        if not name or (name and len(name) < 2):
            raise PypackError("Package name must be at least two characters.")
        # TODO: implement
        return name

    def make_package(self):
        """
        Create the package and its contents.
        """
        if os.path.exists(self.target_dir):
            raise PathExists("Target directory exists; aborting.")
        os.mkdir(self.target_dir)
        os.mkdir(self.pkg_dir)
        for content in self.contents:
            print "creating file:", os.path.join(self.pkg_dir, content.path)
            content.copy_to(self.pkg_dir,
                            self.build_context(self.name, self.options))
