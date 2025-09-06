# Fractal Flower Generator

A code base for generating flowers using fractal logic! Python for 2D rendering and C++/OpenGL for 3D rendering. Nature exhibits self-similarity through branching structures, and this can be modeled using recursion. Here, I implement both iterative and recursive algorithms to generate unique flower-like structures.

<img width="309" height="470" alt="Screenshot 2025-09-06 at 12 22 48 PM" src="https://github.com/user-attachments/assets/e41082ea-b267-4068-8017-660af328f90e" />

## Requirements

### Python Version
- **PIL**
- **matplotlib**

### C++ Version
- **C++ Compiler** (GCC 11+, Clang, or MSVC)
- **CMake** (3.10+)
- **OpenGL** (3.0+)
- **GLFW** (for window management)
- **GLAD** (for OpenGL loading)

## Installation

### Python Setup
```bash
git clone https://github.com/dnzy06/fractal-flower.git
cd 2DPlant
pip install -r requirements.txt
python drawPlant.py
```

### C++ Setup

#### macOS
```bash
brew install glfw cmake
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt install build-essential cmake libglfw3-dev libglm-dev
```

#### Build Instructions
```bash
mkdir build && cd build
cmake ..
make
./draw3DPlant
```
