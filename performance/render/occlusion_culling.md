### 遮挡剔除

* 预计算原始的PVS（UE4)
  * 运行时消耗低，但无法处理动态模型的剔除，可见性烘培的时间较长，需要额外的占用内存

* Umbra的dPVS(Unity)
  * 烘焙速度快，但CPU实际开销不稳定，不支持Steaming大世界，内存开销较大
  * 离线下是不计算所有可见性的，而只是生成一个空间数据结构，也就是一个BSP描述的节点信息，用于之后的空间位置查询。因此它在离线计算的时候速度可以提升很多，但是在线消耗会提升

[返回目录](https://hehanxin.github.io/TA/index)