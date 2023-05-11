cmake_minimum_required(VERSION 3.13)

configure_file(version.hpp.in ${CMAKE_CURRENT_SOURCE_DIR}/version.hpp)
configure_file(../Doxyfile.in ${CMAKE_CURRENT_SOURCE_DIR}/../Doxyfile)

add_executable(${PROJECT_NAME})
# add_library(${PROJECT_NAME} STATIC)
# add_library(${PROJECT_NAME} SHARED)

set_target_properties(${PROJECT_NAME}
PROPERTIES
    CXX_EXTENSIONS NO
    LINK_FLAGS_RELEASE -s
    RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin
    ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/lib
    LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/lib
)

target_include_directories(${PROJECT_NAME}
PRIVATE
    ${PROJECT_SOURCE_DIR}/include
)

target_link_directories(${PROJECT_NAME}
PRIVATE
)

target_link_libraries(${PROJECT_NAME}
PRIVATE
)

target_link_options(${PROJECT_NAME}
PRIVATE
)

target_compile_definitions(${PROJECT_NAME}
PRIVATE
)

target_compile_features(${PROJECT_NAME}
PRIVATE
    c_std_11
    cxx_std_20
)

target_compile_options(${PROJECT_NAME}
PRIVATE
    -Wall
    -pedantic-errors
)

target_sources(${PROJECT_NAME}
PRIVATE
    main.cpp
)
