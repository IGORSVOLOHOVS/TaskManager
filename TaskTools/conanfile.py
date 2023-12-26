import os
from conan import ConanFile
from conan.tools.files import load, copy, collect_libs, save
from conan.tools.cmake import CMake

class TaskConan(ConanFile):
    name = "task"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    requires = [
        "yaml-cpp/0.8.0",
        "benchmark/1.8.3"
    ]
    test_requires = [
        "gtest/1.14.0"
    ]
    generators = [
        "CMakeToolchain",
        "CMakeDeps"
    ]
    default_options = {
        "*:shared": True
    }

    def layout(self):
        self.folders.build = "build"
        self.folders.source = "."
        self.folders.generators = "cmake"
        self.folders.bin = "bin"
        self.folders.test = "test"

    def build(self):
        cmake = CMake(self)
        # Выбор предустановки CMake в зависимости от runMode
        cmake.configure()
        cmake.build()

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)


