def ConvertMorphToSizeBox(morphs_matrix, max_surface_length, max_volume_length):

	"""

	Script function that converts morphing boxes to size boxes.


	@morphs_matrix object: A list that contains morphing boxes.

	@max_surface_length float: (optional)Values for surface lengthand.

	@max_volume_length float: (optional)Values for surface length.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def DvgridStart(elements_flag):

	"""

	Script function for creating DVGRID's.


	@elements_flag integer: (optional)0: For all elements.
	1: For shells.
	2: For solids.
	(Default: 0)

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def DvgridStop(element, tolerance, ret_ent):

	"""

	Script function for creating DVGRID's.


	@element object: The DESVAR entity.

	@tolerance float: (optional)Used in order to ignore very small movements.

	@ret_ent boolean: (optional)If set to True, this function will return the DESVAR entity instead of its id.

	@returns object: Returns the desvar id on success, 0 on failure.
	If ret_ent is set to True, it returns the desvar entity instead.

	"""

def FEOutputName(filename):

	"""

	Script function to pass as argument the Output filename to the Optimization Task.


	@filename string: The path and the filename.

	@returns integer: Returns 1 on success, or 0 on failure.

	"""

def InputDV(filename):

	"""

	Script function to pass as argument the Design Variable filename to the Optimization Task.


	@filename string: The desired filename.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphAdjust(hatch):

	"""

	Script function for adjusting morph hatches.


	@hatch object: The morph hatch object, where the box will be adjusted.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphAlign(id_curve_or_plane , curve_or_plane, mpoints, flag):

	"""
	Deprecated since version 17.1.0. Use function AlignBoxPoints instead.

	Script function for the alignment of morph control points.


	@id_curve_or_plane integer: A curve or a working plane id.

	@curve_or_plane string: The type. 'c' for curve, 'w' for working plane.

	@mpoints object: A list of morph control point.

	@flag integer: This flag should be 1 for morphing or 0 for modifying only 
	edges without FE movement.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function AlignBoxPoints instead.", DeprecationWarning)

def MorphAlign3Grids(grid1, grid2, grid3, m1, flag):

	"""
	Deprecated since version 17.1.0. Use function AlignBoxPoints instead.

	Script function for the alignment of morph control points.


	@grid1 object: The first grid element to define a plane.

	@grid2 object: The second grid element to define a plane.

	@grid3 object: The third grid element to define a plane.

	@m1 object: A list of morph control point to align.

	@flag integer: This flag should be 1 for morphing or 0 for modifying 
	only edges without FE movement.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function AlignBoxPoints instead.", DeprecationWarning)

def MorphBoxDel(boxes):

	"""

	Script function to delete morph boxes.


	@boxes object: An object or list containing the morph elements to be deleted.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphBoxUndel(morphes):

	"""

	Script function for undelete a morph box


	@morphes object: A list containing the morph elements that will be undeleted.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphByPoints(points, solid_type):

	"""

	Script function for creating 3D morph boxes from existing nodes or edges, shells.


	@points object: A list with entities from where 5,6,7 or 8 points will be taken to
	create TETRA, PYRAMID, PENTA or HEXA box.

	@solid_type string: (optional)Defines the solid type in case that the input points could be used for the creation
	of more than one solid types. It takes the values "hexa", "penta", "tetra" or "pyramid".

	@returns object: Returns a reference to the created morph on success, or 0 on failure.

	"""

def MorphCalcDvgrid(morph_points, directory, entities_flag):

	"""

	This function calculates Dvgrid values and produces the corresponding files based on unity movement of morphing points.


	@morph_points object: A list containing morph point entities.

	@directory string: The path to the directory where the produces files will be saved.

	@entities_flag integer: (optional)Select which elements types to use.
	
	for shells and solids select 0 (zero). Default
	for only shells select 1.
	for only solids select 2.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphContents(morphes):

	"""
	Deprecated since version 21.0.0. Use function CollectEntities instead.

	Script function for acquiring morph contents.


	@morphes object: A list containing morph entities.

	@returns object: Returns a list of entities on success, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use function CollectEntities instead.", DeprecationWarning)

def MorphConvert(convert_type, entities, options):

	"""

	Script function for converting morph entities.


	@convert_type string: The type of the desired conversion, that can be one of these:
	"MorphToHexa", to convert morphes to HexaBoxes
	"MorphToSizeBox", to convert morphes to SizeBoxes
	"MorphFacesToGeo", to convert morphing faces to geometrical faces
	"MorphEdgesToCurve", to convert morphing edges to geometrical curves
	"Morph2DTo3D", to convert morphes from 2D to 3D
	"MorphCylindricalToOrtho", to convert morphes from Cylindrical to ortho-box
	"Unlink", unlink boxes (morphing boxes, size boxes or hexa-block boxes)
	"SizeBoxToHexa", convert size box to hexa-block box
	"ConvertToDeckBox", convert boxes (morphing boxes, size boxes or hexa-block boxes) 
	to deck boxes
	"SizeBoxCylindricalToOrtho",  to convert size box from Cylindrical to ortho-box

	@entities object: A list containing the entities to convert.

	@options integer: (optional)A dictionary that contains pairs of arguments. The pairs that can be
	assigned are the following:
	1) "MorphToSizeBox": 'max_surface_length': float, 'max_volume_length': float
	2) "MorphFacesToGeo": 'paste_cons': boolean, 
	'fillet_shape': 'Round' or 'Planar' or 'None' (string), 'radius': float
	3) 'MorphCylindricalToOrtho', 'Morph2DTo3D': 'delete_original': boolean

	@returns object: Returns a list of entities on success, or 0 on failure.

	"""

def MorphCylindrical(curve, rad1, rad2, auto_sort):

	"""

	Script function for creating a cylindrical morph box.


	@curve object: A list of CURVEs or POINTs.

	@rad1 float: The inner radius of the cylinder.

	@rad2 float: The outer radius of the cylinder.

	@auto_sort boolean: (optional)True (default): The order of objects in curve list will be reorder 
	in order to have an improved result.
	False: The order of objects in curve list will be preserved.

	@returns object: Returns a reference to the newly created cylindrical morph on success, or 0 on failure.

	"""

def MorphDepress(curve, set, matrix):

	"""

	Script function for the creation of depressions


	@curve object: A curve object.

	@set object: A set object were the depression will be applied.

	@matrix object: A list with 6 entries: Width, Height, Rows, Element length (if negative or zero average will be used), 
	Type (should be one of "Box", "Triangle", "Trapezoid", "Ellipse"), Flat width.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphDirectFit(Origin_Target, Entities, Bounds):

	"""

	Script function for direct morphing fit.


	@Origin_Target object: A list of origin and target curves|cons. Origin and target are kept into pairs.
	Odd index keeps the origin curve|cons and the next index keeps the target curve.

	@Entities object: A list of entities that will be morphed.

	@Bounds object: A list of curves/cons that will be used as bounds.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphEdgeFit(origin_target, edge_fit_add_flag, morphing_flag):

	"""

	Script function for fitting morph edges on to curves.


	@origin_target object: A list of lists with morph edges - curves or a dictionary containing 
	tuples of morph edges - curves.

	@edge_fit_add_flag boolean: (optional)The auto insertion of morph control point.
	True to add or False for no auto insertion.

	@morphing_flag boolean: (optional)True for morphing, or False for modifying only 
	edges without FE movement.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphFacesAccordingNodes(faces):

	"""

	Script function for applying node deformations to different geometries. 
	This script function is used for morphing geometry faces to a new position,
	according to the movement of their shell mesh.


	@faces object: A list of geometry faces.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphFlagStatus(morphing_flags, set_morphing_flags):

	"""

	Script function for reporting and setting morph flags status.


	@morphing_flags string: One of the following ANSA.defaults values:
	"BOXINBOX_MORPHING", "LOAD_MORPH_POINTS", "FREEZE_CHECK",
	"MORPHING_FLAG", "LOAD_FE_MODEL", "LOAD_NODES",
	"LOAD_FACES", "LOAD_CURVES", "APPLY_TANGENCY",
	"MORPH_TRANSLATE_POINTS", "MORPH_FORCE_FROZEN_ENTS", "PRESERVE_LOCAL_SHAPE","MORPH_INNER_RADIUS", "MORPH_SPIN_ALL_EDGES", "MORPH_MOVE_ALL_INNER"
	and values that are not stored in ANSA.defaults and replace old functions 
	like MorphReconstruct, MorphSmooth, MorphEdgeFitAdd:
	"AUTO_RECONSTRUCT", "AUTO_SMOOTH", "EDGE_FIT_ADD".

	@set_morphing_flags boolean: (optional)Set the desired value (True or False).

	@returns integer: Returns the value of each flag (1: true 0: false), or -1 on failure.

	"""

def MorphHistory():

	"""

	Script function for recording history states.


	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphHistoryState(history_state):

	"""

	Script function for applying morph history states.


	@history_state object: The history state to be applied.

	@returns integer: Returns the id on success, or 0 on failure.

	"""

def MorphInner(morph, dist):

	"""

	Script function for the insertion of a morphing box's inner edges.


	@morph object: The cylindrical morph.

	@dist float: The desired position in range 0-1 (parametric).

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphInsert(pnt1, pnt2, edg, s):

	"""

	Script function for the insertion of morph control points.


	@pnt1 object: The first morph control point to get direction.

	@pnt2 object: The second morph control point to get direction.

	@edg object: A morph edge element.

	@s string: A parameter in the 0-1 range or an approximate distance (~distance).

	@returns integer: Returns the new id on success, 0 on failure.

	"""

def MorphJoin(hatch, flag):

	"""

	Script function for joining a morph hatch.


	@hatch object: The morph hatch element that will be joined.

	@flag integer: A flag for leaving or deleting the morph points that are left from 
	joined hatches. (1 or 0)

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphLoad(morphes_to_load, entities_to_load, db_or_visib, strict_project, keep_loaded):

	"""

	Script function for loading elements and nodes to a morphing box.


	@morphes_to_load object: A list of target morphing boxes.

	@entities_to_load object: (optional)A list containing the elements to be loaded.

	@db_or_visib string: (optional)A string to indicate Database or Visible elements to be included.
	Accepted values: "DB" or "Visib".

	@strict_project boolean: (optional)A boolean flag to exclude nodes very close, but outside the boundary of the morph box

	@keep_loaded boolean: (optional)A flag to append any new entities to already existing ones

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphMappingDeformations(deformation_parameter, moved_elements, sampling_points, work_on_visible, bound_entities, max_displacement):

	"""

	Script function for applying node deformations to different geometries.
	This script function can be used in two modes:
	-Apply morphing on geometry by having defined already the "Deformation parameters".
	 The initial geometry will be moved to the final position of the "Deformation parameters". 
	-Move the initial Geometry on the FE(that has been morphed) according to node deformations that can been read by a text file.


	@deformation_parameter object: Can be one of the following:
	-Morphing deformation parameter.
	-Morphing History states.
	-OpenFoam Sensitivities.
	-Nastran DESVAR.
	-Text file with values (x , y , z, dx, dy, dz).

	@moved_elements object: A list with objects to be morphed.

	@sampling_points integer: A maximum number of sampling points in order to filter very large inputs.

	@work_on_visible boolean: To work on visible items or not.

	@bound_entities object: (optional)Set to True to create auto bound or list with the bound nodes or entities.

	@max_displacement float: (optional)Set the maximum displacement for the deformation. All values will be scaled accordingly.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphMinMax(coordinate,min_xyz,max_xyz):

	"""

	Script function for creating a morph box from two points (min, max).


	@coordinate object: The coordinate element (None for global).

	@min_xyz object: A list containing minimum coordinates (xmin, ymin, zmin).

	@max_xyz object: A list containing maximum coordinates (xmax, ymax, zmax).

	@returns integer: Returns the newly created morph object on success, or 0 on failure.

	"""

def MorphMove(morph_points,  morph_edges, flag, dist):

	"""

	Script function for the movement (SLIDE/EXTEND) of morph control points.


	@morph_points object: A list with morph control poits.

	@morph_edges object: A list with morph edges.

	@flag integer: Should be 1 for morphing or 0 for modifying only edges, 
	without FE movement.

	@dist float: The distance of the movement.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphMultBox(coord, load, min_flag, factor):

	"""

	Script function for the creation of multiple morph boxes.


	@coord object: The coordinate element (None for global).

	@load object: Defines if the box will contain the visible (1) or the DB(0)
	or a list of user defined elements( shells, parts etc ).

	@min_flag integer: Corresponds to the type of the created box. When min_flag equals 1, 
	then the created box obeys the minimum volume contraint. 
	If min_flag equals 0, then the created box is a typical orthogonal box.

	@factor float: The scale factor.

	@returns object: Returns a list with the newly created morph objects on success, or 0 on failure.

	"""

def MorphMultBoxAbsDis(coord, load, min_flag, distance, boxesType):

	"""

	Script function for the creation of multiple morph boxes. By using this function, the
	user has two options, either to create an O-ring or a Hexa type structure of multiple
	boxes. The description of the arguments follows:


	@coord object: The coordinate element (None for global).

	@load object: Defines if the box will contain the visible (1), the DB (0) or 
	a list of user defined elements (shells, parts etc).

	@min_flag integer: Corresponds to the type of the created box. When min_flag equals 1, 
	then the created box obeys the minimum volume contraint. 
	If min_flag equals 0, then the created box is a typical orthogonal box.

	@distance float: The distance from the faces of the initial morphing box, to which the multiple 
	boxes are extended.

	@boxesType integer: The type of the structure. If you want an O-ring structure, 
	then boxesType has to be equal to 0. If you want a Hexa structure, 
	then boxesType should equal to 1.

	@returns object: Returns a list with the newly created morph objects on success, or 0 on failure.

	"""

def MorphNested(set, reference_grid):

	"""

	Function for creating a morphing nested entity.


	@set object: A set of entities. The nested will use the grids of the elements of the set.

	@reference_grid object: The grid that will be the reference grid of the nested. If this value is None, 
	then the reference grid will be the center of gravity.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphNumber(morph_edge, string):

	"""

	Script function for the insertion of any number of morph control points.


	@morph_edge object: A box edge or a list of box edges.

	@string string: A number or a symbol (+/-).

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphOffset(morph_hatces, offset_value, flag_morphing):

	"""

	Script function for offsetting morph hatches.


	@morph_hatces object: A list with morph hatch elements.

	@offset_value float: The offsetting value.

	@flag_morphing integer: 1: For morphing.
	0: For modifying only edges without FE movement.

	@returns object: Returns 1 on success, or 0 on failure.

	"""

def MorphOffsetBox(morph_hatches, offset_value):

	"""

	Script function for creating morphing boxes by setting an offset to some morph hatches.


	@morph_hatches object: A morph hatch elements.

	@offset_value float: The offsetting value.

	@returns object: Returns a list with the newly created morph objects on success, or 0 on failure.

	"""

def MorphOneDimCreate(curves_list, load_radius, part):

	"""

	Script function for creating one dimensional morphes.


	@curves_list object: A list with curves or points to create the one dimensional morph.

	@load_radius float: The load radius of the crated morph.

	@part object: (optional)The part to add the created morph (None for default).

	@returns object: Returns the newly created morph object on success, or 0 on failure.

	"""

def MorphOrtho(loaded_elements, db_or_visible, coordinate, min_flag):

	"""

	Script function for the creation of a morph box.


	@loaded_elements object: (optional)A list with elements to be loaded in the created morph.

	@db_or_visible string: (optional)Can have values 'DB' or 'Visible' for elements to be loaded in the created morph.

	@coordinate object: (optional)A local coordinate object instead of global.

	@min_flag boolean: (optional)True or False for minimum volume morph.

	@returns object: Returns the newly created morph object on success, or 0 on failure.

	"""

def MorphParPrj(dx, dy, dz, morph, morph_edge):

	"""

	Script function for the projection of x,y,z on a morph edge.


	@dx float: The x coordinate of the point to project.

	@dy float: The y coordinate of the point to project.

	@dz float: The z coordinate of the point to project.

	@morph object: The morph box element to which the edge belongs.

	@morph_edge object: The morph edge element.

	@returns integer: Returns the new id on success, or 0 on failure.

	"""

def MorphParam(param, dist):

	"""

	Script function for editing morph parameters.


	@param object: The parameter element.

	@dist float: The value that will be applied in the parameter.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphParamCreate(name, type, arguments_list):

	"""

	Script function for the creation of a morph parameter.
	
	It uses other script functions to create a morph parameter.


	@name string: is the desired name for the new parameter

	@type string: type can be one of the following parameter types:
	"MorphTransl" -- it will create a Transform- Translate parameter.
	arguments_list: object is a list with 5 entries
	list morph_points
	coordinate system object
	dx, dy, dz translate vector
	"MorphTransform" -- it will create a Transform- Transform parameter.
	arguments_list: object is a list with 2 entries
	list morph_points and list transform entities (points or coordinates)
	"MorphScale" -- it will create a Transform- Scale parameter.
	arguments_list: object is list with 4 entries
	list morph_points
	scale points cordinates origin_x, origin_y, origin_z
	"MorphRotate" -- it will create a Transform- Rotate parameter.
	arguments_list: object is list with 8 entries
	list morph_points
	coordinate system object
	dx, dy, dz vector
	origin_x, origin_y, origin_z origin position
	"arguments_list: object is a list with 5 entries
	list morph_points
	"MorphAlign" == it will create an Transform -Align parameter
	arguments_list: is an object created by MorphCreateMorphAlignArgs
	"MorphUserTang" -- it will create an User Tangent parameter.
	arguments_list: object is list with 1 entry
	list morph_user_tangency
	"MorphAngle" -- it will create an Angle parameter.
	arguments_list: object is list with 1 entry
	list morph_edges in stady-moved format
	"MorphDeform" -- it will create a Deformation parameter.
	arguments_list: object is list with 1 entry
	integer flag for affected 0:All, 1: Moved
	"MorphEdgeFit" -- it will create an EdgeFit parameter.
	arguments_list: object is list with 2 entries
	list morph_edges
	list curves
	"MorphMove" -- it will create an Extend parameter.
	arguments_list: object is list with 2 entries
	list morph_points
	list morph_edges
	"MorphOffset" -- it will create an Offset parameter.
	arguments_list: object is list with 1 entry
	list of morph_faces
	"MorphRadius" -- it will create a Radius parameter.
	arguments_list: object is list with 1 entry
	list of morph_faces 
	"MorphInner" -- it will create an Inner parameter.
	arguments_list: object is list with 1 entry
	list of morph_concentric_edges 
	"MorphSetsAlign" -- it will create a Direct Align parameter.
	arguments_list: object is list with 5 entries
	set object of elements to be included
	set object of elements to move as rigid
	set of elements to retain position
	set of elements to align to
	align distance
	"MorphSetsOffset" -- it will create a Direct Offset parameter.
	arguments_list: object is list with 3 entries
	set of elements to be included
	set of elements to move as rigid
	set of elements to retain position
	"MorphSetsTranslate" -- it will create a Direct Translate parameter.
	arguments_list: object is list with 6 entries
	set of elements to be included
	set of elements to move as rigid
	set of elements to retain position
	dx, dy, dz
	"MorphSetsRotate" -- it will create a Direct Rotate parameter.
	arguments_list: object is list with 9 entries
	set of elements to be included
	set of elements to move as rigid
	set of elements to retain position 
	dx, dy, dz, origin_x, origin_y, origin_z
	"DFMTranslate" -- it will create a DFM Translate parameter.
	arguments_list: object is list with 6 entries
	list entities or list of matrices of lists to be translated
	list [dx, dy, dz] or list of lists [dx, dy, dz] with the translate vector(s),
	list of entities to be morphed,
	list of bounds,
	C.Entities Sampling flag: 0 to disable sampling, 1 to sample points from perimeters
	Auto Bounds flag: 1 to activate automatic bounds recognition, 0 otherwise.

	@arguments_list

	@returns integer: Returns the id of the created parameter on success, 0 on failure.

	"""

def MorphPaste(hatch1, hatch2, paste_on_middle):

	"""

	Script function for pasting 2 free morph hatches.


	@hatch1 object: The first object of a free morph hatch.

	@hatch2 object: The second object of a free morph hatch.

	@paste_on_middle boolean: (optional)A flag that defines whether to paste on middle plane (True) 
	or not (False-default value).

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphPntSnap(grid_point, morph_point, flag):

	"""

	Script function for the movement of morph control points.


	@grid_point object: The grid point to get coordinates.

	@morph_point object: The morph control point to move.

	@flag integer: Should be 1 for morphing or 0 for modifying only edges, 
	without FE movement.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphPointDel(morph_points):

	"""

	Script function for the deletion of morph control points.


	@morph_points object: A list of morph control points.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphProject(x, y, z, morph_edge):

	"""

	Script function for the projection of x,y,z on a morph edge.


	@x float: The x global coordinate.

	@y float: The y global coordinate.

	@z float: The z global coordinate.

	@morph_edge object: The morph edge element.

	@returns integer: Returns the id of the new Control Point on success, or 0 on failure.

	"""

def MorphRMDBL(tolerance):

	"""

	Script function for deleting close control points in all visible morphes.


	@tolerance float: The tolerance where close points will be searched.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphRadius(morph_hatces, d, flag):

	"""

	Script function for changing the radius of cylindrical morph hatches.


	@morph_hatces object: A list with morph hatch elements of cylindrical morphes.

	@d float: The new radius for the hatces.

	@flag integer: 1 for morphing or 0 for modifying only edges, 
	without FE movement.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphRelocate(morph_edges):

	"""

	Script function for relocating control points in morph edges.


	@morph_edges object: A list of morph edges elements, in order for their middle 
	control points to be equally distributed over the edge.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphRmTang():

	"""

	Script function for removing all tangency from all visible morphes.


	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphScale(morph, flag, d1, d2, d3, d4):

	"""

	Script function for scaling a morph.


	@morph object: The morph element that will be copied.

	@flag integer: 1 or 0 to morph or not the loaded elements.

	@d1 float: The scale factor.

	@d2 float: The x global coordinate of the base point.

	@d3 float: The y global coordinate of the base point.

	@d4 float: The z global coordinate of the base point.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphResult(directory, openfoam_gw, max_displacement):

	"""

	Script function for result based morphing.


	@directory string: Output directory.

	@openfoam_gw string: Gw openfoam filename.

	@max_displacement float: Maximium displacement.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphSplit(box_points, non_isoparam, fit_new_skin_edges, box_edges, number_of_splits, work_on):

	"""
	Deprecated since version 21.0.0. Use class BoxSplit instead.

	Script function for splitting morph box(es). 
	The split can be performed either isoparametrically or at two different parameters in opposite edges.
	In the first case the user can provide one morphing point or a list of morphing points in which the 
	split will be performed and travelled throughout the box in the same parameter. In the second case 
	the user must provide a list of morphing points where each and every pair of them gives the starting 
	and the ending point of the split. For example, if the user provides a list with four morphing points, 
	a non-isoparametrical split (cut) will be performed for the first and the second point in the list and 
	another one for the third and fourth one. If the box points list has an odd number of points, the last 
	point will be ignored except for the case of a single point where isoparametrical split will be performed. 


	@box_points object: (optional)A box point or a list of box points, where the box(es) will be cut.

	@non_isoparam boolean: (optional)For a non-isoparametrical split (cut), this value should be set to 'True'.

	@fit_new_skin_edges boolean: (optional)If set to True, new skin edges will fit on the underlying model.
	Default value is False.

	@box_edges object: (optional)A box edge or a list of box edges, where the box(es) will be cut
	according to the number of splits that is defined (argument 
	"number_of_splits").

	@number_of_splits integer: (optional)Defines the number of splits on the input box edges (argument 
	"box_edges")

	@work_on string: (optional)Defines where the projection is going to take place:
	'whole_db' fit skin edges will take place on the whole database,
	'visible'  fit skin edges will take place only on the visible elements
	If work_on is not set then whole_db will be the default argument.
	This option is only available only when fit_skin_edges is set to true.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class BoxSplit instead.", DeprecationWarning)

def MorphTangent(entities):

	"""

	Script function for the creation of tangency between morph edges or morph boxes. 


	@entities object: A list of morph edges or morph boxes.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphTopoVis(tolerance):

	"""

	Script function for connecting all visible morphing boxes. Available option for
	the definition of topology tolerance mode.


	@tolerance string: (optional)A string to define the tolerance mode, accepting
	"draft", "middle", "fine" or "extra fine".
	Default mode depends on Resolution/Tolerances/Units
	and Morph/Optimization settings.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphTransl(m1, p1, dx, dy, dz):

	"""

	Script function for the translation of morph control points.


	@m1 object: A list of morph control points.

	@p1 object: A valid coordinate element or None for global.

	@dx float: The x component of the vector.

	@dy float: The y component of the vector.

	@dz float: The z component of the vector.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphUserTangent(m1, dx, dy, dz):

	"""

	Script function for the definition or modification of user tangents at morph control points.


	@m1 object: A list that contains the morph control points and edges where 
	user tangents will be created. Definition of morph edges is 
	necessary in cases that we want to create user tangents on 
	corner points. For intermediate points, there is no need to
	define edges. In cases that we want to create user tangents on 
	corner points, matrix should contain the control point, 
	followed by its edge.

	@dx float: The x component of the user defined tangent.

	@dy float: The y component of the user defined tangent.

	@dz float: The z component of the user defined tangent.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def PerformDoeStudy(opt_task_id, comb_file, dir_path, solver, solver_session_file, post_processing, meta_session_file, meta_response_file, empty_experiments_directory, single_directory, pre_processing, save_database, dm_signature):

	"""

	Function to perform a DOE study.


	@opt_task_id integer: Define the id of the optimization task you want to run.

	@comb_file string: Define the path of the file that contains the combinations 
	you want to run.

	@dir_path string: Define the directory you want to save the experiments.
	The value "DM:" must be used in order for the Experiments to be automatically uploaded to DM

	@solver string: (optional)Defines the solver that will be used in DOE. Supported solvers 
	are "NASTRAN", "LS-DYNA", "PAMCRASH", "ABAQUS", "ANSYS",
	"EPILYSIS", "FLUENT" and "FLUENT 2D".

	@solver_session_file string: (optional)The path of the session file necessary to run a solver. Session 
	file is essential for running Ansys.

	@post_processing string: (optional)Defines if META will be used after running solver. Accepted 
	keyword's values are "Meta" and "None".

	@meta_session_file string: (optional)The path of the session file that META requires.
	(without it, META cannot run)

	@meta_response_file string: (optional)The name of the response file that META will generate. 
	This keyword is optional for running META (by default, 
	response filename is "response.txt").

	@empty_experiments_directory boolean: (optional)Define if experiments' directory will be emptied 
	before the generation of the new experiments.
	(Default: False)

	@single_directory boolean: (optional)Define if all output files are saved in a single directory.
	(Default: False)

	@pre_processing string: (optional)Accepted values are "based_on_current" and "create_experiments".
	It defines if DOE will be performed to existing experiments or it will 
	create new.
	(Default: "create_experiments")

	@save_database boolean: (optional)Define if ANSA database is saved for every experiment.
	(Default: False)

	@dm_signature object: (optional)The Simulation Run signature for DM, defining the Simulation_Model and LoadCase where the Runs will be stored under.
	This argument must be a dictionary with keys: "Simulation_Model" and "LoadCase"
	and values dictionaries for the respective names/values.

	@sim_run_save_action string: (optional)Specify this argument in case of "DM:". By using "DOE Iteration" value, initial state will additionally run.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphEdgeFitOnSurfs(edges, surface_ents, add_pnts, search_distance, user_projection_mode_vector):

	"""

	A function to fit box edges on target surface (target surface can be defined by shells and geometrical faces).


	@edges object: A list with morph edges.

	@surface_ents object: A list of entities, parts, properties, materials, sets or macros.
	If it equals to 0, the visible shells and/or faces are collected.

	@add_pnts integer: A flag to define the auto insertion of control point on box edges.
	Set it 1 for auto insertion and 0 for no auto insertion.

	@search_distance float: (optional)A search distance for projection.

	@user_projection_mode_vector object: (optional)A list with a user projection vector [dx,dy,dz].

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphParamMerge(parameters):

	"""

	Function for merging morph parameters.


	@parameters object: A list containing morph parameters to be merged.
	(Should be of the same type)

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphInnerMod(edge, morph_entities, ddiam):

	"""

	Function that modifies the inner cylindrical edges of cylindrical boxes.


	@edge object: The inner cylindrical morphing edges that will be changed.

	@morph_entities integer: 1 if you want the action to perform morph at the entities loaded to the box, 
	0 otherwise.

	@ddiam float: Value that will be added to the diameter of the inner edge of the box.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphSlFeatureCurve(elements, curve, dist, orient, copy):

	"""
	Deprecated since version 21.1.0. Use class DCFeatureSlide instead.

	Function for sliding a feature onto a curve, following the curvature of the surface.


	@elements object: A list of connected elements.

	@curve object: A curve to follow.

	@dist float: The distance on curve.

	@orient integer: Set to 1 to follow the curve's orientation, or 0 to retain the initial orientation.

	@copy integer: Set to 0 to move the selected feature or define the number (steps) of new features 
	that would be generated.

	@returns object: Returns a list of lists on success:
	    The list contains 1 list in case of move, (N+1) lists in case of copy.
	    The first element of the list is a list of the initial shells (updated in case of copy).
	    The rest elements of the list are also lists generated only in case of copy. Each list contains a new created feature.
	Returns None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.1.0. Use class DCFeatureSlide instead.", DeprecationWarning)

def MorphSlFeatureRotate(elements, p1, angle, origin_x, origin_y, origin_z, dx, dy, dz, copy):

	"""
	Deprecated since version 21.1.0. Use class DCFeatureSlide instead.

	Function for rotating a feature onto its surface.


	@elements object: A list of connected elements.

	@p1 object: A valid coordinate element or None for global.

	@angle float: The rotational angle.

	@origin_x float: The x coordinate of the origin point.

	@origin_y float: The y coordinate of the origin point.

	@origin_z float: The z coordinate of the origin point.

	@dx float: The x component of the rotational vector.

	@dy float: The y component of the rotational vector.

	@dz float: The z component of the rotational vector.

	@copy integer: Set to 0 to move the selected feature or define the number (steps) of new features 
	that would be generated.

	@returns object: Returns a list of lists on success:
	    The list contains 1 list in case of move, (N+1) lists in case of copy.
	    The first element of the list is a list of the initial shells (updated in case of copy).
	    The rest elements of the list are also lists generated only in case of copy. Each list contains a new created feature.
	Returns None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.1.0. Use class DCFeatureSlide instead.", DeprecationWarning)

def MorphSlFeatureTransl(elements, p1, dist, dx, dy, dz, copy):

	"""
	Deprecated since version 21.1.0. Use class DCFeatureSlide instead.

	Function for translating a feature onto its surface.


	@elements object: A list of connected elements.

	@p1 object: A valid coordinate element or None for global.

	@dist float: The translational distance.

	@dx float: The x component of the translational vector.

	@dy float: The y component of the translational vector.

	@dz float: The z component of the translational vector.

	@copy integer: Set to 0 to move the selected feature or define the number (steps) of new features 
	that would be generated

	@returns object: Returns a list of lists on success:
	    The list contains 1 list in case of move, (N+1) lists in case of copy.
	    The first element of the list is a list of the initial shells (updated in case of copy).
	    The rest elements of the list are also lists generated only in case of copy. Each list contains a new created feature.
	Returns None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.1.0. Use class DCFeatureSlide instead.", DeprecationWarning)

def MorphSweepGlide(extrusion_type, guideline_ents, box_face, curves, points, section_type, radius, width, dx, dy, dz, height, lower_base, upper_base):

	"""

	Function for creating a morph box through extrusion. Both 'sweep' and 'glide' extrusion types are supported. 
	
	The direction of the extrusion is defined through curves, or points, or a combination of them.
	Curves may form a connected or disconnected path (a path will be automatically created).
	Note that single points are ignored (i.e. if any points are to be used, they should be at least two).
	
	The user has four options in defining the cross section, one with a box face, one with curves, 
	one with curves and points and, finally, one with a predefined shape.
	The box_face option expects a single box face entity (which will be pasted to the new one after creation of the box) 
	The curves option expects one or more curves (unconnected ones will be automatically connected to form 
	a closed cross section shape). The selected curves should contain at least 4 points, so that they can 
	be adopted for the definition of the four box edges.
	The points option should only follow a previous curves-curve_entities pair, and explicitly defines the 
	points to be used for the four box edges definition. These points should be part of the curve_entities provided. 
	The predefined cross section includes a circular with the required radius, a square with its side 
	length, a rectangular with its width and height, and a trapezoidal with its two bases' lenths and 
	height. Except for the circular, these cross sections also require a vector defining the 'height' 
	direction of the cross section.
	Note that several kind of edges may be used as a curve, including element edges (provided as edge sets), 
	CONS, 3D curves and box edges. Similarly, grids, hot points and box edge corner points may be employed 
	for any point entities.


	@extrusion_type string: One of "sweep" or "glide", denoting the type of the extrusion.

	@guideline_ents object: A list of entities defining the direction of the extrusion 
	(collection of curves and/or points).

	@box_face object: (optional)A box face entity to be used as a cross section 
	(note that new face will be pasted to old).

	@curves object: (optional)A list of curve entities defining the cross section 
	(they do not have to form a closed perimeter).

	@points object: (optional)A list of point entities defining the position of the box edges 
	(used only in conjunction with 'curves'). Note that points should 
	be among the points of the curve_entities provided above.

	@section_type string: (optional)A string specifying the predefined section type ("circular", "square", 
	"rectangular", trapezoidal").
	Additional data needed per case:
	-"circular" requires "radius".
	-"square" requires "width" and  height direction "dx","dy","dz".
	-"rectangular" requires "width", "height", and height direction "dx","dy","dz".
	-"trapezoidal" requires "lower_base", "upper_base", "height", and height 
	  direction "dx","dy","dz".

	@radius float: (optional)In case of "circular" section_type, the radius of the cross section.

	@width float: (optional)In case of "square" section_type, the width of the cross section.

	@dx float: (optional)In case of "square", "rectangular" or "trapezoidal" section_type, 
	the x-component of the vector defining the section's height direction
	(does not need to be normalized).

	@dy float: (optional)In case of "square", "rectangular" or "trapezoidal" section_type, 
	the y-component of the vector defining the section's height direction 
	(does not need to be normalized).

	@dz float: (optional)In case of "square", "rectangular" or "trapezoidal" section_type, 
	the z-component of the vector defining the section's height direction 
	(does not need to be normalized).

	@height float: (optional)In case of "rectangular" or "trapezoidal" section_type, the height of 
	the cross section.

	@lower_base float: (optional)In case of "trapezoidal" section_type, the length of the sections' lower base.

	@upper_base float: (optional)In case of "trapezoidal" section_type, the length of the sections' upper base.

	@returns object: Returns a list with references to the newly created morph boxes.

	"""

def MorphCornerPoints(boxes):

	"""

	A function that collects corner points of morphing boxes. 
	Note that this function collects the corner points per box, so the common 
	points (belonging to common box faces) will be collected multiple times.


	@boxes object: An object or list with the morphing box entities.

	@returns object: Returns a list of entities on success, or 0 on failure.

	"""

def MorphParamCreateTranslate(name, morph_points, coord, dx, dy, dz):

	"""
	Deprecated since version 17.1.0. Use function NewParameterTranslate instead.

	Function for the creation of a tranlsate morph parameter for morph points.


	@name string: The desired name for the new parameter.

	@morph_points object: A list of morph points.

	@coord object: A coordinate system that the displacement vector will be defined.
	If coord is None, the global coordinate system will be used.

	@dx float: The x component of the displacement vector.

	@dy float: The y component of the displacement vector.

	@dz float: The z component of the displacement vector.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterTranslate instead.", DeprecationWarning)

def MorphParamCreateEdgeFit(name, morph_edges, curves):

	"""
	Deprecated since version 17.1.0. Use function NewParameterEdgeFit instead.

	Script function for the creation of an edge fit morph parameter for morph edges.


	@name string: The desired name for the new parameter.

	@morph_edges object: A list of morph edges.

	@curves object: A list of curves.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterEdgeFit instead.", DeprecationWarning)

def MorphParamCreateExtend(name, morph_points, morph_edges):

	"""
	Deprecated since version 17.1.0. Use function NewParameterExtend instead.

	Script function for the creation of an extend morph parameter for morph boxes.


	@name string: The desired name for the new parameter.

	@morph_points object: A list of morph points.

	@morph_edges object: A list of morph edges.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterExtend instead.", DeprecationWarning)

def MorphParamCreateOffset(name, morph_faces):

	"""
	Deprecated since version 17.1.0. Use function NewParameterOffset instead.

	Script function for the creation of an offset morph parameter for morph faces.


	@name string: The desired name for the new parameter.

	@morph_faces object: A list of morph faces.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterOffset instead.", DeprecationWarning)

def MorphParamCreateRadiusOuter(name, morph_faces):

	"""
	Deprecated since version 17.1.0. Use function NewParameterRadiusOuter instead.

	Script function for the creation of a radius outer morph parameter for cylindrical morph boxes.


	@name string: The desired name for the new parameter.

	@morph_faces object: A list of circular faces of cylindrical morph boxes.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterRadiusOuter instead.", DeprecationWarning)

def MorphParamCreateRadiusInner(name, concentric_edges):

	"""
	Deprecated since version 17.1.0. Use function NewParameterRadiusInner instead.

	Script function for the creation of a radius inner morph parameter for cylindrical morph boxes.


	@name string: The desired name for the new parameter.

	@concentric_edges object: A list of concentric edges.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterRadiusInner instead.", DeprecationWarning)

def MorphParamCreateSetsAlign(name, s_elements, s_aligned, s_retained, s_target, search_distance):

	"""
	Deprecated since version 17.1.0. Use function NewParameterDFMAlign instead.

	Script function for the creation of a direct align on sets morph parameter.


	@name string: The desired name for the new parameter.

	@s_elements object: A set of elements that will be morphed by the parameter.

	@s_aligned object: A set of elements that will be aligned to the s_target set. 
	These elements will be used as guide for the displacement of the s_elements.

	@s_retained object: A set of elements that will retain their position during the morphing action.
	These elements will also affect the deformation of the s_elements.

	@s_target object: A set of elements that will be used as the target entities of the alignement action.

	@search_distance float: The search distance of the alignment action.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterDFMAlign instead.", DeprecationWarning)

def MorphParamCreateSetsOffset(name, s_elements, s_offset, s_retained):

	"""
	Deprecated since version 17.1.0. Use function NewParameterDFMOffset instead.

	Script function for the creation of a direct offset on sets morph parameter.


	@name string: The desired name for the new parameter.

	@s_elements object: A set of elements that will be morphed by the parameter.

	@s_offset object: A set of elements that will be offset. 
	These elements will be used as guide for the displacement of the s_elements.

	@s_retained object: A set of elements that will retain their position during the morphing action.
	These elements will also affect the displacement of the s_elements.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterDFMOffset instead.", DeprecationWarning)

def MorphParamCreateSetsTranslate(name, s_elements, s_translate, s_retained, dx, dy, dz):

	"""

	Script function for the creation of a direct translate on sets morph parameter.


	@name string: The desired name for the new parameter.

	@s_elements object: A set of elements that will be morphed by the parameter.

	@s_translate object: A set of elements that will be translated. 
	These elements will be used as guide for the displacement of the s_elements.

	@s_retained object: A set of elements that will retain their position during the morphing action.
	These elements will also affect the displacement of the s_elements.

	@dx float: The x component of the displacement vector.

	@dy float: The y component of the displacement vector.

	@dz float: The z component of the displacement vector.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

def MorphParamCreateSetsRotate(name, s_elements, s_rotate, s_retained, x, y, z, dx, dy, dz):

	"""
	Deprecated since version 17.1.0. Use function NewParameterDFMRotate instead.

	Script function for the creation of a direct rotate on sets morph parameter.


	@name string: The desired name for the new parameter.

	@s_elements object: A set of elements that will be morphed by the parameter.

	@s_rotate object: A set of elements that will be rotated. 
	These elements will be used as guide for the displacement of the s_elements.

	@s_retained object: A set of elements that will retain their position during the morphing action.
	These elements will also affect the displacement of the s_elements.

	@x float: The x component of the origin's position vector of the rotation axis.
	double x component of the direction vector of the rotation axis.

	@y float: The y component of the origin's position vector of the rotation axis.
	double y component of the direction vector of the rotation axis.

	@z float: The z component of the origin's position vector of the rotation axis.
	double z component of the direction vector of the rotation axis.

	@dx float: The x component of the direction vector of the rotation axis.

	@dy float: The y component of the direction vector of the rotation axis.

	@dz float: The z component of the direction vector of the rotation axis.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterDFMRotate instead.", DeprecationWarning)

def MorphParamCreateAngle(name, morph_edges):

	"""
	Deprecated since version 17.1.0. Use function NewParameterAngle instead.

	Function for the creation of an angle morph parameter for morph edges.


	@name string: The desired name for the new parameter.

	@morph_edges object: A list of morph edges. The list must have even size.
	Morph edges in the odd indicies of the list will retain their position 
	while those in even indicies will rotate.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterAngle instead.", DeprecationWarning)

def MorphParamCreateRotate(name, morph_points, coord, x, y, z, dx, dy, dz):

	"""
	Deprecated since version 17.1.0. Use function NewParameterRotate instead.

	Script function for the creation of a rotate morph parameter for morph points.


	@name string: The desired name for the new parameter.

	@morph_points object: A list of morph points.

	@coord object: A coordinate system that the rotation axis will be defined.
	If coord is None the global coordinate system will be used.

	@x float: The x component of the origin's position vector of the rotation axis.

	@y float: The y component of the origin's position vector of the rotation axis.

	@z float: The z component of the origin's position vector of the rotation axis.

	@dx float: The x component of the direction vector of the rotation axis.

	@dy float: The y component of the direction vector of the rotation axis.

	@dz float: The z component of the direction vector of the rotation axis.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterRotate instead.", DeprecationWarning)

def MorphParamCreateDeformation(name, affected):

	"""
	Deprecated since version 17.1.0. Use function NewParameterDeformation instead.

	Script function for the creation of a deformation morph parameter.


	@name string: The desired name for the new parameter.

	@affected string: Indicates which entities will be recorded by the deformation parameter.
	Possible values are 'All' and 'Moved'.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterDeformation instead.", DeprecationWarning)

def MorphParamCreateScale(name, morph_points, x, y, z):

	"""
	Deprecated since version 17.1.0. Use function NewParameterScale instead.

	Script function for the creation of a scale morph parameter for morph points.


	@name string: The desired name for the new parameter.

	@morph_points object: A list of morph points.

	@x float: The x component of the scale origin.

	@y float: The y component of the scale origin.

	@z float: The z component of the scale origin.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterScale instead.", DeprecationWarning)

def MorphParamCreateUserTangent(name, morph_tang):

	"""
	Deprecated since version 17.1.0. Use function NewParameterUserTangent instead.

	Script function for the creation of a user tanget morph parameter for morph edges.


	@name string: The desired name for the new parameter.

	@morph_tang object: A list of morph tangents.

	@returns integer: Returns the ID of the created parameter or 0 in case of failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterUserTangent instead.", DeprecationWarning)

def MorphParamCreateDFMFitEdges(name, edge_fit_args, entities, bounds, autobounds):

	"""

	Function for the creation of a DFM edge fit morph parameter.


	@name string: Tthe desired name for the new parameter.

	@edge_fit_args object: A list of objects created by MorphCreateDFMFitEdgesArgs

	@entities object: A list of entities that will be morphed.

	@bounds object: A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.

	@autobounds boolean: An option to enable the automatic bound determination.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

def MorphCreateDFMFitEdgesArgs(source, target):

	"""

	Script function for the creation of an object that will be used by MorphParamCreateDFMFitEdges script function.
	This is an auxiliary function.


	@source object: A list of entities that will be used as source of DFM edge fit parameter.

	@target object: A list of entities that will be used as target of DFM edge fit parameter.

	@returns object: Returns the created object or None in case of failure.

	"""

def MorphParamCreateDFMFitSurfaces(name, surafce_fit_args, morphed, bounds, autobounds):

	"""

	Script function for the creation of a DFM surface fit morph parameter.
	


	@name string: The desired name of the parameter.

	@surafce_fit_args object: A list of objects created by MorphCreateDFMFitSurfsArgs.

	@morphed object: A list of entities that will be morphed.

	@bounds object: A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.

	@autobounds boolean: Option to enable the automatic bound determination.

	@returns integer: Returns the ID of the created parameter, or 0 in case of failure.

	"""

def MorphCreateDFMFitSurfsArgs(source_area, target_area, source_points, target_points):

	"""

	Script function for the creation of an object that will be used by MorphParamCreateDFMFitSurfaces script function.
	This is an auxiliary function.
	


	@source_area object: A list of entities that will be used as the source area.

	@target_area object: A list of entities that will be used as the target area.

	@source_points object: A list of perimetric points of the source area.

	@target_points object: A list of perimetric points of the target area.

	@returns object: Returns the created object, or None in case of failure.

	"""

def MorphParamCreateDFMTranslate(name, translate_arg, entities, bounds, autobounds):

	"""

	Script function for the creation of a dfm translate parameter.


	@name string: The desired name of the parameter.

	@translate_arg object: A list objects created by MorphCreateDFMTranslateArgs.

	@entities object: A list of entities that will be morphed.

	@bounds object: A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.

	@autobounds boolean: Option to enable the automatic bound determination.

	@returns integer: Returns the ID of the created parameter, or 0 in case of failure.

	"""

def MorphCreateDFMTranslateArgs(translated, dx, dy, dz):

	"""

	Script function for the creation of an object that will be used by MorphParamCreateDFMTranslate script function.
	This is an auxiliary function


	@translated object: A list of entities that will be translated.

	@dx float: The x component of the displacement vector.

	@dy float: The y component of the displacement vector.

	@dz float: The z component of the displacement vector.

	@returns object: Returns the created object, or None in case of failure.

	"""

def MorphParamCreateDFMRotate(name, rotate_args, entities, bounds, autobounds):

	"""

	Script function for the creation of a dfm rotate parameter.


	@name string: The desired name of the parameter.

	@rotate_args object: A list of objects created by MorphCreateDFMRotateArgs.

	@entities object: A list of entities that will be morphed.

	@bounds object: A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.

	@autobounds boolean: Option to enable the automatic bound determination.

	@returns integer: Returns the ID of the created parameter, or 0 in case of failure.

	"""

def MorphCreateDFMRotateArgs(rotated, x, y, z, dx, dy, dz):

	"""

	Script function for the creation of an object that will be used by MorphParamCreateDFMRotate script function.
	This is an auxiliary function


	@rotated object: A list of entities that will be rotated.

	@x float: The x component of the origin's position vector of the rotation axis.

	@y float: The y component of the origin's position vector of the rotation axis.

	@z float: The z component of the origin's position vector of the rotation axis.

	@dx float: The x component of the direction vector of the rotation axis.

	@dy float: The y component of the direction vector of the rotation axis.

	@dz float: The z component of the direction vector of the rotation axis.

	@returns object: Returns the created object, or None in case of failure.

	"""

def MorphParamCreateDFMScale(name, scale_args, entities, bounds, autobounds):

	"""

	Script function for the creation of a dfm scale parameter.


	@name string: The desired name of the parameter.

	@scale_args object: A list of objects created by MorphCreateDFMScaleArgs.

	@entities object: A list of entities that will be morphed.

	@bounds object: A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.

	@autobounds boolean: Option to enable the automatic bound determination.

	@returns integer: Returns the ID of the created parameter, or 0 in case of failure.

	"""

def MorphCreateDFMScaleArgs(scaled, x, y, z):

	"""

	Script function for the creation of an object that will be used by MorphParamCreateDFMScale script function.
	This is an auxiliary function.


	@scaled object: A list of entities that will be scaled.

	@x float: The x component of the scale origin.

	@y float: The y component of the scale origin.

	@z float: The z component of the scale origin.

	@returns object: Returns the created object, or None in case of failure.

	"""

def MorphParamCreateDFMTransform(name, transformed_args, entities, bounds, autobounds):

	"""

	Script function for the creation of a dfm transform parameter.


	@name string: The desired name of the parameter.

	@transformed_args object: A list of objects created by MorphCreateDFMTransformArgs.

	@entities object: A list of entities that will be morphed.

	@bounds object: A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.

	@autobounds boolean: An option to enable the automatic bound determination.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

def MorphCreateDFMTransformArgs(transformed, src_coord, trg_coord):

	"""

	Function for the creation of an object that will be used by the MorphParamCreateDFMTransform function.
	This is an auxiliary function.


	@transformed object: A list of entities that will be transformed.

	@src_coord object: An ANSA coordinate object that will be used as the source coordinaty system.

	@trg_coord object: An ANSA coordinate object that will be used as the target coordinaty system.

	@returns object: Returns a reference to the newly created object, or None on failure.

	"""

def MorphParamCreateDFMOffset(name, offset, entities, bounds, autobounds):

	"""

	Script function for the creation of a DFM offset morph parameter.


	@name string: The desired name for the new parameter.

	@offset object: A list of entities that will offset.

	@entities object: A list of entities that will be morphed.

	@bounds object: A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.

	@autobounds boolean: An option to enable the automatic bound determination.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

def MorphParamCreateSlideFeatureTranslate(name, elements, coord, dx, dy, dz):

	"""
	Deprecated since version 17.1.0. Use function NewParameterSlideFeatureTranslate instead.

	Script function for the creation of a slide feature translate parameter.


	@name string: The desired name for the new parameter.

	@elements object: A list of elements that describes the feature.

	@coord object: A coordinate system that the displacement vector will be defined.
	If coord is None the global coordinate system will be used.

	@dx float: The x component of the displacement vector.

	@dy float: The y component of the displacement vector.

	@dz float: The z component of the displacement vector.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterSlideFeatureTranslate instead.", DeprecationWarning)

def MorphParamCreateSlideFeatureRotate(name, elements, coord, x, y, z, dx, dy, dz):

	"""
	Deprecated since version 17.1.0. Use function NewParameterSlideFeatureRotate instead.

	Script function for the creation of a slide feature rotate parameter.


	@name string: The desired name for the new parameter.

	@elements object: A list of elements that describes the feature.

	@coord object: A coordinate system that the displacement vector will be defined.
	If coord is None the global coordinate system will be used.

	@x float: The x component of the origin's position vector of the rotation axis.

	@y float: The y component of the origin's position vector of the rotation axis.

	@z float: The z component of the origin's position vector of the rotation axis.

	@dx float: The x component of the direction vector of the rotation axis.

	@dy float: The y component of the direction vector of the rotation axis.

	@dz float: The z component of the direction vector of the rotation axis.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterSlideFeatureRotate instead.", DeprecationWarning)

def MorphParamCreateSlideFeatureScale(name, elements, x, y, z):

	"""
	Deprecated since version 17.1.0. Use function NewParameterSlideFeatureScale instead.

	Script function for the creation of a slide feature scale parameter.


	@name string: The desired name for the new parameter.

	@elements object: A list of elements that describes the feature.

	@x float: The x component of the scale origin.

	@y float: The y component of the scale origin.

	@z float: The z component of the scale origin.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterSlideFeatureScale instead.", DeprecationWarning)

def MorphParamCreateSlideFeatureCurve(name, elements, curve, follow_orientation):

	"""
	Deprecated since version 17.1.0. Use function NewParameterSlideFeatureCurve instead.

	Script function for the creation of a slide feature on curve parameter.


	@name string: The desired name for the new parameter.

	@elements object: A list of elements that describes the feature.

	@curve object: An ANSA curve on which the feature will slide on.

	@follow_orientation boolean: A flag to determine if the feature will follow the curve's orientation.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterSlideFeatureCurve instead.", DeprecationWarning)

def MorphCreateDFMAlignArgs(entities, target_entities, target_axis, target_plane, include_thickness, max_distance, user_direction):

	"""

	Function for the creation of an object that will be used by the MorphParamCreateDFMAlign function.
	This is an auxiliary function.


	@entities object: A list of entities that will be aligned.

	@target_entities object: A list of entities that will be used as the target surface of alignment.

	@target_axis object: A list of doubles that describes an axis that will be used as the target axis.
	The format of this list is (x, y, z, dx, dy, dz) where x, y and z 
	are the components of the origins position vector and dx, dy and dz 
	are the components of the direction vector of the axis.

	@target_plane object: A list of doubles that describes a plane that will be used as the target plane.
	The format of this list is (x, y, z, dx, dy, dz) where x, y and z 
	are the components of the origins position vector of the plane 
	and dx, dy and dz are the components of the direction of the normal vector 
	of the plane.

	@include_thickness boolean: (optional)An option to determine if the thickness of the aligned and target elements 
	will be included in the calculation.
	Default value is False.

	@max_distance float: (optional)Determines the maximun radial search distance where the 
	aligned elements will seek 
	for target entities.
	Default value is infinite.

	@user_direction object: (optional)A list of doubles that describes a user's predefined alignment direction.
	The format of this list is (dx, dy, dz) where dx, dy and dz are the 
	components of the direction vector.

	@returns object: Returns a reference to the newly created object, or None on failure.

	"""

def MorphParamCreateDFMAlign(name, align_args, entities, bounds, autobounds):

	"""

	Function for the creation of a dfm align parameter.


	@name string: The desired name of the parameter

	@align_args object: A list of objects returned by MorphCreateDFMAlignArgs

	@entities object: A list of entities that will be morphed.

	@bounds object: A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.

	@autobounds boolean: An option to enable the automatic bound determination.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

def MorphParamCreateTailoredBlank(entities, properties, lengths, origin, normal, trajectory, movement, cut_mesh, reconstruct, zones, name):

	"""
	Deprecated since version 17.1.0. Use function NewParameterTailoredBlank instead.

	Script function for the creation of a 'Tailored Blank' parameter.


	@entities object: A list of shells.

	@properties object: A list of properties that will be applied on elements.

	@lengths object: A list of doubles that specifies the application length for each property.

	@origin object: A list of three doubles that specifies the position vector of the
	origin of the seperation plane.

	@normal object: A list of three doubles that specifies the direction vector of the
	normal of the seperation plane.

	@trajectory object: (optional)A list of entities that will be used as the trajectory on which
	seperation plane will move.

	@movement integer: (optional)A variable that controls the type of movement of the seperation plane. 
	Possible values are:
	-0 for "Follow trajectory"
	-1 for "Sweep on trajectory"
	-2 for "Glide on trajectory"
	(Default: 0)

	@cut_mesh boolean: (optional)An option that controls if plane cut will take place at each property change.
	(Default: False)

	@reconstruct boolean: (optional)An option to determine if reconstruction of the affected elements 
	will take place after the application of cut.
	This option is meaningfull only if "cut_mesh" is set to True. 
	(Default: False)

	@zones integer: (optional)An option to determine the number of zones that will be reconstructed
	around cut area.
	This option is meaningfull only if "reconstruct" is set to True.
	(Default: 0)

	@name string: (optional)The desired name for the created parameter.
	If not provided ANSA will automaticaly decide a name for the newly 
	created parameter.

	@returns integer: Returns the ID of the newly created parameter or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewParameterTailoredBlank instead.", DeprecationWarning)

def MorphPointProjectToContainer(box_points, target_entities, offset, coordinate_system, freeze_x_axis, freeze_y_axis, freeze_z_axis):

	"""

	Function to project control points on target feature lines or on target surface 
	(target surface can be defined by shells and geometrical faces).


	@box_points object: A list of box points or a box point. The user can also define the box edges and 
	the function will automatically get the correspondent control points.

	@target_entities object: A list of entities, parts, properties, materials or sets, 
	to define the target entities (feature lines or surfaces).

	@offset float: (optional)The distance to move the control points from their projection on target entities.

	@coordinate_system object: (optional)The coordinate system to work with (it is used in combination 
	with the freeze options).

	@freeze_x_axis boolean: (optional)True or False, to define if x axis movement is not allowed.

	@freeze_y_axis boolean: (optional)True or False, to define if y axis movement is not allowed.

	@freeze_z_axis boolean: (optional)True or False, to define if z axis movement is not allowed.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def xyzIsInsideBox(x,y,z):

	"""

	This function takes as arguments the coordinates of a point and checks whether this
	point is inside a box (morph, sizebox, hexablock and d-boxes), 
	and returns a list of the boxes.


	@x float: The x coordinate of the point.

	@y float: The y coordinate of the point.

	@z float: The z coordinate of the point.

	@returns object: Returns a list with the boxes or false for none.

	"""

def CreateStamp(stamp_type, stamp_entities, stamp_parameters, direction_points, invert_direction, auto_reconstruct, add_to_set, save_morph_parameter, return_characteristics, top_is_width):

	"""
	Deprecated since version 21.0.0. Use class Create instead.

	Function for the creation of circular, rectangular or free form stamps.


	@stamp_type string: The type of the stamp, values can be "Circular", "Rectangular rounded" or "Surface".

	@stamp_entities object: A list of the entities where the stamp will be created.

	@stamp_parameters object: A list of the stamp parameters:
	"Circular" = [Diameter, Height, Angle_A, Radius_r1, Radius_r2]
	"Rectangular rounded" = [Width_w1, Width_w2, Corner_R, Height, Angle_A, Radius_r1, Radius_r2]
	"Surface" = [Height, Angle_A, Radius_r1, Radius_r2]

	@direction_points object: (optional)A list of 2 points, to define local bead direction, when Rectangular round feature is created

	@invert_direction boolean: (optional)Boolean to invert direction of the feature

	@auto_reconstruct object: (optional)Dictionary with Improve mesh value {'Reconstruct', 'Smooth', ' Reshape'} and a value an integer of zones around the created feature.

	@add_to_set integer: (optional)Integer id of the Set, to add the create feature shells

	@save_morph_parameter boolean: (optional)Boolean to save a morphing parameter on the create feature

	@return_characteristics boolean: (optional)Boolean value to control the return of the function. Set it to True
	to return a Dictionary with key and value:
	
	{ 'ALL': [ shells ] , 'TOP_FILLET': [ shells ], 'BOTTOM_FILLET': [ shells ], 'TOP': [ shells ], 'BODY': [ shells ]}

	@top_is_width boolean: (optional)Set to True for parameter ANGLE_A to be width and not an angle, default False. Applicable only in Circular

	@returns object: Returns the shells of the created stamp or 0 on error, use "return_characteristics" to return a dictionary

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class Create instead.", DeprecationWarning)

def CreateBead(bead_type, bead_entities, bead_parameters, invert_direction, auto_reconstruct, add_to_set, save_morph_parameter,direction_points, return_characteristics,top_is_width):

	"""
	Deprecated since version 21.0.0. Use class Create instead.

	A function for the creation of beads (straight or curved).


	@bead_type string: The type of the bead. Accepted values: "Straight", "Straight rounded", 
	"Curved" or "Curved rounded".

	@bead_entities object: A list of entities, where the bead will be created.

	@bead_parameters object: A list of the bead parameters: [Width_w1, Height, Angle_A, Radius_r1, Radius_r2]. 
	Radius_r2 is optional and if given it will create a flat bottom bead, 
	otherwise a rounded bottom one.

	@invert_direction boolean: (optional)Boolean to invert direction of the bead

	@auto_reconstruct object: (optional)Dictionary with Improve mesh value {'Reconstruct', 'Smooth', ' Reshape'} and a value an integer of zones around the created bead.

	@add_to_set integer: (optional)Integer id of the Set, to add the create bead shells

	@save_morph_parameter boolean: (optional)Boolean to save a morphing parameter on the create bead

	@direction_points object: (optional)A list of 2 points, to define local bead direction, when X, T or L type  feature is created

	@return_characteristics boolean: (optional)Boolean value to control the return of the function. Set it to True
	to return a Dictionary with key and value:
	
	{ 'ALL': [ shells ] , 'TOP_FILLET': [ shells ], 'BOTTOM_FILLET': [ shells ], 'TOP': [ shells ], 'BODY': [ shells ], 'JUNCTION': [ shells ], 'MEMBER_1': [ shells ] ... }

	@top_is_width boolean: (optional)Set to True for parameter ANGLE_A to be width and not an angle, default False.

	@returns object: Returns the shells of the created stamp or 0 on error, use "return_characteristics" to return a dictionary

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class Create instead.", DeprecationWarning)

def CreateFlangedOpening(open_type, open_entities, open_parameters, direction_points, invert_direction, auto_reconstruct, add_to_set, save_morph_parameter,return_characteristics, top_is_width):

	"""
	Deprecated since version 21.0.0. Use class Create instead.

	Function for the creation of flanged openings.


	@open_type string: The type of the opening. Values can be "Circular", "Rectangular rounded", 
	"Surface", "Straight", "Straight rounded", "Curved" or "Curved rounded".

	@open_entities object: A list of entities where the opening will be created.

	@open_parameters object: A list of the opening parameters:
	
	"Circular": [Diameter, Height, Angle_A, Radius_r1]
	"Rectangular rounded": [Width_w1, Width_w2, Corner_R, Height, Angle_A, Radius_r1]
	"Surface": [Height, Angle_A, Radius_r1]
	"Straight": [Width_w1, Height, Angle_A, Radius_r1]
	"Straight rounded": [Width_w1, Height, Angle_A, Radius_r1]
	"Curved": [Width_w1, Height, Angle_A, Radius_r1]
	"Curved rounded": [Width_w1, Height, Angle_A, Radius_r1]

	@direction_points object: (optional)A list of 2 points, to define local bead direction, when Rectangular round feature is created

	@invert_direction boolean: (optional)Boolean to invert direction of the feature

	@auto_reconstruct object: (optional)Dictionary with Improve mesh value {'Reconstruct', 'Smooth', ' Reshape'} and a value an integer of zones around the created feature.

	@add_to_set integer: (optional)Integer id of the Set, to add the create feature shells

	@save_morph_parameter boolean: (optional)Boolean to save a morphing parameter on the create feature

	@return_characteristics boolean: (optional)Boolean value to control the return of the function. Set it to True
	to return a Dictionary with key and value:
	
	{ 'ALL': [ shells ] , 'BOTTOM_FILLET': [ shells ], 'BODY': [ shells ]}

	@top_is_width boolean: (optional)Set to True for parameter ANGLE_A to be width and not an angle, default False.

	@returns object: Returns the shells of the created stamp or 0 on error, use "return_characteristics" to return a dictionary

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class Create instead.", DeprecationWarning)

def CreateOpening(open_type, open_entities, open_parameters, direction_points, invert_direction, auto_reconstruct, add_to_set, save_morph_parameter):

	"""
	Deprecated since version 21.0.0. Use class Create instead.

	Function for the creation of openings.


	@open_type object: The type of the opening, values can be "Circular", "Rectangular rounded", 
	"Surface", "Straight", "Straight rounded", "Curved" or "Curved rounded".

	@open_entities object: A list of entities where the opening will be created.

	@open_parameters object: A list of the opening parameters:
	-"Circular": [Diameter]
	-"Rectangular rounded": [Width_w1, Width_w2, Corner_R]
	-"Surface": []
	-"Straight"
	-"Straight rounded"
	-"Curved"
	-"Curved rounded": [Width_w1]

	@direction_points object: (optional)A list of 2 points, to define local bead direction, when Rectangular round feature is created

	@invert_direction boolean: (optional)Boolean to invert direction of the feature

	@auto_reconstruct object: (optional)Dictionary with Improve mesh value {'Reconstruct', 'Smooth', ' Reshape'} and a value an integer of zones around the created feature.

	@add_to_set integer: (optional)Integer id of the Set, to add the create feature shells

	@save_morph_parameter boolean: (optional)Boolean to save a morphing parameter on the create feature

	@returns object: Returns the nodes of the new opening or 0 on error.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class Create instead.", DeprecationWarning)

def CreateRib(rib_type, rib_entities, rib_parameters, add_to_set):

	"""
	Deprecated since version 21.0.0. Use class Create instead.

	Function for the creation of ribs.


	@rib_type string: The type of the rib, values can be "Rib 3D" or "Rib 2D".

	@rib_entities object: A list of entities where the rib will be created.

	@rib_parameters object: A list of the rib parameters:
	
	- "Rib 2D": [Length], length is optional, if left blank it will be calculated 
	   from the points given in "rib_entities".
	
	- "Rib 3D": [Length, Width, Angle, "Top", value, "Bottom", value], length is optional, 
	   if left blank it will be calculated from the points given in "rib_entities".
	   "Top" and "Bottom" are string values and can take values "Chamfer" or "Fillet" and 
	   the value for each one (see examples).

	@add_to_set integer: (optional)Integer id of the Set, to add the created feature shells

	@returns object: Returns the shells of the created rib, or 0 on error.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class Create instead.", DeprecationWarning)

def SimulateDoeWindow(mainitem, values, designs, algorithm, generate, experiments_file):

	"""

	Function for accessing the "Simulate-Doe" window in Optimization task.


	@mainitem object: An Optimization_Task item.

	@values string: A filename with the values to be loaded in the window.

	@designs integer: The number of designs.

	@algorithm string: The selected algorithm values can be: 
	-'Linear'
	-'Random'
	-'Full Factorial'
	-'Uniform Latin Hypercube'

	@generate boolean: Auto generate experiments based on the previous values.

	@experiments_file string: (optional)The full path of the output file should always follow the string argument "experiments_file". This output file will contain all the experiments that the 
	user created on the window's table. For more information, look at the examples.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphConstraintPlanar(entities, morphed, bounds, autobounds):

	"""
	Deprecated since version 21.0.0. Use class ConstraintPlanar instead.

	Script function for creating a planar morph constraint.
	
	The generated constraint may be included in the morphed entities of a DFM, and will 
	force the constraint's 'entities' to become coplanar when the DFM executes.
	To alleviate and/or confine the effects of the constraint, 'morphed' and 'bounds' 
	entities may be provided to the constraint, essentially defining a transition region.
	
	In most aspects, the constraint operates like an automatic DFM, subsequent to the main DFM.


	@entities object: A list of the entities to become coplanar.

	@morphed object: A list of the entities to be morphed by constraint.

	@bounds object: A list of the entities defining the bounds of the constraint's fitting process.

	@autobounds boolean: (optional)An option to enable the automatic bounds determination.
	(Default: False)

	@returns object: Returns a reference to the newly created morph constraint object.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class ConstraintPlanar instead.", DeprecationWarning)

def MorphConstraintRigid(entities, morphed, bounds, autobounds):

	"""
	Deprecated since version 21.0.0. Use class ConstraintRigid instead.

	Script function for creating a rigid morph constraint.
	
	The generated constraint may be included in the morphed entities of a DFM, and will force 
	the constraint's 'entities' to move (translate/rotate) rigidly when the DFM executes.
	To alleviate and/or confine the effects of the constraint, 'morphed' and 'bounds' entities 
	may be provided to the constraint, essentially defining a transition region.
	
	In most aspects, the constraint operates like an automatic DFM, subsequent to the main DFM.


	@entities object: A list of the entities to remain rigid.

	@morphed object: A list of the entities to be morphed by constraint.

	@bounds object: A list of the entities defining the bounds of the constraint's fitting process.

	@autobounds boolean: (optional)An option to enable the automatic bounds determination.
	(Default: False)

	@returns object: Returns the created morph constraint.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class ConstraintRigid instead.", DeprecationWarning)

def MorphConstraintScaled(entities, morphed, bounds, autobounds):

	"""
	Deprecated since version 21.0.0. Use class ConstraintScaled instead.

	Script function for creating a scaled morph constraint.
	
	The generated constraint may be included in the morphed entities of a DFM, and will force 
	the constraint's 'entities' to move (translate/rotate) rigidly, subject to homogeneous 
	scaling, when the DFM executes. To alleviate and/or confine the effects of the constraint, 
	'morphed' and 'bounds' entities may be provided to the constraint, essentially defining 
	a transition region.
	
	In most aspects, the constraint operates like an automatic DFM, subsequent to the main DFM.


	@entities object: A list of the entities to remain rigid (subject to homogeneous scaling).

	@morphed object: A list of the entities to be morphed by constraint.

	@bounds object: A list of the entities defining the bounds of the constraint's fitting process.

	@autobounds boolean: (optional)An option to enable the automatic bounds determination.
	(Default: False)

	@returns object: Returns a reference to the newly created morph constraint object.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class ConstraintScaled instead.", DeprecationWarning)

def MorphConstraintDirectional(entities, morphed, bounds, coordinate, x_status, y_status, z_status, autobounds):

	"""
	Deprecated since version 21.0.0. Use class ConstraintDirectional instead.

	A function for creating a directional morph constraint.
	
	The generated constraint may be included in the morphed entities of a DFM, and will force 
	the constraint's 'entities' to morph only along user permisible direction(s) when the DFM 
	executes. To alleviate and/or confine the effects of the constraint, 'morphed' and 'bounds' 
	entities may be provided to the constraint, essentially defining a transition region.
	
	In most aspects, the constraint operates like an automatic DFM, subsequent to the main DFM.


	@entities object: A list of the entities to morph in user defined direction(s).

	@morphed object: A list of the entities to be morphed by constraint.

	@bounds object: A list of the entities defining bounds of constraint's fitting process.

	@coordinate object: A local coordinate system, defining the allowable/non-allowable morphing axes.

	@x_status string: -'active': morphing will occur as normal in local x-axis.
	-'inactive': will freeze movement along local x-axis.

	@y_status string: -'active': morphing will occur as normal in local y-axis.
	-'inactive': will freeze movement along local y-axis.

	@z_status string: -'active': morphing will occur as normal in local z-axis.
	-'inactive': will freeze movement along local z-axis.

	@autobounds boolean: (optional)An option to enable the automatic bounds determination.
	(Default: False)

	@returns object: It returns the created morph constraint.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class ConstraintDirectional instead.", DeprecationWarning)

def MorphConstraintPathFollower(entities, morphed, bounds, path, autobounds):

	"""
	Deprecated since version 21.0.0. Use class ConstraintPathFollower instead.

	A function for creating a path follower morph constraint.
	
	The generated constraint may be included in the morphed entities of a DFM, and will force 
	the constraint's 'entities' to move only along a pre-defined path when the DFM executes. 
	To alleviate and/or confine the effects of the constraint, 'morphed' and 'bounds' entities 
	may be provided to the constraint, essentially defining a transition region.
	
	In most aspects, the constraint operates like an automatic DFM, subsequent to the main DFM.


	@entities object: A list of the entities [edges or points] to remain along a path.

	@morphed object: A list of the entities to be morphed by constraint.

	@bounds object: A list of the entities defining bounds of constraint's fitting process.

	@path object: A list of the entities [edges or points] defining the movement path.

	@autobounds boolean: (optional)An option to enable the automatic bounds determination.
	(Default: False)

	@returns object: Returns the created morph constraint.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class ConstraintPathFollower instead.", DeprecationWarning)

def MorphSplitProject(box_edge, points, fit_new_skin_edges, work_on):

	"""
	Deprecated since version 21.0.0. Use class BoxSplit instead.

	A function for projecting points array on an edge to split morph box(es).


	@box_edge object: The box edge that will be split (point will be projected on this edge).

	@points object: A point (3D point, node, hot point, etc) to project on the box edge.

	@fit_new_skin_edges boolean: (optional)If set to True, new skin edges will fit on the underlying model.
	Default value is False.

	@work_on string: (optional)Defines where the projection is going to take place:
	'whole_db' fit skin edges will take place on the whole database,
	'visible'  fit skin edges will take place only on the visible elements
	If work_on is not set then whole_db will be the default argument.
	This option is only available only when fit_skin_edges is set to true.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class BoxSplit instead.", DeprecationWarning)

def MorphAdaptCrossections(entities, number_or_length):

	"""

	A function for the creation of morphing boxes between 2 or more crossections.
	The function will create multicut crossections based on the given length or number  
	and morphing boxes with length and width parameters to manipulate the crossections.


	@entities object: A list with the shell elements to cut and create crossections.

	@number_or_length string: The number or length to cut. Use ~ to define length.

	@returns object: Returns a list containing references to the newly created morphing boxes.

	"""

def MorphByCurves(height_edges, top_bottom_edges):

	"""

	A function for creating a 3D morphing box by defining its four "height" edges
	and the "top", "bottom" edges (optionally).


	@height_edges object: A list that contains all the entities that define the four box "height" edges.

	@top_bottom_edges object: (optional)A list that contains all the entities that define the 
	"top" and "bottom" edges of the new box.

	@returns object: Returns a reference to the newly created box object on success, or 0 on failure.

	"""

def Morph2DCreate (type, entities, thickness, delete_original, paste, convert_to_ortho):

	"""

	A function to create a 2D morphing box using the input entities.
	Thickness of the 2D morphing box may be defined (optional argument).
	For "hatches" case, the original 3D boxes may be deleted (optional argument).
	For "wireframe" case, there is the option to paste the created 2D boxes 
	(paste=True) and to convert them to orthogonal boxes (convert_to_ortho=True).
	These two arguments (paste & convert_to_ortho) are mutually exclusive.
	If they are both set "True" they will be evaluated as "False". 


	@type string: A string that defines the input entities. It can have 
	the values "points", "curves", "hatches" and "wireframe".

	@entities object: A list of the entities that are used for the creation of the 2D morphing box.
	According to the "type" it takes different entities: 
	-"points" - list with entities whose points will be used to create the new 2D box,
	-"curves" - list containing four lists with the input curves/cons/edges,
	-"hatches" - list containing the input box faces,
	-"wireframe" - list containing the input curves.

	@thickness float: (optional)The thickness of the 2D morphing box.

	@delete_original boolean: (optional)Defines if the original boxes will be deleted.
	It is used only for the "hatches" type.

	@paste boolean: (optional)Defines if the created 2D boxes will be pasted or not.
	It is used only for the "wireframe" case.
	(Default: False)

	@convert_to_ortho boolean: (optional)Defines if the created 2D boxes will be converted to orthogonal boxes or not.
	It is used only for the "wireframe" case.
	(Default: False)

	@returns object: If "type" = "points" or "curves": Returns a reference to the newly created box object.
	If "type" = "hatches": Returns a list containing references to the newly created box objects.
	On failure, returns None.

	"""

def MorphEdgesRedistribute(box_edges, factor, nodal_number_redistribution):

	"""

	Script function to redistribute boxes splits along input box edges.
	Splits (corner points of box edges) are redistributed within the 
	original position and the equally-spaced position. Redistribution 
	is applied to chains of connected box edges (input edges are classified 
	to these chains).


	@box_edges object: A list containing input box edges.

	@factor float: The redistribution factor. It takes values from 0 (original
	position) to 1 (equally-spaced position).

	@nodal_number_redistribution boolean: (optional)Defines if redistribution will be applied according to
	uniform nodal distribution.

	@returns integer: Always returns 1.

	"""

def MorphEdgesMatch(box_edges, target_edges, factor):

	"""

	A function to match the shape of input box edges tothe target edges.
	Input box edges are classified to chains of connected box edges and each chain is matched separately.


	@box_edges object: A list containing the input box edges.

	@target_edges object: A list containing the target edges.

	@factor float: The match factor. It takes values from 0 (input edges'
	original shape) to 1 (target edges' shape).

	@returns: Always returns None.

	"""

def MorphTopo(boxes, tolerance):

	"""

	Script function to connect the input boxes, provided that the Control Points of their 
	neighboring Box Faces, reside within the specific tolerance.


	@boxes object: A list containing the input boxes.

	@tolerance string: (optional)A string to define the tolerance mode, accepting
	"draft", "middle", "fine" or "extra fine".
	Default mode depends on Resolution/Tolerances/Units
	and Morph/Optimization settings.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphSplitToPenta(box_points):

	"""
	Deprecated since version 21.0.0. Use class BoxSplit instead.

	This function splits quad faces of hexahedral boxes in order to form two penta boxes.


	@box_points object: A list containing pairs of box points (two consecutive points that correspond 
	to the points that split will be performed to) of quad box faces.

	@returns integer: Returns the number of successful splits.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class BoxSplit instead.", DeprecationWarning)

def MorphRelease(entities):

	"""

	This function releases input boxes or box faces. 
	It can be used for morphing boxes, size boxes and hexa block boxes.


	@entities object: A list containing boxes or box faces to be released.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MorphCollapse(box_face, box_edge, target_point, collapse_entire_topology):

	"""

	A function that generates PENTA boxes by collapsing box edges.


	@box_face object: The box face to collapse.

	@box_edge object: The box edge (that belongs to the input box face) to collapse.

	@target_point object: (optional)A box point (corner point of input edge) to define the collapse 
	direction. If it is not defined, collapse is applied to the middle 
	of the input box edge.

	@collapse_entire_topology boolean: (optional)Defines if all the boxes from the side of the collapsed edge 
	will be collapsed.

	@returns: No value is returned.

	"""

def CoarseBoxTopology(boxes, box_edge, coarse_ratio, distance):

	"""

	Function to convert complicated Box structures to more coarse. 
	The function automatically creates C- & L- type structures inside the 
	buffer zone, in order to achieve the desired coarsening ratio.


	@boxes object: A list containing the input boxes to coarse.

	@box_edge object: The box edge denoting the coarsening direction.

	@coarse_ratio string: A string that takes the values "3-1" or "2-1" and defines the shape of
	the boxes in the buffer zone.

	@distance float: The distance that defines how much the buffer zone will be extended.

	@returns: Always returns None.

	"""

def DCPositionApply(entity, distance):

	"""

	The function applies the distance to the given design change position entity.


	@entity object: The DC_POSITION entity.

	@distance float: The distance that will be applied.

	@returns boolean: Returns True on success, False otherwise.

	"""

def DCCrossSectionApply(entity, width, height):

	"""

	The function will apply a width and height change to the given DC_CROSS_SECTION entity.


	@entity object: The DC_CROSS_SECTION entity.

	@width float: Width change value.

	@height float: Height change value.

	@returns boolean: Returns True on success, False otherwise.

	"""

def MorphParamCreateTransform(name, morph_points, transform_points):

	"""

	Function for the creation of a transform morph parameter for morph points.


	@name string: The desired name for the new parameter.

	@morph_points object: A list of morph points.

	@transform_points object: A list of 6 points to get transformation coordinates or 2 coordinates.

	@returns integer: Returns the ID of the newly created parameter, or 0 on failure.

	"""

def MorphCreateMorphAlignArgs(entities, target_entities, distance, offset, user_direction, align_to_midplane, align_on_geometry):

	"""
	Deprecated since version 17.1.0. Use function NewMorphAlignArgs instead.

	Function for the creation of an object to be used in creating an Align parameter.


	@entities object: A list with morph points to align.

	@target_entities object: A list with entities where morph points will be aligned.
	Can have either 3 points to define a plane or anything else..

	@distance float: (optional)The alignment distance.

	@offset float: (optional)Any offset value.

	@user_direction object: (optional)A list with 3 doubles to define a used defined vector.

	@align_to_midplane boolean: (optional)Boolean to define if it will align to mid plane or not.

	@align_on_geometry boolean: (optional)Boolean to define if it will align to geometry or not.

	@returns object: Returns a reference to the newly created object, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 17.1.0. Use function NewMorphAlignArgs instead.", DeprecationWarning)

def NewParameterDFMFitEdges(args, entities, bounds, autobounds, name):

	"""
	Deprecated since version 21.0.0. Use class DFM instead.

	Function for the creation of a DFM edge fit morph parameter.


	@args object: A list of objects created by NewDFMFitEdgesArgs.

	@entities object: (optional)A list of entities that will be morphed.
	(Default: None)

	@bounds object: (optional)A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.
	(Default: None)

	@autobounds boolean: (optional)An option to enable the automatic bound determination. 
	(Default: True)

	@name string: (optional)The desired name for the new parameter. 
	(Default: 'DFM_Edge_Fit')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFM instead.", DeprecationWarning)

def NewDFMFitEdgesArgs(source, target):

	"""
	Deprecated since version 21.0.0. Use class DFMFitEdges instead.

	Function for the creation of an object that will be used by the NewParameterDFMFitEdges function.
	This is an auxiliary function.


	@source object: A list of entities that will be used as source of DFM edge fit parameter.

	@target object: A list of entities that will be used as target of DFM edge fit parameter.

	@returns object: Returns a list containing references to the newly created objects on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFMFitEdges instead.", DeprecationWarning)

def NewDFMFitSurfsArgs(source_area, target_area, source_points, target_points):

	"""
	Deprecated since version 21.0.0. Use class DFMFitSurfaces instead.

	Function for the creation of an object that will be used by the NewParameterDFMFitSurfaces function.
	This is an auxiliary function.


	@source_area object: A list of entities that will be used as the source area

	@target_area object: A list of entities that will be used as the target area

	@source_points object: A list of perimetric points of the source area

	@target_points object: A list of perimetric points of the target area

	@returns object: Returns a list containing references to the newly created objects on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFMFitSurfaces instead.", DeprecationWarning)

def NewDFMTranslateArgs(translated, dx, dy, dz):

	"""
	Deprecated since version 21.0.0. Use class DFMTranslate instead.

	Function for the creation of an object that will be used by the NewParameterDFMTranslate function.
	This is an auxiliary function.


	@translated object: A list of entities that will be translated.

	@dx float: The x component of the displacement vector.

	@dy float: The y component of the displacement vector.

	@dz float: The z component of the displacement vector.

	@returns object: Returns a reference to the newly created object on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFMTranslate instead.", DeprecationWarning)

def NewDFMRotateArgs(rotated, x, y, z, dx, dy, dz):

	"""

	Function for the creation of an object that will be used by the NewParameterDFMRotate function.
	This is an auxiliary function.


	@rotated object: A list of entities to be rotated.

	@x float: The x component of the origin's position vector of the rotation axis.

	@y float: The y component of the origin's position vector of the rotation axis.

	@z float: The z component of the origin's position vector of the rotation axis.

	@dx float: The x component of the direction vector of the rotation axis.

	@dy float: The y component of the direction vector of the rotation axis.

	@dz float: The z component of the direction vector of the rotation axis.

	@returns object: Returns a list containing references to the newly created objects on sucess, or None on failure.

	"""

def NewDFMScaleArgs(scaled, x, y, z):

	"""
	Deprecated since version 21.0.0. Use class DFMScale instead.

	Function for the creation of an object that will be used by the NewParameterDFMScale function.
	This is an auxiliary function.


	@scaled object: A list of entities that will be scaled.

	@x float: The x component of the scale origin.

	@y float: The y component of the scale origin.

	@z float: The z component of the scale origin.

	@returns object: Returns a list containing references to the newly created objects on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFMScale instead.", DeprecationWarning)

def NewDFMTransformArgs(transformed, src_coord, trg_coord):

	"""
	Deprecated since version 21.0.0. Use class DFMTransform instead.

	Script function for the creation of an object that will be used by NewParameterDFMTransform script function.
	This is an auxiliary function


	@transformed object: a list of entities that will be transformed

	@src_coord object: is an ANSA coordinate object that will be used as the source coordinate system.

	@trg_coord object: is an ANSA coordinate object that will be used as the target coordinate system.

	@returns object: Returns a list containing references to the newly created objects on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFMTransform instead.", DeprecationWarning)

def NewDFMAlignArgs(entities, target_entities, target_axis, target_plane, include_thickness, max_distance, user_direction):

	"""
	Deprecated since version 21.0.0. Use class DFMAlign instead.

	Function for the creation of an object that will be used by NewParameterDFMAlign script function.
	This is an auxiliary function.


	@entities object: A list of entities that will be aligned.

	@target_entities object: (optional)A list of entities that will be used as the target surface of alignment.

	@target_axis object: (optional)A list of doubles that describes an axis that will be used as the target axis.
	The format of this list is (x, y, z, dx, dy, dz) where x, y and z 
	are the components of the origins position vector and dx, dy and dz 
	are the components of the direction vector of the axis.

	@target_plane object: (optional)A list of doubles that describes a plane that will be used as the target plane.
	The format of this list is (x, y, z, dx, dy, dz) where x, y and z 
	are the components of the origins position vector of the plane 
	and dx, dy and dz are the components of the direction of the normal vector 
	of the plane.

	@include_thickness boolean: (optional)An option to determine if the thickness of the aligned and target elements 
	will be included in the calculation.
	(Default: False)

	@max_distance float: (optional)Determines the maximun radial search distance where the 
	aligned elements will seek 
	for target entities.
	Default value is infinite.

	@user_direction object: (optional)A list of doubles that describes a user's predefined alignment direction.
	The format of this list is (dx, dy, dz) where dx, dy and dz are the 
	components of the direction vector.

	@returns object: Returns a list containing references to the newly crated objects on success, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFMAlign instead.", DeprecationWarning)

def NewParameterAngle(morph_edges, name):

	"""

	Function for the creation of an angle morph parameter for morph edges.


	@morph_edges object: A list of morph edges. The list must have even size.
	Morph edges in the odd indicies of the list will retain their position 
	while those in even indicies will rotate.

	@name string: (optional)The desired name for the new parameter.
	(Default: 'Angle')

	@returns object: Returns a reference to the newly created object on sucess, or None on failure.

	"""

def NewParameterDeformation(affected, name):

	"""

	Function for the creation of a deformation morph parameter.


	@affected string: (optional)Indicates which entities will be recorded by the deformation parameter.
	Possible values are 'All' and 'Moved'.
	(Default: 'All')

	@name string: (optional)The desired name for the new parameter.
	(Default: 'Deform')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

def NewParameterDFMAlign(args, entities, bounds, autobounds, name):

	"""
	Deprecated since version 21.0.0. Use class DFM instead.

	Function for the creation of a dfm align parameter.


	@args object: A list of objects returned by NewDFMAlignArgs.

	@entities object: (optional)A list of entities that will be morphed.
	(Default: None)

	@bounds object: (optional)A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.
	(Default: None)

	@autobounds boolean: (optional)An option to enable the automatic bound determination.
	(Default: True)

	@name string: (optional)The desired name of the parameter.
	(Default: 'DFM_Align')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFM instead.", DeprecationWarning)

def NewParameterDFMFitSurfaces(args, entities, bounds, autobounds, name):

	"""
	Deprecated since version 21.0.0. Use class DFM instead.

	Function for the creation of a DFM surface fit morph parameter.


	@args object: A list of objects created by NewDFMFitSurfsArgs.

	@entities object: (optional)A list of entities that will be morphed.
	(Default: None)

	@bounds object: (optional)A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.
	(Default: None)

	@autobounds boolean: (optional)An option to enable the automatic bound determination.
	(Default: True)

	@name string: (optional)The desired name of the parameter.
	(Default: 'DFM_Surface_Fit')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFM instead.", DeprecationWarning)

def NewParameterDFMOffset(offset_ents, morph_ents, bounds, autobounds, name):

	"""
	Deprecated since version 21.0.0. Use class DFM instead.

	Function for the creation of a DFM offset morph parameter.


	@offset_ents object: A list of entities that will offset.

	@morph_ents object: (optional)A list of entities that will be morphed.
	(Default: None)

	@bounds object: (optional)A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.
	(Default: None)

	@autobounds boolean: (optional)An option to enable the automatic bound determination.
	(Default: True)

	@name string: (optional)The desired name for the new parameter.
	(Default: 'DFM_Offset')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFM instead.", DeprecationWarning)

def NewParameterDFMRotate(args, entities, bounds, autobounds, name):

	"""
	Deprecated since version 21.0.0. Use class DFM instead.

	Function for the creation of a dfm rotate parameter.


	@args object: A list of objects created by NewDFMRotateArgs

	@entities object: (optional)A list of entities that will be morphed.
	(Default: None)

	@bounds object: (optional)A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.
	(Default: None)

	@autobounds boolean: (optional)An option to enable the automatic bound determination.
	(Default: True)

	@name string: (optional)The desired name of the parameter
	(Default: 'DFM_Rotate')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFM instead.", DeprecationWarning)

def NewParameterDFMScale(args, entities, bounds, autobounds, name):

	"""
	Deprecated since version 21.0.0. Use class DFM instead.

	Function for the creation of a dfm scale parameter.


	@args object: A list of objects created by NewDFMScaleArgs.

	@entities object: (optional)A list of entities that will be morphed.
	(Default: None)

	@bounds object: (optional)A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.
	(Default: None)

	@autobounds boolean: (optional)An option to enable the automatic bound determination.
	(Default: True)

	@name string: (optional)The desired name of the parameter.
	(Default: 'DFM_Scale')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFM instead.", DeprecationWarning)

def NewParameterDFMTranslate(args, entities, bounds, autobounds, name):

	"""
	Deprecated since version 21.0.0. Use class DFM instead.

	Function for the creation of a dfm translate parameter.


	@args object: A list of objects created by NewDFMTranslateArgs.

	@entities object: (optional)A list of entities that will be morphed.
	(Default: None)

	@bounds object: (optional)A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.
	(Default: None)

	@autobounds boolean: (optional)An option to enable the automatic bound determination.
	(Default: True)

	@name string: (optional)The desired name of the parameter.
	(Default: 'DFM_Translate')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFM instead.", DeprecationWarning)

def NewParameterDFMTransform(args, entities, bounds, autobounds, name):

	"""
	Deprecated since version 21.0.0. Use class DFM instead.

	Function for the creation of a dfm transform parameter.


	@args object: A list of objects created by NewDFMTransformArgs.

	@entities object: (optional)A list of entities that will be morphed.
	(Default: None)

	@bounds object: (optional)A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.
	(Default: None)

	@autobounds boolean: (optional)An option to enable the automatic bound determination.
	(Default: True)

	@name string: (optional)The desired name of the parameter.
	(Default: 'DFM_Transform')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFM instead.", DeprecationWarning)

def NewParameterTransform(morph_points, transform_points, name):

	"""

	Function for the creation of a transform morph parameter for morph points.


	@morph_points object: A list of morph points.

	@transform_points object: A list of 6 points to get transformation coordinates or 2 coordinates.

	@name string: (optional)The desired name of the parameter.
	(Default: 'Transform')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

def NewParameterTranslate(morph_points, dx, dy, dz, coord, name):

	"""

	Function for the creation of a tranlsate morph parameter for morph points.


	@morph_points object: A list of morph points.

	@dx float: The x component of the displacement vector.

	@dy float: The y component of the displacement vector.

	@dz float: The z component of the displacement vector.

	@coord object: (optional)A coordinate system that the displacement vector will be defined.
	If coord is None the global coordinate system will be used.
	(Default: None)

	@name string: (optional)The desired name for the new parameter.
	(Default: 'Translate')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

def NewParameterEdgeFit(morph_edges, curves, name):

	"""

	Function for the creation of an edge fit morph parameter for morph edges.


	@morph_edges object: A list of morph edges.

	@curves object: A list of curves.

	@name string: (optional)The desired name for the new parameter.
	(Default: 'Edge_Fit')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

def NewParameterExtend(morph_points, morph_edges, name):

	"""
	Deprecated since version 18.0.0. Use function NewParameterSlideBoxPoints instead.

	Function for the creation of a parameter that slides box points.


	@morph_points object: A list of morph points.

	@morph_edges object: A list of morph edges.

	@name string: (optional)The desired name of the parameter.
	(Default: 'Slide Box Points')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 18.0.0. Use function NewParameterSlideBoxPoints instead.", DeprecationWarning)

def NewParameterOffset(morph_faces, name):

	"""

	Function for the creation of an offset morph parameter for morph faces.


	@morph_faces object: A list of morph faces.

	@name string: (optional)The desired name for the new parameter.
	(Default: 'Offset')

	@returns object: Returns a reference to the newly created parameter object on success, or None on failure.

	"""

def NewParameterRadiusInner(concentric_edges, name):

	"""

	Function for the creation of a radius inner morph parameter for cylindrical morph boxes.


	@concentric_edges object: A list of concentric edges.

	@name string: (optional)The desired name for the new parameter.
	(Default: 'Radius_Inner')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

def NewParameterRadiusOuter(morph_faces, name):

	"""

	Function for the creation of a radius outer morph parameter for cylindrical morph boxes.


	@morph_faces object: A list of circular faces of cylindrical morph boxes.

	@name string: (optional)The desired name for the new parameter.
	(Default: 'Radius_Outer')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

def NewParameterRotate(morph_points, x, y, z, dx, dy, dz, coord, name):

	"""

	Function for the creation of a rotate morph parameter for morph points.


	@morph_points object: A list of morph points.

	@x float: The x component of the origin's position vector of the rotation axis.

	@y float: The y component of the origin's position vector of the rotation axis.

	@z float: The z component of the origin's position vector of the rotation axis.

	@dx float: The x component of the direction vector of the rotation axis.

	@dy float: The y component of the direction vector of the rotation axis.

	@dz float: The z component of the direction vector of the rotation axis.

	@coord object: (optional)A coordinate system that the rotation axis will be defined.
	If coord is None the global coordinate system will be used.
	(Default: None)

	@name string: (optional)The desired name for the new parameter.
	(Default: 'Rotate')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

def NewParameterUserTangent(morph_tang, name):

	"""

	Function for the creation of a user tanget morph parameter for morph edges.


	@morph_tang object: A list of morph tangents.

	@name string: (optional)The desired name for the new parameter.
	(Default: 'UserTangent')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

def NewParameterScale(morph_points, x, y, z, name):

	"""

	Function for the creation of a scale morph parameter for morph points.


	@morph_points object: A list of morph points.

	@x float: The x component of the scale origin.

	@y float: The y component of the scale origin.

	@z float: The z component of the scale origin.

	@name string: (optional)The desired name for the new parameter.
	(Default: 'Scale')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

def NewParameterSlideFeatureCurve(feature, curves, follow_orientation, name):

	"""
	Deprecated since version 21.1.0. Use class DCFeatureSlide instead.

	Function for the creation of a slide feature on curve parameter.


	@feature object: A list of elements that describes the feature.

	@curves object: An ANSA curve on which the feature will slide on.

	@follow_orientation boolean: (optional)A flag to determine if the feature will follow the curve's orientation.
	(Default: True)

	@name string: (optional)The desired name for the new parameter.
	(Default: 'SF_Curve')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.1.0. Use class DCFeatureSlide instead.", DeprecationWarning)

def NewParameterSlideFeatureRotate(feature, x, y, z, dx, dy, dz, coord, name):

	"""
	Deprecated since version 21.1.0. Use class DCFeatureSlide instead.

	Function for the creation of a slide feature rotate parameter.


	@feature object: A list of elements that describes the feature.

	@x float: The x component of the origin's position vector of the rotation axis.

	@y float: The y component of the origin's position vector of the rotation axis.

	@z float: The z component of the origin's position vector of the rotation axis.

	@dx float: The x component of the direction vector of the rotation axis.

	@dy float: The y component of the direction vector of the rotation axis.

	@dz float: The z component of the direction vector of the rotation axis.

	@coord object: (optional)A coordinate system that the displacement vector will be defined.
	If coord is None the global coordinate system will be used.
	(Default: None)

	@name string: (optional)The desired name for the new parameter.
	(Default: 'SF_Rotate')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.1.0. Use class DCFeatureSlide instead.", DeprecationWarning)

def NewParameterSlideFeatureScale(feature, x, y, z, name):

	"""
	Deprecated since version 21.1.0. Use class DCFeatureSlide instead.

	Function for the creation of a slide feature scale parameter.


	@feature object: A list of elements that describes the feature.

	@x float: The x component of the scale origin.

	@y float: The y component of the scale origin.

	@z float: The z component of the scale origin.

	@name string: (optional)The desired name for the new parameter.
	(Default: 'SF_Scale')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.1.0. Use class DCFeatureSlide instead.", DeprecationWarning)

def NewParameterSlideFeatureTranslate(feature, dx, dy, dz, coord, name):

	"""
	Deprecated since version 21.1.0. Use class DCFeatureSlide instead.

	Function for the creation of a slide feature translate parameter.


	@feature object: A list of elements that describes the feature.

	@dx float: The x component of the displacement vector.

	@dy float: The y component of the displacement vector.

	@dz float: The z component of the displacement vector.

	@coord object: (optional)A coordinate system that the displacement vector will be defined.
	If coord is None the global coordinate system will be used.
	(Default: 'None')

	@name string: (optional)The desired name for the new parameter.
	(Default: 'SF_Translate')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.1.0. Use class DCFeatureSlide instead.", DeprecationWarning)

def NewParameterTailoredBlank(entities, properties, lengths, origin, normal, trajectory, movement, cut_mesh, reconstruct, zones, name):

	"""

	Function for the creation of a 'Tailored Blank' parameter.


	@entities object: A list of shells.

	@properties object: A list of properties that will be applied on elements.

	@lengths object: A list of doubles that specifies the application length for each property.

	@origin object: A list of three doubles that specifies the position vector of the
	origin of the separation plane.

	@normal object: A list of three doubles that specifies the direction vector of the
	normal of the separation plane.

	@trajectory object: (optional)A list of entities that will be used as the trajectory on which
	separation plane will move.
	(Default: None)

	@movement integer: (optional)A variable that controls the type of movement of the seperation plane. 
	Possible values are:
	0 for "Follow trajectory"
	1 for "Sweep on trajectory"
	2 for "Glide on trajectory"
	(Default: 0)

	@cut_mesh boolean: (optional)An option that controls if plane cut will take place at each 
	property change.
	(Default: False)

	@reconstruct boolean: (optional)An option to determine if reconstruction of the affected elements 
	will take place after the application of cut.
	This option is meaningful only if "cut_mesh" is set to True. 
	(Default: False)

	@zones integer: (optional)An option to determine the number of zones that will be reconstructed
	around cut area.
	This option is meaningful only if "reconstruct" is set to True.
	(Default: 0)

	@name string: (optional)The desired name for the created parameter.
	If not provided ANSA will automatically decide a name for the newly 
	created parameter.

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

def NewMorphAlignArgs(entities, target_entities, distance, offset, user_direction, align_to_midplane, align_on_geometry):

	"""

	Function for the creation of an object to be used in creating an Align parameter.


	@entities object: A list with morph points to align.

	@target_entities object: A list with entities where morph points will be aligned.
	Can have either 3 points to define a plane or anything else.

	@distance float: (optional)The alignment distance.

	@offset float: (optional)Any offset value.

	@user_direction object: (optional)A list with 3 doubles to define a used defined vector.

	@align_to_midplane boolean: (optional)Boolean to define if it will align to mid plane.

	@align_on_geometry boolean: (optional)Boolean to define if it will align to geometry.

	@returns object: Returns a list containing references to the newly created objects on sucess, or None on failure.

	"""

def DFMGetContents(parameter, category):

	"""
	Deprecated since version 21.0.0. Use class DFM instead.

	A function that returns the entities that participate in the DFM parameter.


	@parameter object: The DFM Parameter.

	@category string: (optional)Option to define which entities should be returned:
	- "__CONTROL__" will return the control entities.
	- "__MORPHED__" will return the morphed entities.
	- "__BOUNDS__" will return the bounds.
	- "__CONSTRAINTS__" will return the constraints.

	@returns object: Returns a list with the ANSA entities that participate in the DFM parameter.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFM instead.", DeprecationWarning)

def DFMRecalculateBounds(parameter):

	"""
	Deprecated since version 21.0.0. Use class DFM instead.

	Function that auto recalculates and updates the bounds of a DFM parameter.


	@parameter object: The DFM parameter.

	@returns boolean: Returns True on success, or False otherwise.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFM instead.", DeprecationWarning)

def DFMSetContents(parameter, category, entities, recalculate_bounds):

	"""
	Deprecated since version 21.0.0. Use class DFM instead.

	Function to set the entities that participate in the defined DFM parameter.


	@parameter object: The DFM Parameter.

	@category string: An argument to define which elements will be replaced:
	-"__MORPHED__" will replace the morphed entities.
	-"__BOUNDS__" will replace the bounds.
	- "__CONSTRAINTS__" will replace the constraints.

	@entities object: A list with the new entities.

	@recalculate_bounds boolean: (optional)An option to enable the automatic bound determination. 
	(Default: True)

	@returns boolean: Returns True on success, False otherwise.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFM instead.", DeprecationWarning)

def MorphParamSetSlideContents(parameter, feature):

	"""

	Function to set entities in Slide Feature parameter.


	@parameter object: The Slide Feature parameter.

	@feature object: A list with all the slide entities.

	@returns boolean: Returns True on success, False otherwise.

	"""

def BoxesByWireframe3D(curves, box_type, max_surf_len, max_vol_len):

	"""

	Function that generates Ortho Morphing, Hexa Block or Size boxes out of a wireframe of 3D Curves. 


	@curves object: A list of 3D Curves. (ANSA Entities, type = "CURVE")

	@box_type string: (optional)Keyword in order to specify the type of the boxes to be generated.
	If no keyword or false keyword is specified, the default box type is the 
	morphing box. 
	- "Morph" - for morphing boxes.
	- "Hexa_Block" - for hexa block boxes.
	- "Size_Box" - for size boxes.

	@max_surf_len float: (optional)Maximum surface length. Used optionally only in the case of size boxes.
	(Default: 1)

	@max_vol_len float: (optional)Maximum volume length. Used optionally only in the case of size boxes.
	(Default: 1)

	@returns object: Returns a list with the created boxes.

	"""

def MorphAdapt (entities, fe_or_geom, bounds, transform, split, angle, part):

	"""

	A function to create a morphing box that will adapt on a selected FE or geometry area.
	There is also the option to adapt the bounding morphing faces of the box to the preselected bounds.
	The user can select 0, 1 or 2 bounds. A bound can be a morphing face, a cross-section or a working plane.
	The resulting box can be expanded in order to include all the selected entities (transform = True) 
	and also can be splitted to multiple boxes (split = True) based on an angle criterion (angle: angle 
	between two successive cutting planes that pass from the middle line of the selected area, in degrees).  


	@entities object: A list that contain shells or solids (type : "SHELL", "SOLID") and 
	geometric faces (type: "FACE"). The box will be adapted on these 
	entities based on the boolean value of the next argument (fe_or_geom).

	@fe_or_geom boolean: True: The Box will adapt on shells and solids. 
	False: The Box will adapt on faces.

	@bounds object: (optional)A list with zero, one or two objects, which are the bounds of the morphing box.
	These can be Morphing Faces (type: "MORPHFACE"), Cross-Sections (type: "CROSS_SECTION") 
	or Working Planes(type: "WPLANE").
	The user can select two different type of bounds.
	Default Value: empty list = {}

	@transform boolean: (optional)An option in order to expand the box in such a way that no red hatches 
	are emerging in the 4 side morphing faces. 
	(Default: False)

	@split boolean: (optional)An option to split the morphing box in multiple boxes based on an angle criterion 
	between successive cutting planes in the principal axis of the selection volume.
	(Default: False)

	@angle float: (optional)The angle on which the splitting of the box can be performed.
	The angle varies between 0-90 degrees.
	-90 degrees means that no split will occur (there is a tolerance of 90 
	 degrees turning angle).
	-0 degrees means that there is no tolerance at all and the box will split to 
	 as many boxes as possible. 
	(Default: 90.0)

	@part object: (optional)The part where the resulting box will belong to. 
	(Default: None)

	@returns object: Returns a list with the resulting morphing boxes that were created.
	In all other cases, except from the enabled split option, the list will have only one member.

	"""

def AlignBoxPoints(entities, target_entities, distance, offset, user_direction, align_to_midplane, align_on_geometry):

	"""

	Script function to align box points on target entities.


	@entities object: A list with box points to align.

	@target_entities object: A list with entities where box points will be aligned. Can have either 
	3 points to define a plane or anything else.

	@distance float: (optional)The alignment distance.

	@offset float: (optional)Any offset value.

	@user_direction object: (optional)A list with 3 doubles to define a used defined vector.

	@align_to_midplane boolean: (optional)Boolean to define if it will align to mid plane.

	@align_on_geometry boolean: (optional)Boolean to define if it will align to geometry.

	@returns integer: Returns 1 in case of successful alignment, 0 in case of failure.

	"""

def CreateDvgridsFromParameter(morph_parameter, design_variable, distance, tolerance):

	"""

	Script function for creating DVGRID's from a morphing parameter movement.


	@morph_parameter object: The parameter element.

	@design_variable object: (optional)The DESVAR element. If set to None. a new one will be created.

	@distance float: (optional)The distance to move the morph parameter.
	(Default: 1)

	@tolerance float: (optional)is the tolerance to accept a movement as valid and record a dvgrid for it.
	(Default: 0)

	@returns object: Returns the input or the created DESVAR object on success, None on failure.

	"""

def MorphLinks(morph_box_links, all_depths):

	"""

	A function for getting the link information of morphing boxes


	@morph_box_links object: A list of morphing boxes.

	@all_depths boolean: (optional)Set to "True" to get link information for all linked morphes 
	with the same "Parent".
	Set to "False" to get link information for only one level 
	"Parent -> children" or "Child->Parent"
	(Default: "False")

	@returns object: Returns a dictionary with key the given morphing box and data a list with linked morphing boxes.

	"""

def NewParameterSlideBoxPoints(morph_points, morph_edges, name):

	"""

	Function for the creation of a parameter that slides box points.


	@morph_points object: A list of morph points.

	@morph_edges object: A list of morph edges.

	@name string: (optional)The desired name of the parameter.
	(Default: 'Slide Box Points')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

def GetDoeStudyCurrentExperimentDir():

	"""

	A function that returns the full path of the current experiment's directory.


	@returns object: Returns a string that corresponds to the experiment's path on success, 
	or None on failure (if DOE is not running when function is called).

	"""

def GetDoeStudyExperiments(design_variables, algorithm, level, experiments_number, seed, taguchi_array, dv_taguchi_columns, reject_duplicates, comb_file):

	"""

	Function to get the experiments of the input design variables.


	@design_variables object: list or objects of design variables and/or optimization tasks
	(in case of optimization task, design variables are derived 
	from them)

	@algorithm string: algorithm used to generate the experiments.
	Supported algorithms are " "Full Factorial", "Uniform Latin Hypercube",
	"Random", "Taguchi Orthogonal Arrays", "Mod.Ext.Lattice.Seq(MELS)" and "Linear".

	@level object: (optional)it may be a single integer value used for all design variables 
	("Full Factorial" or "Taguchi Orthogonal Arrays" algorithms) or
	a dictionary of design variable and level value (for "Full Factorial"
	every design variable may have its own level value). Default value
	is 2.

	@experiments_number integer: (optional)the number of the generated experiments (used in "Uniform Latin Hypercube", "Random" and "Linear" algorithms).

	@seed integer: (optional)positive number used to initialize the random number generator
	(used in "Uniform Latin Hypercube" and "Random" algorithms).

	@taguchi_array string: (optional)Taguchi array to be used for experiments generation. 
	Taguchi array is related to the level value. 
	For level = 2, supported arrays are "L4", "L8", "L12", 
	"L16", "L20", "L24", "L32", "L64", "L128", "L256".
	For level = 3, supported arrays are "L9", "L18", "L27", 
	"L36", "L54", "L81", "L108".
	For level = 4, supported arrays are "L16", "L32", "L64".
	For level = 5, supported arrays are "L25", "L50".

	@dv_taguchi_columns object: (optional)dictionary with design variable and the correspondent column 
	(column > 0) of the Taguchi array. By default, the first columns
	of the Taguchi array are used.

	@reject_duplicates boolean: (optional)reject duplicate experiments in Taguchi algorithm

	@comb_file string: (optional)the generated combinations file that contains all
	the experiments of the input design variables

	@returns object: Returns a list of lists (every list corresponds to a single experiment).

	"""

def MorphDistorted():

	"""

	Script function to check all morphing boxes if they are distorted.


	@returns: A list with the distorted morphes

	"""

def NewDFMSweepGlideArgs(entities, path, movement, rigid_deformable):

	"""

	Function for the creation of an object that will be used by the NewParameterDFMSweepGlide function.
	This is an auxiliary function.


	@entities object: A list of entities that will be moved along the path in a sweep or glide manner.

	@path object: A list of entities that will be used to define the sweep/glide path

	@movement string: (optional)String value of movement type. 
	Possible values are:
	"Sweep" [Default]
	"Glide"

	@rigid_deformable string: (optional)String value to control if the entities should move as a
	rigid or deformable body.
	Possible values:
	"Deformable body" [Default]
	"Rigid body"

	@returns object: Returns a reference to the newly created object on sucess, or None on failure.

	"""

def NewParameterDFMSweepGlide(args, entities, bounds, autobounds, name):

	"""
	Deprecated since version 21.0.0. Use class DFM instead.

	Function for the creation of a dfm sweep-glide parameter.


	@args object: A list of objects created by NewDFMSweepGlideArgs.

	@entities object: (optional)A list of entities that will be morphed.
	(Default: None)

	@bounds object: (optional)A list of entities that will retain their position during the morphing action.
	These entities will also affect the deformation of the entities.
	(Default: None)

	@autobounds boolean: (optional)An option to enable the automatic bound determination.
	(Default: True)

	@name string: (optional)The desired name of the parameter.
	(Default: 'DFM_SweepGlide')

	@returns object: Returns a reference to the newly created parameter object on sucess, or None on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFM instead.", DeprecationWarning)

def MorphIntersections(morphes):

	"""

	Script function to collect interesecting entities


	@morphes object: morphes is a list of morphes to check

	@returns object: Return a list with the intersecting elements

	"""

def DeformMorphPoints(morph_points, dx, dy, dz):

	"""

	Function that deforms independently a list of morph points. 


	@morph_points object: a list of morph points ('MORPHPOINT')

	@dx object: a list with the x component of the deformation vectors

	@dy object: a list with the y component of the deformation vectors

	@dz object: a list with the z component of the deformation vectors

	@returns integer: 1 on success and 0 on failure

	"""

def DCFeatureSlideApply(entity, dx, dy, dz, rx, ry, rz, fx, fy, fz):

	"""

	The function applies the deformation to the given DC_FEATURE_SLIDE entity.


	@entity object: The DC_FEATURE_SLIDE entity

	@dx float: Deformation value in local x-axis.

	@dy float: Deformation value in local y-axis.

	@dz float: Deformation value in local z-axis.

	@rx float: Angle around local x-axis.

	@ry float: Angle around local y-axis.

	@rz float: Angle around local z-axis.

	@fx float: Scale value in local x-axis.

	@fy float: Scale value in local y-axis.

	@fz float: Scale value in local z-axis.

	"""

def DCFeatureSlideSurfaceApply(entity, ds, dt, rw, fs, ft):

	"""

	The function applies the deformation to the given DC_FEATURE_SLIDE entity.


	@entity object: The DC_FEATURE_SLIDE entity.

	@ds float: Deformation value in local s-axis.

	@dt float: Deformation value in local t-axis.

	@rw float: Angle around local w-axis.

	@fs float: Scale value in local s-axis.

	@ft float: Scale value in local t-axis.

	"""

def DCFeatureSlidePathApply(entity, dist):

	"""

	The function applies the deformation to the given DC_FEATURE_SLIDE entity.


	@entity object: The DC_FEATURE_SLIDE entity.

	@dist float: Distance on defined path.

	"""

def DCFeatureCopyApply(entity, dx, dy, dz, rx, ry, rz, fx, fy, fz, steps):

	"""

	The function applies the deformation to the given DC_FEATURE_COPY entity.


	@entity object: The DC_FEATURE_COPY entity.

	@dx float: Deformation value in local x-axis.

	@dy float: Deformation value in local y-axis.

	@dz float: Deformation value in local z-axis.

	@rx float: Angle around local x-axis.

	@ry float: Angle around local y-axis.

	@rz float: Angle around local z-axis.

	@fx float: Scale value in local x-axis.

	@fy float: Scale value in local y-axis.

	@fz float: Scale value in local z-axis.

	@steps integer: The number of new features that would be generated.

	"""

def DCFeatureCopySurfaceApply(entity, ds, dt, rw, fs, ft, steps):

	"""

	The function applies the deformation to the given DC_FEATURE_COPY entity.


	@entity object: The DC_FEATURE_COPY entity.

	@ds float: Deformation value in local s-axis.

	@dt float: Deformation value in local t-axis.

	@rw float: Angle around local w-axis.

	@fs float: Scale value in local s-axis.

	@ft float: Scale value in local t-axis.

	@steps integer: The number of new features that would be generated.

	"""

def DCFeatureCopyPathApply(entity, dist, steps):

	"""

	The function applies the deformation to the given DC_FEATURE_COPY entity.


	@entity object: The DC_FEATURE_COPY entity.

	@dist float: Distance on defined path.

	@steps integer: The number of new features that would be generated.

	"""

def CheckForDuplicateBoxes(tolerance, check_on):

	"""

	Function for the check of boxes duplicates. Given the tolerance, similar boxes are identified.


	@tolerance float: (optional)A tolerance to define maximum value of boxes differences.
	Default value depends on node tolerance.

	@check_on string: (optional)Can have values 'all' or 'visible', for boxes to run the check.
	The default value runs a check for visible entities.

	@returns object: Returns a list of duplicate box groups. Each group is implemented as a list of similar box entities.

	"""

def MorphConstraintFlange(entities, contacts, morphed, bounds, autobounds, align, offset ):

	"""
	Deprecated since version 21.0.0. Use class ConstraintFlanges instead.

	A function for creating a flange morph constraint.
	
	The generated constraint may be included in the morphed entities of a DFM, and will force 
	the constraint's 'entities' to adjust on 'contacts' surface when the DFM 
	executes. To alleviate and/or confine the effects of the constraint, 'morphed' and 'bounds' 
	entities may be provided to the constraint, essentially defining a transition region.
	
	In most aspects, the constraint operates like an automatic DFM, subsequent to the main DFM.
	


	@entities object: A list of the entities to define flange area.

	@contacts object: A list of the entities to define contact area.

	@morphed object: A list of the entities to be morphed by constraint.

	@bounds object: A list of the entities defining bounds of constraint's fitting process.

	@autobounds boolean: (optional)An option to enable the automatic bounds determination.
	(Default: False)

	@align string: (optional)An option to preserve the current flange distance or align based on an offet value 
	- 'preserve' : Preserve the flange distance from contact area.
	- 'thickness' : Set an offset distance from contact area.
	(Default: 'preserve')

	@offset float: (optional)User defined flange('entities') offset distance from 'contact' area.
	Enabled if 'align' argument set to 'thickness'

	@returns object: It returns the created morph constraint.

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class ConstraintFlanges instead.", DeprecationWarning)

def VideoFromEntities(filename, parameters, initial_final, frames, duration, lock_view_time, images_per_sec):

	"""

	Function for video creation using parameters for morph. Video options are provided.


	@filename string: Video will be saved at this path.
	The extension of file name determines the video format.

	@parameters object: A list of parameters to be used for morphing.
	Could be morph parameters, design variables or an optimization task.

	@initial_final object: (optional)A list of initial and final values.
	Two values for each parameter are required.

	@frames integer: (optional)Video frames per second default value at 20fps.

	@duration float: (optional)Video duration default value at 5 sec.

	@lock_view_time object: (optional)A dictionary including lock view names as keys and appearance times as values.

	@images_per_sec integer: (optional)how many images should be taken per second for the video creation (increase for quality or decrease for speed), default value 4

	@returns: Always returns None.

	"""

def GetDoeStudyCurrentExperimentId():

	"""

	A function that return the active's experiment id


	@returns integer: Returns a integer experiment id

	"""

def MorphSplitToHexa(box_faces, tangency, preserve_local_shape, fit_new_skin_edges, work_on, ret_ents):

	"""

	Takes a MORPHFACE or HEXA_BLOCK_FACE list and splits the boxes that are on the 
	specific faces and their opposites to hexas. Works only on pentaboxes or in 
	hexaboxes.


	@box_faces object: It sets the faces of the morph that are going to be splitted to hexa boxes.

	@tangency string: Sets the type of tangency
	'off'          is for no tangency
	'default'      is for default tangency
	'user_tangent' is for user tangency

	@preserve_local_shape boolean: (optional)If set to True, it preserves the local shape of the pre-existing moedges 
	after the split by inserting more points.
	This option is available only when tangency is set to 'off'.
	If tangency is different than 'off', then this argument value is irrelevant

	@fit_new_skin_edges boolean: (optional)If set to True, new skin edges will fit on the underlying model.
	If fit_new_skin_edges will not be set, then the default argument is false.

	@work_on string: (optional)Sets where the projection is going to take place
	'whole_db' fit skin edges will take place the whole database
	'visible'  fit skin edges will take place only on the visible elements
	If work_on is not set then whole_db will be the default argument.
	This option is only available only when fit_skin_edges is set to true.

	@ret_ents boolean: (optional)If set to true it returns the new boxes generated from the function as tuple 
	or if set to false returns only if the procedure was successful.

	@returns object: If 'ret_ents' argument is set to true it returns a tuple where its first argument returns true or false 
	depending on the success of the procedure and for the second element it returns the new 
	and modified morphes.
	If 'ret_ents' argument is set to false it returns only true or false depending on the success of the procedure.

	"""

def NewParameterDFMSymmetry(entity):

	"""
	Deprecated since version 21.0.0. Use class DFM instead.

	Function for the creation of DFM symmetry parameter


	@entity object: Dfm morph parameter.

	@returns object: Returns a reference to the newly created dfm morph parameter

	"""

	import warnings; warnings.warn("Deprecated since version 21.0.0. Use class DFM instead.", DeprecationWarning)

def NewDCFeatureSlide(entities, coord):

	"""

	The function creates a new DC_FEATURE_SLIDE entity.


	@entities object: A list of entities that will slide.

	@coord object: The initial coordinate

	@returns: Returns the DC_FEATURE_SLIDE entity.

	"""

def DCSymmetry(design_change):

	"""
	Deprecated since version 21.1.0. Use class DCPosition instead.

	Script function to create a symmetric, related to the default symmetry plane, design change entity from an existing one. 


	@design_change object: DESIGN_CHANGE entity (DC_POSITION, DC_CROSS_SECTION, DC_FEATURE_COPY, DC_FEATURE_SLIDE)

	@returns object: The symmetric DESIGN_CHANGE entity or None if creation fails.

	"""

	import warnings; warnings.warn("Deprecated since version 21.1.0. Use class DCPosition instead.", DeprecationWarning)

def OptimizationTool(optimization_task, load_experiments, export_file, dv_file, doe_algorithm, number_of_designs, hide_buttons, show_deviation, clear_table, save_in_dm):

	"""

	Function to open OptimizationTool or for creating DOE experiments.


	@optimization_task object: (optional)An Optimization_Task item.

	@load_experiments string: (optional)A filename with the values to be loaded in the window.

	@export_file string: (optional)A filename to save created experiments in the table on confirmation.

	@dv_file string: (optional)A filename to import Design Variables, the format is the same as in Optimization Task - DVFile.

	@doe_algorithm string: (optional)The selected algorithm values can be: 
	-'Linear'
	-'Random'
	-'Full Factorial'
	-'Uniform Latin Hypercube'

	@number_of_designs integer: (optional)The number of designs to generate

	@hide_buttons boolean: (optional)Simplified view of the tool, showing only the DOE-Setup page.

	@show_deviation boolean: (optional)Shows the deviation from current value in the DOE table.

	@clear_table boolean: (optional)Clears the table before applying any generation or importing of experiments.

	@save_in_dm boolean: (optional)Flag to set the tool to work with DM, instead of local directory

	@returns integer: Return 0 for success or 1 for failure, the function will wait only if hide_buttons = True.

	"""

def PMEntityGeometryUpdate(pm_entities):

	"""

	Function that will update the geometry managed by PM_EXTRUDE, PM_SWEEP and PM_LOFT entities.
	It will identify any modified curves of the cross sections and will recreate the related faces, while trying not to affect the rest.


	@pm_entities object: An iterable with PM_EXTRUDE, PM_SWEEP and PM_LOFT entities.

	@returns object: Always returns None

	"""

def PMEntityGeometryRegenerate(pm_entities):

	"""

	Function that will regenerate the geometry managed by PM_EXTRUDE, PM_SWEEP and PM_LOFT entities.
	It will delete all the old faces and will create new ones.


	@pm_entities object: An iterable with PM_EXTRUDE, PM_SWEEP and PM_LOFT entities.

	@returns object: None

	"""

def PMEntityGeometryDelete(pm_entities):

	"""

	Function that will delete the geometry managed by PM_EXTRUDE, PM_SWEEP and PM_LOFT entities.


	@pm_entities object: An iterable with PM_EXTRUDE, PM_SWEEP and PM_LOFT entities.

	@returns object: None

	"""

def PMEntityGeometryRelease(pm_entities):

	"""

	Function that removes the association of the created faces with PM_EXTRUDE, PM_SWEEP and PM_LOFT entities and ensures that any action further on, will not affect these faces any more. 


	@pm_entities: An iterable with PM_EXTRUDE, PM_SWEEP and PM_LOFT entities.

	@returns object: None

	"""

def SculptingSmooth(smooth_area, smooth_algorithm, distortion, angle, intensity, iterations):

	"""

	Smooth area using sculpting smooth algothims


	@smooth_area object: A list of entities that will smooth

	@smooth_algorithm string: The smooth algorithm. Should be 'Generic' or 'Feature preserve'.

	@distortion float: (optional)Distortion parameter for 'Generic' smooth algothim.  Higher values mean that the edges are not preserved at all. The value should be between 0. and 1.

	@angle float: (optional)Feature angle for 'Feature preserve' algorithm. The minimum angle for the features to be preserved. Feature angles below that value will be smoothed.

	@intensity float: (optional)The intensity of the smooth algorithm. The value should be between 0. and 1.

	@iterations integer: (optional)Number of smooth iterations. Default value is 1.

	@returns integer: This function always returns 1

	"""

def NewParameterCylindricalSpin(morph_point, name):

	"""

	Function for the creation of a spin morph parameter on cylindrical morph box.


	@morph_point object: A single morph point of cylindrical morph box.

	@name string: (optional)The desired name for the new parameter.
	(Default: 'Spin')

	@returns: Returns a reference to the newly created parameter on sucess, or None on failure.

	"""

class BoxSplit:

	"""

	A class that handles all functionality related to splits of morphing, hexa-block and size boxes.

	"""


	fit_new_skin_edges = None
	"""
	fit new skin edges on the underlying geometry (geometric or finite elements model) , Default: False

	"""

	work_on = None
	"""
	'all'  or 'visible',   Default: 'all'

	"""

	def on_points(box_points):

		"""

		Split the boxes on existing middle box points of the same edge. 


		@box_points object: An iterable containing box point entities (MORPHPOINT, HEXA_BOX_POINT, SIZEBOXPOINT)

		@returns integer: 1 on success, 0 on failure

		"""


	def number(box_edges, number_of_splits):

		"""

		Split box edges to a number of equally spaced intervals.  


		@box_edges object: An iterable of box edges entities (MORPHEDGE, HEXA_BOX_EDGE, SIZEBOXEDGE)

		@number_of_splits integer: The number of splits to be performed for each box edge.

		@returns integer: 1 on success, 0 on failure

		"""


	def project(box_edge, points):

		"""

		Split a box edge on the projections of point entities upon it.


		@box_edge object: A box edge entity (MORPHEDGE, HEXA_BOX_EDGE, SIZEBOXEDGE)

		@points object: An iterable of point-like entities (MORPHPOINT, HEXA_BOX_POINT, SIZEBOXPOINT, HOT POINT)

		@returns: 1 on success , 0 on failure

		"""


	def to_penta(box_points):

		"""

		Split boxes in half by creating two penta boxes for each box.  


		@box_points object: An iterable of box point entities (MORPHPOINT, HEXA_BOX_POINT, SIZEBOXPOINT). Boxes will be split on these points. The iterable should contain an even number of points.

		@returns integer: 1 on success, 0 on failure

		"""


	def cut(box_points_a, box_point_b):

		"""

		Split a box on two points of opposite edges


		@box_points_a object: An iterable of box point entities or a single box point entity (MORPHPOINT, HEXA_BOX_POINT, SIZEBOXPOINT). In the first case, each split uses two box points from the iterable sequentially.

		@box_point_b object: (optional)A box point entity (MORPHPOINT, HEXA_BOX_POINT, SIZEBOXPOINT). Only in case that the first argument is a single box point entity.

		@returns: 1 on success, 0 on failure

		"""


	def __init__(fit_new_skin_edges, work_on):

		"""

		Constructor of class


		@fit_new_skin_edges boolean: (optional)The same as object's member

		@work_on string: The same as object's member

		"""

class Create:

	"""

	Class providing methods for the creation of features (openings, stamps, ribs, beads) in the finite elements mesh. 

	"""


	invert_direction = None
	"""
	Turn the created feature upside down. Default: False

	"""

	auto_reconstruct = None
	"""
	A dictionary with key-value pairs as of "set_improve_mesh" method. See below. Default: None

	"""

	set_id = None
	"""
	The id of an ANSA entity "SET" to which the created entities should be added. Default: 0

	"""

	save_morph_parameter = None
	"""
	Store a DC_FEATURE_SLIDE entity for the created feature. Default: False

	"""

	return_elements = None
	"""
	A list with the created elements. This member cannot be changed.

	"""

	def __init__(invert_direction, auto_reconstruct, set_id, save_morph_parameter):

		"""

		Constructor of class


		@invert_direction boolean: (optional)The same with object's member

		@auto_reconstruct object: (optional)The same with object's member

		@set_id integer: (optional)The same with object's member

		@save_morph_parameter boolean: (optional)The same with object's member

		"""


	def flanged_opening_surface(entities, height, angle, radius, return_characteristics):

		"""


		@entities object: list of ANSA entities

		@height float

		@angle float

		@radius float

		@return_characteristics boolean: (optional)If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

		@returns object: A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

		"""


	def flanged_opening_straight(opening_point1, opening_point2, width, height, angle, radius, straight_rounded, return_characteristics, top_is_width):

		"""


		@opening_point1 object: An ANSA point-like entity.

		@opening_point2 object: An ANSA point-like entity

		@width float

		@height float

		@angle float

		@radius float

		@straight_rounded boolean: (optional)True for "straight-rounded", False for "straight"

		@return_characteristics boolean: (optional)If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

		@top_is_width boolean: (optional)If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

		@returns object: A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

		"""


	def flanged_opening_curved(opening_entities, width, height, angle, radius, curved_rounded, return_characteristics, top_is_width):

		"""


		@opening_entities object: A list of ANSA entities

		@width float

		@height float

		@angle float

		@radius float

		@curved_rounded boolean: (optional)True for "curved_rounded", False for "curved".

		@return_characteristics boolean: (optional)If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned. A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

		@top_is_width boolean: (optional)If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

		@returns object: A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

		"""


	def flanged_opening_circular(center_point, diameter, height, angle, radius, direction_point1, direction_point2, return_characteristics, top_is_width):

		"""


		@center_point object: An ANSA point-like entity

		@diameter float

		@height float: An ANSA point-like entity

		@angle float

		@radius float

		@direction_point1 object: (optional)An ANSA point-like entity

		@direction_point2 object: (optional)An ANSA point-like entity

		@return_characteristics boolean: (optional)If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

		@top_is_width boolean: (optional)If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

		@returns object: A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

		"""


	def stamp_rectangular_rounded(center_point, width1, width2, corner, height, angle, radius1, radius2, direction_point1, direction_point2, return_characteristics):

		"""


		@center_point object: An ANSA point-like entity

		@width1 float

		@width2 float

		@corner float

		@height float

		@angle float

		@radius1 float

		@radius2 float

		@direction_point1 object: (optional)An ANSA point-like entity

		@direction_point2 object: (optional)An ANSA point-like entity

		@return_characteristics boolean: (optional)If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

		@returns object: A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

		"""


	def stamp_circular(center_point, diameter, height, angle, radius1, radius2, direction_point1, direction_point2, return_characteristics, top_is_width):

		"""


		@center_point object: An ANSA point-like entity

		@diameter float

		@height float

		@angle float

		@radius1 float

		@radius2 float

		@direction_point1 object: (optional)An ANSA point-like entity

		@direction_point2 object: An ANSA point-like entity

		@return_characteristics boolean: (optional)If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

		@top_is_width boolean: (optional)If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

		@returns object: A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

		"""


	def stamp_surface(stamp_entities, height, angle, radius1, radius2, return_characteristics):

		"""


		@stamp_entities object: A list of ANSA entities

		@height float

		@angle float

		@radius1 float

		@radius2 float

		@return_characteristics boolean: (optional)If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

		@returns object: A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

		"""


	def rib_3d(rib_top1, rib_top2, rib_height, width, angle, top_type, top_value, bottom_type, bottom_value, length):

		"""


		@rib_top1 object: ANSA entity

		@rib_top2 object: ANSA entity

		@rib_height object: ANSA entity

		@width float

		@angle float

		@top_type string

		@top_value float

		@bottom_type string: An ANSA point-like entity

		@bottom_value float

		@length float

		@returns object: A list of created entities

		"""


	def rib_2d(rib_top1, rib_top2, rib_height, length):

		"""


		@rib_top1 object: ANSA entity

		@rib_top2 object: ANSA entity

		@rib_height object: ANSA entity

		@length float

		@returns object: A list of created entitites

		"""


	def opening_curved(opening_entities, width, curved_rounded):

		"""


		@opening_entities object: A list of ANSA entities

		@width float

		@curved_rounded boolean: (optional)True for "curved_rounded", False for "curved"

		@returns object: A list of created entities

		"""


	def opening_surface(opening_entities):

		"""


		@opening_entities object: A list of ANSA entities

		@returns object: A list of created entities

		"""


	def opening_circular(center_point, diameter, direction_point1, direction_point2):

		"""


		@center_point object: ANSA point-like entity

		@diameter float

		@direction_point1 object: (optional)ANSA point-like entity

		@direction_point2 object: (optional)ANSA point-like entity

		@returns object: A list of created entities

		"""


	def opening_straight(opening_point1, opening_point2, width, straight_rounded):

		"""


		@opening_point1 object: ANSA point-like entity

		@opening_point2 object: ANSA point-like entity

		@width float

		@straight_rounded boolean: (optional)True for "straight_rounded", False for "straight"

		@returns object: A list of created entities

		"""


	def opening_rectangular_rounded(center_point, width1, width2, corner, direction_point1, direction_point2):

		"""


		@center_point object: ANSA point-like entity

		@width1 float

		@width2 float

		@corner float

		@direction_point1 object: (optional)ANSA point-like entity

		@direction_point2 object: (optional)ANSA point-like entity

		@returns object: A list of created entities

		"""


	def bead_straight(bead_point1, bead_point2, width, height, angle, radius1, radius2, straight_rounded, return_characteristics, top_is_width):

		"""


		@bead_point1 object: ANSA point-like entity

		@bead_point2 object: ANSA point-like entity

		@width float

		@height float

		@angle float

		@radius1 float

		@radius2 float

		@straight_rounded boolean: (optional)True for "straight_rounded", False for "straight"

		@return_characteristics boolean: (optional)If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

		@top_is_width boolean: (optional)If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

		@returns object: A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

		"""


	def bead_curved(bead_entities, width, height, angle, radius1, radius2, curved_rounded, return_characteristics, top_is_width):

		"""


		@bead_entities object: A list of ANSA entities

		@width float

		@height float

		@angle float

		@radius1 float

		@radius2 float

		@curved_rounded boolean: (optional)True for "curved_rounded", False for "curved".

		@return_characteristics boolean: (optional)If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

		@top_is_width boolean: (optional)If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

		@returns object: A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

		"""


	def set_improve_mesh(type, zones):

		"""

		Select the mesh improvement method and associated zones around created feature. The "auto_reconstruct" class member shall be a corresponding dictionary with the improvement type ("type") as key and the number of zones ("zones") as value. 


		@type string: "Reconstruct" or "Smooth" or "Reshape" (mesh improvement choice)

		@zones integer: Number of zones included around the created feature for mesh improvement

		"""


	def set_direction_points(direction_point1, direction_point2):

		"""

		This method enables to globally set the direction points that can be used to all of the constructive methods of the class. 


		@direction_point1 object: ANSA point-like entity

		@direction_point2 object: ANSA point-like entity

		"""


	def clear_return_elems():

		"""

		Clears the container of created elements. 


		@returns boolean: True

		"""


	def bead_X_type(bead_point, width1, width2, height, angle_a, radius1, radius2, length1, length2, length3, length4, angle_b, radius_a, radius_b, X_type_rounded, return_characteristics, top_is_width):

		"""


		@bead_point object: ANSA point-like entity

		@width1 float

		@width2 float

		@height float

		@angle_a float

		@radius1 float

		@radius2 float

		@length1 float

		@length2 float

		@length3 float

		@length4 float

		@angle_b float

		@radius_a float

		@radius_b float

		@X_type_rounded boolean: (optional)Set to "True" for an X type stamp with rounded edges.

		@return_characteristics boolean: (optional)If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

		@top_is_width boolean: (optional)If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

		@returns object: A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

		"""


	def bead_L_type(bead_point, width1, width2, height, angle_a, radius1, radius2, length1, length2, angle_b, L_type_rounded, return_characteristics, top_is_width):

		"""


		@bead_point object: An ANSA point-like entity.

		@width1 float

		@width2 float

		@height float

		@angle_a float

		@radius1 float

		@radius2 float

		@length1 float

		@length2 float

		@angle_b float

		@L_type_rounded boolean: (optional)Set to "True" for an L type stamp with rounded edges.

		@return_characteristics boolean: (optional)If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

		@top_is_width boolean: (optional)If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

		@returns object: A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

		"""


	def bead_T_type(bead_point, width1, width2, height, angle_a, radius1, radius2, length1, length2, length3, angle_b, radius_a, T_type_rounded, return_characteristics, top_is_width):

		"""


		@bead_point object: An ANSA point-like entity.

		@width1 float

		@width2 float

		@height float

		@angle_a float

		@radius1 float

		@radius2 float

		@length1 float

		@length2 float

		@length3 float

		@angle_b float: If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

		@radius_a float

		@T_type_rounded boolean: (optional)Set to "True" for a T type stamp with rounded edges.

		@return_characteristics boolean: (optional)If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

		@top_is_width boolean: (optional)If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

		@returns object: A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

		"""


	def flanged_opening_rectangular_rounded(center_point, width1, width2, corner, height, angle, radius1, direction_point1, direction_point2, return_characteristics):

		"""


		@center_point object: A point-like entity to define center of opening.

		@width1 float

		@width2 float

		@corner float

		@height float

		@angle float

		@radius1 float

		@direction_point1 object: (optional)A point-like entity.

		@direction_point2 object: (optional)A point-like entity.

		@return_characteristics boolean: (optional)If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

		@returns object: A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

		"""

class DFMTranslate:

	"""

	Class providing methods to define a translational movement of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action. 

	"""


	value = None
	"""
	Numerical value of movement magnitude.

	"""

	entities = None
	"""
	A list of entities to be translated.

	"""

	coord = None
	"""
	Coordinate entity

	"""

	def set_value(dist):

		"""


		@dist float

		"""


	def insert_entities(entities):

		"""


		@entities object: A list of entities to be included in movement.

		"""


	def set_entities(entities):

		"""


		@entities object: A list of entities to be included in the movement. Preexisting entities will be discarded.

		"""


	def remove_entities(entities):

		"""


		@entities object: A list of entities to be excluded from the movement.

		"""


	def clear_entities():

		"""


		"""


	def decrease_entities_zone(zones):

		"""


		@zones integer: Number of zones around entities to be excluded from movement.

		"""


	def increase_entities_zone(zones):

		"""


		@zones integer: Number of zones around entities to be included in movement.

		"""


	def set_translate_vector(dx, dy, dz):

		"""


		@dx float

		@dy float

		@dz float

		"""


	def set_coord(coord):

		"""


		@coord object: Coordinate entity

		"""


	def __init__():

		"""

		Constructor of class DFMTranslate


		"""

class DFMTransform:

	"""

	Class providing methods to define an euclidean transformation of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action. 

	"""


	value = None
	"""
	Numerical value of movement magnitude

	"""

	entities = None
	"""
	A list of entities to be transformed

	"""

	source_coord = None
	"""
	Coordinate entity

	"""

	target_coord = None
	"""
	Coordinate entity

	"""

	def set_value(dist):

		"""


		@dist float

		"""


	def insert_entities(entities):

		"""


		@entities object: A list of entities to be included in the movement.

		"""


	def set_entities(entities):

		"""


		@entities object: A list of entities to be included in the movement. Preexisting entities will be discarded.

		"""


	def remove_entities(entities):

		"""


		@entities object: A list of entities to be excluded from the movement.

		"""


	def clear_entities():

		"""

		Remove all existing entities included in movement. 


		"""


	def decrease_entities_zone(zones):

		"""


		@zones integer: Number of zones around entities to be excluded from movement.

		"""


	def increase_entities_zone(zones):

		"""


		@zones integer: Number of zones around entities to be included in the movement.

		"""


	def set_source_coord(coord):

		"""


		@coord object: Coordinate entity

		"""


	def set_target_coord(coord):

		"""


		@coord object: Coordinate entity

		"""


	def __init__():

		"""

		Constructor of class MDTransform


		"""

class DFMScale:

	"""

	Class providing methods to define a scaling transformation of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action. 

	"""


	value = None
	"""
	Numerical value of movement magnitude.

	"""

	entities = None
	"""
	A list of entities to be scaled.

	"""

	def set_value(dist):

		"""


		@dist float

		"""


	def insert_entities(entities):

		"""


		@entities object: A list of entities to be included in movement.

		"""


	def set_entities(entities):

		"""


		@entities object: A list of entities to be included in movement. Preexisting entities will be discarded.

		"""


	def remove_entities(entities):

		"""


		@entities object: A list of entities to be excluded from movement.

		"""


	def clear_entities():

		"""

		          Remove all existing entities included in movement. 


		"""


	def decrease_entities_zone(zones):

		"""


		@zones integer: Number of zones around entities to be excluded from movement.

		"""


	def increase_entities_zone(zones):

		"""


		@zones integer: Number of zones around entities to be included in movement.

		"""


	def set_origin(x, y, z):

		"""


		@x float

		@y float

		@z float

		"""


	def __init__():

		"""

		Constructor of class DFMScale


		"""

class DFMOffset:

	"""

	Class providing methods to define an offset movement of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action. 

	"""


	value = None
	"""
	Numerical value of movement magnitude.

	"""

	entities = None
	"""
	A list of entities to offset.

	"""

	def set_value(dist):

		"""


		@dist float

		"""


	def insert_entities(entities):

		"""


		@entities object: A list of entities to be included in movement.

		"""


	def set_entities(entities):

		"""


		@entities object: A list of entities to be included in movement. Preexisting entities will be discarded.

		"""


	def remove_entities(entities):

		"""


		@entities object: A list of entities to be excluded from movement.

		"""


	def clear_entities():

		"""

		          Remove all existing entities included in movement. 


		"""


	def decrease_entities_zone(zones):

		"""


		@zones integer: Number of zones around entities to be excluded from movement.

		"""


	def increase_entities_zone(zones):

		"""


		@zones integer: Number of zones around entities to be included in movement.

		"""


	def __init__():

		"""

		Constructor of DFMOffset class


		"""

class DFMRotate:

	"""

	Class providing methods to define a rotational movement of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action. 

	"""


	value = None
	"""
	Numerical value of movement magnitude.

	"""

	entities = None
	"""
	A list of entities to be rotated.

	"""

	coord = None
	"""
	Coordinate entity

	"""

	def set_value(dist):

		"""


		@dist float

		"""


	def insert_entities(entities):

		"""


		@entities object: A list of entities to be included in movement.

		"""


	def set_entities(entities):

		"""


		@entities object: A list of entities to be included in movement. Preexisting entities will be discarded.

		"""


	def remove_entities(entities):

		"""


		@entities object: A list of entities to be excluded from movement.

		"""


	def clear_entities():

		"""

		          Remove all existing entities included in movement. 


		"""


	def decrease_entities_zone(zones):

		"""


		@zones integer: Number of zones around entities to be excluded from movement.

		"""


	def increase_entities_zone(zones):

		"""


		@zones integer: Number of zones around entities to be included in movement.

		"""


	def set_rotate_axis(x, y, z, dx, dy, dz):

		"""


		@x float

		@y float

		@z float

		@dx float

		@dy float

		@dz float

		"""


	def set_coord(coord):

		"""


		@coord object: Coordinate entity

		"""


	def __init__():

		"""

		Constructor of class DFMRotate


		"""

class DFMSweepGlide:

	"""

	Class providing methods to define a sweep/glide movement of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action. 

	"""


	value = None
	"""
	Numerical value of movement magnitude.

	"""

	entities = None
	"""
	A list of entities to sweep/glide.

	"""

	path = None
	"""
	A list of entities to define path of movement.

	"""

	movement_type = None
	"""
	"Glide" or "Sweep"

	"""

	rigid_deformable = None
	"""
	"Rigid" or "Deformable"

	"""

	def set_value(dist):

		"""


		@dist float

		"""


	def insert_entities(entities):

		"""


		@entities object: list of entities to be included in movement.

		"""


	def set_entities(entities):

		"""


		@entities object: A list of entities to be included in movement. Preexisting entities will be discarded.

		"""


	def remove_entities(entities):

		"""


		@entities object: A list of entities to be excluded from movement.

		"""


	def clear_entities():

		"""

		Remove all existing entities included in movement.


		"""


	def decrease_entities_zone(zones):

		"""


		@zones integer: Number of zones around entities to be excluded from movement.

		"""


	def increase_entities_zone(zones):

		"""


		@zones integer: Number of zones around entities to be included in movement.

		"""


	def insert_path(path_entities):

		"""


		@path_entities object: A list of entities to define path of movement.

		"""


	def set_path(path_entities):

		"""


		@path_entities object: A list of entities to define path of movement. Preexisting entities will be discarded.

		"""


	def remove_path(path_entities):

		"""


		@path_entities object: A list of entities to be excluded from path of movement.

		"""


	def clear_path():

		"""

		Remove all existing entities in path of movement. 


		"""


	def __init__():

		"""

		Constructor of class DFMSweepGlide.


		"""

class DFMFitEdges:

	"""

	A class to define a fit-to-edges transformation of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action. 

	"""


	value = None
	"""
	Numerical value of movement magnitude.

	"""

	source_entities = None
	"""
	A list of entities set as source edges.

	"""

	target_entities = None
	"""
	A list of entities set as target edges.

	"""

	steady_section_entities = None
	"""
	A list of entities set as steady section entities.

	"""

	def set_value(dist):

		"""


		@dist float

		"""


	def set_source_entities(source_entities):

		"""


		@source_entities object: A list of source edges to be included in movement. Preexisting source edges will be discarded.

		"""


	def insert_source_entities(source_entities):

		"""


		@source_entities object: A list of source edges to be included in movement.

		"""


	def remove_source_entities(source_entities):

		"""


		@source_entities object: A list of source edges to be excluded from movement.

		"""


	def clear_source_entities():

		"""

		Remove all existing source edges included in movement.


		"""


	def set_target_entities(target_entities):

		"""


		@target_entities object: A list of target edges to be included in movement. Preexisting target edges will be discarded.

		"""


	def insert_target_entities(target_entities):

		"""


		@target_entities object: A list of target edges to be included in movement.

		"""


	def remove_target_entities(target_entities):

		"""


		@target_entities object: A list of target edges to be excluded from movement.

		"""


	def clear_target_entities():

		"""

		Remove all target edges included in movement. 


		"""


	def decrease_source_zones(zones):

		"""


		@zones integer: Number of zones around source edges to be excluded from movement.

		"""


	def increase_source_zones(zones):

		"""


		@zones integer: Number of zones around source edges to be included in movement.

		"""


	def decrease_target_zones(zones):

		"""


		@zones integer: Number of zones around target edges to be excluded from movement.

		"""


	def increase_target_zones(zones):

		"""


		@zones integer: Number of zones around target edges to be included in movement.

		"""


	def __init__():

		"""

		Constructor of class DFMFitEdges.


		"""


	def set_steady_section(steady_section):

		"""


		@steady_section object: A list of steady section entities to be included in movement.

		"""


	def insert_steady_section(steady_section):

		"""


		@steady_section object: A list of steady section entities to be included in movement. Preexisting steady section entities will be discarded.

		"""


	def remove_steady_section(steady_section):

		"""


		@steady_section object: A list of steady section entities to be excluded from movement.

		"""


	def clear_steady_section():

		"""

		Remove all steady section entities included in movement.


		"""

class DFMFitSurfaces:

	"""

	A class to define a fit-to-surfaces transformation of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action.

	"""


	value = None
	"""
	Numerical value of movement magnitude.

	"""

	source_entities = None
	"""
	A list of entities to define source surface.

	"""

	target_entities = None
	"""
	A list of entities to define target surface.

	"""

	def set_value(dist):

		"""


		@dist float

		"""


	def set_source_entities(source_entities):

		"""


		@source_entities object: A list of source entities to be included in movement. Preexisting source entities will be discarded.

		"""


	def insert_source_entities(source_entities):

		"""


		@source_entities object: A list of source entities to be included in movement.

		"""


	def remove_source_entities(source_entities):

		"""


		@source_entities object: A list of source entities to be excluded from movement.

		"""


	def clear_source_entities():

		"""

		          Remove all existing source entities included in movement.


		"""


	def set_target_entities(target_entities):

		"""

		 


		@target_entities object: A list of target entities to be included in movement. Preexisting target entities will be discarded.

		"""


	def insert_target_entities(target_entities):

		"""


		@target_entities object: A list of target entities to be included in movement.

		"""


	def remove_target_entities(target_entities):

		"""


		@target_entities object: A list of target entities to be excluded from movement.

		"""


	def clear_target_entities():

		"""

		          Remove all target entities included in movement. 


		"""


	def decrease_source_zone(zones):

		"""


		@zones integer: Number of zones around source entities to be excluded from movement.

		"""


	def increase_source_zone(zones):

		"""


		@zones integer: Number of zones around source entities to be included in movement.

		"""


	def decrease_target_zone(zones):

		"""


		@zones integer: Number of zones around target entities to be excluded from movement.

		"""


	def increase_target_zone(zones):

		"""


		@zones integer: Number of zones around target entities to be included in movement.

		"""


	def set_source_target_points(source_points, target_points):

		"""


		@source_points object: A list of points to define source surface.

		@target_points object: A list of points to define target surface.

		"""


	def __init__():

		"""

		Constructor of class DFMFitSurfaces.


		"""

class DFMAlign:

	"""

	A class to define an alignment transformation of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action.

	"""


	source_entities = None
	"""
	A list of entities set as source.

	"""

	target_entities = None
	"""
	A list of entities set as target.

	"""

	max_distance = None

	def set_value(dist):

		"""


		@dist float

		"""


	def set_source_entities(source_entities):

		"""


		@source_entities object: A list of source entities to be included in movement. Preexisting source entities will be discarded.

		"""


	def insert_source_entities(source_entities):

		"""


		@source_entities object: A list of source entities to be included in movement.

		"""


	def remove_source_entities(source_entities):

		"""


		@source_entities object: A list of source entities to be excluded from movement.

		"""


	def clear_source_entities():

		"""

		Remove all source entities included in movement. 


		"""


	def set_target_entities(target_entities):

		"""


		@target_entities object: A list of target entities to be included in movement. Preexisting target entities will be discarded.

		"""


	def insert_target_entities(target_entitites):

		"""


		@target_entitites object: A list of target entities to be included in movement.

		"""


	def remove_target_entities(target_entities):

		"""


		@target_entities object: A list of target entities to be excluded from movement.

		"""


	def clear_target_entities():

		"""

		Remove all target entities included in movement. 


		"""


	def decrease_source_zone(zones):

		"""


		@zones integer: Number of zones around source entities to be excluded from movement.

		"""


	def increase_source_zone(zones):

		"""


		@zones integer: Number of zones around source entities to be included in movement.

		"""


	def decrease_target_zone(zones):

		"""


		@zones integer: Number of zones around target entities to be excluded from movement.

		"""


	def increase_target_zone(zones):

		"""


		@zones integer: Number of zones around target entities to be included in movement.

		"""


	def set_target_plane(x, y, z, dx, dy, dz):

		"""


		@x float

		@y float

		@z float

		@dx float

		@dy float

		@dz float

		"""


	def set_target_axis(x, y, z, dx, dy, dz):

		"""


		@x float

		@y float

		@z float

		@dx float

		@dy float

		@dz float

		"""


	def set_user_direction(dx, dy, dz):

		"""


		@dx float

		@dy float

		@dz float

		"""


	def set_max_distance(max_distance):

		"""


		@max_distance float

		"""


	def set_include_thickness(include_thickness):

		"""


		@include_thickness boolean

		"""


	def set_align_on_axis():

		"""

		Call this method if the alignment must be done on axis. This option is mutually exclusive with "set_align_on_entities".


		"""


	def set_align_on_entities():

		"""

		Call this method if alignment must be done on entities. This option is mutually exclusive with set_align_on_axis method. 


		"""


	def __init__():

		"""

		Constructor of class DFMAlign.


		"""

class ConstraintRigid:

	"""

	Class providing methods to define a constraint of type 'Rigid' to be included in a direct morphing action. The entities belonging to such a constraint shall follow a rigid body motion during the morphing action. Class can be used either to create a MORPH_CONSTRAINT entity of 'Rigid' type or to modify an existing one. 

	"""


	morphed = None
	"""
	A list of entities to be in the transition zone.

	"""

	bounds = None
	"""
	A list of entities set as fixed perimeters.

	"""

	entities = None
	"""
	A list of entities constrained to remain rigid.

	"""

	def insert_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed".

		"""


	def set_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

		"""


	def remove_morphed(morphed):

		"""


		@morphed object: A list of entities to be removed from object's member "morphed".

		"""


	def clear_morphed():

		"""

		Remove all entities from object's member "morphed". 


		"""


	def insert_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds".

		"""


	def set_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

		"""


	def remove_bounds(bounds):

		"""


		@bounds object: A list of entities to be removed from object's member "bounds".

		"""


	def clear_bounds():

		"""

		Remove all entities from object's member "bounds". 


		"""


	def calculate_bounds():

		"""

		Automatic calculation of bounds. The result will be inserted to object's member "bounds". 


		@returns object: A list of entities found as fixed perimeters.

		"""


	def increase_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be included also in object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def decrease_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be excluded from object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def insert_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities".

		"""


	def set_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

		"""


	def remove_entities(entities):

		"""


		@entities object: A list of entities to be excluded from object's member "entities".

		"""


	def clear_entities():

		"""

		Remove all entities from object's member "entities". 


		"""


	def __init__(rigid_constraint):

		"""

		Constructor of class ConstraintRigid. 


		@rigid_constraint object: (optional)MORPH_CONSTRAINT entity of Rigid type.

		"""


	def reg():

		"""

		Create the MORPH_CONSTRAINT entity from a ConstraintRigid object and register it in the database.  


		@returns object: The created and registered MORPH_CONSTRAINT entity. Method returns None if the corresponding entity was already registered.

		"""

class ConstraintPathFollower:

	"""

	Class providing methods to define a constraint of type 'Path Follower' to be included in a direct morphing action. The entities belonging to such a constraint shall follow a user defined path during the morphing action. Class can be used either to create a MORPH_CONSTRAINT entity of 'Path Follower' type or to modify an existing one. 

	"""


	morphed = None
	"""
	A list of entities to be in the transition zone.

	"""

	bounds = None
	"""
	A list of entities set as fixed perimeters.

	"""

	entities = None
	"""
	A list of entities constrained to follow a path.

	"""

	path = None
	"""
	A list of entities that define a path.

	"""

	def insert_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed".

		"""


	def set_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

		"""


	def remove_morphed(morphed):

		"""


		@morphed object: A list of entities to be removed from object's member "morphed".

		"""


	def clear_morphed():

		"""

		          Remove all entities from object's member "morphed". 


		"""


	def insert_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds".

		"""


	def set_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

		"""


	def remove_bounds(bounds):

		"""


		@bounds object: A list of entities to be removed from object's member "bounds".

		"""


	def clear_bounds():

		"""

		Remove all entities from object's member "bounds".


		"""


	def calculate_bounds():

		"""

		Automatic calculation of bounds. The result will be inserted to object's member "bounds". 


		@returns object: A list of entities found as fixed perimeters.

		"""


	def increase_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be included also in object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def decrease_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be excluded from object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def insert_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities".

		"""


	def set_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

		"""


	def remove_entities(entities):

		"""


		@entities object: A list of entities to be removed from object's member "entities".

		"""


	def clear_entities():

		"""

		Remove all entities from object's member "entities". 


		"""


	def insert_path(path_entities):

		"""


		@path_entities object: A list of entities to be inserted in object's member "path".

		"""


	def set_path(path_entities):

		"""


		@path_entities object: A list of entities to be inserted in object's member "path". Preexisting entities will be discarded.

		"""


	def remove_path(path_entities):

		"""


		@path_entities object: A list of entities to be removed from object's member "path".

		"""


	def clear_path():

		"""

		Remove all entities from object's member "path".


		"""


	def __init__(path_follower_constraint):

		"""

		Constructor of class ConstraintPathFollower


		@path_follower_constraint object: (optional)MORPH_CONSTRAINT entity of Path Follower type.

		"""


	def reg():

		"""

		Create the MORPH_CONSTRAINT entity from a ConstraintPathFollower object and register it in the database. 


		@returns object: The created and registered MORPH_CONSTRAINT entity. Method returns None if the corresponding entity was already registered.

		"""

class ConstraintPlanar:

	"""

	Class providing methods to define a constraint of type 'Planar' to be included in a direct morphing action. The entities belonging to such a constraint shall lie all on the same plane, as much as possible, during the morphing action. Class can be used either to create a MORPH_CONSTRAINT entity of 'Planar' type or to modify an existing one. 

	"""


	morphed = None
	"""
	A list of entities to be in the transition zone.

	"""

	bounds = None
	"""
	A list of entities set as fixed perimeters.

	"""

	entities = None
	"""
	A list of entities constrained to remain planar.

	"""

	def insert_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed".

		"""


	def set_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

		"""


	def remove_morphed(morphed):

		"""


		@morphed object: A list of entities to be removed from object's member "morphed".

		"""


	def clear_morphed():

		"""

		          Remove all entities from object's member "morphed". 


		"""


	def insert_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds".

		"""


	def set_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

		"""


	def remove_bounds(bounds):

		"""


		@bounds object: A list of entities to be removed from object's member "bounds".

		"""


	def clear_bounds():

		"""

		Remove all entities from object's member "bounds". 


		"""


	def calculate_bounds():

		"""

		Automatic calculation of bounds. The result will be inserted to object's member "bounds".


		@returns object: A list of entities found as fixed perimeters.

		"""


	def increase_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be included also in object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def decrease_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be excluded from object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def insert_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities".

		"""


	def set_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

		"""


	def remove_entities(entities):

		"""


		@entities object: A list of entities to be excluded from object's member "entities".

		"""


	def clear_entities():

		"""

		Remove all entities from object's member "entities". 


		"""


	def __init__(planar_constraint):

		"""

		Constructor of class ConstraintPlanar.


		@planar_constraint object: (optional)MORPH_CONSTRAINT entity of Planar type.

		"""


	def reg():

		"""

		Create the MORPH_CONSTRAINT entity from a ConstraintPlanar object and register it in the database. 


		@returns object: The created and registered MORPH_CONSTRAINT entity. Method returns None if the corresponding entity was already registered.

		"""

class ConstraintScaled:

	"""

	Class providing methods to define a constraint of type 'Scaled' to be included in a direct morphing action. The entities belonging to such a constraint shall retain their relative size ratios during the morphing action. Class can be used either to create a MORPH_CONSTRAINT entity of 'Scaled' type or to modify an existing one. 

	"""


	morphed = None
	"""
	A list of entities to be in the transition zone.

	"""

	bounds = None
	"""
	A list of entities set as fixed perimeters.

	"""

	entities = None
	"""
	A list of entities constrained to be scaled.

	"""

	def insert_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed".

		"""


	def set_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

		"""


	def remove_morphed(morphed):

		"""


		@morphed object: A list of entities to be removed from object's member "morphed".

		"""


	def clear_morphed():

		"""

		Remove all entities from object's member "morphed". 


		"""


	def insert_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds".

		"""


	def set_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

		"""


	def remove_bounds(bounds):

		"""


		@bounds object: A list of entities to be removed from object's member "bounds".

		"""


	def clear_bounds():

		"""

		 Remove all entities from object's member "bounds". 


		"""


	def calculate_bounds():

		"""

		Automatic calculation of bounds. The result will be inserted to object's member "bounds". 


		@returns object: A list of entities found as fixed perimeters.

		"""


	def increase_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be included also in object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def decrease_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be excluded from object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def insert_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities".

		"""


	def set_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

		"""


	def remove_entities(entities):

		"""


		@entities object: A list of entities to be excluded from object's member "entities".

		"""


	def clear_entities():

		"""

		Remove all entities from object's member "entities". 


		"""


	def __init__(scaled_constraint):

		"""

		Constructor of class ConstraintScaled.


		@scaled_constraint object: (optional)MORPH_CONSTRAINT entity of Scaled type.

		"""


	def reg():

		"""

		Create the MORPH_CONSTRAINT entity from a ConstraintScaled object and register it in the database.  


		@returns object: The created and registered MORPH_CONSTRAINT entity. Method returns None if the corresponding entity was already registered.

		"""

class ConstraintDirectional:

	"""

	Class providing methods to define a constraint of type 'Directional' to be included in a direct morphing action. The entities belonging to such a constraint shall move on a user defined direction during the morphing action. Class can be used either to create a MORPH_CONSTRAINT entity of 'Directional' type or to modify an existing one. 

	"""


	morphed = None
	"""
	A list of entities to be in the transition zone.

	"""

	bounds = None
	"""
	A list of entities set as fixed perimeters.

	"""

	entities = None
	"""
	A list of entities constrained to move in a direction.

	"""

	def insert_morphed(morphed):

		"""


		@morphed object: list of entities to be inserted in object's member "morphed".

		"""


	def set_morphed(morphed):

		"""


		@morphed object: list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

		"""


	def remove_morphed(morphed):

		"""


		@morphed object: A list of entities to be removed from object's member "morphed".

		"""


	def clear_morphed():

		"""

		Remove all entities from object's member "morphed". 


		"""


	def insert_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds".

		"""


	def set_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

		"""


	def remove_bounds(bounds):

		"""


		@bounds object: A list of entities to be removed from object's member "bounds".

		"""


	def clear_bounds():

		"""

		Remove all entities from object's member "bounds".


		"""


	def calculate_bounds():

		"""

		 Automatic calculation of bounds. The result will be inserted to object's member "bounds". 


		@returns object: A list of entities found as fixed perimeters.

		"""


	def increase_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be included also in object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def decrease_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be excluded from object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def insert_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities".

		"""


	def set_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

		"""


	def remove_entities(entities):

		"""


		@entities object: A list of entities to be excluded from object's member "entities".

		"""


	def clear_entities():

		"""

		Remove all entities from object's member "entities". 


		"""


	def set_coord(coord):

		"""


		@coord object: Coordinate entity

		"""


	def set_status(x_status, y_status, z_status):

		"""


		@x_status boolean: (optional)Set active or not the x-status.

		@y_status boolean: (optional)Set active or not the y-status.

		@z_status boolean: (optional)Set active or not the z-status.

		"""


	def set_x_active(status):

		"""


		@status boolean: Set active or not the x-status.

		"""


	def set_y_active(status):

		"""


		@status boolean: Set active or not the y-status.

		"""


	def set_z_active(status):

		"""


		@status boolean: Set active or not the z-status.

		"""


	def __init__(directional_constraint):

		"""

		Constructor of class ConstraintDirectional.


		@directional_constraint object: (optional)A MORPH_CONSTRAINT of Directional type.

		"""


	def reg():

		"""

		Create the MORPH_CONSTRAINT entity from a ConstraintScaled object and register it in the database.  


		@returns object: The created and registered MORPH_CONSTRAINT entity. Method returns None if the corresponding entity was already registered.

		"""

class ConstraintFlanges:

	"""

	Class providing methods to define a constraint of type 'Flanges' to be included in a direct morphing action. The entities belonging to the flanges, shall be aligned to the defined contact area, as much as possible, during the morphing action. Class can be used either to create a MORPH_CONSTRAINT entity of 'Flanges' type or to modify an existing one. 

	"""


	morphed = None
	"""
	A list of entities to be in the transition zone.

	"""

	bounds = None
	"""
	A list of entities set as fixed perimeters.

	"""

	entities = None
	"""
	A list of entities consisting the flanges.

	"""

	contacts = None
	"""
	A list of entities constrained to be in contact with flanges.

	"""

	def insert_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed".

		"""


	def set_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

		"""


	def remove_morphed(morphed):

		"""


		@morphed object: A list of entities to be removed from object's member "morphed".

		"""


	def clear_morphed():

		"""

		Remove all entities from object's member "morphed". 


		"""


	def insert_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds".

		"""


	def set_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

		"""


	def remove_bounds(bounds):

		"""


		@bounds object: A list of entities to be removed from object's member "bounds".

		"""


	def clear_bounds():

		"""

		Remove all entities from object's member "bounds".


		"""


	def calculate_bounds():

		"""

		Automatic calculation of bounds. The result will be inserted to object's member "bounds". 


		@returns object: A list of entities found as fixed perimeters.

		"""


	def increase_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be included also in object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def decrease_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be excluded from object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def insert_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities".

		"""


	def set_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

		"""


	def remove_entities(entities):

		"""


		@entities object: A list of entities to be excluded from object's member "entities".

		"""


	def clear_entities():

		"""

		 Remove all entities from object's member "entities".


		"""


	def insert_contacts(contacts):

		"""


		@contacts object: A list of entities to be inserted in object's member "contacts".

		"""


	def set_contacts(contacts):

		"""


		@contacts object: A list of entities to be inserted in object's member "contacts". Preexisting entities will be discarded.

		"""


	def remove_contacts(contacts):

		"""


		@contacts object: A list of entities to be excluded from object's member "contacts".

		"""


	def clear_contacts():

		"""

		Remove all entities from object's member "contacts". 


		"""


	def set_thickness_flange_gap(offset):

		"""


		@offset float: Flange gap thickness.

		"""


	def set_preserve_flange_gap():

		"""

		Call this method to preserve the flange gap. 


		"""


	def __init__(flanges_constraint):

		"""

		Constructor of class ConstraintFlanges.


		@flanges_constraint object: (optional)MORPH_CONSTRAINT entity of Flanges type.

		"""


	def reg():

		"""

		Create the MORPH_CONSTRAINT entity from a ConstraintFlanges object and register it in the database.  


		@returns object: The created and registered MORPH_CONSTRAINT entity. Method returns None if the corresponding entity was already registered.

		"""

class DCPosition:

	"""

	Class providing methods for a direct morphing action identical to the one provided by Design Change Position functionality in ANSA. 

	"""


	morphed = None
	"""
	A list of entities to be morphed.

	"""

	bounds = None
	"""
	A list of entities to bound the movement.

	"""

	entities = None
	"""
	A list of entities to be translated.

	"""

	value = None
	"""
	Numerical value of movement magnitude.

	"""

	constraints = None
	"""
	A list of MORPH_CONSTRAINT entities participating in the movement.

	"""

	defined_constraints = None
	"""
	A list of MORPH_CONSTRAINT entities related to the contents of the movement. This object cannot be changed.

	"""

	def insert_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed".

		"""


	def set_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

		"""


	def remove_morphed(morphed):

		"""


		@morphed object: A list of entities to be removed from object's member "morphed".

		"""


	def clear_morphed():

		"""

		Remove all entities from object's member "morphed".


		"""


	def insert_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds".

		"""


	def set_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

		"""


	def remove_bounds(bounds):

		"""


		@bounds object: A list of entities to be removed from object's member "bounds".

		"""


	def clear_bounds():

		"""

		Remove all entities from object's member "bounds".


		"""


	def calculate_bounds():

		"""

		Automatic calculation of bounds. The result will be inserted to object's member "bounds". 


		@returns object: A list of entities found as bounds.

		"""


	def increase_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be included also in object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def decrease_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be excluded from object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def insert_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities".

		"""


	def set_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

		"""


	def remove_entities(entities):

		"""


		@entities object: A list of entities to be excluded from object's member "entities".

		"""


	def clear_entities():

		"""

		Remove all entities from object's member "entities".


		"""


	def decrease_entities_zone(zones):

		"""


		@zones integer: Number of zones around entities to be included also in object's member "entities".

		"""


	def increase_entities_zone(zones):

		"""


		@zones integer: Number of zones around entities to be excluded from object's member "entities".

		"""


	def set_user_direction(dx, dy, dz):

		"""


		@dx float

		@dy float

		@dz float

		"""


	def set_value(dist):

		"""


		@dist float

		"""


	def insert_constraints(constraints):

		"""


		@constraints object: A list of MORPH_CONSTRAINT entities to be included in object's member "constraints".

		"""


	def set_constraints(constraints):

		"""


		@constraints object: A list of MORPH_CONSTRAINT entities to be included in object's member "constraints". Preexisting entities will be discarded.

		"""


	def remove_constraints(constraints):

		"""


		@constraints object: A list of MORPH_CONSTRAINT entities to be excluded from object's member "constraints".

		"""


	def clear_constraints():

		"""

		Remove all entities from object's member "constraints".


		"""


	def __init__(dc_position):

		"""

		Constructor of class DCPosition


		@dc_position object: (optional)A "DC_POSITION" entity.

		"""


	def preview():

		"""

		Preview the result of the morphing action. WARNING: Unless method "apply" is called, the morphing action will be finally cancelled in the end of the python script. 


		"""


	def disable_preview():

		"""

		Disable the preview of the morphing action. 


		"""


	def apply():

		"""

		Perform the morphing action and confirm it. After the call to "apply" method, the morphing is permanent and the object is able to perform another morphing with another arbitrary configuration. WARNING: Unless a call to this method, the morphing action will be cancelled at the end of the Python script. 


		"""


	def save_as_DC_Position():

		"""

		Create a "DC_POSITION" entity in the ANSA database based on DCPosition object's definition. 


		@returns object: The created "DC_POSITION" entity or None in case of failure.

		"""

class DFM:

	"""

	Class providing methods for direct morphing of finite elements mesh or geometry entities. 

	"""


	morphed = None
	"""
	A list of entities to be morphed.

	"""

	bounds = None
	"""
	A list of entities to bound the movement.

	"""

	constraints = None
	"""
	A list of MORPH_CONSTRAINT entities participating in the movement.

	"""

	defined_constraints = None
	"""
	A list of MORPH_CONSTRAINT entities related to the contents of the movement. This object cannot be changed.

	"""

	move_types = None
	"""
	A list of objects defining the movement types of morphing. Objects must be instances of the following classes: morph.DFMTranslate, morph.DFMRotate, morph.DFMScale, morph.DFMTransform, morph.DFMFitEdges, morph.DFMFitSurfaces, morph.DFMAlign, morph.DFMSweepGlide

	"""

	volume_finder = None
	"""
	A list of SIZEBOX entities used as volume finders aiding the selection of entities. WARNING: The volume_finder entities are active only in CFD Decks.

	"""

	def insert_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed".

		"""


	def set_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

		"""


	def remove_morphed(morphed):

		"""


		@morphed object: A list of entities to be removed from object's member "morphed".

		"""


	def clear_morphed():

		"""

		Remove all entities from object's member "morphed".


		"""


	def insert_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds".

		"""


	def set_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

		"""


	def remove_bounds(bounds):

		"""


		@bounds object: A list of entities to be removed from object's member "bounds".

		"""


	def clear_bounds():

		"""

		Remove all entities from object's member "bounds".


		"""


	def calculate_bounds():

		"""

		 Automatic calculation of bounds. The result will be inserted to object's member "bounds".


		@returns object: A list of entities found as bounds.

		"""


	def increase_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be included also in object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def decrease_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be excluded from object's member "morphed".

		@returns object: A list of entities included in object's member "morphed".

		"""


	def insert_volume_finder(size_boxes):

		"""


		@size_boxes object: A list of SIZEBOX entities to be inserted in object's member "volume_finder".

		"""


	def set_volume_finder(size_boxes):

		"""


		@size_boxes object: A list of SIZEBOX entities to be inserted in object's member "volume_finder". Preexisting entities will be discarded.

		"""


	def remove_volume_finder(size_boxes):

		"""


		@size_boxes object: A list of SIZEBOX entities to be removed from object's member "volume_finder".

		"""


	def clear_volume_finder():

		"""

		Remove all entities from object's member "volume_finder".


		"""


	def get_move_types():

		"""


		@returns object: A list with the entities in object's member "move_types". See "move_types" member for information about the entities types.

		"""


	def add_translate(transl_obj):

		"""

		Add a morph.DFMTranslate object or create a new one. If no argument is given, a new instance of morph.DFMTranslate will be created. 


		@transl_obj object: (optional)An instance of morph.DFMTranslate class.

		@returns object: The created or added morph.DFMTranslate object.

		"""


	def add_rotate(rotate_obj):

		"""

		Add a morph.DFMRotate object or create a new one. If no argument is given, a new instance of morph.DFMRotate will be created. 


		@rotate_obj object: (optional)An instance of morph.DFMRotate class.

		@returns object: The created or added morph.DFMRotate object.

		"""


	def add_scale(scale_obj):

		"""

		Add a morph.DFMScale object or create a new one. If no argument is given, a new instance of morph.DFMScale will be created. 


		@scale_obj object: (optional)An instance of morph.DFMScale class.

		@returns object: The created or added morph.DFMScale object.

		"""


	def add_transform(transform_obj):

		"""

		Add a morph.DFMTransform object or create a new one. If no argument is given, a new instance of morph.DFMTransform will be created. 


		@transform_obj object: (optional)An instance of morph.DFMTransform class.

		@returns object: The created or added morph.DFMTransform object.

		"""


	def add_fit_edges(fit_edges_obj):

		"""

		Add a morph.DFMFitEdges object or create a new one. If no argument is given, a new instance of morph.DFMFitEdges will be created. 


		@fit_edges_obj object: (optional)An instance of morph.DFMFitEdges class.

		@returns object: The created or added morph.DFMFitEdges class.

		"""


	def add_fit_surfs(fit_surfs_obj):

		"""

		Add a morph.DFMFitSurfaces object or create a new one. If no argument is given, a new instance of morph.DFMFitSurfaces will be created. 


		@fit_surfs_obj object: (optional)An instance of morph.DFMFitSurfaces class.

		@returns object: The created or added morph.DFMFitSurfaces object.

		"""


	def add_align(align_obj):

		"""

		Add a morph.DFMAlign object or create a new one. If no argument is given, a new instance of morph.DFMAlign will be created. 


		@align_obj object: (optional)An instance of morph.DFMAlign class.

		@returns object: The created or added morph.DFMAlign object.

		"""


	def add_sweep_glide(sweep_glide_obj):

		"""

		Add a morph.DFMSweepGlide object or create a new one. If no argument is given, a new instance of morph.DFMSweepGlide will be created. 


		@sweep_glide_obj object: (optional)An instance of morph.DFMSweepGlide class.

		@returns object: The created or added morph.DFMSweepGlide object.

		"""


	def save_as_param(name):

		"""


		@name string: (optional)The name of the parameter to create.

		@returns object: A morph parameter entity (PARAMETERS).

		"""


	def save_as_DVGrids():

		"""


		"""


	def insert_constraints(constraints):

		"""


		@constraints object: A list of MORPH_CONSTRAINT entities to be included in object's member "constraints".

		"""


	def set_constraints(constraints):

		"""


		@constraints object: A list of MORPH_CONSTRAINT entities to be included in object's member "constraints". Preexisting entities will be discarded.

		"""


	def remove_constraints(constraints):

		"""


		@constraints object: A list of MORPH_CONSTRAINT entities to be excluded from object's member "constraints".

		"""


	def clear_constraints():

		"""

		Remove all entities from object's member "constraints".


		"""


	def set_performance(performance_option):

		"""


		@performance_option string: 'Fast' or 'Accurate'

		"""


	def set_tangency(tangency_option):

		"""


		@tangency_option string: 'Default' or 'Smooth'

		"""


	def create_symmetric():

		"""

		Create a symmetric DFM parameter relative to the default symmetry plane. The current morph.DFM object doesn't have to be saved as DFM Parameter. 


		@returns object: The created PARAMETERS entity or None if symmetry failed.

		"""


	def remove_move_type(move_type):

		"""

		Remove an entity from object's member "move_types". 


		@move_type object: An instance of one of the classes mentioned in object's member "move_types".

		"""


	def __init__(dfm_parameter):

		"""

		Constructor of class DFM. 


		@dfm_parameter object: (optional)An entity PARAMETERS of DFM type.

		"""


	def add_constraint_obj(constraint_obj):

		"""

		Add an instance of morph.Constraint*** classes. This is an alternative way to insert constraints rather than inserting through "insert_constraints" and "set_constraints" methods which require to insert only ANSA entities. The corresponding MORPH_CONSTRAINT entity is inserted in member "constraints".  


		@constraint_obj object: (optional)An instance of one of the classes: morph.ConstraintRigid, morph.ConstraintPlanar, morph.ConstraintPathFollower, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintFlanges).

		"""


	def set_improve_mesh(type, zones):

		"""

		Define the mesh improvement action that shall take place after the main morphing action. 


		@type string: Options: 
		'None'
		'Reconstruct'
		'Smooth'
		'Reshape'

		@zones integer: (optional)Number of zones of entities around main morphing area to be included in mesh improvement action.

		"""


	def preview():

		"""

		Preview the result of the morphing action. WARNING: Unless method "apply" is called, the morphing action will be finally cancelled in the end of the python script. 


		"""


	def disable_preview():

		"""

		Disable the preview of the morphing action. 


		"""


	def apply():

		"""

		Perform the morphing action and confirm it. After the call to "apply" method, the morphing is permanent and the object is able to perform another morphing with another arbitrary configuration. WARNING: Unless a call to this method, the morphing action will be cancelled at the end of the Python script. 


		"""

class Form:

	"""

	Form - a class to define bending, twisting, tapering and extending of FE or Geometry entities, while preserving the cross-section.

	"""


	formed = None
	"""
	A list of entities to be forme.

	"""

	transition = None
	"""
	A list of entities to be morphed.

	"""

	fixed = None
	"""
	A list of entities to stay fixed and bound the transition.

	"""

	constraints = None
	"""
	A list of MORPH_CONSTRAINT entities participating in the movement.

	"""

	volume_finder = None
	"""
	A list of SIZEBOX entities used as volume finders aiding the selection of entities.

	"""

	coordinate = None
	"""
	Coordinate entity defining center and direction of bending, twisting, tapering and extending. By default it is placed at formed entities CoG and aligned in to formed entities principal axes. Neutral axis is along the largest dimension and Bending axis along the second largest dimension.

	"""

	positive_plane_length = None
	"""
	Definition of positive plane's distance from coordinate system, across neutral axis.

	"""

	negative_plane_length = None
	"""
	Definition of negative plane's distance from coordinate system, across neutral axis.

	"""

	positive_plane_angle = None
	"""
	Definition of the angle formed among positive plane's initial position, coordinate center and positive plane's final position.

	"""

	negative_plane_angle = None
	"""
	Definition of the angle formed among negative plane's initial position, coordinate center and negative plane's final position.

	"""

	def insert_formed(formed):

		"""


		@formed object: A list of entities to be inserted in object's member "formed".

		"""


	def set_formed(formed):

		"""


		@formed object: A list of entities to be inserted in object's member "formed". Preexisting entities will be discarded.

		"""


	def remove_formed(formed):

		"""


		@formed object: A list of entites to be removed from object's member "formed".

		"""


	def clear_formed():

		"""

		Remove all entities from object's member "formed".


		"""


	def increase_formed_zone(zones):

		"""


		@zones integer: Number of zones around formed entities to be included also in object's member "formed".

		"""


	def decrease_formed_zone(zones):

		"""


		@zones integer: Number of zones around formed entities to be excluded from object's member "formed".

		"""


	def insert_transition(transition):

		"""


		@transition object: A list of entities to be inserted in object's member "transition".

		"""


	def set_transition(transition):

		"""


		@transition object: A list of entities to be inserted in object's member "transition". Preexisting entities will be discarded.

		"""


	def remove_transition(transition):

		"""


		@transition object: A list of entites to be removed from object's member "transition".

		"""


	def clear_transition():

		"""

		Remove all entities from object's member "transition".


		"""


	def increaze_transition_zone(zones):

		"""


		@zones integer: Number of zones around transition and formed entities to be included also in object's member "transition".

		"""


	def decrease_transition_zone(zones):

		"""


		@zones integer: Number of zones aroud transition entities to be excluded from object's member "transition".

		"""


	def insert_fixed(fixed):

		"""


		@fixed object: A list of entities to be inserted in object's member "fixed".

		"""


	def set_fixed(fixed):

		"""


		@fixed object: A list of entities to be inserted in object's member "fixed". Preexisting entities will be discarded.

		"""


	def remove_fixed(fixed):

		"""


		@fixed object: A list of entities to be removed from object's member "fixed".

		"""


	def clear_fixed():

		"""

		Remove all entities from object's member "fixed".


		"""


	def calculate_fixed():

		"""

		Automatic calculation of fixed. The result will be inserted to object's member "fixed".


		"""


	def insert_constraints(constraints):

		"""


		@constraints object: A list of MORPH_CONSTRAINT entities to be included in object's member "constraints".

		"""


	def set_constraints(constraints):

		"""


		@constraints object: A list of MORPH_CONSTRAINT entities to be included in object's member "constraints". Preexisting entities will be discarded.

		"""


	def remove_constraints(constraints):

		"""


		@constraints object: A list of MORPH_CONSTRAINT entities to be excluded from object's member "constraints".

		"""


	def clear_constraints():

		"""

		Remove all entities from object's member "constraints".


		"""


	def insert_volume_finder(size_boxes):

		"""


		@size_boxes object: A list of SIZEBOX entities to be inserted in object's member "volume_finder".

		"""


	def set_volume_finder(size_boxes):

		"""


		@size_boxes object: A list of SIZEBOX entities to be inserted in object's member "volume_finder". Preexisting entities will be discarded.

		"""


	def remove_volume_finder(size_boxes):

		"""


		@size_boxes object: A list of SIZEBOX entities to be removed from object's member "volume_finder".

		"""


	def clear_volume_finder():

		"""

		Remove all entities from object's member "volume_finder".


		"""


	def set_coordinate(coordinate):

		"""

		Set a new entity for coordinate system. Neutral axis will be represented by X axis and Bending axis by Y.


		@coordinate object: A coordinate entity.

		"""


	def move_coordinate_to_cog():

		"""

		Move coordinate origin to the center of gravity of formed entities.


		"""


	def align_to_principal_axes():

		"""

		Align the coordinate axes to the principal axes of formed entities.


		"""


	def set_positive_plane_length(length):

		"""


		@length float: Numerical value to set the distance among positive plane and coordinate system, across neutral axis.

		"""


	def set_positive_plane_angle(angle):

		"""


		@angle float: Numerical value to define the angle formed among positive plane's initial position, coordinate center and positive plane's final position.

		"""


	def set_negative_plane_length(length):

		"""


		@length float: Numerical value to set the distance among negative plane and coordinate system, across neutral axis.

		"""


	def set_negative_plane_angle(angle):

		"""


		@angle float: Numerical value to define the angle formed among negative plane's initial position, coordinate center and negative plane's final position.

		"""


	def reset_positive_plane_length():

		"""

		Reset object's member "positive_plane_length" to the maximum value.


		"""


	def reset_negative_plane_length():

		"""

		Reset object's member "negative_plane_length" to the maximum value.


		"""


	def set_link_planes(link_planes):

		"""

		Enable planes linkage to bend, twist, taper and extend identically in both ends. Positive plane's bend length and angle, twist angle, taper and extend ratios will be used as reference. 


		@link_planes boolean: Input True to link planes movement. Input False to disable linking feature.

		"""


	def set_improve_mesh(type, expand_zones):

		"""

		Set mesh improvement to be applied after move and accept.


		@type string: Type of mesh improvement. Only 'None', 'Reconstruct', 'Smooth', 'Reshape' inputs are acceptable.

		@expand_zones integer: Numerical input for the number of expanded zones to be included in mesh improvement.

		"""


	def preview():

		"""

		Preview the result of the morphing action. WARNING: Unless method "apply" is called, the morphing action will be finally cancelled in the end of the python script. 


		"""


	def disable_preview():

		"""

		Disable the preview of the morphing action.


		"""


	def apply():

		"""

		Perform the morphing action and confirm it. After the call to "apply" method, the morphing is permanent and the object is able to perform another morphing with another arbitrary configuration. WARNING: Unless a call to this method, the morphing action will be cancelled at the end of the Python script. 


		"""


	def create_symmetric():

		"""

		Create a symmetric DIRECT_FORM entity relative to the default symmetry plane. The current morph.Bend object doesn't have to be saved as DIRECT_FORM entity. 


		@returns object: The created MD_MOVE_BEND entity or None if symmetry failed.

		"""


	def save_as_Direct_Form(name):

		"""


		@name string: (optional)The name of the entity to create.

		"""


	def set_positive_plane_twist(angle):

		"""


		@angle float: Numerical value to set the twisting angle of positive plane cross-section orientation, across neutral axis.

		"""


	def set_negative_plane_twist(angle):

		"""


		@angle float: Numerical value to set the twisting angle of negative plane cross-section orientation, across neutral axis.

		"""


	def set_positive_plane_stretch(s_ratio):

		"""


		@s_ratio float: Numerical value to set the stretching ratio of positive plane's side.

		"""


	def set_negative_plane_stretch(s_ratio):

		"""


		@s_ratio float: Numerical value to set the stretching ratio of negative plane's side.

		"""


	def set_negative_plane_y_taper(y_ratio):

		"""


		@y_ratio float: Numerical value to set the y-tapering ratio of negative plane's side.

		"""


	def set_positive_plane_y_taper(y_ratio):

		"""


		@y_ratio float: Numerical value to set the y-tapering ratio of positive plane's side.

		"""


	def set_positive_plane_z_taper(z_ratio):

		"""


		@z_ratio float: Numerical value to set the z-tapering ratio of positive plane's side.

		"""


	def set_negative_plane_z_taper(z_ratio):

		"""


		@z_ratio float: Numerical value to set the z-tapering ratio of negative plane's side.

		"""

class DCFeatureSlide:

	"""

	A class defining methods for sliding a feature (bead, stamp, rib, hole) consisting of finite elements. 

	"""


	feature_area = None
	"""
	A list of entities that represent the features to be morphed. The type of these entities can be SHELL, SHELLEDGE or a type of FEATURE group (HOLE 2D, HOLE 3D, RIB 2D, STAMP).

	"""

	surface_area = None
	"""
	A list of SHELL entities that represent the surface on which the feature entities will slide.

	"""

	path = None
	"""
	A list of entities (SHELLEDGE, CURVE) that define a path for feature entities to slide on.

	"""

	movement_type = None
	"""
	A string that defines the movement type of slide. It can be one of the following strings: 
	'Free': A free movement according to a local Cartesian coordinate system established in the COG of the feature entities. 
	'OnSurface': Feature entities shall slide only on the underlying surface. Movement is defined by a local two-dimensional coordinate system corresponding to the surface's isoparametric directions. 
	'FollowPath' : Feature entities shall slide only on a defined path.

	"""

	movement_on_path = None
	"""
	A string that defines if the movement on path will be of type 'Sweep' or 'Glide'.

	"""

	def set_feature_area(feature_area_entities):

		"""


		@feature_area_entities object: A list of entities to be inserted in object's member "feature_area". Preexisting entities will be discarded.

		"""


	def insert_feature_area(feature_area_entities):

		"""


		@feature_area_entities object: A list of entities to be inserted in object's member "feature_area".

		"""


	def remove_feature_area(feature_area_entities):

		"""


		@feature_area_entities object: A list of entities to be removed from object's member "feature_area".

		"""


	def clear_feature_area():

		"""

		Remove all entities from object's member "feature_area". 


		"""


	def set_surface_area(surface_area_entities):

		"""


		@surface_area_entities object: A list of entities to be inserted in object's member "surface_area". Preexisting entities will be discarded.

		"""


	def insert_surface_area(surface_area_entities):

		"""


		@surface_area_entities object: A list of entities to be inserted in object's member "surface_area".

		"""


	def remove_surface_area(surface_area_entities):

		"""


		@surface_area_entities object: A list of entities to be removed from object's member "surface_area".

		"""


	def clear_surface_area():

		"""

		Remove all entities from object's member "surface_area". 


		"""


	def set_path(path_entities):

		"""


		@path_entities object: A list of entities to be inserted in object's member "path". Preexisting entities will be discarded.

		"""


	def insert_path(path_entities):

		"""


		@path_entities object: A list of entities to be inserted in object's member "path".

		"""


	def remove_path(path_entities):

		"""


		@path_entities object: A list of entities to be removed from object's member "path".

		"""


	def clear_path():

		"""

		Remove all entities from object's member "path". 


		"""


	def set_movement_type_free():

		"""

		Set object's member "movement_type" to "Free". 


		"""


	def set_movement_type_on_surface():

		"""

		Set object's member "movement_type" to "OnSurface". 


		"""


	def set_movement_type_follow_path():

		"""

		Set object's member "movement_type" to "FollowPath". 


		"""


	def set_movement_on_path(type):

		"""

		Define the type of movement on path. 


		@type string: 'Sweep' or 'Glide'.

		"""


	def save_as_DC_Feature():

		"""

		Save the current DC Slide Feature configuration as a "DC_FEATURE_SLIDE" entity in ANSA database. The saved entity is returned by this method. 


		@returns object: The created "DC_FEATURE_SLIDE" entity.

		"""


	def set_translation_vector(dx_or_ds, dy_or_dt, dz):

		"""

		Define the translation vector for a 'Free' or 'OnSurface' translation of feature entities. 


		@dx_or_ds float: The 'dx' component of translation corresponding to local X axis for a 'Free' movement type or the 'ds' component of translation corresponding to local S axis (first isoparametric direction of the surface) for an 'OnSurface' movement type.

		@dy_or_dt float: The 'dy' component of translation corresponding to local Y axis for a 'Free' movement type or the 'dt' component of translation corresponding to local T axis (second isoparametric direction of the surface) for an 'OnSurface' movement type.

		@dz float: (optional)The 'dz' component of translation corresponding to local Z axis, required only for a 'Free' movement type.

		"""


	def set_rotation_angles(rx_or_r, ry, rz):

		"""

		Define the rotation angles for a 'Free' or 'OnSurface' rotation of feature entities. 


		@rx_or_r float: The 'rx' component of a rotation angles vector corresponding to local X axis for a 'Free' movement type or the angle 'r' of the rotation around the normal axis to the surface for an 'OnSurface' movement type.

		@ry float: (optional)The 'ry' component of a rotation angles vector corresponding to local Y axis only for a 'Free' movement type.

		@rz float: (optional)The 'rz' component of a rotation angles vector corresponding to local Z axis only for a 'Free' movement type.

		"""


	def set_scale_factors(fx_or_fs, fy_or_ft, fz):

		"""

		Define the scale factors for a 'Free' or 'OnSurface' scaling of feature entities. 


		@fx_or_fs float: The 'fx' component of scale factors' vector corresponding to local X axis for a 'Free' movement type or the 'fs' component of scale factors' vector corresponding to local S axis (first isoparametric direction of the surface) for an 'OnSurface' movement type.

		@fy_or_ft float: The 'fy' component of scale factors' vector corresponding to local Y axis for a 'Free' movement type or the 'ft' component of scale factors' vector corresponding to local T axis (second isoparametric direction of the surface) for an 'OnSurface' movement type.

		@fz float: (optional)The 'fz' component of scale factors' vector corresponding to local Z axis only for a 'Free' movement type.

		"""


	def set_distance_on_path(distance):

		"""

		Define the distance that feature entities should slide along the defined path for a 'FollowPath' movement type. 


		@distance float: The distance that feature entities should slide along the defined path.

		"""


	def set_frozen_perimeters(perimeters_entities):

		"""


		@perimeters_entities object: A list of one-dimensional entities (SHELLEDGE) to be regarded as 'frozen' during the morphing.

		"""


	def clear_frozen_perimeters():

		"""

		Cancel the marking of any perimeters (SHELLEDGE) as 'Frozen'. 


		"""


	def set_improve_mesh(type, zones):

		"""

		Define the mesh improvement action to be applied after the sliding of feature entities. 


		@type string: Mesh improvement action options: 'None', 'Reconstruct', 'Smooth', 'Reshape'

		@zones integer: (optional)Number of zones around feature entities to be included in the mesh improvement action. Default: 0

		"""


	def snap_to_feature_lines(active):

		"""


		@active boolean: If 'True', feature entities will snap to feature lines during morphing.

		"""


	def set_projection_direction(type):

		"""

		Define the type of projection direction. 


		@type string: For movement types 'Free' or 'FollowPath' the projection direction options are: 
		- 'Free'
		- 'X_Axis'
		- 'Y_Axis'
		- 'Z_Axis'
		For movement type 'OnSurface' the projection direction options are:
		- 'Free'
		- 'Normal'

		"""


	def set_projection_distance(distance):

		"""


		@distance float: Maximum projection distance.

		"""


	def set_projection_distance_active(active):

		"""


		@active boolean: If 'True', morphing will respect the maximum projection distance and direction.

		"""


	def apply():

		"""

		Perform the morphing action (sliding of the feature entities). Mesh improvement actions defined by method 'set_improve_mesh' will be applied also after the call to this method. 


		"""


	def __init__(dc_feature_slide):

		"""

		Constructor of class DCFeatureSlide. 


		@dc_feature_slide object: (optional)Use this argument to construct an instance of DCFeatureSlide class from an existing "DC_FEATURE_SLIDE" entity.

		"""


	def set_coord(coord):

		"""

		Define the local coordinate system according to which feature entities will be transformed (translations, rotations, scalings). The method is valid only for 'free' movement type. 


		@coord object: A "COORD" type entity.

		"""


	def set_s_axis(ds1, ds2, ds3):

		"""

		Propose an S axis to define the local coordinate system according to which the feature entities will be transformed. Based on this proposal, a local coordinate system S-T-W will be configured, where W is always the normal to the surface and S will be the best match to the proposed axis. This method is valid only for 'on surface' movement type. 


		@ds1 float: x-component of proposed S axis.

		@ds2 float: y-component of proposed S axis.

		@ds3 float: z-component of proposed S axis.

		"""


	def create_symmetric():

		"""

		Create a DC_FEATURE_SLIDE entity which is symmetric to the object's one according to the default symmetry plane.


		@returns object: The created "DC_FEATURE_SLIDE" entity or None if symmetry operation failed.

		"""

class DCFeatureCopy:

	"""

	A class defining methods for copying a feature (bead, stamp, rib, hole) consisting of finite elements, in other positions on the mesh. 
	
	Most of the members and the methods of this class are exactly the same with that of DCFeatureSlide class. The essential difference between these two classes, is that in DCFeatureSlide class, feature entities are really sliding on a surface or on a path while in the present class, DCFeatureCopy, the pattern of the selected feature entities is copied to other positions in the FE mesh. Therefore, the term "slide" in the subsequent description does not imply an actual sliding of the feature entities but the route in which this pattern will follow in order to be copied in new position. The parent pattern can be copied an arbitrary number of times in the FE mesh and this additional option is the attribute "steps" of the present class. 

	"""


	feature_area = None
	"""
	A list of entities that represent the features to be morphed. The type of these entities can be SHELL, SHELLEDGE or a type of FEATURE group (HOLE 2D, HOLE 3D, RIB 2D, STAMP).

	"""

	surface_area = None
	"""
	A list of SHELL entities that represent the surface on which the feature entities will slide.

	"""

	path = None
	"""
	A list of entities (SHELLEDGE, CURVE) that define a path for feature entities to slide on.

	"""

	movement_type = None
	"""
	A string that defines the movement type of slide. It can be one of the following strings: 
	'Free': A free movement according to a local Cartesian coordinate system established in the COG of the feature entities. 
	'OnSurface': Feature entities shall slide only on the underlying surface. Movement is defined by a local two-dimensional coordinate system corresponding to the surface's isoparametric directions. 
	'FollowPath' : Feature entities shall slide only on a defined path.

	"""

	movement_on_path = None
	"""
	A string that defines if the movement on path will be of type 'Sweep' or 'Glide'.

	"""

	steps = None
	"""
	Number of copies to be created from the parent pattern i.e. the entities in "feature_area" member.

	"""

	def set_feature_area(feature_area_entities):

		"""


		@feature_area_entities object: A list of entities to be inserted in object's member "feature_area". Preexisting entities will be discarded.

		"""


	def insert_feature_area(feature_area_entities):

		"""


		@feature_area_entities object: A list of entities to be inserted in object's member "feature_area".

		"""


	def remove_feature_area(feature_area_entities):

		"""


		@feature_area_entities object: A list of entities to be removed from object's member "feature_area".

		"""


	def clear_feature_area():

		"""

		Remove all entities from object's member "feature_area". 


		"""


	def set_surface_area(surface_area_entities):

		"""


		@surface_area_entities object: A list of entities to be inserted in object's member "surface_area". Preexisting entities will be discarded.

		"""


	def insert_surface_area(surface_area_entities):

		"""


		@surface_area_entities object: A list of entities to be inserted in object's member "surface_area".

		"""


	def remove_surface_area(surface_area_entities):

		"""


		@surface_area_entities object: A list of entities to be removed from object's member "surface_area".

		"""


	def clear_surface_area():

		"""

		Remove all entities from object's member "surface_area". 


		"""


	def set_path(path_entities):

		"""


		@path_entities object: A list of entities to be inserted in object's member "path". Preexisting entities will be discarded.

		"""


	def insert_path(path_entities):

		"""


		@path_entities object: A list of entities to be inserted in object's member "path".

		"""


	def remove_path(path_entities):

		"""


		@path_entities object: A list of entities to be removed from object's member "path".

		"""


	def clear_path():

		"""

		Remove all entities from object's member "path". 


		"""


	def set_movement_type_free():

		"""

		Set object's member "movement_type" to "Free". 


		"""


	def set_movement_type_on_surface():

		"""

		Set object's member "movement_type" to "OnSurface". 


		"""


	def set_movement_type_follow_path():

		"""

		Set object's member "movement_type" to "FollowPath". 


		"""


	def set_movement_on_path(type):

		"""

		Define the type of movement on path. 


		@type string: 'Sweep' or 'Glide'.

		"""


	def save_as_DC_Feature():

		"""

		Save the current DC Slide Feature configuration as a "DC_FEATURE_COPY" entity in ANSA database. The saved entity is returned by this method. 


		"""


	def set_translation_vector(dx_or_ds, dy_or_dt, dz):

		"""

		Define the translation vector for a 'Free' or 'OnSurface' translation of feature entities. 


		@dx_or_ds float: The 'dx' component of translation corresponding to local X axis for a 'Free' movement type or the 'ds' component of translation corresponding to local S axis (first isoparametric direction of the surface) for an 'OnSurface' movement type.

		@dy_or_dt float: The 'dy' component of translation corresponding to local Y axis for a 'Free' movement type or the 'dt' component of translation corresponding to local T axis (second isoparametric direction of the surface) for an 'OnSurface' movement type.

		@dz float: (optional)The 'dz' component of translation corresponding to local Z axis, required only for a 'Free' movement type.

		"""


	def set_rotation_angles(rx_or_r, ry, rz):

		"""

		Define the rotation angles for a 'Free' or 'OnSurface' rotation of feature entities. 


		@rx_or_r float: The 'rx' component of a rotation angles vector corresponding to local X axis for a 'Free' movement type or the angle 'r' of the rotation around the normal axis to the surface for an 'OnSurface' movement type.

		@ry float: (optional)The 'ry' component of a rotation angles vector corresponding to local Y axis only for a 'Free' movement type.

		@rz float: (optional)The 'rz' component of a rotation angles vector corresponding to local Z axis only for a 'Free' movement type.

		"""


	def set_scale_factors(fx_or_fs, fy_or_ft, fz):

		"""

		Define the scale factors for a 'Free' or 'OnSurface' scaling of feature entities. 


		@fx_or_fs float: The 'fx' component of scale factors' vector corresponding to local X axis for a 'Free' movement type or the 'fs' component of scale factors' vector corresponding to local S axis (first isoparametric direction of the surface) for an 'OnSurface' movement type.

		@fy_or_ft float: The 'fy' component of scale factors' vector corresponding to local Y axis for a 'Free' movement type or the 'ft' component of scale factors' vector corresponding to local T axis (second isoparametric direction of the surface) for an 'OnSurface' movement type.

		@fz float: (optional)The 'fz' component of scale factors' vector corresponding to local Z axis only for a 'Free' movement type.

		"""


	def set_distance_on_path(distance):

		"""

		Define the distance that feature entities should slide along the defined path for a 'FollowPath' movement type. 


		@distance float: The distance that feature entities should slide along the defined path.

		"""


	def set_frozen_perimeters(perimeters_entities):

		"""


		@perimeters_entities object: A list of one-dimensional entities (SHELLEDGE) to be regarded as 'frozen' during the morphing.

		"""


	def clear_frozen_perimeters():

		"""

		Cancel the marking of any perimeters (SHELLEDGE) as 'Frozen'. 


		"""


	def set_improve_mesh(type, zones):

		"""

		Define the mesh improvement action to be applied after the sliding of feature entities. 


		@type string: Mesh improvement action options: 'None', 'Reconstruct', 'Smooth', 'Reshape'

		@zones integer: Number of zones around feature entities to be included in the mesh improvement action. Default: 0

		"""


	def snap_to_feature_lines(active):

		"""


		@active boolean: If 'True', feature entities will snap to feature lines during morphing.

		"""


	def set_projection_direction(type):

		"""

		Define the type of projection direction. 


		@type constant: For movement types 'Free' or 'FollowPath' the projection direction options are: 
		- 'Free'
		- 'X_Axis'
		- 'Y_Axis'
		- 'Z_Axis'
		For movement type 'OnSurface' the projection direction options are:
		- 'Free'
		- 'Normal'

		"""


	def set_projection_distance(distance):

		"""


		@distance integer: Maximum projection distance.

		"""


	def set_projection_distance_active(active):

		"""


		@active boolean: If 'True', morphing will respect the maximum projection distance and direction.

		"""


	def apply():

		"""

		Perform the morphing action (copying of the feature entities). Mesh improvement actions defined by method 'set_improve_mesh' will be applied also after the call to this method. 


		"""


	def set_steps(num_steps):

		"""


		@num_steps integer: Sets the value "num_steps" in object's member "steps".

		"""


	def __init__(dc_feature_copy):

		"""

		The constructor of class DCFeatureCopy. 


		@dc_feature_copy object: (optional)Use this argument to construct an instance of DCFeatureCopy class from an existing "DC_FEATURE_COPY" entity.

		"""


	def set_coord(coord):

		"""

		Define the local coordinate system according to which feature entities will be transformed (translations, rotations, scalings). The method is valid only for 'free' movement type. 


		@coord object: A "COORD" type entity.

		"""


	def set_s_axis(ds1, ds2, ds3):

		"""

		Propose an S axis to define the local coordinate system according to which the feature entities will be transformed. Based on this proposal, a local coordinate system S-T-W will be configured, where W is always the normal to the surface and S will be the best match to the proposed axis. This method is valid only for 'on surface' movement type. 


		@ds1 float: x-component of proposed S axis.

		@ds2 float: y-component of proposed S axis.

		@ds3 float: z-component of proposed S axis.

		"""


	def create_symmetric():

		"""

		Create a DC_FEATURE_COPY entity which is symmetric to the object's one according to the default symmetry plane.


		@returns object: The created "DC_FEATURE_COPY" entity or None if symmetry operation failed.

		"""

class ChangeHoleDiameter:

	"""

	A class providing methods for changes in the diameter of ANSA hole entities. 

	"""


	def __init__(hole_2d_feature):

		"""

		Constructor of class ChangeHoleDiameter. 


		@hole_2d_feature object: A "HOLE 2D" entity.

		"""


	def set_offset(offset_value):

		"""

		Define the change in hole's diameter to be perfomed via offset of the hole's boundary edges. 


		@offset_value float: The value of the offset of hole's boundary edges.

		"""


	def set_radial_offset(radial_offset_value):

		"""

		Define the change in hole's diameter to be perfomed via radial offset of the hole's boundary edges. 


		@radial_offset_value float: The value of the radial offset of hole's boundary edges.

		"""


	def set_target_diameter(diameter):

		"""

		Define the absolute value of hole's diameter to be set. 


		@diameter float: The target value of hole's diameter.

		"""


	def move_on_middle_plane():

		"""

		Set the morphing of the hole to be perfomed by movements in the middle plane of the hole. 


		"""


	def move_on_surface():

		"""

		Set the morphing of the hole to be performed by movements on hole's surface. 


		"""


	def preview():

		"""

		Preview the result of the morphing action. WARNING: Unless method "apply" is not called afterwards, morphing action will be canceled in the end of the script. 


		"""


	def disable_preview():

		"""

		Disable the preview of the morphing action's result. 


		"""


	def apply():

		"""

		Perform and confirm the morphing action. Unless this method has been called, the morphing action of the object will be canceled in the end of the script. 


		"""

class ConstraintSteadySection:

	"""

	Class providing methods to define a constraint of type 'Steady Section' to be included in a direct morphing action. The entities belonging to such a constraint shall retain their cross section along a neutral line during the morphing action. Class can be used either to create a MORPH_CONSTRAINT entity of 'Steady Section' type or to modify an existing one. 

	"""


	morphed = None
	"""
	A list of entities to be in the transition zone.

	"""

	bounds = None
	"""
	A list of entities set as fixed perimeters.

	"""

	entities = None
	"""
	A list of entities constrained to preserve their cross section shape.

	"""

	neutral_line_entities = None
	"""
	A list of entities to describe a neutral line across which the cross section shall be preserved.

	"""

	def insert_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed".

		"""


	def set_morphed(morphed):

		"""


		@morphed object: A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

		"""


	def remove_morphed(morphed):

		"""


		@morphed object: A list of entities to be removed from object's member "morphed".

		"""


	def clear_morphed():

		"""

		 Remove all entities from object's member "morphed". 


		"""


	def insert_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds".

		"""


	def set_bounds(bounds):

		"""


		@bounds object: A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

		"""


	def remove_bounds(bounds):

		"""


		@bounds object: A list of entities to be removed from object's member "bounds".

		"""


	def clear_bounds():

		"""

		 Remove all entities from object's member "bounds". 


		"""


	def calculate_bounds():

		"""

		Automatic calculation of bounds. The result will be inserted to object's member "bounds". 


		"""


	def increase_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be included also in object's member "morphed".

		"""


	def decrease_morphed_zone(zones):

		"""


		@zones integer: Number of zones around morphed entities to be excluded from object's member "morphed".

		"""


	def insert_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities".

		"""


	def set_entities(entities):

		"""


		@entities object: A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

		"""


	def remove_entities(entities):

		"""


		@entities object: A list of entities to be excluded from object's member "entities".

		"""


	def clear_entities():

		"""

		Remove all entities from object's member "entities". 


		"""


	def __init__(steady_section_constraint):

		"""

		Constructor of class ConstraintSteadySection.


		@steady_section_constraint object: (optional)MORPH_CONSTRAINT entity of Steady Section type.

		"""


	def reg():

		"""

		Create the MORPH_CONSTRAINT entity from a ConstraintScaled object and register it in the database.  


		"""


	def insert_neutral_line(neutral_line_entities):

		"""


		@neutral_line_entities object: A list of entities to be inserted in object's member "neutral_line_entities"

		"""


	def set_neutral_line(neutral_line_entities):

		"""


		@neutral_line_entities object: A list of entities to be inserted in object's member "neutral_line_entities". Preexisting entities will be discarded.

		"""


	def remove_neutral_line(neutral_line_entities):

		"""


		@neutral_line_entities object: A list of entities to be removed from object's member "neutral_line_entities".

		"""


	def clear_neutral_line():

		"""

		Remove all entities from object's member "neutral_line_entities". 


		"""

class TubesDepenetrate:

	"""

	 Class that facilitates the automatic fix of penetrations between tubes FE and their surroundings.

	"""


	tubes_series_separation_angle = None
	"""
	Angle (in degrees, between 0 and 90) based on which tubes series can be separated. Default: 75.

	"""

	solution_method = None
	"""
	Penetrations' fix method: 'transform', 'transform_and_resize'.  Default: 'transform'

	"""

	factor_distance = None
	"""
	Penetration parametric option. Default: 1.

	"""

	check_same_pids = None
	"""
	Penetration parametric option. Default: FalseMembers

	"""

	allow_planar_self_proximities = None
	"""
	Penetration parametric option. Default: False

	"""

	round_shell_edges = None
	"""
	Penetration parametric option. Default: True

	"""

	edge_to_edge = None
	"""
	Penetration parametric option: 'check_single_edges', 'check_all_edges', 'check_no_edges'. Default: 'check_single_edges'

	"""

	quad_projection = None
	"""
	Penetration parametric option: 'preserve', 'split_to_2_trias', 'split_to_4_trias'. Default: 'preserve'

	"""

	thickness_definition = None
	"""
	Penetration parametric option: 'segment_thickness', 'nodal_thickness', 'user_thickness'. Default: 'segment_thickness'

	"""

	calculate_nodes_thickness_from = None
	"""
	Penetration parametric option: 'model', 'all'. Default: 'model'.

	"""

	def load_tubes_properties(properties):

		"""

		Load the PROPERTY entities that represent the tubes.


		@properties object: An iterable of shell or solid PROPERTY entities.

		"""


	def unload_tubes_properties(properties):

		"""

		Unload the tubes PROPERTY entities from object. 


		@properties object: An iterable of shell or solid PROPERTY entities.

		"""


	def clear_tubes_properties():

		"""

		Clear the selection of tubes PROPERTY entities. 


		"""


	def load_surrounding_properties(properties):

		"""

		Load the PROPERTY entities that represent the surrounding entities which should not penetrate with tubes.In case no surrounding properties are loaded when method ".run()" is called, all the model shell properties except for the ones already included in tubes properties, shall be loaded as surrounding properties. 


		@properties object: An iterable of shell PROPERTY entities.

		"""


	def unload_surrounding_properties(properties):

		"""

		Unload the surrounding PROPERTY entities from object.


		@properties object: An iterable of shell PROPERTY entities.

		"""


	def clear_surrounding_properties():

		"""

		Clear the selection of surrounding PROPERTY entities.


		"""


	def load_dragged_elements(elements):

		"""

		Load secondary elements (RBE2, RBE3, RBAR, CBUSH, CBEAM etc...) so they are dragged alongside tubes elements during morphing.


		@elements object: An iterable of standard finite elements (excluding shell and solids).

		"""


	def unload_dragged_elements(elements):

		"""

		Unload dragged elements (RBE2, RBE3, RBAR, CBUSH, CBEAM etc...) from object.


		@elements object: An iterable of standard finite elements excluding shells and solids.

		"""


	def clear_dragged_elements():

		"""

		Clear the selection of dragged elements.


		"""


	def load_fixed_grids(grids):

		"""

		Load GRIDs that should stay fixed during morphing.


		@grids object: An iterable of GRID entities.

		"""


	def unload_fixed_grids(grids):

		"""

		Unload fixed GRIDs from object.


		@grids object: An iterable of GRID entities.

		"""


	def clear_fixed_grids():

		"""

		Clear the selection of fixed GRIDs.


		"""


	def validate():

		"""

		Check if the object is valid for run. Use this method, optionally, before calling method ".run()" to assure that penetration fix is able to start. 


		@returns string: Returns 'OK' is object is valid, otherwise error description is returned as string.

		"""


	def run():

		"""

		Run the automatic penetration fix process. This may take a while depending on the complexity of the model. After this method is called, no modifications of object's setup (tubes properties, dragged elements etc.) are allowed. 


		"""


	def cancel():

		"""

		Cancel the morphing action. All GRIDs return to their initial position.


		"""


	def build_morphing_boxes():

		"""

		Build cylindrical morphing boxes out of the tubes.


		@returns object: A list of MORPHBOX entities.

		"""


	def get_penetration_pairs(state):

		"""


		@state string: Desired state of tubes: 'initial', 'transform', 'transform_and_resize'

		@returns object: A list of tuples. Each tuple contains two entities and represents a penetration pair with one entity (shell or solid) belonging to tubes and the other entity (shell) belonging to the surrounding properties.

		"""


	def get_penetration_total_depth(state):

		"""

		Get the total penetration depth of all penetration pairs. 


		@state string: Desired state of tubes: 'initial', 'transform', 'transform_and_resize'.

		@returns float: The total penetration depth as sum of all penetration pairs' depth.

		"""

class ChangeTubeDiameter:

	"""

	A class providing methods for changes in the diameter of ANSA HOLE 3D entities.

	"""


	def __init__(hole_3d_feature):

		"""

		Constructor of class ChangeTubeDiameter. 


		@hole_3d_feature object: A "HOLE 3D" entity.

		"""


	def set_radial_offset(radial_offset_value):

		"""

		Define the change in hole's diameter to be perfomed via radial offset of the tube's entities. 


		@radial_offset_value float: The value of the radial offset of tube's entities

		"""


	def set_target_diameter(diameter):

		"""

		Define the absolute value of tube's diameter to be set. Notice that both diameter 1 and 2 will be set to the same value.


		@diameter float: The target value of tube's diameter

		"""


	def move_on_radius():

		"""

		Set the morphing of the hole perimeters at the top and bottom of the tube to be performed on the radial direction.


		"""


	def move_on_surface():

		"""

		Set the morphing of the hole perimeters at the top and bottom of the tube to be performed by movements on surrounding surface. 


		"""


	def preview():

		"""

		Preview the result of the morphing action. WARNING: Unless method "apply" is not called afterwards, morphing action will be canceled in the end of the script. 


		"""


	def disable_preview():

		"""

		Disable the preview of the morphing action's result. 


		"""


	def apply():

		"""

		Perform and confirm the morphing action. Unless this method has been called, the morphing action of the object will be canceled in the end of the script.


		"""

