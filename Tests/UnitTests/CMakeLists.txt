# Target name
set(target UnitTests)

# Includes
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/../../Includes
    ${CMAKE_CURRENT_SOURCE_DIR}/../../Libraries/doctest
    ${CMAKE_CURRENT_SOURCE_DIR}
)

# Sources
file(GLOB sources
    ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)

# Build executable
add_executable(${target}
    ${sources})

# Project options
set_target_properties(${target}
    PROPERTIES
    ${DEFAULT_PROJECT_OPTIONS}
)

# Compile options
target_compile_options(${target}
    PUBLIC
    ${DEFAULT_COMPILE_OPTIONS}
)

target_compile_definitions(${target}
    PRIVATE
    RESOURCE_DIR="${PROJECT_SOURCE_DIR}/Resources/"
    ${DEFAULT_COMPILE_DEFINITIONS}
)

# Link libraries
target_link_libraries(${target}
    PUBLIC
    ${DEFAULT_LINKER_OPTIONS}
	${DEFAULT_LIBRARIES}
    5dChess) 