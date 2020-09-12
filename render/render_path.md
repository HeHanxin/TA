## Render Path

#### Forward Rendering

##### Tranditional Forward Rendering

* shader path number : n个object * m个灯光

##### Unity forward rendering

* render mode设置为not important的光源始终为每顶点或SH光源
* 最亮的方向光始终为每像素光源
* render mode设置为important的光源始终为每像素光源
* 如果上述情况中，光源数少于当前的pixel light count质量设置，则按照亮度降低顺序，更多光源采用每像素渲染方式

##### Tile based forward rendering

* z-pre pass：为了获取深度进行depth bound，但是z-pre pass也会辅助硬件进行early-z
* 将z-buffer分tile，每个tile用compute shader计算depth bound
* 进行lighting cull，得到light index list
* 同forward一样，每个物体走fragment shader，用该fragment所在的tile对应的light index list进行光照的计算

#### Deferred Rendering

##### Tranditional Deferred Rendering

* 作用：解决大量光源产生的计算开销
* 原理
  * 几何处理阶段
    * 将光照计算所需要的各种数据，如位置、法线、贴图颜色等存储到g-buffer上
  * 光照处理阶段
    * 从g-buffer而不是顶点着色器中获取输入变量，根据g-buffer中的数据对屏幕中每一个像素进行光照计算
* 缺点
  * 不支持硬件抗锯齿
    * 现实原因，并非理论上不可实现
    * MSAA流程所有缓冲区都变成了原来的N倍，增加了显存和带宽消耗
    * 延迟渲染使用了多个缓冲区，但各缓冲区的重要性不同
  * 透明渲染问题
    * 需要先渲染不透明物体，透明物体按照forward render的方式渲染
  * g-buffer带来较大的带宽开销
    * multi render target

##### Tile-based Deferred Rendering

* 作用：减少了带宽的占用
* 原理
  * 按照传统延迟渲染的几何处理阶段生成g-buffer
  * 将g-buffer分成tile，每个tile计算出depth bound
  * 进行light culling，得到light index list
  * color pass：使用g-buffer的信息，用该fragment所在的tile的light index list进行绘制

##### Light Pre-pass

#### Real-time ray tracing

* 待补充

[返回目录](https://hehanxin.github.io/TA/index)