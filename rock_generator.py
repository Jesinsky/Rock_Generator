import bpy
import random


class RockGenerator(bpy.types.Operator):
    bl_idname = "object.rock_generator"
    bl_label = "Rock Generator"

    def execute(self, context):
        
        #add a cube
        bpy.ops.mesh.primitive_cube_add()
        so = bpy.context.active_object

        #smooth the object
        bpy.ops.object.shade_smooth()

        #random shape object
        num1 = random.randint(3, 5)
        num2 = random.randint(4, 5)
        bpy.ops.object.editmode_toggle()
        bpy.ops.transform.vertex_random(offset=num1, seed=num2)


        #create subdivision surface modifiers
        mod_subsurf = so.modifiers.new("My Modifier", 'SUBSURF')

        #change modifier value
        mod_subsurf.levels = 5  #MagicNumber

        #create displacement modifier
        mod_displace = so.modifiers.new("My Displacement", 'DISPLACE')
        mod_displace.strength = 0.7 #MagicNumber

        #create the texture
        new_tex = bpy.data.textures.new("My Texture", 'VORONOI')

        #change the texture settings
        new_tex.noise_scale = 1.2 #MagicNumber
        new_tex.noise_intensity = 0.8 #MagicNumber

        #assign the texture to displacement modifier
        mod_displace.texture = new_tex

        #create a decimate modifier
        mod_decimate = so.modifiers.new("My Decimate", 'DECIMATE')
        mod_decimate.ratio = 0.129496 #MagicNumber

        #create a bevel modifier
        mod_bevel = so.modifiers.new("My Bevel", 'BEVEL')
        mod_bevel.segments = 2 #MagicNumber  
        
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(RockGenerator.bl_idname, text=RockGenerator.bl_label)

# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access)
def register():
    bpy.utils.register_class(RockGenerator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(RockGenerator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.rock_generator()
