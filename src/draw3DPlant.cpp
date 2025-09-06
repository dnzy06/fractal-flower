#include "draw3DPlant.h"

// Mouse rotation variables
float rotZ = 0.0f;
float rotY = 0.0f;
double lastMouseX = 320;
double lastMouseY = 240;

// Mouse callback function
void mouse_callback(GLFWwindow* window, double xpos, double ypos) {
    // Calculate how much mouse moved
    double deltaX = xpos - lastMouseX;
    double deltaY = ypos - lastMouseY;
    
    // Update rotation based on mouse movement
    rotZ += deltaX * 0.5f;  // Horizontal mouse = rotate around Y axis
    rotY += deltaY * 0.5f;  // Vertical mouse = rotate around X axis
    
    // Remember current mouse position
    lastMouseX = xpos;
    lastMouseY = ypos;
}

void drawBranch(float radius, float length, bool endBranch) {
    int segments = 12;
    if (endBranch) {
    }

    glBegin(GL_TRIANGLES);
        glColor3f(0.27f, 0.49f, 0.25f);
        if (endBranch) {
            glColor3f(1.0f, 0.0f, 0.0f);  // red
        }
        
        // Draw cylinder sides
        for (int i = 0; i < segments; i++) {
            float angle1 = (i * 2.0f * 3.14159f) / segments;
            float angle2 = ((i + 1) * 2.0f * 3.14159f) / segments;
            
            float x1 = radius * cos(angle1);
            float y1 = radius * sin(angle1);
            float x2 = radius * cos(angle2);
            float y2 = radius * sin(angle2);
            
            // Two triangles per segment
            glVertex3f(x1, y1, 0.0f);  // Bottom
            glVertex3f(x2, y2, 0.0f);  // Bottom
            glVertex3f(x1, y1, length);   // Top
            
            glVertex3f(x2, y2, 0.0f);  // Bottom
            glVertex3f(x2, y2, length);   // Top
            glVertex3f(x1, y1, length);   // Top
        }
        
        // Draw bottom cap
        for (int i = 0; i < segments; i++) {
            float angle1 = (i * 2.0f * 3.14159f) / segments;
            float angle2 = ((i + 1) * 2.0f * 3.14159f) / segments;
            
            float x1 = radius * cos(angle1);
            float y1 = radius * sin(angle1);
            float x2 = radius * cos(angle2);
            float y2 = radius * sin(angle2);
            
            glVertex3f(0.0f, 0.0f, 0.0f);  // Center bottom
            glVertex3f(x1, y1, 0.0f);      // Edge point 1
            glVertex3f(x2, y2, 0.0f);      // Edge point 2
        }
        
        // Draw top cap
        for (int i = 0; i < segments; i++) {
            float angle1 = (i * 2.0f * 3.14159f) / segments;
            float angle2 = ((i + 1) * 2.0f * 3.14159f) / segments;
            
            float x1 = radius * cos(angle1);
            float y1 = radius * sin(angle1);
            float x2 = radius * cos(angle2);
            float y2 = radius * sin(angle2);
            
            glVertex3f(0.0f, 0.0f, length);   // Center top
            glVertex3f(x2, y2, length);       // Edge point 2
            glVertex3f(x1, y1, length);       // Edge point 1
        }
    glEnd();
}

void createRandomQueues(std::queue<int>& randomAngles, std::queue<float>& randomLengths, float currLength, int depth) {
    std::random_device rseed;
    std::mt19937 rng(rseed());
    std::uniform_int_distribution<int> dist(-9,9);

    if (depth <= 0) {
        return;
    }

    randomLengths.push(currLength);
    randomAngles.push(18 + dist(rng));
    randomAngles.push(rand() % 360);
    createRandomQueues(randomAngles, randomLengths, currLength * (0.5 + static_cast <float> (rand()) /( static_cast <float> (RAND_MAX/(0.7-0.5)))), depth-1);

    randomAngles.push(-18 + dist(rng));
    randomAngles.push(rand() % 360);
    createRandomQueues(randomAngles, randomLengths, currLength * (0.5 + static_cast <float> (rand()) /( static_cast <float> (RAND_MAX/(0.7-0.5)))), depth-1);

    randomAngles.push(0);
    randomAngles.push(rand() % 360);
    createRandomQueues(randomAngles, randomLengths, currLength * (0.5 + static_cast <float> (rand()) /( static_cast <float> (RAND_MAX/(0.7-0.5)))), depth-1);
}

void drawPlant(float radius, int depth, std::queue<int>& randomAngles, std::queue<float>& randomLengths) {

    if (depth <= 0) {
        return;
    }

    bool endBranch = false;
    if (depth == 1) {
        endBranch = true;
        // std::cout << "hi" << std::endl;
    }

    glPushMatrix();

    float length = randomLengths.front();
    randomLengths.pop();

    if (length < 0.1) {
        length = 0.1;
    }

    drawBranch(radius, length, endBranch);

    float newRadius = radius;
    if (radius > 0.01f) {
        newRadius = radius - 0.005f;
    }
    
    // branch 1

    glTranslatef(0.0f, 0.0f, length);
    glRotatef(randomAngles.front(), 0.0f, 1.0f, 0.0f);
    glRotatef(-18, 1.0f, 0.0f, 0.0f);
    randomAngles.pop();
    glRotatef(randomAngles.front(), 0.0f, 0.0f, 1.0f);
    randomAngles.pop();
    drawPlant(newRadius, depth-1, randomAngles, randomLengths);
    glPopMatrix();

    glPushMatrix();

    // branch 2

    glTranslatef(0.0f, 0.0f, length);
    glRotatef(randomAngles.front(), 0.0f, 1.0f, 0.0f);
    glRotatef(0, 1.0f, 0.0f, 0.0f);
    randomAngles.pop();
    glRotatef(randomAngles.front(), 0.0f, 0.0f, 1.0f);
    randomAngles.pop();
    drawPlant(newRadius, depth-1, randomAngles, randomLengths);
    glPopMatrix();

    glPushMatrix();

    // branch 3

    glTranslatef(0.0f, 0.0f, length);
    glRotatef(randomAngles.front(), 0.0f, 1.0f, 0.0f);
    glRotatef(18, 1.0f, 0.0f, 0.0f);
    randomAngles.pop();
    glRotatef(randomAngles.front(), 0.0f, 0.0f, 1.0f);
    randomAngles.pop();
    drawPlant(newRadius, depth-1, randomAngles, randomLengths);
    glPopMatrix();
}

int main() {

    int depth = 10;
    int startingLength = 2.0f;

    std::queue<int> randomAngles;
    std::queue<float> randomLengths;

    createRandomQueues(randomAngles, randomLengths, startingLength, depth);

    // Initialize GLFW
    if (!glfwInit()) {
        return -1;
    }

    // Create window
    GLFWwindow* window = glfwCreateWindow(800, 800, "3D Plant", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);
    
    // Initialize GLAD
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        return -1;
    }

    // Enable depth testing for 3D
    glEnable(GL_DEPTH_TEST);
    
    // Set mouse callback
    glfwSetCursorPosCallback(window, mouse_callback);

    // Main loop
    while (!glfwWindowShouldClose(window)) {
        glfwPollEvents();
        
        // Clear screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        glClearColor(1.0f, 1.0f, 1.0f, 1.0f);  // white background

        // Set up 3D projection
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, 30.0);

        // Set up 3D view
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        glTranslatef(0.0f, 0.0f, -9.0f);  // Move camera back
        
        // Apply mouse rotations
        glRotatef(rotZ, 1.0f, 0.0f, 0.0f);  // Rotate around X axis
        glRotatef(rotY, 0.0f, 1.0f, 0.0f);  // Rotate around Y axis

        // Draw a 3D cylinder (filled)
        float radius = 0.03f;  // Cylinder radius variable
        int segments = 12;    // Number of sides
        
        std::queue<int> currRandomAngles = randomAngles;
        std::queue<float> currRandomLengths = randomLengths;
        drawPlant(radius, depth, currRandomAngles, currRandomLengths);

        glfwSwapBuffers(window);
    }

    glfwTerminate();
    return 0;
}