## Rendering Performance

##### CPU Render

* Drawcall
  * 合批中避免频繁重建batch
  * 合理降低drawcall
* UI
  * 动静态分离
  * 血条
  * 动态图集

##### GPU Render

* Shading
  * Texture cache miss
    * 不是按照顶点shader插值的uv读取贴图会破坏tex缓存导致cache经常thrashed，因为基本不会命中，还会导致缓存经常被刷新。
    * 贴图不能过大贴图太大，导致贴图cache超载，使得cache不能命中
    * 贴图格式尽量小
    * Tiled Rasterization会有助于在光栅化时命中Cache，避免三角形过大和光栅化与贴图方向不同产生的cache miss/page break问题
    * 使用mipmap
    * 压缩贴图可以节省带宽，并且因为cache中存储的是压缩的texel，所以能增加tex cache中存储texel的数量，因为解压缩是在数据出tex cache后在tex unit中进行的。
  * Vertex shader
    * 根据实际情况，尽量将大多数可以在顶点着色器中处理的数据放到顶点着色器中进行
  * 指令数

[返回目录](https://hehanxin.github.io/TA/index)