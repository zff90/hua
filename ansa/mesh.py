def AlignMeshToMesh(source_part, target_parts):

	"""

	Geometrical function that aligns the entities contained into the source
	container with one of the target containers, based on geometry similarities.
	
	The alignment is performed by doing an 6 DOF motion on the source, in order to
	find a best match on one of the targets.
	 
	As source_part or target_parts, any ANSA entity such as Part, Set or Property can be used.
	 
	The user can abort the procedure by hitting the Break key,


	@source_part object: Any ANSA entity such as Part, Set or Property can be used.

	@target_parts object: Any ANSA entity such as Part, Set or Property can be used.

	@returns object: On success, the functions returns a Dictionary with the following members:
	        "matched_part"          -> the best matched part to our source.
	        "distance"              -> the distance of our source to the best matched part.
	        "transformation_matrix" -> the 4x3 transfomation matrix that aligns the source part to
	                                   the best matched target. 
	On failure, returns None.

	"""

def AspacingCFD(Growth_rate, Feature_angle, Min_length, Max_length, Sharp_angle_limit, Sharp_angle_length):

	"""

	This function can be used to apply automatically curvature dependant Perimeter node spacing
	for CFD applications.


	@Growth_rate float: The growth rate of the mesh.

	@Feature_angle float: The feature angle limit.

	@Min_length float: The minimun length of the mesh.

	@Max_length float: The maximum length of the mesh.

	@Sharp_angle_limit float: The sharp angle limit.

	@Sharp_angle_length float: The sharp angle length.

	@returns: No value is returned.

	"""

def AspacingSTL(chordal_deviation, max_length, feature_angle, min_length):

	"""

	This function can be used to automatically apply curvature dependant Perimeter node spacing
	for STL meshing.


	@chordal_deviation anything: Chordal deviation. Absolute or relative value. It can be defined as a float value or 
	a string, which can optionally contain the percentage symbol to indicate a relative value

	@max_length float: Maximum length.

	@feature_angle float: If 0 is specified then it is not active.

	@min_length float: (optional)Minimum length.

	@returns: No value is returned.

	"""

def AutoMatch(visible, shells, nodes, project_on_geometry, project_2nd_order_nodes, isolate, move_to, preserve_id, distance, name):

	"""

	Function that makes function Grids->Match->AUTO usable via script.


	@visible boolean: (optional)The function will run for every visible element of the model.

	@shells object: (optional)A list of shells.

	@nodes object: (optional)A list of nodes.

	@project_on_geometry boolean: (optional)Nodes will also be projected upon geometry.

	@project_2nd_order_nodes boolean: (optional)Choose whether to project upon geometry the Second order nodes or not.

	@isolate boolean: (optional)Isolate the area where nodes that are going to be matched are found.

	@move_to string: (optional)Choose where the node that derives from the match procedure will be placed.
	Valid values: "average pos", "geometry pos", "FE pos".

	@preserve_id string: (optional)Choose which node id will be set on the node that derives from the match 
	procedure. Valid values: "max" , "min".

	@distance float: (optional)The distance from the primary nodes that will be searched to find 
	matching candidates.

	@name string: (optional)Match nodes with the given name only.

	@returns integer: Returns 1 upon success, 0 on failure.

	"""

def AutoPaste(visible, shells, nodes, project_on_geometry, project_2nd_order_nodes, isolate, move_to, preserve_id, distance, name, allow_element_collapse):

	"""

	Function that makes function Grids->Paste->AUTO usable via script.


	@visible boolean: (optional)The function will run on every visible element of the model.

	@shells object: (optional)A list of shells where the function will be run on.

	@nodes object: (optional)A list of nodes where the function will be run on.

	@project_on_geometry boolean: (optional)If True, the nodes will also be projected on the geometry.

	@project_2nd_order_nodes boolean: (optional)Choose whether to project upon geometry the Second order nodes or not.

	@isolate boolean: (optional)Isolate the area where the nodes that are going to be pasted are found.

	@move_to string: (optional)Choose where the node that derives from the paste procedure will be placed.
	Valid values: "average pos", "geometry pos", "FE pos".

	@preserve_id string: (optional)Choose which node id will be set on the node that derives from the
	paste procedure. Valid values: "max" or "min"

	@distance float: (optional)The distance from the primary nodes to search in order to find the
	paste candidates.

	@name string: (optional)Paste nodes with the given name only.

	@allow_element_collapse boolean: (optional)If True paste will be forced for grids that belong to the same element 
	(this may result in element collapse)

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def CheckShellTheta(shells, prototype_shell, do_fix, tolerance):

	"""

	Function that checks the material orientation of given shells by Theta angle, using a prototype Shell. 
	Although the algorithm uses the given shell as prototype, it tries to maintain a smooth regional orientation.


	@shells object: A list of shells to check material orientation.

	@prototype_shell object: A shell prototype to check orientation by.

	@do_fix boolean: (optional)If True, any shells found with different orientation will be oriented accordingly.
	(Default: False)

	@tolerance float: (optional)The angle tolerance to be used in orientation comparison.

	@returns object: If no disoriented shells are found, the function returns None.
	If there are such shells, the function will return the list containing them.

	"""

def CollapseShells(COLLAPSE_TOLERANCE):

	"""

	Collapses edges of visible elemens according to specified tolerance.


	@COLLAPSE_TOLERANCE float: The collapse tolerance.

	@returns integer: Returns 0 in each case.

	"""

def CompSkin():

	"""

	Find the differences between the skin of visible tetras, pyramids and the skin of visible shells. Then remesh localy the solids to make the skins compatible.


	@returns integer: 1: Success
	0: Failure

	"""

def ConvertToPolyhedrals(solids, feature_angle, exclude_ANSA_layers, ret_ents, result_type, split_layers_at_sharp_convex_features ):

	"""

	This function will convert solid elements into polyhedral and shell elements into polygons. 
	Input solids and attached shells will be erased.


	@solids object: (optional)A list of ansa entities (if not given all solids of the db will be converted).
	These entities may be ansa solids, parts, properties or volumes.

	@feature_angle float: (optional)Feature angle limit to be respected in conversion 
	(if not given default value 20 is set).

	@exclude_ANSA_layers boolean: (optional)Set True to ignore solids that belongs to ANSA layers volume from coversion.

	@ret_ents boolean: (optional)If set to True a list with the created entities will be returned.

	@result_type string: (optional)Determines what the output of the conversion will be. It can be either "FE Solids", "Volumes" or "Light volume representation". Default option is "Volumes". If the conversion does not run on the whole db the result will be FE Solids.

	@split_layers_at_sharp_convex_features boolean: (optional)When on the layers on convex features are split to improve quality

	@returns object: Returns 0 on success and 1 on failure.
	If ret_ents=True it will return a list with the created entities or None if no entities are created.

	"""

def ConvertHexaToMorph(entities):

	"""

	Script function that converts hexa boxes to morphing boxes.


	@entities object: A list that contains hexa boxes.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def ConvertHexaToSizeBox(entities,  max_surface_length, max_volume_length):

	"""

	Script function that converts hexa boxes to size boxes.


	@entities object: A list that contains hexa boxes.

	@max_surface_length float: (optional)The maximum value for surface length.

	@max_volume_length float: (optional)The maximum value for volume length.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def Convex(input_data, tolerance, offset_status, offset_mode, offset_value, module_id, property_id):

	"""

	Creates a convex mesh for the user data.


	@input_data object: A list of convex input data. The object of input data can be 
	points, curves, face, grids, elements, properties, materials, volumes, sets,
	includes, parts or groups.

	@tolerance float: The value of tolerance for the convex function.

	@offset_status string: The string that will allow to 'offset' the convex. This string takes two 
	values "yes" or "no".

	@offset_mode string: The string that defines the type of offset for the convex. That string takes
	two values "absolute" or "parametric".

	@offset_value float: The value of offset.

	@module_id string: The string for the 'module Id' of part/group. If the string is empty (""),
	the function create a default part to place the results of the convex.

	@property_id integer: The value of the 'property Id'. If the value is equal to zero or negative, the
	function creates one default property to place the results of the convex.

	@returns object: Returns a list with the results of the convex.
	The list contains the elements of the convex. If the list is empty, the function is not 
	able to create the convex of input data. If the data are coplanar, then a 2D convex will be created. 
	Note, that the elements of 2D-convex are straight curves in sequence. In other case, 
	the matrix will contain shell elements.

	"""

def CreateOGridTopology(hexa_boxes, free_faces, offset, pattern_type, pattern_coef, branch_faces, fix_intersections, offset_algorithm):

	"""

	Script function that creates O-Grid topology for the input boxes.


	@hexa_boxes object: A list that contains boxes that will be affected when O-Grid is created.

	@free_faces object: A list that contains the faces where no O-Grid will be generated from.

	@offset float: The offset value of the created O-Grid topology.

	@pattern_type string: A string that defines O-Grid topology's pattern. There are three 
	types: (i) "Automatic", (ii) "Linear" and (iii) "Bell Shape".

	@pattern_coef float: (optional)A number that defines the factor of pattern  algorithm. 
	It's a real number that takes values from 0 to 1.
	This parameter is used only for "Linear" and "Bell Shape" patterns.

	@branch_faces object: (optional)A list that contains branch faces of the structure. This parameter is 
	used only for "Linear" and "Bell Shape" patterns.

	@fix_intersections boolean: (optional)Activates a mechanism that fixes intersections.

	@offset_algorithm string: (optional)It takes the values "Absolute offset value", "Factor of local length"
	and "Parametric (0-1)".
	(Default: "Absolute offset value")

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def CutShellsWithPlane(input, coordinates, target_edges_number, zones, number_of_shell_zones_affected, move_projection_to_nearest_perimeter, add_results_to_set, cut_faces_on_result_edges, cut_faces_on_result_zones, release_result_edges, dont_reconstruct_mesh, freeze_non_single_boundary):

	"""

	This function cuts shells with planes.


	@input object: Can be a single or an array of entities, parts, properties, 
	materials, sets or macros. If the INPUT is 0, 
	the visible shells are collected.

	@coordinates object: A list containing 3 lists that descibe the three points that 
	define the plane.

	@target_edges_number integer: (optional)Greater than 0. Resulting edges number.

	@zones object: (optional)A list of zones offset.

	@number_of_shell_zones_affected integer: (optional)Number of shell zones around cut to be affected.

	@move_projection_to_nearest_perimeter float: (optional)Minimum distance between projections and near perimeters.

	@add_results_to_set string: (optional)Add the results to the specified set.

	@cut_faces_on_result_edges boolean: (optional)Create perimeters on resulting edges option.

	@cut_faces_on_result_zones boolean: (optional)Create perimeters on resulting zones option.

	@release_result_edges boolean: (optional)Release resulting edges option.

	@dont_reconstruct_mesh boolean: (optional)Avoid reconstructing mesh option.

	@freeze_non_single_boundary boolean: (optional)Determines whether an additional zone of elements will be added automatically so as to not have frozen edges in the initial selection.(Default=False)

	@returns integer: Returns 1 on success, or 0 on failure.

	"""

def DeleteOGridTopology(entities):

	"""

	Script function to delete O-Grid topologies.


	@entities object: A list that contains O-Grid entities

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def EdgesToPerimeter(SET):

	"""

	Creates perimeters in given edges (via set).


	@SET object: The set with the edges.

	@returns integer: Returns -1 in case of no edges, 0 if everything is OK, 1 if an error occurs.

	"""

def FEMToSurf(shells, delete, ret_ents):

	"""

	This function creates Faces from each shell element of shells list.


	@shells object: A list with shell elements.

	@delete boolean: Delete shells or not.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@returns object: Returns 1 on success, 0 on failure.
	If ret_ents=True it will return a list with the created entities, or None if no entities are created.

	"""

def FEMToSurfArea(shells, ret_ents, delete, imprint):

	"""

	This function creates one Face per group of shell elements. Those groups are formed by
	feature detection between the given shell elements.


	@shells object: A list of shell objects or a string with value 'visible'. If it is called 
	with 'visible' it works for all the visible shell elements.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@delete boolean: (optional)If set to 'True', non-frozen shells that created macros will get deleted.

	@imprint boolean: (optional)If set to 'False', shells will not get imprinted on macros.

	@returns object: Returns 1 on success, 0 on failure.
	If ret_ents=True it will return a list with the created entities, or None if no entities are created.

	"""

def FemTopo(tolerance, shells_to_be_pasted, max_tolerance, steps):

	"""

	The function performs pasting of shells elements in FE models, for which the distance
	between the opposite boundary edges does not exceed the given one in the
	tolerance value. The list contains all shells which may have boundary edges
	that may or may not be pasted. If the tolerance passed as argument is equal to 0,
	the default nodes matching distance will be used instead. In case the list is
	empty or 0, FemTopo function will be applied to all visible shells. In this case a
	range of tolerances can be defined so that a series of pastings can be performed
	starting from a tolerance value of 'tolerance' up to the value set by 'max_tolerance'.
	The number of steps is declared in the 'steps' value. If max_tolerance and steps
	are set to 0, only one pasting will be performed based on the 'tolerance' value.


	@tolerance object: The tolerance value, which the distance between the opposite boundary edges 
	should not exceed. If the tolerance is equal to 0, the default nodes matching 
	distance will be used instead.

	@shells_to_be_pasted object: A list that contains all shells which may have boundary edges.
	In case that the list is empty or 0, the FemTopo function will be applied to 
	all the visible shells.

	@max_tolerance: The maximum tolerance value.

	@steps: The number of steps.

	@returns integer: Returns 1 on success, 0 otherwise.

	"""

def FillGapFreeShells(SET1, SET2, RECONS, PART, PROP):

	"""

	Fill the gap between two sets of shells. The function, automatically, keeps the
	outer most perimeter of each set and tries to fill the gap between the two
	perimeters.


	@SET1 object: A list of entity objects (shell property, shell,set, include, ansapart or ansagroup) 
	with SET objects defining the first set.

	@SET2 object: A list of entity objects (shell property, shell,set, include, ansapart or ansagroup) 
	with SET objects defining the second set.

	@RECONS object: The reconstruction flag:
	-not equal to 0: reconstruction will take place.
	-equal to 0: no reconstruction.

	@PART object: A part object or a part id (module_id).

	@PROP object: A prop object or a prop id.
	 If 0 a new property will be created.

	@returns object: Returns a list with the results (shell elments).

	"""

def FillHole(diameter, point_on_center, convert_to_spot, create_curve, zones_num, part_or_property, with_stl):

	"""

	This function fills holes on fe models or holes opened with the Open Hole function.


	@diameter float: The maximun diameter of the holes to be filled.

	@point_on_center boolean: Determines whether a 3d point will be created at the center of the hole.

	@convert_to_spot boolean: Can be used to convert the center 3d point to a connection point.

	@create_curve boolean: If set to True, a curve will be created on the hole's perimeter.

	@zones_num integer: Sets the number of shell zones around the hole to be reconstructed after the fill.

	@part_or_property string: (optional)Can be passed to set the part or property of the shells created.

	@with_stl boolean: (optional)If set to True, stl type mesh will be created.

	@returns object: Returns a list of the shells involved in the procedure, or None if fill hole failed.

	"""

def FixQualSolids(external_bounds_distance):

	"""

	This function moves solids nodes in order to fix mesh quality criteria problems, without altering mesh topology.
	The function works only on visible.


	@external_bounds_distance anything: (optional)Defines the maximum distance from external bounds that a node is allowed to move.
	It can be defined as an integer, a float value, or an expression containing "local", 
	which is the local length for every node. If not specified, the external bound distance
	will be set from Defaults ("maximum_distance_from_external_bounds").

	@returns integer: Returns 1 in case of valid expression for external bounds distance, otherwise 0.

	"""

def GetGridsThickness(Grids):

	"""

	A function that gets nodal thickness of given grids.


	@Grids object: A list of grid references.

	@returns object: Returns a list that contains the thicknesses of the given grids. If a grid belongs to more than one shell and
	thus, has been assigned more than one nodal thickness the matrix contains the arithmetic mean of these thicknesses.

	"""

def GetMacroShells(macros):

	"""

	This function gets all the shells of the given macros.


	@macros object: A list of Macro objects.

	@returns object: Returns a list that contains all the shells that were found, or 0 if no shell was found.

	"""

def GetMapVolumeBoundaries(volume):

	"""

	This function collects the boundary of a given Map volume.


	@volume object: The volume whose boundary will be returned.

	@returns object: Returns a dict with keys "master", "slave", "round". Each key has a list with entities as value. 
	Returns None on error.

	"""

def GetReconstructAttachedSolidsValue(labels):

	"""
	Deprecated since version 19.0.0. Use function GetANSAdefaultsValues instead.

	Gets parameter values concerning all shell mesh functions that run reconstruct 
	when there are attached solids on the shells.


	@labels object: A List of string values. Accepting values are "attached solids" and "conflicting areas".

	@returns integer: Returns a dictionary with two items:
	-key: "attached_solids"      value: a value of {local remesh, affect only skin, freeze skin, always ask}
	-key: "conflicting_areas"    value: a value of {merge, keep larger, select, always ask}

	"""

	import warnings; warnings.warn("Deprecated since version 19.0.0. Use function GetANSAdefaultsValues instead.", DeprecationWarning)

def GetShellMacro(shells):

	"""

	This function gets the macros the given shells belong to.


	@shells object: A list of shell objects.

	@returns object: Returns a list that contains all found macros or 0 if no macro could be found.

	"""

def GetSmoothAttachedSolidsValue(labels):

	"""
	Deprecated since version 19.0.0. Use function GetANSAdefaultsValues instead.

	Gets parameter values concerning all shell mesh functions that run smooth 
	when there are attached solids on the shells.


	@labels object: A List of string values. Accepting values are "attached solids" and "conflicting areas".

	@returns object: Returns a dictionary with two items:
	-key: "attached_solids"      value: a value of {local remesh, affect only skin, freeze skin, always ask}
	-key: "conflicting_areas"    value: a value of {merge, keep larger, select, always ask}

	"""

	import warnings; warnings.warn("Deprecated since version 19.0.0. Use function GetANSAdefaultsValues instead.", DeprecationWarning)

def GetVolumeBoundary(volume):

	"""

	This function collects the boundary of a given volume. The argument is the volume whose boundary elements
	will be returned.


	@volume object: A reference to a volume object, whose boundary elements will be returned.

	@returns object: Returns a list with the boundary elements on success, or None on failure.

	"""

def GetVolumesMapParameters(volume):

	"""

	This function returns the parameters of a given Map volume.


	@volume object: The volume whose parameters will be returned as an argument.

	@returns object: Returns a list of the parameters ("Normal parts" or "Thin parts" method, number of steps) 
	if the values are returned properly and 0 otherwise.

	"""

def GetVolumesOffsetParameters(volume):

	"""

	This function returns the parameters of a given Offset volume.


	@volume object: The volume object whose parameters will be returned.

	@returns object: Returns a list of the offset parameters(dist, steps, middle, bias_type, bias_factor) 
	if the values are returned properly and 0 otherwise.

	"""

def GetVolumesRotateParameters(volume):

	"""

	This function returns the parameters of a given Rotate volume.


	@volume object: The volume object whose parameters will be returned.

	@returns object: Returns a dict with keys "origin" (this is a list (x, y, z)), "vector" (this is a list (dx, dy, dz)), 
	"angle", "steps", "biasing_type" and "biasing_factor".

	"""

def GetVolumesTranslateParameters(volume):

	"""

	This function returns the parameters of a given Rotate volume.


	@volume object: The volume object whose parameters will be returned.

	@returns object: Returns a list with the following parameters parameters 
	[dx", "dy", "dz", dist, steps] on success, or 0 otherwise.

	"""

def HexaBlockLength(edges, length, distribution, is_factor):

	"""

	A function to define the element length on hexa box edges.


	@edges object: A list that contains hexa box edges.

	@length float: The element length that we want to apply.

	@distribution string: (optional)A parameter used to define length on input opposite edges and 
	takes the following values: 
	i) "max": distribute nodes according to the edge 
	with the maximum number of nodes (default value).
	ii) "min": distribute nodes according to the edge 
	with the minimum number of nodes.
	iii) "average": distribute nodes according to the 
	average number of nodes on opposite edges.

	@is_factor boolean: (optional)If 'True', the final length is calculated by multiplying the input length by 
	the existing element length. If 'False', the final length equals the input length.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def HexaBlockNumber(input, number, apply_multiple_number, remesh_macros, apply_number_of, ortho_spaced):

	"""

	This function defines a new number of edges (or nodes) on Hexa Box Edges.


	@input object: Input can be an entity or an array of entities, parts, 
	hexa box faces, hexa box edges. If the input is 0, visible 
	hexa box edges are collected.

	@number string: A string which can either be a number (eg. "3"), 
	or an expression to add or remove nodes (eg. "+2", "-3", "*2").

	@apply_multiple_number boolean: (optional)If set to True, the function creates chains of connected 
	box edges and distributes accordingly the given number 
	to the chains. If deactivated (False) or missing, then all 
	entities will get the same number.

	@remesh_macros boolean: (optional)If set to True, the function remeshes affected hexa box faces
	after applying number. If missing (False) then the current gui 
	value will be used.

	@apply_number_of string: (optional)It takes the values "edges" or "nodes", and it applies as 
	INPUT as a number of edges or nodes. If missing then the 
	current gui value will be used.

	@ortho_spaced boolean: (optional)Defines if ortho-spaced numbering algorithm will
	be applied for input box edges. This option is valid
	only in the case that we don't apply the "multiple number" algorithm.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def HexaBlockSpacing(edges, algorithm, factor, dmin, dmax, dmax_dmin_ratio, dlimit, steps, dir, factor_end, apply_to_opposite, u_parameters, dstart, dend):

	"""

	A function that distributes nodes according to a spacing algorithm.


	@edges object: A list that contains hexa box edges.

	@algorithm string: A string that defines the spacing algorithm. There are 
	five spacing algorithms: (i) "Linear", (ii) "Geometric", "Bell Curve",
	"User Defined" and "Bi-Geometric". Every spacing algorithm requires 
	some specific arguments.

	@factor float: (optional)A number that defines the factor of the algorithm. For "Linear" 
	and "Bell Curve" spacing it is any positive real number. For 
	"Geometric" and "Bi-Geometruc" spacing, it should be greater than 1.

	@dmin float: (optional)A number that defines minimum nodal distance (>0). 
	It is used only for "Geometric" spacing.

	@dmax float: (optional)A number that defines maximum nodal distance (>0). 
	It is used only for "Geometric" spacing.

	@dmax_dmin_ratio float: (optional)A number that defines the ratio of maximum to minimum 
	nodal distance. It is used only for "Geometric" spacing.

	@dlimit float: (optional)A number that defines the limiting nodal distance 
	(when reached, the geometric series will keep it. It is 
	used only for "Geometric" spacing.

	@steps integer: (optional)The number of steps applied to the spacing algorithm

	@dir string: (optional)A flag that defines whether spacing will be applied 
	from the start (dir="start") or end point (dir="end") of 
	the hexa box edge. It is used for "Linear", "Geometric" and "Bi-Geometric"
	spacing algorithms. For "Linear" spacing, if "factor_end" 
	is used, "dir" is ignored.

	@factor_end float: (optional)Defines the factor for the spacing that begins from 
	the end point of box edge. If this factor is used, "Dir" 
	keyword is ignored. It is only used for "Linear" spacing 
	algorithm.

	@apply_to_opposite boolean: (optional)Defines if spacing will be applied to all opposite
	box edges.

	@u_parameters object: (optional)List of parameters that define the position of nodes
	on box edges.

	@dstart float: (optional)A number that defines the length value (>0) at start of box edges. 
	It is used only for "Bi-Geometric" spacing. If it is not defined, it is 
	regarded equal to "dend".

	@dend float: (optional)A number that defines the length value (>0) at end of box edges. 
	It is used only for "Bi-Geometric" spacing. If it is not defined, it is 
	regarded equal to "dstart".

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def HexaBlockVolSkin(volumes, ret_ents):

	"""

	Script function that generates volume skin for the specified hexa block volumes.


	@volumes object: A list that contains volumes (the volumes should be meshed).

	@ret_ents boolean: (optional)If set to True a list with the created entities will be returned.

	@returns integer: Returns 1 on success, 0 on failure.
	If ret_ents=True it will return a list with the created entities or None if no entities are created.

	"""

def HexaBlockVolumes(boxes, tolerance, project, output_filename, ret_ents, tolerance_expr, apply_surface_fit, project_non_associated):

	"""

	A function that generates volume mesh for the specified hexa boxes.


	@boxes object: A list that contains the hexa boxes that we want 
	to mesh (hexa boxes should not be meshed).

	@tolerance float: (optional)The tolerance to project on geometry.

	@project boolean: (optional)A flag that defines whether to project (True) or 
	not (False) on geometry.

	@output_filename string: (optional)An argument to define the full path where output of the 
	generated mesh will be stored (output file contains 
	information for Node Id, x, y, z, Box Id). If this argument 
	is not filled, no output will be generated for these boxes.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@tolerance_expr string: (optional)An expression to define the tolerance as a percentage of the minimum 
	element length (Lmin). If expression is defined, "tolerance" is argument
	will be ignored.

	@apply_surface_fit boolean: (optional)A flag that defines if surface-fit will be applied for
	fully associated box faces (box faces with points,
	edges and face association).

	@project_non_associated boolean: (optional)A flag that defines if nodes of non-associated box
	faces will be projected on the geometry.

	@returns object: Returns 1 on success, 0 on failure.
	If ret_ents=True it will return a list with the created entities, or None if no entities are created.

	"""

def HexaBoxDelete(boxes):

	"""

	Script function that deletes Hexa-Block boxes.


	@boxes object: An object or list that contains the Hexa-Block boxes to be deleted.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def HexaBoxUndelete(entities):

	"""

	Script function that "undeletes" previously deleted hexa boxes.


	@entities object: A list that contains the hexa boxes to get "undeleted".

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def HexaInterior(coordinate, maximum_length, volume):

	"""

	The HexaInterior() function applies volume meshing to defined volumes, producing hexainterior.


	@coordinate object: The coordinate entity.

	@maximum_length float: The maximum length.

	@volume object: (optional)The volume to be meshed.
	If it is not given, all volumes will be meshed.

	@returns integer: It returns 0 in case of success, non-zero on failure.

	"""

def HexaInteriorbyID(volume, coord, Maxlength):

	"""
	Deprecated since version 18.0.0. Use function HexaInterior instead.

	This function meshes a Volume in question with the algorithm HEXA-INTERIOR.


	@volume integer: The Id of the volume to be meshed.

	@coord integer: The Id of the coordinate system that defines the orientation of the HEXA elements. 
	If 0 is typed the orientation is defined according to the global coordinate system.

	@Maxlength float: The maximum element length of the HEXA elements.

	@returns integer: It returns 0 in case of success, non-zero on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 18.0.0. Use function HexaInterior instead.", DeprecationWarning)

def InitPerimeters(cons, remesh_macros, initialize_number, initialize_spacing, use_ansa_defaults_values):

	"""

	This function initializes the nodal spacing of perimeters. 
	It works like the gui function PERIMETERs>INIT.
	The INPUT is a matrix that contains perimeters (CONS, FE perimeters).


	@cons object: A list of CONS objects.

	@remesh_macros boolean: (optional)True or False. (Default: False)

	@initialize_number boolean: (optional)True or False. (Default: False)

	@initialize_spacing boolean: (optional)True or False. (Default: False)

	@use_ansa_defaults_values boolean: (optional)If set to True, the function uses parameters from ANSA.defaults, by-passing all other arguments.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def IsVolumeMeshed(volume):

	"""

	This function checks whether a volume is meshed or not.


	@volume object: A reference to the volume object.

	@returns integer: Returns 1 if the volume is meshed and 0 otherwise.

	"""

def IsolateBaffles( baffles_inside_volumes, baffles_with_red_bounds ):

	"""

	This function isolates on the screen all the identified zero-thickness walls.


	@baffles_inside_volumes boolean: (optional)If set to True, then the function will leave visible only the baffles 
	identified inside closed volumes, otherwise also elements or geometry 
	that does not belong to a closed volume will remain visible.
	(Default: False)

	@baffles_with_red_bounds boolean: (optional)If set to true then the baffles that do not have any red bounds are 
	ignored and are not isolated.
	(Default: False)

	@returns integer: Returns 0 in all cases.

	"""

def IsolateFeatureShells(PARAMS, EXPAND_LEVEL):

	"""

	Collect visible shells that are recognized as features that are giong to be treated, according to user defined parameters.


	@PARAMS string: Contains keywords that correspond to features to collect.
	Accepted keywords are "FILLETS", "FLANGES", "HOLES" and "VIOL".
	Fillets, flanges and holes recognition is based on PARAM fillets, 
	flanges and holes treatment parameters correspondingly. 
	Violating shells recognition is based on Quality Criteria.

	@EXPAND_LEVEL integer: The number of the expanding shells zones added around recognized shells.

	@returns object: Returns a list that contains all the shells recognized as features.

	"""

def JoinMacros(entities, keep_mesh, auto_delete_hot_points, use_ansa_defaults_values):

	"""

	This function joins the macros that belong to the given perimeters (Cons, FE).


	@entities object: A list that contains perimeters (Cons, FE).

	@keep_mesh boolean: (optional)If the existing mesh should be kept or erased after the joining.

	@auto_delete_hot_points boolean: (optional)If the hot points should be deleted after the joining or not.

	@use_ansa_defaults_values boolean: (optional)If set to True, the function uses parameters from ANSA.defaults, by-passing all other arguments.

	@returns integer: Returns the number of all succeeded joinings or 0 if no joining could be performed.

	"""

def ApplyNewLengthToMacros(element_length, perimeters, use_ansa_defaults_values):

	"""

	This function applies a specified element length to Perimeter Segments of Macros and FE perimeters.


	@element_length string: The element length that will be applied.

	@perimeters object: (optional)A list that contains perimeters (Cons, FE). If it is set to 0, visible perimeters will be used.

	@use_ansa_defaults_values boolean: (optional)If set to True, the function uses parameters from ANSA.defaults, by-passing all other arguments.

	@returns integer: Returns 0 in all cases.

	"""

def EraseMesh():

	"""

	This function deletes the shell mesh of visible Macro Areas.


	@returns integer: Returns 0 in all cases.

	"""

def Remesh():

	"""

	This function meshes using the last used algorithm.
	The function works only on visible macros.


	@returns integer: Returns 0 in all cases.

	"""

def FixQuality():

	"""

	This function moves nodes in order to fix mesh quality criteria problems, without altering mesh topology.
	The function works only on visible macros.


	@returns integer: Returns 0 in all cases.

	"""

def Reconstruct():

	"""

	This function is applied on an existing mesh and performs remeshing to optimize the overall quality and flow of the mesh, correct quality criteria violations and enforce special mesh treatments. The function can be applied on Macro Area mesh or FE-Model mesh. The function works only on visible macros like the GUI function Reconstruct[Visible].


	@returns integer: Returns 0 in all cases.

	"""

def Reshape():

	"""

	This function is the most advanced quality improvement function. It can be applied on meshed Macro Areas in order to optimize the mesh quality in various aspects. Apart from leading to a high quality mesh, one of its main advantages is the fact that it eliminates to a minimum the need to manually cut, join and align Macro Areas.
	The function works only on visible entities (Macros or released FE shell elements).


	@returns integer: Returns 0 in all cases.

	"""

def Smooth():

	"""

	This function is useful in order to smooth the mesh after a manual node pasting or element splitting or joining.
	The function works only on visible macros.


	@returns integer: Returns 0 in all cases.

	"""

def ModifyOGridTopology(ogrid, offset, pattern_type, pattern_coef, fix_intersections, offset_algorithm):

	"""

	Script function that modifies the input O-Grid topology.


	@ogrid object: The O-Grid topology that will be modified.

	@offset float: (optional)The value defining the offset value of the O-Grid topology.
	It's a real number different than zero.

	@pattern_type string: (optional)Defines the O-Grid pattern type. There are three types: 
	(i) "Automatic" 
	(ii) "Linear" 
	(iii) "Bell Shape"

	@pattern_coef float: (optional)The value defining the factor of pattern algorithm.
	It's a real number that accepts values from 0 to 1.

	@fix_intersections boolean: (optional)Activates the mechanism that fixes the intersections.

	@offset_algorithm string: (optional)It accepts the values "Absolute offset value", "Factor of local length"
	and "Parametric (0-1)".

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MoveGridsToOrigin(entities):

	"""

	Moves all incoming grids to their origin position.


	@entities object: A list of grids.

	@returns integer: Always returns 1.

	"""

def OpenHole(coordinates, tolerance, number_of_zones, nodes_around_hole, hole_diameter, zone1_length, zone2_length, entities):

	"""

	This function opens holes or creates spots on the whole or on certain parts of the base.
	The user can provide the function with one or more 3D points by giving their coordinates.


	@coordinates object: A list with (x, y, z) coordinates tuples.

	@tolerance float: The tolerance value.

	@number_of_zones integer: The number of affected shell zones  during reconstruct. Limiting the number of affected zones may affect the mesh quality.

	@nodes_around_hole integer: The target number of nodes on the hole's perimeter. A value <4 is not accepted whereas negative number 
	means that there is no restriction to this number and zero means that a spot 
	will be created.

	@hole_diameter float: The diameter of the hole.

	@zone1_length object: The zone's 1 length. If a negative number is inserted no zone will be created.
	A list with floats.

	@zone2_length object: The zone's 2 length. If a negative number is inserted no zone will be created.
	A list with floats.

	@entities object: (optional)determines where the function will search for a shell to make the
	projection. If entities[0] is a reference to a part and entities[1] 
	is a reference to a material the search will be performed on the 
	specified part and material. Supported references are references to 
	parts, groups, properties, materials and sets. If zero is entered the search
	is performed on the whole base.

	@returns object: Returns a list, where the first three elements are lists containing references to the 
	nodes on the first hole's perimeter and on the first and second zone respectively. 
	If an element does not exist (ex. no zone created), then zero is placed on this element.

	"""

def OrientVolumebyID(volume):

	"""
	Deprecated since version 18.0.0. Use function OrientVolume instead.

	This function orients all the elements of the volume so that they all point inwards (gray side).


	@volume integer: The Id of the volume that is going to be oriented.

	@returns integer: Returns 1 on success and 0 otherwise

	"""

	import warnings; warnings.warn("Deprecated since version 18.0.0. Use function OrientVolume instead.", DeprecationWarning)

def ProjectNodesArrayOnShells(input, nodes_array, projection_tolerance, maximum_projections_number, user_projection_mode_vector, zones, number_of_shell_zones_affected, move_projection_to_nearest_perimeter, move_to_projected_perims, paste_projected_and_result_edges, add_results_to_set, cut_faces_on_result_edges, cut_faces_on_result_zones, release_result_edges, apply_fill_gap_on_results, open_closed_perimeter_hole, freeze_non_single_boundary, is_extend):

	"""

	This function projects a polyline defined by nodes on shells.


	@input object: Can be an object, a list of objects, parts, properties, 
	materials, sets or macros.
	If input is 0, the visible shells are collected.

	@nodes_array object: A list containing node objects that define the polyline. In case of more that one polylines the list should contain lists of node objects defining each polyline. Closed polylines should contain the same first and last node

	@projection_tolerance float: (optional)Maximum distance between the projection and the 
	projected entity.

	@maximum_projections_number integer: (optional)Maximum number of projections.

	@user_projection_mode_vector object: (optional)A list of the vector components for the user defined 
	project vector.

	@zones object: (optional)A list of zones offset. Create zones at projection. Each offset 
	value must be greater than 0.

	@number_of_shell_zones_affected float: (optional)Number of shell zones around projection to be affected.

	@move_projection_to_nearest_perimeter float: (optional)Minimum distance between projections and near perimeters.

	@move_to_projected_perims float: (optional)Between 0. and 1. Parameter to move the result edges towards 
	the projected perimeters.

	@paste_projected_and_result_edges boolean: (optional)Paste projected and result edges.

	@add_results_to_set string: (optional)The name of the existing set. If the set doesn't exist, 
	a default set will be created.

	@cut_faces_on_result_edges boolean: (optional)Create perimeters on resulting edges option.

	@cut_faces_on_result_zones boolean: (optional)Create perimeters on resulting zones option.

	@release_result_edges boolean: (optional)Release resulting edges option.

	@apply_fill_gap_on_results boolean: (optional)Applies fill gap between source and projected edges.

	@open_closed_perimeter_hole boolean: (optional)Creates an opening if the projected edges form a closed perimeter.

	@freeze_non_single_boundary boolean: (optional)Determines whether an additional zone of elements will be 
	added automatically so as to not have frozen edges in the 
	initial selection.

	@is_extend boolean: (optional)If True projection vector will be in the extend direction. Works only If user_projection_mode_vector is empty.

	@returns integer: This function always returns 1

	"""

def ProjectOpenHole(holes, add_to_set, cut_faces_on_holes_edges, cut_faces_on_zones_edges):

	"""

	ProjectOpenHole opens holes or creates spots on parts specified for each point.


	@holes object: A list containing lists with objects that define the hole. A list for 
	every hole is needed
	-coordinates: Is an array with three float numbers one for each 
	corresponding coordinate of the point we need to project in order to 
	create a hole on each part.
	-parts: Is an array that holds every part we need to create a hole upon.
	-parameters: Is an array that holds all the necessery parameters for 
	the hole creation, these are:
	int zone_num,
	float proj_tolerance, 
	int target_node_num, 
	float diameter,
	float zone1_len,
	float zone2_len,
	bool quads_around_proj_point,
	bool square_holes, 
	bool create_perfect_zone.
	
	The specified point will be projected to every part determined in 
	parts with distance less than proj_tolerance.
	-proj_tolerance should be greater or equal to zero.
	 A hole will be opened or a spot will be created on every projection.
	-zone_num is the number of shell zones that will be affected around 
	 the hole respectively. Valid values are greater than zero.
	-target_node_num is the target number of nodes on the hole's perimeter. 
	 Zero value means that a spot will be created instead of a hole.
	 Less that zero values will assign a rundom number.
	-diameter is the diameter of the hole. Valid values are greater thar zero. 
	-zone1_len and zone2_len are the desired zones' length.
	 Zero value for a zone length means that the corresponding zone will not 
	 be created. Negative values are not valid.
	-quads_around_proj_point indicates that 4 quads will be created 
	 around spots, for values different than zero. 
	-square_holes indicates that a square hole will be created (affects only 
	 holes with 8 nodes around hole), for values different than zero.
	-create_perfect_zone indicates that perfect zones will be created 
	 for values different than zero.

	@add_to_set string: (optional)The set's name to which new holes will be set to.
	If the set doesn't exist, a default set will be created.

	@cut_faces_on_holes_edges boolean: (optional)Controls whether the faces will be cut on opened hole edges.

	@cut_faces_on_zones_edges boolean: (optional)Controls whether faces will be cut on opened hole zone edges.

	@returns object: Returns an array containing integers. 
	For every hole of array holes and every part of array parts of each hole, the returned array contains a value.
	If the hole is created on the corresponding part, value 1 is placed in the array, otherwise 0.
	The order of the values is defined by the order of the holes and each parts.

	"""

def ProjectPerimeterOnShells(input, perimeters, projection_tolerance, maximum_projections_number, user_projection_mode_vector, target_edges_number, zones, number_of_shell_zones_affected, move_projection_to_nearest_perimeter, move_to_projected_perims, add_results_to_set, cut_faces_on_result_edges, cut_faces_on_result_zones, release_result_edges, freeze_non_single_boundary, apply_fill_gap_on_results, open_closed_perimeter_hole, is_extend):

	"""

	This function projects perimeters on shells.


	@input object: Can be an object or an array of objects, parts, properties, 
	materials, sets or macros.
	If the INPUT is 0, the visible shells are collected.

	@perimeters object: It can be an object or a list of curves, cons or morph edges.

	@projection_tolerance float: (optional)Maximum distance between the projection and the projected 
	entity.

	@maximum_projections_number float: (optional)Maximum number of projections.

	@user_projection_mode_vector object: (optional)A list of vector components to define the user project vector.

	@target_edges_number float: (optional)Resulting edges number.

	@zones object: (optional)A list of zones offset. Create zones at projection. Each offset 
	value must be greater than 0.

	@number_of_shell_zones_affected float: (optional)Number of shell zones around projection to be affected.

	@move_projection_to_nearest_perimeter float: (optional)Minimum distance between projections and near perimeters.

	@move_to_projected_perims float: (optional)Between 0. and 1. Parameter to move the result edges towards 
	the projected perimeters.

	@add_results_to_set string: (optional)Name of existing set. If the set doesn't exist, a default set 
	will be created.

	@cut_faces_on_result_edges boolean: (optional)Create perimeters on resulting edges option.

	@cut_faces_on_result_zones boolean: (optional)Create perimeters on resulting zones option.

	@release_result_edges boolean: (optional)Release resulting edges option.

	@freeze_non_single_boundary boolean: (optional)Determines whether an additional zone of elements will be 
	added automatically so as to not have frozen edges in the 
	initial selection.

	@apply_fill_gap_on_results boolean: (optional)Determines whether apply gap will be applied between the 
	projected and the resulting edges.

	@open_closed_perimeter_hole boolean: (optional)Determines whether a hole will be opened when a closed 
	perimeter is projected.

	@is_extend boolean: (optional)If True projection vector will be in the extend direction. Works only If user_projection_mode_vector is empty.

	@returns integer: This function always returns 1

	"""

def ReadMeshParams(FILENAME):

	"""

	This function reads mesh parameters.


	@FILENAME string: The path to the filename containing the parameters.

	@returns integer: Returns 0 if file does not exist, or 1 otherwise.

	"""

def ReadQualityCriteria(FILENAME):

	"""

	This function reads quality criteria.The argument is the path to the filename containing the criteria.


	@FILENAME: The path to the filename.

	@returns integer: Returns 0 if file does not exist, or 1 otherwise.

	"""

def ReconstructShells(SHELLS):

	"""

	The function perfrorms Reconstruct on shells given by the user.


	@SHELLS object: A list with the shells to be reconstructed.

	@returns integer: Returns 1 in all cases.

	"""

def ReconstructTetra():

	"""

	This function applies the IMPROVE>Reconstruct function on the visible Tetras.


	@returns integer: Returns 0 in any case.

	"""

def ReconstructViolatingTetra(N):

	"""

	This function reconstructs the violating TETRAs and N neighboring zones.


	@N integer: The number of neighboring zones.

	@returns integer: Returns 0 in any case.

	"""

def RefineElements(ELEMENTS_TO_BE_REFINED, EXTERNAL_TRANSITION_ZONE, MAX_REFINEMENT_STEPS, MIN_EDGE_LENGTH, NUMBER_OF_TRANSITION_ZONES, ALLOW_TRIAS_AT_REFINED_AREA, REFINEMENT_MESH_TYPE, SMOOTH_EXTERNAL_TRANS_ZONE, FREEZE_FREE_EDGES):

	"""

	The function refines elements.


	@ELEMENTS_TO_BE_REFINED object: A list of shell entities.

	@EXTERNAL_TRANSITION_ZONE integer: An option that forbids the refining of the external element zone 
	of the elements contained in the list.
	Set 1 to enable or 0 to disable.

	@MAX_REFINEMENT_STEPS integer: The number of the maximum possible refinement steps that are going to be applied.

	@MIN_EDGE_LENGTH float: The minimum edge length of the refined elements.

	@NUMBER_OF_TRANSITION_ZONES integer: The number of not refined elements zones
	that lie between two successive refinement step areas.

	@ALLOW_TRIAS_AT_REFINED_AREA integer: An option that allows the existence of trias at the refined area.
	Set 1 to enable or 0 to disable.

	@REFINEMENT_MESH_TYPE integer: The type of mesh created during refinement.
	It can be defined as "MIXED", "QUAD", "RADIAL_QUAD",
	"SMOOTHED_QUAD", "MIXED 1 TO 3" and "QUAD 1 TO 3".
	However, some trias may be created at "QUAD" REFINEMENT_MESH_TYPE.

	@SMOOTH_EXTERNAL_TRANS_ZONE integer: An option that allows the smoothing of the external element zone, if this exists.
	Set 1 to enable or 0 to disable.

	@FREEZE_FREE_EDGES integer: An option that does not allow splitting single free boundaries.
	Set 1 to enable or 0 to disable.

	@returns integer: Returns 1 in case the list ELEMENTS_TO_BE_REFINE is valid and 0 in case it is invalid.

	"""

def RefineTrias(shells, number_of_transition_zones, preview_result):

	"""

	Refines the triangles contained in a list of shells.


	@shells object: A list of shell entities.

	@number_of_transition_zones integer: (optional)Expand levels of transition area to reconstruct.
	Valid values are greater than 0.
	(Default: 0)

	@preview_result boolean: (optional)Preview the refinement result. Acceptable value are 'True', 'False'.
	(Default: True)

	@returns integer: Always returns 1.

	"""

def ReleaseElements(FACES_VOLUMES_FOR_RELEASE):

	"""

	This function detaches the shell mesh from Macros or solid mesh from Volumes and creates independent FE-Model mesh.


	@FACES_VOLUMES_FOR_RELEASE object: A list that contains faces or volumes for release.

	@returns integer: Returns 0 in all cases.

	"""

def ReleaseMacros(macros, remesh_macros, keep_mesh, delete_hot_points, use_ansa_defaults_values):

	"""

	This function releases joined macro area boundaries.


	@macros object: A list that can contains perimeters (CONS) or macros (FACE).

	@remesh_macros boolean: (optional)Remesh the macros around the affected area.

	@keep_mesh boolean: (optional)Keep the existing mesh.

	@delete_hot_points boolean: (optional)Automatically delete the hot points after the release.

	@use_ansa_defaults_values boolean: If set to True, the function uses parameters from ANSA.defaults, by-passing all other arguments.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def SaveMeshParams(FILENAME):

	"""

	This function saves mesh parameters.


	@FILENAME string: The path of the filename where the parameters will be saved.

	@returns integer: Returns 1 in case of successful saving of the meshing parameters
	and 0 if the meshing parameters are not saved.

	"""

def SaveQualityCriteria(FILENAME):

	"""

	This function saves quality criteria.


	@FILENAME string: The path to the filename where the parameters will be saved.

	@returns integer: Returns 1 in case of successful saving of the quality criteria
	and 0 if the quality criteria are not saved.

	"""

def SealGaps(min_distance, max_distance, width, feat_line_angle, ret_ents):

	"""

	Script version of function MESH>SHELL_MESH>GILL_GAP>Seal.
	Works on visible.


	@min_distance float: Gaps with distance < min_distance will not be sealed.

	@max_distance float: Gaps with distance > max_distance will not be sealed, 
	must be min_distance < max_distance.

	@width integer: Expressed as a percentage, must be in [0,100].

	@feat_line_angle float: The feature line angle in degrees, must be in [0,180].

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@returns object: Returns 1.
	If ret_ents=True it will return a list with the created entities, 
	or None if no entities are created.

	"""

def SealHoles(max_diameter, ret_ents):

	"""

	Script version of function MESH>SHELL_MESH>GILL_GAP>Seal.
	Works on visible.


	@max_diameter float: Holes with diameter > max_diameter will not be sealed.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@returns integer: Returns 1.
	If ret_ents=True it will return a list with the created entities, 
	or None if no entities are created.

	"""

def SetGridsThickness(grids, thickness, use_original_thickness):

	"""

	A function that Sets nodal thickness upon given grids. The number of the given thicknesses 
	must be one (1) or equal to the number of the given grids. 
	The thickness list must have the exact same number of thicknesses as the Grids list. 
	If a Grid is included more than once then this Grid will be assigned the last given thickness.


	@grids object: A list of grid entities.

	@thickness object: A list of thicknesses corresponding to the list of grids.

	@use_original_thickness string: (optional)"Add" / "Multiply". Choose whether the new value should be added 
	or multiplied with the original nodal thickness of each grid.

	@returns integer: Returns 1 on success and 0 otherwise.

	"""

def SetMeshParamTargetLength(function, value):

	"""

	This function sets the target element length value.


	@function string: Can have the values "init_local", "average_length", "absolute" or "free".

	@value float: (optional)Target length for "absolute", or length multiplier for "init_local" or "average_length".

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def SetReconstructAttachedSolidsValue(attached_solids, conflicting_areas):

	"""
	Deprecated since version 19.0.0. Use function SetANSAdefaultsValues instead.

	Sets parameter values concerning all shell mesh functions that run reconstruct 
	when there are attached solids on the shells.


	@attached_solids string: (optional)One of "local remesh", "affect only skin", "freeze skin" or "always ask" 
	Determines if in case of attached solids the solids will be remeshed locally along with the shells, the shell mesh will change but solid mesh will remain untouched, the shells will be frozen or ask every time how to proceed (in no gui mode "local remesh" will be used in case of "always ask")

	@conflicting_areas string: (optional)One of "merge", "keep larger", "select" or "always ask"
	Defines the behaviour of the algorithm when the shells to be reconstruct are attached on structured solids in opposite areas.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 19.0.0. Use function SetANSAdefaultsValues instead.", DeprecationWarning)

def SetSmoothAttachedSolidsValue(attached_solids, conflicting_areas):

	"""
	Deprecated since version 19.0.0. Use function SetANSAdefaultsValues instead.

	Sets parameter values concerning all shell mesh functions that run smooth 
	when there are attached solids on the shells.


	@attached_solids string: (optional)One of "local remesh", "affect only skin", "freeze skin" or "always ask" 
	Determines if in case of attached solids the solids will be remeshed locally along with the shells, the shell mesh will change but solid mesh will remain untouched, the shells will be frozen or ask every time how to proceed (in no gui mode "local remesh" will be used in case of "always ask")

	@conflicting_areas string: (optional)One of "merge", "keep larger", "select" or "always ask"
	Defines the behavior of the algorithm when the shells to be reconstruct are attached on structured solids in opposite areas.

	@returns integer: Always returns 1.

	"""

	import warnings; warnings.warn("Deprecated since version 19.0.0. Use function SetANSAdefaultsValues instead.", DeprecationWarning)

def SetVolumesMapParameters(volume, method, steps):

	"""

	This function specifies the parameters of a given Map volume.


	@volume object: The volume object of which the parameters will be changed.

	@method string: The meshing method, the values of which can be "Normal parts" 
	or "Thin parts".

	@steps integer: The number of the steps in the round area.

	@returns integer: Returns 1 if the values are properly assigned and 0 otherwise.

	"""

def SetVolumesOffsetParameters(volume, dist, steps, middle, biasing, factor):

	"""

	This function specifies the parameters of a given Offset volume.


	@volume object: The volume whose parameters will be changed.

	@dist float: The offset length.

	@steps integer: The number of the generated elements.

	@middle integer: Can be 0 if offset is normal or 1 if the elements are divided 
	in the middle and are extracted in both sides of the shell elements.

	@biasing string: The biasing type: 'Linear', 'Exponential', Bell Curve' or 'No Biasing'.

	@factor float: The biasing factor.

	@returns integer: Returns 1 if the values are returned correctly and 0 otherwise.

	"""

def SetVolumesRotateParameters(volume, x, y, z, dx, dy, dz, angle, steps, biasing, factor):

	"""

	This function specifies the parameters of a given Offset volume.


	@volume object: The volume whose parameters will be changed.

	@x float: The x coordinate of the origin point.

	@y float: The y coordinate of the origin point.

	@z float: The z coordinate of the origin point.

	@dx float: The x component of the rotational vector.

	@dy float: The y component of the rotational vector.

	@dz float: The z component of the rotational vector.

	@angle float: The rotational angle.

	@steps integer: The number of the generated elements.

	@biasing string: The biasing type: 'Linear', 'Exponential', 'Bell Curve'or 'No Biasing'.

	@factor float: The biasing factor.

	@returns integer: Returns 1 if the values are returned correctly and 0 otherwise.

	"""

def SetVolumesTranslateParameters(volume, dx, dy, dz, dist, steps, biasing, factor):

	"""

	This function specifies the parameters of a given Offset volume.


	@volume object: The volume whose parameters will be changed.

	@dx float: The x component of the translational vector.

	@dy float: The y component of the translational vector.

	@dz float: The z component of the translational vector.

	@dist float: The translational distance.

	@steps integer: The number of the generated elements.

	@biasing string: The biasing type: 'Linear', 'Exponential', 'Bell Curve' or 'No Biasing'.

	@factor float: The biasing factor.

	@returns integer: Returns 1 if the values are returned correctly and 0 otherwise.

	"""

def SimplifyMacros(faces, fine_draft_slider, keep_perimeters_on_symmetry_plane, maintain_sharp_edges, minimum_side_length, minimum_perimeter_corner_angle, freeze_meshed_macros, test_gui_result):

	"""

	This function integrates the manual operations of JOIN Perimeter Segments, 
	or CUT Perimeter Segments, in order to satisfy the minimum requirements.


	@faces object: Accepted values: A list of faces, "ALL", "VISIBLE", 
	None (runs for all faces of the database).

	@fine_draft_slider float: (optional)This scale affects the number of non-feature perimeters that 
	will be joined.
	Accepted values are 0 - 100.
	The closer to 100 the more perimeters will be joined.

	@keep_perimeters_on_symmetry_plane boolean: (optional)If set to True, then if a perimeter is on the symmetry plane, 
	it will not be joined.

	@maintain_sharp_edges boolean: (optional)If set to True, then the function does not affect sharp edges.

	@minimum_side_length float: (optional)The distance, under which the function will join one perimeter and 
	make a new cut so that this value is not violated.

	@minimum_perimeter_corner_angle float: (optional)The angle between two perimeters, under which the function will 
	join one perimeter and make a new cut so that this value is not
	violated.

	@freeze_meshed_macros boolean: (optional)If set to True, then the function does not affect meshed macros.

	@test_gui_result boolean: (optional)If set to True, tests the result on GUI.

	@returns integer: Returns 1 on success, 0 on error.

	"""

def SmoothTetra():

	"""

	This function applies IMPROVE>SMOOTH on visible TETRA elements.


	@returns integer: Returns 0 in any case.

	"""

def SplitEdges(option_for_trias):

	"""

	This function splits all visible edges in the model in a similar way to the
	SPLIT function when edges are selected. Its argument is an integer.


	@option_for_trias integer: Accepted Values are 1 and 2, where 1 determines that triangles are split so
	that they form 4 other triangles, and 2 determines that they will be split as
	to form 3 quads. Quads will be split in a way to form 4 other quads.

	@returns integer: Always returns 1.

	"""

def SplitElements(shells, ret_ents):

	"""

	The function splits all quad elements contained in a list, which is passed as argument.


	@shells object: A list containing all the quad elements to be splitted.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@returns integer: Returns 1 on success, otherwise 0.
	
	If ret_ents=True it will return a list with the created entities or an empty list if no entities were created.

	"""

def SplitNodes():

	"""

	This function splits shells similarly to the SPLIT function with nodes selected.
	It accepts no arguments, quads are split to form two triangles and triangles are
	split to form three other triangles.


	@returns integer: Always returns 1.

	"""

def SplitPolys():

	"""

	This function splits polygons to triangles. The new triangles are assigned the
	same property with the polygon, or a new default property, if the polygon is 
	a polyhedral face with no property. Shells are also created to the feature lines 
	between properties. The function accepts no arguments.


	@returns integer: Always returns 1.

	"""

def TetraCFD(volume):

	"""

	The function generates tetra volume meshing of defined Volumes using the Tetra CFD algorithm.


	@volume object: (optional)The volume to be meshed.
	If it is not given, all volumes will be meshed.

	@returns integer: Returns 0 on success, non-zero on failure.

	"""

def TetraCFDbyID(Vol_ID):

	"""
	Deprecated since version 18.0.0. Use function TetraCFD instead.

	The function generates tetra volume meshing to a Volume defined by its id, using the Tetra CFD algorithm.


	@Vol_ID integer: The volume id.

	@returns integer: Returns 0 on success, non-zero on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 18.0.0. Use function TetraCFD instead.", DeprecationWarning)

def TetraFEM(volume):

	"""

	Script function for tetra volume meshing of defined Volumes using the Tetra FEM algorithm.


	@volume object: (optional)The volume to be meshed.
	If it is not given, all volumes will be meshed.

	@returns integer: Returns 0 on success, non-zero on failure.

	"""

def TetraFEMbyID(VOL_ID):

	"""

	Script function for tetra volume meshing, defining it by its id, using the Tetra FEM algorithm.


	@VOL_ID integer: The volume id.

	@returns integer: Returns 0 on success, non-zero on failure.

	"""

def UnmeshedMacros():

	"""

	This function hides all the meshed macros and leaves only the unmeshed ones visible.
	It has the exact same effect as the UNMESHED>MACROs button on the FOCUS menu.


	@returns integer: Returns the number of the unmeshed macros.

	"""

def UnmeshedVolumes(return_volumes):

	"""

	This function hides all the meshed volumes and leaves only the unmeshed ones visible.
	It has the exact same effect as the UNMESHED>VOLUMEs button of the FOCUS menu.


	@return_volumes object: (optional)If True then it returns an array with the unmeshed volume entities found

	@returns integer: Returns 0 if no unmeshed volumes are found and 1 if there is any unmeshed volumes.

	"""

def VolumeType(volume):

	"""

	This function returns the type of a given volume, the values of which can be "Undefined", "Translate", 
	"Rotate", "Offset", "Glide", "Sweep", "Dual Sweep", "Tetra FEM", "Tetra CFD", "Hexa Interior", "Tetra rapid", 
	"Layers", "Tetra Rapid", "Map Thin", "Map" or "HexaPoly".


	@volume object: The volume object to get its type.

	@returns string: Returns the type of the volume on success and blank otherwise.

	"""

def VolumesDelete(volume):

	"""

	This function deletes a given volume or an array of volumes.


	@volume object: A reference to the volume entity to be deleted or an array of volumes.

	@returns integer: Returns 1 on success and 0 otherwise.

	"""

def VolumesDetect(method_option, return_volumes, include_facets, whole_db):

	"""

	This function can be used in order to detect volumes. The model must be already surface meshed.


	@method_option integer: (optional)A number that corresponds to the detection method.
	Its value can be:
	1: Detects all valid volumes and their sub-volumes.
	2: Detects volumes independantly from their sub_volumes.
	3: Detects volumes independantly from their sub_volumes neglecting any zero-
	   thickness walls.
	(Default: 1)

	@return_volumes boolean: (optional)Determines if the function will return a list with the detected volumes 
	or the number of the detected volumes.

	@include_facets boolean: (optional)If set to True, free solid facets will also be included in the volume detection.

	@whole_db boolean: (optional)If set to True, it will search for volumes in the entire model, 
	otherwise it will work on visible.

	@returns object: Returns the number of volumes that have been detected, if the argument 'return_volumes' is ommited or set to False.
	Otherwise it returns a list with the detected volumes.

	"""

def VolumesErase(volume):

	"""

	This function erases the volume mesh of a given meshed volume or an array of volumes.


	@volume: A reference to the volume entity or an array of volumes.

	@returns integer: Returns 1 on success and 0 otherwise.

	"""

def VolumesMap(master, slave, round, method, steps, part, prop, ret_ents, light_volume_representation):

	"""

	This function can be used in order to define and mesh a "Map" volume.


	@master object: A list of shell objects that define the master area.

	@slave object: A list of shell objects that define the slave area.

	@round object: A list of shell objects that define the side area.

	@method string: (optional)The method used for the solid elements calculation, whose values 
	can be "Normal parts" or "Thin parts".

	@steps integer: (optional)The number of the solid steps that will be created along the round area.

	@part string: (optional)The part that will be assigned to the created volume.

	@prop string: (optional)The property that will be assigned to the created volume.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@light_volume_representation boolean: (optional)If set to True, the created volume will be of light volume representation.

	@returns object: Returns 1 on success or 0 on failure.
	If ret_ents=True it will return a list with the created entities,
	or None if no entities are created.

	"""

def VolumesMeshV(volume, mesh_type):

	"""

	This function can be used in order to automatically mesh an already defined volume or an array of volumes.


	@volume object: The volume to be meshed or an array of volumes

	@mesh_type string: Corresponds to the mesh generator.
	The string values for each mesh type can be:
	"TETRA RAPID", "TETRA FEM", "TETRA CFD", 
	"HEXA INTERIOR" or "HEXAPOLY".

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def VolumesOffset(boundary_array, dist, steps, middle, bias, factor, part, property):

	"""

	This function can be used in order to generate a volume by offsetting a shell mesh 
	along a direction specified by the normal vector of the elements.


	@boundary_array object: A list of ANSA entities that will be used as the base from which solid elements 
	will be generated via offsetting.
	This list may contain:
	-FACEs.
	-Released SHELL elements that do not belong in a FACE.

	@dist float: The offset length. Use a negative number to offset to the opposite direction.

	@steps integer: The number of generated elements along the offset direction.

	@middle integer: Defines the offset mode:
	-0: Offset normally towards positive direction.
	-1: Offset towards both directions, by splitting distance and 
	    steps for each direction.

	@bias string: Define biasing in the distribution of generated elements along the offset direction.
	Possible values are:
	-'Linear'
	-'Exponential'
	-'Bell Curve'
	-'No Biasing'

	@factor float: Factor to be used by the offset method defined in the 'bias' argument.

	@part object: (optional)The part where the entities will be placed in.
	If absent, the current part will be used.

	@property object: (optional)The property where the generated solid elements will refer to.
	If absent, a new one will be created.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def VolumesParameters(growth_rate, max_length, criterion_type, criterion_val, geometry_checks):

	"""

	This function specifies the volume meshing parameters as they appear in the 
	MESH>VOLUMEs>PARAM window.


	@growth_rate float: The maximum growth rate.

	@max_length float: The maximum element length.

	@criterion_type string: Containing the criterion definition.
	The values of this argument can be:
	-"NASTRAN Aspect"
	-"FLUENT Aspect"
	-"I-DEAS Stretch"
	-"ABAQUS Shape Factor"
	-"FLUENT Skewness"

	@criterion_val float: The criterion value.

	@geometry_checks boolean: Defines if geometry checks will be performed or not.

	@returns integer: Returns 1 if the values are properly assigned and 0 otherwise.

	"""

def VolumesRemesh(ENTITY):

	"""

	This function can be used in order to automatically mesh an already defined volume or an array of volumes.


	@ENTITY object: The volume object to be meshed or an array of volumes

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def VolumesRotate(boundary_array, x, y, z, dx, dy, dz, angle, steps, bias, factor, part, property):

	"""

	This function can be used in order to generate a volume by rotating a predefined shell mesh around an axis.


	@boundary_array object: A list of shell objects.

	@x float: The x coordinate of the origin point.

	@y float: The y coordinate of the origin point.

	@z float: The z coordinate of the origin point.

	@dx float: The x component of the rotational vector.

	@dy float: The y component of the rotational vector.

	@dz float: The z component of the rotational vector.

	@angle float: The rotational angle.

	@steps integer: The number of the generated elements.

	@bias string: One of "Linear", "Exponential", "Bell Curve" or "No Biasing".

	@factor float: The biasing factor.

	@part object: (optional)The reference of the part where the volume will belong.

	@property object: (optional)The reference of the property that will be assigned.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def VolumesTranslate(boundary_array, dx, dy, dz, dist, steps, bias, factor, part, property):

	"""

	This function can be used in order to generate a volume by translating a predefined shell mesh along a direction specified by a vector.


	@boundary_array object: A list of shell objects to be translated.

	@dx float: The x component of the translational vector.

	@dy float: The y component of the translational vector.

	@dz float: The z component of the translational vector.

	@dist float: The translational distance.

	@steps integer: The number of generated element steps.

	@bias string: One of "Linear", "Exponential", "Bell Curve" or "No Biasing".

	@factor float: The biasing factor.

	@part string: (optional)The part name.

	@property integer: (optional)The property id.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def Volumize(entities, solid_layers, paste_tol, merge_distance, offset_mode, sharp_edges_angle, thickness_factor, thickness_averaging, delete_original_shells, refine_single_bounds, max_aspect):

	"""

	Applies volumize function on shells.


	@entities object: A list of shell objects. If None it will run on all visible shells.

	@solid_layers integer: If '0', the function will not create any solids inside the volumize result.
	Any other number specifies the number of layers of solids inside the volumize result.

	@paste_tol float: Will paste the volumize edges where the initial model had single edges and thickness 
	under paste_tol value.

	@merge_distance float: The function will collide flanges within this tolerance.

	@offset_mode integer: if 1, volumize will be implemented towards the 'grey' side of the source shells.
	if -1, volumize will be implemented towards the 'yellow' side of the source shells.
	if 0 volumize will be implemented towards both sides of the source shells.

	@sharp_edges_angle float: (optional)The cut-off angle that limits the movement of nodes on sharp edges.

	@thickness_factor float: (optional)Apply this factor in thickness of result entities.

	@thickness_averaging string: (optional)If "Keep average", the average offset of node-neighboring entities is used.
	If "Keep maximum", the maximum offset of node-neighboring entities is used.
	If "Keep minimum", the minimum offset of node-neighboring entities is used.

	@delete_original_shells boolean: (optional)Decides whether original shells are deleted or not.

	@refine_single_bounds boolean: (optional)Decides whether refinement of single bounds is enabled.

	@max_aspect float: (optional)The maximum aspect for "Refine single bounds".

	@returns object: Returns 0 if for any reason volumizing failed.
	Returns a list containing all volumized elements if volumizing succeeded.

	"""

def Wrap(input_data, tolerance, volume_type, wrap_style, wrap_style_argument, separate_sets_flags, separate_sets_angle, counter_volumes, part_name, property_id):

	"""

	Creates a wrap mesh for the user data.


	@input_data object: A list with objects of input data of the wrap. The object can be shell, solid, 
	face, property shell, property solid, volume, set, include, part or group.

	@tolerance float: The value of tolerance for the wrap function.

	@volume_type string: Defines the type of volume. That string takes two values "in" or "out".

	@wrap_style string: Defines the style of the wrap. That string takes two values "tight" or "smooth".

	@wrap_style_argument float: For the wrap style "tight" the value must be float while for the wrap style 
	"smooth" it must be integer.

	@separate_sets_flags string: Defines the creation of separate sets, (set "yes" or "no" to enable or not).

	@separate_sets_angle float: The value of angle for the creation of separate sets.

	@counter_volumes integer: The number of volumes to be created. If it is negative or bigger
	than the number of detected volumes, the wrap function will be applied on all 
	detected volumes. If the value is positive and smaller than the number of detected
	volumes, the wrap function will be applied on the specified number of volumes
	in descending order.

	@part_name string: The 'module Id' of part/group. If the string is empty (e. ""),
	the function creates a default part to place the results of the wrap.

	@property_id integer: The value of the 'property Id'. If the value is equal to zero or negative, the
	function creates one default property to place the results of the wrap.

	@returns object: Returns a list with the results of the wrap. 
	The list contains two lists. The list in position '0' has the lists
	of elements for each volume. The list in position '1' is created, if the user
	set argument 'separate_sets_flags' equal to "yes" and the values of
	that are the sets for each volume. The two above lists have the same number of
	data which is equal to the number of volumes specified from the user. Also,  
	there is one to one correspondence between them. Thus, the 'elements' and 'sets'
	of volume 'i' are located in position 'i' of the above lists. In these positions 'i'
	the entities are lists of 'elements' and 'sets' for volume 'i'.

	"""

def xyzIsInsideVolume(x, y, z, return_all_volumes):

	"""

	This function takes as arguments the coordinates of a point and checks whether this
	point is inside a defined volume, and if yes in which.


	@x float: The x coordinate of the point.

	@y float: The y coordinate of the point.

	@z float: The z coordinate of the point.

	@return_all_volumes boolean: (optional)If set to True, the function returns a list with all the volumes 
	the point belongs to.

	@returns object: If the argument "return_all_volumes" is omitted or is set to False, the function 
	returns the id of the smaller volume the point belongs to or 0 if no volume found. 
	If the optional argument is set to True, then a list with all the volumes the point 
	belongs to is returned. In case the point is not inside a defined volume, None is returned.

	"""

def xyzIsInsideVolumeMatrix(points_coordinates, return_all_volumes, input_vols):

	"""

	This function takes as argument a matrix with the coordinates of points and checks 
	whether these points are inside a defined volume, and if yes in which volume.


	@points_coordinates object: A list with lists defining points.

	@return_all_volumes boolean: (optional)If set to True, the function will return a list containing a list for 
	every xyz point with all the volumes it belongs to.

	@input_vols object: (optional)Array of volumes on which to perform the check. If nothing is provided then the entire db is checked

	@returns object: Returns a list of integers where each of them corresponds to the given points. The value can be
	either greater than 0, in case the given point is inside a defined volume and corresponds to the id 
	of the volume, or 0, in case the point is not inside any defined volume.
	If the argument "return_all_volumes" is set to True, then it will return a list for each point 
	containing all the volumes the point belongs to.

	"""

def CreateBestMesh():

	"""

	This function meshes the Macros with all the algorithms and keeps only the mesh with the 
	best quality according to QCHECK Skewness. The function works only on visible macros.


	@returns integer: Returns 0 in any case.

	"""

def CreateCfdMesh():

	"""

	This function incorporates an advanced meshing algorithm tailored made to meet CFD specs 
	or other application areas where a variable size mesh is required. The algorithm meshes 
	with variable element length depending on the local curvature of the underlying CAD surface, 
	under tight user-controlled specifications.
	The function works only on visible macros.


	@returns integer: Returns 0 in all cases.

	"""

def CreateFreeMesh():

	"""

	This function meshes using the free algorithm. This algorithm generates as few 
	elements as possible, trying to maintain the best quality possible.
	The function works only on visible macros.


	@returns integer: Returns 0 in all cases.

	"""

def CreateGradualMesh():

	"""

	This function incorporates a meshing algorithm, which generates more elements 
	and its goal is to give better results to Macro Areas with uneven nodal 
	distributions that require a gradual transition of the element size.
	The function works only on visible macros.


	@returns integer: Returns 0 in all cases.

	"""

def CreateMapMesh():

	"""

	This function incorporates a meshing algorithm, which generates a structured 
	mesh close to quadrilateral shaped Macro Areas.
	The function works only on visible macros.


	@returns integer: Returns 0 in all cases.

	"""

def CreateSpotMesh():

	"""

	This function incorporates a meshing algorithm, which generates more elements than the free 
	algorithm and brings better results to Macros that have Weld or Connecting Spots on them.
	The function works only on visible macros.


	@returns integer: Returns 0 in all cases.

	"""

def CreateStlMesh():

	"""

	This function meshes using the STL algorithm. This algorithm can be used for applications where 
	the quality of the elements is not very important but the exact geometry representation is.
	The function works only on visible macros.


	@returns integer: Returns 0 in all cases.

	"""

def CreateAdvFrontMesh():

	"""

	The algorithm of this function generates shell elements starting from the boundaries of the Macro Areas.
	As a result the mesh follows the shape of the Perimeter Segments.
	The function works only on visible macros.


	@returns integer: Returns 0 in all cases.

	"""

def NumberPerimeters(input, number, apply_multiple_number, remesh_macros, apply_number_of, use_ansa_defaults_values):

	"""

	This function defines a new number of edges (or nodes) on Macro Area's perimeter segments, FE perimeters or Hexa Box Edges.


	@input object: Can be an entity or a list of entities, parts, properties, materials, 
	sets, macros, CONS, hexa box faces or hexa box edges.
	If the input is 0, visible CONS and hexa box edges are collected.

	@number string: A string which can either be equal to a number (eg. "3"), or an expression 
	to add or remove nodes (eg. "+2", "-3", "*2").

	@apply_multiple_number boolean: (optional)If set to True, the function creates chains of connected Perimeters 
	(or hexa box edges) and distributes accordingly the given number 
	to the chains. If deactivated (False) or missing, then all the entities will 
	get the same number.

	@remesh_macros boolean: (optional)If set to True, the function remeshes the affected macros (or hexa box faces) 
	after applying the number. If missing (False) then the current gui value 
	will be used.

	@apply_number_of string: (optional)It takes the values "edges" or "nodes", and it applies as INPUT as a 
	number of edges or nodes. If missing then the current gui value will be used.

	@use_ansa_defaults_values boolean: (optional)If set to True, the function uses parameters from ANSA.defaults, by-passing all other arguments.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def GetCompareWorkingDirectory():

	"""

	The function returns the path to the defined working directory of the Compare Tool.


	@returns string: Returns a string containing the path of the working directory of the Compare Tool.

	"""

def SetCompareWorkingDirectory(path):

	"""

	The function sets the path of the working directory of the Compare Tool.


	@path string: The path of the working directory.

	@returns integer: Returns 1 if a valid path is given, 0 otherwise.

	"""

def VolumizeComposites(deck, entities, delete_original_shells, stacking, fill_ply_drop_offs, ret_ents, create, merge_method, merge_t_tol, merge_theta_tol, drop_off_prop, force_split_woven_layers, avoid_hanging_edges, ret_all, rows_num):

	"""

	This function creates composite solids (SOLID_LAMINATE) from composite shells (PCOMP or LAMINATE).


	@deck constant: One of NASTRAN, ABAQUS or ANSYS.

	@entities object: A list of composite shells, properties, sets or parts containing 
	composite shells

	@delete_original_shells boolean: (optional)A flag for deleting original shells.

	@stacking string: (optional)One of "single element" or "per ply".

	@fill_ply_drop_offs boolean: (optional)A flag for filling ply drop-offs.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@create string: (optional)One of "thick_shells" or "solids".

	@merge_method string: (optional)The method by which the layers of different properties will be merged.
	One of "by_tolerances", "by_gplyid", "by_layer_name".
	Required only for multiple properties and stacking = "per ply".

	@merge_t_tol float: (optional)The thickness tolerance by which the layers of different properties
	will be merged. Required for merge_method = "by_tolerances".

	@merge_theta_tol float: (optional)The theta tolerance by which the layers of different properties
	will be merged. Required for merge_method = "by_tolerances".

	@drop_off_prop object: (optional)The simple solid property of the ply drop-offs. If not given and 
	fill_ply_drop_offs is True, then a default solid property is created.

	@force_split_woven_layers boolean: (optional)If True, woven layers are split.
	If False, woven layers are not split, except from SOLID_LAMINATE
	in LSDYNA, PAMCRASH, RADIOSS and PERMAS.

	@avoid_hanging_edges boolean: (optional)When stacking is "per ply" and fill_ply_drop_offs is True,
	avoid hanging edges by creating pyramids (drop-off elements)
	and by splitting hexas to pentas (layer elements).

	@ret_all object: (optional)If True the function returns a numedtuple with all the available data.
	(Default: False)

	@rows_num integer: (optional)Number of rows per layer that will be created.

	@returns object: Returns 0 on success.
	If ret_ents=True it will return a list with the created entities, 
	or None if no entities are created.
	
	If ret_all=True it will return a namedtuple 'ret' with the following members:
	ret.created_elements: a list of the created elements
	ret.property_pairs: a list of tuples: (original shell property, created thick shell or solid property)

	"""

def IntersectSolidDescription(input, fuse_distance, inflate_distance, ignore_same_pid, ignore_same_part, ignore_same_set, ignore_same_neighour_zones, keep_separation_walls, create_pid_for_separation_walls, improve_mesh_quality):

	"""

	This function intersects FE shells and identifies inner and outer walls,


	@input object: A single object or a list of parts, properties, materials or sets.
	If input equals to 0, the visible shells are collected.

	@fuse_distance float: (optional)See tooltip at MESH>SHELL_MESH>INTERSECT>Solid description wizard.

	@inflate_distance float: (optional)See tooltip at MESH>SHELL_MESH>INTERSECT>Solid description wizard.

	@ignore_same_pid boolean: (optional)If set to True, ignores intersections within the same property.

	@ignore_same_part boolean: (optional)If set to True, ignores intersections within the same part.

	@ignore_same_set boolean: (optional)If set to True, ignores intersections within the same set.

	@ignore_same_neighour_zones integer: (optional)If set to True, ignores intersection between shells that are 
	within n zones from each other.

	@keep_separation_walls boolean: (optional)If set to True, keeps primary inner walls.

	@create_pid_for_separation_walls boolean: (optional)If set to True, creates pids for primary inner walls.

	@improve_mesh_quality boolean: (optional)If set to True, improves the mesh quality in 1 zone around 
	the intersected shells.

	@returns integer: Always returns 1.

	"""

def IntersectSkinDescription(input, fuse_distance, ignore_same_pid, ignore_same_part, ignore_same_set, ignore_same_neighour_zones, improve_mesh_quality):

	"""

	This function intersects FE shells,


	@input object: An single object or a list of parts, properties, materials or sets.
	If input equals to 0, the visible shells are collected.

	@fuse_distance float: (optional)See tooltip at MESH>SHELL_MESH>INTERSECT>Solid description wizard.

	@ignore_same_pid boolean: (optional)If set to True, ignores intersections within the same property.

	@ignore_same_part boolean: (optional)If set to True, ignores intersections within the same part.

	@ignore_same_set boolean: (optional)If set to True, ignores intersections within the same set.

	@ignore_same_neighour_zones integer: (optional)If set to True, ignores intersection between shells that are 
	within n zones from each other.

	@improve_mesh_quality boolean: (optional)If set to True, improves the mesh quality in 1 zone around 
	the intersected shells.

	@returns integer: Always returns 1.

	"""

def FillGapCoons(input, alternative, improve_result_zones, result_set_id, ret_ents):

	"""

	This function creates FE shells to fill a gap defined by cons, curves or edges.
	Each call of the function fills a single gap.


	@input object: A list of cons, curves or sets of edges.

	@alternative boolean: (optional)Fills with alternative option on, if available.

	@improve_result_zones integer: (optional)Improves the quality of the result FE shells and [user defined] zones 
	around them.

	@result_set_id integer: (optional)Adds the result FE shells to a set with [user defined] id.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@returns integer: Returns the number of the created FE shells (before mesh improvement).
	If ret_ents=True it will return a list with the created entities or None if no entities are created.

	"""

def FillGapDraft(input, alternative, improve_result_zones, result_set_id, ret_ents):

	"""

	This function creates FE shells to fill a gap defined by cons, curves or edges.
	Each call of the function fills a single gap.


	@input object: A list of cons, curves, sets of edges.

	@alternative boolean: (optional)Fills with alternative option on, if available.

	@improve_result_zones integer: (optional)Improves the quality of the result FE shells and [user defined] zones 
	around them.

	@result_set_id integer: (optional)Adds the result FE shells to a set with [user defined] id.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@returns integer: Returns the number of the created FE shells (before mesh improvement).
	If ret_ents=True it will return a list with the created entities or None if no entities are created.

	"""

def HexaBoxSweepGlide(extrusion_type, guideline_ents, box_face, curves, points, section_type, radius, width, dx, dy, dz, height, lower_base, upper_base):

	"""

	Function for creating a hexa box through extrusion. Both 'sweep' and 'glide' extrusion types are supported. 
	
	The direction of the extrusion is defined through curves, or points, or a combination of them. 
	Curves may form a connected or disconnected path (a path will be automatically created). 
	Note that single points are ignored (i.e. if any points are to be used, they should be at least two).
	
	The user has four options in defining the cross section, one with a box face, one with curves, 
	one with curves and points and, finally, one with a predefined shape.
	The box_face option expects a single box face entity (which will be pasted to the new one after creation of the box). 
	The curves option expects one or more curves (unconnected ones will be automatically connected 
	to form a closed cross section shape). The selected curves should contain at least 4 points, 
	so that they can be adopted for the definition of the four box edges.
	The points option should only follow a previous curves-curve_entities pair, and explicitly 
	defines the points to be used for the four box edges definition. These points should be 
	part of the curve_entities provided. 
	The predefined cross section includes a circular with the required radius, a square with 
	its side length, a rectangular with its width and height, and a trapezoidal with its two 
	bases' lenths and height. Except for the circular, these cross sections also require a 
	vector defining the 'height' direction of the cross section.
	Note that several kind of edges may be used as a curve, including element edges 
	(provided as edge sets), CONS, 3D curves and box edges. Similarly, grids, hot points 
	and box edge corner points may be employed for any point entities.


	@extrusion_type string: The keyword "sweep" or "glide", denoting the type of the extrusion.

	@guideline_ents object: A list of entities defining the direction of the extrusion.
	(Collection of curves and/or points)

	@box_face object: (optional)A box face entity to be used as a cross section.
	(Note that new face will be pasted to the old)

	@curves object: (optional)Curve entities defining the  cross section.
	(They do not have to form a closed perimeter)

	@points object: (optional)Point entities defining the position of the box edges (used only in 
	conjunction with 'curves'). Note that points should be among the 
	points of the curve_entities provided above.

	@section_type string: (optional)A string specifying the predefined section type ("circular", "square", 
	"rectangular", trapezoidal"). Additional data needed per case:
	-"circular" requires "radius".
	-"square" requires "width" and  height direction "dx","dy","dz".
	-"rectangular" requires "width", "height", and height direction "dx","dy","dz".
	-"trapezoidal" requires "lower_base", "upper_base", "height", and height 
	  direction "dx","dy","dz".

	@radius float: (optional)In case of "circular" section_type, the radius of the cross section.

	@width float: (optional)In case of "square" section_type, the width of the cross section.

	@dx float: (optional)In case of "square", "rectangular" or "trapezoidal" section_type, 
	the x-component of the vector defining the section's height direction.
	(Does not need to be normalized)

	@dy float: (optional)In case of "square", "rectangular" or "trapezoidal" section_type, 
	the y-component of the vector defining the section's height direction.
	(Does not need to be normalized)

	@dz float: (optional)In case of "square", "rectangular" or "trapezoidal" section_type, 
	the z-component of the vector defining the section's height direction.
	(Does not need to be normalized)

	@height float: (optional)In case of "rectangular" or "trapezoidal" section_type, the height 
	of the cross section.

	@lower_base float: (optional)In case of "trapezoidal" section_type, the length of the sections' lower base.

	@upper_base float: (optional)In case of "trapezoidal" section_type, the length of the sections' upper base.

	@returns object: Returns a reference to the newly created Hexablock boxes objects.

	"""

def VoxelGeneration(shells_or_faces, voxel_len, allow_surface_intersection, nth_largest, ret_ents, different_properties_per_volume, smooth_iterations, mesh_method, sharp_angle, coordinate_sys_id, coordinate_sys_auto):

	"""

	Creates a mesh around or inside a solid description of faces or shells.


	@shells_or_faces object: A list of faces/shells. If set to "visible" then it runs for all 
	the visible faces/shells of the database.

	@voxel_len float: The length of the created voxels (> 0).

	@allow_surface_intersection boolean: (optional)Set to True, to capture the volume around the solid description.
	Set to False, to capture the volume on the interior.

	@nth_largest integer: (optional)Create the nth largest volumes that will be detected.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@different_properties_per_volume boolean: (optional)If set to True, the algorithm will see existing ANSA volumes and 
	will create separate properties per volume for the result .

	@smooth_iterations integer: (optional)The number of iterations for hexas smoothing. This option is used only in "Free" mesh method.

	@mesh_method string: (optional)Defines the method for the mesh generation.
	Available options are "Free" and "Snap".
	- "Free" creates a smooth voxel mesh.
	- "Snap" creates a voxel mesh that will be snapped to the model.
	Default option is "Free"

	@sharp_angle float: (optional)Sharp angle defines a limit for the angle between two adjacent shells above which their common edge will be identified as sharp and the mesh will try to capture it. This option is used only in "Snap" mesh method.
	Set to 0 to deactivate it.
	Default value is 0.

	@coordinate_sys object: (optional)Coordinate system entity (CS) to align voxel mesh to.
	If value 'auto' is set, the voxel mesh will be alligned to an automatically calculated coordinate system.
	By default it is deactivated and global CS will be used.

	@returns integer: Returns 1 on success or 0 on failure.
	If ret_ents=True it will return a list with the created entities, 
	or None if no entities are created.

	"""

def RemeshShells(shells, mesh_generator):

	"""

	This function runs mesh generators on shells.
	It uses mesh parameters to get critiria like mesh type and order of mesh.
	Also It seperates input shells to different areas according to geometry 
	masegments or feature lines if shells are fe.


	@shells object: A list of shell objects or a string with value 'visible'.
	If it is called with 'visible' it works for all the visible shell elements.

	@mesh_generator string: The mesh generator to run.
	Options are "CFD", "ADVFRNT", "FREE", "SPOT" or "GRADUAL".

	@returns object: Returns a list containing references to all the new shell objects.

	"""

def PerimetersOfMacro(faces):

	"""

	The function collects all the Perimeters of a macro. If a face that it not a macro is 
	provided, the function returns the perimeters of its macro.


	@faces object: A list of faces, parts or properties.

	@returns object: Returns a list with the collected Perimeters, or 0 on failure.

	"""

def FillGapFitted(input, improve_result_zones, result_set_id, ret_ents):

	"""

	This function creates FE shells to fill a gap defined by cons, curves or edges.
	Each call of the function fills a single gap.


	@input object: A list of cons, curves or sets of edges.

	@improve_result_zones integer: (optional)Improves the quality of the result FE shells and [user defined] zones 
	around them.

	@result_set_id integer: (optional)Adds the result FE shells to a set with [user defined] id.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@returns integer: Returns the number of the created FE shells (before mesh improvement).
	If ret_ents=True it will return a list with the created entities or None if no entities are created.

	"""

def FillGapPlanar(input, improve_result_zones, result_set_id, ret_ents):

	"""

	This function creates FE shells to fill a gap defined by cons, curves or edges.
	Each call of the function fills a single gap.


	@input object: A list of cons, curves or sets of edges.

	@improve_result_zones integer: (optional)Improves the quality of the result FE shells and [user defined] zones 
	around them.

	@result_set_id integer: (optional)Adds the result FE shells to a set with [user defined] id.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@returns integer: Returns the number of the created FE shells (before mesh improvement).
	If ret_ents=True it will return a list with the created entities or None if no entities are created.

	"""

def ReconstructViolatingShells(expand_level):

	"""

	The function perfrorms Reconstruct on violating shells.


	@expand_level integer: (optional)The number of zones around violating shells.
	(Default: 0)

	@returns integer: Returns 0 in all cases.

	"""

def ReshapeViolatingShells(expand_level):

	"""

	The function perfrorms Reshape on violating shells.


	@expand_level integer: (optional)The number of zones around violating shells.
	(Default: 0)

	@returns integer: Returns 0 in all cases.

	"""

def FillSingleBoundHoles(max_diameter, fill_ext_perim, point_at_center, connection_by, curve_at_perimeter, reshape_zones, set_id, pid_id, ret_ents, fill_method, part, geom_fill_method):

	"""

	This function identifies and fills single bound holes with FE shells or faces.
	Works on visible shells and macros.


	@max_diameter float: The maximum diameter of the holes that will be filled.

	@fill_ext_perim boolean: Fill the largest perimeter of each connectivity group.

	@point_at_center boolean: (optional)Create points at hole centers.

	@connection_by string: (optional)Create connection points at hole centers. Can be "PID" or "Module_ID".

	@curve_at_perimeter boolean: (optional)Create curves at hole perimeters.

	@reshape_zones integer: (optional)Defines the zones of shells around the holes that will be reshaped.

	@set_id object: (optional)Adds the new shells/faces to a set. If None, a new set will be created by ANSA.

	@pid_id object: (optional)Adds the new shells/faces to a pid. If None, a new pid will be created by ANSA.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@fill_method string: (optional)Defines the triangulation method for FE holes. Can be "draft", "planar" or "bridge".
	(Default: "draft")

	@part object: (optional)Adds the new shells/faces to a part.

	@geom_fill_method string: (optional)Defines the fill method for geom holes.
	Can be "draft", "planar", "create_new_faces" or "expand_existing_faces".
	(Default: "create_new_faces")

	@returns integer: Returns 1 on success and 0 on failure.
	If ret_ents=True it will return a list with the created entities, 
	or None if no entities are created.

	"""

def FillSingleBoundConcavities(max_width, point_at_center, curve_at_perimeter, reshape_zones, set_id, pid_id, ret_ents, part):

	"""

	This function identifies and fills concavities along single bound perimeters.
	Works on visible FE shells and meshed macros.


	@max_width float: The maximum width of the concavities that will be filled.

	@point_at_center boolean: (optional)Create points at concavity centers.

	@curve_at_perimeter boolean: (optional)Create curves at concavity perimeters.

	@reshape_zones integer: (optional)Defines the zones of shells around the filled concavities that will be reshaped.

	@set_id object: (optional)Adds the new shells to a set. If None, a new set will be created by ANSA.

	@pid_id object: (optional)Adds the new shells to a pid. If None, a new pid will be created by ANSA.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@part object: (optional)Adds the new shells to a part.

	@returns object: Returns 1 on success and 0 on failure.
	If ret_ents=True it will return a list with the created entities, 
	or None if no entities are created.

	"""

def FillSolidHoles(max_diameter, feat_angle, feat_type, max_distortion, point_at_center, curve_at_perimeter, reshape_zones, set_id, pid_id, ret_ents, fill_method, part, solids_set, solids_pid, solids_part, geom_fill_method):

	"""

	This function identifies and fills tubes and blind concavities. Works on visible shells and solids.


	@max_diameter float: The maximum diameter of the solid holes that will be filled.

	@feat_angle float: Defines the feature line angle.

	@feat_type string: Defines the type of features that will be identified.
	Can be "convex" or "concave".

	@max_distortion float: The maximum allowed distance between perimeter nodes and the hole's mid plane, 
	given as a percentage of the hole's diameter.

	@point_at_center boolean: (optional)Create points at hole centers.

	@curve_at_perimeter boolean: (optional)Create curves at hole perimeters.

	@reshape_zones integer: (optional)Defines the zones of shells around the holes that will be reshaped.

	@set_id object: (optional)Adds the new shells/faces to a set. If None, a new set will be created by ANSA.

	@pid_id object: (optional)Adds the new shells/faces to a pid. If None, a new pid will be created by ANSA.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@fill_method string: (optional)Defines the triangulation method for FE holes. Can be "draft" or "planar".
	(Default: "draft")

	@part object: (optional)Adds the new shells/faces to a part.

	@solids_set object: (optional)Adds the new solids to a set.

	@solids_pid object: (optional)Adds the new solids to a pid.

	@solids_part object: (optional)Adds the new solids to a part.

	@geom_fill_method string: (optional)Defines the fill method for geom holes.
	Can be "draft", "planar", "create_new_faces" or "expand_existing_faces".
	(Default: "create_new_faces")

	@returns integer: Rreturns 1 on success and 0 on failure.
	If ret_ents=True it will return a list with the created entities, 
	or None if no entities are created.

	"""

def FillFeatureLineHoles(max_diameter, feat_angle, feat_type, max_distortion, detach_triple_perimeters, point_at_center, curve_at_perimeter, reshape_zones, set_id, pid_id, ret_ents, fill_method, part, allow_intersecting_result_shells ):

	"""

	This function identifies and fills feature line holes. Works on visible FE shells and meshed macros.


	@max_diameter float: The maximum diameter of the solid holes that will be filled.

	@feat_angle float: Defines the feature line angle.

	@feat_type string: Defines the type of features that will be identified.
	Can be "convex" or "concave".

	@max_distortion float: The maximum allowed distance between perimeter nodes and the 
	hole's mid plane, given as a percentage of the hole's diameter.

	@detach_triple_perimeters boolean: (optional)Detaches triple bounds at hole perimeters, to create a manifold result mesh.

	@point_at_center boolean: (optional)Create points at hole centers.

	@curve_at_perimeter boolean: (optional)Create curves at hole perimeters.

	@reshape_zones integer: (optional)Defines the zones of shells around the holes that will be reshaped.

	@set_id object: (optional)Adds the new shells to a set. If None, a new set will be created by ANSA.

	@pid_id object: (optional)Adds the new shells to a pid. If None, a new pid will be created by ANSA.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@fill_method string: (optional)Defines the triangulation method. Can be "draft" or "planar".
	(Default: "draft")

	@part object: (optional)Adds the new shells to a part.

	@allow_intersecting_result_shells boolean: (optional)Option to allow intersections between the created shells and the existing shells/faces.

	@returns integer: Returns 1 on success and 0 on failure.
	If ret_ents=True it will return a list with the created entities, 
	or None if no entities are created.

	"""

def SuppressFeatureLines(feature_angle_limit, max_dist_from_prev_pos, shells):

	"""

	SuppressFeatureLines performs suppress on the visible model.


	@feature_angle_limit float: The maximum feature angle allowed after suppress has taken place.

	@max_dist_from_prev_pos float: The maximum node from the node's previous position.

	@shells object: (optional)The shells on which the function will work. Can be an object, a list of objects, parts, properties, materials, sets or macros. If this argument is ommitted the function is performed on the visible shells

	@returns integer: Returns 0 in all cases.

	"""

def ReduceMesh( shells, reduce_percentage, distortion, maximum_length, maximum_aspect, distortion_angle ):

	"""

	Reduces the number of elements by a distortion value.


	@shells object: A list of shell entities. Set 0 to work on visible.

	@reduce_percentage float: Maximum percentage of shells number to reduce.

	@distortion float: The distortion value.

	@maximum_length float: (optional)Maximum allowed element length.

	@maximum_aspect float: (optional)Maximum allowed element aspect.

	@distortion_angle float: (optional)The distortion angle value.

	@returns integer: Returns 1 on success.

	"""

def AssociateBoxEdgesToEdges(box_edges, target_edges, connect_to_cons, remove_points, box_edge_points):

	"""

	Script function to associate box edges to target feature lines (curves, cons, shell edges).
	


	@box_edges object: A box edge or a list of box edges to be associated with the target entities.

	@target_edges object: An entity or a list of entities, parts or sets corresponding 
	to the target feature lines.

	@connect_to_cons boolean: (optional)If set to True,  connect the nodes of the box edges to the associated Cons, 
	after meshing the boxes.

	@remove_points boolean: (optional)Remove the existing control points from the box edges.

	@box_edge_points object: (optional)A dictionary to define the number of points per box edge.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def AssociateBoxEdgesToSurfs(box_edges, surface_ents, user_projection_mode_vector, remove_points, box_edge_points, cut_geometric_faces, connect_to_cons):

	"""

	Script function to associate box edges to target surface entities (shells, geometrical faces).


	@box_edges object: A box edge or a list of box edges to be associated with target entities.

	@surface_ents object: An entity or a list of entities, properties, materials, parts or sets 
	corresponding to the target surface entities.

	@user_projection_mode_vector object: (optional)A projection vector.

	@remove_points boolean: (optional)If set to True, remove existing control points from box edges.

	@box_edge_points object: (optional)A dictionary to define the number of points per box edge.

	@cut_geometric_faces boolean: (optional)If it set to True, target geometric faces will be cut
	on the position of the input box edges (after projecting 
	them to the geometric faces). Default value is False.

	@connect_to_cons boolean: (optional)If set to True,  connect the nodes of the box edges to the
	created Cons (used only if argument cut_geometric_faces 
	is set to True)

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def AssociateBoxFacesToSurfs(box_faces, surface_ents, user_projection_mode_vector, remove_points, box_edge_points):

	"""

	Script function to associate box faces to target surface entities (shells, geometrical faces).


	@box_faces object: A box face or a list of box faces to be associated with target entities.

	@surface_ents object: An entity or a list of entities, properties, materials, parts or sets corresponding 
	to the target surface entities.

	@user_projection_mode_vector object: (optional)A projection vector.

	@remove_points boolean: (optional)If set to True, remove existing control points from box edges.

	@box_edge_points object: (optional)A dictionary to define the number of points per box edge.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def AssociateBoxPointsToEdges(box_points, target_edges, insert_hot_point):

	"""

	Script function to associate box points to target feature lines (curves, cons, shell edges).


	@box_points object: A box point or a list of box points to be associated with the target entities.

	@target_edges object: An entity or a list of entities, parts or sets corresponding to the target feature lines.

	@insert_hot_point boolean: (optional)If it set to True, hot points will be inserted on the position of 
	the projection to the target Cons. Default value is False.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def AssociateBoxPointsToPoints(box_points, target_points):

	"""

	Script function to associate box points to target points. The maximum number of points equals 4.


	@box_points object: A box point or a list of box points to be associated with target entities.

	@target_points object: An entity or a list of entities, parts or sets corresponding to the target points.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def AssociateBoxPointsToSurfs(box_points, surface_ents, user_projection_mode_vector):

	"""

	Script function to associate box points to target surface entities (shells, geometrical faces).


	@box_points object: A box point or a list of box points to be associated with target 
	entities.

	@surface_ents object: An entity or a list of entities, properties, materials, parts or sets 
	corresponding to the target surface entities.

	@user_projection_mode_vector object: (optional)A projection vector.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def EraseBoxEdgesAssociation(box_edges):

	"""

	This function erases association from box edges.


	@box_edges object: A box edge or list of box edges to remove association.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def EraseBoxFacesAssociation(box_faces):

	"""

	This function erases association from box faces.


	@box_faces object: A box face or list of box faces to remove association.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def EraseBoxPointsAssociation(box_points):

	"""

	This function erases association from box points.


	@box_points object: A box point or list of box points to remove association.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def ZoneCutGradual( input, first_height_value, first_height_mode, growth_factor, number, max_aspect, separate_angle, connect_angle, regenerate_macro_shells, element_type, expand_level, smooth_zones, proximity_distance_value, proximity_distance_mode, cut_faces_on_zones, zones_set_id ):

	"""

	This function creates zones with gradual width around element edges.


	@input object: A list of sets of edges, sets of CONS, and CONS.

	@first_height_value float: The value of the first height.

	@first_height_mode string: The type of first height, "Absolute" or "Relative".

	@growth_factor float: The growth factor of the consecutive zones to create.

	@number integer: The number of the zones to create.

	@max_aspect float: (optional)The maximum allowed element aspect (height / base length).
	(Default: 0.4)

	@separate_angle float: (optional)The angle that determines the separation of a layer.
	(Default: 90)

	@connect_angle float: (optional)The angle that determines the connection of a layer with perimeters.
	(Default: 60)

	@regenerate_macro_shells boolean: (optional)Option to regenerate macro shells. Enabled by default.

	@element_type string: (optional)"Quad" or "Tria". Option to create tria zone elements, for tria mesh only.
	(Default: "Quad")

	@expand_level integer: (optional)The number of expanding shells zones added around selected edges.
	(Default: 1)

	@smooth_zones string: (optional)The option to smooth the created zones.
	Acceptable values: "Full", "Semi", "Off".
	(Default: "Full")

	@proximity_distance_value float: (optional)The  allowed distace for the proximity gap.
	(Default: 1)

	@proximity_distance_mode string: (optional)The mode of the proximity distance. 
	Acceptable values: "*last height", "*local height", "*min length", " ".
	(Default: "*last height")

	@cut_faces_on_zones boolean: (optional)Option to cut faces on last zone. Disabled by default.

	@zones_set_id integer: (optional)Adds the result zone shells to a set with [user defined] id.
	Not used by default.

	@returns integer: Returns 1.

	"""

def ZoneCutSpecificWidth(input, zones_offset, radial_offset, blended, expand_level, smooth_zones, proximity_distance_value, proximity_distance_mode, cut_faces_on_zones, zones_set_id):

	"""

	This function creates zones with specific width around element edges.


	@input object: A list of sets of edges, sets of CONS and CONS.

	@zones_offset object: A list of the width of each zone to create.

	@radial_offset boolean: (optional)An option to define zones width by radial distance.
	(Default: False)

	@blended boolean: (optional)An option to create blended zones.
	(Default: False)

	@expand_level integer: (optional)The number of expanding shells zones added around selected edges.
	(Default: 1)

	@smooth_zones string: (optional)The option to smooth the created zones.
	Acceptable values: "Full", "Semi", "Off".
	(Default: "Full")

	@proximity_distance_value float: (optional)The allowed distace for the proximity gap.
	(Default: 1)

	@proximity_distance_mode string: (optional)The mode of the proximity distance. 
	Acceptable values: "*last height", "*local height", "*min length", " ".
	(Default: "*last height")

	@cut_faces_on_zones boolean: (optional)An option to cut faces on last zone.
	(Default: False)

	@zones_set_id integer: (optional)Adds the result zone shells to a set with [user defined] id.
	Not used by default.

	@returns integer: Always returns 1.

	"""

def HexaBlockDeleteVolume(boxes):

	"""

	Script function to delete volumes of hexa block boxes.


	@boxes object: A box or a list of boxes to delete their volumes.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def HexaBlockEraseShellMesh(box_faces):

	"""

	Script function to erase shell mesh from box faces.


	@box_faces object: A box face or a list of box faces to erase shell mesh.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def HexaBlockEraseVolumeMesh(boxes):

	"""

	Script function to erase volume mesh from hexa block boxes.


	@boxes object: A box or a list of boxes to erase volume mesh.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def HexaBlockShellMesh(box_faces, tolerance, project, generator, apply_surface_fit, project_non_associated):

	"""

	Function to generate the shell mesh for input box_faces.
	
	By default, the "Map" algorithm is used for the mesh generation and "project", 
	"tolerance" values are defined by ANSA defaults.
	
	box_faces: object Box faces or list of box faces to generate shell mesh. 
	If box_faces equals 0, mesh is generated for all visible box faces.
	
	tolerance (optional): string String defining projection tolerance. String may contain 
	a real value (eg. "0.05"), or an expression (eg. "0.05*Lmin", where Lmin is the minimum
	length defined on box edges) 
	
	project (optional): boolean Flag that defines, whether to project (True) or not 
	(False) on geometry
	


	@box_faces object: A box face or a list of box faces to generate the shell mesh. 
	If box_faces equals to 0, mesh is generated for all visible box faces.

	@tolerance string: (optional)Defines the projection tolerance. The string may contain a 
	real value (eg. "0.05"), or an expression (eg. "0.05*Lmin", 
	where Lmin is the minimum length defined on box edges).

	@project boolean: (optional)A flag that defines whether to project (True) or not (False) on geometry.

	@generator string: (optional)Definition of the meshing algorithm to be used. 
	This value should be one of: "Map", "Free", "Spot Mesh",
	"Advancing Front" or "CFD".
	(Default: "Map"(Algorithm to be used))

	@apply_surface_fit boolean: (optional)A flag that defines if surface-fit will be applied for
	fully associated box faces (box faces with points,
	edges and face association).

	@project_non_associated boolean: (optional)A flag that defines if nodes of non-associated box
	faces will be projected on the geometry.

	@returns object: Returns a list containing the generated shells on success, None on failure.

	"""

def VolumesGlide(boundary_array, guideline_array, distribution, paste_nodes, paste_distance, steps_type, steps, element_length, biasing, factor, reference_point, part, property):

	"""

	This function can be used in order to generate a volume by gliding a predefined shell mesh along a given guideline.


	@boundary_array object: The shell mesh that will be extruded. Elements could be Faces, Shells or Facets.

	@guideline_array object: The guideline that defines the direction of the extrusion.
	Elements could be Perimeters, Edges or curves.

	@distribution string: Defines if the extrusion will use the guideline distribution or 
	if the user will define it.
	Accepted values: "Guideline", "User defined".

	@paste_nodes integer: Defines if the created nodes along guideline will be pasted on guideline 
	within a paste_distance.
	Accepted values: 0, 1.
	Works only if distribution is set to "Guideline", otherwise set to zero.

	@paste_distance float: The nodes along guideline and extrusion will be pasted under this tolerance.
	Works only if distribution is set to "Guideline", otherwise set to zero.

	@steps_type string: Defines if the user will set steps or element length for the extrusion.
	Accepted values: "Steps", "Element length".
	Works only if distribution is set to "User defined", otherwise set to zero.

	@steps integer: The number of the desired steps for the extrusion.
	Works only if distribution is set to "User defined", otherwise set to zero.

	@element_length float: The height of the elements in every step.

	@biasing string: Defines a biasing in the extrusion according to a factor.
	Accepted values: "Linear", "Exponential", "Bell Curve", "No Biasing".

	@factor float: The factor of the biasing.

	@reference_point string: Defines if the extrusion will start from the surface or the guideline.
	Accepted values: "On surface", "On guideline".

	@part object: (optional)Default values will be used if they are omitted.

	@property object: (optional)Default values will be used if they are omitted.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def VolumesSweep(boundary_array, guideline_array, distribution, paste_nodes, paste_distance, steps_type, steps, element_length, biasing, factor, reference_point, part, property):

	"""

	This function can be used in order to generate a volume by sweeping a predefined shell mesh along a given guideline.


	@boundary_array object: The shell mesh that will be extruded. Elements could be Faces, Shells or Facets.

	@guideline_array object: The guideline that defines the direction of the extrusion.
	Elements could be Perimeters, Edges or curves.

	@distribution string: Defines if the extrusion will use the guideline distribution or 
	if the user will define it.
	Accepted values: "Guideline", "User defined".

	@paste_nodes integer: Defines if the created nodes along guideline will be pasted on guideline 
	within a paste_distance.
	Accepted values: 0, 1.
	Works only if distribution is set to "Guideline", otherwise set to zero.

	@paste_distance float: The nodes along guideline and extrusion will be pasted under this tolerance.
	Works only if distribution is set to "Guideline", otherwise set to zero.

	@steps_type string: Defines if the user will set steps or element length for the extrusion.
	Accepted values: "Steps", "Element length".
	Works only if distribution is set to "User defined", otherwise set to zero.

	@steps integer: The number of the desired steps for the extrusion.
	Works only if distribution is set to "User defined", otherwise set to zero.

	@element_length float: The height of the elements in every step.

	@biasing string: Defines a biasing in the extrusion according to a factor.
	Accepted values: "Linear", "Exponential", "Bell Curve", "No Biasing".

	@factor float: The factor of the biasing.

	@reference_point string: Defines if the extrusion will start from the surface or the guideline.
	Accepted values: "On surface", "On guideline".

	@part object: (optional)Default values will be used if they are omitted.

	@property object: (optional)Default values will be used if they are omitted.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def VolumesDualSweep(boundary_array, guideline1_array, guideline2_array, distribution, paste_nodes, paste_distance, steps_type, steps, element_length, biasing, factor, reference_point, part, property):

	"""

	This function can be used in order to generate a volume, by sweeping a predefined shell mesh along two given guidelines.


	@boundary_array object: The shell mesh that will be extruded. Elements could be Faces, Shells or Facets.

	@guideline1_array object: The guideline that defines the direction of the extrusion.
	Elements could be Perimeters, Edges or curves.

	@guideline2_array object: The guideline that defines the rotation of the extrusion along the direction.
	Elements could be Perimeters, Edges or curves.

	@distribution string: Defines if the extrusion will use the guideline distribution or 
	if the user will define it.
	Accepted values: "Guideline", "User defined".

	@paste_nodes integer: Defines if the created nodes along guideline will be pasted on guideline 
	within a paste_distance.
	Accepted values: 0, 1.
	Works only if distribution is set to "Guideline", otherwise set to zero.

	@paste_distance float: The nodes along guideline and extrusion will be pasted under this tolerance.
	Works only if distribution is set to "Guideline", otherwise set to zero.

	@steps_type string: Defines if the user will set steps or element length for the extrusion.
	Accepted values: "Steps", "Element length".
	Works only if distribution is set to "User defined", otherwise set to zero.

	@steps integer: The number of the desired steps for the extrusion.
	Works only if distribution is set to "User defined", otherwise set to zero.

	@element_length float: The height of the elements in every step.

	@biasing string: Defines a biasing in the extrusion according to a factor.
	Accepted values: "Linear", "Exponential", "Bell Curve", "No Biasing".

	@factor float: The factor of the biasing.

	@reference_point string: Defines if the extrusion will start from the surface or the guideline.
	Accepted values: "On surface", "On guideline".

	@part object: (optional)Default values will be used if they are omitted.

	@property object: (optional)Default values will be used if they are omitted.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def IsolateWashers(shells, include_filled_connection_holes):

	"""

	Isolates the washers shells found at the input shells.


	@shells object: A list of shell entities. Set 0 to work on visible.

	@include_filled_connection_holes boolean: (optional)Set to True, to include washers around filled connection holes.

	@returns object: Returns the washers shells in a list.

	"""

def IsolateExterior(input, groups_number, classification, group_entities, separate_at_blue_bounds, separate_at_pid_bounds, feature_angle, feature_type, view_point):

	"""

	The function separates the input entities to groups according to how exterior they are.


	@input object: A list that can contain faces, shells and solids.

	@groups_number integer: The number of groups in which the input entities will be categorized.

	@classification string: (optional)Specifies the way the connectivity groups will be classified.
	They can be classified by an average value by the outermost or 
	the innermost entity.
	Available options are "average", "outermost" and "innermost".
	(Default: "average")

	@group_entities boolean: (optional)If set to True, the entities will be isolated as whole connectivity groups.
	If set to False, each entity will be isolated separately.
	(Default: True)

	@separate_at_blue_bounds boolean: (optional)If set to True, then regions connected via triple bounds are placed into 
	separate connectivity groups.
	If set to False, then all connected entities are placed into the same group.
	This option is valid only when group_entities = True.
	In case of group_entities = False it is ignored.
	(Default: True)

	@separate_at_pid_bounds boolean: (optional)If set to True, then all entities contained in a connectivity group 
	will have the same PID.
	If set to False, then each connectivity group can contain connected 
	entities with different PIDs.
	This option is valid only when group_entities = True.
	In case of group_entities = False it is ignored.
	(Default: True)

	@feature_angle float: (optional)The feature angle limit in degrees.
	If this value is exceeded, the groups get separated at this feature line.
	Valid values are 0 - 180.
	If set to 0, the feature line separation is disabled.
	This option is valid only when group_entities = True.
	In case of group_entities = False it is ignored.
	(Default: 60.0)

	@feature_type string: (optional)Specifies the type of the feature lines in which the connectivity groups 
	will be separated.
	Groups get separated at the examined bound only if feature_angle is 
	exceeded and the feature type is of the specified type.
	Available options are "convex", "concave" and "convex_and_concave".
	This option is valid only when group_entities = True and feature_angle > 0.
	In case of group_entities = False or feature_angle = 0 it is ignored.
	(Default: "convex_and_concave")

	@view_point string: (optional)Specifies the view point from wich the model will be observed.
	Available options are "scan_all_around" and "normal_to_screen".
	(Default: "scan_all_around")

	@returns object: Returns a list.
	This list contains lists with entities that correspond to each group on how exterior they are.
	The lists are sorted from the most interior group of entities to the most exterior.
	The first list contains the absolutely interior entities and the last the absolutely exterior.

	"""

def CalculateThickness(middle_entities, skin_entities, maximum_thickness, keep_thickness_at_junctions):

	"""

	This function calculates the proper thickness for every node of each middle shell based on the specified skin entities.


	@middle_entities object: A list that contains the entities that will get a new 
	calculated thickness.

	@skin_entities object: A list that contains the middle entities that represent 
	the solid description of the model.

	@maximum_thickness float: Determines the distance from the middle within which the 
	function will begin to search for the corresponding skin.

	@keep_thickness_at_junctions integer: Determines if the thickness of the ribs will be kept while 
	approaching to the junctions or not.

	@returns integer: Always returns 1.

	"""

def SplitToTetras(solids, improve, ret_ents):

	"""

	This function will convert solids elements into tetrahedrals. 
	The solids are given as an arguement and the they are going to be deleted.
	If improve_quality is active then any off elements that will be created will be reconstructed


	@solids object: The solids that are going to be converted.

	@improve boolean: If true, then after the spliting any off elements are going to be reconstructed.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@returns integer: Returns 0 on success and 1 on failure.
	If ret_ents=True it will return a list with the created entities, 
	or None if no entities are created.

	"""

def IntersectWeldingFE(input, thick_ratio, extend_distance, ignore_same_pid, ignore_same_part, ignore_same_set, ignore_same_neighbour_zones, improve_mesh_quality):

	"""

	This function extends and connects skinned FE meshes.


	@input object: A single object or a list of parts, properties, materials or sets.
	If input equals to 0, the visible shells are collected.

	@thick_ratio float: (optional)The extension limit expressed as a ratio of the local nodal thickness.
	(Default: 0.0)

	@extend_distance float: (optional)The extension limit expressed as an absolute value.
	(Default: 0.0)

	@ignore_same_pid boolean: (optional)If set to True, ignores intersections within the same property.

	@ignore_same_part boolean: (optional)If set to True, ignores intersections within the same part.

	@ignore_same_set boolean: (optional)If set to True, ignores intersections within the same set.

	@ignore_same_neighbour_zones boolean: (optional)If set to True, ignores intersection between shells that are 
	within n zones from each other.

	@improve_mesh_quality boolean: (optional)If set to True, improves the mesh quality in 1 zone around 
	the intersected shells.

	@returns integer: Always returns 1.

	"""

def IntersectFusePanels(input, offset_distance, ignore_same_pid, ignore_same_part, ignore_same_set, ignore_same_neighbour_zones, improve_mesh_quality, fuse_direction, dx, dy, dz, project_shells):

	"""

	This function implements fuse parallel overlapping FE panels to create watertight mesh.


	@input object: A single object or a list of parts, properties, materials or sets.
	If input equals to 0, the visible shells are collected.

	@offset_distance float: The offset distance between different panels, measured in the direction 
	of the negative normal vector.

	@ignore_same_pid boolean: (optional)If set to True, ignores intersections with the same property.

	@ignore_same_part boolean: (optional)If set to True, ignores intersections within the same part.

	@ignore_same_set boolean: (optional)If set to True, ignores intersections within the same set.

	@ignore_same_neighbour_zones boolean: (optional)If set to True, ignores intersection between shells that are 
	within n zones from each other.

	@improve_mesh_quality boolean: (optional)If set to True, improves the mesh quality in 1 zone around 
	the intersected shells.

	@fuse_direction string: (optional)Defines the fuse direction.
	Can be "negative_offset", "user_defined" or "project".
	(Default: "negative_offset")

	@dx float: (optional)The x-coordinate for the projection direction.
	This is taken into account only when fuse_direction = "user_defined".

	@dy float: (optional)The y-coordinate for the projection direction.
	This is taken into account only when fuse_direction = "user_defined".

	@dz float: (optional)The z-coordinate for the projection direction.
	This is taken into account only when fuse_direction = "user_defined".

	@project_shells object: (optional)A list of shells to be projected on "input" shells.
	This is taken into account only when fuse_direction = "project".

	@returns integer: Always returns 1.

	"""

def HexaBoxOrtho(loaded_elements, db_or_visible, coordinate, min_flag):

	"""

	Function for the creation of a hexa box.


	@loaded_elements object: (optional)A list with the elements to be included by the created hexa box.

	@db_or_visible string: (optional)Can have values 'DB' or 'Visible', for elements to be included 
	by the created hexa box.

	@coordinate object: (optional)A local coordinate object instead of global.

	@min_flag boolean: (optional)True or False for minimum volume hexa box.

	@returns object: Returns a reference to the newly created hexa box object on success, or 0 on failure.

	"""

def CreateShellsOnSolidsPidSkin(solids, ret_ents):

	"""

	This function creates shells/shedras on the skin of the solid properties, while assigning 
	those shells to a new pid and part with similar name 
	as the solids on whose facets they were created.
	The function works with Solids of first and second order, as well as with polyhedra.


	@solids object: An array of solids/polyhedra where the solid pids will be found.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@returns object: Returns 0 on success and 1 on failure.
	If ret_ents=True, then it returns a list with the created entities.

	"""

def ExtrudeOffset(source, target, rem_source, connect_source, direction, distance, steps, first_height, biasing, factor, factor_dir, side_treatment, angle, snap_to_target, connect_to_target, part, property):

	"""
	Deprecated since version 20.1.0. Use class VolumesExtrude instead.

	This function generates Hexa and/or Penta volume elements, through extruding a Source area.
	Source area may consist either of Macro Areas, that do not have to be necessarily meshed, 
	FE Shells or Solid Facets (or a combination of the previous). A normal vector of source 
	area is used as offset vector. The user may select a Linear, Exponential or Bell Curve 
	biasing function to achieve the desired volume element distribution.


	@source object: A list of shells, faces or facets which are used as source area.

	@target object: (optional)A list of shells, faces or facets which are used as target area.

	@rem_source object: (optional)A list of shells, faces or facets which are removed from source area.

	@connect_source boolean: (optional)Connect source areas.

	@direction string: (optional)Direction of offset vector. Can be "default", "inverted" or "both".

	@distance float: (optional)Target distance.

	@steps integer: (optional)Number of distribution steps.

	@first_height float: (optional)The height of the first layer.

	@biasing string: (optional)Type of distribution biasing. Can be "linear", "exponential", "bell" or "no".

	@factor float: (optional)Biasing factor.

	@factor_dir string: (optional)Biasing direction. Can be "default" or "inverted".

	@side_treatment string: (optional)Side treatment can be "snap" for Snap to Side, "collapse" for Collapse 
	free edges, "no" for no side treatment.

	@angle float: (optional)Angle used for side treatment.

	@snap_to_target boolean: (optional)Snap to target bounds.

	@connect_to_target boolean: (optional)Connect to target area.

	@part object: (optional)The part assigned to the created volume.

	@property object: (optional)The property assigned to the created volume.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use class VolumesExtrude instead.", DeprecationWarning)

def ExtrudeProject(source, target, rem_source, connect_source, steps, first_height, biasing, factor, factor_dir, side_treatment, angle, snap_to_target, connect_to_target, part, property):

	"""

	This function generates Hexa and/or Penta volume elements, through extruding a Source area.
	Source area may consist either of Macro Areas, that do not have to be necessarily meshed, 
	FE Shells or Solid Facets (or a combination of the previous). The projection of source 
	area to target area leads the extrusion. The user may select a Linear, Exponential or 
	Bell Curve biasing function to achieve the desired volume element distribution.


	@source object: A list of shells, faces or facets which are used as source area.

	@target object: A list of shells, faces or facets which are used as target area.

	@rem_source object: (optional)A list of shells, faces or facets which are removed from source area.

	@connect_source boolean: (optional)Connect source areas.

	@steps integer: (optional)Number of distribution steps.

	@first_height float: (optional)The height of the first layer.

	@biasing string: (optional)Type of distribution biasing. Can be "linear", "exponential", "bell" or "no".

	@factor float: (optional)Biasing factor.

	@factor_dir string: (optional)Biasing direction. Can be "default" or "inverted".

	@side_treatment string: (optional)Side treatment can be "snap" for Snap to Side, "collapse" for Collapse 
	free edges, "no" for no side treatment.

	@angle float: (optional)Angle used for side treatment.

	@snap_to_target boolean: (optional)Snap to target bounds.

	@connect_to_target boolean: (optional)Connect to target area.

	@part object: (optional)The part assigned to the created volume.

	@property object: (optional)The property assigned to the created volume.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def ExtrudeRotate(source, rotation_axis, rotation_angle, target, rem_source, connect_source, steps, first_height, biasing, factor, factor_dir, side_treatment, angle, snap_to_target, connect_to_target, part, property):

	"""

	This function generates Hexa and/or Penta volume elements, through extruding a Source area.
	Source area may consist either of Macro Areas, that do not have to be necessarily meshed, 
	FE Shells or Solid Facets (or a combination of the previous). Source area elements are 
	rotated using a rotation axis and a rotation angle. The user may select a Linear, Exponential 
	or Bell Curve biasing function to achieve the desired volume element distribution. 


	@source object: A list of shells, faces or facets which are used as source area.

	@rotation_axis object: Rotation Axis must be a list with two vectors, the first one defines the origin of the axis, the second one its direction, i.e. ((50,0,0), (0,0,1))

	@rotation_angle float: Angle used when rotational axis has been selected as guideline.

	@target object: (optional)A list of shells, faces or facets which are used as target area.

	@rem_source object: (optional)A list of shells, faces or facets which are removed from source area.

	@connect_source boolean: (optional)Connect source areas.

	@steps integer: (optional)Number of distribution steps.

	@first_height float: (optional)The height of the first layer.

	@biasing string: (optional)Type of distribution biasing. Can be "linear", "exponential", "bell" or "no".

	@factor float: (optional)Biasing factor.

	@factor_dir string: (optional)Biasing direction. Can be "default" or "inverted".

	@side_treatment string: (optional)Side treatment can be "snap" for Snap to Side, "collapse" for Collapse 
	free edges, "no" for no side treatment.

	@angle float: (optional)Angle used for side treatment.

	@snap_to_target boolean: (optional)Snap to target bounds.

	@connect_to_target boolean: (optional)Connect to target area.

	@part object: (optional)The part assigned to the created volume.

	@property object: (optional)The property assigned to the created volume.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def ExtrudeTranslate(source, translation_axis, target, rem_source, connect_source, distance, steps, first_height, biasing, factor, factor_dir, side_treatment, angle, snap_to_target, connect_to_target, part, property):

	"""

	This function generates Hexa and/or Penta volume elements, through extruding a Source area.
	Source area may consist either of Macro Areas, that do not have to be necessarily meshed, 
	FE Shells or Solid Facets (or a combination of the previous). A translation vector is 
	used to create volume elements. The user may select a Linear, Exponential or Bell Curve 
	biasing function to achieve the desired volume element distribution.


	@source object: A list of shells, faces or facets which are used as source area.

	@translation_axis object: Translation Axis must be a list with two vectors, 
	i.e. ((10, 10, 10),  (5, 5, 5)).

	@target object: (optional)A list of shells, faces or facets which are used as target area.

	@rem_source object: (optional)A list of shells, faces or facets which are removed from source area.

	@connect_source boolean: (optional)Connect source areas.

	@distance float: (optional)Target distance.

	@steps integer: (optional)Number of distribution steps.

	@first_height float: (optional)The height of the first layer.

	@biasing string: (optional)Type of distribution biasing. Can be "linear", "exponential", "bell" or "no".

	@factor float: (optional)Biasing factor.

	@factor_dir string: (optional)Biasing direction. Can be "default" or "inverted".

	@side_treatment string: (optional)Side treatment can be "snap" for Snap to Side, "collapse" for Collapse 
	free edges, "no" for no side treatment.

	@angle float: (optional)Angle used for side treatment.

	@snap_to_target boolean: (optional)Snap to target bounds.

	@connect_to_target boolean: (optional)Connect to target area.

	@part object: (optional)The part assigned to the created volume.

	@property object: (optional)The property assigned to the created volume.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def ExtrudeSweepGlide(algorithm, source, guideline, target, rem_source, connect_source, guide_distribution, steps, first_height, biasing, factor, factor_dir, side_treatment, angle, snap_to_target, connect_to_target, part, property):

	"""

	This function generates Hexa and/or Penta volume elements, through extruding a Source area.
	Source area may consist either of Macro Areas, that do not have to be necessarily meshed, 
	FE Shells or Solid Facets (or a combination of the previous). Source area elements are 
	swept or glided using Curves, Macro Areas' Perimeter segments or edges as guidelines. 
	The user may select a Linear, Exponential or Bell Curve biasing function to achieve the 
	desired volume element distribution. 


	@algorithm string: Algorithm used for extrusion, can be "sweep" or "glide".

	@source object: A list of shells, faces or facets which are used as source area.

	@guideline object: Perimeters, curves or edges used as guide lines.

	@target object: (optional)A list of shells, faces or facets which are used as target area.

	@rem_source object: (optional)A list of shells, faces or facets which are removed from source area.

	@connect_source boolean: (optional)Connect source areas.

	@guide_distribution boolean: (optional)Use guide distribution.
	If enabled all other distribution arguments should not be used.

	@steps integer: (optional)Number of distribution steps.

	@first_height float: (optional)The height of the first layer.

	@biasing string: (optional)Type of distribution biasing. Can be "linear", "exponential", "bell" or "no".

	@factor float: (optional)Biasing factor.

	@factor_dir string: (optional)Biasing direction. Can be "default" or "inverted".

	@side_treatment string: (optional)Side treatment can be "snap" for Snap to Side, "collapse" for Collapse 
	free edges, "no" for no side treatment.

	@angle float: (optional)Angle used for side treatment.

	@snap_to_target boolean: (optional)Snap to target bounds.

	@connect_to_target boolean: (optional)Connect to target area.

	@part object: (optional)The part assigned to the created volume.

	@property object: (optional)The property assigned to the created volume.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def ExtrudeDualSweep(source, guideline, target, rem_source, connect_source, guide_distribution, steps, first_height, biasing, factor, factor_dir, side_treatment, angle, snap_to_target, connect_to_target, part, property):

	"""

	This function generates Hexa and/or Penta volume elements, through extruding a Source area. 
	Source area may consist either of Macro Areas, that do not have to be necessarily meshed, 
	FE Shells or Solid Facets (or a combination of the previous). Source area elements are swept 
	along two guidelines of Curves, Macro Areas' Perimeter segments or edges. The user may select 
	a Linear, Exponential or Bell Curve biasing function to achieve the desired volume element 
	distribution. 


	@source object: A list of shells, faces or facets which are used as source area.

	@guideline object: Perimeters, curves or edges used as guide lines.

	@target object: (optional)A list of shells, faces or facets which are used as target area.

	@rem_source object: (optional)A list of shells, faces or facets which are removed from source area.

	@connect_source boolean: (optional)Connect source areas.

	@guide_distribution boolean: (optional)Use guide distribution.
	If enabled all other distribution arguments should not be used.

	@steps integer: (optional)Number of distribution steps.

	@first_height float: (optional)The height of the first layer.

	@biasing string: (optional)Type of distribution biasing. Can be "linear", "exponential", "bell" or "no".

	@factor float: (optional)Biasing factor.

	@factor_dir string: (optional)Biasing direction. Can be "default" or "inverted".

	@side_treatment string: (optional)Side treatment can be "snap" for Snap to Side, "collapse" for Collapse 
	free edges, "no" for no side treatment.

	@angle float: (optional)Angle used for side treatment.

	@snap_to_target boolean: (optional)Snap to target bounds.

	@connect_to_target boolean: (optional)Connect to target area.

	@part object: (optional)The part assigned to the created volume.

	@property object: (optional)The property assigned to the created volume.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def ExtrudeMap(source, guideline, target, rem_source, connect_source, guide_distribution, steps, first_height, biasing, factor, factor_dir, side_treatment, angle, snap_to_target, connect_to_target, part, property):

	"""

	This function generates Hexa and/or Penta volume elements, through extruding a Source area.
	Source area may consist either of Macro Areas, that do not have to be necessarily meshed, 
	FE Shells or Solid Facets (or a combination of the previous). Source area elements are 
	extruded using two or more guidelines of Curves, Macro Areas' Perimeter segments or edges.
	The user may select a Linear, Exponential or Bell Curve biasing function to achieve the 
	desired volume element distribution. 


	@source object: A list of shells, faces or facets which are used as source area.

	@guideline object: Perimeters, curves or edges used as guide lines.

	@target object: (optional)A list of shells, faces or facets which are used as target area.

	@rem_source object: (optional)A list of shells, faces or facets which are removed from source area.

	@connect_source boolean: (optional)Connect source areas.

	@guide_distribution boolean: (optional)Use guide distribution.
	If enabled all other distribution arguments should not be used.

	@steps integer: (optional)Number of distribution steps.

	@first_height float: (optional)The height of the first layer.

	@biasing string: (optional)Type of distribution biasing. Can be "linear", "exponential", "bell" or "no".

	@factor float: (optional)Biasing factor.

	@factor_dir string: (optional)Biasing direction. Can be "default" or "inverted".

	@side_treatment string: (optional)Side treatment can be "snap" for Snap to Side, "collapse" for Collapse 
	free edges, "no" for no side treatment.

	@angle float: (optional)Angle used for side treatment.

	@snap_to_target boolean: (optional)Snap to target bounds.

	@connect_to_target boolean: (optional)Connect to target area.

	@part object: (optional)The part assigned to the created volume.

	@property object: (optional)The property assigned to the created volume.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def HexaBlockInitBoxEdges(box_edges, remesh_box_faces, initialize_number, initialize_spacing):

	"""

	This function initializes the nodal spacing of hexa block edges.


	@box_edges object: A list that contains box edges to be initialized.

	@remesh_box_faces boolean: A flag to control if the box faces will be remeshed after the initialization.

	@initialize_number boolean: Initialize the nodal number of box edges.

	@initialize_spacing boolean: Initialize the spacing of box edges.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def HexaBlockVolumesMap(box_faces, boxes, tolerance, project, apply_surface_fit, project_non_associated):

	"""

	Script function that generates the volume mesh according to the Hexa Block "Map" generator.


	@box_faces object: A list that contains hexa box faces whose shell mesh will be used 
	to generate solid elements (hexas and pentas).

	@boxes object: (optional)The boxes where the shell mesh pattern will be transmitted.

	@tolerance string: (optional)An expression to define the tolerance as a percentage of 
	the minimum element length (Lmin).

	@project boolean: (optional)A flag that defines whether to project (True) or not (False) on geometry.

	@apply_surface_fit boolean: (optional)A flag that defines if surface-fit will be applied for
	fully associated box faces (box faces with points,
	edges and face association).

	@project_non_associated boolean: (optional)A flag that defines if nodes of non-associated box
	faces will be projected on the geometry.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def Redistribute(property, num_layers, layers_dir, growth_rate, modify, num_layers_applied, create_shells):

	"""

	This function changes the distribution of solid element layers that belong to a given property.


	@property object: The property of the solid layers to be redistributed.

	@num_layers object: The number of layers.

	@layers_dir integer: (optional)The direction of the layers redistribution.
	Can be 1, 2, 3, -1, -2, -3 (Note: 1 is the direction of ANSA layers)

	@growth_rate float: (optional)The growth rate.

	@modify string: (optional)Determines whether changes are applied per layer or for all layers.
	It can be "per_layer" or "all_layers".

	@num_layers_applied integer: (optional)If enabled, redistribution is applied only at the given number of first layers.

	@create_shells boolean: (optional)If enabled, new shells are created instead of modifying existing layers.

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def ChangeHeightOfLayers( property, increase_by, type, layers_dir, mod_dir, num_layers_applied ):

	"""

	This function modifies the height of solid element layers that belong to a given property.


	@property object: Property of solid layers to be modified

	@increase_by float: Increase value

	@type string: Type of increase value; can be "percentage" or "absolute"

	@layers_dir integer: (optional)Direction of layers modification; can be 1, 2, 3, -1, -2, -3 (Note: 1 is the direction of ANSA layers)

	@mod_dir string: (optional)Determines the direction where the height is modified; can be "up", "down" or "both"

	@num_layers_applied integer: (optional)If enabled modifications are applied only at the given number of first layers

	@returns integer: One 1 upon success zero 0 on failure

	"""

def HexaBlockOrthoSmooth(box_faces, feature_lines, layers_number, layers_smooth_iterations, smooth_through_boxes, smooth_base_surface_mesh, smooth_iterations, fix_violating_solids, boxes):

	"""

	Smooths Hexa Block Orthos.


	@box_faces object: A list of box faces where layers grow from. O-Grid topologies 
	can also be used as input (in this case, O-Grid box faces will
	be used by the function).

	@feature_lines object: (optional)A list of box edges that define the model's feature lines. If no
	box edges are defined as feature lines, default feature lines
	will be used (according to the feature line angle).

	@layers_number integer: (optional)The number of layers to be smoothed for orthogonality.
	If it is not defined, the default value will be used.

	@layers_smooth_iterations integer: (optional)The number of iterations that control the smoothing of layers' vectors.
	More iterations result in smoother layers' vectors (they deviate more 
	from surface normal vectors).
	If it is not defined, the default value will be used.

	@smooth_through_boxes boolean: (optional)A flag to define if smoothing will affect the whole hexa block model.

	@smooth_base_surface_mesh boolean: (optional)A flag to define if the surface mesh of the boundary box faces 
	will be smoothed.

	@smooth_iterations integer: (optional)The number of iterations that define the smoothing of neighboring solids 
	and/or base surface mesh. More iterations result in smoother 
	(shell/solid) mesh. If it is not defined, default value will be used.

	@fix_violating_solids boolean: (optional)A flag to activate a mechanism that fixes solids having 
	intersections or negative volume.

	@boxes object: (optional)The boxes to be smoothed by the general smoothing algorithm.
	It is used to avoid smoothing the whole hexa block model (defined 
	by the flag smooth_through_boxes).

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def MatchShellsAndSolids(shells, solids):

	"""

	Returns a list of matched Shells and Solids. Every 2 instances of the list is a pair.
	It needs a list of shells and a list of solids.


	@shells object: A list of shells.

	@solids object: A list of solids.

	@returns object: Returns a list of pairs of shells and solids.

	"""

def CreateFillet(fillet_type, edges, chamfer_width, fillet_radius, fillet_rows, ret_ents):

	"""

	This function creates fillet or chamfer on FE shells at dach areas. Givien as input 
	the edges of the dach, it creates fillet/chamfer according to the rest input parameters.


	@fillet_type string: The fillet type that will be created. It can be "fillet" or "chamfer".

	@edges object: Edges of the dach area.

	@chamfer_width float: (optional)The width of the chamfer.

	@fillet_radius float: (optional)The radius of the fillet.

	@fillet_rows integer: (optional)The rows of the fillet.

	@ret_ents boolean: (optional)If set to True, a list with the shells of the created fillet/chamfer will be returned.

	@returns object: Returns 1 on success or 0 on failure.
	If ret_ents=True, it will return a list with the shells of the created fillet/chamfer, or None in case of error.

	"""

def ModifyFillet( fillet_type, shells, edges, chamfer_width, fillet_radius, fillet_rows, ret_ents):

	"""

	This function creates dach, chamfer or fillet on FE shells at chamfer/fillet areas. 
	Giving as input the shells of the existing chamfer/fillet and the upper and down edges 
	that define the fillet direction, it modifies it according to the rest input parameters. 
	It can be used to change the existing fillet type into another or to change its parameters.
	For example change a fillet into dach, or just change a fillet's rows.


	@fillet_type string: The fillet type that the existing chamfer/fillet will be modified into.
	Can be "dach", "fillet" or "chamfer".

	@shells object: The FE shells of the existing chamfer/fillet.

	@edges object: The upper and down edges of the existing chamfer/fillet that 
	define the fillet direction.

	@chamfer_width float: (optional)The width of the chamfer.

	@fillet_radius float: (optional)The radius of the fillet.

	@fillet_rows integer: (optional)The rows of the fillet.

	@ret_ents boolean: (optional)If set to True, a list with the shells of the created fillet/chamfer will be returned.

	@returns object: Returns 1 on success or 0 on failure.
	If ret_ents=True, it will return a list with the shells of the created fillet/chamfer, or None in case of error.

	"""

def ElementsExtrude(algorithm, edges, guideline1, use_edges_nodes, distribution, ref_point, guideline2, paste_nodes, tolerance, length, bias_type, bias_factor, point1, point2):

	"""

	This function generates shell mesh through extruding the input edges based on one or two guidelines.
	Edges are swept or glided using curves, perimeters or edges as guidelines. The user may select a Linear, 
	Exponential or Bell Curve biasing function to achieve the desired element distribution.
	There is also the possibility to translate the final mesh to a desired reference point.


	@algorithm string: Algorithm used for extrusion. Can be "sweep" or "glide".

	@edges object: The edges that will be extruded.

	@guideline1 object: Perimeters, curves or edges, used as basic guideline.

	@use_edges_nodes boolean: Use the existing nodes of the guideline if it is not curve, 
	otherwise the distribution will be "user_defined".

	@distribution string: The type of the distribution used for the extrusion, 
	can be "guideline" or "user_defined".

	@ref_point string: The reference point from where to start the extrusion, 
	can be "on_edges" or "on_guideline".

	@guideline2 object: (optional)Perimeters, curves or edges, used as secondary guideline 
	in case of "sweep" algorithm.

	@paste_nodes boolean: (optional)Paste the nodes along the guideline, if it is not curve.

	@tolerance float: (optional)The tolerance in case of "guideline" distribution.

	@length float: (optional)The element length used in case of "user_defined" distribution.

	@bias_type string: (optional)Type of biasing in case of "user_defined" distribution.
	Can be "linear", "exponential", "bell_curve".

	@bias_factor float: (optional)Biasing factor.

	@point1 object: (optional)The first point used in case of "on_guideline" reference point.
	It should be a node of the edges given as input.
	The final result will be an extruded mesh shifted so that the point1 
	will overlap point2.

	@point2 object: (optional)The second point used in case of "on_guideline" reference point.
	The final result will be an extruded mesh shifted so that the point1 
	will overlap point2.

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def HexaBoxByPoints(points, solid_type):

	"""

	Function for creating 3D hexa block boxes (TETRA, PENTA or HEXA boxes) 
	from existing nodes, edges or shells.


	@points object: A list with entities from where 5,6,7 or 8 points will be taken to
	create TETRA, PYRAMID, PENTA or HEXA boxes.

	@solid_type string: (optional)An argument that defines the solid type in case
	that the input points could be used for the creation
	of more than one solid types. It takes the values
	"hexa", "penta", "tetra" or "pyramid".

	@returns object: Returns a reference to the newly created box object on success, or 0 on failure.

	"""

def HexaBlockSaveAssociations(filename, hexa_block_entities, geometric_entities, model):

	"""

	This function saves the associations of the hexa block entities.


	@filename string: The path of the file where all the associations of the hexa block 
	entities will be saved.

	@hexa_block_entities string: (optional)Takes the values "Id" or "Name". It defines the way that hexa 
	block entities are saved in the associations file.
	(Default: "Id")

	@geometric_entities string: (optional)Takes the values "Id", "Name" or "Faces_Set_Name". It defines the 
	way that geometric entities are saved in the associations file. Keyword 
	"Faces_Set_Name" is used for CATIA files that are imported in ANSA. 
	In this case, ANSA has the option to create a separate set for every 
	geometric face and create a specific rule to save geometric entities.
	(Default: "Id")

	@model string: (optional)Takes the values "Visible" or "Whole_Database".
	(Default: "Whole_Database")

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def HexaBlockReadAssociations(filename):

	"""

	Reads and applies the associations of a file to the hexa block entities of the database.


	@filename string: The path of the file that contains the associations information of the hexa block entities.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def RedistributeMulti(list, num_layers, layers_dir, growth_rate, modify, num_layers_applied, create_shells):

	"""

	This function changes the distribution of solid element layers that belong to a given list of properties or volumes.


	@list object: A list of Pids and Volumes to be redistributed.

	@num_layers integer: The number of layers.

	@layers_dir integer: (optional)The direction of the layers redistribution.
	Can be 1, 2, 3, -1, -2, -3 (Note: 1 is the direction of ANSA layers).

	@growth_rate float: (optional)The growth rate.

	@modify string: (optional)Determines whether changes are applied per layer or for all layers.
	Can be "per_layer" or "all_layers".

	@num_layers_applied boolean: (optional)If enabled, redistribution is applied only at the given number of first layers.

	@create_shells boolean: (optional)If enabled, new shells are created instead of modifying existing layers.

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def ChangeHeightOfLayersMulti( list, increase_by, type, layers_dir, mod_dir, num_layers_applied ):

	"""

	This function modifies the height of solid element layers that belong to a given list of properties or volumes.


	@list object: List of Pids and Volumes to be modified

	@increase_by float: Increase value

	@type string: Type of increase value; can be "percentage" or "absolute"

	@layers_dir integer: (optional)Direction of layers modification; can be 1, 2, 3, -1, -2, -3 (Note: 1 is the direction of ANSA layers)

	@mod_dir string: (optional)Determines the direction where the height is modified; can be "up", "down" or "both"

	@num_layers_applied integer: (optional)If enabled modifications are applied only at the given number of first layers

	@returns: One 1 upon success zero 0 on failure

	"""

def Create2DEnvelopeFromShellsOnPlane (shells):

	"""

	The function is designed to work on a list of shells that lie on the same plane.
	It creates a planar shell mesh that represents the 2d envelope of the input shells.


	@shells object: A list with references to shell elements.

	@returns object: Returns a list with with the created shells of the 2d envelope.
	On error, it returns an empty list.

	"""

def SuppressNoise(shells, intensity, only_move_nodes, movement_direction):

	"""

	This function will smooth and flatten anomalies that exist in FE mesh.


	@shells object: A list of shell entities.

	@intensity string: (optional)Defines how intense the suppressing of the noise will be.
	Available options are "high", "middle", "low" and "local_peaks".
	(Default: "high")

	@only_move_nodes boolean: (optional)If set to True, the mesh connectivity will remain and the result will have 
	the same nodes but in a new position.
	If set to False, the mesh connectivity will change and some nodes will be pasted.
	(Default: False)

	@movement_direction string: (optional)Defines the direction towards the nodes will be moved.
	Available options are "both_sides", "grey_side" or "yellow_side".
	(Default: "both_sides")

	@returns integer: Returns 1 in all cases.

	"""

def SolidsMeshV(solids, mesh_type):

	"""

	This function remeshes an array of solids with a specified generator.


	@solids object: A list with the solid elements to be remeshed.

	@mesh_type string: Corresponds to the mesh generator. The string values for each mesh type can be:
	"TETRA RAPID", "TETRA FEM", "TETRA CFD", "HEXA INTERIOR" or "HEXAPOLY".

	@returns integer: Returns 1 on success or 0 on failure.

	"""

def HexaBoxByCurves(height_edges, top_bottom_edges):

	"""

	A function for creating a hexa block box by defining its four "height" edges
	and the "top", "bottom" edges (optionally).


	@height_edges object: A list that contains all the entities that define 
	the four box "height" edges.

	@top_bottom_edges object: (optional)A list that contains all the entities that define 
	the "top" and "bottom" edges of the new box.

	@returns object: Returns a reference to the newly created box object on success, or 0 on failure.

	"""

def CavityWrap(entities, leak_distance, target_length, maximum_length, nth_largest, snap_nodes, features_set):

	"""

	This function creates constant length wraps suitable for inner cavities.


	@entities object: A list of input entities.

	@leak_distance float: The maximum length gaps that the algorithm will not intrude.
	The octree voxel length.

	@target_length float: The target length of the final wrap mesh.

	@maximum_length float: The strict maximum length that the final wrap will not violate.

	@nth_largest integer: (optional)The number of the largest inner cavities that will be wrapped.
	(Default: 1)

	@snap_nodes boolean: (optional)If set to True the nodes of wrap will be snapped to the closest 
	nodes of structure.
	(Default: False)

	@features_set object: (optional)The set with curves, edges or cons that will be captured by 
	the wrap.

	@returns integer: Returns 0 if the wrap is created succesfully and 1 otherwise.

	"""

def CavityVolumeTetra( shells, maximum_length, growth_rate, sensors_set ):

	"""

	This function creates volume meshes for cavities, consisting of tetras.


	@shells object: A list of the input shells, that will define the volume boundary.

	@maximum_length float: The maximum element length of the created volume mesh.

	@growth_rate float: (optional)The growth rate of the created tetras towards the inner of the cavity.
	(Default: 1.5)

	@sensors_set object: (optional)The set that contains nodes that will be used also as nodes of the 
	volume mesh.

	@returns integer: Returns 0 if the volume mesh was created succesfully and 1 otherwise.

	"""

def CavityVolumeHexaInterior( shells, maximum_length, buffer_zones, sensors_set ):

	"""

	This function creates volume meshes for cavities, consisting of hexas in the interior, 
	some pentas and pyramids, and a zone of tetras near the boundary.


	@shells object: A list of the input shells, that will define the volume boundary.

	@maximum_length float: The maximum element length of the created volume mesh.

	@buffer_zones integer: (optional)The number of buffer zones, that will exist in the hexa interior mesh.
	(Default: 1)

	@sensors_set object: (optional)The set that contains nodes that will be used also as nodes of the 
	volume mesh.

	@returns integer: Returns 0 if the volume mesh was created succesfully and 1 otherwise.

	"""

def CavityVolumeHexaDominant(shells, boundary_length, maximum_length, nth_largest, buffer_zones, sensors_set, features_set, feature_angle):

	"""

	This function creates volume meshes for cavities, consisting of mostly hexas and a few pentas and tetras.


	@shells object: A list of the input shells, that will define the cavity to be 
	volume meshed with HexaDominant.

	@boundary_length float: The length of the elements of the volume near the volume 
	boundary.

	@maximum_length float: The maximum element length of the created volume mesh.
	The element length of the biggest hexas.

	@nth_largest integer: (optional)The number of the largest inner cavities that will be volume meshed.
	(Default: 1)

	@buffer_zones integer: (optional)The number of buffer zones, that will exist in the hexa dominant mesh.
	(Default: 1)

	@sensors_set object: (optional)The set that contains nodes that will be used also as nodes of the 
	volume mesh.

	@features_set object: (optional)The set of edges, that belong to the structure, that will be captured 
	by the volume.

	@feature_angle float: (optional)A limit angle for features to be captured by the volume.
	(Default: 60)

	@returns integer: Returns 0 if the volume mesh was created succesfully and 1 otherwise.

	"""

def ConstantWrap(entities, type, target_length, nth_largest, smooth_factor, mode, wrap_pid, shell_type, offset_factor, coordinate_system):

	"""

	This function creates constant length wraps.


	@entities object: A list of input entities.

	@type string: Defines whether the wrap will be outer or inner.
	Available options are "outer" and "inner", respectively.

	@target_length float: The target length of the final wrap mesh.

	@nth_largest integer: (optional)The number of the largest inner cavities that will be wrapped.
	This option is valid only when type = "inner".
	In case of type = "outer" it is ignored.
	(Default: 1)

	@smooth_factor float: (optional)A value between 0.0 - 1.0, that defines how smooth the result will be.
	When set to 0.0 the result will look like the initial octree with some pasted nodes.
	When set to 1.0 the result will be very smooth.
	(Default: 0.5)

	@mode string: (optional)Defines the positioning of the wrap compared to the structure.
	Available options are "nodes_out", "nodes_tight", "nodes_on_features", "shells_out", "free" and "castellated".
	- "nodes_out" means that the wrap nodes will lie out of the structure 
	   shells.
	- "nodes_tight" or "nodes_on_structure" means that the wrap nodes will lie exactly on the 
	   structure shells.
	- "nodes_on_features" means that the wrap nodes will try to lie on features.
	- "shells_out" means that the whole shells of the wrap will lie out of the 
	   structure shells.
	- "free" means that the nodes will lie in the most suitable position to achieve 
	   better smoothness, regardless their positioning compared to the structure.
	- "castellated" means that the node will lie at the initial octree positions.
	(Default: "nodes_out")

	@wrap_pid string: (optional)Defines the PID that will be assigned to the created wrap.
	Available options are "from_structure" and "new".
	- "from_structure" means that each wrap shell will have the same PID 
	   with its closest structure shell.
	- "new" means that a new PID will be creates for each new wrap.
	- "new_single_per_volume" means that each separate volume will have a single new property.
	(Default: "from_structure")

	@shell_type string: (optional)Defines the shell type of the result mesh.
	Available options are "trias" and "quads".
	- "trias" for tria mesh result.
	- "quads" for quad mesh result.
	(Default: "trias")

	@offset_factor integer: (optional)Option to inflate the wrap mesh away from the surface by a factor times the wrap length.

	@coordinate_system object: (optional)The coordinate system that the wrap result will be aligned with.

	@returns integer: Returns 0 if the wrap was created succesfully and 1 otherwise.

	"""

def IsolateSkin( type, leak_length, nth_largest, group_entities, separate_at_blue_bounds, separate_at_pid_bounds, feature_angle, feature_type, mpar_file ):

	"""

	This function isolates on the screen all the inner or outer wetted entities of the visible model.


	@type string: Defines whether the entities that will be kept are outer or inner.
	Available options are "outer", "inner" and "seed_points".

	@leak_length float: The maximum length gaps that the algorithm will not intrude.
	The octree voxel length.

	@nth_largest integer: (optional)The number of the largest inner cavities that will be isolated.
	This option is valid only when type = "inner".
	In case of type = "outer" or type = "seed_points"  it is ignored.
	(Default: 1)

	@group_entities boolean: (optional)If set to True, the entities will be isolated as whole connectivity groups.
	If set to False, each entity will be isolated separately.
	(Default: False)

	@separate_at_blue_bounds boolean: (optional)If set to True, then regions connected via triple bounds are placed into 
	separate connectivity groups.
	If set to False, then all connected entities are placed into the same group.
	This option is valid only when group_entities = True.
	In case of group_entities = False it is ignored.
	(Default: True)

	@separate_at_pid_bounds boolean: (optional)If set to True, then all entities contained in a connectivity group 
	will have the same PID.
	If set to False, then each connectivity group can contain connected 
	entities with different PIDs.
	This option is valid only when group_entities = True.
	In case of group_entities = False it is ignored.
	(Default: True)

	@feature_angle float: (optional)The feature angle limit in degrees.
	If this value is exceeded, the groups get separated at this feature line.
	Valid values are 0 - 180.
	If set to 0 then feature line separation is disabled.
	This option is valid only when group_entities = True.
	In case of group_entities = False it is ignored.
	(Default: 60)

	@feature_type string: (optional)Specifies the type of the feature lines in which the connectivity 
	groups will be separated.
	Groups get separated at the examined bound only if feature_angle 
	is exceeded and the feature type is of the specified type.
	Available options are "convex", "concave" and "convex_and_concave".
	This option is valid only when group_entities = True and feature_angle > 0.
	In case of group_entities = False or feature_angle = 0 it is ignored.
	(Default "convex_and_concave")

	@mpar_file string: (optional)The path of the file containing the parameters. If such a file is given, 
	its parameters will be consider as dominant over the given ones. 
	For example, given 'type' and 'leak_length' will be replaced if the 
	mpar_file contains these parameters.

	@returns integer: Returns 0 if the isolation is completed succesfully and 1 otherwise.

	"""

def HexaBlockAutoCFDSpacing(input, growth_rate, feature_angle, min_length, max_length, sharp_edges_angle_limit, convex_sharp_edges_length, convex_sharp_edges_length_mode, concave_sharp_edges_length, concave_sharp_edges_length_mode):

	"""

	This function can be used to apply automatically curvature dependant 
	perimeter nodal spacing for CFD applications. Algorithm works according 
	to the input parameters. If parameters are not defined, default values 
	are used.


	@input object: Box edges where the "Auto CFD Spacing" algorithm will be applied to.

	@growth_rate float: (optional)Geometric factor of element length growth.

	@feature_angle float: (optional)The maximum allowed angle between neighboring edges or shells, 
	for the curvature resolution.

	@min_length float: (optional)The minimum length of the mesh.

	@max_length float: (optional)The maximum length of the mesh.

	@sharp_edges_angle_limit float: (optional)The sharp edges angle limit.

	@convex_sharp_edges_length float: (optional)The length on identified convex sharp edges.

	@convex_sharp_edges_length_mode string: (optional)Takes the values "absolute" or "local_length" to define the way that 
	the convex sharp edges length will be calculated.

	@concave_sharp_edges_length float: (optional)The length on identified concave sharp edges.

	@concave_sharp_edges_length_mode string: (optional)Takes the values "absolute" or "local_length" to define the way that 
	the concave sharp edges length will be calculated.

	@returns: Nothing is returned.

	"""

def PointCloudMesh (points, algorithm):

	"""

	This function will create shell mesh elements on a cloud of points or grids.
	Element type (Mixed, Tria, Quad, OrthoTria) will respect the mesh parameters value.


	@points object: List of reference to points or grids.

	@algorithm string: (optional)Defines the algorithm that will run.
	Options are "free", "terrain" and "manifold".

	@returns object: Returns a list with the created shells on success, or None on error.

	"""

def CreateTransitionZones (boxes, box_faces, direction, element_ratio):

	"""

	This function can be used to create transition zones 
	in hexa-block topology in order to coarsen the mesh.


	@boxes object: A list containing the hexa-block boxes.

	@box_faces object: A list containing the box faces that correspond to the 
	model's transition zones.

	@direction string: Defines the direction of the transition zones and it takes 
	the value "inwards" (coarsening is applied inside the input 
	boxes) or "outwards" (coarsening is applied outside the 
	input boxes).

	@element_ratio object: A dictionary containing pairs of box edge and the 
	element ratio (e.g. '2-1', '3-1').

	@returns object: Always returns None.

	"""

def ModifyTransitionZones(element_ratio):

	"""

	This function can be used to modify existing transition zones in hexa-block topology.


	@element_ratio object: A dictionary containing pairs of box edge objects and their element ratio ('2-1', '3-1').
	(See the example)

	@returns object: Always returns None.

	"""

def RemoveTransitionZones(box_faces):

	"""

	This function can be used to remove existing transition zones from a hexa-block topology.


	@box_faces object: A list containing the box faces to remove from the transition zones.

	@returns object: Always returns None.

	"""

def CheckSkin(skin, solid_description, distance, create_points):

	"""

	This function checks how good is the result of Skin function.


	@skin object: A list of input entities that is the skin representation of the 
	model (the result of the Skin function).

	@solid_description object: A list of input entities that is the solid description of the 
	model (the input of the Skin function).

	@distance float: The maximum distance from the correct position within which 
	the result will be considered good.

	@create_points boolean: (optional)If set to True points will be created at areas where the result is not good.
	(Default: False)

	@returns object: Returns a list with 2 values that range between 0 and 1.
	The first one represents the area percentage of the result model that is good 
	according tothe middle position.
	The second one represents the perimeter percentage of the result model that is 
	good according the position of the single bounds.

	"""

def CheckMiddleSurface(middle_surface, solid_description, middle_deviation_value, middle_deviation_type, bounds_deviation_value, bounds_deviation_type, thickness_deviation_value, thickness_deviation_type, check_missing_middle, exclude_near_junctions, l_junction_angle):

	"""

	This function checks if a middle surface is good compared to the solid description,
	concerning the following:
	-The positioning of the middle.
	-The positioning of the bounds.
	-The thickness.
	-The missing middle areas.
	-The missing solid description areas.
	-The volume deviation.


	@middle_surface object: A list of input entities that is the middle surface of the model.

	@solid_description object: A list of input entities that is the solid description of the model.

	@middle_deviation_value float: (optional)The maximum distance from the exact middle position in order 
	to be considered as good.
	(Default: 0.05)

	@middle_deviation_type string: (optional)Defines if the middle_deviation_value is an absolute value or a 
	percentage of the thickness.
	Available options are "absolute" and "thickness_percentage".
	(Default: "thickness_percentage")

	@bounds_deviation_value float: (optional)The maximum distance from the exact position of bounds in order 
	to be considered as good.
	(Default: 0.05)

	@bounds_deviation_type string: (optional)Defines if the bounds_deviation_value is an absolute value or a 
	percentage of the thickness.
	Available options are "absolute" and "thickness_percentage".
	(Default: "thickness_percentage")

	@thickness_deviation_value float: (optional)The maximum difference between the current and the correct 
	thickness in order to be considered as good.
	(Default: 0.05)

	@thickness_deviation_type string: (optional)Defines if the thickness_deviation_value is an absolute value or 
	a percentage of the thickness.
	Available options are "absolute" and "thickness_percentage".
	(Default: "thickness_percentage")

	@check_missing_middle boolean: (optional)Defines if the check is going to search for areas of missing 
	middle surface.
	(Default: True)

	@exclude_near_junctions boolean: (optional)Defines whether the check is going to exclude problematic areas 
	that are near junctions or not.
	(Default: True)

	@l_junction_angle float: (optional)Defines the limit angle over which the bounds are going to be 
	considered as L junctions.
	(Default: 60)

	@returns object: Returns an object with 6 values.
	-middle_deviation_area represents the area of the model that was identified as not good, 
	 according to the positioning in the middle of the solid description.
	-bound_deviation_area represents the area of the model that was identified as not good, 
	 according to the positioning of the bound.
	-thickness_deviation_area represents the area of the model that was identified as 
	 not good, according to the thickness.
	-missing_middle_area represents the area of the solid description of the model 
	 that was identified that has no corresponding middle.
	-failed_to_check_area represents the area of the the model that failed to check.
	-volume_deviation represents the difference between the volume of the solid description 
	 and the volume that has the middle surface taking into acount its thickness values.

	"""

def SolidSmooth(solids, freeze_skin):

	"""

	This function applies IMPROVE>SMOOTH on solid elements.


	@solids object: A list of solid objects.

	@freeze_skin boolean: (optional)Freeze the volume skin.
	(Default: "True")

	@returns integer: Returns 0 in any case.

	"""

def OrientVolume(volume):

	"""

	This function orients all the elements of the volume so that they all point inwards (gray side).


	@volume object: The volume that is going to be oriented.

	@returns integer: Returns 1 on success ,0 otherwise.

	"""

def SplitQuads(entities, method):

	"""

	This function applies ELEMENTS>SPLIT QUADS on shells and solid facets.


	@entities object: Accepted values: A list of shells and/or solid facets, "all", "visible", 0.
	If set to 0 or "all", runs for all shells of the database.
	If set to "visible," runs for visible shells.

	@method string: (optional)Defines the split method.
	Can be: "oriented_hybrid", "oriented_1", "oriented_2", "quality_based" or "violating".
	(Default: "oriented_hybrid")

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def BatchGenerator(entities):

	"""
	Deprecated since version 22.0.0.

	Uses the Batch generator for user input entities.


	@entities object: A list of properties, parts, shells or faces.
	If 0 is specified, the function works on visible faces.

	@returns integer: Always returns 0.

	"""

	import warnings; warnings.warn("Deprecated since version 22.0.0.", DeprecationWarning)

def ApplyOctreeFilters(octree):

	"""

	This function applies the defined filters, in order to load the wanted parts, groups or pids to the octree scenario.
	It also distributes them to the proper area if needed.


	@octree object: The input octree entity.

	@returns boolean: Returns True if the process completed succesfully and False otherwise.

	"""

def RunOctree(octree):

	"""

	This function runs the defined octree.


	@octree object: The input octree entity.

	@returns boolean: Returns True if the process completed succesfully and False otherwise.

	"""

def ApplyAutoAssociation(distance, box_points, box_edges, box_faces, work_on_visible, cut_geometric_faces, connect_to_cons, insert_hot_points):

	"""

	A function that automatically associates the input Hexa-Block entities.


	@distance float: Maximum distance to search for geometric entities 
	that will be associated to the input Hexa-Block entities.

	@box_points object: (optional)The box points to associate.

	@box_edges object: (optional)The box edges to associate.

	@box_faces object: (optional)The box faces to associate.

	@work_on_visible boolean: (optional)If set to True, the function will search for geometric entities
	only in visible entities. If it is set to False (default value), the 
	function will search for geometric entities in the whole database.

	@cut_geometric_faces boolean: (optional)If set to True, the target geometric faces will be cut
	on the position of the input box edges (after projecting 
	them to the geometric faces).
	(Default: False)

	@connect_to_cons boolean: (optional)If set to True, connects the nodes of the box edges to 
	the associated Cons, after meshing the boxes.
	(Default: False)

	@insert_hot_points boolean: (optional)If set to True, inserts hot points on the position of edges 
	start/end points (after projecting them to the geometric CONS).
	(Default: False)

	@returns integer: Always returns 1.

	"""

def ProjectShellsOnShells(source, target, projection_tolerance, maximum_projections_number, user_projection_mode_vector, number_of_shell_zones_affected, move_projection_to_nearest_perimeter, move_to_projected_shells, paste_projected_and_result_shells, add_results_to_set, join_perimeters_mode, cut_faces_on_boundary, open_closed_perimeter_hole, freeze_non_single_boundary):

	"""

	This function projects a group of shells on another group of shells.


	@source object: The shells that will be projected. It can be an object or an array of objects, parts, properties, materials, sets or macros.
	If the INPUT is "visible", the visible shells are collected.

	@target object: The shells that the source shells be projected on. It can be an object or an array of objects, parts, properties, materials, sets or macros.
	If the INPUT is "visible", the visible shells are collected.

	@projection_tolerance float: (optional)Maximum distance between the projection and the projected entities.

	@maximum_projections_number integer: (optional)Maximum number of projections on the target shells.

	@user_projection_mode_vector object: (optional)A list of floating point numbers to define the user project vector.

	@number_of_shell_zones_affected integer: (optional)Number of shell zones around projection to be affected.

	@move_projection_to_nearest_perimeter float: (optional)Maximum distance between projections and near perimeters.

	@move_to_projected_shells float: (optional)Between 0. and 1. Parameter to move the result shells towards the projected.

	@paste_projected_and_result_shells integer: (optional)Can be 1 or 2. 1 means that the nodes of the result shells and the projected will be pasted and two that their coordinates will be matched

	@add_results_to_set string: (optional)Name of existing set where the result shells will be stored. If the set doesn't exist, a default set will be created.

	@join_perimeters_mode integer: (optional)Can be 0, 1 or 2. 0 means that reshape will be called and perimeters that interfere with the projectiuon will be joined to create a compatible mesh. 1 means that the algorithm will try to maintain the perimeters by snapping the projection onto them and if it fails they will be joined. 2 means that no perimeters will be joined and only snap will be performed where possible

	@cut_faces_on_boundary boolean: (optional)Determines whether the result shells will cut the geometry on their boundary

	@open_closed_perimeter_hole boolean: (optional)Determines whether a hole will be opened on the target shells if a red bound opening is projected on them

	@freeze_non_single_boundary boolean: (optional)Determines whether an additional zone of elements will be 
	added automatically so as to not have frozen edges in the 
	initial selection.

	@returns integer: This function always returns 1

	"""

def ProjectPointsOnShells(shells, points, projection_tolerance, maximum_projections_number, user_projection_mode_vector, number_of_shell_zones_affected, move_projection_to_nearest_perimeter, move_to_projected_points, paste_projected_and_result_points, add_results_to_set, mark_result_macro_grids):

	"""

	This function projects points or nodes on shells


	@shells object: It is the shells on which the points will be projected. It can be an object or an array of objects, parts, properties, materials, sets or macros.
	If the INPUT is "visible", the visible shells are collected.

	@points object: It can be an object or a list of points or nodes

	@projection_tolerance float: (optional)Maximum distance between the projection and the projected entity.

	@maximum_projections_number integer: (optional)Maximum projection number on the target shells

	@user_projection_mode_vector object: (optional)A list of vector components to define the user projection vector.

	@number_of_shell_zones_affected integer: (optional)Number of shell zones around projection to be affected.

	@move_projection_to_nearest_perimeter float: (optional)Maximum distance between projections and near perimeters.

	@move_to_projected_points float: (optional)Between 0. and 1. Parameter to move the result towards the projected points

	@paste_projected_and_result_points integer: (optional)Can be 1 or 2. 1 means that the projected and result nodes will be pasted and 2 that only their positions will be matched

	@add_results_to_set string: (optional)Name of an existing set to store the projected nodes. If the set doesn't exist, a default one will be created.

	@mark_result_macro_grids boolean: (optional)Determines whether the result nodes will become spots if they belong to macros

	@returns integer: This function always returns 1

	"""

def HexaBlockSmooth(boxes, feature_lines, smooth_iterations, fix_violating_solids):

	"""

	Smooth Hexa-Block boxes.


	@boxes object: The boxes to be smoothed.

	@feature_lines object: (optional)A list of box edges that define the model's feature lines. If no
	box edges are defined as feature lines, default feature lines
	will be used (according to the feature line angle).

	@smooth_iterations integer: (optional)The number of iterations that define the smoothing of neighboring solids. 
	More iterations result in smoother (shell/solid) mesh. If it is not defined, 
	default value will be used.

	@fix_violating_solids boolean: (optional)A flag to activate a mechanism that fixes solids having 
	intersections or negative volume.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def CheckOctreeLeaks(octree):

	"""

	This function builds the defined octree entity and creates curves if there are any leaks.


	@octree object: The input octree entity.

	@returns boolean: Returns True if there are any leaks and False otherwise

	"""

def ConvertToLightVolumeRepresentation(volumes):

	"""

	This function will convert volumes to Light Volume Representation.
	Input volumes must have attached shells on their boundary.


	@volumes object: (optional)A list of ansa volumes (if not given all volumes of the db will be converted).

	@returns integer: Returns 0 on success, non zero on error, where:
	
	0: Success
	1: Failure: No valid volumes were found for conversion.
	2: Failure: Found volume without shells on boundary.

	"""

def CollapseViolating():

	"""

	Collapses violating elements.


	@returns object: Always returns none.

	"""

def RotatingInterface( rotating_entities, static_entities, offset, start_x, start_y, start_z, end_x, end_y, end_z, offset_type, minimum_offset, vertical_intersection_entities, vertical_intersection_points, fill_concavities, auto_axis_calc , planar_external_direction ):

	"""

	Automatic creation of the sliding interface boundary for rotating volume mesh around wheels.
	Intersections between rotating and static entities should be avoided.


	@rotating_entities object: A list of ansa entities.
	These entities must be faces or shells.

	@static_entities object: A list of ansa entities.
	These entities must be faces or shells.

	@offset float: Offset value of rotating interface from rotating entities.

	@start_x float: X coordinate of rotation axis start.

	@start_y float: Y coordinate of rotation axis start.

	@start_z float: Z coordinate of rotation axis start.

	@end_x float: X coordinate of rotation axis end.

	@end_y float: Y coordinate of rotation axis end.

	@end_z float: Z coordinate of rotation axis end.

	@offset_type string: Offset type.
	Available options are "max_clearance" and "average_clearance" respectively.

	@minimum_offset float: Minimum offset from rotating entities that the rotating interface should respect.

	@vertical_intersection_entities object: (optional)A list of ansa entities.
	These entities must be faces or shells.

	@vertical_intersection_points object: (optional)A list of ansa entities.
	These entities must be nodes or hotpoints.

	@fill_concavities boolean: (optional)Fill concavities option.
	False disabled , True enabled.

	@auto_axis_calc boolean: (optional)Automatic axis calculation option.
	False disabled , True enabled.

	@planar_external_direction object: (optional)Define external direction in case of planar interface at the external of the wheel.

	@returns object: Returns an object containing the following:
	ret.status                       : (integer)  0 on succes , 1 if intersections are detected , 2 if minimum offset is 
	                                    violated , 3 if HOT POINTS and CONS matching distance is violated , 4 if HOT 
	                                    POINTS matching distance is violated , 5 if CONS matching distance is violated , 
	                                    6 if offset distance is too big , 7 if axis cannot calculated automatically.
	ret.result_faces                 : (list)     A list with the created faces of the sliding interface.
	ret.errors_intersections_set     : (ANSA Set) If intersections are detected a set with the intersected shells is returned.
	ret.minimum_offset_violation_set : (ANSA set) If minimum offset violations are detected a set with the violating region is                                    returned.
	ret.minimum_offset_found         : (float) If minimum offset violations are detected the possible minimum offset is                                           returned.

	"""

def Create4SidedMesh(entities, only_4sided, only_aligned, corner_angle, smooth_type, split_method, spacing):

	"""

	This function uses 4 Sided mesh generator to produce 4-sided mapped mesh.
	It works for both macros and FE shells.


	@entities object: A list of faces and/or shells.
	If entities equals to 0, the visible faces and shells are used

	@only_4sided boolean: (optional)If set to True, only macros identified as 4-sided are meshed.

	@only_aligned boolean: (optional)If set to True, only macros with same number of nodes at opposite sides are meshed.

	@corner_angle float: (optional)The supplementary angle between perimeters used for corner identification
	If not defined, the default value is used

	@smooth_type string: (optional)Smooth type can be one of the following strings:
	- 'standard'
	- 'isoparametric'
	If not defined, the default value is used.

	@split_method string: (optional)Split quads method can be one of the following strings:
	- 'hybrid'
	- 'oriented1'
	- 'oriented2'
	- 'quality_based'
	- 'none'
	If not defined, the default value is used.

	@spacing string: (optional)Spacing option can be one of the following strings:
	- 'off'
	- 'isospace'
	- 'map_opposite_sides'
	if not defined, the default value is used.

	@returns anything: Always retuns None.

	"""

def CreateCircularMesh(entities, only_circular, only_even, radius_tol, pattern, zones, layers, first_height, growth_factor, max_aspect):

	"""

	This function uses Circular mesh generator to produce mesh patterns for circular areas.
	It works for both macros and FE shells.


	@entities object: A list of faces and/or shells.
	If entities equals to 0, the visible faces and shells are used.

	@only_circular boolean: (optional)If set to True, only macros identified as circular are meshed.

	@only_even boolean: (optional)If set to True, only macros with even number of perimeter nodes are meshed.

	@radius_tol boolean: (optional)The maximum deviation percentage (%) between 
	actual min/max radius and the radius of the equivalent circle.
	If not defined, the default value is used.

	@pattern string: (optional)Pattern can be one of the following strings:
	- 'default'
	- 'o-grid'
	- 'radial'
	If not defined, the default value is used.

	@zones integer: (optional)The desired number of zones around mesh pattern.
	If not defined, the default value is used, in case that the
	corresponding check box in Circular Mesh Wizard is enabled.
	This option is taken into account, only if pattern is default or o-grid.

	@layers integer: (optional)The desired number of layers around o-grid mesh pattern.
	If not defined, the default value is used, in case that the 
	corresponding check box in Circular Mesh Wizard is enabled.
	This option is taken into account, only if pattern is o-grid.

	@first_height float: (optional)The width of the first layer zone.
	If not defined, the default value is used.
	It is taken into account, only in cases that layers option works.

	@growth_factor float: (optional)The growth factor applied on layers' width successively.
	If not defined, the default value is used.
	It is taken into account, only in cases that layers option works.

	@max_aspect float: (optional)The maximum accepted aspect of elements in layers.
	If not defined, the default value is used.
	It is taken into account, only in cases that layers option works.

	@returns anything: Always returns None.

	"""

def VolumesCheckDefinition(volume):

	"""

	The function checks if the volume definition is valid for mesh generation


	@volume object: The volume to be checked

	@returns integer: Returns 1 in case the definition is ok or 0 otherwise

	"""

def AddFilterToOctreeArea(field, expression, value, area, match, case_sensitive, filter_name):

	"""

	The function adds a filter to an existing octree entity or octree area, much like the way it is done through the Octree.
	If the area has an active filter, a new row is added to that filter. Otherwise, a new filter is created and is set as active.


	@field string: Field Name.

	@expression string: Expression.

	@value string: The value that the expression will evaluate.

	@area object: The octree area or octree entity the filter will be added into.

	@match string: (optional)Determines if all the filter rows must be matched. Use "all" or "any" to change 
	the value.

	@case_sensitive string: (optional)Determines if the filter will be case sensitive. Use "yes" or "no" to change 
	the value.

	@filter_name string: (optional)Give a specific name to a filter.

	@returns integer: Returns 1 if the filter was successfully created, or 0 otherwise.

	"""

def AddPartsToOctreeArea( entities, area ):

	"""

	This function adds a list of properties or parts or groups to an octree area or an otcree entity.


	@entities object: References the entities to be added to the area. The type of the entities may be a part, group or property.

	@area object: The octree area or the octree entity the entities will be added to.

	@returns integer: Returns 1 if the entities and the area are valid entities, or 0 otherwise.

	"""

def GetNewOctreeArea(parent_octree, name, min_len, max_len, max_vol_len, part_pid_proximity, self_proximity):

	"""

	This function adds a new octree area in an octree entity.


	@parent_octree object: References the octree entity where the area will be added.

	@name string: (optional)The name of the octree parameters of the created area.

	@min_len float: (optional)Area specific minimum length value.

	@max_len float: (optional)Area specific maximum length value.

	@max_vol_len float: (optional)Area specific maximum volume length value.

	@part_pid_proximity boolean: (optional)Enables proximity refinement between different parts/properties.

	@self_proximity boolean: (optional)Enables self-proximity refinement in a part/property.

	@returns object: Returns a reference to the newly created area.
	In case of an error, the function returns None.

	"""

def GetPartsFromOctreeArea( area ):

	"""

	This function collects all the parts, groups or properties that are included in a specific octree area or an  octree entity.


	@area object: The octree area or the octree entity that its items will be returned.

	@returns object: Returns a list containing all the parts, groups or properties that belong to the specific octre area or octree entity.
	In case the octree area is not valid or it does not contain any parts, an empty list is returned.

	"""

def GetAreasFromOctree( octree ):

	"""

	The function collects all areas belonging to a particular octree entity.


	@octree object: References the octree entity under consideration.

	@returns object: Returns a list containing all the areas that belong to the specific octree entity.
	In case octree is not valid or it does not contain any areas, an empty list is returned.

	"""

def ReadOctreeAreaParams( area, mpar_file ):

	"""

	This function reads octree parameters from a specific file and assigns them to an octree area or to an octree entity.


	@area object: References the octree area or the octree entity that will get the values.

	@mpar_file string: The path of the file containing the parameters.

	@returns integer: Returns 1 if area is valid and the file exists, or 0 otherwise.

	"""

def SaveOctreeAreaParams( area, mpar_file ):

	"""

	This function saves octree parameters of an octree area or an octree entity to a specific file.


	@area object: References the octree area or the octree entity that will get the values.

	@mpar_file string: The path of the file that the parameters will be saved to.

	"""

def RotatingInterfaceAxis( rotating_entities ):

	"""

	Automatic calculation of the axis of rotation of wheels. 
	The function calculates the axis of rotation even if the wheel is not whole usually in case of scanned wheels.


	@rotating_entities object: A list of ansa entities.
	These entities may be faces or shells.

	@returns object: Returns the axis of rotation with a curve in case of success.
	Returns None in case of failure.

	"""

def HexaBlockSetIjk( box, origin_hb_pnt, i_hb_pnt ):

	"""

	Sets to box a coordinate system by setting the origin and i hexablock point. The
	origin and i point must be on the same edge. The rest of the vectors of the 
	coordinate system are calculated from the previous points. The box can be only
	HEXA.


	@box object: The HEXA_BOX which the coordinate system will be 
	set. The box can be only hexahedral.

	@origin_hb_pnt object: The HEXA_BOX_POINT from which the coordinate system 
	will start.

	@i_hb_pnt object: The HEXA_BOX_POINT to which the vector I will 
	end.

	@returns boolean: Returns True if the operation was successful.

	"""

def HexaBlockAlignIjk( guide_box, boxes_to_align ):

	"""

	Aligns HEXA_BOX entities according to guide_box. If the topology of boxes is not
	structured then no alignment will be applied.


	@guide_box object: Sets the guide box that the rest of the boxes will be 
	aligned with.

	@boxes_to_align object: List of HEXA_BOX entities that are going to be aligned with the guide box.

	@returns boolean: Returns true if the procedure is successful.

	"""

def HexaBlockResetIjk( boxes ):

	"""

	Resets Ijk coordinate system to the default one.


	@boxes object: List of HEXA_BOX that are going to be reset.

	@returns: Returns none.

	"""

def LeakTool( mpar_file, sampling_length, group_leaks, close_leaks, chosen_properties ):

	"""

	This function detects leaks, providing the ability to group and close them.


	@mpar_file string: The path of the file containing the parameters.

	@sampling_length float: Minimum target length of octree on the surface of the model.

	@group_leaks boolean: (optional)Group leaks by properties and parts.
	False disabled, True enabled. Default value: False.

	@close_leaks boolean: (optional)Close detected leaks.
	False disabled, True enabled. Default value: False.

	@chosen_properties object: (optional)An array of sets of properties where leaks are biased to be identified and closed.

	@returns boolean: Returns True if there are any leaks and False otherwise.
	Returns None if not a mpar_file exists.

	"""

def AddContentsToSizeFieldRule( entities, rule ):

	"""

	This function adds a list of entities to a SizeField rule.
	


	@entities object: References the entities to be added to the rule. The type of the entities may be a part, group,  property, curve, point or sizebox.

	@rule object: The SizeFIeld rule the entities will be added to.

	@returns boolean: Returns True if the entities and the rule are valid entities, or False otherwise.

	"""

def GetContentsFromSizeFieldRule( rule ):

	"""

	This function collects all the contents that are included in a specific SizeField rule.
	


	@rule object: The SizeField rule that its items will be returned.

	@returns: Returns a list containing all the entities that belong to the specific SizeField rule.
	In case the SizeField rule is not valid or it does not contain any contents an empty list is returned.

	"""

def SaveSizeFieldRuleParams( rule , mpar_file ):

	"""

	This function saves parameters of of a SizeField rule to a specific file.
	


	@rule object: References the SizeField rule that will get the values.

	@mpar_file string: The path of the file that the parameters will be saved to.

	"""

def ReadSizeFieldRuleParams( rule, mpar_file ):

	"""

	This function reads parameters from a specific file and assigns them to a SizeField rule.
	


	@rule object: References the SizeField rule that will get the values.

	@mpar_file string: The path of the file containing the parameters.

	@returns boolean: Returns True if rule is valid and the file exists, or False otherwise.

	"""

def AddFilterToSizeFieldRule(field, expression, value, rule, match, case_sensitive, filter_name):

	"""

	The function adds a filter to an existing SizeField rule, much like the way it is done through the Octree.
	If the area has an active filter, a new row is added to that filter. Otherwise, a new filter is created and is set as active.


	@field string: Field Name.

	@expression string: Expression.

	@value string: The value that the expression will evaluate.

	@rule object: The SizeField rule the filter will be added into.

	@match string: (optional)Determines if all the filter rows must be matched. Use "all" or "any" to change

	@case_sensitive string: (optional)Determines if the filter will be case sensitive. Use "yes" or "no" to change

	@filter_name string: (optional)Give a specific name to a filter.

	@returns integer: Returns 1 if the filter was successfully created, or 0 otherwise.

	"""

def GetRulesFromSizeField( size_field ):

	"""

	The function collects all rules belonging to a particular SizeField entity.
	


	@size_field object: References the SizeField entity under consideration.

	@returns: Returns a list containing all the rules that belong to the specific SizeField entity.
	In case SizeField is not valid or it does not contain any rules, an empty list is returned.

	"""

def BuildSizeField( size_field ):

	"""

	This function builds the defined SizeField.
	


	@size_field object: The input SizeField entity.

	@returns boolean: Returns True if the process completed succesfully and False otherwise.

	"""

def GetNewSizeFieldClosedSurfaceRule( size_field, name, max_surf_len, max_vol_len ):

	"""

	This function adds a new closed surface rule in a SizeField entity.
	


	@size_field object: References the SizeField entity where the rule will be added.

	@name string: (optional)The name of the rule parameters of the created rule.

	@max_surf_len float: (optional)Rule specific maximum surface length value.

	@max_vol_len float: (optional)Rule specific maximum volume length value.

	@returns: Returns a reference to the newly created rule.
	In case of an error, the function returns None.

	"""

def GetNewSizeFieldSurfaceOffsetRule( size_field, name, max_surf_len, max_vol_len , offset ):

	"""

	This function adds a new surface offset rule in a SizeField entity.
	


	@size_field object: References the SizeField entity where the rule will be added.

	@name string: (optional)The name of the rule parameters of the created rule.

	@max_surf_len float: (optional)Rule specific maximum surface length value.

	@max_vol_len float: (optional)Rule specific maximum volume length value.

	@offset float: (optional)Rule specific offset value.

	@returns: Returns a reference to the newly created rule.
	In case of an error, the function returns None.

	"""

def GetNewSizeFieldCylinderRule( size_field, name, max_surf_len, max_vol_len ,radius ):

	"""

	This function adds a new cylinder rule in a SizeField entity.
	


	@size_field object: References the SizeField entity where the rule will be added.

	@name string: (optional)The name of the rule parameters of the created rule.

	@max_surf_len float: (optional)Rule specific maximum surface length value.

	@max_vol_len float: (optional)Rule specific maximum surface length value.

	@radius float: (optional)Rule specific radius value.

	@returns: Returns a reference to the newly created rule.
	In case of an error, the function returns None.

	"""

def GetNewSizeFieldSphereRule( size_field, name, max_surf_len, max_vol_len , radius ):

	"""

	This function adds a new sphere rule in a SizeField entity.
	


	@size_field object: References the SizeField entity where the rule will be added.

	@name string: (optional)The name of the rule parameters of the created rule.

	@max_surf_len float: (optional)Rule specific maximum surface length value.

	@max_vol_len float: (optional)Rule specific maximum volume length value.

	@radius float: (optional)Rule specific radius value.

	@returns: Returns a reference to the newly created rule.
	In case of an error, the function returns None.

	"""

def GetNewSizeFieldSizeBoxRule( size_field, name, max_surf_len, max_vol_len ):

	"""

	This function adds a new sizebox rule in a SizeField entity.
	


	@size_field object: References the SizeField entity where the rule will be added.

	@name string: (optional)The name of the rule parameters of the created rule.

	@max_surf_len float: (optional)Rule specific maximum surface length value.

	@max_vol_len float: (optional)Rule specific maximum volume length value.

	@returns: Returns a reference to the newly created rule.
	In case of an error, the function returns None.

	"""

def SetSizeFieldRuleActive( rule, active ):

	"""

	This function sets a SizeField rule active.
	


	@rule object: References the SizeField rule to set active.

	@active boolean: True to activate the rule, False to de-activate the rule

	@returns: In case of an error, the function returns None.

	"""

def IsSizeFieldRuleActive( rule ):

	"""

	This function checks if a SizeField rule is active.
	


	@rule object: References the SizeField rule to check if active.

	@returns boolean: Returns True if active , False if not active
	In case of an error, the function returns None.

	"""

def SmoothShells(shells):

	"""

	The function perfrorms Smooth on shells given by the user.


	@shells object: A list with the shells to be smoothed.

	@returns integer: Returns 0 in all cases.

	"""

def TurbomachineryTemplate(parameters):

	"""

	A function to create a turbomachinery topology with the input parameters.


	@parameters string: A file that contains all the parameters of the template.

	@returns boolean: Returns True on success, False on failure.

	"""

def CloseOctreeLeaks( octree, chosen_properties ):

	"""

	This function closes automatically all detected octree leaks in order to make the model watertight.


	@octree object: The input octree entity.

	@chosen_properties object: (optional)An array of sets of properties where leaks are biased to be identified and closed.

	@returns boolean: Returns True if managed to make the model watertight.
	Returns False if did not manage to build the octree entity.

	"""

def Outline( dir_x, dir_y, dir_z ):

	"""

	Creates curves from the external outilne of a projected geometry on given plane


	@dir_x float: X coordinate of plane vector

	@dir_y float: Y coordinate of plane vector

	@dir_z float: Z coordinate of plane vector

	@returns object: Returns an object containing the following:
	ret.frontal_area_curves :(list)A list with the created curves of skins of the projected geometries.  
	ret.gaps_holes_curves   :(list)A list with the created curves of gap/hole skins of the projected geometries.
	ret.frontal_area_filled :(float)Frontal area with gap/holes filled.
	ret.frontal_area        :(float)Frontal area.
	ret.gaps_holes_area     :(float)Gaps/holes area

	"""

def GetFEPerimeterShells(fe_perimeters, expand_to_macro):

	"""

	This function returns the shells that lie on the edges of a FE perimeter. If "expand_to_macro" option is True, then it returns all the macro shells, grouped by macro.


	@fe_perimeters object: A list that contains FE perimeters. If it is set to 0, visible FE perimeters will be used.

	@expand_to_macro boolean: If it is set to True, all the macro shells will be returned.

	@returns object: If "expand_to_macro" option is False, it returns a list that contains all the shells that were found. If "expand_to_macro" option is True, then it returns a list of lists, that contain the macro shells grouped by macro.

	"""

def BuildAdaptivityField( adaptivity_field ):

	"""

	This function builds the defined AdaptivityField.


	@adaptivity_field object: The input AdaptivityField entity.

	@returns boolean: Returns True if the process completed succesfully and False otherwise.

	"""

def CreateNewAdaptivityField(name, scale_factor, min_length, max_length, symmetry_mirror):

	"""

	This function creates a new AdaptivityField entity


	@name string: (optional)Name of the newly created AdaptivityField

	@scale_factor float: (optional)Scale factor to convert units of adaptivity data

	@min_length float: (optional)Minimum length of adaptivity field

	@max_length float: (optional)Maximum length of adaptivity field

	@symmetry_mirror boolean: (optional)Option to mirror adaptivity data to the default symmetry plane

	@returns object: Returns the newly created AdaptivityField

	"""

def SetAdaptivityFieldCsvPath( adaptivity_field , csv_file_path ):

	"""

	This function sets the path of the csv file with the adaptivity data


	@adaptivity_field object: The input AdaptivityField entity

	@csv_file_path string: The path of the csv file with the adaptivity data

	"""

def SetAdaptivityFieldActive( adaptivity_field, active ):

	"""

	This function sets an AdaptivityField active.
	


	@adaptivity_field object: References the AdaptivityField to set active.

	@active boolean: True to activate the rule, False to de-activate the rule

	"""

def IsAdaptivityFieldActive( adaptivity_field ):

	"""

	This function checks if an AdaptivityField is active.
	


	@adaptivity_field object: References the AdaptivityField to check if active.

	@returns boolean: Returns True if active , False if not active
	In case of an error, the function returns None.

	"""

def ConvertSizeBoxesToSizeField( size_boxes , size_field ):

	"""

	This function converts all the SizeBoxes of the database or a list of given SizeBoxes to a new or given SizeField.
	


	@size_boxes object: (optional)List of SizeBoxes to convert to SizeField.

	@size_field object: (optional)Already existing SizeField to add the new SizeBox rules.

	@returns object: Returns the SizeField that the new SizeBox rules are added to on success.
	Returns None on failure.

	"""

def CopySizeFieldRules( rules , size_field ):

	"""

	The function copies given SizeField rules to another SizeField
	


	@rules object: A list of the SizeField rules to be copied.

	@size_field object: References the destination SizeField entity.

	@returns boolean: Returns True on success, False otherwise.

	"""

def MoveSizeFieldRules( rules , size_field ):

	"""

	The function moves given SizeField rules to another SizeField
	


	@rules object: A list of the SizeField rules to be moved.

	@size_field object: Destination SizeField entity.

	@returns boolean: Returns True on success, False otherwise.

	"""

def MergeSizeFields( size_fields ):

	"""

	The function merges a list of given SizeField entities
	


	@size_fields object: A list of SizeField entities to be merged.

	@returns object: Returns the merged SizeField entity

	"""

def SmoothHexaField(hexas, smooth_iterations):

	"""

	Smooths a given hexa field


	@hexas object: The hexas to be smoothed.

	@smooth_iterations integer: The number of smooth iterations

	@returns boolean: Returns True on success and False on failure.

	"""

def FillGapBridge(input, improve_result_zones, result_set, ret_ents):

	"""

	This function creates FE shells to fill a gap defined by cons, curves or edges.
	Each call of the function fills a single gap.
	A single gap defined only by curves can not be filled.


	@input object: A list of cons, curves, sets of edges.

	@improve_result_zones integer: (optional)Improves the quality of the result FE shells and [user defined] zones 
	around them.

	@result_set object: (optional)Adds the result FE shells to a [user defined] set.

	@ret_ents boolean: (optional)If set to True, a list with the created entities will be returned.

	@returns integer: Returns the number of the created FE shells (before mesh improvement).
	If ret_ents=True it will return a list with the created entities or None if no entities are created.

	"""

def ApplySizeFieldFilters(size_field):

	"""

	This function applies the defined filters, in order to load the wanted parts, groups or pids to the size field and distribute them to the proper rule.


	@size_field object: The input size field.

	@returns boolean: Returns True if the process completed succesfully and False otherwise.

	"""

def CheckMiddleMesh(shells, faces, options, check_for_unconnected, return_ents):

	"""

	This function checks middle mesh result taking into account both align constraints (if they exist) and real solid
	description. The following checks are performed:
	- Align Definition:
	        - Shells belonging to empty align area constraints are identified and reported
	        - Shells belonging to empty align perimeter constraints are identified and reported
	        - Position of shells' nodes with respect to correct middle position according to area align constraints.
	        - Shells' thickness with respect to thickness calculated from align constraints definition.
	        - Position of shells' nodes with respect to correct boundary position according to perimeter align constraints.
	- Middle Surface:
	        - Position of shells' nodes with respect to middle position calculated from solid description.
	        - Shells' thickness with respect to thickness calculated from solid description.
	        - Position of shells' nodes with respect to solid description boundaries.
	- Incompatible: checks if a shell's nodes belong to 2 or more align constraints with different align positions.
	- Missing Mass: identifies areas in model where middle mesh is not created for the solid description.
	- Unconnected: checks if there are shell mesh connectivity groups in model that are not connected properly with each other.


	@shells object: A list of shells for which checks will be performed.

	@faces object: A list of faces for which checks will be performed.

	@options object: (optional)A dictionary with options regarding which checks will be performed and the
	tolerance of those checks. Both key's ans value's type is string.
	Tolerance could be either absolute or a percentage of thickness values.
	When a tolerance value is left empty the default value is used.
	(Default: all checks with default tolerance values are performed)
	Example values:
	{ "align_middle" : "5%",
	  "align_boundary" : "0.15",
	  "align_thickness" : "5%",
	  "align_empty_areas" : "",
	  "align_empty_perimeters" : "",
	  "incompatible" : "10%",
	  "solid_middle" : "5%",
	  "solid_boundary" : "5%",
	  "missing_mass" : "" }

	@check_for_unconnected boolean: (optional)If set to True the check for unconnected shell mesh connectivity groups
	is performed. (Default: True)

	@return_ents boolean: (optional)If set to True a dictionary with a list of failed entities for every check
	performed is returned. (Default: True)

	@returns object: if return_ents is True then a dictionary with lists of entities for every check is returned, else None is returned.
	For the "unconnected" connectivity groups a list of lists of shells is returned in dictionary as a value.

	"""

def HexaSphere( sphere_center, sphere_radius, number_of_perimeter_elements, light_volume_representation, create_skin_shells, part, solids_property, shells_property ):

	"""

	Generates pure O-Grid Hexa mesh for spherical pattern.


	@sphere_center object: The coordinates of sphere's center.

	@sphere_radius float: The radius of sphere.

	@number_of_perimeter_elements integer: The number of peripheral edges. It must be a positive integer and 
	multiple of 4.

	@light_volume_representation boolean: (optional)Create light solids. Optimized for large volume meshes.
	The default value is False.

	@create_skin_shells boolean: (optional)If enabled, the skin quad shells will be created. Skin quad shells 
	will be always created if light_volume_representation is True.
	The default value is False.

	@part object: (optional)Part that will be assigned to all created quads and hexas.
	If not provided the current part will be used.

	@solids_property object: (optional)Property that will be assigned to all created hexas. 
	Applies only when light_volume_representation is False.
	If not provided, a new one will be created.

	@shells_property object: (optional)Property that will be assigned to all created skin shells.
	If not provided, a new one will be created.

	@returns boolean: Returns True if process completed successfully.
	In any other case, an exception will appear.

	"""

def MapBlock( macros ):

	"""

	MapBlock will detect Map Block volumes either from the given input geometry, or all db will be considered as input if argument is ommited. It will automatically define the appropriate caps and sides and will create surface mesh according to the defined mesh parameters and quality criteria.


	@macros object: (optional)A list of macros that the algorithm will use to run. If not such a list is provided, 
	the algorithm will run on whole database.

	@returns object: Returns a list of the detected Map Block volumes.

	"""

class VolumesExtrude():

	"""

	Class to extrude an area according to a specific rule.

	"""


	def offset(source, target, side, source_remove, disconnect_from_source, stitch_sources, snap_bounds, connect_target, collapse_free_edges, connect_side, direction, biasing, factor, biasing_direction, steps, element_length, distance, part, property, last_layer_facets_set_name):

		"""

		The shell mesh is offset by means of the normal vector of the elements.


		@source object: list of ansa entities

		@target object: (optional)list of ansa entities

		@side object: (optional)list of ansa entities

		@source_remove object: (optional)list of ansa entities

		@disconnect_from_source boolean

		@stitch_sources boolean

		@snap_bounds boolean

		@connect_target boolean

		@collapse_free_edges boolean

		@connect_side boolean

		@direction string: (optional)values could be "default", "inverted", "both_sides" or "both_sides_middle"

		@biasing string: (optional)values could be "no", "smooth", "arithmetic" or "geometric"

		@factor float

		@biasing_direction string: (optional)values could be "ascending" or "descending"

		@steps integer

		@element_length float

		@distance float

		@part object

		@property object

		@last_layer_facets_set_name string: (optional)creates a set with the given name that contains the last layer facets

		@returns integer: Returns 1 on success or 0 on failure.

		"""


	def translate(source, target, side, source_remove, disconnect_from_source, stitch_sources, snap_bounds, connect_bounds, collapse_free_edges, connect_side, axis, biasing, factor, biasing_direction, steps, element_length, distance, part, property, last_layer_facets_set_name):

		"""

		The shell mesh is translated by means of a specified vector.


		@source object: list of ansa entities

		@target object: (optional)list of ansa entities

		@side object: (optional)list of ansa entities

		@source_remove object: (optional)list of ansa entities

		@disconnect_from_source boolean

		@stitch_sources boolean

		@snap_bounds boolean

		@connect_bounds boolean

		@collapse_free_edges boolean

		@connect_side boolean

		@axis object

		@biasing string: (optional)values could be "no", "smooth", "arithmetic" or "geometric"

		@factor float

		@biasing_direction string: (optional)values could be "ascending" or "descending"

		@steps integer

		@element_length float

		@distance float

		@part object

		@property object

		@last_layer_facets_set_name string: (optional)creates a set with the given name that contains the last layer facets

		@returns integer: Returns 1 on success or 0 on failure.

		"""


	def revolute(source, target, side, source_remove, disconnect_from_source, stitch_sources, snap_bounds, connect_bounds, collapse_free_edges, connect_side, axis, biasing, factor, biasing_direction, steps, element_length, angle, part, property, last_layer_facets_set_name):

		"""

		The shell mesh is revoluted around a specified axis.


		@source object: list of ansa entities

		@target object: (optional)list of ansa entities

		@side object: (optional)list of ansa entities

		@source_remove object: (optional)list of ansa entities

		@disconnect_from_source boolean

		@stitch_sources boolean

		@snap_bounds boolean

		@connect_bounds boolean

		@collapse_free_edges boolean

		@connect_side boolean

		@axis object

		@biasing string: (optional)values could be "no", "smooth", "arithmetic" or "geometric"

		@factor float

		@biasing_direction string: (optional)values could be "ascending" or "descending"

		@steps integer

		@element_length float

		@angle float

		@part object

		@property object

		@last_layer_facets_set_name string: (optional)creates a set with the given name that contains the last layer facets

		@returns integer: Returns 1 on success or 0 on failure.

		"""


	def project(source, target, side, source_remove, disconnect_from_source, stitch_sources, snap_bounds, connect_bounds, collapse_free_edges, connect_side, biasing, factor, biasing_direction, steps, element_length, part, property, last_layer_facets_set_name):

		"""

		The shell mesh is extruded by means of the source/target project direction.


		@source object: list of ansa entities

		@target object: list of ansa entities

		@side object: (optional)list of ansa entities

		@source_remove object: (optional)list of ansa entities

		@disconnect_from_source boolean

		@stitch_sources boolean

		@snap_bounds boolean

		@connect_bounds boolean

		@collapse_free_edges boolean

		@connect_side boolean

		@biasing string: (optional)values could be "no", "smooth", "arithmetic" or "geometric"

		@factor float

		@biasing_direction string: (optional)values could be "ascending" or "descending"

		@steps integer

		@element_length float

		@part object

		@property object

		@last_layer_facets_set_name string: (optional)creates a set with the given name that contains the last layer facets

		@returns integer: Returns 1 on success or 0 on failure.

		"""


	def sweep(source, guideline, match_guideline):

		"""

		The shell mesh is swept along the given guideline. The rest arguments same as project.


		@source object: list of ansa entities

		@guideline object: list of ansa entities

		@match_guideline boolean

		@returns integer: Returns 1 on success or 0 on failure.

		"""


	def glide(source, guideline, match_guideline):

		"""

		The shell mesh is glided along the given guideline.


		@source object: list of ansa entities

		@guideline object: list of ansa entities

		@match_guideline boolean

		@returns integer: Returns 1 on success or 0 on failure.

		"""


	def dual_sweep(source, guideline1, guideline2, match_guideline1, match_guideline2):

		"""

		The shell mesh is swept along two given guidelines. The first one (or first match) is the master guideline. The rest arguments same as sweep.


		@source object: list of ansa entities

		@guideline1 object: list of ansa entities

		@guideline2 object: list of ansa entities

		@match_guideline1 boolean

		@match_guideline2 boolean

		@returns integer: Returns 1 on success or 0 on failure.

		"""


	def map(source, guidelines, match_guidelines):

		"""

		The shell mesh is extruded along two or more given guidelines. The first one (or first match) is the master guideline. The rest argumens same as sweep.


		@source object: list of ansa entities

		@guidelines object

		@match_guidelines object

		@returns integer: Returns 1 on success or 0 on failure.

		"""

class ReplaceCavity():

	"""

	ReplaceCavity will locally erase and remesh part of volume meshes contained in a box according to the existing batch mesh.

	"""


	def erase(boxes):

		"""

		A Cavity Area entity will be defined from the box. The solids inside the Cavity Area will be erased and boudnary shell will be created on the remaining free facets.


		@boxes object: A list of MorphBoxes or HexaBoxes to define Cavity Area.

		"""


	def remesh(boxes):

		"""

		The Cavity Area defined from the box will be remesh according to the batch mesh and the neighboring tetra mesh. In case of success the produced volumes will be merged with the neighbouring and the Cavity Area will be deleted.


		@boxes object: A boxes list that contains the Cavity Areas.

		"""

class HexaBlockShellsSmooth:

	"""

	Class provides smoothing for the selected box face(s).

	"""


	def __init__(box_faces):

		"""

		Constructor of the class.


		@box_faces object: A list of box face(s) to be smoothed. The box face(s) can only be meshed with the map function.

		@returns object: Returns the instance of the object.

		"""


	def run(iterations, relaxation, project_on_db):

		"""

		Runs the smoother.


		@iterations integer: Controls the number of iterations of the solver.

		@relaxation float: Limits the distance which a node can travel for each iteration.

		@project_on_db boolean: Instructs the smoother to project to underlying geometry. If it sets to false then the mesh will be projected to the underlying box face(s).

		@returns object: Returns the instance of the object if successful.

		"""


	def accept():

		"""

		When the smoother has finished its run, this method must be called. Applies the new smoothed mesh and fits the inner box edge(s) into new positions.


		@returns object: Returns the instance of the object if successful

		"""


	def auto_detect_feature_lines(feature_line_angle):

		"""

		Auto detects feature lines. 


		@feature_line_angle float: Sets the feature line angle for auto detection.

		@returns object: Returns the instance of the object if successful.

		"""


	def clear_all_feature_lines():

		"""

		Clears all feature lines.


		@returns object: Returns the instance of the object if successful.

		"""


	def remove_feature_lines(box_edges):

		"""

		Removes feature lines given.


		@box_edges object: List of box edge(s) to be removed from feature lines.

		@returns object: Returns the instance of the object if successful.

		"""


	def add_feature_lines(box_edges):

		"""

		Adds feature lines.


		@box_edges object: List of box edge(s) to be added as feature lines.

		@returns object: Returns the instance of the object if successful.

		"""


	def finalize_feature_line_selection():

		"""

		This function must be called after all feature lines are gathered.


		@returns object: Returns the object instance if successful.

		"""


	def set_boundary_condition(edge, boundary_type):

		"""

		Sets the boundary condition for a specific box edge. 


		@edge object: The box edge that its boundary condition will be set.

		@boundary_type string: The value of the new boundary condition.
		"f"   The boundary will be fixed
		"fo" The boundary will be fixed and it will be applied 
		       orthogonality to it.
		"s"  The boundary nodes will slide to the boundary. 
		"so" The boundary nodes will slide to the boundary and
		        it will be applied orthogonality to it.

		@returns object: Returns the object of the class if successful.

		"""


	def get_boundary_condition(edge):

		"""

		Returns the boundary condition and the group of the box edges which it belongs.


		@edge object: Gets the box edge.

		@returns object: Returns a tuple with the group of the HEXA_BLOCK_BOX_EDGEs and the type of boundary condition

		"""

