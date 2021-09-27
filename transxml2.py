#####################################################################################
## Procedure Name : 转换INTESIM XML文件为APDL
## Purpose        : 
## Arguments      : 
## Returns        : 
## Comments       : 目前主要支持以下内容转换
##                  1、材料（全局坐标系） 线弹性结构材料 密度 弹性模量 泊松比 增加热属性,包含热导率、比热容、热膨胀系数。
##                  2、根据物理场组件名和材料对应关系，给组件赋材料
##                  3、边界支持位移、固定（全局坐标系、圆柱坐标系）
##                  4、载荷支持节点力、节点力矩、压力、体加速度（全局坐标系、圆柱坐标系） 增加对流和体生热
##                  5、角速度（支持自定义旋转轴）
##                  6、单元类型目前只支持实体、壳后面增加梁、质量点、rbe2、接触等 增加热场实体单元
#                   7、增加平面单元。
## Version        : 1.0
## FilePath       : \huawei-platform-scriptc:\Users\Administrator\Desktop\4-8ys\transxml2.py
## Author         : FANG
## Date           : 2021-04-23 16:04:21
## LastEditors    : FANG
## LastEditTime   : 2021-04-23 16:07:57
#####################################################################################
import xmltodict
import json


def xml2dict(xmlfile):
    #读取xml文件
    file_object = open(xmlfile, encoding='utf-8')
    try:
        all_the_xmlStr = file_object.read()
    finally:
        file_object.close()
    # xml To dict
    convertedDict = xmltodict.parse(all_the_xmlStr)['Intesim']
    convertedDict.pop('Mesh')
    convertedDict.pop('@version')
    convertedDict.pop('Description')
    convertedDict.pop('Coupling')
    convertedDict.pop('Geometry')
    #去除网格、几何、耦合等无用或数据量较大的标签
    # ensure_ascii 设置为False 中文可以转换
    jsonStr = json.dumps(convertedDict, ensure_ascii=False)
    # 写入文件 写入为utf-8编码
    with open(r'intesim.json', 'w', encoding='utf-8') as f:
        # 除去xmltodict 转换时默认添加的'@' 符号
        f.write(jsonStr.replace('@', ''))
    data = json.loads(jsonStr.replace('@', ''))
    return data


def trans_xmltoapdl(xmldata):
    if xmldata['PhysicsModel']['Model']['type'] == 'Thermal':
        apdl_str = 'ET,1,70\n'
    else:
        apdl_str = 'KEYOPT,1,2,0\nKEYOPT,7,8,1\nKEYOPT,7,3,2\n'
        #增加三种平面单元
        apdl_str += 'et,14,42\nKEYOPT,14,2,1\nKEYOPT,14,3,0\n' #平面应力
        apdl_str += 'et,15,42\nKEYOPT,15,2,1\nKEYOPT,15,3,2\n' #平面应变
        apdl_str += 'et,16,42\nKEYOPT,16,2,1\nKEYOPT,16,3,1\n' #轴对称
    for i in range(1,14):
        apdl_str += 'ETDEL,{0} \n'.format(i)  # 删除无用单元类型
    ############################  global  ###########################
    ############################  CoordSystem #######################
    # 获取旋转轴坐标点
    mat_maping_dict = {'Cylindrical': 1 }
    #0 or CART    1 or CYLIN    2 or SPHE    3 or TORO
    if 'CoordSystem' in xmldata['Global'].keys():
        sysdata = xmldata['Global']['CoordSystem']
        points_data_dict = dict()
        if sysdata.__class__ == dict:
            if sysdata['type'] == 'RotationalAxis':
                point_data = []
                for point in sysdata['Point']:
                    for k, v in point.items():
                        point_data.append(v)
                points_data_dict[sysdata['id']] = point_data
            elif sysdata['type'] == 'Cylindrical':
                apdl_str += "k,1,{0},{1},{2}\n".format(sysdata['Point'][0]['x'], sysdata['Point'][0]['y'], sysdata['Point'][0]['z'])
                apdl_str += "k,2,{0},{1},{2}\n".format(sysdata['Point'][1]['x'], sysdata['Point'][1]['y'], sysdata['Point'][1]['z'])
                apdl_str += "k,3,{0},{1},{2}\n".format(sysdata['Point'][2]['x'], sysdata['Point'][2]['y'], sysdata['Point'][2]['z'])
                new_id = int(sysdata['id']) + 10
                apdl_str += "CSKP,{0},1,1,2,3,,\n".format(str(new_id))
                apdl_str += "kdele,1,3,1\n"
        else:
            for sys_data_i in sysdata:
                if sys_data_i['type'] == 'RotationalAxis':
                    point_data = []
                    for point in sys_data_i['Point']:
                        for k, v in point.items():
                            point_data.append(v)
                    points_data_dict[sys_data_i['id']] = point_data
                elif sys_data_i['type'] == 'Cylindrical':
                    apdl_str += "k,1,{0},{1},{2}\n".format(sys_data_i['Point'][0]['x'], sys_data_i['Point'][0]['y'], sys_data_i['Point'][0]['z'])
                    apdl_str += "k,2,{0},{1},{2}\n".format(sys_data_i['Point'][1]['x'], sys_data_i['Point'][1]['y'], sys_data_i['Point'][1]['z'])
                    apdl_str += "k,3,{0},{1},{2}\n".format(sys_data_i['Point'][2]['x'], sys_data_i['Point'][2]['y'], sys_data_i['Point'][2]['z'])
                    new_id = int(sys_data_i['id']) + 10
                    apdl_str += "CSKP,{0},1,1,2,3,,\n".format(str(new_id))
                    apdl_str += "kdele,1,3,1\n"
    ##############################   metarial  ########################
    # 创建材料APDL
    #超弹材料
    #!*  
    #TB,HYPE,5,1,2,NEO
    #TBTEMP,0
    #TBDATA,,0.01,0.004,,,,
    #
    #TB,HYPE,6,1,2,MOON  
    #TBTEMP,0
    #TBDATA,,0.01,0.02,0.004,,,
    # 
    #TB,HYPE,7,1,3,MOON   
    #TBTEMP,0
    #TBDATA,,0.001,0.02,0.03,0.004,,
    #
    #TB,HYPE,4,1,5,MOON  
    #TBTEMP,0
    #TBDATA,,11,3,2,4,4,4
    mat_maping_dict = {'Density': 'dens', 'Ex': 'ex', 'Nu': 'prxy', 'ALPX': 'ALPX', 'ALPY': 'ALPY', 'ALPZ': 'ALPZ','KXX':'KXX','KYY':'KYY','KZZ':'KZZ','HCAPACITY':'C'}

    matdata = xmldata['Global']['Material']
    if matdata.__class__ == dict:
        for k, v in matdata.items():
            if k != 'id' and k != 'name':
                apdl_str += "mp,{0},{1},{2}\n".format(mat_maping_dict[k], matdata['id'], v['value'])
    else:
        for mat_dict in matdata:
            for k, v in mat_dict.items():
                if k != 'id' and k != 'name':
                    apdl_str += "mp,{0},{1},{2}\n".format(mat_maping_dict[k], mat_dict['id'], v['value'])
    ##############################   ShellSection  ########################
    offsettypemap={"Buttom_Plane":"BOT"}
    if 'ShellSection' in xmldata['Global'].keys():
        shelldata = xmldata['Global']['ShellSection']
        if shelldata.__class__ == dict:
            apdl_str += "sect, {0}, shell,, {1}\n".format(shelldata['id'],shelldata['name'])
            layerdata = shelldata['LayerList']['Layer']
            for layer_i in layerdata:
                apdl_str += "secdata, {0}, {1}, {2}, {3}\n".format(layer_i['thickness'], layer_i['materialId'], layer_i['orientation'], layer_i['nIntPts'])
            apdl_str += "secoffset, {0}\n".format(offsettypemap[shelldata['Shell']['offset_type']])
            apdl_str += "seccontrol,, , , , , ,\n"
        else:
            for shell_dict in shelldata:
                apdl_str += "sect, {0}, shell,, {1}\n".format(shell_dict['id'], shell_dict['name'])
                layerdata = shell_dict['LayerList']['Layer']
                if layerdata.__class__ == dict:
                    apdl_str += "secdata, {0}, {1}, {2}, {3}\n".format(layerdata['thickness'], layerdata['materialId'], layerdata['orientation'], layerdata['nIntPts'])
                else:
                    for layer_i in layerdata:
                        apdl_str += "secdata, {0}, {1}, {2}, {3}\n".format(layer_i['thickness'], layer_i['materialId'], layer_i['orientation'], layer_i['nIntPts'])
                apdl_str += "secoffset, {0}\n".format(offsettypemap[shell_dict['Shell']['offset_type']])
                apdl_str += "seccontrol,, , , , , ,\n"
    ###############################  Model   ######################################

    #遍历组件进行单元属性和材料设置
    # 创建组件名和组件ID关系并对组件赋予材料
    com_id_name_dict = dict()
    com_num_dict = dict()

    for comp_dict in xmldata['PhysicsModel']['Model']['ComponentList']['Component']:
        #根据组件ID获取组件名
        com_id_name_dict[comp_dict['id']] = comp_dict['name']
        #获取组件节点或单元个数
        com_num_dict[comp_dict['id']] = comp_dict['num']
        #实体单元
        if comp_dict['meshtype'] == "Element":
            if 'SOLID' in comp_dict['etype'] or 'THERMAL' in comp_dict['etype']:
                apdl_str += "emodif,{0},mat,{1},\n".format(comp_dict['name'], comp_dict['materialId'])
        #壳单元
        if comp_dict['meshtype'] == "Element" and 'SHELL' in comp_dict['etype']:
            apdl_str += "emodif,{0},sec,{1},\n".format(comp_dict['name'], comp_dict['sectionId'])
        #平面单元
        if comp_dict['meshtype'] == "Element" and 'SOLID2D' in comp_dict['etype']:
            #平面应力单元
            if comp_dict['eLementAttribute'] == 'PlaneStress':
                #comp_dict['thickness']
                apdl_str += "emodif,{0},type,14,\n".format(comp_dict['name'])
            #平面应变单元
            if comp_dict['eLementAttribute'] == 'PlaneStrain':
                apdl_str += "emodif,{0},type,15,\n".format(comp_dict['name'])
            #轴对称单元
            if comp_dict['eLementAttribute'] == 'Axisymmetric':
                apdl_str += "emodif,{0},type,16,\n".format(comp_dict['name'])
        #contact52
        #EMODIF, P51X, TYPE, 20,
    # 边界识别
    ###############################  BCList   #####################################
    bclistdata = xmldata['PhysicsModel']['Model']['BCList']
    for k, v in bclistdata.items():
        # 固定约束
        if k == "FixedSupport":
            if v.__class__ == dict:
                apdl_str += "d,{0},all,0 \n".format(com_id_name_dict[v['compId']])
            else:
                for fixed_data in v:
                    apdl_str += "d,{0},all,0 \n".format(com_id_name_dict[fixed_data['compId']])
            print('ok')
        # 位移约束
        if k == 'Displacement':
            if v.__class__ == dict:
                if 'coordSysId' in v.keys():
                    apdl_str += "CSYS, {0}, \n".format(str(int(v['coordSysId'])+10))
                    apdl_str += "nrotat, {0} \n".format(com_id_name_dict[v['compId']])
                for k_d, v_d in v.items():
                    if k_d in ['UX', 'UY', 'UZ', 'RX', 'RY', 'RZ']:
                        k_d_new = k_d.replace("R", "ROT")
                        apdl_str += "d,{0},{1},{2} \n".format(com_id_name_dict[v['compId']], k_d_new, v_d['value'])
            else:
                for dis_data in v:
                    if 'coordSysId' in dis_data.keys():
                        apdl_str += "CSYS, {0}, \n".format(str(int(dis_data['coordSysId']) + 10))
                        apdl_str += "nrotat, {0} \n".format(com_id_name_dict[dis_data['compId']])
                    for k_d, v_d in dis_data.items():
                        if k_d in ['UX', 'UY', 'UZ', 'RX', 'RY', 'RZ']:
                            k_d_new = k_d.replace("R", "ROT")
                            apdl_str += "d,{0},{1},{2} \n".format(com_id_name_dict[dis_data['compId']], k_d_new, v_d['value'])
            apdl_str += "CSYS,0 \n"
            print('ok')
        
        # 节点力
        if k == 'NodalForce':
            node_num  = 1
            if v.__class__ == dict:
                #判断是否有坐标系选项
                if 'coordSysId' in v.keys():
                    apdl_str += "CSYS, {0}, \n".format(str(int(v['coordSysId'])+10))
                    apdl_str += "nrotat, {0} \n".format(com_id_name_dict[v['compId']])
                #增加节点合力选项
                if v['divideLoad'] != "false" :
                    node_num = int(com_num_dict[v['compId']])
                
                for k_d, v_d in v.items():
                    if k_d in ['FX', 'FY', 'FZ']:
                        apdl_str += "f,{0},{1},{2} \n".format(com_id_name_dict[v['compId']], k_d, str(int(v_d['value'])/node_num))
            else:
                for dis_data in v:
                    
                    if 'coordSysId' in v.keys():
                        apdl_str += "CSYS, {0}, \n".format(str(int(dis_data['coordSysId']) + 10))
                        apdl_str += "nrotat, {0} \n".format(com_id_name_dict[dis_data['compId']])
                    
                    #增加节点合力选项
                    if dis_data['divideLoad'] != "false" :
                        node_num = int(com_num_dict[dis_data['compId']])
                    
                    for k_d, v_d in dis_data.items():
                        if k_d in ['FX', 'FY', 'FZ']:
                            apdl_str += "f,{0},{1},{2} \n".format(com_id_name_dict[dis_data['compId']], k_d, str(int(v_d['value'])/node_num))
            apdl_str += "CSYS,0 \n"
            print('ok')

        # 节点扭矩
        if k == 'NodalMoment':
            if v.__class__ == dict:
                for k_d, v_d in v.items():
                    if k_d in ['MX', 'MY', 'MZ']:
                        apdl_str += "f,{0},{1},{2} \n".format(com_id_name_dict[v['compId']], k_d, v_d['value'])
            else:
                for dis_data in v:
                    for k_d, v_d in dis_data.items():
                        if k_d in ['MX', 'MY', 'MZ']:
                            apdl_str += "f,{0},{1},{2} \n".format(com_id_name_dict[dis_data['compId']], k_d,
                                                                  v_d['value'])
            print('ok')
        # 实体压力
        if k == 'Pressure':
            if v.__class__ == dict:
                for k_p, v_p in v.items():
                    if k_p in ['pressureSolid', 'pressureShell', 'other']:
                        apdl_str += "sf,{0},PRES,{1} \n".format(com_id_name_dict[v['compId']], v_p['value'])
            else:
                for pre_data in v:
                    for k_p, v_p in pre_data.items():
                        if k_p in ['pressureSolid', 'pressureShell', 'other']:
                            apdl_str += "sf,{0},PRES,{1} \n".format(com_id_name_dict[pre_data['compId']], v_p['value'])

            print('ok')
        # 加速度
        if k == 'Acceleration':
            if v.__class__ == dict:
                acel_value = dict()
                acel_value['AX'] = '0'
                acel_value['AY'] = '0'
                acel_value['AZ'] = '0'
                for k_a, v_a in v.items():
                    if k_a in ['AX', 'AY', 'AZ']:
                        print(k_a, v_a)
                        acel_value[k_a] = str(-1*float(v_a['value']))
                apdl_str += "acel,{0},{1},{2} \n".format(acel_value['AX'], acel_value['AY'], acel_value['AZ'])
            else:
                for acc_data in v:
                    acel_value = dict()
                    acel_value['AX'] = '0'
                    acel_value['AY'] = '0'
                    acel_value['AZ'] = '0'
                    for k_a, v_a in acc_data.items():
                        if k_a in ['AX', 'AY', 'AZ']:
                            acel_value[k_a] = str(-1*float(v_a['value']))
                    apdl_str += "acel,{0},{1},{2} \n".format(acel_value['AX'], acel_value['AY'], acel_value['AZ'])
            print('ok')
        # 角速度
        if k == 'AngularVelocity':
            if v.__class__ == dict:
                points = ",".join(str(i) for i in points_data_dict[v['coordSysId']])
                apdl_str += "cmomega,{0},{1},,,{2} \n".format(com_id_name_dict[v['compId']], str(float(v['Omega']['value'])), points)
            else:
                for Ang_data in v:
                    points = ",".join(str(i) for i in points_data_dict[Ang_data['coordSysId']])
                    apdl_str += "cmomega,{0},{1},,,{2} \n".format(com_id_name_dict[Ang_data['compId']], str(float(Ang_data['Omega']['value'])), points)
            print('ok')
        # 节点温度
        if k == 'NodalTemperature':
            if v.__class__ == dict:
                apdl_str += "bf,{0},temp,{1} \n".format(com_id_name_dict[v['compId']], v['TEMP']['value'])
            else:
                for temp_data in v:
                    apdl_str += "bf,{0},temp,{1} \n".format(com_id_name_dict[temp_data['compId']], temp_data['TEMP']['value'])
                print('ok')
        #对流换热
        #SF,COMPONENT33,CONV,5E-6,22
        if k == 'Convection':
            if v.__class__ == dict:
                apdl_str += "SF,{0},CONV,{1},{2} \n".format(com_id_name_dict[v['compId']], v['HF']['value'], v['BULK']['value'])
            else:
                for temp_data in v:
                    apdl_str += "SF,{0},CONV,{1},{2} \n".format(com_id_name_dict[temp_data['compId']], temp_data['HF']['value'], temp_data['BULK']['value'])
                print('ok')

        #生热
        #BFE,REYUAN,HGEN,1,0.01, , ,
        if k == 'HeatGeneration':
            if v.__class__ == dict:
                apdl_str += "BFE,{0},HGEN,1,{1},,, \n".format(com_id_name_dict[v['compId']], v['HEATD']['value'])
            else:
                for temp_data in v:
                    apdl_str += "BFE,{0},HGEN,1,{1},,, \n".format(com_id_name_dict[temp_data['compId']], temp_data['HEATD']['value'])
                print('ok')

    apdl_str += "ALLSEL,ALL \n"
    return apdl_str


def main():
    xmlfile = r'E:\huaweitrans\huawei\tiexin.xml'
    xmldata = xml2dict(xmlfile)
    apdl_str = trans_xmltoapdl(xmldata)
    with open('apdl.txt', 'w+') as f:
        f.write(apdl_str)
if __name__ == '__main__':
    main()
