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

    # создай package только добавь папку pkg и туда скопируй .exe и .dll в pkg
    def package(self):
        os.makedirs(self.build_folder + "/../pkg", exist_ok=True)
        os.makedirs(self.build_folder + "/../pkg-setup", exist_ok=True)
        pkg_dir = os.path.join(self.build_folder + "/../pkg")
        pkg_setup_dir = os.path.join(self.build_folder + "/../pkg-setup")
        main_dir = os.path.join(self.build_folder + "/../")

        # Копирование исполняемых файлов
        self.output.info("Packaging binary files")
        for root, dirs, files in os.walk(self.build_folder):
            for file in files:
                # Копирование DLL и исполняемых файлов(только файлов, не директорий к ним)
                if file.endswith((".dll", ".exe")):
                    copy(self, pattern=file, src=root, dst=pkg_dir)
        
         # Путь к файлу .iss, который будет создан
        iss_path = os.path.join(pkg_setup_dir, f"{self.name}-{self.version}.iss")

        # Шаблон файла .iss
        iss_content = f"""
[Setup]
AppName={self.name}
AppVersion={self.version}
DefaultDirName={{pf}}\\{self.name}
DefaultGroupName={self.name}
OutputDir={self.build_folder}/../
OutputBaseFilename={self.name}-{self.version}-setup
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin
UninstallDisplayName={self.name}
UninstallStyle=modern

[Files]
Source: "{pkg_dir}\\*"; DestDir: "{{app}}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{main_dir}\\LICENSE.txt"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{main_dir}\\README.md"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{main_dir}\\config.yaml"; DestDir: "{{app}}"; Flags: ignoreversion

[Icons]
Name: "{{group}}\\{self.name}"; Filename: "{{app}}\\task.exe"
            """

        # Сохранение файла .iss
        save(self, iss_path, iss_content)
        self.output.info(f"Generated .iss file at {iss_path}")


    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.bindirs = ["bin"]

    def generate(self):
        for dep in self.dependencies.values():
            copy(self, pattern="*.dll", src=dep.cpp_info.bindirs[0], dst=self.folders.bin)

