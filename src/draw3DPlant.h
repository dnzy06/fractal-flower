#include <iostream>
#include <cmath>
#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <random>
#include <queue>

#ifndef draw3DPlant_H
#define draw3DPlant_H

class draw3DPlant {
public:
    void mouse_callback(GLFWwindow* window, double xpos, double ypos);
    void drawBranch(float radius, float length, bool endBranch);
    void createRandomQueues(std::queue<int>& randomAngles, std::queue<float>& randomLengths, float currLength, int depth);
    void drawPlant(float radius, int depth, std::queue<int>& randomAngles, std::queue<float>& randomLengths);
    int main();
};

#endif 
