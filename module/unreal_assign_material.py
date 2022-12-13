import unreal

def set_sk_materials(path_to_sk, materials_to_change):
    """
    path_to_sk = "/Game/Meshes/Bob"
    materials_to_change = {"mat_head": unreal.load_asset("/Game/Materials/mi_head")}
    """
    skeletal_mesh = unreal.load_asset(path_to_sk)
    skeletal_mesh_materials = skeletal_mesh.materials

    material_array = unreal.Array(unreal.SkeletalMaterial)
    for material in skeletal_mesh_materials:
        new_sk_material = unreal.SkeletalMaterial()

        slot_name = material.get_editor_property("material_slot_name")
        material_interface = material.get_editor_property("material_interface")

        if materials_to_change.get(str(slot_name)):
            material_interface = materials_to_change[str(slot_name)]

        new_sk_material.set_editor_property("material_slot_name", slot_name)
        new_sk_material.set_editor_property("material_interface", material_interface)

        material_array.append(new_sk_material)

    skeletal_mesh.set_editor_property("materials", material_array)

def assign_material():
    path_to_sk = '/Game/Characters/Guy/Default'
    shader_head_shader = {'shader_head_shader': unreal.load_asset('/Game/MetaHumans/Guy/Face/Materials/Baked/MI_HeadSynthesized_Baked')}
    shader_teeth_shader = {'shader_teeth_shader': unreal.load_asset('/Game/MetaHumans/Guy/Materials/M_TeethCharacterCreator_Inst')}
    shader_saliva_shader = {'shader_saliva_shader': unreal.load_asset('/Game/MetaHumans/Common/Face/Materials/MI_lacrimal_fluid_Inst')}
    shader_eyeLeft_shader = {'shader_eyeLeft_shader': unreal.load_asset('/Game/MetaHumans/Guy/Face/Materials/MI_EyeRefractive_Inst_L')}
    shader_eyeRight_shader = {'shader_eyeRight_shader': unreal.load_asset('/Game/MetaHumans/Guy/Face/Materials/MI_EyeRefractive_Inst_R')}
    shader_eyeshell_shader = {'shader_eyeshell_shader': unreal.load_asset('/Game/MetaHumans/Common/Face/Materials/MI_EyeOcclusion_Inst')}
    shader_eyelashes_shader = {'shader_eyelashes_shader': unreal.load_asset('/Game/MetaHumans/Guy/Materials/M_EyelashLowerLODs_Inst')}
    shader_eyeEdge_shader = {'shader_eyeEdge_shader': unreal.load_asset('/Game/MetaHumans/Common/Face/Materials/MI_lacrimal_fluid_Inst')}

    set_sk_materials(path_to_sk, shader_head_shader)
    set_sk_materials(path_to_sk, shader_teeth_shader)
    set_sk_materials(path_to_sk, shader_saliva_shader)
    set_sk_materials(path_to_sk, shader_eyeLeft_shader)
    set_sk_materials(path_to_sk, shader_eyeRight_shader)
    set_sk_materials(path_to_sk, shader_eyeshell_shader)
    set_sk_materials(path_to_sk, shader_eyelashes_shader)
    set_sk_materials(path_to_sk, shader_eyeEdge_shader)
