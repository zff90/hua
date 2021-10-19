def AddAssemblyRuleToAssemblyRulesGroup(rules, rules_group):

	"""

	The function adds a list of assembly rules to an assembly rules group.


	@rules object: A list that contains the rules which will be added to the group.

	@rules_group object: A group of rules.

	@returns integer: Returns 1 if the argument rules is of proper type, and rules_group is a valid group.
	Otherwise, 0 is returned.

	"""

def AddAssemblyRulesGroupToAssemblyScenario(rules_groups, scenario):

	"""

	The function adds a list of groups of assembly rules to an assembly scenario.


	@rules_groups object: A list that contains groups of Assembly rules.

	@scenario object: An Assembly Scenario.

	@returns integer: Returns 1 if the rules_groups list is of proper type, and scenario is a valid assembly scenario.
	Otherwise, 0 is returned.

	"""

def AddFilterToAssemblyRule(field, expression, value, session, match, case_sensitive, filter_name):

	"""

	The function adds a filter to an existing assembly rule. If the rule has an active filter, a new row is added to that filter. Otherwise, a new filter is created and is set as active.
	The first, second and third arguments refer to the field, expression and value of the filter respectively. The fourth argument refers to the assembly rule.


	@field string: Field name.

	@expression string: Expression.

	@value string: The value of the expression.

	@session object: The Assembly rule.

	@match string: (optional)Determines if all the filter rows must be matched. Available options are: "all" and 
	"any". Default value is "all".

	@case_sensitive string: (optional)Determines if the filter will be case sensitive. Available options are "yes" and "no".
	Default value is "no".

	@filter_name string: (optional)Defines the filter name. If this filter does not exist, it is created then set as the 
	active filter for the rule.

	@returns integer: Returns 1 if the filter was added successfully, or 0 otherwise.

	"""

def AssignConnectionSettings(connections, parameters):

	"""

	AssignConnectionSettings() assigns the desired setting to the connection without creating the FE representation. 
	
	Default settings are assigned for every setting that is not found or if it is invalid. 
	AssignConnectionSettings() erases the previous FE representation of the connection 
	if there was any.


	@connections object: A list of connection entities.

	@parameters object: A dictionary of keyword/values.

	@returns integer: Returns 0 on error, or 1 for success.

	"""

def AutoSetConnectivityInConnections(connections, filter_visible, output_mode, search_faces, search_shells, search_solids, search_tubes, search_projection, search_holes, use_hole_shape, use_hole_proximity, hole_proximity_distance, hole_proximity_angle, match_hole_params, search_distance, use_settings, search_on_direction, search_from, search_to, find_nearest, find_up_to, find_exactly, between_parts, clear_connectivity, tubes_feature_line_angle_limit, consider_part_hierarchy):

	"""

	This function clears the connectivity of each connection and then sets a new connectivity
	based on the user's parameters. It supports all connection types except hemmings and adhesive
	faces.


	@connections object: A list of connection entities.

	@filter_visible boolean: (optional)Search through visible entities for PIDs or ModuleIDs within the
	search distance.
	(Default: False)

	@output_mode string: (optional)Sets if the connectivity will be assigned by "moduleid" or "pid" or "groups".
	(Default: "pid")

	@search_faces boolean: (optional)Search through faces for PIDs or ModuleIDs within the 
	search distance.
	(Default: True)

	@search_shells boolean: (optional)Search through shells for PIDs or ModuleIDs within the 
	search distance.
	(Default: True)

	@search_solids boolean: (optional)Search through solids for PIDs or ModuleIDs within the 
	search distance.
	(Default: False)

	@search_tubes boolean: (optional)Search for tubes within the specified search area.
	Connection Type: Bolt
	(Default: False)

	@search_projection boolean: (optional)Search for projection within the specified search area.
	Connection Type: Bolt
	(Default: True)

	@search_holes boolean: (optional)Search for holes within the specified area.
	Connection Type: Bolt
	(Default: False)

	@use_hole_shape boolean: (optional)If set to "False", ignores if the hole is rounded ellipsoeid, 
	it will be recognized anyway.
	If set to "True" only rounded holes are accepted.
	Connection Type: Bolt
	(Default: True)

	@use_hole_proximity boolean: (optional)If set to "True", use hole_proximity_distance and 
	hole_proximity_angle to recognize a hole.
	Connection Type: Bolt
	(Default: True)

	@hole_proximity_distance float: (optional)Specifies the maximum distance between recognized holes.
	Connection Type: Bolt
	(Default: 100)

	@hole_proximity_angle float: (optional)Specifies the maximum 'angle' between holes.
	Connection Type: Bolt
	(Default: 10)

	@match_hole_params string: (optional)Each hole will be recognised if 'all' or 'any' of the hole 
	criteria are matched.
	Used with 'search_holes' = 'True'
	Connection Type: Bolt
	(Default: 'any')

	@search_distance float: (optional)The search radius for parts or props 
	to be assigned to connections.
	Connection Type: All
	(Default: 5)

	@use_settings boolean: (optional)Use connection's search parameters to
	define the search area.
	Connection Type: Bolt
	(Default: False)

	@search_on_direction boolean: (optional)If the connection has a direction, the  search can be made 
	in a cylindrical area.
	Used when 'use_settings' = 'False' and
	'search_distance' is used as cylinders radius.
	Connection Type: Bolt
	(Default: False)

	@search_from float: (optional)Defines the cylinder's start point, with respect to the connection 
	reference point, along with the connection's direction.
	Used when 'searcn_on_direction' = 'True'
	Connection Type: Bolt
	(Default: -1)

	@search_to float: (optional)Defines the cylinder's end point, with respect to Bolts 
	connection reference point, along with the connection's direction.
	Used when 'searcn_on_direction' = 'True'
	Connection Type: Bolt
	(Default: 1)

	@find_nearest integer: (optional)Assigns the 'n' nearest parts to the connections.
	(Default: 2)

	@find_up_to integer: (optional)Assigns all parts if their count is less or equal to 'n',
	otherwise no parts are assigned.
	(Default: 2)

	@find_exactly integer: (optional)Assigns all parts if their count is equal to 'n',
	otherwise no parts are assigned.
	(Default: 2)

	@between_parts boolean: (optional)if 'True', connectivity will only be set if the connection lies
	between parts.
	Connection Type: ALL, except connection faces
	(Default: 'False')

	@clear_connectivity boolean: (optional)Removes the existing connectivity information If value 'True' is set.
	Options 'find_nearest', 'find_up_to'/'find_exacty' are ignored.
	(Default: 'True')

	@tubes_feature_line_angle_limit float: (optional)Search tubes according to the feature angle
	from 0 to 90 degrees.
	(Default: 30)

	@consider_part_hierarchy boolean: (optional)Search for the connectivity based on the hierarchical
	relationship between parts and connections.
	For a connection within a part, search only the parts/groups
	at the same level with the connection part (siblings parts).
	(Default: 'False')

	@returns: No value returned.

	"""

def CenterConnections(connections):

	"""

	CenterConnections moves every connection point to the center of the parts it connects.
	The function is supported only for connection points.


	@connections object: A list of connection entities.

	@returns integer: Return value is 1 on success and 0 on failure.

	"""

def CollectAffectedConnectionEntities(part, connection_type, search_option):

	"""

	Based on the provided arguments, the function returns a group of connections that reference the specified part in their connectivity fields.


	@part object: Group or Part referenced by the connections.

	@connection_type string: A string that defines the type of connections that will be returned by the function.
	Available types are:
	"Connections", "Connectors", "GentBuilders", "AllEntities".

	@search_option string: A string that specifies whether the search will be carried for internal or external.
	connections or both. Available types are:
	"Internal", "External", "AllAffected".

	@returns object: Returns a list that contains all the collected entities or 0 upon failure.

	"""

def ConnectivityStringToEnts(connectivity):

	"""

	Returns a list of entities represented by a string, which can be found in the connectivity fields of connectors and connections.


	@connectivity string: A string that represents ANSA entities. For example "#IN1" represents 
	include with id 1, "312" represents part with module id 312 etc.

	@returns object: Returns a list of entities represented by the string.

	"""

def ConvertConnections(connections, point_to, line_to, create_single_line):

	"""

	ConvertConnections converts connection lines and points to another connection line type and point type correspondingly.
	Convertion can take place only in connection points if the second argument is only a point type connection. The same is
	for connection lines too.


	@connections object: A list of connection entities that will be converted
	to a different type.

	@point_to string: (optional)Converts only connection points and valid types are:
	"SpotweldPoint_Type", "GumDrop_Type", "Bolt_Type", 
	"SpotweldLine_Type", "Rivet_Type", "Robscan_Type", "Screw_Type".

	@line_to string: (optional)Converts only connection lines and valid types are:
	"AdhesiveLine_Type", "SeamLine_Type", "SpotweldLine_Type",
	"Hemming_Type".

	@create_single_line boolean: (optional)This option has meaning only when converting spots to a single or more lines.
	With False value connections are grouped in space and by connectivity and 
	more than one lines can be created.
	(Default: True)

	@returns integer: Returns 0 on error, or 1 for success.

	"""

def ConvertConnectivity(connections, connectivity_mode, search_nearest_dist):

	"""

	Converts current connectivity of connections to Parts or Properties or Groups.


	@connections object: A list with connection entities.

	@connectivity_mode string: The new connectivity mode to convert to:
	-"PID" 
	-"ModuleID"
	-"Group"
	-"subsystem": get all subsystems a part belongs
	-"instance_to_part": get all instances of part
	-"part_to_instance": get nearest instance

	@search_nearest_dist float: (optional)The search radius for the nearest properties 
	of a part. If it is not given, function gets 
	all properties of the part.

	@returns: No returned value.

	"""

def ConvertFeRepToConnection(entities, convert_type, connectivity_mode, check_violated_elements):

	"""

	This function assigns a connection in every FE Representation element of the list.
	The connectivity can be assigned by ModuleID or PID or Group.


	@entities object: Contains the elements to convert.

	@convert_type string: Defines the type of the connections to be created. 
	Valid types are:
	-"FE To Cnctn Pts": connection points
	-"FE To Seamline": seamlines
	-"FE To Adhesive": adhesive lines
	-"FE To Adh Face":  adhesive faces
	-"FE To Bolt" : bolts

	@connectivity_mode string: Defines the type of connectivity of the generated entity. 
	Valid types are:
	-"PID"
	-"ModuleID"
	-"Group"

	@check_violated_elements boolean: (optional)False : allow elements with more than 20 nodes 
	to be converted to connections.
	True : Not allow elements with more than 20 nodes 
	to be converted to connections.
	(Default: True)

	@returns object: Returns a list containing all the created connections or None on failure.

	"""

def ConvertTubesToConnections(connection_type, input_faces, connections, matched_faces, unmatched_faces):

	"""

	Converts tubes to connection lines.


	@connection_type string: The connection type the user wants to create, with accepted values:
	-"SpotweldLine_Type"
	-"AdhesiveLine_Type"
	-"SeamLine_Type"
	-"Hemming_Type"

	@input_faces object: A list of faces or a string with accepted values "All" or "Visible".

	@connections boolean: (optional)If True the function will return a list with references to the created connections.

	@matched_faces boolean: (optional)If True the function will return a list with references to the matched faces.

	@unmatched_faces boolean: (optional)If True the function will return a list with references to the unmatched faces.

	@returns object: On success it returns a dictionary which includes:
	key: connections        value: a list with the references of the created connections
	key: matched_faces      value: a list with the references of the matched faces
	key: unmatched_faces    value: a list with the references of the unmatched faces
	
	Return None on failure.

	"""

def CreateConnectionFace(type, faces, id, connectivity, create_new_face):

	"""

	The function creates an adhesive face.


	@type string: "AdhesiveFace_Type".

	@faces object: A list that contains the faces that describe the connection.

	@id integer: (optional)Specify the ID of the connection. Set 0 to let ANSA assign an ID.

	@connectivity object: (optional)A list that contains the connectivity strings of the components that 
	will be connected.

	@create_new_face boolean: (optional)If set to True a new face will be created. 
	(Default: False)

	@returns object: Returns the connection created, or 0 on error.

	"""

def CreateConnectionLine(type, curves, id, connectivity):

	"""

	Creates a connection line (adhesive, seamweld, spotline or hemming).


	@type string: The type of the connection. Available types:
	-"SpotweldLine_Type"
	-"AdhesiveLine_Type"
	-"SeamLine_Type"
	-"Hemming_Type"

	@curves object: A list that contains the curves that describe the connection.

	@id integer: (optional)The ID of the connection that will be created.

	@connectivity object: (optional)A list that contains the connectivity strings of the connected components.

	@returns object: Returns the connection created, or None on error.

	"""

def CreateConnectionPoint(type, position, id, connectivity):

	"""

	Creates a connection point (spotweld, bolt or gumdrop).


	@type string: Type of Connection that will be created.
	Available types are:
	-"SpotweldPoint_Type"
	-"Bolt_Type"
	-"GumDrop_Type"
	-"Rivet_Type"
	-"Screw_Type"

	@position object: A list that contains the coordinates of the connection point.

	@id integer: (optional)The ID of the connection that will be created.

	@connectivity object: (optional)A list that contains the connectivity strings of the connected parts.

	@returns object: Returns the created connection entity, or None on error.

	"""

def CreateNewAssemblyRule(name):

	"""

	This function creates a new assembly rule.


	@name string: (optional)A name for the rule, if left blank an untitled rule will be created.

	@returns object: Returns a reference to the newly created assembly rule.

	"""

def CreateNewAssemblyRulesGroup(name, search_for):

	"""

	This function creates a new assembly rules group. To name the rules group, specify
	the pair (name="rule's name"), otherwise an untitled one is created. 
	
	To specify the type of connections for the group, use the pair (search_for="connection_type"),
	otherwise "SpotweldPoint_Type" will be assigned.


	@name string: (optional)A name for the rules group, otherwise an untitled one is created.

	@search_for string: (optional)Specify the type of connections for the group, otherwise "SpotweldPoint_Type" 
	will be assigned.

	@returns object: Returns a reference to the newly created assembly rules group.

	"""

def CreateNewAssemblyScenario(name):

	"""

	This function creates a new assembly scenario. A name can be assigned to the rule, if the pair 
	(name = "Rule name") is specified. An untitled scenario will be created otherwise.


	@name string: (optional)The name of the Assembly scenario which will be generated.

	@returns object: Returns a reference to the newly created assembly scenario.

	"""

def DefineConnectionHoles(entities, create, output_mode, parts_proximity_for_connection_merging, maximum_length, exclude_single_part_connections, match_hole_params, search_holes, use_hole_shape, use_hole_proximity, hole_proximity_distance, hole_proximity_angle, hole_minimum_diameter, hole_maximum_diameter, tube_minimum_diameter,tube_maximum_diameter, search_tubes, tubes_feature_line_angle_limit):

	"""

	Creates connectors or bolts in the recognized holes and tubes


	@entities object: A list that contains parts, properties, includes,
	shells, faces or solids.

	@create string: Defines the type of the connector or bolt to create.

	@output_mode string: Accepted values: "module_ids" or "properties". Defines 
	whether the connectivity will be assigned by module_ids 
	or properties.

	@parts_proximity_for_connection_merging float: (optional)Holes or tubes within a tolerance distance are handled 
	as one and only one Connection is created.
	(Default: 0)

	@maximum_length float: (optional)The length of the tube or the distance of the most distant 
	holes is assigned to bolt. Sometimes it's large and then 
	user specifies a maximum length that should be assigned. 
	It is only taken into account when specified.

	@exclude_single_part_connections boolean: (optional)Connections with only one part will not be created.
	(Default: False)

	@match_hole_params string: (optional)Accepted values: "any" or "all". Each hole will be 
	recognized if "all" or "any" of the hole criteria are 
	matched.
	(Default: "all")

	@search_holes boolean: (optional)Accepted values: True or False. Set to True to create 
	assembly entities in holes. All hole parameters are 
	ignored if 'search_holes' is False.
	(Default: True)

	@use_hole_shape boolean: (optional)Accepted values: True or False. If set to False, ignores if 
	the hole is rounded or ellipsoid, it will be  recognized 
	anyway. If set to True, only rounded holes are accepted.
	(Default: False)

	@use_hole_proximity boolean: (optional)Accepted values: True or False. Use hole_proximity_distance 
	& hole_proximity_angle with True, to recognize a hole.
	(Default: True)

	@hole_proximity_distance float: (optional)Specifies the maximum distance between recognized holes.
	(Default: 10)

	@hole_proximity_angle float: (optional)Specifies the maximum 'angle' between holes.
	(Default: 10)

	@hole_minimum_diameter float: (optional)Specifies the minimum diameter for hole recognition.

	@hole_maximum_diameter float: (optional)Specifies the maximum diameter for hole recognition.

	@tube_minimum_diameter float: (optional)Specifies the minimum diameter for tube recognition.

	@tube_maximum_diameter float: (optional)Specifies the maximum diameter for tube recognition.

	@search_tubes boolean: (optional)Accepted values: True or False. Set to True, to create 
	assembly entities in tubes. All tube parameters are 
	ignored if 'search_tubes' is False.
	(Default: False)

	@tubes_feature_line_angle_limit float: (optional)Specify the maximum angle of the tubes feature. 
	(Default: 10)

	@returns object: Returns a list with the newly created assembly entities, or None on error.

	"""

def DistributeAllItemsToAssemblyScenarios():

	"""

	The function distributes all connections of the current database to the existing 
	assembly scenarios. It is equivalent to pressing the 'Distribute" button, and
	selecting the "All, ignoring manual status" option.


	@returns integer: Returns 0.

	"""

def EntsToConnectivityString(connectivity):

	"""

	Returns a string that represents the entities in a connectivity list. This string is found in the 
	connectivity fields of connectors and connections.


	@connectivity object: A list that contains entities such as parts, properties, includes etc.

	@returns string: Returns a string that represents the entities in the list.

	"""

def EraseConnectionFeRep(connections):

	"""

	This function erases the FE representation of the specified connections. It can be applied to all connection types.


	@connections object: A list that contains the connection entities whose representation will be erased.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def FindDuplicateConnections(connections1, connections2, point_distance_method, connection_point_distance, average_thickness_factor, curve_face_distance, similarity, equivalent_connectivity, same_type, pair_results, distance_of_projection_center):

	"""

	FindDuplicateConnections matches duplicate connections from a single group or between two groups according to 
	the defined matching criteria. It returns a list with the matched connections.


	@connections1 object: A list that contains the first group of connection entities.

	@connections2 object: (optional)A list that contains the second group of connection entities.

	@point_distance_method string: (optional)Defines the method to calculate the distance between connection 
	points.
	The available methods are the following:
	-'use_average_thickness': distance = factor * average thickness of 
	  projection connectivity flanges. The center of projections is 
	  taken account for the measurement between connections.
	-'use_distance_between_projection_centers':  distance = the 
	  given value. 
	  The center of projections is taken account for the measurement 
	  between connections.
	-'use_absolute_distance': distance = the given value. The 
	  connection's position is taken account for the measurement between 
	  connections. 
	(Default: 'use_average_thickness')

	@connection_point_distance float: (optional)Value must be greater or equal to 0. When "point_distance_method" 
	is defined to "use_absolute_distance", then this argument is used as 
	search radius within two points that are duplicates.
	(Default: 5.0)

	@average_thickness_factor float: (optional)Factor must be greater or equal to 0  when "point_distance_method" 
	is defined to "use_average_thickness", then this argument is used as 
	search radius. 
	Radius = (flange_thick1 + flange_thick2) * factor.
	(Default: 0.5)

	@curve_face_distance float: (optional)Value must be greater or equal to 0. It is the distance between 
	curves or faces that will be checked for similar geometry.
	(Default: 5.0)

	@similarity float: (optional)It is the percentage of the geometrical similarity for compared 
	curves or faces that are found within the defined 
	curve_face_distance.
	(Default: 75.0)

	@equivalent_connectivity boolean: (optional)If True, only compare connections with equal connectivity.
	(Default: False)

	@same_type boolean: (optional)Only compare same type connections.
	e.g. If True, only compare a bolt with a bolt and not a bolt 
	with a spotweld.
	(Default: True)

	@pair_results boolean: (optional)Choose whether the results will be pairs or groups of connections.
	(Default: True)

	@distance_of_projection_center float: (optional)Value must be greater or equal to 0. When "point_distance_method" 
	is defined to "use_distance_of_projection_center" then it is used as 
	search radius between two centered projection points that are 
	duplicates.
	(Default: 5.0)

	@returns object: If pair_results=True it returns a dict with:
	key: group1,    values: the connections found
	key: group2,    values: the connections found
	
	If pair_results=False it returns a dict with:
	key: groups,    values: a list with lists of grouped connections
	key: conflicts, values: a list with connections that belong to more than one group
	                       
	Return 0: User has an incorrect parameter.
	Return 1: The function has run properly but no duplicate connection found.
	Return None: The input connections parameter is incorrect

	"""

def GetAllConnectionSettings(connection):

	"""

	GetAllConnectionSettings() returns all the connections settings of a connection.


	@connection object: The connection entity whose settings will be obtained.

	@returns object: Returns a dictionary of all the settings-keywords and their respective value. 
	If the connection has no parameters, it returns None.

	"""

def GetConnectionProjections(connections, search_distance):

	"""

	Finds the projections of connections.


	@connections object: List of connection entities.

	@search_distance float: (optional)Search distance for the projection.
	If not specified a default value will be used.

	@returns object: Returns a list of Connections. Each Connection has a list of Projections. Each Projection has a list 
	with two items, a list with the coordinates and the entity.

	"""

def GetConnectionSettings(connection, parameters):

	"""

	GetConnectionSettings() returns the connections settings of the requested parameters.


	@connection object: The connection entity whose settings will be obtained.

	@parameters object: A list or tuple that contains the parameter keywords.

	@returns object: Returns a dictionary of the keywords found and their respective value. 
	Returns None if connection has no parameters.

	"""

def GetFirstFeRep(connections):

	"""

	Gets a reference to the first entity of a connection.


	@connections object: A connection entity.

	@returns object: Returns a reference to the entity or None if no entity is found.

	"""

def GetNearestPointOnBound(points, parts_props, search_dist):

	"""

	The function returns a list with the nearest points on bounds.


	@points object: A list (size N) where each entry is a set of coords [X,Y,Z], from which the function 
	will find the nearest points on a bound of the parts/props.

	@parts_props object: A list (size N) where each entry contains a list of Part/Property entities that define 
	the searchfield for each point.

	@search_dist float: A float that determines the maximum search distance.

	@returns object: Returns a list (size N) with the resulting nearest points on bound: 
	Each entry of the matrix is either:
	1) A matrix (size 3) whose coordinates of the point were found.
	2) 0, if such a point was not found within search_dist.

	"""

def GetNearestPointOnFeature(points, parts_props, search_dist, feature_angle):

	"""

	The function returns a list with the nearest points on bounds.


	@points object: A list (size N) where each entry is a set of coords [X,Y,Z] from which the 
	function will find the nearest points on a bound of the parts/props.

	@parts_props object: A list (size N) where each entry contains a list of Part/Property 
	entities that defines the search field for each point.

	@search_dist float: A float that determines the maximum search distance.

	@feature_angle float: A float that defines the feature angle in degrees.

	@returns object: Returns a list (size N) with the resulting nearest points on bound found from search:
	Each entry of the matrix is either:
	1) A matrix (size 3) with the coordinates of the point found.
	2) 0, if such a point was not found within search_dist.

	"""

def GetNextFeRep(connection, entity):

	"""

	Gets a reference to the next 'element' of a connection by specifing the current element.


	@connection object: A connection entity.

	@entity: The next element in the FE representation of connection. 
	Can be retreived from a call to GetFirstFeRep() or GetNextFeRep().

	@returns object: Returns a reference to the entity or None when no entity is found.

	"""

def GetSpwDiamFromThickness(connection, search_distance):

	"""

	The Connection point diameter value is calculated from the Spot Weld Thickness Diameter Map 
	defined in ANSA.defaults. 


	@connection object: A connection entity (Spotweld, Gumdrop, Bolt) with zero diameter.

	@search_distance float: (optional)The search distance. If not given, the connection's search distance is used. 
	Should be greater than 0.

	@returns float: Returns the connection diameter value calculated by Thickness to Diameter Map on success and 0 on failure.

	"""

def OutputConnections(connections, filetype, filename):

	"""

	Outputs a standard connection file with the given connections.


	@connections object: A list that contains the connections entities to be
	output.If you pass a zero-length matrix, 
	ALL the connections are output.

	@filetype string: A string that describes the type of the output file
	Available types:
	"XML","MCF", "VIP", "VIP(pid)", "VIP(csv)", "VIP(csv, pid)", "VIP2", "VIP2(ModuleId)",
	"xMCF 3.1", "xMCF 3.1(pid)".
	If an invalid type is entered, a list valid types will
	be suggested by ANSA.

	@filename string: A string that describes the path and name of the
	connection file. The file will be overwritten if it
	already exists.

	@returns integer: Returns 0 if the filetype is wrong, or if an error occurred during the writing of the file.

	"""

def ReApplyConnections(connections):

	"""

	Create the FE representation of a number of connections, using their current settings.


	@connections object: A list with connection entities or a single connection
	entity to will be reapplied.

	@returns integer: Returns 0 if no connections exists in the list, 1 otherwise.

	"""

def ReadConnections(filetype, filename, group_name, offset_val):

	"""

	Reads a standard connection file and creates connections.


	@filetype string: String declaring the type of the file (ex. "XML", "VIP").
	If an invalid type is entered, a list of valid
	types will be suggested by ANSA.

	@filename string: The path of the file.

	@group_name string: (optional)The name of the connections group that is generated.

	@offset_val integer: (optional)The offset connection id.

	@returns integer: Returns 0 if the filetype is wrong or if the parameters are invalid.

	"""

def RealizeConnections(connections, parameters):

	"""

	Create the FE representation of a number of connections, using either the specified values for
	each type or the default values. 


	@connections object: A list of connection entities that will be 
	realized.

	@parameters object: A dictionary with the FE Rep. Settings fields name and 
	values. If a blank dictionary is specified, the default
	values of each type will be used.

	@returns integer: Returns 0 if all connections fail. Otherwise it returns the number of connections that
	were realized successfully.

	"""

def RemoveDoubleConnections(connections, tolerance, equivalent_connectivity, keep_id, move_to_middle, action):

	"""

	RemoveDoubleConnections() combines or deletes the connections which are considered double, 
	deoending on a tolerance distance and their equivalent connectivity. The remaining connection 
	of every double connections group can be placed to the center of gravity of each group. 
	
	It is highly recommended to use 'FindDuplicateConnections' which matches any kind of 
	connection and not only connection points like 'RemoveDoubleConnections'.
	Also more matching criteria are available.


	@connections object: A list that contains connection point entities.

	@tolerance float: (optional)The search radius.
	(Default: 5)

	@equivalent_connectivity boolean: (optional)This option groups the connections if they have the same connectivity.
	(Default: False)

	@keep_id string: (optional)Accepted values: "highest", "lowest". The connection with the highest 
	or lowest id from each group will be kept.
	(Default: "highest")

	@move_to_middle boolean: (optional)It moves the remaining connection from each group to 
	the center of gravity of the group.
	(Default: False)

	@action string: (optional)Accepted values: "delete", "combine". Select the action for the 
	useless connections of each group.
	(Default: "delete")

	@returns integer: Return 1 on success or 0 on failure, with corresponding message.

	"""

def RunAllAssemblyScenarios(realize_connections):

	"""

	The function applies all the active assembly scenarios of the database.


	@realize_connections boolean: (optional)Determines whether the connections will also be realized.
	(Default: False)

	@returns integer: Returns the number of active assembly rules (i.e. the ones that runned).

	"""

def SetConnectionDrawMode(mode, user_attributes, use_color_bar):

	"""

	SetConnectionDrawMode sets drawing mode for connections.


	@mode string: (optional)Valid drawing modes are "Ent", "Connectivity Num", "Connectivity Parts", 
	"Type", "Status", "FeRep", "Diameter", "User Attributes".

	@user_attributes string: (optional)Define the attribute to draw.
	It is used only for "User Attributes" draw mode.

	@use_color_bar boolean: (optional)Numerical criteria can be drawn using the color bar
	or the default legends table.

	@returns integer: Returns 1 on success and 0 nailure.

	"""

def SetDefault(fields):

	"""

	Changes the default Connection Manager values, stated in the ANSA.default file.
	(e.g. values for adhesive lines in ANSA.default file:
	"AdhesiveLine_Type = RBE3-HEXA-RBE3", defines RBE3-HEXA-RBE3 as the default pattern when
	realizing a connection, "AdhesiveFace_RBE3_HEXA_RBE3_RBE3PinFlags = 123456", defines
	123456 as the default pinflags value for this pattern).
	Change these values, by passing parameters to this function in pairs of:
	"param variable"-"param value"


	@fields object: A tuple, containing consecutive string pairs of: "param variable", "param value".

	@returns integer: Returns 0 on error, or non-zero on success.

	"""

def RunAssemblyScenario(scenarios, realize_connections):

	"""

	The function applies the selected assembly scenario.


	@scenarios object: The assembly scenario which will be applied.

	@realize_connections boolean: (optional)Determines whether the associated connections will be realized.
	(Default: False)

	@returns integer: Returns the number of Assembly Rules groups that the Assembly Scenario contains.

	"""

def ActivateConnectionsEnts(connection_ents, make_active):

	"""

	Activates/Deactivates connections of the database. To be applied in order to control which connections will 
	remain active after actions that turn the related parts to Use/Don't Use representation.


	@connection_ents object: A list with references to connection entities.

	@make_active boolean: True to activate the connections. False to deactivate them.

	@returns integer: Always returns 0.

	"""

def AddFilterToAssemblyRulesGroup(field, expression, value, session, match, case_sensitive, filter_name):

	"""

	The function adds a filter to an existing assembly rules group.


	@field string: The field name.

	@expression string: The expression.

	@value string: The value of the expression.

	@session object: The assembly rules group.

	@match string: (optional)Determines if all the filter rows must be matched.
	Available options are: "all" and "any".
	(Default: "all")

	@case_sensitive string: (optional)Determines if the filter will be case sensitive.
	Available options are "yes" and "no".
	(Default: "no")

	@filter_name string: (optional)Defines the filter name. If this filter does not exist, 
	it is created and set as the active filter for the rule.

	@returns integer: Returns 1 if the filter was added successfully, or 0 otherwise.

	"""

def OpenConnectionManager(connections, mode, inspection_mode, confirm_to_close):

	"""

	Opens the connection manager filled with connections or empty.
	It is opened either in modal mode, with ok/cancel dialog and forces the python script to wait
	until it is closed, or in modeless mode, without ok/cancel dialog where the script continues.


	@connections object: (optional)A list with connections or a single connection.

	@mode string: (optional)'mode' takes 2 values:
	        - 'modal': the script stops here and manager opens
	           with Ok/Cancel dialog.
	           It returns 1 for Ok pressed and 0 for ESC.
	           Script continues when manager closes.
	
	         - 'modeless': script continues and manager opens
	              without Ok/Cancel dialog. It returns always 1.
	(Default: 'modal')

	@inspection_mode boolean: (optional)Set to True to open the Connection Manager in inspection mode.
	(Default: No)

	@confirm_to_close boolean: (optional)If set to True, a window will ask the user to confirm to close 
	the Connection Manager.
	(Default: No)

	@returns boolean: Modal manager returns True for Ok pressed and False for ESC or cancel.
	Modeless manager always returns True.

	"""

def OpenTemplateManager():

	"""

	This function opens the Connection Template Manager and the script stops until it is closed.
	The function is executed in gui mode only.


	@returns object: Always returns None.

	"""

def ReplaceConnectivity(old_connectivity, new_connectivity, connections, connectivity_indexes):

	"""

	Replace the given connections connectivity (part, prop, include, subsytem)
	by one or more parts/props/includes/subsystems to any or Pi connectivities of connections.


	@old_connectivity object: A part, a prop, an include, a subsytem or a list of them.

	@new_connectivity object: A part, a prop, an include, a subsytem or a list of them.

	@connections object: A connection or a list of connections.

	@connectivity_indexes integer: (optional)An integer or a list of integers to define the index of Pi connectivities 
	to replace the connectivity.

	"""

def GroupConnectionsByConnectivity(connections):

	"""

	The function groups the given connections that have the same connectivity.


	@connections object: A list of connection entities

	@returns object: Returns a dictionary where the key is the connectivity string and the data is a list of
	connections that have this connectivity.

	"""

def ConvertConnectionsToGeometry(connections, part):

	"""

	ConvertConnectionsToGeometry converts connection lines and points and connection 
	faces to geometry.
	


	@connections object: A list of connection entities that will be converted
	to geometry.

	@part object: (optional)The ANSA part that will be used for the convertion.

	@returns object: Returns a list with the created entities (ie. curves, points, faces).

	"""

def FindDuplicateTemplates(templates):

	"""

	FindDuplicateTemplates matches duplicate connection templates that are identical. It returns a list of lists with the matched templates.


	@templates object: A list that contains the templates to compare.

	@returns object: Returns 0 on error, or a list of lists of duplicate Templates on success.

	"""

def SetWeldPosition(connections, set_method):

	"""

	Sets Weld Positions in a list of Connections. The connections must be of "SeamLine_Type".


	@connections object: A list of ANSA "SeamLine_Type" connections

	@set_method string: (optional){"Manual", "Automatic"}. The method with which the Weld Position will be set. Default is "Manual".

	@returns object: A list of the connections that failed to set a Weld Position. 
	Note. set_method = "Manual" will always return an empty list.

	"""

def SplitConnectionLinesByAngle(connections, corner_angle):

	"""

	This function breaks a connection line to multiple connection lines on locations where angle formed between two consecutive curves is bigger than corner angle.


	@connections object: A list with connection entities.

	@corner_angle float: The angle formed between two consecutive curves in degrees.

	@returns: A dictionary containing the keys 'splitted' and 'not_splitted'.
	Key 'splitted' has as value a dictionary with key the initial connection and key a list with Connection entities,
	to which initial connection was splitted.
	Key 'not_splitted' has as value a list with objects of Connection entities which was not splitted.

	"""

def CreateConnectorFromInterfacePoints( interface_points, match_only_identical_names, matching_proximity, create_extrenal_connectors_only, representation):

	"""

	This function groups interface points according the defined criteria and creates a connector per group.
	The connector has connectivity, search, interface and representation assigned. Direction is assigned when the connector is defined between 2 interface points.


	@interface_points object: A list with interface points for grouping.

	@match_only_identical_names boolean: (optional)Group interface points with identical name only.
	Default: False

	@matching_proximity float: (optional)The distance where 2 or more interface points
	are grouped.
	Default: 5

	@create_extrenal_connectors_only boolean: (optional)Create connectors which assembly interface points
	which belong to different subsystems.
	Default: False

	@representation string: (optional)The representation which is assigned to
	each new connector.
	Default: None

	@returns object: It returns a dictionary with key the connector and data a list with interface points from which it was created.

	"""

def CollectConnectionCurves(connection):

	"""

	Creates a list with the curves of a connection line.


	@connection object: The connection line if which curves should be returned.

	@returns object: Returns a list with all the collected curves.

	"""

def FindConnectionCharacteristics(connections, search_pattern, average_angle):

	"""

	Gets characteristics from a list of Connections. The connections must be of "SeamLine_Type".


	@connections object: a list of ANSA "SeamLine_Type" connections.

	@search_pattern boolean: (optional)If True it will return the search pattern of the connections.

	@average_angle boolean: (optional)If True it will return the average angle of the connections' connected flanges.

	@returns object: A dictionary with key the connections and value an object of type FindConnectionCharacteristics.
	Each characteristic can be accessed from each returned object from its corresponding member.
	When a characteristic is not requested or it could not be calculated None will be returned.

	"""

def ChangeDensity(connection_groups, density_factor):

	"""

	Increase/Decrease density of the connections in an ORDERED_CONNECTION_GROUP.


	@connection_groups object: A list of ORDERED_CONNECTION_GROUP entities.

	@density_factor float: A factor by which the density of the connections in the group are to be increased, or decreased.

	@returns object: Always returns None.

	"""

def FeRepSettingsConvertIDsToReferences(connections):

	"""

	changes some fields the FE-Rep settings of given connections to use entities 
	by reference instead of entity IDs. Success of this conversion requires that 
	an entity exists in the database that has compatible type and same ID as the ID 
	mentioned in the FE-Rep settings.
	


	@connections object: A list of connection entities that their settings will be
	adjusted to use references

	@returns object: Returns a dict where the keys are the connection entities which were given as input
	and the values are a list of options that could not be adjusted to use
	references.

	"""

def ApplyDensityHistogram(connection_groups, interval_params, densities):

	"""

	Reset the density of the connections in an ORDERED_CONNECTION_GROUP, by providing a histogram.
	This allows to set a density that varies along the polyline of the connection group.
	
	The connections along the ORDERED_CONNECTION_GROUP form a polyline.
	ApplyDensityHistogram() allows you to set a density value for various intervals
	of the polyline.
	
	The begining of the polyline corresponds to parameter value 0.0.
	The ending of the polyline corresponds to parameter value 1.0.
	The middle of the polyline corresponds to parameter value 0.5.
	
	The density of the connections is the number of connections per unit length.
	Density of 0.02 means: 
	0.02 connections per mm. Or 2 connections every 10cm. 
	Therefore, the spacing between consecutive connections is 50mm.
	
	The density histogram can be defined using two lists of equal size:
	
	  interval_params = [0.00, 0.33, 0.66]
	  densities       = [0.04, 0.03, 0.02]
	
	This will set the following densities to each interval of the ORDERED_CONNECTION_GROUP:
	length interval: 0.00 - 0.33   =>  density = 0.04
	length interval: 0.33 - 0.66   =>  density = 0.03
	length interval: 0.66 - 1.00   =>  density = 0.02
	
	Since the intervals are consecutive, only the begining of each interval and the 
	density are required to define the histogram.
	


	@connection_groups object: a list of ANSA "ORDERED_CONNECTION_GROUP" entities.

	@interval_params object: a list of the intervals on the polyline of each ORDERED_CONNECTION_GROUP.

	@densities object: A list, containing the density value for each interval in the 'interval_params'

	"""

