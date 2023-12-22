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
        self.folders.imports = "bin"
        self.folders.test = "test"

    def build(self):
        cmake = CMake(self)
        # Выбор предустановки CMake в зависимости от runMode
        cmake.configure()
        cmake.build()

    def package(self):
        # Создание стандартных директорий для пакета
        include_dir = os.path.join(self.package_folder, "include")
        lib_dir = os.path.join(self.package_folder, "lib")
        bin_dir = os.path.join(self.package_folder, "bin")
        os.makedirs(include_dir, exist_ok=True)
        os.makedirs(lib_dir, exist_ok=True)
        os.makedirs(bin_dir, exist_ok=True)
        
        self.output.info("Packaging binary files")
        for root, dirs, files in os.walk(self.build_folder):
            for file in files:
                full_file_path = os.path.join(root, file)
                relative_dir = os.path.relpath(root, self.build_folder)
                if file.endswith((".h", ".hpp")):
                    # Копирование заголовочных файлов
                    copy(self, pattern=file, src=root, dst=os.path.join(include_dir, relative_dir))
                elif file.endswith(".lib"):
                    # Копирование библиотек
                    copy(self, pattern=file, src=root, dst=os.path.join(lib_dir, relative_dir))
                elif file.endswith((".dll", ".exe")):
                    # Копирование DLL и исполняемых файлов
                    copy(self, pattern=file, src=root, dst=os.path.join(bin_dir, relative_dir)) 
         # Путь к файлу .iss, который будет создан
        iss_path = os.path.join(self.build_folder, f"{self.name}-{self.version}.iss")

        # Шаблон файла .iss
        iss_content = f"""
[Setup]
AppName={self.name}
AppVersion={self.version}
DefaultDirName={{pf}}\\{self.name}
DefaultGroupName={self.name}
OutputDir=.
OutputBaseFilename={self.name}-{self.version}-setup
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin
UninstallDisplayName={self.name}
UninstallStyle=modern

[Files]
Source: "{bin_dir}\\*"; DestDir: "{{app}}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{lib_dir}\\*"; DestDir: "{{app}}\\lib"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{include_dir}\\*"; DestDir: "{{app}}\\include"; Flags: ignoreversion recursesubdirs createallsubdirs
            """

        # Сохранение файла .iss
        save(self, iss_path, iss_content)
        self.output.info(f"Generated .iss file at {iss_path}")

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
