## Animation

##### 骨骼

* 互相连接的骨骼组成骨架结构，通过改变骨骼的朝向和位置来生成动画

##### 蒙皮

* 蒙皮是指把**Mesh的顶点附着（绑定）在骨骼上**，并且每个顶点可以被多个骨骼控制，这样在关节处的顶点由于同时受到父子骨骼的拉扯而改变位置从而消除了缝隙

* 顶点的**蒙皮信息**包含了**顶点受哪些骨骼影响**以及这些**骨骼影响该顶点的权重**

##### 顶点着色器

```
mat4 blendMatrix = mat4(1.0);
blendMatrix = a_boneWeight.x * u_matPalette[int(a_boneIndex.x)];
blendMatrix += a_boneWeight.y * u_matPalette[int(a_boneIndex.y)];
blendMatrix += a_boneWeight.z * u_matPalette[int(a_boneIndex.z)];
blendMatrix += a_boneWeight.w * u_matPalette[int(a_boneIndex.w)];
```

##### CPU Skin

* 引擎希望在骨骼动画中加入一些复杂的如动作融合， 骨骼部位分离动画，IK，重定向，骨骼蒙版，跟骨骼动画等等复杂的动作机制，来表现更高质量的动作表现

##### GPU Skin

* GPU Skin和GPU Instancing
  * 同一种类的怪物，不管他们做什么动作，他们在做动作的某一帧，他们输送给GPU的数据其实是几乎一样的，都是一份相同的处于T-POSE的顶点buffer，那么不同的只是每个角色当前处于的动作帧。
* 沙盒引擎GPU Skin计算过程
  * CPU计算FinalMatrixList，包含当前帧动画中各骨骼的变换矩阵
  * vertex buffer中包含了影响当前顶点的骨骼id，以及各骨骼id对当前顶点影响的权重值
  * 在vertex shader中，通过加权平均来计算动画的融合矩阵

* GPU Skin
  * 把每个顶点每一帧的位置输出到贴图上