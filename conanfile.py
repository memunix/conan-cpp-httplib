from conans import ConanFile, tools
import os

class CpphttplibConan(ConanFile):
    name = "cpp-httplib"
    version = "0.2.4"
    license = "MIT"
    author = "yhirose"
    url = "https://github.com/yhirose/cpp-httplib"
    description = "A C++ single-file header-only cross platform HTTP/HTTPS library."
    # No settings/options are necessary, this is header only
    # exports_sources = "include/*"
    no_copy_source = True

    def source(self):
        self.run("git clone https://github.com/yhirose/cpp-httplib")

    # def source(self):
    #     source_url = "https://github.com/yhirose/cpp-httplib"
    #     tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
    #     extracted_dir = self.name + "-" + self.version
    #     os.rename(extracted_dir, "sources")

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)

    def package_id(self):
        self.info.header_only()
