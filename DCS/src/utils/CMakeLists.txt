cmake_minimum_required(VERSION 2.8)
project(DCS)

find_library(NOISE_LIBRARY
   NAMES libnoise.so
   PATHS /usr/lib /usr/local/lib
)

find_path(NOISE_INCLUDE_DIR
  NAMES libnoise/noise.h noise/noise.h
  PATHS /usr/include /usr/local/include
)

if (NOT NOISE_LIBRARY OR NOT NOISE_INCLUDE_DIR)
   set(errors "${errors}\t\t- libNoise library\n")
   set(dependency_error True)
endif()

## Include path
include_directories(${NOISE_INCLUDE_DIR})
## Linker path
link_directories(${NOISE_LIBRARY})

## Target
set(UTILS_SRCS utils.cpp)
add_library(utils SHARED ${UTILS_SRCS})
target_link_libraries(utils noise)

## Compiler flags
if(CMAKE_COMPILER_IS_GNUCXX)
    set(CMAKE_CXX_FLAGS "-O2 -ansi -pedantic")        ## Optimize
    set(CMAKE_EXE_LINKER_FLAGS "-s")  ## Strip binary
endif()
