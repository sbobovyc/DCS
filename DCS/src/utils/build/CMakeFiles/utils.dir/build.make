# CMAKE generated file: DO NOT EDIT!
# Generated by "MSYS Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canoncical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = "/c/Program Files (x86)/CMake 2.8/bin/cmake.exe"

# The command to remove a file.
RM = "/c/Program Files (x86)/CMake 2.8/bin/cmake.exe" -E remove -f

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = "/c/Program Files (x86)/CMake 2.8/bin/cmake-gui.exe"

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /C/Users/sbobovyc/workspace/DCS/DCS/src/utils

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /C/Users/sbobovyc/workspace/DCS/DCS/src/utils/build

# Include any dependencies generated for this target.
include CMakeFiles/utils.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/utils.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/utils.dir/flags.make

CMakeFiles/utils.dir/utils.cpp.obj: CMakeFiles/utils.dir/flags.make
CMakeFiles/utils.dir/utils.cpp.obj: CMakeFiles/utils.dir/includes_CXX.rsp
CMakeFiles/utils.dir/utils.cpp.obj: ../utils.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /C/Users/sbobovyc/workspace/DCS/DCS/src/utils/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/utils.dir/utils.cpp.obj"
	/C/MinGW/bin/g++.exe   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/utils.dir/utils.cpp.obj -c /C/Users/sbobovyc/workspace/DCS/DCS/src/utils/utils.cpp

CMakeFiles/utils.dir/utils.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/utils.dir/utils.cpp.i"
	/C/MinGW/bin/g++.exe  $(CXX_DEFINES) $(CXX_FLAGS) -E /C/Users/sbobovyc/workspace/DCS/DCS/src/utils/utils.cpp > CMakeFiles/utils.dir/utils.cpp.i

CMakeFiles/utils.dir/utils.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/utils.dir/utils.cpp.s"
	/C/MinGW/bin/g++.exe  $(CXX_DEFINES) $(CXX_FLAGS) -S /C/Users/sbobovyc/workspace/DCS/DCS/src/utils/utils.cpp -o CMakeFiles/utils.dir/utils.cpp.s

CMakeFiles/utils.dir/utils.cpp.obj.requires:
.PHONY : CMakeFiles/utils.dir/utils.cpp.obj.requires

CMakeFiles/utils.dir/utils.cpp.obj.provides: CMakeFiles/utils.dir/utils.cpp.obj.requires
	$(MAKE) -f CMakeFiles/utils.dir/build.make CMakeFiles/utils.dir/utils.cpp.obj.provides.build
.PHONY : CMakeFiles/utils.dir/utils.cpp.obj.provides

CMakeFiles/utils.dir/utils.cpp.obj.provides.build: CMakeFiles/utils.dir/utils.cpp.obj

# Object files for target utils
utils_OBJECTS = \
"CMakeFiles/utils.dir/utils.cpp.obj"

# External object files for target utils
utils_EXTERNAL_OBJECTS =

libutils.dll: CMakeFiles/utils.dir/utils.cpp.obj
libutils.dll: CMakeFiles/utils.dir/build.make
libutils.dll: CMakeFiles/utils.dir/objects1.rsp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX shared library libutils.dll"
	"/c/Program Files (x86)/CMake 2.8/bin/cmake.exe" -E remove -f CMakeFiles/utils.dir/objects.a
	/C/MinGW/bin/ar.exe cr CMakeFiles/utils.dir/objects.a @CMakeFiles/utils.dir/objects1.rsp
	/C/MinGW/bin/g++.exe     -shared -o libutils.dll -Wl,--out-implib,libutils.dll.a -Wl,--major-image-version,0,--minor-image-version,0 -Wl,--whole-archive CMakeFiles/utils.dir/objects.a -Wl,--no-whole-archive -L/c/Users/sbobovyc/Desktop/libnoise/noise/src/.libs -lnoise -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32 

# Rule to build all files generated by this target.
CMakeFiles/utils.dir/build: libutils.dll
.PHONY : CMakeFiles/utils.dir/build

CMakeFiles/utils.dir/requires: CMakeFiles/utils.dir/utils.cpp.obj.requires
.PHONY : CMakeFiles/utils.dir/requires

CMakeFiles/utils.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/utils.dir/cmake_clean.cmake
.PHONY : CMakeFiles/utils.dir/clean

CMakeFiles/utils.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MSYS Makefiles" /C/Users/sbobovyc/workspace/DCS/DCS/src/utils /C/Users/sbobovyc/workspace/DCS/DCS/src/utils /C/Users/sbobovyc/workspace/DCS/DCS/src/utils/build /C/Users/sbobovyc/workspace/DCS/DCS/src/utils/build /C/Users/sbobovyc/workspace/DCS/DCS/src/utils/build/CMakeFiles/utils.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/utils.dir/depend

