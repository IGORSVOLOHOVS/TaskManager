function(add_libs_dependency target_name)
  # Определяем libs_dir в зависимости от конфигурации сборки
  if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    set(libs_dir "libs/debug")
  else()
    set(libs_dir "libs/release")
  endif()

  # Создаем папки, если они не существуют
  file(MAKE_DIRECTORY "${libs_dir}")
  file(MAKE_DIRECTORY "${libs_dir}/lib")
  file(MAKE_DIRECTORY "${libs_dir}/bin")
  file(MAKE_DIRECTORY "${libs_dir}/include")
  
  # Создаем список для хранения путей к .lib файлам
  set(LIBS_LIBRARIES)

  # Находим все .lib файлы в папке libs_dir/lib и ее подпапках
  file(GLOB_RECURSE LIB_FILES "${libs_dir}/lib/*.lib")

  # Добавляем каждый найденный .lib файл в список LIBS_LIBRARIES
  foreach(LIB_FILE ${LIB_FILES})
    list(APPEND LIBS_LIBRARIES ${LIB_FILE})
  endforeach()

  # Создаем список для хранения путей к .dll файлам
  set(LIBS_DLLS)

  # Находим все .dll файлы в папке libs_dir/bin и ее подпапках
  file(GLOB_RECURSE DLL_FILES "${libs_dir}/bin/*.dll")

  # Добавляем каждый найденный .dll файл в список LIBS_DLLS
  foreach(DLL_FILE ${DLL_FILES})
    list(APPEND LIBS_DLLS ${DLL_FILE})
  endforeach()

  # Создаем libs.hpp
  file(WRITE "libs/libs.hpp" "#pragma once\n\n") 

  # Находим все .hpp и .h файлы в папке libs_dir/include и ее подпапках
  file(GLOB_RECURSE HEADER_FILES "${libs_dir}/include/**/*.hpp" "${libs_dir}/include/**/*.h") 
  foreach(HEADER_FILE ${HEADER_FILES})
    # Получаем полный путь к директории include
    get_filename_component(INCLUDE_DIR "${libs_dir}/include" ABSOLUTE)
    # Получаем относительный путь к заголовочному файлу
    file(RELATIVE_PATH HEADER_PATH "${INCLUDE_DIR}" "${HEADER_FILE}")
    # Проверяем, что путь не пустой
    if(HEADER_PATH)
      # Добавляем #include в libs.hpp
      file(APPEND "libs/libs.hpp" "#include <${HEADER_PATH}>\n") 
    endif()
  endforeach()

  # Создаем зависимость target_name как статическую библиотеку
  add_library(${target_name} STATIC libs/libs.hpp libs/main.cpp)

  # Добавляем .lib файлы в зависимость target_name
  target_link_libraries(${target_name} PUBLIC ${LIBS_LIBRARIES})

  # Добавляем папку libs_dir/include в пути поиска заголовочных файлов
  target_include_directories(${target_name} PUBLIC "${libs_dir}/include")

  # Копируем .dll файлы в выходной каталог при сборке
  foreach(DLL_FILE ${LIBS_DLLS})
    add_custom_command(TARGET ${target_name} POST_BUILD
                       COMMAND ${CMAKE_COMMAND} -E copy_if_different
                       ${DLL_FILE}
                       $<TARGET_FILE_DIR:${target_name}>)
  endforeach()

  install(DIRECTORY "${libs_dir}/bin/" DESTINATION bin)
  install(DIRECTORY "${libs_dir}/lib/" DESTINATION lib)
  install(DIRECTORY "${libs_dir}/include/" DESTINATION include)
endfunction()

find_package(Doxygen)
set(DOXYFILE_PROJECT_NAME "Task")
set(DOXYFILE_PROJECT_BRIEF "The templates for tasks")
set(DOXYFILE_PROJECT_VERSION "1.0.0")
set(DOXYFILE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/documentation")
set(DOXYFILE_SOURCE_DIRS "${CMAKE_CURRENT_SOURCE_DIR}")
set(DOXYFILE_GENERATE_LATEX NO) # Disable LaTeX generation
set(DOXYFILE_HTML_STYLESHEET "${CMAKE_CURRENT_SOURCE_DIR}/../tools/other/Doxyfile.css")
configure_file(../tools/other/Doxyfile.in ${CMAKE_BINARY_DIR}/Doxyfile @ONLY)

add_custom_target(documentation
  COMMAND doxygen ${CMAKE_BINARY_DIR}/Doxyfile
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
  COMMAND chrome ${CMAKE_BINARY_DIR}/documentation/html/index.html
)

# if windows
if (WIN64 OR WIN32)
  add_custom_target(vcpkg
    COMMAND powershell -Command "if (-Not (Test-Path 'vcpkg')) { git clone https://github.com/microsoft/vcpkg.git; cd vcpkg; .\\bootstrap-vcpkg.bat }"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )

  add_custom_target(doxygen
    COMMAND powershell -Command "if (-Not (Test-Path 'doxygen')) { choco install doxygen.install -y }"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )

  add_custom_target(conan
    COMMAND powershell -Command "if (-Not (Test-Path 'conan')) { pip install conan }"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )

  add_custom_target(mingw
    COMMAND powershell -Command "if (-Not (Test-Path 'mingw')) { choco install mingw -y }"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )

  add_custom_target(chocolatey
    COMMAND powershell -Command "if (-Not (Test-Path 'chocolatey')) { Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')) }"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )

  add_custom_target(msvc
    COMMAND powershell -Command "if (-Not (Test-Path 'msvc')) { choco install visualstudio2019buildtools visualstudio2019-workload-vctools -y }"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )

  add_custom_target(clang
    COMMAND powershell -Command "if (-Not (Test-Path 'clang')) { choco install llvm -y }"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )

  add_custom_target(emscripten
    COMMAND powershell -Command "if (-Not (Test-Path 'emscripten')) { choco install emscripten -y }"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )

  add_custom_target(nsis
    COMMAND powershell -Command "if (-Not (Test-Path 'nsis')) { choco install nsis -y }"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )

  add_custom_target(ccache
    COMMAND powershell -Command "if (-Not (Test-Path 'ccache')) { choco install ccache -y }"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )

  add_custom_target(ninja
    COMMAND powershell -Command "if (-Not (Test-Path 'ninja')) { choco install ninja -y }"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )
elseif(UNIX)
  add_custom_target(conan
    COMMAND bash -c "if [ ! -d 'conan' ]; then pip install conan; fi"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )

  add_custom_target(ccache
    COMMAND bash -c "if [ ! -d 'ccache' ]; then sudo apt-get install ccache -y; fi"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )

  add_custom_target(doxygen
    COMMAND bash -c "if [ ! -d 'doxygen' ]; then sudo apt-get install doxygen -y; fi"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )

  add_custom_target(build-essential
    COMMAND bash -c "if [ ! -d 'build-essential' ]; then sudo apt-get install build-essential -y; fi"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )

  add_custom_target(emscripten
    COMMAND bash -c "if [ ! -d 'emscripten' ]; then sudo apt-get install emscripten -y; fi"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )

  add_custom_target(ninja
    COMMAND bash -c "if [ ! -d 'ninja' ]; then sudo apt-get install ninja-build -y; fi"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )
endif()




# ---------------------------- [ CPack ] -----------------------------------------
include(InstallRequiredSystemLibraries)
include(GNUInstallDirs)


set(CPACK_PACKAGE_VERSION ${VERSION})
set(CPACK_PACKAGE_NAME ${PROJECT_NAME})
set(CPACK_RESOURCE_FILE_README "${CMAKE_CURRENT_SOURCE_DIR}/../tools/other/README.md")
set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/../tools/other/LICENSE.txt")
set(CPACK_NSIS_MUI_ICON "${CMAKE_CURRENT_SOURCE_DIR}/../tools/other/icon.ico")

include(CPack)
