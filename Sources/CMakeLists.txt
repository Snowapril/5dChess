# Target name
set(target 5dChess)

# Define root directory
set(root_dir ${CMAKE_CURRENT_SOURCE_DIR}/..)

# Includes
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
)

# Sources
file(GLOB header_dir
    ${root_dir}/Includes
)

file(GLOB_RECURSE headers
    ${header_dir}/*.hpp
)

file(GLOB_RECURSE sources
    ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp
)

# Build executable
add_library(${target}
    ${sources})

# Project options
set_target_properties(${target}
    PROPERTIES
    ${DEFAULT_PROJECT_OPTIONS}
)

# Compile options
target_compile_options(${target}
    PRIVATE
    PUBLIC
    ${DEFAULT_COMPILE_OPTIONS}
    INTERFACE
)

# Compile definitions
target_compile_definitions(${target}
    PRIVATE
    RESOURCES_DIR="${RESOURCES_DIR}"
    ${DEFAULT_COMPILE_DEFINITIONS}
)

target_link_libraries(${target}
    PRIVATE
    PUBLIC
    ${DEFAULT_LINKER_OPTIONS}
	${DEFAULT_LIBRARIES}
    INTERFACE
)