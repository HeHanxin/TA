## Spherical Harmonics Lighting

* 从拉普拉斯方程到球谐函数

* 球谐函数展开的基底 - 球谐基函数
  * 基底函数一般都是正交函数（函数空间和向量空间广义正交，即内积为0）
* 勒让德多项式
  * 正交多项式
  * 球谐函数中包含了伴随勒让德多项式

* 蒙特卡洛积分法
  * 将数值求解问题转化为求解数学期望的问题
  * 用SH Coefficients来编码低频环境光

```
void SH_Coefficients()
{
    double weight =4.0 * PI;
    //生成n条光线进行采样
    for(int i=0; i<n_samples; ++i) 
    {
    生成带抖动的无偏采样方向(θ,ϕ)
        for(int n=0; n<n_coeff; ++n)
        {
        //对于某一个light probe，它的每个球谐展开系数c_i就要累加起所有的【某方向上的irradiance * 这个方向上SH函数值】
        result[n] += light(θ,ϕ)* samples[i].SH_basis_coeff[n];
        }
    }
    // 把蒙特卡洛积分的常数项乘上去（恒定的采样权重，总采样数）
    double factor = weight / n_samples;
    for(i=0; i<n_coeff; ++i)
    {
        result[i] = result[i] * factor;
    }
}
```

[返回目录](https://hehanxin.github.io/TA/index)