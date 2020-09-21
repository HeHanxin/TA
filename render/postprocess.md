## 后处理

##### Bloom

* Pre-filter
  * 获取像素颜色亮度
  * 过滤出亮度超过阈值的部分
* Down sample
  * 用若干个pass做down sample
  * 每次down sample的rt的分辨率为上一次的1/2或1/4
  * down sample的过程是与周围像素做加权平均的过程（blur)
* Up sample
  * 用若干个pass做up sample
  * up sample的过程是用上一级的down sample结果与最后一个处理的render target模糊后的结果进行叠加
* Combine
  * 最后一次up sample结果与周围做加权平均后，再与原图做叠加，得到最终bloom结果

```
伪代码
void render()
{
	//pre filter
	SetRenderTarget(prilter_rt);
	prefilterShader->SetMainTexture(sceneTexture);
	prefilterShader->Drawbuffer();
	auto& last = prilter_rt;
	
	//down sample
	for(int level = 0; level < iterations; ++level)
	{
		SetRenderTarget(downsample_rt[level]);
		downsampleShader->SetBlurTexture(last);
		downsampleShader->DrawBuffer();
		last = downsample_rt[level];
	}
	
	//up sample
	for(int level = iterations-2; i >=0; --level)
	{
		SetRenderTarget(upsample_rt[level]);
		upsampleShader->SetMainTexture(last);
		upsampleShader->SetBlurTexture(downsample_rt[level])
		upsampleShader->DrawBuffer();
		last = upsample_rt[level];
	}
	
	//uber
	SetRenderTarget(final_rt);
	uberShader->SetBlurTexture(last);
	uberShader->SetMainTexture(sceneTexture);
}
```

##### Color Grading

* White Balance
  * Temperature
* Tone
  * Exposure
  * Color Filter
  * Hue Shift
  * Saturation
  * Brightness
  * Contrast
* Channel Mixer
  * R/G/B Channel Tint

##### Depth Of Field

* 相机中光圈与景深的关系

  <img src="https://pic1.zhimg.com/80/v2-c70f73d67a323a87c0e0921757f3679c_720w.jpg?source=1940ef5c" alt="img" style="zoom: 67%;" />

* 后处理中的景深

  * near
  * far
  * near < focus < far

##### God Ray

* Raidal Blur Postprocessing
  * 提取高光->径向模糊->增大模糊半径再次镜像模糊->与原图叠加

##### Lens Flare



##### Screen Space Reflection

* 在Screen Space上根据Gbuffer normal获得反射方向做depth ray march，得到Hit坐标点的color

* 生成blur过的mipmap，根据roughness选择mipmap

* 仅在延迟渲染中使用，依赖Gbuffer中的法线

  

[返回目录](https://hehanxin.github.io/TA/index)