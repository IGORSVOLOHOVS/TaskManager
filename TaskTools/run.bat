rm -r build
Set-ExecutionPolicy RemoteSigned
conan install . --build=missing --output-folder build -c tools.env.virtualenv:powershell=True 
cmake --preset conan-default
.\build\build\generators\conanbuild.ps1
.\build\build\generators\conanrun.ps1
cmake --build --preset conan-release
.\build\build\Release\main.exe