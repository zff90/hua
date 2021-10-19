def ChangeIncludeRepresentation(entities, new_representation):

	"""

	Changes the representation of a given list of Include entities, with a new one from the DM, 
	specified by the string new_representation. This can also be the common representation by
	giving the string 'common'.


	@entities object: A list of include entities.

	@new_representation string: The name of the new representation.

	@returns object: The function returns:
	1) An empty list in the case where all the includes have changed representation successfully.
	2) A list that contains all the includes that did not change representation successfully.

	"""

def ChangeRepresentation(entities, new_representation, property_conflicts, material_conflicts, set_conflicts, rbe_option, distance, mass, deck, include_connectors, spc_dofs, coord_conflicts, node_conflicts, propsection_confilcts):

	"""

	Changes the representation of a given list of ANSA PARTS, with a new one from the DM.


	@entities object: A list of ANSA parts whose representation will change.

	@new_representation string: The name of the new representation.

	@property_conflicts string: (optional)"Offset" creates a new entity.
	"KeepOld" keeps the old value.
	"KeepNew" keeps the new value (Default).

	@material_conflicts string: (optional)"Offset" creates a new entity.
	"KeepOld" keeps the old value.
	"KeepNew" keeps the new value (Default).

	@set_conflicts string: (optional)"Offset" creates a new entity (Default).
	"KeepOld" keeps the old value.
	"KeepNew" keeps the new value.

	@rbe_option string: (optional)String Variable that determines the type of the connecting element to be used.
	Valid types are: "RBE2", "RBE3" and only for "Lumped Mass" Representation.

	@distance float: (optional)Search distance of the respective GEB_MT, valid only for "Trim" Representation.

	@mass float: (optional)Mass field of the respective GEB_MT, valid only for "Trim" Representation.

	@deck string: (optional)A string that describes the deck, valid only for "Trim" Representation.
	(Default: Current Deck)

	@include_connectors boolean: (optional)A boolean that determines if the external connectors will be included 
	in the SPC Representation or the "Don't Use" Representation or the 
	Lumped Mass Representation.
	(Default: False)

	@spc_dofs integer: (optional)Integer that specifies the affected Degrees Of Freedom. 
	Valid only for "SPC" Representation.

	@coord_conflicts string: (optional)"Offset" creates a new entity (Default).
	"KeepOld" keeps the old value.
	"KeepNew" keeps the new value.

	@node_conflicts string: (optional)"Offset" creates a new entity (Default).
	"KeepOld" keeps the old value.
	"KeepNew" keeps the new value.

	@propsection_confilcts string: (optional)"Offset" creates a new entity.
	"KeepOld" keeps the old value.
	"KeepNew" keeps the new value (Default).

	@returns object: Returns a dictionary with keys: 'status' and 'session_group'.
	Under 'status' key, value 0 is returned if an invalid representation was given.
	In all other cases, value 1 is returned.
	Under 'session_group' key, a batch mesh scenario will be returned, that is assigned
	to all parts that required a new mesh.

	"""

def SyncRepresentation(parts):

	"""

	Synchronizes the representation of a given list of ANSA PARTS, to all instances of the
	given ANSA PARTS. Any entities that are included in those instances will be deleted.


	@parts object: A list that contains the parts whose instances will be synchronised.

	@returns integer: Returns 1 on error and 0 on success.

	"""

def SaveRepresentation(ents, save_group_or_part, overwrite_opt, skip_save_for_multi_instances, save_marked_read_only, save_empty_groups, conflicts_option, export_jt, export_png, file_type, return_server_ids, return_value_type, backup_failed_save_folder, export_metadb):

	"""

	Saves the representation of a given list of parts, groups or includes in the DM.
	A DM Root has to be already specified.


	@ents object: A list that contains parts, groups or includes.

	@save_group_or_part string: Determines if groups or inner parts will be saved in DM.
	Accepted values: "GROUP" or "PART".

	@overwrite_opt integer: 0: In case current representation is found in DM,
	the save procedure for the particular part should be skipped.
	In this case (skip) the returned value is 1 (failure).
	1: In case current representation is found in DM,
	it should be overwritten.
	2: In case current representation is found in DM,
	Study Version or another versioning scheme counter
	(see argument: conficts_option) is spinned-up
	(only applies to parts).

	@skip_save_for_multi_instances boolean: (optional)True: Do not save multi-instanciated parts.
	False (default): Save only one instance for each
	multi-instanciated part.

	@save_marked_read_only boolean: (optional)True: Save representation for includes marked as read-only.
	False (default): Do not save representation for includes 
	marked as read-only.

	@save_empty_groups boolean: (optional)True: Save empty groups.
	False (default): Do not save empty groups.

	@conflicts_option string: (optional)The name of the versioning scheme counter attribute to be spinned-up
	(overwrite_opt = 2).
	A versioning scheme counter attribute name: a spin-up is performed
	to the value of that attribute.
	Empty: Study Version is spinned-up instead.

	@export_jt boolean: (optional)True: Save jt file during saving representation of part 
	False (default): Do not save jt file

	@export_png boolean: (optional)True: Save png image during saving representation of part 
	False (default): Do not save png image

	@file_type string: (optional)This argument determines the format of the parts representation files that are about to be saved. Acceptable values are :
	"ANSA", "Nastran", "LsDyna", "PamCrash", "Abaqus", "Radioss", "Ansys", "Fluent", "FluentD", "StarCD", "Uh3D", "Cfd++", "OpenFoam", "Permas", "Moldex3D", "TAITHER", "Sestra", "Theseus", "ScTetra", "TAU", "CGNS", "CGNS2D", "Optistruct"

	@return_server_ids boolean: (optional)True: Returns a python list containing the server ids of the parts saved, in the order of their input. Parts that failed to be saved have a "0" entry.
	False: To be used in conjunction with return_value_type argument.

	@return_value_type string: (optional)"server_ids_and_error_messages" : Returns a python list where each of the input parts has a corresponding entry, listed in the order of their input. 
	The parts that were successfully saved have as corresponding entry their server_id. 
	The ones that failed have as corresponding entry a python list containing the error(s) that resulted to their failure to be saved. 
	"server_ids" : Returns a python list containing the server ids of the parts saved, in the order of their input. Parts that failed to be saved have a "0" entry.
	Warning: This argument is overriden if return_server_ids is True.

	@backup_failed_save_folder string: (optional)Argument only for internal usage.

	@export_metadb boolean: (optional)True: Save metadb file during saving representation of part 
	False (default): Do not save metadb file

	@returns integer: 0 (success): If all entities are saved in DM successfully.
	1 (failure): If the saving procedure has failed or was skipped for at least one 
	             entry of the entities list.
	            
	Warning: Return type may be different. See also arguments "return_server_ids"
	and "return_value_type" that affect the returned value.

	"""

def OpenJtRepresentation(parts):

	"""

	Import in ANSA the Jt image of an empty part, as it is saved in the current DM.
	If a Group is provided, all its children are traveled and their Jt images are imported.


	@parts object: A list containing parts.

	@returns integer: Returns 0 on error and 1 on success.

	"""

def SaveSubsystems(ents, conflicts_option, spin_up_attribute, save_repr_file, export_png, export_jt, export_meta_db, file_type, save_ansa_repr_file, save_include_repr_file, autofix, detailed_results):

	"""

	Saves a given list of subsystems in the DM.
	A DM Root directory must already be specified.


	@ents object: A list that contains subsystems.

	@conflicts_option string: (optional)-'Overwrite'
	-'Skip'
	-'Spin_up' (default)

	@spin_up_attribute string: (optional)'Study Version' (default)

	@save_repr_file string: (optional)-'YES': save along with the subsystem a respective representation file.
	-'NO'
	This argument is only available for backward compatibility reasons.
	Use save_ansa_repr_file and save_include_repr_file instead.

	@export_png string: (optional)-'YES': save along with the subsystem an image in .png format.
	-'NO' (default)

	@export_jt string: (optional)-'YES': save along with the subsystem a respective jt file.
	-'NO' (default)

	@export_meta_db string: (optional)This argument is not yet supported.

	@file_type string: (optional)The file type (file extension) of a subsystem's representative
	file in the DM. The argument can either have the value "ANSA" or
	any supported deck's file name, e.g. Nastran, LsDyna, Radioss, Abaqus, etc.

	@save_ansa_repr_file string: (optional)Possible values: "monolithic" / "references" / "structure_only"
	-"monolithic" : The resulting representation file will be an ANSA database
	containing all ANSA entities.
	-"references" : The resulting representation file will be an ANSA database 
	containing the hierarchy in the Model Browser, but no ANSA entities.
	-"structure_only" : No representation file will be saved.

	@save_include_repr_file string: (optional)Possible values: "monolithic" / "references" / "structure_only"
	-"monolithic" : The resulting representation file will be a Deck file according
	to file_type argument containing all ANSA entities
	-"references" : The resulting representation file will be a Deck file according
	to file_type argument containing references to the Subsystem's children Includes 
	as separate files - e.g: #include "C:/home/my_inner_include.nas"
	-"structure_only" : No representation file will be saved.

	@autofix object: (optional)This argument is a List of strings. Possible values it can contain:
	"filetype_discrepancy"
	"missing_subsystem_inner_part_repr_files"
	"unapplied_numbering_rules"
	"generate_missing_solver_files"
	
	All its member string values will attempt to autofix in case the respective 
	errors have been  encountered.

	@detailed_results boolean: (optional)This argument determines whether the return value will be a list of strings 
	representing the server_ids or a list of "SaveInDmObject" named tuples.
	For more information check the "Return type" field.

	@returns object: - In case the detailed_results argument does not exist or is False:
	The return value is a list with the same size as the ents list (input argument).
	Each entry of the returned list is a string with a special id of the saved subsystem.
	In case the subsystem failed to be saved, a string with zero value is returned ('0').
	- In case the detailed_results argument exists and is True:
	Returns a List containing one "SaveInDMObject" named tuple corresponding to each of the Subsystems that we attempted to save in DM.
	Each "SaveInDMObject" ret contains 4 members:
	ret.entity    : ANSA entity we tried to save(the Simulation Model)
	ret.server_id : (string) The id by which it has been saved in DM
	ret.error     : (string) A description of the reason it failed to be saved.
	ret.inners    : (list)   A list of "SaveInDmObject" named tuples corresponding to the
	                         inner SimulationModels/Subsystems/Includes that were 
	                         involved in Save and have caused save failure

	"""

def OpenSubsystemsInNewTab(server_ids, subsystems, type, view, dm_system, tab_name, expand_all, open_in_viewer):

	"""
	Deprecated since version 19.0.0. Use function OpenDMObjectsInNewTab instead.

	This function can be used to open one or more Subsystem's hierarchy in a new tab
	in DM Browser or SDM CONSOLE.
	Specific objects can also be opened in a new tab, such as "parts", "includes" etc.


	@server_ids object: (optional)A list with DM Object server ids.

	@subsystems object: (optional)A list with ANSA entities.

	@type string: (optional)The queried type needs to be defined, e.g. "Subsystems", "parts".
	When undefined, the function will return False.

	@view string: (optional)The new Tab's view, e.g. "Default", "Flat" or a user defined in the dm_views.xml.
	When undefined, the function will return False.

	@dm_system string: (optional)The DM root that will be queried.

	@tab_name string: (optional)The new tab will be given this name.

	@expand_all boolean: (optional)If set to True, all items in the new tab will be expanded.

	@open_in_viewer boolean: (optional)If set to True, all items in the new tab will be loaded to the meta viewer.

	@returns boolean: Returns True if the tab is opened succesfully, otherwise False.

	"""

	import warnings; warnings.warn("Deprecated since version 19.0.0. Use function OpenDMObjectsInNewTab instead.", DeprecationWarning)

def SaveSimulationRun(ents, conflicts_option, spin_up_attribute, file_content_loadcase, file_content_sim_model,file_type, use_loaded_loadcase, autofix, use_loaded_sim_model, ansa_db_save_mode, file_content_base_modules):

	"""

	Saves the representation of a given list of simulation runs in the DM. 
	The file will be saved/outputted corresponding to the file_type format. A DM Root has to be specified.


	@ents object: A list that contains Simulation Runs that the user intends to save in DM.

	@conflicts_option string: (optional)Can support 3 possible values: "Overwrite" / "Skip" / "SpinUp".
	Determines what will happen in case that a Simulation Run that is 
	intented to be saved, is found already inside DM.

	@spin_up_attribute string: (optional)Any of the attributes a SimulationRun has in the current DM root and for 
	which spinning up could be achieved. e.g. "Study Version".
	Note here that even though this is an optional argument, in case that
	conflicts_option="SpinUp", then this argument becomes mandatory.

	@file_content_loadcase string: (optional)Possible values: "monolithic" / "references" / "existing_setup"
	-"monolithic": The resulting Simulation Run file will contain ANSA 
	 entities of its loadcase.
	-"references": The resulting Simulation Run file will contain reference
	  line to a separate file of its loadcase.
	  e.g. #include "C:/home/my_loadcase.nas"
	-"existing_setup": The resulting Simulation Run file will either be a 
	  reference line to its Loadcase or its ANSA entities, depending on the
	  options "ReadOnly" and "Inline" of the Loadcase's  Include.
	-"reference_inner_contents": The resulting Simulation Run file will 
	  contain reference lines directly to inner contents of its Loadcase.
	  e.g. #include "C:/home/MyDm/Barriers/Bar1.dat

	@file_content_sim_model string: (optional)Possible values: "monolithic" / "references" / "existing_setup"
	-"monolithic" : The resulting Simulation Run file will contain ANSA
	  entities of its simulation model.
	-"references" : The resulting Simulation Run file will contain
	  reference line to a separate file of its simulation model.
	  e.g. #include "C:/home/my_sim_model.nas"
	-"existing_setup" : The resulting Simulation Run file will either be a 
	  reference line to its Simulation model or its ANSA entities,
	  depending on the options "ReadOnly" and "Inline"  of the Simulation 
	  Model's Include.
	-"reference_inner_contents": The resulting Simulation Run file will 
	  contain reference lines directly to inner contents of its Simulation 
	  Model.
	  e.g. #include "C:/home/MyDm/Subsystems/Sub1.nas

	@file_type anything: (optional)One of: "ANSA", "structure_only" or constants of Decks
	(e.g. ansa.constants.NASTRAN) 
	In each case:
	-"structure_only": an ".xml" file will be saved in DM for each Simulation Model, 
	                   containing only its hierarchy.
	-"ANSA": ANSA database 
	-ansa.constants.XXXX: a deck format to Output the SimModel.
	
	In case the argument is ommitted, the Current Deck is used.
	Attention!! Current deck outputting is currently fully supported.

	@use_loaded_loadcase boolean: (optional)This argument determines whether the Loadcase that will be outputted in the 
	Simulation Run representation file will be the one currently loaded in ANSA.
	Hence:
	-True: Use Loadcase currently loaded in ANSA (which means that changes of 
	  the user on the current session of ANSA will affect it).
	-False:  Use Loadcase as found in the library items that it refers to, as these 
	  are found in DM.

	@autofix object: (optional)This argument is a List of strings. Possible values it can contain:
	-"filetype_discrepancy"
	-"missing_subsystem_includes"
	-"reduced_representations_not_ready_for_use"
	-"missing_display_include_on_FRF_output".
	-"generate_missing_solver_files".
	
	All its member string values will attempt to autofix in case that the 
	respective errors have been encountered.

	@use_loaded_sim_model boolean: (optional)This argument determines whether the SimModel that will be outputted in the 
	Simulation Run representation file will be the one currently loaded in ANSA.
	Hence:
	-True: Use Loadcase currently loaded in ANSA (which means that changes of 
	  the user on the current session of ANSA will affect it).
	-False: Use Loadcase as found in DM.

	@ansa_db_save_mode string: (optional)This arguments controls the contents of the ansa file to be produced and uploaded
	in DM. Accepted values are the following:
	-"monolithic" : A full ansa db will be uploaded in DM
	-"empty_hierarchy" : A db containing an empty description of the selected 
	  Simulation Run 
	-"structure_only" : No ansa db will be uploaded in DM

	@file_content_base_modules string: (optional)Possible values: "monolithic" / "references" / "existing_setup"
	-"monolithic" : Entities of Base Modules of Simulation Run 
	  will be written monolithically in the resulting Simulation Run file
	-"references" : The resulting Simulation Run file will contain
	  reference lines to separate files of Base Modules 
	  e.g. #include "C:/home/my_base_module.nas"
	-"existing_setup" : Base Modules' handling will depend on
	  value of "Output Option" attribute

	@returns object: Returns a list containing "SaveInDMObject" objects, corresponding to each one of the Simulation Runs 
	that we attempted to save in DM.
	Each "SaveInDMObject" ret contains 3 members:
	ret.entity      : The ANSA entity we tried to save (the Simulation Run).
	ret.server_id   : (string) The id by which it has been saved in DM.
	ret.error       : (string) A description of the reason it failed to be saved.
	ret.inners      : (list) A list of "SaveInDmObject" objects corresponding to the
	                         inner SimulationModels/Subsystems/Includes that were 
	                         involved in Save and have caused save failure.

	"""

def SaveSimulationModel(ents, file_type, conflicts_option, spin_up_attribute,file_content, export_png, export_jt, autofix, contents_based_spin_up_attribute):

	"""

	Saves the representation of a given list of simulation models in the DM. 
	The files may be ANSA databases, simple XML files containing only hierarchy 
	information or current deck output files. A DM Root has to be already specified.


	@ents object: A list that contains simulation models.

	@file_type anything: (optional)One of: "ANSA", "structure_only" or constants of Decks
	(e.g. ansa.constants.NASTRAN) 
	In each case:
	-"structure_only": an ".xml" file will be saved in DM for each Simulation Model, 
	                   containing only its hierarchy.
	-"ANSA": ANSA database 
	-ansa.constants.XXXX: a deck format to Output the SimModel.
	
	Attention!! Current deck outputting is currently fully supported.

	@conflicts_option string: (optional)Possible values: "Overwrite" / "Skip" / "SpinUp".
	Determines what will happen in case a Simulation Model that is intented 
	to be saved, is already found inside DM.

	@spin_up_attribute string: (optional)Any of the attributes a Simulation Model has in the current DM root and for 
	which spinning up could be achieved. Example: "Study Version".
	Note here that even though this is an optional argument in general, 
	in case conflicts_option="SpinUp" then this argument becomes mandatory.

	@file_content string: (optional)Examine this argument in combination with the "file_type" argument.
	Assuming file_type="structure_only":
	- file_content argument is not compatible with file_type : "structure_only" 
	
	Assuming file_type="ANSA":
	- file_content="monolithic" : The Simulation Model representation file will be 
	  an .ansa file containing all the ANSA entities of its subsystems, and also all 
	  the information regarding its hierarchy loaded in its Model Browser.
	- file_content="references": The Simulation Model representation file 
	  will be an .ansa file containing no ANSA entities, but only the information 
	  regarding its hierarchy loaded in its Model Browser.
	
	Assuming file_type=ansa.constants.xxx (e.g. ansa.constants.NASTRAN):
	- file_content="monolithic" : The Simulation Model representation file will be
	  a file of the specified DeckCode format(e.g. a .nas file) containing all the 
	  ANSA entities of its subsystems, and also all the information regarding its 
	  hierarchy loaded in its Model Browser.
	-file_content="references" : The Simulation Model representation file 
	  will be a file of the specified DeckCode format (e.g. a .nas file) containing 
	  reference lines to the separate files of its Subsystems
	(e.g. #include "C/home/Subsystem1.nas", 
	      #include "C:/home/Subsystem2.nas")

	@export_png boolean: (optional)Possible values: True / False
	Determines whether a .png preview file will be created and stored in 
	DM for each one of the saved Simulation Models.

	@export_jt boolean: (optional)Possible values: True / False
	Determines whether a .jt light representation file will be created and 
	stored in DM for each one of the saved Simulation Models.

	@autofix object: (optional)This argument is a List of strings. Possible values it can contain:
	"filetype_discrepancy"
	"missing_subsystem_includes".
	"generate_missing_solver_files"
	
	All its member string values will attempt to autofix in case the respective 
	errors have been  encountered.

	@contents_based_spin_up_attribute string: (optional)If current DM schema supports contents based spinup of Simulation Model, specify any of the versioning scheme attributes of Simulation Model's parent DM object type.

	@returns object: Returns a List containing one "SaveInDMObject" named tuple corresponding to each of the Simulation Runs 
	that we attempted to save in DM.
	Each "SaveInDMObject" ret contains 4 members:
	ret.entity    : ANSA entity we tried to save(the Simulation Model)
	ret.server_id : (string) The id by which it has been saved in DM
	ret.error     : (string) A description of the reason it failed to be saved.
	ret.inners    : (list)   A list of "SaveInDmObject" named tuples corresponding to the
	                         inner SimulationModels/Subsystems/Includes that were 
	                         involved in Save and have caused save failure

	"""

def CheckForUpdates(type, entities, data):

	"""

	Search in DM for:
	1. updates of specified entities, or
	2. entities of defined ANSA type which satisfy specified filters.


	@type string: (optional)The ANSA type of the entities which are searched
	in DM (2nd Use Case).

	@entities object: (optional)A list of DM objects (e.g. Parts, Subsystems, etc.)
	to check for updates in DM (1st Use Case).

	@data object: Based on the Use Case, it can be:
	1. a dictionary to specify the Check DM Updates options, or
	2. a list to specify the filters which are applied to DM.

	@returns object: Returns a dictionary with the following keys and values:
	key = 'error'
	value = 0(Success), 1(Nothing found), 2(No DM Root was set), 3(No access to DM Root),
	        4(Error in filters)
	key = 'output'
	value = A list with the results. The result can be:
	        sub-list, when updates are found for the specified entity, and
	        0, when no results are found for the specified entity
	
	Each one of the result entities in the sub-lists has a "DM Updates" attribute which
	describe the type of update (e.g. "Newer File", "Newer Version", etc.). These
	entities can be downloaded by using the DownloadEntities() script function.

	"""

def DoesRepresentationExist(entity, representation, deck):

	"""

	This functions checks if the given representation exists in DM for one or more parts or includes.


	@entity object: May either be one ANSA Part or Include, or a list containing 
	multiple Parts/Includes.

	@representation string: A string describing a potential representation name.

	@deck constant: (optional)The deck, in case that the entity is an Include.

	@returns object: When the input to the function is one entity:
	        The function returns 1, if a representation file by the name of repr_name exists.
	        In case that PART is not a valid part or a file by the name repr_name does not exist, 0 is returned.
	When a list with entities is given as input:
	        The function returns a dictionary with the entity as the key and the return value as the value.

	"""

def DownloadEntities(part, property_conflicts, material_conflicts, set_conflicts, coord_conflicts, node_conflicts):

	"""

	This function may only be used along with CheckForUpdates function.


	@part object: Contains DM Items which were output from
	the CheckForUpdates() function, in the same way they
	were given in the output array. Otherwise, they may be
	collected from the database and given as a list.

	@property_conflicts string: (optional)-"Offset" creates a new entity.
	-"KeepOld" keeps the old value.
	-"KeepNew" keeps the new value (Default).

	@material_conflicts string: (optional)-"Offset" creates a new entity.
	-"KeepOld" keeps the old value.
	-"KeepNew" keeps the new value (Default).

	@set_conflicts string: (optional)-"Offset" creates a new entity (Default).
	-"KeepOld" keeps the old value.
	-"KeepNew" keeps the new value.

	@coord_conflicts string: (optional)-"Offset" creates a new entity (Default).
	-"KeepOld" keeps the old value.
	-"KeepNew" keeps the new value.

	@node_conflicts constant: (optional)-"Offset" creates a new entity (Default).
	-"KeepOld" keeps the old value.
	-"KeepNew" keeps the new value.

	@returns integer: Returns the total number of entities that were actually downloaded from DM.

	"""

def FindMatches(parts, tolerance):

	"""

	Given a parts list, this function searches the DM for matching parts, under the tolerance value.


	@parts object: A list that contains the ANSA parts for which a match will be searched in DM.

	@tolerance float: The match tolerance value.

	@returns object: Returns the list of matches that were found in DM. Otherwise it returns None.

	"""

def SaveUpdates(dm_items, dm_root):

	"""

	This function may only be used along with CheckForUpdates function.
	It accepts the CheckForUpdates's function output.


	@dm_items object: A list that contains DM Items which were output from the CheckForUpdates() 
	function, in the same way they were given in the output array.
	Otherwise, a single result may be given.

	@dm_root string: (optional)The target DM Root, where the update will be copied. 
	When unspecified, the current DM is used.

	@returns integer: Returns the total number of DM items that were successfully uploaded to the target DM.

	"""

def AddIncludeFile (filename, module_id, deck_name, st_version_conflict, entity_representation, entity_name, entity_version):

	"""

	This function adds a new file in DM, under the includes directory, based on the arguments provided. The file
	specified by the string variable 'file_path' will be copied in DM, under a directory structure which will be created
	based on the string variables 'module_id', 'deck' and a number of optional ones, which can be set to define
	more accurately the save path. Varlen is the list of optional (argument name,value) pairs.


	@filename string: The include's filename.

	@module_id string: The module id of the include file.

	@deck_name string: A string specifying the deck, i.e. constants.

	@st_version_conflict string: (optional)Defines the action to be taken in case another entry with the 
	characteristis defined above, has already been added in DM. 
	In such a case you can decide either to create a new study version
	by setting the variable to 'NEW_ST_VERSION' or overwite the 
	existing file in DM by setting the variable to 'OVERWRITE'.

	@entity_representation string: (optional)Defines the representation name to be used during the building of the 
	DM directory structure where the new file will be added. If it is not set, 
	the default representation 'common' will be used.

	@entity_name string: (optional)Defines the name to be assigned to new file to be created in DM. If this 
	is not set, the name will be extracted from the string variable 'file_path'. 
	The file_path's last section will be assigned as name. If this also fails,
	then the file will be assigned the default name 'Default_DM_Name'.

	@entity_version string: (optional)Defines the version name to be used during the building of the DM directory
	structure where the new file will be added. If it is not set, the default
	version 'A1' will be used.

	@returns integer: Returns 0 if the file has been successfully added in DM, or 1 otherwise.

	"""

def AddIncludes(includes, st_version_option):

	"""

	This function adds new files in DM, under the includes directory, based on the DM field values of the 
	specified include entities, provided in matrix includes. For each of the include entities, the file specified
	in the field 'FullPathName' will be copied in DM, under a directory structure which will be created based
	on the include's corresponding DM values. Varlen is the list of optional (argument name,value) pairs.


	@includes object: An entity or a list of include entities.

	@st_version_option string: (optional)Defines the action to be taken in case another entry with the
	attributes defined above, has already been added in DM.
	In such a case you can decide either to create a new study version
	by setting the variable to 'NEW_ST_VERSION',
	overwite the existing file in DM by setting the variable
	to 'OVERWRITE', or skip the specific include by setting the variable
	to "SKIP". The default value is 'NEW_ST_VERSION'.

	@returns integer: Returns 0 if the files have been successfully added in DM and 1 otherwise.

	"""

def GetCommonProperties():

	"""

	The function will return common Properties among the "Simulation Models", "Simulation Runs" and "Loadcases" types.


	@returns object: Returns a dictionary with the Property name and it's value.

	"""

def SetCommonProperties(names_values, apply_to_subsystems):

	"""

	The function will set values for common Properties among the "Simulation Models",
	"Simulation Runs" and "Loadcases" types.


	@names_values object: A dictionary with the Property name and its value.

	@apply_to_subsystems boolean: (optional)When True, the common Properties will be applied to all Subsystems 
	existing in the current Model.

	@returns boolean: The function will return True if the values for common Properties were set successfully.
	Otherwise it will return False.

	"""

def GetEntityProperties(entity):

	"""

	When connected to a DM, one may need to get an entity's DM Properties as a list.


	@entity object: The input entity whose properties will be returned.
	It may be one of the following: 
	-ANSAPART
	-ANSA_SUBSYSTEM
	-ANSA_SIMULATION_MODEL
	-ANSA_CONFIGURATION
	-ANSA_SIMULATION_RUN
	-ANSA_LOADCASE
	-ANSA_LIBRARY_ITEM
	-INCLUDE

	@returns object: Returns a list containing the DM Properties.
	Any properties that are ANSA Attributes, are returned with the "DM" prefix, e.g."DM/Discipline".

	"""

def ReadComponentXml(filename):

	"""

	Given an XML that was downloaded from DM, either for a Subsystem or a Simulation Model,
	this function will merge the hierarchy in to the current Model.


	@filename string: The xml filepath.

	@returns integer: Returns 1 on success.

	"""

def LoadEntities(entities, load):

	"""

	This functions loads/unloads Model Browser entities from DM.
	When in Load mode all specified entities will first be cleared of their contents and then be loaded (downloaded) from DM.
	When in Unload mode, entities will be cleared and left empty.


	@entities object: A list of Model Browser entities which can be loaded/unloaded.
	These can be Subsystems, Simulation Models, Simulation Runs, 
	Library Items, or any combination of them.

	@load boolean: True: Load mode.
	False: Unload mode.

	@returns: Returns an empty list on success.In case of failure it returns a list containing the references of the objects which failed to load/unload.

	"""

def AddSimulationRun(names_values, file_type, overwrite, link):

	"""

	Adds a Simulation Run to the DM. If the Simulation Run file contains a hierarchy 
	of Includes, they will be added as well to the DM.


	@names_values object: All the attribute values of the Simulation Run.

	@file_type string: (optional)The file type of the Simulation Run file (eg. NASTRAN, LSDYNA, etc).

	@overwrite boolean: (optional)When set to True, the Simulation Run will not replace an existing 
	Simulation Run in the DM if it has the same primary values.
	(Default: False)

	@link boolean: (optional)When set to True, files will not be copied to the DM, but hard linked.
	(Default: False)

	@returns object: Returns the server id of the newly added Simulation Run, unless the addition 
	fails or the overwrite flag is False and the Simulation Run already exists in 
	the DM (then it returns None).

	"""

def GetSaveRepresentationConflictOptions(entity, save_group_or_part):

	"""

	When trying to upload an entity to DM, one can get the conflict options when the
	entity already exists in DM.


	@entity object: The input entity.

	@save_group_or_part string: (optional)Determines if a Group or Part will be checked in DM.
	Valid values: "GROUP" or "PART".
	(Default: "PART")

	@returns object: Returns a list with the available conflict options, only if the entity already
	exists in DM. Otherwise, it returns None.

	"""

def UpdateEntityAttributesFromDM(entities):

	"""

	The function will update the values for all existing secondary Attributes 
	of the input Model Browser Entities with the respective values for anything 
	that is found in DM.


	@entities object: A list containing the Model Browser Containers, or a single entity.
	Accepted entities are Parts, Subsystems, Simulation_Models, etc.

	@returns boolean: Returns True if at least one entity's Attribute values were updated.

	"""

def LoadInterfaceRepresentation(subsystems, detailed_results):

	"""

	Loads the Interface Representation of Subsystems and Library Items.


	@subsystems object: A list of containers whose Interface 
	Representation is going to be loaded.

	@detailed_results boolean: (optional)Return the error for each container whose Interface 
	Representation failed to be loaded.
	(Default: False)

	@returns object: A list of containers whose Interface Representation failed to be loaded.
	If 'detailed_results' argument is set to True, a dictionary where:
	        key: is the container which failed to be loaded
	        value: a string comment ('invalid entity'/'missing DM file'/'internal load error')

	"""

def SaveLoadcase(ents, file_type, conflicts_option, spin_up_attribute, file_content, autofix):

	"""

	Saves the representation of a given list of loadcases in the DM. 
	The files may be ANSA databases, simple XML files containing only hierarchy 
	information or current deck output files. A DM Root has to be already specified.


	@ents object: A list that contains Loadcases.

	@file_type anything: (optional)One of: "ANSA", "structure_only" or constants of Decks
	(e.g. ansa.constants.NASTRAN) 
	In each case:
	-"structure_only": an ".xml" file will be saved in DM for each Loadcase, 
	                   containing only its hierarchy.
	-"ANSA": ANSA database 
	-ansa.constants.XXXX: a deck format to Output the Loadcase.

	@conflicts_option string: (optional)Possible values: "Overwrite" / "Skip" / "SpinUp".
	Determines what will happen in case a Loadcase that is intented 
	to be saved, is already found inside DM.

	@spin_up_attribute string: (optional)Any of the attributes a Loadcase has in the current DM root and for 
	which spinning up could be achieved. Example: "Study Version".
	Note here that even though this is an optional argument in general, 
	in case conflicts_option is "SpinUp" then this argument becomes mandatory.

	@file_content string: (optional)Examine this argument in combination with the "file_type" argument.
	Assuming file_type="structure_only":
	- file_content argument is not compatible with file_type : "structure_only" 
	
	Assuming file_type="ANSA":
	- file_content="monolithic" : The Loadcase representation file will be 
	  an .ansa file containing all the ANSA entities of its subsystems and library 
	  items,and also all the information regarding its hierarchy loaded in its 
	  Model Browser.
	- file_content="references": The Loadcase representation file 
	  will be an .ansa file containing no ANSA entities, but only the information 
	  regarding its hierarchy loaded in its Model Browser.
	
	Assuming file_type=ansa.constants.xxx (e.g. ansa.constants.NASTRAN):
	- file_content="monolithic" : The Loadcase representation file will be
	  a file of the specified DeckCode format(e.g. a .nas file) containing all the 
	  ANSA entities of its subsystems and library items, and also all the 
	  information regarding its hierarchy loaded in its Model Browser.
	-file_content="references" : The Loadcase representation file 
	  will be a file of the specified DeckCode format (e.g. a .nas file) containing 
	  reference lines to the separate files of its Subsystems and Library Items.
	(e.g. #include "C/home/Subsystem1.nas", 
	      #include "C:/home/Subsystem2.nas")

	@autofix object: (optional)This argument is a List of strings. Possible values it can contain:
	"filetype_discrepancy"
	"missing_subsystem_includes".
	"generate_missing_solver_files"
	
	All its member string values will attempt to autofix in case the respective 
	errors have been  encountered.

	@returns object: Returns a List containing one "SaveInDMObject" named tuple corresponding to each of the Loadcases 
	that we attempted to save in DM.
	Each "SaveInDMObject" ret contains 4 members:
	ret.entity    : ANSA entity we tried to save(the Loadcase)
	ret.server_id : (string) The id by which it has been saved in DM
	ret.error     : (string) A description of the reason it failed to be saved.
	ret.inners    : (list)   A list of "SaveInDmObject" named tuples corresponding to the
	                         inner LibItems/Subsystems/Includes that were 
	                         involved in Save and have caused save failure

	"""

def DownloadDMObjects(server_ids, type, hierarchy_only):

	"""

	Download objects from DM by providing their server ids. Optionally, the type of DM
	objects can be provided to ensure that only objects of the specified type will be
	downloaded. For Subsystems, it is possible to download only the parts hierarchy.


	@server_ids object: the server id(s) of the DM object(s) to be downloaded.
	The value be a string (for single object) or a list
	of strings (for multiple objects).

	@type string: (optional)the type of DM objects to be downloaded. When it is
	specified, only objects of this type will be downloaded.
	The specified type can be ANSA type (e.g. ANSA_LOADCASE)
	or the DM type defined through the Data Model (e.g. Loadcase).

	@hierarchy_only boolean: (optional)specify whether the representation (False) or just the parts
	hierarchy (True) will be downloaded. Default value is False.
	When the value is set True, the type should also be defined
	as it is supported only for Subsystems.

	@returns object: Return a list of booleans with size equal to the size of the server ids list. The
	values can be True on success or False on failure.

	"""

def UploadInterfaceRepresentation(mbcontainers, force_upload, detailed_results):

	"""

	Uploads the Interface Representation of valid Model Browser Containers to the 
	connected DM.


	@mbcontainers object: A list of Model Browser Containers that their 
	Interface Representation will be uploaded to 
	the currently connected DM.

	@force_upload boolean: (optional)If set to False, Containers which already 
	have an uploaded Interface Representation file 
	in DM will be skipped.
	If set to True (default), Interface Representation file 
	of these containers will be overwritten.

	@detailed_results boolean: (optional)Return the error for each container whose Interface 
	Representation failed to be uploaded in DM
	(Default: False)

	@returns object: A list of Model Browser Containers whose Interface Representation failed to be uploaded in DM.
	If 'detailed_results' argument is set to True, a dictionary where:
	        key: is the failed container
	        value: a string comment

	"""

def SaveLibraryItems(ents, conflicts_option, spin_up_attribute, autofix):

	"""

	Saves the representation of a given list of library items in the DM. 
	A DM Root has to be already specified.


	@ents object: A list that contains Library Items.

	@conflicts_option string: (optional)Possible values: "Overwrite" / "Skip" / "SpinUp".
	Determines what will happen in case a Library Item that is intented 
	to be saved, is already found inside DM.

	@spin_up_attribute string: (optional)Any of the attributes a Library Item has in the current DM root and for 
	which spinning up could be achieved. Example: "Study Version".
	Note here that even though this is an optional argument in general, 
	in case conflicts_option is "SpinUp" then this argument becomes mandatory.

	@autofix object: (optional)This argument is a List of strings. Possible values it can contain:
	"unapplied_numbering_rules"
	
	All its member string values will attempt to autofix in case the respective 
	errors have been  encountered.

	@returns object: Returns a List containing one "SaveInDMObject" named tuple corresponding to each of the Library Items 
	that we attempted to save in DM.
	Each "SaveInDMObject" ret contains 4 members:
	ret.entity    : ANSA entity we tried to save(the Library Item)
	ret.server_id : (string) The id by which it has been saved in DM
	ret.error     : (string) A description of the reason it failed to be saved.
	ret.inners    : (list)   A list of "SaveInDmObject" named tuples corresponding to the
	                         inner LibItems/Includes that were 
	                         involved in Save and have caused save failure

	"""

def NextIteration(server_ids):

	"""

	Create a Next Iteration of DM objects providing their server ids.
	The result is an empty hierarchy of the specified DM objects.


	@server_ids object: the server id(s) of the DM object(s) to create a Next Iteration.
	The value can be a string (for single object) or a list
	of strings (for multiple objects).

	@returns object: Returns a dictionary containing pairs of:
	<Requested Server Id - Result of Next Iteration>
	Result of Next Iteration can be "Success" or "Invalid for Next Iteration"

	"""

def RefreshEntriesInCurrentTab(server_ids, entities, type):

	"""

	This function refreshes entries as given with server ids or entities and entity type in current tab.
	Function will fail for cases like: 
	- no entity type is given
	- no server ids and no entitites are given
	- couldn't collect server ids for input arguments
	- entity type does not match the type of the tab. Excluded cases: Subsystem in Simulation Model tab, Parts in any tab 
	
	If entities list is NULL, server ids list will be used to refresh tab.
	


	@server_ids object: (optional)This argument is a list of server ids for the entries we want to refresh in tab.

	@entities object: (optional)This argument is a list of entities we want to refresh (e.g., subsystems).

	@type string: (optional)This argument is the entity type of the entries we want to refresh.

	@returns boolean: Returns True for success,
	        False otherwise.

	"""

def GetChildIdsWithRelativePositions(object_id):

	"""

	This function, given a row id, returns a dictionary with this item's children ids and the respective 
	transformation matrices.  


	@object_id string: This argument is the row id of the item we will get further information from 
	(children row ids and transformation matrices).

	@returns: Returns a dictionary with children row ids and the repsective transformation matrix in case of success,
	        None or NULL otherwise.

	"""

def SendDMObjectsToOtherDM(server_ids, path):

	"""
	Deprecated since version 22.0.0. Use function SendDMObjectsToDM instead.

	Send a list of DM Objects' server ids to a specified local path.


	@server_ids object: a list of strings for the given server ids of the DM Objects.

	@path string: the absolute path of the local DM root.

	@returns object: Returns a Dictionary of type {server_id : (error_code, new_server_id, error_message)}, where:
	- server_id (String) is the server id of the checked-out item,
	- result_code (Int) can be 0 for success, 1 for failure, 2 for skip, 3 for spin-up, and 4 for next iteration,
	- new_server_id (String) is the new Server Id of the item,
	- error_message (String) is the message/reason of failure or skip.

	"""

	import warnings; warnings.warn("Deprecated since version 22.0.0. Use function SendDMObjectsToDM instead.", DeprecationWarning)

def OpenDMBrowserToSelect(type, query, server_ids):

	"""

	OpenDMBrowserToSelect function opens DM Browser on current DM root and allows user to select DM objects.
	User can select one or multiple items and press the 'Download' button in order to get the selected DM objects 
	or press ESC to close DM Browser without selecting anything.
	


	@type string: Give object type to open DM Browse on the respective tab

	@query object: (optional)Give query to be applied to DM Browser before launch (as used in dm.QueryDMObjects):
	* A list of [<attribute_name>, <condition>, <value>] lists which specify the query. 
	* A BetaQL string

	@server_ids object: (optional)Give specific server ids to be filtered in tab (applied if 'query' is not given)

	@returns object: A list with the selected DM Objects

	"""

def SendDMObjectsToDM(server_ids, path):

	"""

	Send a list of DM Objects' server ids to a specified local path or to their source DM Path.


	@server_ids object: a list of strings for the given server ids of the DM Objects.

	@path string: (optional)the absolute path of the local DM root. When it is not specified, the DM Objects are sent to their source DM Path (they should be descendants of already transferred DM Objects).

	@returns object: Returns a Dictionary of type {server_id : SendToDMResult}, where:
	- server_id (String) is the server id of the checked-out item,
	- SendToDMResult (Object) with members:
	  - result (Int) can be 0 for success, 1 for failure, 2 for skip, 3 for spin-up, and 4 for next iteration,
	  - new_server_id (String) is the new Server Id of the item,
	  - output_path (String) is the DM Path where the DM Objects were sent,
	  - result_message (String) is the message based on the result.

	"""

def loadDMFoldersOfPath(title, dm_path):

	"""

	Load the DM items and folders, which are found in a defined path, in a pop-up
	window. The user can select only one of the displayed entities.


	@title string: is the title of the pop-up window.

	@dm_path string: is the DM path of DM items and folders.

	@returns object: The function returns a list [error_code, selection_name]
	error_code:     int      0      if input is correct
	                        -1      if 'dm_path' is invalid
	                        -2      if cancel was pressed
	                        -100    if the user does not have respective privileges
	selection_name: str     is the name of selected entity.

	"""

def AddAttachmentToFolder(entity, server_id, folder_name, filename, attribute_name, entity_type, link):

	"""

	This function can be used to:
	- add a file under a folder in the Library Items,
	- attach a file/folder under a DM Object's attribute of type Attached File/Directory
	  respectively. If this attribute does not exist, it is created as Additional Attribute.
	A DM root should have been specified.


	@entity object: (optional)the ANSA entity to be found in the connected
	DM root. The file/folder will be attached under
	an attribute of this object (if found in DM).

	@server_id string: (optional)the server id of the object contained to the
	connected DM root. The file/folder will be
	attached under an attribute of this object.

	@folder_name string: (optional)the name of the folder in the Library Items,
	where the specified file will be attached.
	For DM Objects in file-based DM, a sub-folder
	with this name will be created, and the file
	will be placed there.

	@filename string: the full path of the file/folder to be attached.

	@attribute_name string: (optional)the name of the DM Object's attribute where the
	specified file/folder will be attached.

	@entity_type string: (optional)the type of the DM object.

	@link boolean: (optional)enables the ability to link a folder and not copy
	its contents under a DM Object's attribute. By
	default, the contents are copied (False).

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def DeleteAttachment(entity, server_id, folder_name, filename, entity_type):

	"""

	When connected to a DM, this function allows for an existing attachment to a DM object to be deleted. 
	If no DM Object is specified, a library item can be deleted.


	@entity object: (optional)When this argument is given, the ANSA entity will be searched in DM and if found, 
	the attachment will be deleted from the corresponding DM Object.

	@server_id string: (optional)The DM Object's server id, whose attachment will be deleted.

	@folder_name string: (optional)A subfolder with this name will be deleted.

	@filename string: (optional)The filename which will be deleted.

	@entity_type string: (optional)If the server_id is given as an argument, one may define the Object's type by 
	using this argument.

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def DownloadAttachment(entity, server_id, folder_name, output_folder, subfolder_name, filename, entity_type, attribute_name):

	"""

	Downloads the attachments of an object contained to the defined DM root. A DM root
	should have been specified.


	@entity object: (optional)the ANSA entity to be found in the connected
	DM root. The attachments of this object (if
	found in DM) will be downloaded.

	@server_id string: (optional)the server id of the object contained to the
	connected DM root. The attachments of this
	object will be downloaded.

	@folder_name string: (optional)the name of the folder which contains the
	attachments.

	@output_folder string: the full path of the folder where the attachments
	will be downloaded.

	@subfolder_name string: (optional)the name of the subfolder to be downloaded.

	@filename string: (optional)the name of the file to be downloaded.

	@entity_type string: (optional)the type of the DM object.

	@attribute_name string: (optional)the name of attribute which contains the
	attachments.

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def CreateAttachedFolder(entity, server_id, attribute_name, entity_type):

	"""

	Creates an empty attached folder under an existing object in DM. New files/folders
	can be added as attachments in that folder afterwards. A DM root should have been
	specified.


	@entity object: (optional)the ANSA entity to be found in the connected
	DM root. The new folder will be attached under
	this object (if found in DM).

	@server_id string: (optional)the server id of the object contained to the
	connected DM root. The new folder will be
	attached under this object.

	@attribute_name string: (optional)the name of the folder to be attached.

	@entity_type string: (optional)the type of the DM object.

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def CreateNewSubFolder(entity, server_id, folder_name, attribute_name, entity_type):

	"""

	Creates an empty subfolder in an exisitng attached folder of a DM object. New
	files/folders can be added as attachments in that subfolder afterwards. A DM root
	should have been specified. This function can also be used to create subfolders
	for library items in DM (e.g."batch_mesh_sessions").


	@entity object: (optional)the ANSA entity to be found in the connected
	DM root. The new subfolder will be attached
	under this object (if found in DM).

	@server_id string: (optional)the server id of the object contained to the
	connected DM root. The new subfolder will
	be attached under this object.

	@folder_name string: the name of the subfolder to be attached.

	@attribute_name string: (optional)the name of the parent attribute/folder where
	the new subfolder will be created. The default
	value id 'DA'.

	@entity_type string: (optional)the type of the DM object.

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def DownloadLibraryItem(library, output_folder, filename):

	"""

	This function is used to download a file from the DM library items, e.g. a "batch_mesh_session".  


	@library string: The library item's type.

	@output_folder string: (optional)The folder where the item will be copied.
	Although it's an optional argument, it needs to be defined.

	@filename string: (optional)The library item's name.
	Although it's an optional argument, it needs to be defined.

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def QueryForAllResults(type):

	"""

	Gets a list with all the items in DM for a specific type.


	@type string: The type of the DM Object. The specified type can be ANSA type
	(e.g. ANSA_SUBSYSTEM) or the DM type defined through the Data
	Model (e.g. Subsystems). The supported DM Objects are Parts,
	Subsystems, and Configurations ('configurations').

	@returns: Returns a list with dictionaries for each DM entry. The dictionary contains all the attributes
	of the DM entry, including its Module Id, Version, Study Version, Representation etc.

	"""

def CreateRootFolder(folder_name, dm_structure_xml):

	"""

	This function creates a new folder which can be then used as a DM Root.
	If a dm_structure.xml file is defined, it will be copied into that new folder.


	@folder_name string: The desired folder that will be used as a DM Root.

	@dm_structure_xml string: (optional)The source dm_structure.xml that will be copied to the new DM folder.

	@returns integer: Returns 1 on success.
	Returns  0 on failure:
	- If the new folder exists but has no write access.
	- If the new folder can't be created.
	- If the dm_structure.xml can't be copied to the new folder.

	"""

def GetAvailableLibraryItems(folder_name, search_for):

	"""

	This function can be used to get a list with all the items in a library in DM,
	e.g. all "batch_mesh_sessions" or specific "batch_mesh_sessions" that match a 
	search pattern.


	@folder_name string: The library's name.

	@search_for string: (optional)This can be a search pattern that will be used for the query.

	@returns object: Returns a list with all the library item names.

	"""

def IsConnectionValid(dm_root, reconnect):

	"""

	The function is used to check if the connection to the url-based DM root is actually valid.
	If no arguments are given, the current DM is checked.
	If a "dm_root" argument pair is given, then that url will be checked.


	@dm_root string: (optional)When this argument is given, then that url will be checked.

	@reconnect boolean: (optional)Set to True, if you automatically wish to try and reconnect if the connection is invalid.

	@returns integer: Returns 1 if the connection is valid, or 0 if it is invalid or no DM root has been defined.

	"""

def GetRoot():

	"""

	Returns the path that currently points to DM.


	@returns string: Returns a string containing the current DM root.
	A string of length 0 is returned if no DM path is currently set.

	"""

def SetRoot(dm_root, username, password, role, ticket):

	"""

	Sets the current DM root to the path DM_PATH.


	@dm_root string: A string that describes the path of the DM root directory.

	@username string: (optional)Username (For login to web based DMs).

	@password string: (optional)Password (For login to web based DMs).

	@role string: (optional)User role (For setting the user's role to web based DMs).

	@ticket string: (optional)Ticket (For login to web based DMs). This argument is provided
	when the connection should employ an already available ticket,
	and there is no need to authenticate with username / password.

	@returns integer: Returns 1 if the new DM root has been set successfully and 0 otherwise.

	"""

def RemoveRoot(dm_root):

	"""

	Removes the specified DM path or url from the "Set DM Paths" window list.


	@dm_root string: The DM path in question.

	@returns integer: Returns 1 if the specified DM root has been removed successfully and 0 otherwise.

	"""

def GetRootsList():

	"""

	Returns the whole DM Roots list, with all the info about which DM is current or 
	is enabled for "Check DM Updates".


	@returns object: Returns None in case no DM paths found or a list of dictionaries containing the information of each DM Root.
	The keys in each dictionary are shown in the following example:
	
	[{'updates_enabled': True, 'is_current': True, 'dm_root': '//mnt/DM1/'},
	 {'updates_enabled': True, 'is_current': False, 'dm_root': '//mnt/DM2/'},
	 {'updates_enabled': False, 'is_current': False, 'dm_root': 'http://dm3:8989/'}]

	"""

def GetAcceptedValuesForAttribute(type, attribute_name, return_accepted_values_from_rules):

	"""

	Given a type and an attribute's name, this function will return the accepted 
	values, as they are defined in the dm_structure.xml or hardcoded, if they exist.


	@type string: The type whose Attribute the values are requested. The specified type
	can be ANSA type (e.g. ANSA_LOADCASE) or the DM type defined
	through the Data Model (e.g. Loadcase).

	@attribute_name string: The Attribute's name. It can either be a Primary or Secondary Attribute.

	@return_accepted_values_from_rules boolean: (optional)Defines if the returned accepted values will be based on the specified rules (True) or if they will be ignored (False)
	Default value: False

	@returns object: If 'return_accepted_values_from_rules' is False, the function returns a list with the accepted values as strings, if they exist, otherwise returns an empty list.
	If 'return_accepted_values_from_rules' is True, the function returns a list [accepted_values, base_object_type, base_property_name],
	where:
	    'accepted_values' is a dictionary with keys the values of the property of the base object and values the accepted values according to the specified rules.
	    'base_object_type' is a string with the type of the base object
	    'base_property_name' is a string with the property of the base object
	If the Attribute or the Type don't exist, or if any other DM error occurs, None is returned.

	"""

def GetAttachmentAttributeValues(server_id, filename, entity_type):

	"""

	This function will collect all attributes and their values for a DM Object's attachment.


	@server_id string: The DM Object's server id.

	@filename string: The attachment's filename, relative to the DM Object.

	@entity_type string: (optional)The type of the DM Object. The specified type can be ANSA type
	(e.g. ANSA_LOADCASE) or the DM type defined through the Data
	Model (e.g. Loadcase).

	@returns object: Returns a dictionary with attribute names/values as the key/data.
	If nothing is found, None is returned.

	"""

def SetAttachmentAttributeValues(server_id, filename, entity_type, names_values):

	"""

	This function will set values for attributes for a DM Object's attachment.


	@server_id string: (optional)The DM Object's server id.
	Although it's an optional argument, it needs to be defined.

	@filename string: (optional)The attachment's filename, relative to the DM Object.

	@entity_type string: (optional)The type of the DM Object. The specified type can be ANSA type
	(e.g. ANSA_LOADCASE) or the DM type defined through the Data
	Model (e.g. Loadcase).

	@names_values object: (optional)A dictionary which holds the attributes to be set, along with their values.

	@returns integer: Returns 1 on success, or 0 on failure.

	"""

def GetAttributesFromUniqueRepresentations(server_id, type, values, ask_ansa, object_id):

	"""

	This function will return all Properties/Attributes for a specific input, 
	either server ids, a filter or a DM Browser window item.


	@server_id anything: (optional)The server id of the DM Object, or a list with server ids, if it is already known.
	Required even though it's optional.

	@type string: (optional)The type of the DM Object. The specified type can be ANSA type
	(e.g. ANSA_LOADCASE) or the DM type defined through the Data
	Model (e.g. Loadcase).

	@values object: (optional)A dictionary which holds a filter (names - values)
	that will be used when no server ids or object ids are defined.

	@ask_sdm boolean: (optional)In case of SDM CONSOLE, we can query the already downloaded values
	instead of querying DM. It should be used in cases where the query is expected 
	to be very slow.

	@object_id anything: (optional)When this function is called through an action in DM Browser or SDM CONSOLE,
	object_id is the GUI item's id, or a list with object ids. It can be used when 
	we don't know the server_id.

	@returns object: Returns a list with dictionaries, with the specified attribute values. 
	If the function fails, the list will be empty.

	"""

def GetSubHierarchyChildIds(names_values, server_id, child_server_id, hierarchy, get_group_ids):

	"""

	Use this function to get server ids for the children of a DM Object, but at an inner level in the hierarchy.


	@names_values object: (optional)A dictionary which holds the DM Object's property values
	(all property values must be present for the object's identification).

	@server_id string: (optional)The server id of the DM Object, if it is already known.
	If present, the type and names_values arguments can be omitted.

	@child_server_id string: (optional)The child server id whose subhierarchy will be searched.
	It is used along with the 'hierarchy' argument.

	@hierarchy string: (optional)The "Hierarchy" value for the child whose subhierarchy will be searched.
	It is used along with the 'child_server_id' argument.

	@get_group_ids boolean: (optional)If set to True (default), server ids for Groups will also be returned.
	Otherwise, only items that have no children will be returned.

	@returns object: Returns a list with server ids for DM Objects that exist in the subhierarchy.

	"""

def GetComponentsChildIds(server_id, get_group_ids, ask_ansa, object_id):

	"""

	Use this function to get server ids for the children of a DM Object.


	@server_id string: (optional)The DM Object's server id.
	Required even though it's optional.

	@get_group_ids boolean: (optional)When this is True (default), server ids for Groups will also be returned.
	Otherwise, only items that have no children will be returned.

	@ask_sdm boolean: (optional)In case of SDM CONSOLE, we can query the already downloaded values 
	instead of querying DM. It should be used in cases where the query is expected to be very slow.

	@object_id integer: (optional)When this function is called through an action in DM Browser or SDM CONSOLE,
	object_id is the GUI item's id. It can be used when
	we don't know the server_id.

	@returns object: A list with server ids for DM Objects that exist in the hierarchy.

	"""

def AddFile(file_name, type, attributes, server_id, dm_root, target_dm_root, add_attachments, add_children):

	"""

	Adds a file in the current or target DM.


	@file_name string: (optional)The file path of the file to be added in DM.

	@type string: (optional)Accepted values: 'parts', 'includes', 'Subsystems'.
	For parts an .ansa file must be provided.

	@attributes object: (optional)A dictionary with the key DM attributes of the file. 
	The module id, version, study version and representation
	must be provided. The names of the attributes must be 
	provided as they appear in Model Browser and DM Browser.

	@server_id string: (optional)Instead of the file, a server id from a source dm root can be provided as source.
	file_name and server_id are mutually exclusive arguments.

	@dm_root string: (optional)The  dm root server_id refers to. if not provided, the current dm is assumed.
	This option is used only if server_id is provided.

	@target_dm_root string: (optional)The dm root where the file will be added. If not provided, the current dm root 
	is assumed. This option is used only if server_id is provided.

	@add_attachments boolean: (optional)Default: false. If true, any attachments of the server_id will also be added in dm.
	This option is used only if server_id is provided.

	@add_children boolean: (optional)This option is used only if the server_id of a Subsystem is provided.
	If True: the parts of the subsystem will also be added in target dm.
	(Default: False)

	@returns integer: The function returns an integer:
	        0: Success.
	        1: Add in DM failed.
	        2: Invalid dm root.
	        3: Invalid input type.
	        4: Incomplete input dictionary.
	        5: Conflict between the input dictionary and the values in the provided file.
	        6: The file has not been produced with Save Representation.

	"""

def ExecuteSimManagerQuery(query_string, dm_root, progress_bar):

	"""

	Runs a query using the SimManager's REST API functionality.
	It is about requesting data for a set of objects. 


	@query_string string: type=[OT]&expr=[EL]&view=[VIEW1]&view=[VIEW2]&pageSize=[SIZE]&page=[PAGE]
	oid=[OID]&expr=[EL]
	query=[QUERY_SPEC]
	query=[QUERY_SPEC]&f=[EL1]&f=[EL2]
	
	type: Object type, Is the type of the objects on which the expression is evaluated 
	      (optional, but either type, oid, or query are required).	
	expr: EL expression, Is an EL expression being evaluated on the object type.
	      It's optional. If missing, "this" is assumed. The expression can be a filter
	      (e.g. [name == 'ABC*'], or a navigation expression (e.g. results.keyResults), 
	      or any combination of both. Sorting is also supported.	
	view: View, Is the name of a view. It defines the fields being returned for each 
	      object. If multiple views are specified, then fields of the first valid view in 
	      the list will be returned. It's optional. If missing, "Default" is assumed.	
	pageSize: Integer, Defines the maximum number of objects to be returned.
	          It's optional. If missing, "100" is assumed.
	page: Integer, Defines the which page of the data is returned if there are more 
	      than SIZE objects. It's optional. If missing, "1" is assumed.		
	oid: Object id, Is the ID of an object (id:tid). It can be used instead of an object 
	     type as a starting point. Then the expression will be evaluated in this object.
	query: Query, A serialized query definition 
	       (optional, but either type, oid, or query are required).
	f: EL expression, Instead of providing the name of a view, fields can be specified 
	   defining a new "view". Those fields could be any kind of EL expression.

	@dm_root string: (optional)The target DM root(URL). If not provided, the current DM is assumed.

	@progress_bar object: (optional)The progress can be shown in a BCProgressBar,
	created with guitk.BCProgressBarCreate.

	@returns object: Returns a list of dictionaries, with name/value pairs.

	"""

def LaunchSimManagerAction(action_name, arguments, dm_root, return_process_id, progress_bar):

	"""

	Launches an Action in SimManager, using the REST API functionality.


	@action_name string: The Action's name, e.g. "Search".

	@arguments object: A dictionary with the Action's parameters.
	The values need to be percent encoded.

	@dm_root string: (optional)The target DM root(URL). If not provided, the current DM is assumed.

	@return_process_id boolean: (optional)In case you need the process id returned, this argument should be set to True.

	@progress_bar object: (optional)The progress can be shown in a BCProgressBar,
	created with guitk.BCProgressBarCreate.

	@returns anything: If the Action runs successfully, True is returned.
	Otherwise, False is returned.
	If the argument return_process_id=True, the process id is returned. If it fails, 
	None will be returned.

	"""

def GetConnectedUsername(dm_root):

	"""

	The function is used to return the username that was used to connect to the url-based DM.
	If no arguments are given, the current DM is checked.
	If a "dm_root" argument pair is given, then that url will be checked.


	@dm_root string: (optional)When this argument is given, then that url will be checked.

	@returns string: Returns the Username.
	If something goes wrong, None will be returned.

	"""

def GetLogFileText():

	"""

	This function assembles logging data from the current My_DM.log file, as well
	as the previously rotated, compressed archives and returns it as a single
	string.
	
	When the lock cannot be acquired, a Runtime exception is thrown. The reason may
	be a transient failure (other operations are running which need to lock the log
	file), or a stale lock file. Stale lock files may be remnants of abnormally
	terminated processes, whose locks have not expired yet.


	@returns string: Returns a string holding all My_DM.log data.

	"""

def GetLibraryItemAttributeValues(library, filename):

	"""

	This function will collect all attributes and their values for a library item File.
	It needs to be a generic Library Item file.


	@library string: The library's name, e.g. "batch_mesh_sessions".

	@filename string: The file's filename, relative to the library, e.g. "test1/test2/file.txt".

	@returns object: Returns a dictionary with attribute names/values as the key/data.
	If nothing is found, an empty dictionary is returned.

	"""

def PrintToLogFile(text, with_timestamp):

	"""

	Prints a line of text to My_DM.log. 
	
	If 'with_timestamp' is set to 'True', additional timestamp and user data are printed along with 'text'.
	If 'with_timestamp' is set to 'False', only 'text' is printed.


	@text string: The line of text to be printed in the My_DM.log.

	@with_timestamp boolean: (optional)Determines wether to print additional timestamp and user data along with 'text'.
	(Default: True)

	"""

def ClearLogFile(clear_archived_files):

	"""

	Clears the contents of the My_DM.log.
	
	If 'clear_archived_files' is set to True, archived log files (if any) are also deleted.
	If 'clear_archived_files' is set to False, only the contents of the current log file are cleared.
	By default, 'clear_archived_files' is True.


	@clear_archived_files boolean: (optional)Determines wether to clear the archived DM log files along with the current.
	(Default: True)

	@returns boolean: Returns:
	True: If both the current log file and the archived were successfully cleared.
	False: If any of the log files failed to be cleared.

	"""

def GetDMTypeAttributes(type):

	"""

	Gets the secondary attributes of a particular DM object type  
	(e.g. part, include etc.)


	@type string: The type of the DM Object. The specified type can be ANSA type
	(e.g. ANSA_LOADCASE) or the DM type defined through the Data
	Model (e.g. Loadcase).
	
	In case of file-based DM with no dm_structure.xml, 
	the accepted values for the argument "type" are:
	"parts", "includes", "configurations", "subsystems",
	"simulation_model", "simulation_run", "report",
	"session", "loadcase", "dm_library_item"

	@returns object: Returns a list of secondary attributes. Each secondary attribute in the list 
	is a dictionary of key:value (strings) pairs for all the supported attribute 
	member properties:
	
	'name': the name of the attribute
	'type': the type of the attribute
	'format': the max number of digits allowed by the attribute format, as a string
	'prefix': the prefix for the attribute value
	'default_value': the default value of the attribute
	'accepted_values': a comma seperated list of the attribute's accepted values 
	'colors_for_accepted_values': a comma seperated list of accepted values colors
	'allow_null': 'YES'/'NO', whether the attribute accepts empty (null) values
	'read_only': 'YES'/'NO', whether the attribute is ReadOnly

	"""

def GetDMTypeProperties(type):

	"""

	Gets the properties (primary attributes) of a particular DM object type 
	(e.g. part, include etc.)


	@type string: The type of the DM Object. The specified type can be ANSA type
	(e.g. ANSA_LOADCASE) or the DM type defined through the Data
	Model (e.g. Loadcase).
	
	In case of file-based DM with no dm_structure.xml, 
	the accepted values for the argument "type" are:
	"parts", "includes", "configurations", "subsystems",
	"simulation_model", "simulation_run", "report",
	"session", "loadcase", "dm_library_item"

	@returns object: Returns a list of properties. Each property in the list is a dictionary of 
	key:value (strings) pairs for all the supported property member attributes:
	
	'name': the name of the property
	'type': the type of the property
	'format': the max number of digits allowed by the property format, as a string
	'prefix': the prefix for the property value
	'default_value': the default value of the property
	'accepted_values': a comma seperated list of the property's accepted values 
	'colors_for_accepted_values': a comma seperated list of accepted values colors
	'allow_null': 'YES'/'NO', whether the property accepts empty (null) values
	'read_only': 'YES'/'NO', whether the property is ReadOnly

	"""

def OpenDMObjectsInNewTab(server_ids, entities, type, view, dm_system, tab_name, expand_all, open_in_viewer, open_in_reports_table):

	"""

	This function can be used to open one or more hierarchies of any DM Object type,
	in a new tab, in DM Browser or KOMVOS.


	@server_ids object: (optional)A list with DM Object server ids.

	@entities object: (optional)A list with ANSA entities.

	@type string: (optional)The type of the DM Object. The specified type can be ANSA type
	(e.g. ANSA_LOADCASE) or the DM type defined through the Data
	Model (e.g. Loadcase).

	@view string: (optional)The new Tab's view, e.g. "Default", "Flat" or a user defined in the dm_views.xml.
	When undefined, the function will return False.

	@dm_system string: (optional)The DM root that will be queried.

	@tab_name string: (optional)The new tab will be given this name.

	@expand_all boolean: (optional)If set to True, all items in the new tab will be expanded.

	@open_in_viewer boolean: (optional)If set to True, all items in the new tab will be loaded to the meta viewer.

	@open_in_reports_table boolean: (optional)If set to True, Reports Table will also be launched for all  the items in the
	new tab that is opened. In case the requested Type is not supported in
	Reports Table (SimulationModel, LoadCase, SimulationRun) or no Reports
	are found in DM for the requested server_ids, the scipt function will just 
	open the server_ids in a new tab and no Reports Table tabs will be opened.

	@returns boolean: Returns True if the tab is opened succesfully, otherwise False.

	"""

def ExportFileFromSimManager(server_id, expr, extension, dm_root, progress_bar):

	"""

	Exports a file using the SimManager's REST API functionality.
	This is about exporting files from the vault.
	The server transfers the file in its original format and will supply 
	a MIME type based on the extension of the file name.


	@server_id string: Is the ID of an object (id:tid). It can be used instead of an object type as a starting point. Then the expression will be evaluated in this object.

	@expr string: Is the EL epxression leading from the given object to the file to be transfered. Care has to be taken that only one file is referenced, e.g. files.model, file.pom_ExportedData.

	@extension string: The extension that will be added to the downloaded file.
	SimManager will not add any extension, therefore it's up to the user to define it.

	@dm_root string: (optional)The target DM root(URL). If not provided, the current DM is assumed.

	@progress_bar object: (optional)The progress can be shown in a BCProgressBar,
	created with guitk.BCProgressBarCreate.

	@returns string: Returns the exported filename, usually in a temporary location.
	Returns None in case of failure.

	"""

def GetLibraryItemTypes(dm_root):

	"""

	This function returns a list containing the names of all the Rich Library Item
	types that can exist for the DM.


	@dm_root string: (optional)When this argument is given, then that DM will be used.
	Otherwise, the current DM root is used.

	@returns object: Returns a list containing strings.
	An empty list is returned if no Rich Library Item types are defined.
	If something goes wrong, None is returned.

	"""

def GetObjectHierarchyIds(server_id):

	"""

	This function provides hierarchy related information for all directly contained
	DM objects. With 'directly contained', it is meant that a single query on the
	Server ID provided as argument will only be done. No recursive, follow-up
	queries on children objects will be done, in order to check whether they 
	contain children of their own.
	
	For example, when a Simulation Model gets queried with this function, all 
	contained Subsystems will be returned only, without any information about 
	possible groups or parts within the subsystems.
	
	On the other hand, when a Subsystem gets queried, all contained groups / parts
	will be returned (which may form arbitrary subhierarchies).


	@server_id string: The DM Object's server id.

	@returns object: This function returns a list of tuples. For each contained DM object, a tuple of
	the form (server_id, parent_server_id) is to be found in the list.

	"""

def RunDMSession(server_id, session_id):

	"""

	Run a DM Session on a certain DM server id


	@server_id string: The server id on which the session will run

	@session_id string: The id of the session

	"""

def HasAttributeConditionRule(type, attribute_name):

	"""

	Given a type and an attribute's name, this function will check whether a condition rule is defined.


	@type string: The type of the DM Object. The specified type can be ANSA type
	(e.g. ANSA_LOADCASE) or the DM type defined through the Data
	Model (e.g. Loadcase).

	@attribute_name string: The Attribute's name. It can either be a Primary or Secondary Attribute.

	@returns boolean: Returns True if the attribute has a condition rule. Otherwise, it returns False.

	"""

def IsAttributeRuleGenerated(type, attribute_name):

	"""

	Given a type and an attribute's name, this function will check whether the value of this attribue is auto-generated by a rule.


	@type string: The type of the DM Object. The specified type can be ANSA type
	(e.g. ANSA_LOADCASE) or the DM type defined through the Data
	Model (e.g. Loadcase).

	@attribute_name string: The Attribute's name. It can either be a Primary or Secondary Attribute.

	@returns boolean: Returns True if the attribute value is auto-generated by a rule. Otherwise, it returns False.

	"""

def GetAttributeValueFromGenerationRule(type, attribute_name, attribute_values):

	"""

	Given a type, an attribute's name and the attribute values, this function will 
	return the generated value that is defined by the rule in the dm_structure.xml.


	@type string: The type whose Attribute the value is requested. The specified type can be ANSA type (e.g. ANSA_LOADCASE) or the DM type defined through the Data Model (e.g. Loadcase).

	@attribute_name string: The Attribute' s name. It can either be a Primary or Secondary Attribute.

	@attribute_values object: A dictionary containing the attribute name-values dictionary per attribute type that determine the value of the input attribute. e.g. {'Parts' : {'Name': 'my_name', 'Module Id':''001'}, 'Subsystems : {'Name':'subsystem_name', 'Version':A}}

	@returns string: The generated attribute value.
	If the attribute is not rule generated it will return None.
	If not all required attribute values are given in 'attribute_values' the default values will be selected.
	If the argument 'attribute_values' is not a dict with dicts as value it will return None.

	"""

def ShowDMPathsWindow():

	"""

	Shows the "Set DM Paths" window.


	@returns string: Returns a string containing the current DM root if it succeeds.
	Returns None in case of "Cancel" or failure to add a DM.

	"""

def GetAttributeGenerationRule(type, attribute_name):

	"""

	Given a type and an attribute's name, this function will return the generation
	rule, if exists.


	@type string: The type whose Attribute the generation rule is requested. The specified type
	can be ANSA type (e.g. ANSA_LOADCASE) or the DM type defined
	through the Data Model (e.g. Loadcase).

	@attribute_name string: The Attribute's name. It can either be a Primary or Secondary Attribute.

	@returns object: A dictionary with key the attribute type and value a list of the attribute names 
	that determine the value of the input attribute.
	e.g. {'Subsystems': ['Module Id', 'Version', 'Study Version']}
	If the attribute is not rule generated, it will return None.

	"""

def ExportDMStructureXml(filename):

	"""

	Exports the current Data Model to an XML file in the user defined directory. 


	@filename string: (optional)The full path directory (including the filename) where the XML file will be exported.
	If filename is not defined the XML file will replace the dm_structure.xml of the current DM.

	@returns boolean: Funtion returns a boolean  defining the result of the function.

	"""

def SetAcceptedValuesForAttribute(type, attr_name, accepted_values):

	"""

	Changes the Accepted Values of an Attribute if the Type of that specific Attribute allows it.


	@type string: The name of the object that contains the Attribute whose Accepted Values will change.

	@attr_name string: The name of the Attribute whose Accepted Values will change.

	@accepted_values string: The Accepted values that will be applied to the Attribute.

	@returns boolean: Function returns a boolean variable defining the result of the function.

	"""

def SetDefaultValueForAttribute(type, attr_name, default_value):

	"""

	Changes the Default Value of an Attribute if the Type of that specific Attribute allows it.


	@type string: The name of the object that contains the Attribute whose Default Value will change.

	@attr_name string: The name of the Attribute whose Default Value will change.

	@default_value string: The Default Value that will be applied to the Attribute.

	@returns boolean: Function returns a boolean variable defining the result of the function.

	"""

def GetDefaultValueForAttribute(type, attr_name):

	"""

	Returns the current Default Value of an Attribute.


	@type string: The name of the object that contains the Attribute whose Default Value will be returned.

	@attr_name string: The name of the Attribute whose Default Value will be returned.

	@returns string: Function returns a string with the Default Value of the Attribute contained in the Object Type.

	"""

def CreateGenerationRule(type, rule_name, disc_chars, generated_value, rejected_characters):

	"""

	This function is used in order to create a new Generation Rule for the current DM.


	@type string: The name of the object that will contain the created Generation Rule.

	@rule_name string: The name of the Generation Rule that will be created.

	@disc_chars string: (optional)The Discarded values of the Generation Rule.

	@generated_value string: (optional)The Generated Value of the Generation Rule.

	@rejected_characters string: (optional)The discarded characters of the Generation Rule.

	@returns boolean: Function returns a boolean variable defining the result of the function.

	"""

def DeleteGenerationRule(type, rule_name):

	"""

	This function is used in order to delete a Generation Rule for the current DM.


	@type string: The name of the object that contains the Generation Rule about to be deleted.

	@rule_name string: The name of the Generation Rule that will be deleted.

	@returns boolean: Function returns a boolean variable defining the result of the function.

	"""

def GetGeneratedValueOfGenerationRule(type, rule_name):

	"""

	Returns the current Generated Value of a Generated Rule.


	@type string: The name of the object that contains the Generation Rule.

	@rule_name string: The name of the Generation Rule whose Generated Value will be returned.

	@returns string: Function returns a string with the Generated Value of the Generation Rule contained in the Object Type.

	"""

def SetGeneratedValueOfGenerationRule(type, rule_name, generated_value):

	"""

	Using this function you can change the Generated Value of an existing Generation Rule.


	@type string: The name of the object that contains the Generation Rule.

	@rule_name string: The name of the Generation Rule whose Generated Value will be modified.

	@generated_value string: The new Generated Value of the Generation Rule.

	@returns boolean: Function returns a boolean variable defining the result of the function.

	"""

def CreateConditionRule(type, rule_name, generator_name, generator_value, accepted_values):

	"""

	This function is used in order to create a new Condition Rule for the current DM.


	@type string: The name of the object that will contain the created Condition Rule.

	@rule_name string: The name of the Condition Rule that will be created.

	@generator_name string: The Generator Name of the Condition Rule.

	@generator_value string: (optional)The Generator Value of the Condition Rule.

	@accepted_values string: (optional)The Accepted Values of the Condiition Rule.

	@returns boolean: Function returns a boolean variable defining the result of the function.

	"""

def DeleteConditionRule(type, rule_name, generator_value):

	"""

	This function is used in order to delete a Condition Rule for the current DM.


	@type string: The name of the object that contains the Condition Rule about to be deleted.

	@rule_name string: The name of the Condition Rule that will be deleted.

	@generator_value string: The Generator Value of the Condition Rule.

	@returns boolean: Function returns a boolean variable defining the result of the function.

	"""

def GetGeneratorValuesOfConditionRules(type, rule_name):

	"""

	This function returns all the Generator Values used by a specific rule name.
	Multiple Condition Rules can have the same rule and generator name but different generator values.


	@type string: The type of the object that will contain Condition Rules.

	@rule_name string: The name of the Condition Rules that contain the Generator Values.

	@returns object: Returns a list of strings with the generator values of the specific Condition Rule contained in the specific Object Type

	"""

def SetGeneratorValueOfConditionRule(type, rule_name, old_generator_value, generator_value):

	"""

	This Function is used in order to change the Generator Value of a specific Condition Rule.


	@type string: The type of the object that contains the Condition Rule about to be modified.

	@rule_name string: The name of the Condition Rule that will be modified.

	@old_generator_value string: The old value of the Generator Value. This value is needed because multiple Condition Rules can have the same rule name.

	@generator_value string: The new value of the Generator Value.

	@returns boolean: Function returns a boolean variable defining the result of the function.

	"""

def QueryDMObjects(query, type):

	"""

	Search in DM for objects which satisfy the specified query.


	@query object: The query can be expressed in two forms:
	* A list of [<attribute_name>, <condition>, <value>] lists which
	  specify the query. For Attributes of Versioning Scheme Counter
	  type (e.g. Team Version, Study Version, etc.) the "Latest"
	  keyword is supported as follows:
	  [<versioning_attribute_name>, "equals", "Latest"]
	* A BetaQL string

	@type string: The type of the DM Object. The specified type can be ANSA type
	(e.g. ANSA_LOADCASE) or the DM type defined through the Data
	Model (e.g. Loadcase).

	@returns object: Returns a dictionary with the following keys and values:
	key = 'error'
	value = 0(Success), 1(Nothing found), 2(No DM Root was set), 3(No access to DM Root),
	        4(Error in filters)
	key = 'output'
	value = A list with the DM objects which satisfy the query.

	"""

def UploadFileToSimManagerVault(file_path, sim_activity_name, file_param_name, object_type, progress_bar):

	"""

	Uploads a file to the SimManager vault and retrieves the vault id.


	@file_path string: The file that will be uploaded to SimManager.

	@sim_activity_name string: The activity's name is needed for SimManager 2014.

	@file_param_name string: The name of the FILE parameter in the SimActivity.

	@object_type string: The object type of the object to which the file will be attached. 
	If there is no target object type, use "Project".

	@progress_bar object: (optional)The progress can be shown in a BCProgressBar,
	created with guitk.BCProgressBarCreate.

	@returns string: If the file is successfully added, the vault id will be returned.
	Returns None in case of failure.

	"""

def GetObjectTypeFromAnsaKeyword(keyword, dm_root):

	"""

	This function returns the DM object type of dm_root that corresponds to the input ANSA keyword.
	If dm_root is not defined, the current DM root is used.


	@keyword string: The input ANSA keyword.

	@dm_root string: (optional)When this argument is given, then that DM will be used.
	Otherwise, the current DM root is used.

	@returns string: Returns the DM object type. If no object type is found, it returns None.

	"""

def GetAnsaKeywordFromObjectType(type, dm_root):

	"""

	This function returns the ANSA keyword that corresponds to the input DM object type of dm_root.
	If dm_root is not defined, the current DM root is used.


	@type string: The input DM object type.

	@dm_root string: (optional)When this argument is given, then that DM will be used.
	Otherwise, the current DM root is used.

	@returns string: Returns the ANSA keyword. If no ANSA keyword is found, it returns None.

	"""

def GetDMReferences(server_id, ref_server_id, ref_type):

	"""

	This function queries the DM for all references that satisfy certain criteria.
	Each of the 3 optional arguments provides a filtering criterion:
	* server_id
	  Server ID of the object doing the referring (reference source). This argument
	  defines the object that is using some other objects.
	* ref_server_id
	  Server ID of the object being referred-to (reference target). This argument
	  defines the object that is being used by some other objects.
	* ref_type
	  Reference type
	  
	When multiple arguments are provided, then the corresponding criteria are 
	combined with an AND logical operator.


	@server_id string: (optional)When present, the DM References query will
	search for references that originate from
	the object with this specific Server ID
	(Object is user)

	@ref_server_id string: (optional)When present, the DM References query will
	search for references that point to the
	object with this specific Server ID.
	(Object is being used)

	@ref_type string: (optional)When present, the DM References query will
	search for references of the specific type.

	@returns object: Returns the list of DMReferences that satisfy the provided criteria

	"""

def RemoveDMReference(reference):

	"""

	This function deletes a Reference from the DM


	@reference object: DMReference object, describing the reference to be removed

	@returns boolean: Returns True when the removal operation was successful, regardless of whether an
	actual reference existed / got deleted from the DM or not. It is certain though
	that such a reference no longer exists.

	"""

def AddClusterMember(path, nickname):

	"""

	This function inserts a new, read only member into the currently configured
	Cluster DM.


	@path string: DM Root of the DM that will be backing the new
	cluster member.

	@nickname string: (optional)String to be used as nickname for the new
	cluster member. May contain the latin letters, 
	digits, the underscore and dash characters.
	If this argument is not provided, the new
	cluster member's nickname will be auto generated
	from the path argument.

	@returns boolean: Returns True if the new member was successfully admitted into the cluster.

	"""

def GetClusterMembers():

	"""

	This function fetches information about all the cluster members existing in the
	currently configured Cluster DM.


	@returns object: Returns all cluster members as a list of DMClusterMember objects.

	"""

def RemoveClusterMember(path):

	"""

	This function removes an existing, read only member from the currently 
	configured Cluster DM, provided that there are no cluster level dependencies on
	it.


	@path string: DM Root of the cluster member to be removed.

	@returns boolean: Returns True if the member was successfully removed from the cluster.

	"""

def GetConnectedUserRole():

	"""

	Get the current role of the user who is connected to SPDRM-based DM root.


	@returns string: Returns the User Role.
	None is returned in case of error (e.g. the user is not connected to DM root).

	"""

def GetUserRoles(dm_root, username, password):

	"""

	Get the available roles of a user in an SPDRM-based DM root.


	@dm_root string: The url of the SPDRM-based DM root.

	@username string: The username of the user.

	@password string: The password of the user.

	@returns object: Returns a list with the available user roles.
	None is returned in case of error.

	"""

def InitializeDMForDOE(dm_root):

	"""

	This function initializes the Filebased DM with the necessary Properties
	and Attributes for use with DOE.
	It will only update the DM when it's empty.


	@dm_root string: (optional)The function works on the current DM, unless this
	argument is specified.

	@returns boolean: False when the DM isn't empty.
	True if the DM is empty and the initialization is successful.

	"""

def GetTicket(dm_root):

	"""

	This function returns the authentication ticket that is currently being used in
	a connection to a remote, web based DM (SPDRM or SimManager).


	@dm_root string: (optional)The URL of the remote, web based DM. If this argument
	is not provided, the Current DM Root will be used.

	@returns string: Returns the authentication ticket as a string.

	"""

def GetFeatureItemTypes(dm_root):

	"""

	This function returns a list containing the names of all the Feature Item types
	that can exist for the DM.


	@dm_root string: (optional)When this argument is given, then that DM will 
	be used. Otherwise, the current DM root is used.

	@returns object: Returns a list containing strings.
	An empty list is returned if no Feature Item types are defined.
	If an error occurs, None is returned.

	"""

def GetMultiDMReferences(server_ids, ref_types, recursive, returned_ents):

	"""

	This function queries the DM for all references that involve multiple Server IDs
	and for possibly multiple reference types. The query can be recursive and it is
	user selectable whether the query should search for the objects being used or
	are using the Server IDs provided as arguments


	@server_ids object: Sequence of strings, holding the Server IDs for
	which references will be queried.

	@ref_types object: (optional)Sequence of strings, holding the Reference Types
	for which reference will be queried. If empty, 
	then all types of references will be returned.
	Default value: Empty list

	@recursive boolean: (optional)This value defines whether references should be
	recursively queried, using the provided server ids
	as starting points.
	Default value: False

	@returned_ents integer: (optional)This value defines whether references originating
	from or terminating into the provided Server IDs
	should be queried.
	Default value: dm.constants.DM_REF_FROM

	@returns object: Returns the list of DMReferences that satisfy the provided criteria

	"""

def RebuildFromDisk(dm_root):

	"""

	The DM's database file is updated by scanning the DM directory contents.


	@dm_root string: (optional)The function works on the current DM, unless this
	argument is specified.

	@returns boolean: False when the DM isn't Filebased.
	True if the DM is Filebased.

	"""

def IsIntermodularConnectivityLinksFeatureSupported():

	"""

	The function is used to check if intermodular_connectivity_links 
	feature is supported by current DM schema.


	@returns boolean: Returns True if feature is supported, or False if not supported.

	"""

class DMObject():

	"""

	A class that handles communication with DM and functionality regarding Objects in DM.

	"""


	names_values = None
	"""
	A dictionary with DM Properties that completely defines the Object.
	It needs the Object type as well.

	"""

	type = None
	"""
	The type of the DM Object. The specified type can be ANSA type
	(e.g. ANSA_LOADCASE) or the DM type defined through the Data
	Model (e.g. Loadcase). Required when creating an Object with
	specified "names_values".

	"""

	server_id = None
	"""
	The Object's server id, its unique id in DM.
	If the value is empty, should the script ask for it, the DM will be queried for the 
	"names_values" and retrieve the value.

	"""

	ghost_id = None
	"""
	When an Object is partially deleted, the server_id is None
	and the ghost_id has the Id.
	The ghost_id can be used to create a new DMObject and get
	conflict options for saving it in DM.
	When the Object doesn't exist, both the server_id and 
	ghost_id are None.
	When the Object exists, the ghost_id will be equal to
	the server_id.

	"""

	def export(output_directory, export_type, child_server_id, hierarchy):

		"""

		Download the Object's Representation File or hierarchy to a XML file.


		@output_directory string: Specify where the file/files will be downloaded.

		@export_type string: (optional)Accepted values: "hierarchy", "sub_hierarchy", blank.
		When this argument is omitted, the Representation File(s) 
		will be exported.
		When the argument is "hierarchy", an XML file with the Object's 
		hierarchy will be exported.
		When the argument is "sub_hierarchy", an XML file with 
		a subhierarchy will be exported.
		It is used along with the "child_server_id" and "hierarchy" 
		arguments.

		@child_server_id string: (optional)The child server id whose subhierarchy will be exported.
		It is used along with the 'hierarchy' argument.

		@hierarchy string: (optional)The "Hierarchy" value for the child whose subhierarchy will be 
		exported. It is used along with the 'child_server_id' argument.

		@returns string: The resulting directory is returned on success.

		"""


	def remove(only_representation_file):

		"""

		Delete the Object from DM.


		@only_representation_file string: (optional)Use "YES" when only the Representation File should be 
		deleted and the Object should be kept in the database.

		@returns integer: 1 if the function was successful.0 for failure.

		"""


	def set_attribute_values(attributes_values, attributes_types):

		"""

		This function can change Attribute values for the Object.


		@attributes_values object: A dictionary which specifies the Attributes to change, 
		in a names-values format.

		@attributes_types object: (optional)A dictionary mapping attribute names to types. This
		information will be used in case new attributes will be
		created and the DM supports typed attributes.

		@returns boolean: True : If the at least one values was set successfully.False: If the function failed to set any value.

		"""


	def get_attribute_values(attributes):

		"""

		This function can return some specified Attribute values of a Object.


		@attributes object: (optional)A list in which the user can specify Attribute names, 
		for their values to be returned. If this arguments is not 
		present, all the object's values will be returned.

		@returns object: If the object was found, a dictionary will be returned with the specified attribute values.If the function fails, "None" will be returned.

		"""


	def get_all_values():

		"""

		This function will return all the Properties and Attributes for the Object in the form of a dictionary.


		@returns object: A list with a dictionary for the Object that is actually found in DM.

		"""


	def connect(references):

		"""

		This function connects DM Objects, by referencing. After its execution,the Object will reference the Objects specified in the "references" dict.


		@references object: A dictionary which holds server_id->reference-type pairs.
		Please see the REMARKS section for more information on the "reference_type" accepted values.

		@returns boolean: True : If the new references were made successfully.False: If the function failed to make one of the connections.

		"""


	def add_new(overwrite, link, get_repr_file_siblings, filename, spin_up_attribute):

		"""

		This function adds an Object to DM, if it does not already exist.


		@overwrite boolean: (optional)Set to True if the object should be overwritten if it
		already exists in the DM. (Default: False)

		@link boolean: (optional)Set to True if you wish create a link to the file that 
		corresponds to the object. (Default: False)

		@get_repr_file_siblings boolean: (optional)Set to True if you wish to copy along all files that exist
		in the same directory as the representation file.
		Applicable for Subsystems, Simulation Models, Load 
		Cases and Simulation Runs, when a non-ANSA file
		is set as representation file.
		(Default: False)

		@filename string: (optional)When the data model doesn't specify a "File" Property/Attribute for the Object, a Representation File can be added using this argument.
		For example, when adding a Subsystem to a Filebased DM, the file will be stored in DM by adding a filename to this method.

		@spin_up_attribute string: (optional)The primary attribute to spin-up. The 'overwrite' attribute should be set to False. By default, the 'spin_up_attribute' is not specified and the 'overwrite' = False, which means that the process will be skipped if the object already exists in DM.

		@returns object: None: If an error occured.server_id string: If the object was successfully saved.

		"""


	def get_representation_file():

		"""

		This function will return the absolute file path to the DMObject's Representation File. In case of a server-based DM, e.g. SPDRM, SimManager,the file will be downloaded locally, to a temporary location, only the first time it is asked for. All following calls to the function will return the same file path, so long as the DMObject isn't updated. The temporary files deletion is handled automatically.


		@returns string: If the Representation File exists and is successfully found, it's absolute file path will be returned.Otherwise, "None" will be returned.

		"""


	def get_conflict_options():

		"""

		When trying to upload an object to DM, one can get the conflict options when the object already exists in DM.


		@returns object: Returns a list with the available conflict options, only if the object already exists in DM.Otherwise, it returns None.

		"""


	def get_contained_objects(type):

		"""

		This function will query DM and collect all Objects of the specified type contained under this DM Object.


		@type string: The type of the DM Object that will be queried for. The specified type can be ANSA type (e.g. ANSA_LOADCASE) or the DM type defined through the Data Model (e.g. Loadcase).

		@returns object: Return a list of DMObject objects.

		"""


	def set_contents(server_ids):

		"""

		This function sets the contents of the object (e.g. the Subsytems belonging to a Simulation Model).


		@server_ids object: The server ids identifying the objects to be set as contents.

		@returns boolean: True : If the object contents were set successfully. False : If the object contents couldn't be set.

		"""


	def get_contents():

		"""

		Get the list of objects that are contents of the object


		@returns object: Returns the server ids of the object contents

		"""


	def get_references(returned_ents):

		"""

		Get the objects which:- use this DM Object,- are used by this DM Object,- use and are used by this DM Object.


		@returned_ents integer: (optional)define the requested objects:
		0 to get the objects which use this DM Object,
		1 to get the objects which are used by this DM Object,
		2 to get the objects which use and are used by this DM Object.
		By default, the objects, which use this DM Object, are returned.

		@returns object: Returns a list with the requested objects.

		"""


	def get_type():

		"""

		Use this method to query DM for the DMObject's type.


		"""


	def download_attachment(output_folder, folder_name, subfolder_name, filename, attribute_name):

		"""

		Downloads an attached file/folder of the DMObject.


		@output_folder string: the full path of the folder where the attachment will be downloaded.

		@folder_name string: (optional)the name of the folder which contains the attachment.

		@subfolder_name string: (optional)the name of the sub-folder to be downloaded.

		@filename string: (optional)the name of the file to be downloaded.

		@attribute_name string: (optional)the name of attribute which contains the attachment.

		@returns string: Returns the full path of the downloaded attachment on success and None on failure.

		"""


	def get_attachment_values():

		"""

		In case of Filebased DMs, this function returns absolute paths for attachments that aren't declared in the data model and will not be returned by dm.DMObject.get_all_values. In case of SPDRM, this function may return absolute or relative paths for these attachments, depending on SPDRM configuration.


		@returns object: Returns a dictionary with the attribute name as the key and the absolute file path as the value.

		"""

class DMReference():

	"""

	DM objects can refer to other objects within the same DM. Such relationships are
	described by 3 data fields:
	* DM Object that is doing the referring, i.e. is using another object
	* DM Object that is being referred to, i.e. is being used by another object
	* Reference type
	
	Instances of the DMReference class encapsulate all information needed to 
	describe such a reference between DM Objects.
	
	Based on the reference type, references can be classified as strong / weak:
	Objects cannot be deleted if there are any outstanding strong references
	pointing to them. Weak references on the other hand do not obstruct the deletion
	of the referred-to objects.
	
	Even though the reference type can be any arbitrary string, there are predefined
	reference types accomodating standard use cases. The predefined reference types
	are:
	* adaptation
	  Used for adapted DM objects to point to their standalone counterparts (e.g.
	  LoadCases) (strong)
	* creation
	  Used for DM objects to point to the DM object that triggered their creation
	  (e.g. Reports pointing to the META Session) (strong)
	* history
	  Used to show how objects have evolved over time and track their origins:
	  recent objects point to their immediate ancestors (weak)
	* repr_derivation
	  Used for automatically saved FE representation objects to point to the
	  original ANSA representation objects (weak)
	* changeset
	  Used for connecting an object in the DM, with the changeset that ordered its
	  creation (strong)
	* training
	  Used to show how data were used in ML training sessions: the generated 
	  predictor object points to the Simulation Run objects used during training
	  (weak)
	* modular_environment_profile
	  Used to show what configuration was used during the save of an object (strong)
	* strong
	  Generic strong reference. Recommended for user created references
	* weak
	  Generic weak reference. Recommended for user created references

	"""


	server_id = None
	"""
	Server ID of the object that is doing the referring,
	i.e. using the other object.

	"""

	ref_server_id = None
	"""
	Server ID of the object that is being referred to
	i.e. is being used by the other object.

	"""

	ref_type = None
	"""
	Field describing the type of the reference

	"""

	def __init__(server_id, ref_server_id, ref_type):

		"""

		DMReference object constructor, initializing all members


		@server_id string: See respective member definition

		@ref_server_id string: See respective member definition

		@ref_type string: See respective member definition

		@returns object: Returns the created DMReference object

		"""

class DMClusterMember():

	"""

	DMClusterMember objects describe a DM Cluster membership, providing information
	on which the backing DMs are and how they are employed within the cluster.

	"""


	path = None
	"""
	DM Root of the DM that is backing this cluster member.

	"""

	nickname = None
	"""
	String that will be used to tag DM Object fields (e.g.
	Server IDs, Paths) in order to identify the contributing
	member.
	Can contain latin letters, digits, the underscore and dash
	characters.

	"""

	identifier = None
	"""
	String that is fetched from the member DM the first time
	it is admitted into the cluster. Used to validate
	subsequent insertions of the DM into the cluster.

	"""

	flags = None
	"""
	Bitfield describing properties of the cluster member. The
	supported flags are defined as constants:
	* dm.PRIMARY_MEMBER
	  This member is the primary one for the cluster (i.e.
	  used for both reading / writing)
	* dm.READ_ONLY_MEMBER
	  This member is used only for reading

	"""

	def __init__(path, nickname, identifier, flags):

		"""

		DMClusterMember object constructor, initializing all members


		@path string: See respective member definition

		@nickname string: See respective member definition

		@identifier string: See respective member definition

		@flags integer: See respective member definition

		@returns object: Returns the created DMClusterMember object

		"""

