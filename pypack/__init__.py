import datetime
import os
from string import Template


class PypackError(Exception): pass
class PathExists(PypackError): pass


class FSNode(object):

    def __init__(self, path):
        self.path = path
        

class File(FSNode):

    template_dir = os.path.join(os.path.dirname(__name__), 'pypack', 'templates')

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

    def __init__(self, path, template=None, recurse=True):
        super(Directory, self).__init__(path)
        self.recurse = recurse

    def copy_to(self, dir, context):
        file_path = os.path.join(dir, self.path)
        os.mkdir(file_path)


class PackageBuilder(object):

    def __init__(self, name, dir=None):
        """
        dir specifies the directory to build the package in; if None, then
        build package in the current directory.
        """
        self.name = self.check_name(name)
        self.dir = dir if dir is not None else os.getcwd()
        self.pkg_dir = os.path.join(self.dir, self.name)
        self.context = {
            'author': 'Joe Smith',
            'author_email': 'joe@smith.com',
            'name': 'mypackage',
            'description': 'This is a description.',
            'url': 'http://mysite.com',
            'date': datetime.date.today().strftime('%B %d, %Y'),
            'version': 0.7,
            'manifest_items': """\
include *.txt
recursive-include docs *.txt""",
        }
        self.context['dashes'] = '=' * len(self.context['name'])
        self.context['version_and_date'] = '%s - %s' % (self.context['version'],
                                                        self.context['date']) 
        self.context['version_and_date_dashes'] = '=' * len(self.context['version_and_date'])
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

    @staticmethod
    def check_name(name):
        """
        Ensure that given name is a valid Python package name.
        """
        # TODO: implement
        return name
    
    def ask_for_context(self):
        pass

    def make_package(self):
        if os.path.exists(self.pkg_dir):
            raise PathExists("Path: '%s' already exists" % self.pkg_dir)
        else:
            os.mkdir(self.pkg_dir)
        for content in self.contents:
            print('copying', content.path, 'to', self.pkg_dir)
            content.copy_to(self.pkg_dir, self.context)


if __name__ == "__main__":
    name = raw_input("Enter name for new package: ")
    builder = PackageBuilder(name)
    builder.make_package()
