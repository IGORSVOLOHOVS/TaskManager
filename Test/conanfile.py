
from conan import ConanFile
from conan.tools.cmake import CMakeDeps, CMakeToolchain, cmake_layout

class TaskConan(ConanFile):
    name = "Task"
    version = "0.1.0"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "src/*", "tests/*", "extern/*", "cmake/*"

    def requirements(self):
        self.requires("gtest/1.14.0")
        self.requires("spdlog/1.15.1")
        self.requires("protobuf/5.27.0")
        self.requires("grpc/1.72.0")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.cache_variables["CMAKE_EXPORT_COMPILE_COMMANDS"] = "ON"
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()
