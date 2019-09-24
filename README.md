# build package locally
conan create . memunix/stable
# add to CMakeLists.txt
conan_cmake_run(REQUIRES
        cpp-httplib/0.2.4@memunix/stable
        BASIC_SETUP BUILD missing
        )


