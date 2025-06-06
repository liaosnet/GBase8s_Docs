# Docker版本列表  

更新时间：2025-04-23  
## Docker 版本列表  
- **x86_64架构**   

|**TAG**|**对应版本**|**是否支持k8s部署**|**说明**|  
|:---|:---|:---|:---|  
|v8.8_3513x28_csdk_x64 *|v8.8 3.5.1_3x2_8|是|当前最新版本，latest，包含csdk|
|v8.8_3513x25_csdk_x64|v8.8 3.5.1_3x2_5|是|包含csdk|
|v8.8_3513x13_csdk_x64|v8.8 3.5.1_3x1_3|否|包含csdk|
|v8.8_3513_x64|v8.8 3.5.1_3|否|不含csdk|
|v8.8_3503x1_x64|v8.8 3.5.0_3x1|否|不含csdk|
|v8.8_3331x12_x64|v8.8 3.3.3_1x1_2|否|不含csdk|
|3.3.0_2csdk_amd64|v8.8 3.3.0_2|否|含csdk|
|3.3.0_2_amd64|v8.8 3.3.0_2|否|不含csdk|
|3.0.0_1|v8.8 3.0.0|否|不含csdk|
|v8.8_2201x21_csdk_x64 *|v8.8 2.2.0_1x2_1|否|含csdk|
|v8.8_201a26x41_csdk_x64 *|v8.8 2.0.1a2_6x4_1|否|含csdk|
|2.0.1a2_2|v8.8 2.0.1a2_2|否|不含csdk|

星号（*）表示建议使用版本

- **aarch64架构**  

|**TAG**|**对应版本**|**是否支持k8s部署**|**说明**|  
|:---|:---|:---|:---|  
|v8.8_3633x11_csdk_arm64 *|v8.8 3.6.3_3x1_1|是|含csdk|  
|v8.8_3513x28_csdk_arm64 *|v8.8 3.5.1_3x2_8|是|含csdk|  
|v8.8_3513x13_csdk_arm64|v8.8 3.5.1_3x1_3|否|含csdk|  
|v8.8_3331x1_arm64|v8.8 3.3.3_1x1|否|不含csdk|  
|3.0.0|v8.8 3.0.0|否|不含csdk|  

星号（*）表示建议使用版本  
arm64版本使用了qemu-aarch64-static打包  

## 获取方式  

```shell
docker pull liaosnet/gbase8s:TAG
```