## 渲染管线 

#### 应用程序阶段

##### 准备数据

* vertex buffer : position, uv1, uv2, color, normal, tangent ...
* index buffer
* texture
* uniform
* other
  * state
  * command

##### 提交drawcall

* cpu runtime
  * 提交数据、状态、命令
  * check state
* user mode driver
  * check state
  * 编译成GPU能执行的微码流
  * 与应用程序同一个进程
* kernel mode driver
  * 全系统只有一个
  * 在不同的应用程序之间协调GPU资源
  * 可通过总线向GPU发送绘制数据
* 总线
  * kernel mode driver通过总线向GPU发送数据
  * 有一定带宽
* GPU
  * 执行绘制命令
  * 储存绘制数据、渲染状态

#### 几何阶段

##### 顶点着色器

* 主要作用
  * 顶点数据的读取，计算各顶点在裁剪空间中的位置
  * 向pixel shader传递数据，如uv和不需要逐像素处理的数据
* 空间变换
  * 模型空间 -> 世界空间 -> 观察空间 -> 裁剪空间
  * 法线变换到世界空间
  * 投影矩阵
    * 透视投影
      * fov, aspect(width/height), zNear, zFar
      * 近大远小
    * 正交投影
      * left, right, bottom, top, near, far
      * 恒等变换
    * 应用
      * 可以在投影矩阵上直接修改深度值
      * 通过在投影矩阵上乘以一个矫正矩阵可以实现投影后的平移
* 其它
  * tangent.w

##### 几何着色器

* 创建和销毁点线面
* OpenGL ES 3.2或OpenGL ES 3.1 + AEP

##### 视锥体裁剪

* 根据视锥体进行裁剪
* 产生新的顶点

##### 屏幕坐标映射

* 投影到屏幕空间来生成2d坐标

#### 光栅化阶段

* 将三角面转换为片元，为下一步进行片元着色提供数据
* 像素填充率
  * GPU每一帧之内向帧缓存写入的像素的数量
  * 影响像素填充率的因素
    * 屏幕分辨率
    * overdraw
* 锯齿
  * 由光栅化引起
  * 抗锯齿
    * MSAA
      * OpenGL内建
      * NXMSAA：为每个像素添加N个采样点，根据三角面覆盖采样点的情况来决定像素的颜色
      * 三角形的硬边被比实际颜色浅一些的颜色所包围，因此观察者从远处看上去比较平滑
      * 采样点的数量是任意的，更多的采样点能带来更精确的覆盖率
      * 延迟渲染不支持
        * MSAA流程所有缓冲区都变成了原来的N倍，增加了显存和带宽消耗

#### 像素处理阶段

##### 片元着色器

* 计算每一个片元的颜色

##### 片元处理

###### 阶段

* scissor test：限制绘制区域
* alpha test
  * alpha test打断Early-Z：Early-Z通过后需要执行写深度操作
  * 由于alpha test会打断Early-Z，会重新执行一次完整的depth test，产生额外的消耗，因此移动平台慎用
* stencil test：提供一个8bit的stencil buffer
* depth test
* blending
  * tranditional transparency：Blend SrcAlpha OneMinusSrcAlpha
  * premultiplied transparency：Blend One OneMinusSrcAlpha
  * Additive：Blend SrcAlpha One
  * Soft Additive：Blend OneMinusDstColor One
* Dithering

###### 渲染顺序

* 由于Early-Z的存在，不透明物体从前往后渲染，可以避免深度覆盖的像素重复绘制
* 透明物体从后往前渲染，保证计算的正确性

[返回目录](https://hehanxin.github.io/TA/index)