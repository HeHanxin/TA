## Screen Space Reflection

* 在Screen Space上根据Gbuffer normal获得反射方向做depth ray march，得到Hit坐标点的color

* 生成blur过的mipmap，根据roughness选择mipmap

* 仅在延迟渲染中使用，依赖Gbuffer中的法线

[返回目录](https://hehanxin.github.io/TA/index)