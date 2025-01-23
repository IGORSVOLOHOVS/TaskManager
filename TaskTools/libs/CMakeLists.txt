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
