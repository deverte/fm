from conan import ConanFile
from conan.tools.files import copy


class Fm(ConanFile):
    name = "fm"
    version = "0.1.2"
    exports_sources = "include/*"
    no_copy_source = True

    def requirements(self):
        self.requires("nlohmann_json/3.11.2") # Workaround for conaninfo.txt generation

    def package(self):
        copy(self, "*.h", self.source_folder, self.package_folder)

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []