cmake_minimum_required(VERSION 3.13)

execute_process(COMMAND git describe --tags --abbrev=0        RESULT_VARIABLE VerResult OUTPUT_VARIABLE VerString ERROR_QUIET OUTPUT_STRIP_TRAILING_WHITESPACE)
execute_process(COMMAND git describe --tags --abbrev=8 --long RESULT_VARIABLE RevResult OUTPUT_VARIABLE RevString ERROR_QUIET OUTPUT_STRIP_TRAILING_WHITESPACE)

set(SysString a)

if(VerResult)
    set(VerString 0.0.0)
endif()
if(RevResult)
    set(RevString 0.0.0-0-g00000000)
endif()

project(${SysString} VERSION ${VerString})
set(PROJECT_BRIEF "Empty project")

add_subdirectory(${PROJECT_SOURCE_DIR}/src)

if(UNIT_TEST)
    enable_testing()
    add_subdirectory(${PROJECT_SOURCE_DIR}/test)
endif()
