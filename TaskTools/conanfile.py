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
        self.folders.lib = "lib"
        self.folders.include = "include"
        self.folders.test = "test"


    def build(self):
        cmake = CMake(self)
        # Выбор предустановки CMake в зависимости от runMode
        cmake.configure()
        cmake.build()

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
        
    def generate(self):
        for dep in self.dependencies.values():
            copy(self, "*.dll", dep.cpp_info.bindirs[0], self.build_folder + "/bin")
            copy(self, "*.so", dep.cpp_info.bindirs[0], self.build_folder + "/bin")

        if self.settings.compiler == "gcc" and self.settings.os == "Windows":
            gcc_bin = "C:/MinGW/bin"
            gcc_dll = ["libgcc_s_seh-1.dll", "libstdc++-6.dll", "libwinpthread-1.dll"]
            for dll in gcc_dll:
                copy(self, dll, gcc_bin, self.build_folder + "/bin")
                
        if self.settings.os == "Windows" and self.settings.compiler == "msvc":
            vs_bin = "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.29.30133/bin/HostX64/x64"
            vs_dll = ["msvcp140.dll", "vcruntime140.dll", "vcruntime140_1.dll"]
            for dll in vs_dll:
                copy(self, dll, vs_bin, self.build_folder + "/bin")
            
            kernel32_dll = "C:/Windows/System32"
            copy(self, "kernel32.dll", kernel32_dll, self.build_folder + "/bin")
