cmake_minimum_required(VERSION 3.12)

execute_process(COMMAND git describe --tags --abbrev=0        RESULT_VARIABLE VerResult OUTPUT_VARIABLE VerString ERROR_QUIET OUTPUT_STRIP_TRAILING_WHITESPACE)
execute_process(COMMAND git describe --tags --abbrev=7 --long RESULT_VARIABLE RevResult OUTPUT_VARIABLE RevString ERROR_QUIET OUTPUT_STRIP_TRAILING_WHITESPACE)

set(SysString a)

if(${VerResult})
    set(VerString 0.0.0)
endif()

if(${RevResult})
    set(RevString 0.0.0-0-g0000000)
endif()

project(${SysString} VERSION ${VerString})
set(PROJECT_BRIEF "Empty project")

configure_file(version.hpp.in ${PROJECT_SOURCE_DIR}/version.hpp)
configure_file(../Doxyfile.in ${PROJECT_SOURCE_DIR}/../Doxyfile)

add_executable(${PROJECT_NAME})
set_target_properties(${PROJECT_NAME} PROPERTIES CXX_EXTENSIONS NO)

target_include_directories(${PROJECT_NAME}
PRIVATE
)

target_link_libraries(${PROJECT_NAME}
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
