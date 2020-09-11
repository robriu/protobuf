# minimum CMake required
cmake_minimum_required(VERSION 2.8.12)

# project
project(main)

# find required protobuf package
find_package(protobuf CONFIG REQUIRED)

if(protobuf_VERBOSE)
  message(STATUS "Using Protocol Buffers ${Protobuf_VERSION}")
endif()

set(CMAKE_INCLUDE_CURRENT_DIR TRUE)

# include the output directory for code generation
include_directories(${CMAKE_CURRENT_BINARY_DIR})
# add the protos directory
include_directories(${CMAKE_CURRENT_BINARY_DIR}/protos)

# set the sources of the project
set(SOURCES cpp/main.cpp)

# set the protos of the project
set(MAIN_PROTOS proto/<file_name>.proto)

# code Generation
if(protobuf_MODULE_COMPATIBLE) 
    # legacy Support
    protobuf_generate_cpp(MAIN_PROTO_SRCS MAIN_PROTO_HDRS ${MAIN_PROTOS})
    list(APPEND SOURCES ${MAIN_PROTO_SRCS} ${MAIN_PROTO_HDRS})
endif()

# executable setup
set(executable_name main)

# add the executable
add_executable(${executable_name} ${SOURCES} ${MAIN_PROTOS})

if(protobuf_MODULE_COMPATIBLE) 
    # legacy mode
    target_include_directories(${executable_name} PUBLIC ${PROTOBUF_INCLUDE_DIRS})
    target_link_libraries(${executable_name} ${PROTOBUF_LIBRARIES})
else()
    target_link_libraries(${executable_name} protobuf::libprotobuf)
    protobuf_generate(TARGET ${executable_name})
endif()