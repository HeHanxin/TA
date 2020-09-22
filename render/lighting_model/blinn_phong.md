## Blinn-Phong

$$
Ispecular = Ks * Id * (dot(N, H))^E
$$

Ks：镜面反射系数

Id：直接光源强度

E：高光指数

N：顶点的单位法向量

H：单位半角向量 H =（L+V/|L+V|）

```
//vertex shader
uniform mat4 u_matObjectToWorld;
uniform mat4 u_matWorldToClip;
uniform mat4 u_matObjectToWorldNormal;

attribute vec3 a_position;
attribute vec2 a_texCoord;
attribute vec3 a_normal;

varying vec2 v_texCoord;
varying vec3 v_normal;
varying vec3 v_reflectDir;

void main()
{
	vec4 worldPosition = u_matObjectToWorld * vec4(a_position, 1.0);
	gl_Position = u_matWorldToClip * worldPosition;
	
	v_normal = u_matObjectToWorldNormal * a_normal;
	v_texCoord = v_texCoord;
	v_reflectDir = reflect(u_lightDir, v_normal);
}

//pixel shader
uniform sampler2D u_texDiffuse;
uniform vec3 u_lightIntensity;
uniform vec3 u_viewDir;
uniform vec3 u_lightDir;
uniform float u_specExp;

varying vec2 v_texCoord;
varying vec3 v_normal;
varying vec3 v_reflectDir;

void main()
{
	vec4 baseColor = texture2D(u_texDiffuse, v_texCoord);
	float diffuse = max(dot(v_normal, u_lightDir), 0.0);
	vec3 halfVec = normalize(u_lightDir + u_viewDir);
	float specular = pow(max(dot(v_normal, halfVec), 0.0), u_specExp);
	
	gl_FragColor = (diffuse * baseColor + specular) * u_lightIntensity;
}
```

[返回目录](https://hehanxin.github.io/TA/index)