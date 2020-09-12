## 颜色空间

#### Linear Space Workflow

###### sRGB

* 颜色纹理为了满足显示要求，通常是保存在经过Gamma校正的sRGB空间

###### Linear Space工作流

* 着色器中读取sRGB纹理时，使用GPU的sRGB采样器将纹理从Gamma空间反校正到线性空间，在输出到帧缓存时转换回sRGB的Gamma空间
* 通过在线性空间中正确地进行照明和其它计算，可以得到更高的视觉保真度
* OpenGL ES 3.0支持

[返回目录](https://hehanxin.github.io/TA/index)