cmake_minimum_required(VERSION 3.13)

find_package(Boost COMPONENTS unit_test_framework REQUIRED)
include_directories(${PROJECT_SOURCE_DIR}/include ${Boost_INCLUDE_DIRS})
link_directories(${PROJECT_SOURCE_DIR}/lib ${Boost_LIBRARY_DIRS})
link_libraries(${PROJECT_NAME} Boost::unit_test_framework)

# add_executable(example_test example.cpp)
# target_compile_features(example_test PRIVATE c_std_11 cxx_std_20)
# target_compile_options(example_test PRIVATE -Wall -pedantic-errors)
# set_target_properties(example_test PROPERTIES C_EXTENSIONS NO CXX_EXTENSIONS NO)
# add_test(NAME example_test COMMAND $<TARGET_FILE:example_test>)
