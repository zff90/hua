import ansa
import math
from ansa import base
from ansa import constants
from ansa import mesh
global deck
deck = base.SetCurrentDeck(constants.LSDYNA)
def record_start(deck,type):
    return base.CollectEntities(deck, None, type, recursive=True)
def record_end(deck,type,strat_list):
    #获取无对象返回的函数执行后新增的对象
    end_list = base.CollectEntities(deck, None, type, recursive=True)
    return list(set(end_list)-set(strat_list))
def approx(a,b,tol=0.01):
    dert = a - b
    f_tol = -1*tol
    if dert > f_tol and dert < tol:
        return True
    else:
        return False
def get_distance_p(p1,p2):
    dx = p1[0]-p2[0]
    dy = p1[1]-p2[1]
    dz = p1[2]-p2[2]
    dis = (dx*dx+dy*dy+dz*dz)**0.5
    return dis
def create_arc(p1,p2,z=0):
    p01 = (p1[0],p2[1],z)
    line01 = base.CurvesNew([p01,p1])
    line02 = base.CurvesNew([p01,p2])
    arc = CreataArcByTwoCurve(line01,line02,p1,p2)
    return arc
def CreataArcByTwoCurve(line01,line02,p1,p2):
    #无法通过圆心和起始点创建弧度小于90度的圆弧，只能通过相切创建
    arg1 = {}
    arg1[line01] = p1
    arg2 = {}
    arg2[line02] = p2
    curve = ansa.base.CircleTangentToCurves(arg1, arg2)
    ansa.base.DeleteCurves([line01,line02], False)
    return curve
def compare_cons_curve(curve,con,tol=0.01):
    curve_dict = base.GetEntityCardValues(deck,curve,('Length','Min Radius','Start X','Start Y','Start Z','End X','End Y','End Z',))
    con_dict = base.GetEntityCardValues(deck,con,('Length','Min Radius','Start Point','End Point'))
    if approx(curve_dict['Length'],con_dict['Length']):
        curve_Start_point = [curve_dict['Start X'],curve_dict['Start Y'],curve_dict['Start Z']]
        curve_End_point = [curve_dict['End X'],curve_dict['End Y'],curve_dict['End Z']]
        con_Start_point = [float(i) for i in con_dict['Start Point'].split(',')]
        con_End_point = [float(i) for i in con_dict['End Point'].split(',')]
        res_dis1 = get_distance_p(curve_Start_point,con_Start_point)
        res_dis2 = get_distance_p(curve_End_point,con_End_point)
        res_dis3 = get_distance_p(curve_Start_point,con_End_point)
        res_dis4 = get_distance_p(curve_End_point,con_Start_point)
        if approx(res_dis1,0) and approx(res_dis2,0):
            return True
        elif approx(res_dis3,0) and approx(res_dis4,0):
            return True
        else:
            return False
    else:
        return False
def compare_cons_cons(con1,con2,tol=0.01):
    con_dict1 = base.GetEntityCardValues(deck,con1,('Length','Min Radius','Start Point','End Point'))
    con_dict2 = base.GetEntityCardValues(deck,con2,('Length','Min Radius','Start Point','End Point'))
    if approx(con_dict1['Length'],con_dict2['Length']):
        con1_Start_point = [float(i) for i in con_dict1['Start Point'].split(',')]
        con1_End_point = [float(i) for i in con_dict1['End Point'].split(',')]
        con2_Start_point = [float(i) for i in con_dict2['Start Point'].split(',')]
        con2_End_point = [float(i) for i in con_dict2['End Point'].split(',')]
        res_dis1 = get_distance_p(con1_Start_point,con2_Start_point)
        res_dis2 = get_distance_p(con1_End_point,con2_End_point)
        res_dis3 = get_distance_p(con1_Start_point,con2_End_point)
        res_dis4 = get_distance_p(con1_End_point,con2_Start_point)
        if approx(res_dis1,0) and approx(res_dis2,0):
            return True
        elif approx(res_dis3,0) and approx(res_dis4,0):
            return True
        else:
            return False
    else:
        return False
def get_face_cons(f,lines):
    cons = base.CollectEntities(deck,f,"CONS",recursive=True)
    res_line=[]
    for l_i in lines:
        if l_i._ansaType(deck) == "CONS":
            res_line.append(l_i) 
        else:
            for con in cons:
                if compare_cons_curve(l_i,con):
                    res_line.append(con)
    return res_line
def main(part_name,iner_w,iner_l,outer_r,outer_l,pcb_h,pcb_cell_h,mesh_size,solid_h=1):
    #创建存放锡焊的part
    part = base.NewPart(part_name)
    sold_prop = base.NameToEnts("soldber_prop",deck,constants.ENM_EXACT)
    if sold_prop == None:
        sold_prop = base.CreateEntity(deck,"SECTION_SOLID",{"Name":"soldber_prop"})
    else:
        sold_prop = sold_prop[0]
    pin_prop = base.NameToEnts("pin_prop",deck,constants.ENM_EXACT)
    if pin_prop == None:
        pin_prop =  base.CreateEntity(deck,"SECTION_SOLID",{"Name":"pin_prop"})
    else:
        pin_prop=pin_prop[0]
    pcb_prop = base.NameToEnts("pcb_prop",deck,constants.ENM_EXACT)
    if pcb_prop == None:
        pcb_prop =  base.CreateEntity(deck,"SECTION_SOLID",{"Name":"pcb_prop"})
    else:
        pcb_prop=pcb_prop[0]
    base.SetCurrentEntity(part)
    current_part = base.GetCurrentEntity(deck, "ANSAPART")
    base.Or(part)
    p0 = (0,0,0)
    p1 = (iner_l/2,0,0)
    p2 = (0,iner_w/2,0)
    r1 = iner_w/2+0.2
    l1 = iner_l/2+0.25-r1
    if l1 < 0.01:
        r1 = iner_l/2+0.2
        l1 = iner_w/2+0.25-r1
    p3 = (r1+l1,0,0)
    p4 = (0,r1,0)
    p04 = (p3[0]-p4[1],p4[1],0)
    p5 = (outer_l/2+outer_r,0,0)
    p6 = (0,outer_r,0)
    p06 = (p5[0]-p6[1],p6[1],0)
    p7 = (p1[0],p2[1],0)
    p8 = (p7[0]+p5[0]*math.cos(math.pi/4),p7[1]+p5[0]*math.sin(math.pi/4),0)
    p00 = (0,0,solid_h)
    p10 = (p1[0],0,solid_h)
    p11 = (0,p2[1],solid_h)
    p12 = (p10[0],p11[1],solid_h)
    line1 = base.CurvesNew([p0,p1])
    line2 = base.CurvesNew([p0,p2])
    line3 = base.CurvesNew([p1,p3])
    line4 = base.CurvesNew([p2,p4])
    line5 = base.CurvesNew([p3,p5])
    line6 = base.CurvesNew([p4,p6])
    line7 = base.CurvesNew([p4,p04])
    line8 = base.CurvesNew([p6,p06])
    line9 = base.CurvesNew([p7,p8])
    line11 = base.CurvesNew([p00,p10])
    line12 = base.CurvesNew([p00,p11])
    line_v_1 = base.CurvesNew([p0,p00])
    line_v_2 = base.CurvesNew([p1,p10])
    line_v_3 = base.CurvesNew([p2,p11])
    line_v_4 = base.CurvesNew([p7,p12])
    line_v_5 = base.CurvesNew([p5,p10])
    line_v_6 = base.CurvesNew([p6,p11])
    c1 = base.CurvesNew([p1,p7])
    c10 = base.CurvesNew([p2,p7])
    c2 = create_arc(p3,p04)
    c3 = create_arc(p5,p06)
    c4 = base.CurvesNew([p10,p12])
    c40 = base.CurvesNew([p11,p12])
    start_list = record_start(deck,"CURVE")
    base.HotPointsIntersect(line9, c2)
    c20_l = record_end(deck,"CURVE",start_list)
    for c in c20_l:
        c_end = base.GetEntityCardValues(deck,c,('End X','Min Radius'))['End X']
        if c_end - p8[0] < 0.01 and c_end - p8[0] > -0.01:
            line10 = c
        else:
            c20 = c
    start_list = record_start(deck,"CURVE")
    base.HotPointsIntersect(line10, c3)
    c30_l = record_end(deck,"CURVE",start_list)
    for c in c30_l:
        c_end = base.GetEntityCardValues(deck,c,('End X','Min Radius'))['End X']
        if c_end - p8[0] < 0.01 and c_end - p8[0] > -0.01:
            p9_s = c
        else:
            c30 = c
    p9_coords = base.GetEntityCardValues(deck,p9_s,('Start X','Start Y','Start Z','Min Radius'))
    p9_x = p9_coords['Start X']
    p9_y = p9_coords['Start Y']
    p9_z = p9_coords['Start Z']
    p9 = (p9_x,p9_y,p9_z)
    line_v_7 = base.CurvesNew([p9,p12])
    f1 = base.FacesNewPlanar(faces_array=[line3,c1,line9,c2],ret_ents=True)
    [line3,c1,line9,c2] = get_face_cons(f1,[line3,c1,line9,c2])
    f2 = base.FacesNewPlanar(faces_array=[line4,c10,line9,c20,line7],ret_ents=True)
    [line4,c10,line9,c20,line7] = get_face_cons(f2,[line4,c10,line9,c20,line7])
    f3 = base.FacesNewPlanar(faces_array=[line5,c2,line10,c3],ret_ents=True)
    [line5,c2,line10,c3] = get_face_cons(f3,[line5,c2,line10,c3])
    f4 = base.FacesNewPlanar(faces_array=[line6,line7,c20,line10,c30,line8],ret_ents=True)
    [line6,line7,c20,line10,c30,line8] = get_face_cons(f4,[line6,line7,c20,line10,c30,line8])
    f5 = base.FacesNewPlanar(faces_array=[line3,line5,line_v_2,line_v_5],ret_ents=True)
    [line3,line5,line_v_2,line_v_5] = get_face_cons(f5,[line3,line5,line_v_2,line_v_5])
    f6 = base.FacesNewPlanar(faces_array=[line4,line6,line_v_3,line_v_6],ret_ents=True)
    [line4,line6,line_v_3,line_v_6] = get_face_cons(f6,[line4,line6,line_v_3,line_v_6])
    f7 = base.FacesNewPlanar(faces_array=[c1,line_v_2,c4,line_v_4],ret_ents=True)
    [c1,line_v_2,c4,line_v_4] = get_face_cons(f7,[c1,line_v_2,c4,line_v_4])
    f8 = base.FacesNewPlanar(faces_array=[c10,line_v_3,c40,line_v_4],ret_ents=True)
    [c10,line_v_3,c40,line_v_4] = get_face_cons(f8,[c10,line_v_3,c40,line_v_4])
    f9 = base.SurfsCoons(faces_array=[c3,line_v_7,c4,line_v_5],ret_ents=True)
    [c3,line_v_7,c4,line_v_5] = get_face_cons(f9,[c3,line_v_7,c4,line_v_5])
    f10 = base.SurfsCoons(faces_array=[c30,line8,line_v_6,c40,line_v_7],ret_ents=True)
    [c30,line8,line_v_6,c40,line_v_7] = get_face_cons(f10,[c30,line8,line_v_6,c40,line_v_7])
    f11 = base.FacesNewPlanar(faces_array=[line1,c1,line2,c10], ret_ents=True)
    [line1,c1,line2,c10] = get_face_cons(f11,[line1,c1,line2,c10])
    base.DeleteVisibleHotPoints()
    base.SetANSAdefaultsValues({'element_type': 'quad'})
    faces = base.CollectEntities(deck, part, "FACE",recursive=True)
    base.AutoCalculateOrientation(faces, True)
    vector = base.GetFaceOrientation(f11)
    if vector[2] != -1:
        base.Orient(f11)
    mesh.SetMeshParamTargetLength("absolute", mesh_size)
    cons = base.CollectEntities(deck,part,"CONS",recursive=True)
    mesh.ApplyNewLengthToMacros(str(mesh_size), cons)
    round_faces = f1+f2+f3+f4+f7+f8+f9+f10
    mesh.Create4SidedMesh(round_faces+f11, only_4sided=True, only_aligned=False, smooth_type='standard', spacing='map_opposite_sides')
    vol = mesh.VolumesMap(f5, f6, round_faces, "Normal parts", prop=sold_prop)# , ret_ents=True,
    base.DeleteEntity(f5+f6+f7+f8+f9+f10,True) 
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 1, 0, 0, 0, 0, 1, part)
    vol_all = base.CollectEntities(deck, part, "VOLUME",recursive=True)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, part)
    bodring_volume = base.CollectEntities(deck, part, "VOLUME",recursive=True)
    paste_node = base.CollectEntities(deck,bodring_volume,"NODE",recursive=True)
    mesh.AutoPaste(nodes=paste_node, distance=0.001)
    start_list = record_start(deck,"VOLUME")
    mesh.ExtrudeOffset(source=f11, connect_source=True, direction='default', distance=pcb_h, steps=int(pcb_h/mesh_size), property=pin_prop)
    mesh.ExtrudeOffset(source=f11, connect_source=True, direction='inverted', distance=solid_h, steps=int(solid_h/mesh_size), property=pin_prop)
    end_list = record_end(deck,"VOLUME",start_list)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 1, 0, 0, 0, 0, 1, end_list)
    end_list = record_end(deck,"VOLUME",start_list)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, end_list)
    pin_volume = record_end(deck,"VOLUME",start_list)
    paste_node = base.CollectEntities(deck,pin_volume,"NODE",recursive=True)
    mesh.AutoPaste(nodes=paste_node, distance=0.001)
    start_list0 = record_start(deck,"VOLUME")
    vol1 = mesh.ExtrudeOffset(source=f1+f2, connect_source=True, direction='default', property=sold_prop, distance=solid_h, steps=int(solid_h/mesh_size))
    end_list = record_end(deck,"VOLUME",start_list0)
    start_list1 = record_start(deck,"VOLUME")
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 1, 0, 0, 0, 0, 1, end_list)
    end_list2 = record_end(deck,"VOLUME",start_list1)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, end_list)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, end_list2)
    bodring_volume.extend(record_end(deck,"VOLUME",start_list0))
    paste_node = base.CollectEntities(deck,bodring_volume,"NODE",recursive=True)
    mesh.AutoPaste(nodes=paste_node, distance=0.001)
    start_list0 = record_start(deck,"VOLUME")
    vol4 = mesh.ExtrudeOffset(source=f3+f4, connect_source=True, direction='default', property=pcb_prop, distance=pcb_h, steps=int(pcb_h/mesh_size))
    end_list = record_end(deck,"VOLUME",start_list0)
    start_list1 = record_start(deck,"VOLUME")
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 1, 0, 0, 0, 0, 1, end_list)
    end_list2 = record_end(deck,"VOLUME",start_list1)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, end_list)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, end_list2)
    pcb_volume=record_end(deck,"VOLUME",start_list0)
    paste_node = base.CollectEntities(deck,pcb_volume,"NODE",recursive=True)
    mesh.AutoPaste(nodes=paste_node, distance=0.001)
    base.RedrawAll()
    return part
main('part_name',iner_w=0.88,iner_l=0.75,outer_r=0.825,outer_l=0.51,pcb_h=1.0,pcb_cell_h=0,mesh_size=0.3,solid_h=1)