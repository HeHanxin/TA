# OpenGL ES 3.0

* Texturing
  * linear space workflow
    * sRGB Texture 采样器
    * 输出到framebuffer时转换到Gamma Space
  * 2D texture arrays
  * 3D textures
    * 体纹理
  * Depth Buffer可以储存在纹理中
  * Seamless Cubemaps
    * 采样立方体贴图边缘使过渡平滑
  * 浮点纹理
    * 16-bit and filtered
    * 32-bit but not filtered
    * 支持存储超过1的数值
  * ETC2/EAC支持
  * 整型纹理
    * render to and fetch from texture stored as unnormalized signed or unsigned 8-bit, 16-bit, and 32-bit integer texture
  * Texture level of detail
* Shader
  * 二进制存储
  * Non-square matrices
    * 矩阵计算自动补齐（4x3 matrix * 4x4 matrix）
  * Uniform Block
  * Instance and vertex ID
    * 如果使用intance rendering可以访问instance id
  * Fragment Depth
    * 片元着色器可以控制当前片段的深度
  * 放松限制
    * 不再限制指令长度，完整支持循环和分支，支持数组索引 

* Geometry
  * 可以在缓冲区对象中捕捉顶点着色器的输出
  * intanced rendering
* Buffer Objects
  * Uniform buffer objects
  * Vertex array objects
  * Sampler objects
  * Sync objects
  * Pixel buffer objects
    * CPU与GPU之间更加高效的异步数据和纹理传输
  * Buffer object to buffer object copies
    * 更高效的buffer数据拷贝
    * 无需CPU介入

* Framebuffer
  * multiple render targets
  * multisample renderbuffers 
  * Framebuffer invalidation hints
  * New blend equations
    * min/max functions

[返回目录](https://hehanxin.github.io/TA/index)