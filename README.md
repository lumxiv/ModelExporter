# ModelExporter
Export models frame by frame to gltf for use in VFXEditor

## Requirements
- [Blender 5.2](https://www.blender.org/)
- [VFXEditor](https://github.com/0ceal0t/Dalamud-VFXEditor)

## Installation
Download the addon from the [releases](https://github.com/lumxiv/ModelExporter/releases).  
Go to `Edit > Preferences > Add-ons > Install From Disk...` and select the entire `.zip` file. Make sure to enable the add-on as well.

> Note on updating: you may need to uninstall the add-on, restart Blender, and then re-install it
<img width="661" height="552" alt="blender_CvvK5zAQlx" src="https://github.com/user-attachments/assets/0ef01974-d70f-4a2e-b648-16f517fc94d1" />

## Overview
<img width="245" height="168" alt="blender_PPKORKTFYT" src="https://github.com/user-attachments/assets/95480104-9574-40e8-8862-a74a69d9bf38" />

Clicking export will generate as many .glb as specified by the start - end frame range  
Each will be named after where it's supposed to go in VFXEditor, assuming 8 models per particle:  
<img width="228" height="307" alt="explorer_btZTCjPGrd" src="https://github.com/user-attachments/assets/065b0221-a8a0-4336-bc5b-663edc29e0de" />


`particle x - model y - (frame z)`  


x being the particle count  
<img width="557" height="152" alt="ffxiv_dx11_h8THNc0wIB" src="https://github.com/user-attachments/assets/d0057c37-42be-4f9b-a5bf-3ed81126764f" />  

y being the model count (inside model particle)  
<img width="715" height="227" alt="ffxiv_dx11_tiknuGQ4Ji" src="https://github.com/user-attachments/assets/71f095f4-9e64-49ee-91b9-ea3bb39ca7ba" />  

z being the frame captured, for reference
