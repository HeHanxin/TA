## Unity Shader

### 语义

##### Vertex Shader Input Semantics

* POSITION
  * float3/float4
  * 表示模型的顶点坐标
* NORMAL
  * float3
  * 表示模型的法线
* TEXCOORD0~N
  * float2/float3/float4
  * TEXCOORD0表示第一套UV，TEXCOORDN表示第N-1套UV

* TANGENT
  * float4
  * 表示模型的切线

* COLOR
  * float
  * 表示模型的顶点颜色

##### Vertex Shader Output Semantics/Fragment Shader Input Semantics

* Semantics
  * SV_POSITION
    * float4
    * 表示模型顶点在裁剪空间中的坐标
  * TEXCOORD0~N
    * float4
    * 用来保存高精度数据，例如纹理坐标，位置坐标
    * 插值器（interpolator)
      * OpenGL ES 2.0 / DX9 Shader Model 2.0 : 8个
      * DX9 Shader Model 3.0：10个
      * OpenGL ES 3.0 / Metal : 16个
      * DX10 Shader Model 4.0：32个
  * COLOR0~N
    * fixed4
    * 用来表示低精度数据，比如0~1之间的颜色值
* Vertex Shader中输出值将按照三角面片进行插值，随后作为Fragment Shader的输入

##### Fragment Shader Output Semantics

* SV_Target0~N
  * float4/fixed4
  * 表示片元最终颜色，一般很少用到SV_Target1这些输出，SV_Target0等价于SV_Target
* SV_Depth
  * float
  * 输出片元深度值
  * 会有性能损耗，一般很少用

##### 精度

* float：32bit
* half：16bit，用来存储颜色、单位矢量等
* fixed：11bit，目前在基本不用在移动平台，会被当作half对待

### Unity Shader Model

* #pragma target 2.0
  * DX9 Shader Model 2.0，适用于Unity支持的所有平台
  * 8个插值器
  * 有限数量的算术和纹理指令，没有顶点纹理采样，没有显式的LOD纹理采样，片元着色器中没有衍生指令
* #pragma target 2.5（默认值）
  * 几乎与target 3.0相同
  * 8个插值器
  * 没有显示的LOD纹理采样
* #pragma target 3.0
  * DX9 Shader Model 3.0：衍生指令，纹理LOD采样，允许更多的算术/纹理指令，10个插值器
  * 某些 OpenGL ES 2.0 设备可能无法完全支持，具体取决于存在的驱动程序扩展和使用的功能
* #pragma target 3.5（或 es3.0）
  * OpenGL ES 3.0 功能（D3D 平台上的 DX10 SM4.0，只是没有几何着色器）
  * 在 DX11 9.x (WinPhone) 和 OpenGL ES 2.0 上不支持
  * 在 DX11+、OpenGL 3.2+、OpenGL ES 3+、Metal、Vulkan 和 PS4/XB1 游戏主机上支持

* #pragma target 4.0
  * DX11 Shader Model 4.0
  * 在 DX11 9.x (WinPhone)、OpenGL ES 2.0/3.0/3.1 和 Metal 上不支持
  * 在 DX11+、OpenGL 3.2+、OpenGL ES 3.1+AEP、Vulkan 和 PS4/XB1 游戏主机上支持
  * 具有几何着色器以及 es3.0 目标所具有的一切功能
* #pragma target 4.5（或 es3.1）
  * OpenGL ES 3.1 功能（D3D 平台上的 DX11 SM5.0，只是没有曲面细分着色器）
  * 在早于 SM5.0 的 DX11、早于 4.3 的 OpenGL（即 Mac）和 OpenGL ES 2.0/3.0 上不支持
  * 在 DX11+ SM5.0、OpenGL 4.3+、OpenGL ES 3.1、Metal、Vulkan 和 PS4/XB1 游戏主机上支持
  * 有Compute Shader、随机访问纹理写入、原子等。没有几何着色器和曲面细分着色器
* #pragma target 4.6（或 gl4.1）
  * OpenGL 4.1 功能（D3D 平台上的 DX11 SM5.0，只是没有计算着色器）。Mac 支持的最高 OpenGL 级别。
  * 在早于 SM5.0 的 DX11、早于 4.1 的 OpenGL、OpenGL ES 2.0/3.0/3.1 和 Metal 上不支持
  * 在 DX11+ SM5.0、OpenGL 4.1+、OpenGL ES 3.1+AEP、Vulkan、Metal（不含几何体）和 PS4/XB1 游戏主机上支持。

* #pragma target 5.0
  * DX11 Shader Model 5.0
  * 在早于 SM5.0 的 DX11、早于 4.3 的 OpenGL（即 Mac）、OpenGL ES 2.0/3.0/3.1 和 Metal 上不支持。
  * 在 DX11+ SM5.0、OpenGL 4.3+、OpenGL ES 3.1+AEP、Vulkan、Metal（不含几何体）和 PS4/XB1 游戏主机上支持。

[返回目录](https://hehanxin.github.io/TA/index)