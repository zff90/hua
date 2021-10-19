def AddFilterToScenario(field, expression, value, session, match, case_sensitive, filter_name):

	"""

	The function adds a filter to an existing batch mesh scenario (meshing, layers, wrap or volume), much like the way it is done through the batch mesh manager. If the scenario has an active filter, a new row is added to that filter. 
	Otherwise, a new filter is created and is set as active.
	The first, second and third arguments refer to the field, expression and value of the filter respectively.


	@field string: Field Name.

	@expression string: Expression.

	@value string: The value that the expression will evaluate.

	@session object: The reference to the Assembly rule.

	@match string: (optional)Determines if all the filter rows must be matched. Use "all" or "any" to change 
	the value.

	@case_sensitive string: (optional)Determines if the filter will be case sensitive. Use "yes" or "no" to change 
	the value.

	@filter_name string: (optional)Give a specific name to a filter.

	@returns integer: Returns 1 if the filter was added successfully, or 0 otherwise.

	"""

def AddFilterToSession(field, expression, value, session, match, case_sensitive, filter_name):

	"""

	The function adds a filter to an existing batch mesh session (meshing, layers or volume), much like the way it is done through the batch mesh manager.
	If the session has an active filter, a new row is added to that filter. Otherwise, a new filter is created and is set as active.


	@field string: Field Name.

	@expression string: Expression.

	@value string: The value that the expression will evaluate.

	@session object: The reference to the Assembly rule entity.

	@match string: (optional)Determines if all the filter rows must be matched. Use "all" or "any" to change 
	the value.

	@case_sensitive string: (optional)Determines if the filter will be case sensitive. Use "yes" or "no" to change 
	the value.

	@filter_name string: (optional)Give a specific name to a filter.

	@returns integer: Returns 1 if the filter was successfully created, or 0 otherwise.

	"""

def AddPartToMeshingScenario(INPUT_ref, SCENARIO_ref):

	"""

	This function adds an item or an array of items (part, group, property or volume) to a batch mesh scenario.


	@INPUT_ref object: References the item to be added to the senario. The type of the item may be a part,  group, 
	property or volume.

	@SCENARIO_ref object: References the senario. The senario's type must be in accordance to the type of the item.

	@returns integer: Returns 1 if INPUT and SCENARIO are valid and the items were added, or 0 otherwise.

	"""

def AddPartToSession(ITEM_ref, SESSION_ref):

	"""

	This function adds an item to a batch mesh session.


	@ITEM_ref object: References the item to be added to the session. The type of the item may be a part, group, 
	property or volume.

	@SESSION_ref object: References the session.The session's type must be in accordance to the type of the item.

	@returns integer: Returns 1 if the numbers referencing the item and the session are valid entities, or 0 otherwise.

	"""

def AddSessionToMeshingScenario(SESSION_list, SCENARIO_ref):

	"""

	The function adds an array of batch mesh sessions to a scenario.


	@SESSION_list object: References the the list of sessions to be added to the scenario.It may be either a
	meshing,layers or volume session.

	@SCENARIO_ref object: References the senario to be used and must be of the same type as the first argument.

	@returns integer: Returns 1 if the SESSION_ARRAY is of proper type, SCENARIO is a valid scenario, according to the type of the array, and all the sessions have been successfully added to the scenario. Otherwise, 0 is returned.

	"""

def DistributeAllItemsToScenarios():

	"""

	The function distributes all parts/groups/properties of the current database to any meshing and layers scenarios that may exist. The filters for each scenario are taken into account.


	@returns integer: Always returns 0.

	"""

def GetNewLayersScenario(name, search_for):

	"""

	The function creates a new batch mesh layers scenario.


	@name string: (optional)Define a name for the scenario, or create an 
	untitled one by leaving the argument blank.

	@search_for string: (optional)Type of entities to add to the scenario. Accepted 
	values are "PARTS", "GROUPS", "PIDS".

	@returns object: Returns a reference to the newly created layers scenario.

	"""

def GetNewLayersSession(name):

	"""

	This function creates a new batch mesh layer session.


	@name string: (optional)Define a name for the session, or create an untitled one by leaving the argument blank.

	@returns object: Returns a reference to the newly created layer session.

	"""

def GetNewMeshingScenario(name, search_for):

	"""

	The function creates a new meshing scenario.


	@name string: (optional)Define a name for the scenario, or create an 
	untitled one by leaving the argument blank.

	@search_for string: (optional)Change the type of entities to add to the scenario. 
	Accepted values are: "PARTS", "GROUPS" or "PIDS".

	@returns object: Returns a reference to the newly created meshing scenario.

	"""

def GetNewSession(name):

	"""

	This function creates a new batch mesh session.


	@name string: (optional)Define a name for the session, or create an untitled one by leaving the argument blank.

	@returns object: Returns a reference to the newly created batch mesh session.

	"""

def GetNewVolumeScenario(name):

	"""

	The function creates a new batch mesh volume scenario.


	@name string: (optional)Define a name for the scenario, or create an untitled one by leaving the argument blank.

	@returns object: Returns a reference to the newly created volume meshing scenario.

	"""

def GetNewVolumeSession(name):

	"""

	This function creates a new batch mesh volume session.


	@name string: (optional)Define a name for the session, or create an 
	untitled one by leaving the argument blank.

	@returns object: Returns a reference to the newly created volume mesh session.

	"""

def GetNewWrapScenario(name,search_for):

	"""

	This function creates a new wrap scenario.


	@name string: (optional)Define a name for the scenario, or create an untitled 
	one by leaving the argument blank.

	@search_for string: (optional)Type of entities to add to the scenario. Accepted 
	values are: "PARTS", "GROUPS" or "PIDS".

	@returns object: Returns a reference to the newly created wrapping scenario, or 0 otherwise.

	"""

def GetNewWrapSession(name):

	"""

	This function creates a new batch mesh wrap session.


	@name string: (optional)Define a name for the session, or create an untitled one by leaving the argument blank.

	@returns object: Returns a reference to the newly created wrap session, or 0 otherwise.

	"""

def GetPartsFromMeshingScenario(MESHING_SCENARIO_ref):

	"""

	The function collects all parts, groups or properties belonging to a particular meshing scenario.


	@MESHING_SCENARIO_ref object: References the meshing scenario under consideration.

	@returns object: Returns a list containing all the parts, groups or properties that belong to the specific meshing scenario.
	In case MESHING_SCENARIO is not a valid reference or it does not contain any parts, an empty list is returned.

	"""

def GetPartsFromSession(SESSION_ref):

	"""

	This function collects all the parts, groups or properties that are included in a specific session or area.


	@SESSION_ref object: References the meshing session or area under consideration.

	@returns object: Returns a list containing all the parts, groups or properties that belong to the specific session or area.
	In case the SESSION or area is not a valid reference or it does not contain any parts, an empty list is returned.

	"""

def GetSessionMeshParamsName(session_ref):

	"""

	Gets the name of batch meshing sessions' parameters.


	@session_ref object: References the meshing session under consideration.

	@returns string: Returns the name of the session parameters.

	"""

def GetSessionQualityCriteriaName(session_ref):

	"""

	Gets the name of batch meshing sessions' quality criteria.


	@session_ref object: References the meshing session under consideration.

	@returns string: Returns the name of the session quality criteria.

	"""

def GetSessionsFromMeshingScenario(MESHING_SCENARIO_ref):

	"""

	The function collects all sessions belonging to a particular meshing scenario.


	@MESHING_SCENARIO_ref object: References the meshing senario under consideration.

	@returns object: Returns a list containing all the sessions that belong to the specific meshing scenario.
	In case MESHING_SCENARIO is not a valid reference or it does not contain any sessions, an empty list is returned.

	"""

def ImportMeshingFiles(filename, property_conflicts, material_conflicts, set_conflicts, coord_conflicts, node_conflicts):

	"""

	This function opens an ansa file containing parts/groups previously saved with the SaveMeshingSession function and replaces them with parts/groups of the current database that may match them.


	@filename string: The path of the ansa file to be imported.

	@property_conflicts string: (optional)"Offset" creates a new entity.
	"KeepOld" keeps the old value.
	"KeepNew" keeps the new value. (Default)

	@material_conflicts string: (optional)"Offset" creates a new entity.
	"KeepOld" keeps the old value.
	"KeepNew" keeps the new value. (Default)

	@set_conflicts string: (optional)"Offset" creates a new entity. (Default)
	"KeepOld" keeps the old value.
	"KeepNew" keeps the new value.

	@coord_conflicts string: (optional)"Offset" creates a new entity. (Default)
	"KeepOld" keeps the old value.
	"KeepNew" keeps the new value.

	@node_conflicts string: (optional)"Offset" creates a new entity. (Default)
	"KeepOld" keeps the old value.
	"KeepNew" keeps the new value.

	@returns integer: Returns 1 if session is a valid file with read permission, and 0 if it is invalid or the file does not exist.

	"""

def IsolateAndCopyParameters(ITEM_ref):

	"""

	This function isolates entities of ITEM and copies mesh parameters and quality criteria of ITEM
	to the respective fields of Shell Mesh Parameters and Quality Criteria. ITEM can be either Session
	or Box.


	@ITEM_ref object: References the meshing session under consideration.

	@returns float: Returns 1 if the ITEM is of proper type, is isolated and parameters are successfully copied. Otherwise, 0 is returned.

	"""

def ReadSessionMeshParams(SESSION_ref, FILENAME_str):

	"""

	This function reads mesh parameters from a specific file and assigns them to a batch mesh session or area (wrap, layers).


	@SESSION_ref object: References the batch mesh session accepting the values.
	It may also reference a wrap or layers area.

	@FILENAME_str integer: The path of the file containing the parameters.

	@returns integer: Returns 1 if SESSION is a valid reference and the file exists, or 0 otherwise.

	"""

def ReadSessionQualityCriteria(SESSION_ref, FILENAME_str):

	"""

	This function reads quality criteria from a specific file for batch mesh sessions.
	The first argument refers to the batch mesh session accepting the values. 
	The second argument is the path of the file containing the criteria.


	@SESSION_ref object: References the the batch mesh session accepting the values.

	@FILENAME_str integer: The path of the file containing the criteria.

	@returns integer: Returns 1 if session is a valid batch mesh session and the file exists, or 0 otherwise.

	"""

def RunAllMeshingScenarios(time_limit):

	"""

	The function runs all active meshing scenarios of database, which may be meshing, layers or volume scenario.


	@time_limit integer: (optional)Time limit in minutes. If execution time exceeds TIME_LIMIT, 
	the process is halted.

	@returns integer: Returns:
	0, If all scenarios are dectivated.
	1, If at least one scenario has run.
	2, If at least one scenario hasn't run.
	-1, If the process is halted due to the time limit being exceeded or due to Pause-Break key being pressed.

	"""

def RunMeshingScenario(session, time_limit):

	"""

	The function runs all sessions in a batch mesh scenario.


	@session object: References the scenario that will be run, which may be a meshing, layers, wrap 
	or volume scenario.

	@time_limit integer: (optional)Time limit in minutes. If execution time exceeds TIME_LIMIT, process is halted.

	@returns integer: Returns:
	0, If SCENARIO is deactivated.
	1, If SCENARIO has run.
	2, If SCENARIO hasn't run.

	"""

def RunSession(session, time_limit):

	"""

	This function runs a batch mesh session.


	@session object: References the session that will be run, which may be meshing, layers or volume
	scenario.

	@time_limit integer: (optional)Time limit in minutes. If execution time exceeds TIME_LIMIT, process is halted.

	@returns integer: Returns:
	0, If SESSION isn't active.
	1, If SESSION has run.
	2, If SESSION hasn't run.
	-1, If the process is halted due to the time limit being exceeded or due to Pause-Break key being pressed.

	"""

def SaveMeshingSession(session, filename, only_failed, single_seperate):

	"""

	This function saves a session with its parts in the same way it is saved from the right click option
	in the Batch Mesh Manager window.


	@session object: References the session that will be saved, which may be meshing, layers or
	volume scenario.

	@filename string: The name with which the session will be saved.

	@only_failed integer: (optional)The option to save only failed parts, TYPE: integer, VALUES: 0 or 1. If the
	option is omitted, only failed parts are saved.

	@single_seperate string: (optional)Values are 'SINGLE' and 'SEPARATE'.

	@returns integer: Returns 1 on success, or 0 if the input entity is not a meshing session.

	"""

def SaveSessionMeshParams(SESSION_ref, FILENAME_str):

	"""

	This function saves the mesh parameters of a batch mesh session or area (wrap, layers) to a specified file.


	@SESSION_ref object: References the session whose parameters will be saved, which may be
	meshing, layers or volume scenario.
	It may also reference a wrap or layers area.

	@FILENAME_str string: The path of the file where the parameters will be written.

	@returns integer: Returns 1 if SESSION is a valid batch mesh session reference and the file is accessible, or 0 otherwise.

	"""

def SaveSessionQualityCriteria(SESSION_ref, FILENAME_str):

	"""

	This function saves the quality criteria of a batch mesh session to a specified file.


	@SESSION_ref object: References the session whose criteria will be saved, which may be
	meshing, layers or volume scenario.

	@FILENAME_str string: The path of the file where the criteria will be written.

	@returns integer: Returns 1 if SESSION is a valid batch mesh session reference and the file is accessible, or 0 otherwise.

	"""

def WriteStatistics(SESSION_ref, FILENAME_str):

	"""

	This function saves the statistics report of a batch mesh session or meshing scenario to a file.


	@SESSION_ref object: References the session or the meshing scenario that will be saved.

	@FILENAME_str string: The path where the file will be saved.

	@returns integer: Returns 0 if the SESSION is not a valid reference or if the file cannot be accessed, 
	2 if the session has status "Complete" and 1 otherwise.
	If the file exists it is overwritten.

	"""

def SetSessionVisibility(session, visibility):

	"""

	This function sets the visibility of the session.
	The session can be either (Mesh, Layers, Volume, Wrap) Session or (Mesh) Box.
	It can be shown, hidden or it can be isolated (shown alone).
	The session's visibility can be controlled by the respective parameter in the arguments list.


	@session object: Specific session or box object.

	@visibility string: "Show" to show the session.
	"Hide" to hide it.
	"ShowOnly" to isolate it.

	@returns integer: Returns 0 if invalid arguments were specified, 1 otherwise.

	"""

def CopySessionParameters(session, mesh_parameters, quality_criteria):

	"""

	This function copies the mesh parameters and quality criteria of a session to the 
	respective fields of global (Shell or Solid) Mesh Parameters and Quality 
	Criteria. 'session' can be either Session (Mesh, Layers, Volume, Wrap) or Box 
	(Mesh). The Mesh Parameters and the Quality Criteria can be handled
	independently with the use of the respective flags in the arguments list. If no
	optional arguments are specified nothing happens.


	@session object: A reference to a Session (Mesh, Layers, Volume, Wrap) 
	or a Box (Mesh) object.

	@mesh_parameters boolean: (optional)True or False to specify if the mesh parameters will be 
	copied or not.

	@quality_criteria boolean: (optional)True or False to specify if the quality criteria will be
	 copied or not.

	@returns integer: Returns 0 if invalid arguments are specified, 1 otherwise.

	"""

def GetNewLayersArea(parent_session, name, first_height, first_height_method, growth_factor, zero_thickness, layers_prop_name, number_of_layers, additional_outer_layers, orthogonal_layers, smooth_top_cap, switch_to_variable_growth_rate, varibable_growth_rates):

	"""

	This function adds a new layers area in a layers scenario, in the Batch Mesh Manager.


	@parent_session object: References the session where layers area will be added.

	@name string: (optional)The name of the mesh parameters of created area.

	@first_height float: (optional)First layer height value of the mesh parameters of created area.

	@first_height_method string: (optional)Determines whether first layer height value is expressed as an absolute value
	or as a factor (aspect) of the local element length.
	Accepted values "aspect" or "absolute".

	@growth_factor float: (optional)Growth rate of layers.

	@zero_thickness boolean: (optional)Will grow layers for both sides of zero thickness walls.

	@layers_prop_name string: (optional)Property name of generated solid elements.

	@number_of_layers integer: (optional)Number of layers to be generated

	@additional_outer_layers integer: (optional)Additional outer layers to be generated in aspect mode

	@orthogonal_layers integer: (optional)Number of layers on which no vector smoothing will be applied

	@smooth_top_cap boolean: (optional)Apply smooth top cap or not

	@switch_to_variable_growth_rate boolean: (optional)If true then variable growth rate will be applied

	@varibable_growth_rates string: (optional)The variable growth rates as a string

	@returns object: Returns a reference to the newly created layers area.
	In case of an error, the function returns None.

	"""

def GetNewWrapArea(parent_session, name, min_len, max_len, part_pid_proximity, self_proximity, reduction_factor):

	"""

	This function adds a new wrap area in a wrap scenario, in the Batch Mesh Manager.


	@parent_session object: References the session where the wrap area will be added.

	@name string: (optional)The name of the mesh parameters of the created area.

	@min_len float: (optional)Area specific minimum length value.

	@max_len float: (optional)Area specific maximum length value.

	@part_pid_proximity boolean: (optional)Enables proximity refinement between different parts/properties.

	@self_proximity boolean: (optional)Enables self-proximity refinement in a part/property.

	@reduction_factor float: (optional)Further reduction factor of local minimum length.

	@returns object: Returns a reference to the newly created wrap area.
	In case of an error, the function returns None.

	"""

def GetBatchMeshItemActiveState(batch_mesh_item):

	"""

	This function provides the active state of a batch mesh item.


	@batch_mesh_item object: The batch mesh item whose status will be provided.

	@returns boolean: Returns True or False depending on the item's active state.

	"""

def SetBatchMeshItemActiveState(batch_mesh_item, active_state):

	"""

	This function sets the active state of a batch mesh item.


	@batch_mesh_item object: The batch mesh item whose status will be changed.

	@active_state boolean: The desired active status.

	@returns object: Always returns none.

	"""

def GetNewBox(parent_session, contents):

	"""

	This function adds a box in a batch mesh session, in the Batch Mesh Manager.
	


	@parent_session object: References the session where the box will be added.

	@contents object: A list of items suitable for a batch mesh box. Accepted item types are BCBOX and MORPHBOX.

	@returns object: Returns a reference to the newly created box.
	In case of an error, the function returns None.

	"""

