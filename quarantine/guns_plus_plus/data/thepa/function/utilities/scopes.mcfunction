
#we back again

item modify entity @s[scores={gz_id=53,gz_bullets=1..},nbt={SelectedItem:{components:{"minecraft:custom_data":{gz_data:{}}}}}] weapon.mainhand {"type":"minecraft:set_components","components":{"minecraft:equippable":{"camera_overlay":"scopes/acogscope","slot":"mainhand"}}}

item modify entity @s[scores={gz_id=19,gz_bullets=1..},nbt={SelectedItem:{components:{"minecraft:custom_data":{gz_data:{}}}}}] weapon.mainhand {"type":"minecraft:set_components","components":{"minecraft:equippable":{"camera_overlay":"scopes/rpgscope","slot":"mainhand"}}}


execute if predicate {terms:[{entity:"this",scores:{gz_id:11},type:"minecraft:entity_scores"},{type:"minecraft:entity_scores",entity:"this",scores:{gz_id:30}},{type:"minecraft:entity_scores",entity:"this",scores:{gz_id:22}},{type:"minecraft:entity_scores",entity:"this",scores:{gz_id:38}},{type:"minecraft:entity_scores",entity:"this",scores:{gz_id:42}},{type:"minecraft:entity_scores",entity:"this",scores:{gz_id:21}},{type:"minecraft:entity_scores",entity:"this",scores:{gz_id:36}},{type:"minecraft:entity_scores",entity:"this",scores:{gz_id:41}},{type:"minecraft:entity_scores",entity:"this",scores:{gz_id:43}},{type:"minecraft:entity_scores",entity:"this",scores:{gz_id:46}},{type:"minecraft:entity_scores",entity:"this",scores:{gz_id:51}},{type:"minecraft:entity_scores",entity:"this",scores:{gz_id:56}}],type:"minecraft:any_of"} run item modify entity @s[nbt={SelectedItem:{components:{"minecraft:custom_data":{gz_data:{}}}}},scores={gz_bullets=1..}] weapon.mainhand {"type":"minecraft:set_components","components":{"minecraft:equippable":{"camera_overlay":"scopes/sniperscope","slot":"mainhand"}}}
