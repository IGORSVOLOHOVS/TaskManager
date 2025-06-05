find_package(Protobuf REQUIRED)
find_package(gRPC REQUIRED)

set(PROTO_FILES_DIR ${CMAKE_CURRENT_SOURCE_DIR}/cmake/structs)
set(PROTO_FILE_PATH ${PROTO_FILES_DIR}/task.proto)
set(GENERATED_FILES_DIR ${CMAKE_CURRENT_SOURCE_DIR}/extern)

include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/src # Директория с вашими исходниками (main.cpp и т.д.)
    ${Protobuf_INCLUDE_DIRS}       # Заголовочные файлы Protobuf
    ${gRPC_INCLUDE_DIRS}           # Заголовочные файлы gRPC
    ${GENERATED_FILES_DIR}         # Директория со сгенерированными заголовочными файлами
)

protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS
    ${PROTO_FILE_PATH}
    OUT_DIR ${GENERATED_FILES_DIR}  # Явно указываем выходную директорию
)

protobuf_generate_grpc_cpp(GRPC_SRCS GRPC_HDRS
    ${PROTO_FILE_PATH}
    OUT_DIR ${GENERATED_FILES_DIR} # Явно указываем выходную директорию
)

# Предполагается, что они находятся в директории src/
set(APPLICATION_SOURCES
    src/main.cpp
    # Добавьте сюда другие ваши .cpp файлы
    ${PROTO_SRCS}    # Сгенерированные Protobuf исходники
    ${GRPC_SRCS}     # Сгенерированные gRPC исходники
)

target_include_directories(${PROJECT_NAME} PUBLIC     
    ${Protobuf_INCLUDE_DIRS}      
    ${gRPC_INCLUDE_DIRS}           
    ${GENERATED_FILES_DIR} 
)
target_link_libraries(${PROJECT_NAME} PRIVATE
    ${Protobuf_LIBRARIES} # Библиотеки Protobuf (например, libprotobuf)
    gRPC::grpc++          # Основная библиотека gRPC C++
    gRPC::grpc            # Базовая библиотека gRPC
    Threads::Threads      # gRPC часто требует библиотеку для работы с потоками
)
