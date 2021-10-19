#####################################################################################
## Procedure Name : 
## Purpose        : 
## Arguments      : 
## Returns        : 
## Comments       : 整体逻辑如下：
#                   1、遍历锡焊BOM,将BOM按PCB分类；
#                   2、获取每个PCB板的法向向量，写入到json中；
#                   3、遍历每个元件，参数化创建相应的锡焊；
#                   4、将锡焊平移和旋转到装配体中。
## Version        : 1.0
## FilePath       : \zff\pcbAndBodering.py
## Author         : FANG
## Date           : 2021-08-26 20:24:54
## LastEditors    : FANG
## LastEditTime   : 2021-10-15 09:26:09
#####################################################################################
from math import *
import inspect
import json
import math
import os
import re
import sys
import difflib
import ansa
from ansa import base
from ansa import constants
from ansa import mesh
global deck
deck = base.SetCurrentDeck(constants.LSDYNA)

import ansa
from ansa import base
from ansa import constants
from ansa import mesh
# base.SetCurrentDeck(constants.LSDYNA)
# global deck
# deck = base.CurrentDeck()
def GetConsOfHotPointsFromListOfHotPointsEntities():
    # collect all hot points of data-base
    hots_list = base.CollectEntities(deck, None, "HOT POINT", recursive=True)
    # collect adjacent CONS of hot points contained in list hots_list
    cons_list = base.GetConsOfHotPoints(hots_list)
    # pick CONS contained in list cons_list
    base.PickEntities(deck, "CONS", initial_entities=cons_list)
def GetConsOfHotPointsFromSingleHotPointEntity():
    # collect hot point with ID 2165 from data-base (## Change here to desired ID ##)
    hot_entity = base.GetEntity(deck, "HOT POINT", 2165)
    # collect adjacent CONS of hot point entity
    cons_list = base.GetConsOfHotPoints(hot_entity)
    # pick CONS contained in list cons_list
    base.PickEntities(deck, "CONS", initial_entities=cons_list)
def GetConsOfHotPointsFromListOfHotPointIDs():
    # Define a list of hot point IDs (## Change here to desired IDs ##)
    hots_ids_list = [2168, 2161, 1719]
    # collect adjacent CONS of hot points contained in list hots_ids_list
    cons_list = base.GetConsOfHotPoints(hots_ids_list)
    # pick CONS contained in list cons_list
    base.PickEntities(deck, "CONS", initial_entities=cons_list)
def GetConsOfHotPointFromSingleHotPointID():
    # collect adjacent CONS of hot point with ID 2161 (## Change here to desired ID ##)
    cons_list = base.GetConsOfHotPoints(hot_points = 2161)
    # pick CONS contained in list cons_list
    base.PickEntities(deck, "CONS", initial_entities=cons_list)
def GetConsOfHotPoinsFromListOfHotPointEntitiesAndIDs():
    # Define a list of hot point entities/IDs (## Change here to desired IDs ##)
    hots_list = [2168, base.GetEntity(deck, "HOT POINT", element_id=2165), 1752]
    # collect adjacent CONS of  hot points contained in list hots_list
    cons_list = base.GetConsOfHotPoints(hots_list)
    # pick CONS contained in list cons_list
    base.PickEntities(deck, "CONS", initial_entities=cons_list)
def curves_new(points):
    curve = base.CurvesNew(points)
    return curve
def CreateLineByCoord(list_coord):
    num_points = len(list_coord)
    # print (num_points)
    list_x_p = []
    list_y_p = [] 
    list_z_p = []
    for i in list_coord:
        list_x_p.append(i[0])
        list_y_p.append(i[1])
        list_z_p.append(i[2])
    # print (list_x_p)
    curves = base.CreateCurve(num_points, list_x_p, list_y_p, list_z_p)
    return curves
def CreataArcByTwoCurve(line01,line02,p1,p2):
    arg1 = {}
    arg1[line01] = p1
    arg2 = {}
    arg2[line02] = p2
    curve = ansa.base.CircleTangentToCurves(arg1, arg2)
    ansa.base.DeleteCurves([line01,line02], False)
    return curve
def getEntityByIds(deck,type,ids):
    entity=[]
    for i in ids:
        entity.append(base.GetEntity(deck,type,i))
    return entity
def record_start(deck,type):
    return base.CollectEntities(deck, None, type, recursive=True)
def record_end(deck,type,strat_list):
    end_list = base.CollectEntities(deck, None, type, recursive=True)
    return list(set(end_list)-set(strat_list))
def get_same_prop_obj(obj):
    obj_prop = obj.get_entity_values(deck,["PID"])["PID"]
    obj_type = obj.ansa_type(deck)
    #f1_prop = base.Entity(deck,f1_prop_id,"__PROPERTIES__")
    return base.CollectEntities(deck,obj_prop,obj_type,recursive=True) 
def create_arc(p1,p2,z=0):
    p01 = (p1[0],p2[1],z)
    line01 = base.CurvesNew([p01,p1])
    line02 = base.CurvesNew([p01,p2])
    arc = CreataArcByTwoCurve(line01,line02,p1,p2)
    return arc
def approx(a,b,tol=0.01):
    dert = a - b
    f_tol = -1*tol
    if dert > f_tol and dert < tol:
        return True
    else:
        return False
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
    #curve_dict = base.GetEntityCardValues(deck,con1,('Length','Min Radius','Start X','Start Y','Start Z','End X','End Y','End Z',))
    con_dict1 = base.GetEntityCardValues(deck,con1,('Length','Min Radius','Start Point','End Point'))
    con_dict2 = base.GetEntityCardValues(deck,con2,('Length','Min Radius','Start Point','End Point'))
    if approx(con_dict1['Length'],con_dict2['Length']):
        #curve_Start_point = [curve_dict['Start X'],curve_dict['Start Y'],curve_dict['Start Z']]
        #curve_End_point = [curve_dict['End X'],curve_dict['End Y'],curve_dict['End Z']]
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
def topo_cons_1b1(cons1,cons3=[]):
    for con1 in cons1:
        cons1.remove(con1)
        con_topo_temp = cons1
        con1_res = [con1]
        for con2 in con_topo_temp:
            if compare_cons_cons(con1,con2):
                con1_res.append(con2)
                cons1.remove(con2)
        if cons3 != []:
            for con3 in cons3:
                if compare_cons_cons(con1,con3):
                    con1_res.append(con3)
                    cons3.remove(con3)
        base.Topo(con1_res)
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
def create_j_y(part_name,iner_w,iner_l,outer_r,pcb_h,pcb_cell_h,mesh_size,solid_h=1):
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
    p3 = (iner_l/2+0.2,0,0)
    p4 = (0,iner_l/2+0.2,0)
    p5 = (outer_r,0,0)
    p6 = (0,outer_r,0)
    p7 = (p1[0],p2[1],0)
    p8 = (p4[1]*math.cos(math.pi/4),p4[1]*math.sin(math.pi/4),0)
    p9 = (p6[1]*math.cos(math.pi/4),p6[1]*math.sin(math.pi/4),0)

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
    line9 = base.CurvesNew([p7,p8])
    line10 = base.CurvesNew([p9,p8])
    
    line11 = base.CurvesNew([p00,p10])
    line12 = base.CurvesNew([p00,p11])
    line_v_1 = base.CurvesNew([p0,p00])
    line_v_2 = base.CurvesNew([p1,p10])
    line_v_3 = base.CurvesNew([p2,p11])
    line_v_4 = base.CurvesNew([p7,p12])
    line_v_5 = base.CurvesNew([p5,p10])
    line_v_6 = base.CurvesNew([p6,p11])
    line_v_7 = base.CurvesNew([p9,p12])
    #c1 = base.CreateCircleCenter2PointsRadius(p0, p1 p2, r0)
    #c0 = base.CreateCircleCenter2PointsRadius(p0, p1, p2, 1)
    #c0 = getEntityByIds(deck,"CURVE",c0)
    c1 = base.CurvesNew([p1,p7])
    c10 = base.CurvesNew([p2,p7])
    c2 = create_arc(p3,p4)
    c3 = create_arc(p5,p6)
    c4 = base.CurvesNew([p10,p12])
    c40 = base.CurvesNew([p11,p12])
    start_list = record_start(deck,"CURVE")
    base.HotPointsIntersect(line9, c2)
    c20 = record_end(deck,"CURVE",start_list)
    start_list = record_start(deck,"CURVE")
    base.HotPointsIntersect(line10, c3)
    c30 = record_end(deck,"CURVE",start_list)
    #ret = base.CurvesCreateFillet (line01, line02, 1)
    f1 = base.FacesNewPlanar(faces_array=[line3,c1,line9,c2],ret_ents=True)
    [line3,c1,line9,c2] = get_face_cons(f1,[line3,c1,line9,c2])
    f2 = base.FacesNewPlanar(faces_array=[line4,c10,line9,c20[0]],ret_ents=True)
    [line4,c10,line9,c200] = get_face_cons(f2,[line4,c10,line9,c20[0]])
    f3 = base.FacesNewPlanar(faces_array=[line5,c2,line10,c3],ret_ents=True)
    [line5,c2,line10,c3] = get_face_cons(f3,[line5,c2,line10,c3])
    f4 = base.FacesNewPlanar(faces_array=[line6,c200,line10,c30[0]],ret_ents=True)
    [line6,c200,line10,c300] = get_face_cons(f4,[line6,c200,line10,c30[0]])
    #底面
    #两侧面
    f5 = base.FacesNewPlanar(faces_array=[line3,line5,line_v_2,line_v_5],ret_ents=True)
    [line3,line5,line_v_2,line_v_5] = get_face_cons(f5,[line3,line5,line_v_2,line_v_5])
    f6 = base.FacesNewPlanar(faces_array=[line4,line6,line_v_3,line_v_6],ret_ents=True)
    [line4,line6,line_v_3,line_v_6] = get_face_cons(f6,[line4,line6,line_v_3,line_v_6])
    #矩形侧面
    f7 = base.FacesNewPlanar(faces_array=[c1,line_v_2,c4,line_v_4],ret_ents=True)
    [c1,line_v_2,c4,line_v_4] = get_face_cons(f7,[c1,line_v_2,c4,line_v_4])
    f8 = base.FacesNewPlanar(faces_array=[c10,line_v_3,c40,line_v_4],ret_ents=True)
    [c10,line_v_3,c40,line_v_4] = get_face_cons(f8,[c10,line_v_3,c40,line_v_4])
    #大侧面line_v_7
    #f9 = base.FacesNewFitted(faces_array=[c3,line_v_7,c4,line_v_5],ret_ents=True)
    #f10 = base.FacesNewFitted(faces_array=[c30[0],line_v_6,c40,line_v_7],ret_ents=True)
    f9 = base.SurfsCoons(faces_array=[c3,line_v_7,c4,line_v_5],ret_ents=True)
    [c3,line_v_7,c4,line_v_5] = get_face_cons(f9,[c3,line_v_7,c4,line_v_5])
    f10 = base.SurfsCoons(faces_array=[c300,line_v_6,c40,line_v_7],ret_ents=True)
    [c300,line_v_6,c40,line_v_7] = get_face_cons(f10,[c300,line_v_6,c40,line_v_7])
    #f8 = base.FacesNewPlanar(faces_array=c0, ret_ents=True)
    f11 = base.FacesNewPlanar(faces_array=[line1,c1,line2,c10], ret_ents=True)
    
    #ansa.base.Topo("visible")
    base.DeleteVisibleHotPoints()
    base.SetANSAdefaultsValues({'element_type': 'quad'})#quad,mixed,tria
    faces = base.CollectEntities(deck, part, "FACE",recursive=True)
    base.AutoCalculateOrientation(faces, True)
    vector = base.GetFaceOrientation(f11)
    if vector[2] != -1:
        base.Orient(f11)
    mesh.SetMeshParamTargetLength("absolute", 0.2)
    cons = base.CollectEntities(deck,part,"CONS",recursive=True)
    mesh.ApplyNewLengthToMacros("0.2", cons)
    #base.SetEntityCardValues(deck,cons,{"Elem. Length":0.2}) 
    #for consi in cons:
    #    consi.set_entity_values(deck,{"Elem. Length":0.2})
    round_faces = f1+f2+f3+f4+f7+f8+f9+f10
    mesh.Create4SidedMesh(round_faces+f11, only_4sided=True, only_aligned=False, smooth_type='standard', spacing='map_opposite_sides')
    #f3 f4 为目标面和源面
    #后面可以修改为batchmesh对面进行网格划分
    vol = mesh.VolumesMap(f5, [], round_faces, "Normal parts", ret_ents=True,prop=sold_prop)
    base.DeleteEntity(f5+f6+f7+f8+f9+f10,True,True)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 1, 0, 0, 0, 0, 1, part)
    vol_all = base.CollectEntities(deck, part, "VOLUME",recursive=True)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, part)
    bodring_volume = base.CollectEntities(deck, part, "VOLUME",recursive=True)
    paste_node = base.CollectEntities(deck,bodring_volume,"NODE",recursive=True)
    mesh.AutoPaste(nodes=paste_node, distance=0.001)
    start_list0 = record_start(deck,"VOLUME")
    mesh.ExtrudeOffset(source=f11, connect_source=True, direction='default', distance=pcb_h, steps=int(pcb_h/mesh_size), property=pin_prop)
    mesh.ExtrudeOffset(source=f11, connect_source=True, direction='inverted', distance=solid_h, steps=int(solid_h/mesh_size), property=pin_prop)
    end_list = record_end(deck,"VOLUME",start_list0)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 1, 0, 0, 0, 0, 1, end_list)
    end_list = record_end(deck,"VOLUME",start_list0)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, end_list)
    pin_volume = record_end(deck,"VOLUME",start_list0)
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
def create_y_p(part_name,iner_r,outer_r,outer_l,pcb_h,pcb_cell_h,mesh_size,solid_h=1):
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
    #base.SetEntityPart(volume,part)
    #base.SetEntityPart(part, group)
    #current_part = base.CreateEntity(deck, "ANSAPART", {"name":part_name}) 
    base.SetCurrentEntity(part)
    current_part = base.GetCurrentEntity(deck, "ANSAPART")
    base.Or(part)
    p0 = (0,0,0)
    p1 = (iner_r,0,0)
    p2 = (0,iner_r,0)
    p_1 = (-1*iner_r,0,0)
    p_2 = (0,-1*iner_r,0)
    p3 = (iner_r+0.2,0,0)
    p4 = (0,iner_r+0.1,0)
    p04 = (p3[0]-p4[1],p4[1],0)
    p5 = (outer_l/2+outer_r,0,0)
    p6 = (0,outer_r,0)
    p06 = (p5[0]-p6[1],p6[1],0)
    p00 = (0,0,solid_h)
    p7 = (iner_r,0,solid_h)
    p8 = (0,iner_r,solid_h)
    line1 = base.CurvesNew([p0,p1])
    line2 = base.CurvesNew([p0,p2])
    line3 = base.CurvesNew([p1,p3])
    line4 = base.CurvesNew([p2,p4])
    line5 = base.CurvesNew([p3,p5])
    line6 = base.CurvesNew([p4,p6])
    line7 = base.CurvesNew([p4,p04])
    line8 = base.CurvesNew([p6,p06])
    
    line9 = base.CurvesNew([p00,p7])
    line10 = base.CurvesNew([p00,p8])
    line_v_1 = base.CurvesNew([p0,p00])
    line_v_2 = base.CurvesNew([p1,p7])
    line_v_3 = base.CurvesNew([p2,p8])
    line_v_4 = base.CurvesNew([p5,p7])
    line_v_5 = base.CurvesNew([p6,p8])
    #c1 = base.CreateCircleCenter2PointsRadius(p0, p1 p2, r0)
    #c0 = base.CreateCircleCenter2PointsRadius(p0, p1, p2, 1)
    #c0 = getEntityByIds(deck,"CURVE",c0)
    c1 = create_arc(p1,p2)
    c1_1 = create_arc(p1,p_2)
    c1_2 = create_arc(p_1,p_2)
    c1_3 = create_arc(p_1,p2)
    c2 = create_arc(p3,p04)
    c3 = create_arc(p5,p06)
    c4 = create_arc(p7,p8,1)
    #ret = base.CurvesCreateFillet (line01, line02, 1)
    f1 = base.FacesNewPlanar(faces_array=[line3,c1,line4,line7,c2],ret_ents=True)
    [line3,c1,line4,line7,c2] = get_face_cons(f1, [line3,c1,line4,line7,c2])
    f2 = base.FacesNewPlanar(faces_array=[line5,c2,line7,line6,line8,c3],ret_ents=True)
    [line5,c2,line7,line6,line8,c3] = get_face_cons(f2, [line5,c2,line7,line6,line8,c3])
    f3 = base.FacesNewPlanar(faces_array=[line3,line5,line_v_2,line_v_4],ret_ents=True)
    [line3,line5,line_v_2,line_v_4] = get_face_cons(f3, [line3,line5,line_v_2,line_v_4])
    f4 = base.FacesNewPlanar(faces_array=[line4,line6,line_v_3,line_v_5],ret_ents=True)
    [line4,line6,line_v_3,line_v_5] = get_face_cons(f4, [line4,line6,line_v_3,line_v_5])
    #f5 = base.FacesNewFitted(faces_array=[c1,line_v_2,c4,line_v_3],ret_ents=True)
    #f6 = base.FacesNewFitted(faces_array=[c3,line8,line_v_4,c4,line_v_5],ret_ents=True)
    f5 = base.SurfsCoons(faces_array=[c1,line_v_2,c4,line_v_3],ret_ents=True)
    [c1,line_v_2,c4,line_v_3] = get_face_cons(f5, [c1,line_v_2,c4,line_v_3])
    f6 = base.SurfsCoons(faces_array=[c3,line8,line_v_4,c4,line_v_5],ret_ents=True)
    [c3,line8,line_v_4,c4,line_v_5] = get_face_cons(f6, [c3,line8,line_v_4,c4,line_v_5])
    #f7 = base.FacesNewPlanar(faces_array=c0, ret_ents=True)
    #f7 = base.FacesNewPlanar(faces_array=[line1,c1,line2], ret_ents=True)
    ansa.base.Topo("visible")
    base.DeleteVisibleHotPoints()
    base.SetANSAdefaultsValues({'element_type': 'quad'})#quad,mixed,tria
    faces = base.CollectEntities(deck, part, "FACE", True)
    base.AutoCalculateOrientation(faces, True)
    #vector = base.GetFaceOrientation(f7)
    #if vector[2] != -1:
    #    base.Orient(f7)
    mesh.SetMeshParamTargetLength("absolute", mesh_size)
    cons = base.CollectEntities(deck,part,"CONS", recursive=True)
    mesh.ApplyNewLengthToMacros(str(mesh_size), cons)
    #base.SetEntityCardValues(deck,cons,{"Elem. Length":0.2}) 
    #for consi in cons:
    #    consi.set_entity_values(deck,{"Elem. Length":0.2})
    mesh.Create4SidedMesh(0, only_4sided=True, only_aligned=True, smooth_type='standard', spacing='map_opposite_sides')
    round_faces = f1+f2+f5+f6
    #f3 f4 为目标面和源面
    #后面可以修改为batchmesh对面进行网格划分
    vol = mesh.VolumesMap(f3, [], round_faces, "Normal parts", ret_ents=True,prop=sold_prop)
    base.DeleteEntity(f3+f4+f5+f6,force=True)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 1, 0, 0, 0, 0, 1, vol)
    #base.SetANSAdefaultsValues({'Normal Vector':'0., 1., 0.' ,'Origin ':' 0., 0., 0.'})
    #base.GeoSymmetry("COPY", 0, "SAME PART", "NONE", vol, keep_connectivity=True)
    vol_all = base.CollectEntities(deck, part, "VOLUME", recursive=True)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, vol_all)
    #base.SetANSAdefaultsValues({'Normal Vector':'1., 0., 0.' ,'Origin ':' 0., 0., 0.'})
    #base.GeoSymmetry("COPY", 0, "SAME PART", "NONE", vol_all, keep_connectivity=True)
    #base.GeoRotate("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 0, 1, 180, vol_all, keep_connectivity=True)
    bodring_volume = base.CollectEntities(deck, part, "VOLUME", recursive=True)
    paste_node = base.CollectEntities(deck,bodring_volume,"NODE", recursive=True)
    mesh.AutoPaste(nodes=paste_node, distance=0.001)
    faces = base.CollectEntities(deck, part, "FACE", True)
    [c1,c1_1,c1_2,c1_3] = get_face_cons(faces,[c1,c1_1,c1_2,c1_3])
    f7 = base.FacesNewPlanar(faces_array=[c1,c1_1,c1_2,c1_3], ret_ents=True)
    vector = base.GetFaceOrientation(f7)
    if vector[2] != -1:
        base.Orient(f7)
    mesh.CreateCircularMesh(f7, zones=1, pattern='o-grid')
    if int(pcb_h/mesh_size) > 3:
        num_pcb = int(pcb_h/mesh_size)
    else:
        num_pcb = 3
    mesh.ExtrudeOffset(source=f7, connect_source=True, direction='default', distance=pcb_h, steps=num_pcb, property=pin_prop)
    mesh.ExtrudeOffset(source=f7, connect_source=True, direction='inverted', distance=solid_h, steps=int(solid_h/mesh_size), property=pin_prop)

    start_list0 = record_start(deck,"VOLUME")
    vol1 = mesh.ExtrudeOffset(source=f1, connect_source=True, direction='default', property=sold_prop, distance=pcb_h, steps=num_pcb)
    #vol2 = mesh.ExtrudeOffset(source=f7, connect_source=False, direction='default', distance=1, steps=5)
    #vol3 = mesh.ExtrudeOffset(source=f7, connect_source=False, direction='inverted', distance=1, steps=5)
    end_list = record_end(deck,"VOLUME",start_list0)
    start_list1 = record_start(deck,"VOLUME")
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 1, 0, 0, 0, 0, 1, end_list)
    end_list2 = record_end(deck,"VOLUME",start_list1)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, end_list)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, end_list2)
    bodring_volume.extend(record_end(deck,"VOLUME",start_list0))
    paste_node = base.CollectEntities(deck,bodring_volume,"NODE", recursive=True)
    mesh.AutoPaste(nodes=paste_node, distance=0.001)
    start_list0 = record_start(deck,"VOLUME")
    vol4 = mesh.ExtrudeOffset(source=f2, connect_source=True, direction='default', property=pcb_prop, distance=pcb_h, steps=num_pcb)
    end_list = record_end(deck,"VOLUME",start_list0)
    start_list1 = record_start(deck,"VOLUME")
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 1, 0, 0, 0, 0, 1, end_list)
    end_list2 = record_end(deck,"VOLUME",start_list1)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, end_list)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, end_list2)
    pcb_volume=record_end(deck,"VOLUME",start_list0)
    paste_node = base.CollectEntities(deck,pcb_volume,"NODE", recursive=True)
    mesh.AutoPaste(nodes=paste_node, distance=0.001)
    base.RedrawAll()
    #facelist1 = get_same_prop_obj(f2[0])
    #cons = base.CollectEntities(deck,facelist1,"CONS",recursive=True)
    #arg2 = base.GetEntity(deck, 'FACE', 1)
    #base.ConsProjectNormal(entities=cons, faces_array=arg2,  delete_faces=True) 
    #base.RedrawAll()
    #facelist1.append(arg2)
    #ents = base.CollectEntities(deck,facelist1,"CONS",recursive=True)
    #ansa.base.Topo(ents)
    #ents = base.CollectEntities(deck,part,["ELEMENT_SHELL","FACE","CURVE"],recursive=True)
    #base.DeleteEntity(ents,force=True)
    return part
def create_j_p(part_name,iner_w,iner_l,outer_r,outer_l,pcb_h,pcb_cell_h,mesh_size,solid_h=1):
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
    #base.SetEntityPart(volume,part)
    #base.SetEntityPart(part, group)
    #current_part = base.CreateEntity(deck, "ANSAPART", {"name":"solderding"}) 
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
    p8 = (p04[0]+p04[1]*math.cos(math.pi/4),p04[1]*math.sin(math.pi/4),0)
    p9 = (p06[0]+p06[1]*math.cos(math.pi/4),p06[1]*math.sin(math.pi/4),0)

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
    line10 = base.CurvesNew([p9,p8])
    
    line11 = base.CurvesNew([p00,p10])
    line12 = base.CurvesNew([p00,p11])
    line_v_1 = base.CurvesNew([p0,p00])
    line_v_2 = base.CurvesNew([p1,p10])
    line_v_3 = base.CurvesNew([p2,p11])
    line_v_4 = base.CurvesNew([p7,p12])
    line_v_5 = base.CurvesNew([p5,p10])
    line_v_6 = base.CurvesNew([p6,p11])
    line_v_7 = base.CurvesNew([p9,p12])
    #c1 = base.CreateCircleCenter2PointsRadius(p0, p1 p2, r0)
    #c0 = base.CreateCircleCenter2PointsRadius(p0, p1, p2, 1)
    #c0 = getEntityByIds(deck,"CURVE",c0)
    c1 = base.CurvesNew([p1,p7])
    c10 = base.CurvesNew([p2,p7])
    c2 = create_arc(p3,p04)
    c3 = create_arc(p5,p06)
    c4 = base.CurvesNew([p10,p12])
    c40 = base.CurvesNew([p11,p12])
    start_list = record_start(deck,"CURVE")
    base.HotPointsIntersect(line9, c2)
    c20 = record_end(deck,"CURVE",start_list)
    start_list = record_start(deck,"CURVE")
    base.HotPointsIntersect(line10, c3)
    c30 = record_end(deck,"CURVE",start_list)
    #ret = base.CurvesCreateFillet (line01, line02, 1)
    f1 = base.FacesNewPlanar(faces_array=[line3,c1,line9,c2],ret_ents=True)
    [line3,c1,line9,c2] = get_face_cons(f1,[line3,c1,line9,c2])
    f2 = base.FacesNewPlanar(faces_array=[line4,c10,line9,c20[0],line7],ret_ents=True)
    [line4,c10,line9,c200,line7] = get_face_cons(f2,[line4,c10,line9,c20[0],line7])
    f3 = base.FacesNewPlanar(faces_array=[f3,c2,line10,c3],ret_ents=True)
    [f3,c2,line10,c3] = get_face_cons(faces,[f3,c2,line10,c3])
    f4 = base.FacesNewPlanar(faces_array=[line6,line7,c200,line10,c30[0],line8],ret_ents=True)
    [line6,line7,c200,line10,c300,line8] = get_face_cons(f4,[line6,line7,c200,line10,c30[0],line8])
    #底面
    #两侧面
    f5 = base.FacesNewPlanar(faces_array=[line3,line5,line_v_2,line_v_5],ret_ents=True)
    [line3,line5,line_v_2,line_v_5] = get_face_cons(f5,[line3,line5,line_v_2,line_v_5])
    f6 = base.FacesNewPlanar(faces_array=[line4,line6,line_v_3,line_v_6],ret_ents=True)
    [line4,line6,line_v_3,line_v_6] = get_face_cons(f6,[line4,line6,line_v_3,line_v_6])
    #矩形侧面
    f7 = base.FacesNewPlanar(faces_array=[c1,line_v_2,c4,line_v_4],ret_ents=True)
    [c1,line_v_2,c4,line_v_4] = get_face_cons(f7,[c1,line_v_2,c4,line_v_4])
    f8 = base.FacesNewPlanar(faces_array=[c10,line_v_3,c40,line_v_4],ret_ents=True)
    [c10,line_v_3,c40,line_v_4] = get_face_cons(f8,[c10,line_v_3,c40,line_v_4])
    #大侧面line_v_7
    f9 = base.SurfsCoons(faces_array=[c3,line_v_7,c4,line_v_5],ret_ents=True)
    [c3,line_v_7,c4,line_v_5] = get_face_cons(f9,[c3,line_v_7,c4,line_v_5])
    f10 = base.SurfsCoons(faces_array=[c300,line8,line_v_6,c40,line_v_7],ret_ents=True)
    [c300,line8,line_v_6,c40,line_v_7] = get_face_cons(f10,[c300,line8,line_v_6,c40,line_v_7])
    #f8 = base.FacesNewPlanar(faces_array=c0, ret_ents=True)
    f11 = base.FacesNewPlanar(faces_array=[line1,c1,line2,c10], ret_ents=True)
    [line1,c1,line2,c10] = get_face_cons(f11,[line1,c1,line2,c10])
    ansa.base.Topo("visible")
    base.DeleteVisibleHotPoints()
    base.SetANSAdefaultsValues({'element_type': 'quad'})#quad,mixed,tria
    faces = base.CollectEntities(deck, part, "FACE",recursive=True)
    base.AutoCalculateOrientation(faces, True)
    vector = base.GetFaceOrientation(f11)
    if vector[2] != -1:
        base.Orient(f11)
    mesh.SetMeshParamTargetLength("absolute", 0.2)
    cons = base.CollectEntities(deck,part,"CONS",recursive=True)
    mesh.ApplyNewLengthToMacros("0.2", cons)
    #base.SetEntityCardValues(deck,cons,{"Elem. Length":0.2}) 
    #for consi in cons:
    #    consi.set_entity_values(deck,{"Elem. Length":0.2})
    round_faces = f1+f2+f3+f4+f7+f8+f9+f10
    mesh.Create4SidedMesh(round_faces+f11, only_4sided=True, only_aligned=False, smooth_type='standard', spacing='map_opposite_sides')
    #f3 f4 为目标面和源面
    #后面可以修改为batchmesh对面进行网格划分
    vol = mesh.VolumesMap(f5, f6, round_faces, "Normal parts", ret_ents=True,prop=sold_prop)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 1, 0, 0, 0, 0, 1, vol)
    #base.SetANSAdefaultsValues({'Normal Vector':'0., 1., 0.' ,'Origin ':' 0., 0., 0.'})
    #base.GeoSymmetry("COPY", 0, "SAME PART", "NONE", vol, keep_connectivity=True)
    vol_all = base.CollectEntities(deck, part, "VOLUME",recursive=True)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, vol_all)
    #base.SetANSAdefaultsValues({'Normal Vector':'1., 0., 0.' ,'Origin ':' 0., 0., 0.'})
    #base.GeoSymmetry("COPY", 0, "SAME PART", "NONE", vol_all, keep_connectivity=True)
    #base.GeoRotate("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 0, 1, 180, vol_all, keep_connectivity=True)
    bodring_volume = base.CollectEntities(deck, part, "VOLUME",recursive=True)
    paste_node = base.CollectEntities(deck,bodring_volume,"NODE",recursive=True)
    mesh.AutoPaste(nodes=paste_node, distance=0.001)
    #base.GeoSymmetry("COPY", 0, "SAME PART", "NONE", f8, keep_connectivity=True)
    #base.Or(f8)
    start_list = record_start(deck,"FACE")
    #base.GeoRotate("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 0, 1, 90, f8, keep_connectivity=True)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 1, 0, 0, 0, 0, 1, f11)
    end_list0 = record_end(deck,"FACE",start_list)
    #base.GeoRotate("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 0, 1, 180, f8, keep_connectivity=True)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, f11)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, end_list0)
    #base.GeoRotate("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 0, 1, 270, f8, keep_connectivity=True)
    face_e = record_end(deck,"FACE",start_list)+f11
    #paste_node = base.CollectEntities(deck,face_e,"NODE",recursive=True)
    #mesh.AutoPaste(nodes=paste_node, distance=0.001)
    start_list = record_start(deck,"VOLUME")
    mesh.ExtrudeOffset(source=face_e, connect_source=True, direction='default', distance=pcb_h, steps=int(pcb_h/mesh_size), property=pin_prop)
    mesh.ExtrudeOffset(source=face_e, connect_source=True, direction='inverted', distance=solid_h, steps=int(solid_h/mesh_size), property=pin_prop)
    start_listf = record_start(deck,"FACE")
    base.GeoTranslate("COPY",0,"SAME PART","NONE",0,0,-1*pcb_h,face_e)
    end_listf = record_end(deck,"FACE",start_listf)
    if pcb_cell_h >0 :
        mesh.ExtrudeOffset(source=end_listf, connect_source=True, direction='default', distance=pcb_cell_h, steps=int(pcb_cell_h/mesh_size), property=pin_prop)
    pin_volume = record_end(deck,"VOLUME",start_list)
    paste_node = base.CollectEntities(deck,pin_volume,"NODE",recursive=True)
    mesh.AutoPaste(nodes=paste_node, distance=0.001)
    #mesh.CreateCircularMesh(0, zones=1, pattern='o-grid')
    #mesh.Create4SidedMesh(0, only_4sided=True, only_aligned=False, smooth_type='standard', spacing='map_opposite_sides')
    #mesh.VolumesRemesh(vol_all)
    #mesh.ReleaseElements(vol_all)
    #base.DeleteEntity(vol_all)
    #nodes = base.CollectEntities(deck, part, "NODE")
    #base.Release(nodes, "nodes")
    #base.ReleaseVolumes()
    #mesh.AutoPaste(visible=True, distance=0.001)
    start_list0 = record_start(deck,"VOLUME")
    vol1 = mesh.ExtrudeOffset(source=f1+f2, connect_source=True, direction='default', property=sold_prop, distance=solid_h, steps=int(solid_h/mesh_size))
    #vol2 = mesh.ExtrudeOffset(source=f8, connect_source=False, direction='default', distance=1, steps=5)
    #vol3 = mesh.ExtrudeOffset(source=f8, connect_source=False, direction='inverted', distance=1, steps=5)
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
    #facelist1 = get_same_prop_obj(f3[0])+get_same_prop_obj(f4[0])
    #cons1 = base.CollectEntities(deck,facelist1,"CONS",recursive=True)
    #facelist2 = get_same_prop_obj(f9[0])+get_same_prop_obj(f10[0])
    #cons2 = base.CollectEntities(deck,facelist2,"CONS",recursive=True)
    #cons = list(set(cons1)&set(cons2))
    #arg2 = base.GetEntity(deck, 'FACE', 1)
    #base.ConsProjectNormal(entities=cons, faces_array=arg2,  delete_faces=True) 
    #base.RedrawAll()
    #facelist1.append(arg2)
    #ents = base.CollectEntities(deck,arg2,"CONS",recursive=True)
    # Need some documentation? Run this with F5
    #base.SetANSAdefaultsValues({"tolerance_mode" : "middle"})
    #p1 = base.GetPartFromName("p1")
    #p2 = base.GetPartFromName("p2")
    
    #cons_of_p1 = base.PerimetersOfFace(facelist1, 'active')
    #cons_of_p2 = base.PerimetersOfFace(arg2, 'active')
    
    #boundaries_of_p1 = base.DefineInterfaceBoundary(facelist1, part=True)
    #boundaries_of_p2 = base.DefineInterfaceBoundary(cons_of_p2, part=True)

    #base.SmartPaste(cons, ents)
    
    #ansa.base.Topo(cons+ents)
    #ents = base.CollectEntities(deck,part,["ELEMENT_SHELL","FACE","CURVE"],recursive=True)
    #base.DeleteEntity(ents,force=True)
    return part
def create_y_y(part_name,iner_r,outer_r,pcb_h,pcb_cell_h,mesh_size,solid_h=1):
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
    #base.SetEntityPart(volume,part)
    #base.SetEntityPart(part, group)
    #current_part = base.CreateEntity(deck, "ANSAPART", {"name":"solderding"}) 
    base.SetCurrentEntity(part)
    current_part = base.GetCurrentEntity(deck, "ANSAPART")
    base.Or(part)
    p0 = (0,0,0)
    p1 = (iner_r,0,0)
    p2 = (0,iner_r,0)
    p_1 = (-1*iner_r,0,0)
    p_2 = (0,-1*iner_r,0)
    p01 = (p1[0],p2[1],0)
    p01_1 = (p1[0],-1*p2[1],0)
    p01_2= (-1*p1[0],-1*p2[1],0)
    p01_3= (-1*p1[0],p2[1],0)
    p3 = (iner_r+0.2,0,0)#PCB上的孔为引脚半径加0.2
    p4 = (0,iner_r+0.2,0)#PCB上的孔为引脚半径加0.2
    p02 = (p3[0],p4[1],0)
    p5 = (outer_r,0,0)
    p6 = (0,outer_r,0)
    p03 = (p5[0],p6[1],0)
    p00 = (0,0,solid_h)
    p7 = (iner_r,0,solid_h)
    p8 = (0,iner_r,solid_h)
    p04 = (p7[0],p8[1],solid_h)
    line1 = base.CurvesNew([p0,p1])
    line2 = base.CurvesNew([p0,p2])
    
    line01 = base.CurvesNew([p01,p1])
    line02 = base.CurvesNew([p01,p2])
    line01_1 = base.CurvesNew([p01_1,p1])
    line02_1 = base.CurvesNew([p01_1,p_2])
    line01_2 = base.CurvesNew([p01_2,p_1])
    line02_2 = base.CurvesNew([p01_2,p_2])
    line01_3 = base.CurvesNew([p01_3,p_1])
    line02_3 = base.CurvesNew([p01_3,p2])
    
    line3 = base.CurvesNew([p1,p3])
    line4 = base.CurvesNew([p2,p4])
    line03 = base.CurvesNew([p02,p3])
    line04 = base.CurvesNew([p02,p4])
    line5 = base.CurvesNew([p3,p5])
    line6 = base.CurvesNew([p4,p6])
    line05 = base.CurvesNew([p03,p5])
    line06 = base.CurvesNew([p03,p6])
    line7 = base.CurvesNew([p00,p7])
    line8 = base.CurvesNew([p00,p8])
    line07 = base.CurvesNew([p04,p7])
    line08 = base.CurvesNew([p04,p8])
    line_v_1 = base.CurvesNew([p0,p00])
    line_v_2 = base.CurvesNew([p1,p7])
    line_v_3 = base.CurvesNew([p2,p8])
    line_v_4 = base.CurvesNew([p5,p7])
    line_v_5 = base.CurvesNew([p6,p8])
    #c1 = base.CreateCircleCenter2PointsRadius(p0, p1 p2, r0)
    #c0 = base.CreateCircleCenter2PointsRadius(p0, p1, p2, 1)
    #c0 = getEntityByIds(deck,"CURVE",c0)
    c1 = CreataArcByTwoCurve(line01,line02,p1,p2)
    c1_1 = CreataArcByTwoCurve(line01_1,line02_1,p1,p_2)
    c1_2 = CreataArcByTwoCurve(line01_2,line02_2,p_1,p_2)
    c1_3 = CreataArcByTwoCurve(line01_3,line02_3,p_1,p2)

    c2 = CreataArcByTwoCurve(line03,line04,p3,p4)
    c3 = CreataArcByTwoCurve(line05,line06,p5,p6)
    c4 = CreataArcByTwoCurve(line07,line08,p7,p8)
    #ret = base.CurvesCreateFillet (line01, line02, 1)
    f1 = base.FacesNewPlanar(faces_array=[c1,line3,c2,line4],ret_ents=True)
    [c1,line3,c2,line4] = get_face_cons(f1,[c1,line3,c2,line4])
    f2 = base.FacesNewPlanar(faces_array=[c2,line5,c3,line6],ret_ents=True)
    [c2,line5,c3,line6] = get_face_cons(f2,[c2,line5,c3,line6])
    f3 = base.FacesNewPlanar(faces_array=[line3,line5,line_v_2,line_v_4],ret_ents=True)
    [line3,line5,line_v_2,line_v_4] =get_face_cons(f3,[line3,line5,line_v_2,line_v_4])
    f4 = base.FacesNewPlanar(faces_array=[line4,line6,line_v_3,line_v_5],ret_ents=True)
    [line4,line6,line_v_3,line_v_5] =get_face_cons(f4,[line4,line6,line_v_3,line_v_5])
    f5 = base.SurfsCoons(faces_array=[c1,line_v_2,c4,line_v_3],ret_ents=True)
    [c1,line_v_2,c4,line_v_3] = get_face_cons(f5,[c1,line_v_2,c4,line_v_3])
    f6 = base.SurfsCoons(faces_array=[c3,line_v_4,c4,line_v_5],ret_ents=True)
    [c3,line_v_4,c4,line_v_5] = get_face_cons(f6,[c3,line_v_4,c4,line_v_5])
    faces = base.CollectEntities(deck, part, "FACE", True)
    base.AutoCalculateOrientation(faces, True)

    #mesh.SetMeshParamTargetLength("absolute", mesh_size)
    cons = base.CollectEntities(deck,part,"CONS", recursive=True)
    mesh.ApplyNewLengthToMacros(str(mesh_size), cons)
    #base.SetEntityCardValues(deck,cons,{"Elem. Length":0.2}) 
    #for consi in cons:
    #    consi.set_entity_values(deck,{"Elem. Length":0.2})
    round_faces = f1+f2+f5+f6
    mesh.Create4SidedMesh(0, only_4sided=True, only_aligned=False, smooth_type='standard', spacing='map_opposite_sides')
    #f3 f4 为目标面和源面
    #后面可以修改为batchmesh对面进行网格划分
    vol = mesh.VolumesMap(f3, [], round_faces, "Normal parts", ret_ents=True,prop=sold_prop)
    ents = f3+f4+f5+f6
    base.DeleteEntity(ents,force=True)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 1, 0, 0, 0, 0, 1, vol)
    #base.SetANSAdefaultsValues({'Normal Vector':'0., 1., 0.' ,'Origin ':' 0., 0., 0.'})
    #base.GeoSymmetry("COPY", 0, "SAME PART", "NONE", vol, keep_connectivity=True)
    vol_all = base.CollectEntities(deck, part, "VOLUME", recursive=True)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, vol_all)
    #base.SetANSAdefaultsValues({'Normal Vector':'1., 0., 0.' ,'Origin ':' 0., 0., 0.'})
    #base.GeoSymmetry("COPY", 0, "SAME PART", "NONE", vol_all, keep_connectivity=True)
    #base.GeoRotate("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 0, 1, 180, vol_all, keep_connectivity=True)
    bodring_volume = base.CollectEntities(deck, part, "VOLUME", recursive=True)
    paste_node = base.CollectEntities(deck,bodring_volume,"NODE", recursive=True)
    mesh.AutoPaste(nodes=paste_node, distance=0.001)
    faces = base.CollectEntities(deck, part, "FACE", True)
    [c1,c1_1,c1_2,c1_3] = get_face_cons(faces,[c1,c1_1,c1_2,c1_3])
    f7 = base.FacesNewPlanar(faces_array=[c1,c1_1,c1_2,c1_3], ret_ents=True)
    vector = base.GetFaceOrientation(f7)
    if vector[2] != -1:
        base.Orient(f7)
    mesh.CreateCircularMesh(f7, zones=1, pattern='o-grid')

    if int(pcb_h/mesh_size) > 3:
        num_pcb = int(pcb_h/mesh_size)
    else:
        num_pcb = 3
    start_list = record_start(deck,"VOLUME")
    mesh.ExtrudeOffset(source=f7, connect_source=True, direction='default', distance=pcb_h, steps=num_pcb, property=pin_prop)
    #pcb_cell_h,mesh_size,solid_h=1
    mesh.ExtrudeOffset(source=f7, connect_source=True, direction='inverted', distance=solid_h, steps=int(solid_h/mesh_size), property=pin_prop)
    pin_volume = record_end(deck,"VOLUME",start_list)
    paste_node = base.CollectEntities(deck,pin_volume,"NODE")
    mesh.AutoPaste(nodes=paste_node, distance=0.001)
    #base.DeleteEntity(f7,force=True)
    
    start_list0 = record_start(deck,"VOLUME")
    vol1 = mesh.ExtrudeOffset(source=f1, connect_source=True, direction='default', distance=pcb_h, steps=num_pcb, property=sold_prop)
    end_list = record_end(deck,"VOLUME",start_list0)
    start_list1 = record_start(deck,"VOLUME")
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 1, 0, 0, 0, 0, 1, end_list)
    end_list2 = record_end(deck,"VOLUME",start_list1)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, end_list)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, end_list2)
    bodring_volume.extend(record_end(deck,"VOLUME",start_list0))
    paste_node = base.CollectEntities(deck,bodring_volume,"NODE")
    mesh.AutoPaste(nodes=paste_node, distance=0.001)
    #ents = base.CollectEntities(deck,part,["ELEMENT_SHELL","FACE","CURVE"],recursive=True)
    start_list0 = record_start(deck,"VOLUME")
    vol4 = mesh.ExtrudeOffset(source=f2, connect_source=True, direction='default', distance=pcb_h, steps=num_pcb,  property=pcb_prop)
    end_list = record_end(deck,"VOLUME",start_list0)
    start_list1 = record_start(deck,"VOLUME")
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 1, 0, 0, 0, 0, 1, end_list)
    end_list2 = record_end(deck,"VOLUME",start_list1)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, end_list)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", 0, 0, 0, 0, 1, 0, 0, 0, 1, end_list2)
    pcb_volume=record_end(deck,"VOLUME",start_list0)
    paste_node = base.CollectEntities(deck,pcb_volume,"NODE")
    mesh.AutoPaste(nodes=paste_node, distance=0.001)
    base.RedrawAll()
    #facelist1 = get_same_prop_obj(f2[0])
    #cons = base.CollectEntities(deck,facelist1,"CONS",recursive=True)
    #arg2 = base.GetEntity(deck, 'FACE', 1)
    #base.ConsProjectNormal(entities=cons, faces_array=arg2,  delete_faces=True) 
    #base.RedrawAll()
    #facelist1.append(arg2)
    #ents = base.CollectEntities(deck,facelist1,"CONS",recursive=True)
    #ansa.base.Topo(ents)
    #ents = base.CollectEntities(deck,part,["ELEMENT_SHELL","FACE","CURVE"],recursive=True)
    #base.DeleteEntity(ents,force=True)
    return part
def create_j_p2(part_name,iner_w,iner_l,outer_r,outer_l,pcb_h,pcb_cell_h,mesh_size,solid_h=1):
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
    #base.SetEntityPart(volume,part)
    #base.SetEntityPart(part, group)
    #current_part = base.CreateEntity(deck, "ANSAPART", {"name":"solderding"}) 
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
    #p8 = (p04[0]+p04[1]*math.cos(math.pi/4),p04[1]*math.sin(math.pi/4),0)
    #p9 = (p06[0]+p06[1]*math.cos(math.pi/4),p06[1]*math.sin(math.pi/4),0)
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
    #line10 = base.CurvesNew([p9,p8])
    
    line11 = base.CurvesNew([p00,p10])
    line12 = base.CurvesNew([p00,p11])
    line_v_1 = base.CurvesNew([p0,p00])
    line_v_2 = base.CurvesNew([p1,p10])
    line_v_3 = base.CurvesNew([p2,p11])
    line_v_4 = base.CurvesNew([p7,p12])
    line_v_5 = base.CurvesNew([p5,p10])
    line_v_6 = base.CurvesNew([p6,p11])
    #line_v_7 = base.CurvesNew([p9,p12])
    #c1 = base.CreateCircleCenter2PointsRadius(p0, p1 p2, r0)
    #c0 = base.CreateCircleCenter2PointsRadius(p0, p1, p2, 1)
    #c0 = getEntityByIds(deck,"CURVE",c0)
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
    #ret = base.CurvesCreateFillet (line01, line02, 1)
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
    #底面
    #两侧面
    f5 = base.FacesNewPlanar(faces_array=[line3,line5,line_v_2,line_v_5],ret_ents=True)
    [line3,line5,line_v_2,line_v_5] = get_face_cons(f5,[line3,line5,line_v_2,line_v_5])
    f6 = base.FacesNewPlanar(faces_array=[line4,line6,line_v_3,line_v_6],ret_ents=True)
    [line4,line6,line_v_3,line_v_6] = get_face_cons(f6,[line4,line6,line_v_3,line_v_6])
    #矩形侧面
    f7 = base.FacesNewPlanar(faces_array=[c1,line_v_2,c4,line_v_4],ret_ents=True)
    [c1,line_v_2,c4,line_v_4] = get_face_cons(f7,[c1,line_v_2,c4,line_v_4])
    f8 = base.FacesNewPlanar(faces_array=[c10,line_v_3,c40,line_v_4],ret_ents=True)
    [c10,line_v_3,c40,line_v_4] = get_face_cons(f8,[c10,line_v_3,c40,line_v_4])
    #大侧面line_v_7
    f9 = base.SurfsCoons(faces_array=[c3,line_v_7,c4,line_v_5],ret_ents=True)
    [c3,line_v_7,c4,line_v_5] = get_face_cons(f9,[c3,line_v_7,c4,line_v_5])
    f10 = base.SurfsCoons(faces_array=[c30,line8,line_v_6,c40,line_v_7],ret_ents=True)
    [c30,line8,line_v_6,c40,line_v_7] = get_face_cons(f10,[c30,line8,line_v_6,c40,line_v_7])
    #f8 = base.FacesNewPlanar(faces_array=c0, ret_ents=True)
    f11 = base.FacesNewPlanar(faces_array=[line1,c1,line2,c10], ret_ents=True)
    [line1,c1,line2,c10] = get_face_cons(f11,[line1,c1,line2,c10])
    #ansa.base.Topo("visible")
    base.DeleteVisibleHotPoints()
    base.SetANSAdefaultsValues({'element_type': 'quad'})#quad,mixed,tria
    faces = base.CollectEntities(deck, part, "FACE",recursive=True)
    base.AutoCalculateOrientation(faces, True)
    vector = base.GetFaceOrientation(f11)
    if vector[2] != -1:
        base.Orient(f11)
    mesh.SetMeshParamTargetLength("absolute", 0.2)
    cons = base.CollectEntities(deck,part,"CONS",recursive=True)
    mesh.ApplyNewLengthToMacros("0.2", cons)
    #base.SetEntityCardValues(deck,cons,{"Elem. Length":0.2}) 
    #for consi in cons:
    #    consi.set_entity_values(deck,{"Elem. Length":0.2})
    round_faces = f1+f2+f3+f4+f7+f8+f9+f10
    mesh.Create4SidedMesh(round_faces+f11, only_4sided=True, only_aligned=False, smooth_type='standard', spacing='map_opposite_sides')
    #f3 f4 为目标面和源面
    #后面可以修改为batchmesh对面进行网格划分
   
    vol = mesh.VolumesMap(f5, [], round_faces, "Normal parts", prop=sold_prop)# , ret_ents=True,
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
def create_pcb_pcb(part_name,height,length,dert,solder_c,pcb_h,mesh_size,solid_h=1):
    #创建存放锡焊的part
    part = base.NewPart(part_name)
    sold_prop = base.NameToEnts("soldber_prop",deck,constants.ENM_EXACT)
    if sold_prop == None:
        sold_prop = base.CreateEntity(deck,"SECTION_SOLID",{"Name":"soldber_prop"})
        print(sold_prop)
    else:
        sold_prop = sold_prop[0]
    base.SetCurrentEntity(part)
    current_part = base.GetCurrentEntity(deck, "ANSAPART")
    base.Or(part)
    height = height-0.2
    p0 = (0,0,0)
    p1 = (height,0,0)
    p2 = (height,0,1)
    p3 = (height+0.2,0,1)
    p4 = (height+0.2,0,0)
    p5 = (height+0.2,0,-1*pcb_h)
    p6 = (height,0,-1*pcb_h)

    line1 = base.CurvesNew([p0,p1])
    line2 = base.CurvesNew([p1,p2])
    line3 = base.CurvesNew([p0,p2])
    line4 = base.CurvesNew([p2,p3])
    line5 = base.CurvesNew([p3,p4])
    line6 = base.CurvesNew([p4,p1])
    line7 = base.CurvesNew([p4,p5])
    line8 = base.CurvesNew([p5,p6])
    line9 = base.CurvesNew([p6,p1])


    f1 = base.FacesNewPlanar(faces_array=[line1,line2,line3],ret_ents=True)
    [line1,line2,line3] = get_face_cons(f1,[line1,line2,line3])
    f2 = base.FacesNewPlanar(faces_array=[line2,line4,line5,line6],ret_ents=True)
    [line2,line4,line5,line6] = get_face_cons(f2,[line2,line4,line5,line6])
    f3 = base.FacesNewPlanar(faces_array=[line6,line7,line8,line9],ret_ents=True)
    [line6,line7,line8,line9] = get_face_cons(f3,[line6,line7,line8,line9])
    #ansa.base.Topo("visible")
    base.DeleteVisibleHotPoints()
    base.SetANSAdefaultsValues({'element_type': 'mixed'})#quad,mixed,tria
    mesh.SetMeshParamTargetLength("absolute", 0.2)
    cons = base.CollectEntities(deck,f1,"CONS",recursive=True)
    mesh.ApplyNewLengthToMacros("0.2", cons)
    base.Or(f1) 
    mesh.CreateSpotMesh()
    round_faces = f2+f3
    cons = base.CollectEntities(deck,round_faces,"CONS",recursive=True)
    for con in cons:
        con_l = base.GetEntityCardValues(deck,con,['Length'])
        if round(con_l['Length'],1) == 0.2:
            mesh.NumberPerimeters(con, '2')
    mesh.Create4SidedMesh(round_faces, only_4sided=False, only_aligned=False, smooth_type='standard', spacing='map_opposite_sides')
    face_e = f1+f2+f3
    for i in range(len(length)):
        base.GeoTranslate("MOVE",0,"SAME PART","NONE",0,dert[i],0,face_e)
        mesh.ExtrudeOffset(source=face_e, connect_source=False, direction='inverted', distance=length[0], steps=int(length/mesh_size), property=sold_prop,part=part)
        base.GeoTranslate("MOVE",0,"SAME PART","NONE",0,-1*dert[i],0,face_e)
    base.GeoMirrorPlane("COPY", 0, "SAME PART", "NONE", solder_c[0], 0, 0, solder_c[0], 1, 0, solder_c[0], 0, 1, part)
    return part

def CompNameWithPath(comp_name,comp_path):
    str_name_new = comp_name + "_"+ comp_path
    str_name_new = str_name_new.replace(',','_')
    return str_name_new
def trans_solder():
    #dict_solder = ReadDicFromJsonFile("GO_soldering.json")
    dict_solder = json.load(open('E:/ansa2/zff/out/GO_soldering.json',mode='r',encoding='UTF-8'))
    module = sys.modules[__name__]
    dict_solder_new = {}
    for solder in dict_solder['soldering']:
        for k,v in solder.items():
            setattr(module, k,v)
        pcb_name = CompNameWithPath(pcb_comp_name,pcb_comp_path)
        if pcb_name not in dict_solder_new.keys():
            dict_solder_new[pcb_name] = []
        dict_solder_new[pcb_name].append(solder)
    return dict_solder_new
def get_distance(ents1,ents2,data=1):
    input = []
    if data == 0:
        p0 = base.Newpoint(ents1[0],ents1[1],ents1[2])
        p1 = base.Newpoint(ents2[0],ents2[1],ents2[2])
        input.append(p0)
        input.append(p1)
    else:
        input.append(ents1)   # get only the 1. selected node
        input.append(ents2)  # get only the 1. selected curve
    msr = base.CreateMeasurement(input, 'DISTANCE')
    if msr:
        ret_res = base.GetEntityCardValues(deck, msr, ('ID', 'RESULT', 'RES1', 'RES2', 'RES3'))
        print("A new measurement is created with id: ", ret_res['ID'])
        print("The result is d: ", ret_res['RESULT'], ", dx: ", ret_res['RES1'], ", dy: ", ret_res['RES2'], ", dz: ", ret_res['RES3'])
        base.DeleteEntity(msr,force=True)
        if data == 0:
            base.DeleteEntity(input,force=True)
        return ret_res['RESULT']
    else:
        return None
def get_distance_p(p1,p2):
    dx = p1[0]-p2[0]
    dy = p1[1]-p2[1]
    dz = p1[2]-p2[2]
    dis = (dx*dx+dy*dy+dz*dz)**0.5
    #[3.5, 6.22, 0] [3.5, 5.97, 0]
    #***********
    #0.3536
    return dis
def get_pcb_vector(pcb_name,point):
    p0 = base.Newpoint(point[0],point[1],point[2])
    try:
        part = base.GetPartFromName(pcb_name)
    except:
        return None
    faces = base.CollectEntities(deck,part,'FACE',recursive=True)
    res = None
    for face in faces:
        dis = round(get_distance(p0,face),2)
        base.DeleteEntity(p0,force=True)
        if dis == 0.0:
            vector = base.GetFaceOrientation(face)
            res = (face,vector)
            break
        else:
            res = None
    return res
def get_ang_two_vector(v1,v2):
    # 引入numpy模块并创建两个向量x和y
    import numpy as np
    #计算法向量
    x1=v1[0]
    y1=v1[1]
    z1=v1[2]
    x2=v2[0]
    y2=v2[1]
    z2=v2[2]
    x3 = round(y1*z2-y2*z1,2)
    y3 = -1*round(x1*z2-x2*z1,2)
    z3 = round(x1*y2-x2*y1,2)
    Second_point = [x3,y3,z3]
    x=np.array(v1)
    y=np.array(v2)
    np.multiply(v1,v2)
    # 分别计算两个向量的模：
    l_x=np.sqrt(x.dot(x))
    l_y=np.sqrt(y.dot(y))
    print('向量的模=',l_x,l_y)
    
    # 计算两个向量的点积
    dian=x.dot(y)
    print('向量的点积=',dian)
    
    # 计算夹角的cos值：
    cos_=dian/(l_x*l_y)
    print('夹角的cos值=',cos_)
    
    # 求得夹角（弧度制）：
    angle_hu=np.arccos(cos_)
    print('夹角（弧度制）=',angle_hu)
    
    # 转换为角度值：
    angle_d=angle_hu*180/np.pi
    print('夹角=%f°'%angle_d)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    return angle_d,Second_point
def get_mid_p(p1,p2):
    x_m = p1[0]+(p2[0]-p1[0])/2
    y_m = p1[1]+(p2[1]-p1[1])/2
    z_m = p1[2]+(p2[2]-p1[2])/2
    mid_p = (x_m,y_m,z_m)
    return mid_p
def get_vector_p(p1,p2):
    dis = get_distance_p(p1,p2)
    x_v = (p2[0]-p1[0])/dis
    y_v = (p2[1]-p1[1])/dis
    z_v = (p2[2]-p1[2])/dis
    vector_p = (x_v,y_v,z_v)
    return vector_p
def get_node_coord(ref_node_id):
    print('00000')
    node_obj = base.GetEntity(deck,'NODE',ref_node_id) 
    print(node_obj)
    vals=('X','Y','Z')
    coord = base.GetEntityCardValues(deck,node_obj,vals)
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
def tans_solder_r(origin_part,comp_name_new,angle_d,Second_point,pin_num,solder_center,pin_center,solder_points1,solder_points2,ref_node1,ref_node2):
    base.RotatePart(origin_part,                     
                    transformation_mode="MOVE",      
                    x1=solder_center[0],
                    y1=solder_center[1],
                    z1=solder_center[2],                 
                    x2=solder_center[0]+Second_point[0], 
                    y2=solder_center[1]+Second_point[1], 
                    z2=solder_center[2]+Second_point[2],             
                    connectivity=True,                 
                    ext_connectors="INCLUDE",          
                    angle=angle_d)                     
    base.TranslatePart(origin_part,                    
                       transformation_mode="MOVE",     
                       x=pin_center[0]-solder_center[0], 
                       y=pin_center[1]-solder_center[1],
                       z=pin_center[2]-solder_center[2],           
                       connectivity=True,              
                       ext_connectors="INCLUDE") 
    #solder_center = get_mid_p(solder_points[1],solder_points[4])
    ref_node_coord1 = get_node_coord(ref_node1)
    ref_node_coord2 = get_node_coord(ref_node2)
    vector1 = get_vector_p(ref_node_coord1,ref_node_coord2)
    #vector2 = get_vector_p(solder_points[1],solder_points[4])
    vector2 = get_vector_p(solder_points1,solder_points2)
    angle_d,Second_point2 = get_ang_two_vector(vector1,vector2)
    if angle_d != 0.0:
        base.RotatePart(origin_part,                      #Parts to be rotated
                transformation_mode="MOVE",       #Parts will be rotated-moved
                x1=pin_center[0], 
                y1=pin_center[1], 
                z1=pin_center[2],                 #First point to specify the rotation axis
                x2=pin_center[0]+Second_point2[0], 
                y2=pin_center[1]+Second_point2[1], 
                z2=pin_center[2]+Second_point2[2],                #Second point to specify the rotation axis
                connectivity=True,                 #Connecting nodes will NOT be released
                ext_connectors="INCLUDE",          #External connections and connectors will also be moved
                angle=angle_d)                     #Rotation angle
def getmax_min_index(list):
    if approx(max(list), min(list),0.001):
        return True
    else:
        max_index = list.index(max(list))
        min_index = list.index(min(list))
        if max_index < 2 and min_index < 2:
            return True
        else:
            return False
def check_1p_in_2p(p0,p1,p2):
    c_x = getmax_min_index([p0[0],p1[0],p2[0]])
    c_y = getmax_min_index([p0[1],p1[1],p2[1]])
    c_z = getmax_min_index([p0[2],p1[2],p2[2]])
    if c_x and c_y and c_z:
        return True
    else:
        return False
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
            print(comp_name_new)
            #if comp_name_new != "nujiangdianrong5_dkba41426905_zz_-2_54_518_565_939":
            #    continue
            #外圆内圆
            part_name = '{0}_pin_1'.format(comp_name_new)
            if solder_type == "circular" and pin_type == "circular":
                continue
                pin_center = solder['pin_center']
                print(pin_center[0],pin_points[0])
                iner_r = round(get_distance_p(pin_center[0],pin_points[0]),2)
                print('***********')
                print("iner_r is {0}".format(iner_r))
                outer_r = round(get_distance_p(solder_center[0],solder_points[0]),2)
                if outer_r-iner_r < 0.2:
                    outer_r = iner_r+0.4
                print("outer_r is {0}".format(outer_r))
                pcb_h = round(pcb_thickness,2)
                pcb_cell_h = 0
                mesh_size = 0.3
                part_solder = create_y_y(part_name,iner_r,outer_r,pcb_h,pcb_cell_h,mesh_size,solid_h=1)
                tans_solder(part_solder,comp_name_new,angle_d,Second_point,pin_num,pin_center)
            #外跑道内圆
            elif solder_type == "course" and pin_type == "circular":
                continue
                pin_center = solder['pin_center']
                iner_r = round(get_distance_p(pin_center[0],pin_points[0]),2)
                outer_r = round(get_distance_p(solder_points[0][0],solder_points[0][2]),2)/2
                outer_l = round(get_distance_p(solder_points[0][2],solder_points[0][3]),2)
                pcb_h = round(pcb_thickness,2)
                pcb_cell_h = 0
                mesh_size = 0.3
                part_solder = create_y_p(part_name,iner_r,outer_r,outer_l,pcb_h,pcb_cell_h,mesh_size,solid_h=1)
                coords = (outer_l/2+outer_r,0,0)
                print(coords)
                node = base.NearestNode(coords, 0.1, [part_solder])
                node_id = node[0]._id
                print(node)
                tans_solder_p(part_solder,comp_name_new,angle_d,Second_point,pin_num,pin_center,solder_points[0][1],solder_points[0][4],node_id)
            #外圆内矩
            elif solder_type == "circular" and pin_type == "rectangle":
                #需要考虑矩形长边的方向
                continue
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
                    node_id = node[0]._id
                    tans_solder_p(part_solder,comp_name_new,angle_d,Second_point,pin_num,pin_center,pin_points1,pin_points2,node_id)
                else:
                    tans_solder(part_solder,comp_name_new,angle_d,Second_point,pin_num,pin_center)
            #外跑道内矩
            elif solder_type == "course" and pin_type == "rectangle":
                #需要考虑矩形长边和跑道长边的匹配关系
                continue
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
                part_solder = create_j_p2(part_name,iner_w,iner_l,outer_r,outer_l,pcb_h,pcb_cell_h,mesh_size,solid_h=1)
                coords = (outer_l/2+outer_r,0,0)
                node = base.NearestNode(coords, 0.01, [part_solder])
                node_id = node[0]._id
                tans_solder_p(part_solder,comp_name_new,angle_d,Second_point,pin_num,pin_center,solder_points[0][1],solder_points[0][4],node_id)
            #矩形
            elif solder_type == "rectangle" and pin_type == "rectangle":
                print(solder_type,pin_type)
                i = 1
                for solder_i in  solder["solderingshape"]:
                    part_name = "{0}_pin_{1}".format(comp_name_new,i)
                    i+=1
                    pin_data = solder_i["pin_rectangle"][0]
                    pin_center = get_mid_p(pin_data[0],pin_data[2])
                    solder_data = solder_i["solder_rectangle"]
                    solder_data0 = solder_data[0]
                    print('pin_data is {0}'.format(pin_data))
                    print('solder_data0 is {0}'.format(solder_data0))
                    #pin_data = [[0,0,0],[1,0,0],[1,1,0],[0,1,0]]
                    #solder_data0 = [[0,0,0],[0.5,0,0],[0.5,0.5,0],[0.5,0,0]]
                    pin_point1 = 0
                    for i in range(0,4):
                        j = i + 1
                        if j == 4:
                            j = 0 
                        num = 0
                        print(pin_data[i],pin_data[j],solder_data0)
                        if check_1p_in_2p(pin_data[i],pin_data[j],solder_data0[0]):
                            num += 1
                        if check_1p_in_2p(pin_data[i],pin_data[j],solder_data0[1]):
                            num += 1
                        if check_1p_in_2p(pin_data[i],pin_data[j],solder_data0[2]):
                            num += 1
                        if check_1p_in_2p(pin_data[i],pin_data[j],solder_data0[3]):
                            num += 1
                        if num > 1:
                            pin_point1 = pin_data[i]
                            pin_point2 = pin_data[j]
                            print(long_line)
                            break
                    pin_l = get_distance_p(pin_point1,pin_point2)
                    pin_l_temp = get_distance_p(pin_data[0],pin_data[1])
                    pin_w_temp = get_distance_p(pin_data[1],pin_data[2])
                    if approx(pin_l,pin_l_temp):
                        pin_w = pin_w_temp
                    else:
                        pin_w = pin_l_temp
                    solder_len_list=[]
                    solder_start_len_list=[]
                    for solder_data_i in solder_data:
                        point_len = []
                        point_len_index = []
                        point_w = []
                        for solder_point in solder_data_i:
                            if check_1p_in_2p(pin_point1,pin_point2,solder_point):
                                point_len.append(solder_point)
                                point_len_index.append(solder_data_i.index(solder_point))
                        if len(point_len) == 2:
                            solder_len = get_distance_p(point_len[0],point_len[1])
                            solder_start_len = min(get_distance_p(point_len[0],pin_point1),get_distance_p(point_len[1],pin_point1))
                            max_index = max(point_len_index)
                            max_index2 = max_index + 1
                            if max_index2 == 4:
                                max_index2 = 0
                            solder_w = get_distance_p(solder_data_i[max_index],solder_data_i[max_index])
                            solder_len_list.append(solder_len)
                            solder_start_len_list.append(solder_start_len)
                    #solder_w = solder_data_list[0]['solder_w']
                    solder_c = (solder_w+pin_w/2,pin_l/2,0)
                    part_solder = create_pcb_pcb(part_name=part_name,
                                                 height=solder_w,
                                                 length=solder_len_list,
                                                 dert=solder_start_len_list,
                                                 solder_c=solder_c,
                                                 pcb_h= round(pcb_thickness,2),
                                                 mesh_size=0.3,
                                                 solid_h=1)
                    coords1 = (0,solder_start_len_list[0],0)
                    node1 = base.NearestNode(coords1, 0.01, [part_solder])
                    node_id_1 = node1[0]._id
                    coords2 = (0,solder_start_len_list[0]+solder_len_list[0],0)
                    node2 = base.NearestNode(coords2, 0.01, [part_solder])
                    node_id_2 = node2[0]._id
                    tans_solder_r(part_solder,comp_name_new,angle_d,Second_point,pin_num,solder_c,pin_center,pin_point1,pin_point2,node_id_1,node_id_2)

                    

            else:
                print('ok')
#main()

create_pcb_pcb(part_name="shjkh",height=1,length=2,dert=0.5,pcb_h=1,mesh_size=0.3,solid_h=1)