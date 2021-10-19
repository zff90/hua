def AparameterTaskItemLinkToAparameter(task_item_ref, ansa_parameter_ref, expression):

	"""

	Associates an A_PARAMETER task item of a design variable in the optimization task with an A_PARAMETER.


	@task_item_ref object: The task item object.

	@ansa_parameter_ref object: APARAM object.

	@expression string: (optional)expression to be used when executing the item from the optimization task. Use "$DV" to get Current Value of the Design variable.

	@returns integer: Returns 0 on success, -1 on failure.

	"""

def ChangeTaskItem(task_item_ref):

	"""

	The function changes the status of a task item from checked to unchecked.


	@task_item_ref object: The task item whose status will be switched to unchecked.
	Can be obtained using GetTaskItemsByName() or GetTaskItemsByType().

	@returns integer: Return Value:
	0: The Task Item unupdated succesfuly.
	1: The Task Item failed to unupdate.
	-1: No such Task Item.

	"""

def ClearBreakTaskItem(task_item_ref):

	"""

	@task_item_ref object: The Task Item to remove the break from.
	It can be obtained by a call to GetTaskItemsByName() or GetTaskItemsByType().

	@returns integer: 1: the break on the Task Item was removed.
	-1: no such Task Item.

	"""

def CreateTaskItem(task_item_type , target_task_item_ref):

	"""

	The function creates a new task item in Task Manager. The item type must be given
	exactly as it is displayed in the type field of Task Manager, e.g "Common Model", 
	"Trim Item", "Read XML file" etc. The new item will be created under the 
	target task item.


	@task_item_type string: String that determines the type of the task item to be created.

	@target_task_item_ref object: Target task item. The task item under which the newly created one will be placed.

	@returns object: Returns a reference to the newly created item, or None in case of error.

	"""

def DeleteTaskItem(task_item, delete_results):

	"""

	The function deletes the defined task item.


	@task_item object: The task item that will be deleted. Can be obtained by using GetTaskItemsByName() or 
	GetTaskItemsByType().

	@delete_results string: (optional)Accepted values: "on" or "off". 
	(Default: "off")

	@returns integer: Returns:
	0: The Task Item was deleted succesfuly.
	1: The Task Item failed to delete.
	-1: No such Task Item exists.

	"""

def DisableTaskItem(task_item_ref):

	"""

	The function disables (marks as skipped) the prescribed task item.


	@task_item_ref object: The task item which will disbaled. Can be obtained using GetTaskItemsByName() or 
	 GetTaskItemsByType().

	@returns integer: Returns:
	0: The Task Item was succesfuly disabled.
	1: The Task Item failed to disable.
	-1: No such Task Item existed.

	"""

def EditCommentsTaskItem(task_item_ref, comment):

	"""

	The function sets a comment to the comments field of a task item.


	@task_item_ref object: The task item whose comments field will be edited. Can be
	obtained by using GetTaskItemsByName() or GetTaskItemsByType().

	@comment string: The string that will be inserted as a comment.

	@returns integer: 1: The comment on the Task Item was set.
	-1: No such Task Item.

	"""

def EnableTaskItem(task_item_ref):

	"""

	The function enables (unmark as skipped) the prescribed task item. 


	@task_item_ref object: The task item which will be enabled. Can be obtained by using 
	the GetTaskItemsByName() or GetTaskItemsByType().

	@returns integer: Returns:
	0, if the Task Item was successfully enabled.
	1, if the Task Item failed to enable.
	-1, if there is no such Task Item.

	"""

def ExecTaskItemMenuFun(task_item_ref, item_subfunction_name):

	"""

	Executes any subfunction of a task item context menu. The subfunction name must be given 
	exactly as it is displayed in the context menu.


	@task_item_ref object: The task item from the context menu of which, a subfunction will be selected.

	@item_subfunction_name string: The name of the subfunction.

	@returns integer: Returns 0 on success and -1 on failure.

	"""

def GetAllTaskItems():

	"""

	Returns all task items regardless of their type/name.


	@returns object: Returns a list with the elements of all task items.

	"""

def GetCommentsTaskItem(task_item_ref):

	"""

	The function obtains the entry of the comment field of a task item.


	@task_item_ref object: The task item whose comment field will be obtained. Can be obtained 
	by a call to GetTaskItemsByName() or GetTaskItemsByType().

	@returns string: Returns a string that contains the comment of the task item.

	"""

def GetRootTaskManager():

	"""

	Function that returns a reference to the task manager root.


	@returns object: Returns a reference to the root task manager.

	"""

def GetRunningTaskItem():

	"""

	Gets a reference to the element of the running task item. The running item is a script.
	It can be used in cases where a script item is placed inside a task more than once and 
	performs every time that is called different actions.


	@returns object: Returns a reference to the running task item, or None if the running item is not found.

	"""

def GetTaskItemChildren(task_item_ref, method):

	"""

	The function gets the children of the selected parent task item.


	@task_item_ref object: The task item whose children will be obtained.

	@method integer: The method that will be used.
	Valid types:
	-1: Returns all children.
	-0: Returns first level children.

	@returns object: Returns a list that contains the repsective task items.

	"""

def GetTaskItemName(task_item):

	"""

	The function obtains the name of the prescribed task item.


	@task_item object: The task item whose name will be obtained.

	@returns string: Returns a string containing the name of the task item.

	"""

def GetTaskItemStatus(task_item_ref):

	"""

	The function obtains the status of the defined task item.


	@task_item_ref object: The task item whose status will be obtained.

	@returns integer: Returns one of the following integers:
	0: The Task Item is not updated (not ticked).
	1: The Task Item is updated (ticked).
	2: The Task Item is disabled.
	-1: No such Task Item.

	"""

def GetTaskItemType(task_item_ref):

	"""

	The function obtains the type of the prescribed task item.


	@task_item_ref object: The task item whose type will be obtained.

	@returns string: Returns a string representing the type of the given task item.

	"""

def GetTaskItemsByName(name):

	"""

	The function collects all task item of a specific name.


	@name string: The name of the task items to be collected.

	@returns object: Returns a list of all the matched Task Items.

	"""

def GetTaskItemsByType(type):

	"""

	The function collects all the task items of a specific type.


	@type string: The type of the task items to be collected. Must be set exactly as it 
	is written in the type field of the Task Manager.

	@returns object: Returns a list of all the matched Task Items.

	"""

def MorphparameterTaskItemLinkToMorphparameter(task_item_ref, morph_parameter_ref, after_morph_action, expression):

	"""

	Associates a MORPHPARAMETER task item of a design variable in the optimization task with a morph PARAMETER.


	@task_item_ref object: A task item object.

	@morph_parameter_ref object: A morph parameter object.

	@after_morph_action string: Can have 2 values "Reconstruct" or "Smooth"

	@expression string: (optional)expression to be used when executing the item from the optimization task. Use "$DV" to get Current Value of the Design variable.

	@returns integer: Returns 0 on success, 1 on failure.

	"""

def MoveTaskItem(task_item_ref_to_move, target_task_item_ref, drop_position):

	"""

	Moves the given task item into another item.


	@task_item_ref_to_move object: The task item that will be moved.

	@target_task_item_ref object: The task item under which the moving 
	task item will be placed.

	@drop_position string: (optional)drop_position can have 3 options
	"OnTarget", "BelowTarget" and "AboveTarget"

	@returns integer: 1 : Succesfully moved.
	0 : Failed to move.

	"""

def OpenTaskManager():

	"""

	Opens the Task manager window.


	@returns integer: Always returns 0.

	"""

def ReadTask(task_filename):

	"""

	The function reads a specific task.


	@task_filename string: A string that describes the path and the filename of the ANSA 
	database that contains the task. It can be DM relative.

	@returns integer: Always returns 0.

	"""

def RunAllTasks():

	"""

	Runs all tasks that exist in database.


	@returns integer: Returns:
	0: If all Task Items updated (run) succesfuly.
	1: If any Task Item failed to update (run).

	"""

def SetBreakTaskItem(item):

	"""

	@item object: The Task Item to set a break on it can be obtained by a call to 
	GetTaskItemsByName() or GetTaskItemsByType().

	@returns integer: Returns:
	 1: If the break on the Task Item was set.
	-1: If no such Task Item exists.

	"""

def SetOutputTaskItemName(task_item_ref, new_name_str):

	"""

	This function changes the Output Task Item's exported file name.


	@task_item_ref object: A reference to the task item.

	@new_name_str string: The new path and file name of the exported file.

	@returns integer: Returns:
	 0, on success.
	 1, if failed to name the exported file.
	-1, if there is no such Task Item.

	"""

def SetTaskItemName(task_item_ref, new_name_str):

	"""

	The function renames a task item.


	@task_item_ref object: The task item that will be renamed.

	@new_name_str string: The new name of the task item.

	@returns integer: Returns:
	 0: On sucess. 
	 1: On failure to rename the Task Item.
	-1: If no such Task Item exists.

	"""

def SetToscaOptResultsDir(task_item_ref, directory_str):

	"""

	@task_item_ref object: The Task Item (GENERATE_REPORT_FILE or RUN_SMOOTH).

	@directory_str string: The directory with the optimization results.

	@returns integer: Returns:
	 0: On success.
	 1: On failure name the exported file.
	-1: If no such Task Item exists.

	"""

def UpdateTaskItem(task_item_ref):

	"""

	The function runs the specified task item.


	@task_item_ref object: The task item to be executed. Can be obtained by using 
	the functions GetTaskItemsByName() or GetTaskItemsByType().

	@returns integer: Returns:
	 0, The Task Item was succesfuly updated.
	 1, The Task Item failed to update.
	-1, No such Task Item exists.

	"""

def GetTaskUserScriptData(task_item):

	"""

	Gets the data of a task manager user script.


	@task_item object: The task item whose data will be returned.

	@returns object: Returns a dictionary containing the following information for 
	the given task manager user script:
	module file name:   (module_fname)
	function name:      (function_name)
	arguments:          (arguments)

	"""

def SetTaskUserScriptData(task_item, script_data):

	"""

	Sets the data to a task manager user script.


	@task_item object: The task item of which the data will be edited.

	@script_data object: A dictionary containing the information to be set
	The entries of the dictionary are:
	-module_fname: module file name
	-function_name: function name
	-arguments: arguments
	-store_results: "on" "off"

	@returns integer: Returns 0 on success and 1 on failure.

	"""

def SaveTask(filename):

	"""

	The function saves all the task items of the TaskManager.


	@filename string: A string that describes the path and the filename of the ANSA 
	database, that the task items will be saved.

	@returns integer: Returns 0 on success, or 1 on failure.

	"""

def TaskTemplateItem(template_name, template_reference, template_arguments, template_tip, template_icon):

	"""

	A decorator that adds a User Script task item.
	It must be placed above the definition of the function which you want to be executed
	when called.


	@template_name string: The name of the Task item

	@template_reference string: (optional)The name of the specific Task item's context menu to show

	@template_arguments string: (optional)The arguments to pass in the created User Script

	@template_tip string: (optional)The tip to show on the User Script task item

	@template_icon string: (optional)The icon to show on the User Script task item

	"""

def SetSolverItemData(solver_item, solver_type, output_item, solver_command, solver_options, solver_session):

	"""

	Sets the data to a task manager solver item


	@solver_item object: The Solvet task item

	@solver_type string: Solver type string, it can be one of:
	'Epilysis'
	'NASTRAN'
	'LS-DYNA'
	'PAM-CRASH'
	'ABAQUS'
	'RADIOSS'
	'ANSYS'
	'FLUENT'
	'FLUENT-2D'
	'STAR'
	'UH3D'
	'CFD++'
	'OPENFOAM'
	'PERMAS'
	'MOLDEX3D'
	'TAITHERM'
	'SESTRA'
	'THESEUS'
	'SC/TETRA'
	'TAU'
	'CGNS'
	'CGNS-2D'
	'OPTISTRUCT'
	'MARC'
	'ACTRAN'
	'KINETICS
	'User defined'

	@output_item object: (optional)Output item to use for solving

	@solver_command string: (optional)Solver command to use

	@solver_options string: (optional)Solver options

	@solver_session string: (optional)Session file for CFD Solvers

	@returns integer: Return -1 for error, 0 for success and 1 for failure

	"""

def SetPostProcessingItemData(post_item, post_command, post_session, post_directory, post_response, post_options):

	"""

	Sets the data to a task manager Post-Processing item


	@post_item object: The Post-Processing task item

	@post_command string: (optional)The Meta command, will use the default if empty

	@post_session string: (optional)The session file, will look in current directory if empty

	@post_directory string: (optional)The output directory, current if empty

	@post_response string: (optional)The meta response file

	@post_options string: (optional)the Meta command options

	@returns integer: Return -1 for error, 0 for success and 1 for failure

	"""

def LCPointsFisrtTorsionalWizard(nodes_lc_points):

	"""

	Wizard to create LC_POINTS to be used in order to calculate the First Torsional Mode


	@nodes_lc_points object: (optional)A nodes list to create the LC_POINTS

	@returns object: A list with the created LC_POINTS

	"""

def GetTaskItemParents(task_item_ref, parent_level):

	"""

	Function to get the parents of the given item


	@task_item_ref object: The task item to get its parents

	@parent_level boolean: (optional)True: Returns all parents.
	False: Returns first level parents.
	default value True

	@returns object: A list with the parent items

	"""

def SetTaskItemIcon(task_item, icon_name):

	"""

	The function sets an icon to a task item.


	@task_item object: The task item which icon will be changed

	@icon_name string: The icon path or the icon name for the embedded icons

	@returns integer: Returns:
	 0: On sucess. 
	 1: On failure to set the icon
	-1: If no such Task Item exists.

	"""

def SetResponseItemData( response_item, ansa_entity, ansa_field):

	"""

	Sets the data to a task manager Response item


	@response_item object: The response item

	@ansa_entity object: The ansa entity to retrive response

	@ansa_field string: The ansa field to monitor

	@returns integer: Return -1 for error, 0 for success and 1 for failure

	"""

