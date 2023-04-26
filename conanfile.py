import os

from conan import ConanFile
from conan.tools.files import copy


version = os.environ['version']
project = os.environ['project']


class FM(ConanFile):
    name = project
    version = version
    exports_sources = "include/*"
    no_copy_source = True

    def package(self):
        copy(self, "*.h", self.source_folder, self.package_folder)

    def package_info(self):
         self.cpp_info.bindirs = []
         self.cpp_info.libdirs = []