cmake_minimum_required(VERSION 3.10)

project(draw3DPlant)

add_executable(draw3DPlant src/draw3DPlant.cpp src/draw3DPlant.h src/glad.c)

target_include_directories(draw3DPlant PRIVATE dependencies)

find_package(glfw3 REQUIRED)

find_package(OpenGL REQUIRED)

target_link_libraries(draw3DPlant glfw OpenGL::GL)