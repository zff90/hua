def get_node_coord(node):
    vals=('X','Y','Z')
    coord = base.GetEntityCardValues(deck,node,vals)
    coord = [coord['X'],coord['Y'],coord['Z']]
    return coord
def tans_solder(origin_part,comp_name_new,angle_d,Second_point,pin_num,pin_center):
    base.RotatePart(origin_part,                      #Parts to be rotated
                    transformation_mode="MOVE",       #Parts will be rotated-moved
                    x1=0, y1=0, z1=0,                 #First point to specify the rotation axis
                    x2=Second_point[0], 
                    y2=Second_point[1], 
                    z2=Second_point[2],                #Second point to specify the rotation axis
                    connectivity=True,                 #Connecting nodes will NOT be released
                    ext_connectors="INCLUDE",          #External connections and connectors will also be moved
                    angle=angle_d)                     #Rotation angle
    base.TranslatePart(origin_part,                    #Parts to be translated
                       transformation_mode="MOVE",     #Parts will be translated-moved
                       x=pin_center[0][0], 
                       y=pin_center[0][1],
                       z=pin_center[0][2],           #Translation distance
                       connectivity=True,              #Connecting nodes will be released
                       ext_connectors="INCLUDE")        #External connections and connectors will also be moved
    for i in range(1,pin_num):
        part_name = '{0}_pin_{1}'.format(comp_name_new,i+1)
        part_new = base.NewPart(part_name)
        base.TranslatePart(origin_part,                #Parts to be translated
                       transformation_mode="COPY",     #Parts will be translated-moved
                       x=pin_center[i][0]-pin_center[0][0], 
                       y=pin_center[i][1]-pin_center[0][1],
                       z=pin_center[i][2]-pin_center[0][2],           #Translation distance
                       connectivity=True,               #Connecting nodes will be released
                       group_options="EXISTING PART",
                       existing_part= part_new,
                       ext_connectors="INCLUDE")        #External connections and connectors will also be moved
def tans_solder_p(origin_part,comp_name_new,angle_d,Second_point,pin_num,pin_center,solder_points1,solder_points2,ref_node):
    base.RotatePart(origin_part,                      #Parts to be rotated
                    transformation_mode="MOVE",       #Parts will be rotated-moved
                    x1=0, y1=0, z1=0,                 #First point to specify the rotation axis
                    x2=Second_point[0], 
                    y2=Second_point[1], 
                    z2=Second_point[2],                #Second point to specify the rotation axis
                    connectivity=True,                 #Connecting nodes will NOT be released
                    ext_connectors="INCLUDE",          #External connections and connectors will also be moved
                    angle=angle_d)                     #Rotation angle
    base.TranslatePart(origin_part,                    #Parts to be translated
                       transformation_mode="MOVE",     #Parts will be translated-moved
                       x=pin_center[0][0], 
                       y=pin_center[0][1],
                       z=pin_center[0][2],           #Translation distance
                       connectivity=True,              #Connecting nodes will be released
                       ext_connectors="INCLUDE")        #External connections and connectors will also be moved
    #solder_center = get_mid_p(solder_points[1],solder_points[4])
    ref_node_coord = get_node_coord(ref_node)
    vector1 = get_vector_p(pin_center[0],ref_node_coord)
    #vector2 = get_vector_p(solder_points[1],solder_points[4])
    vector2 = get_vector_p(solder_points1,solder_points2)
    angle_d,Second_point2 = get_ang_two_vector(vector1,vector2)
    if angle_d != 0.0 and angle_d != 180.0:
        base.RotatePart(origin_part,                      #Parts to be rotated
                transformation_mode="MOVE",       #Parts will be rotated-moved
                x1=pin_center[0][0], 
                y1=pin_center[0][1], 
                z1=pin_center[0][2],                 #First point to specify the rotation axis
                x2=pin_center[0][0]+Second_point2[0], 
                y2=pin_center[0][1]+Second_point2[1], 
                z2=pin_center[0][2]+Second_point2[2],                #Second point to specify the rotation axis
                connectivity=True,                 #Connecting nodes will NOT be released
                ext_connectors="INCLUDE",          #External connections and connectors will also be moved
                angle=angle_d)                     #Rotation angle
    for i in range(1,pin_num):
        part_name = '{0}_pin_{1}'.format(comp_name_new,i+1)
        part_new = base.NewPart(part_name)
        base.TranslatePart(origin_part,                #Parts to be translated
                       transformation_mode="COPY",     #Parts will be translated-moved
                       x=pin_center[i][0]-pin_center[0][0], 
                       y=pin_center[i][1]-pin_center[0][1],
                       z=pin_center[i][2]-pin_center[0][2],           #Translation distance
                       connectivity=True,               #Connecting nodes will be released
                       group_options="EXISTING PART",
                       existing_part= part_new,
                       ext_connectors="INCLUDE")        #External connections and connectors will also be moved

def main():
    dict_solder = trans_solder()
    for k in dict_solder.keys():
        print(k)
        for solder in dict_solder[k]:
            try:
                point = solder["solder_center"][0]
                break
            except:
                print('fail')
        #res = get_pcb_vector(k,point)
        #print(res[1])
        origin_vector = [0,0,1]
        if round(pcb_out_vector[2],2) == 1.0:
            angle_d = 0
            Second_point = [0,1,0]
        elif round(pcb_out_vector[2],2) == -1.0:
            angle_d = 180
            Second_point = [0,1,0]
        else:
            angle_d,Second_point = get_ang_two_vector(origin_vector,pcb_out_vector)
        module = sys.modules[__name__]
        for solder in dict_solder[k]:
            for k,v in solder.items():
               setattr(module, k,v)
            comp_name_new = CompNameWithPath(comp_name,comp_path)
            #????????????
            part_name = '{0}_pin_1'.format(comp_name_new)
            if solder_type == "circular" and pin_type == "circular":
                continue
                iner_r = round(get_distance_p(pin_center[0],pin_points[0]),2)
                outer_r = round(get_distance_p(solder_center[0],solder_points[0]),2)
                pcb_h = round(pcb_thickness,2)
                pcb_cell_h = 0
                mesh_size = 0.3
                part_solder = create_y_y(part_name,iner_r,outer_r,pcb_h,pcb_cell_h,mesh_size,solid_h=1)
                tans_solder(part_solder,comp_name_new,angle_d,Second_point,pin_num,pin_center)
            #???????????????
            elif solder_type == "course" and pin_type == "circular":
                continue
                iner_r = round(get_distance_p(pin_center[0],pin_points[0]),2)
                outer_r = round(get_distance_p(solder_points[0][0],solder_points[0][2]),2)/2
                outer_l = round(get_distance_p(solder_points[0][2],solder_points[0][3]),2)
                pcb_h = round(pcb_thickness,2)
                pcb_cell_h = 0
                mesh_size = 0.3
                part_solder = create_y_p(part_name,iner_r,outer_r,outer_l,pcb_h,pcb_cell_h,mesh_size,solid_h=1)
                coords = (outer_l/2+outer_r,0,0)
                node = base.NearestNode(coords, 0.01, [part_solder])
                tans_solder_p(part_solder,comp_name_new,angle_d,Second_point,pin_num,pin_center,solder_points[0][1],solder_points[0][4],node[0])
            #????????????
            elif solder_type == "circular" and pin_type == "rectangle":
                #?????????????????????????????????
                pin_center =[]
                for pin_p in pin_points:
                    p_mid = get_mid_p(pin_p[0],pin_p[2])
                    pin_center.append(p_mid)
                iner_l = round(get_distance_p(pin_points[0][0],pin_points[0][1]),2)
                iner_w = round(get_distance_p(pin_points[0][0],pin_points[0][3]),2)
                pin_points1=pin_points[0][0]
                pin_points2=pin_points[0][1]
                if iner_l < iner_w:
                    iner_w = iner_l
                    iner_l = iner_w
                    pin_points2=pin_points[0][3]
                outer_r = round(get_distance_p(solder_center[0],solder_points[0]),2)
                #outer_r = round(get_distance_p(solder_points[0][0],solder_points[0][2]),2)/2
                #outer_l = round(get_distance_p(solder_points[0][2],solder_points[0][3]),2)
                pcb_h = round(pcb_thickness,2)
                pcb_cell_h = 0
                mesh_size = 0.3
                part_solder = create_j_y(part_name,iner_w,iner_l,outer_r,pcb_h,pcb_cell_h,mesh_size,solid_h=1)
                if iner_l != iner_w:
                    coords = (iner_l/2,0,0)
                    node = base.NearestNode(coords, 0.01, [part_solder])
                    tans_solder_p(part_solder,comp_name_new,angle_d,Second_point,pin_num,pin_center,pin_points1,pin_points2,node[0])
                else:
                    tans_solder(part_solder,comp_name_new,angle_d,Second_point,pin_num,pin_center)
            #???????????????
            elif solder_type == "course" and pin_type == "rectangle":
                #??????????????????????????????????????????????????????
                pin_center =[]
                for pin_p in pin_points:
                    p_mid = get_mid_p(pin_p[0],pin_p[2])
                    pin_center.append(p_mid)
                outer_r = round(get_distance_p(solder_points[0][0],solder_points[0][2]),2)/2
                outer_l = round(get_distance_p(solder_points[0][2],solder_points[0][3]),2)
                iner_l = round(get_distance_p(pin_points[0][0],pin_points[0][1]),2)
                iner_w = round(get_distance_p(pin_points[0][0],pin_points[0][3]),2)
                vector_l_0 = get_vector_p(solder_points[0][2],solder_points[0][3])
                vector_l_1 = get_vector_p(pin_points[0][0],pin_points[0][1])
                angle_d,Second_point2 = get_ang_two_vector(vector_l_0,vector_l_1)
                if 85 < angle_d  and angle_d < 95:
                    iner_w = iner_l
                    iner_l = iner_w
                pcb_h = round(pcb_thickness,2)
                pcb_cell_h = 0
                mesh_size = 0.3
                part_solder = create_j_p(part_name,iner_w,iner_l,outer_r,outer_l,pcb_h,pcb_cell_h,mesh_size,solid_h=1)
                coords = (outer_l/2+outer_r,0,0)
                node = base.NearestNode(coords, 0.01, [part_solder])
                tans_solder_p(part_solder,comp_name_new,angle_d,Second_point,pin_num,pin_center,solder_points[0][1],solder_points[0][4],node[0])
                pass
            #??????
            elif solder_type == "rectangle":
                #??????
                #???????????????????????????????????????,??????????????????????????????????????????????????????????????????
                #????????????????????????,??????????????????????????????,???????????????????????????????????????????????????
                #?????????????????????4??????,????????????????????????????????????????????????,???????????????????????????????????????????????????????????????
                #??????????????????????????????????????????????????????
                #???????????????????????????,?????????????????????,
                
            else:
                print('ok')
    
main()
