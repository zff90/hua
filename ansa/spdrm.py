
class process():
	def getDefinitionWorkflows():
	
		"""
	
		This function queries the SPDRM that is currently configured for Process 
		Management for all workflows.
	
	
		@returns object: The function returns a list of WorkflowDefinition objects
	
		"""
	
	def instantiateWorkflow(workflow_handle_id, input_slot_values, input_dir):
	
		"""
	
		This function instantiates a workflow for execution in the remote SPDRM 
		environment.
	
	
		@workflow_handle_id integer: Identifier of the workflow definition
	
		@input_slot_values object: This argument provides the input values to be offered to
		the nodes in the workflow. It is a map having as keys the
		names of the nodes, while the values are dictionaries
		with keys the input slot names and values the input slot
		values.
	
		@input_dir string: (optional)Path to the directory holding the files that will accompany
		the workflow instantiation request.
		When setting input slots for files transferred within this 
		directory, their value should be set to their relative paths 
		within the input directory.
	
		@returns integer: The function returns an integer:
		  On success it returns the handle id of the instantiated workflow.
		  On failure it returns one of the following values:
		  -1    if 'workflow_handle_id' is invalid
		  -2    if 'input_slot_values' are invalid (i.e. the given value does not match 
		        the input slot variable type)
		  -100  if the user does not have respective privileges
		  -200  if an internal error has happened
	
		"""
	
	def getStateOfWorkflow(workflow_id):
	
		"""
	
		This function queries SPDRM for a running workflow and returns information on 
		its current state.
	
	
		@workflow_id integer: Identifier of the running workflow
	
		@returns object: The function returns a list [error_code, workflow_state, workflow_status]:
		error code:        int      0       if input is correct
		                           -1       if the provided workflow_id was not valid
		                           -100     if the user does not have respective privileges
		                           -200     if an internal error has happened
		workflow_state:    string           is a string with the workflow's state (Finished,Running,Ready)
		workflow_status:                    a WorkflowStatus object, providing more information 
		                                    about the current workflow state
	
		"""
	
	def updateNodeProgress(node_id, node_progress, user_data, dir):
	
		"""
	
		This function is invoked from the ANSA worker, executing a script as part of an
		SPDRM workflow. It reports to the SPDRM server the current progress for the 
		running node.
	
	
		@node_id integer: Handle id of the node for which progress is to be
		reported
	
		@node_progress float: (optional)The progress of the specific node, expressed as a 
		number from 0.0 to 1.0
	
		@user_data object: (optional)A string-to-string dictionary, holding arbitrary
		information that relates to the progress of the
		node
	
		@dir string: (optional)Path of a directory that contains files that are
		relevant to the progress of the node
	
		@returns integer: The function returns an integer:
		   0    on success
		  -1    if 'node_id' is invalid
		  -100  if the user does not have respective privileges
		  -200  if an internal error has happened
	
		"""
	
	def abortWorkflow(workflow_id):
	
		"""
	
		This function aborts the execution of a remotely running SPDRM workflow
	
	
		@workflow_id integer: Identifier of the running workflow
	
		@returns integer: The function returns an integer:
		   0    abort message was successfully signalled to workflow
		  -1    if 'workflow_id' is invalid
		  -100  if the user does not have respective privileges
		  -200  if an internal error has happened
	
		"""
	
	def getWorkflowFiles(workflow_id):
	
		"""
	
		This function fetches from the SPDRM server all files that have been stored on a
		specific workflow instance.
	
	
		@workflow_id integer: Identifier of the workflow instance
	
		@returns object: The function returns a list [error_code, files_path, files_records]:
		error_code:     int      0       if input is correct
		                        -1       if workflow_id given is invalid
		                        -100     if the user does not have respective privileges
		                        -200     if an internal error has occurred
		files_path:     string           holds the path to the directory where the workflow
		                                 files were downloaded. In there, the different node
		                                 files are stored in directories named after the node
		                                 ids.
		files_records:  object           list of FilesRecord objects, each one of them
		                                 describing an SPDRM entity (node / workflow) +
		                                 all files that have been downloaded from this
		                                 entity
	
		"""
	
	def getRoot():
	
		"""
	
		Returns the URL to the SPDRM Server that is currently used for Process Management
		purposes
	
	
		@returns string: Returns a string containing the URL to the Process Management server
	
		"""
	
	def setRoot(url, username, password, role, ticket):
	
		"""
	
		Establishes a connection to a remote server for Process Management purposes. As
		far as authentication is concerned, there are three possibilities:
		* Authenticate with username / password (+ optional role)
		* Provide a ticket to be used in the connection and skip authentication
		* Do not provide anything and search if there is an already stored ticket
		  towards this URL.
	
	
		@url string: URL to the Process Management server
	
		@username string: (optional)Username to be used for authentication
	
		@password string: (optional)Password to be used for authentication
	
		@role string: (optional)User role to authenticate to (in case multiple roles
		are available to user)
	
		@ticket string: (optional)Ticket to used in connection. This argument is provided
		when the connection should employ an already available
		ticket, and there is no need to authenticate with 
		username / password
	
		@returns integer: The function returns an integer:
		    0       on success
		   -1       if the username / password credentials are invalid
		   -2       if role is invalid
		   -3       if ticket is invalid
		   -4       if Process Management is not supported in remote server
		   -5       if no cached ticket could be found
	
		"""
	
	def removeRoot():
	
		"""
	
		Disconnects from the currently connected Process Management server
	
	
		@returns: This function always returns None
	
		"""
	
	def getDefinitionActions(type):
	
		"""
	
		This function queries the current SPDRM for all actions, or for actions of a 
		specific type.
	
	
		@type string: (optional)If provided, the function will return the SPDRM actions of the specific type.
		Otherwise, all kinds of SPDRM actions will be returned.
		Allowed values: All, Generic, DMItem, LibraryItem, Container, Validation
		Default value: All
	
		@returns object: This function returns a list of ActionDefinition objects
	
		"""
	
	class FilesRecord:
	
		"""
	
		The objects of this class are employed when the files of a workflow are to be
		accessed. For each workflow / node that had files downloaded, a FilesRecord 
		object is created. This object holds information on the entity and the files that 
		were downloaded
	
		"""
	
	
		handle_id = None
		"""
		The handle id for the SPDRM entity
	
		"""
	
		entity_name = None
		"""
		The name of the SPDRM entity
	
		"""
	
		entity_type = None
		"""
		The type of the SPDRM entity (node / workflow)
	
		"""
	
		entity_path = None
		"""
		The logical path of this entity within the workflow
	
		"""
	
		files = None
		"""
		A dictionary where keys are the attribute names and values
		are the absolute paths where the corresponding files have 
		been downloaded to.
	
		"""
	class WorkflowDefinition:
	
		"""
	
		The objects of this class provide information on SPDRM Workflows
	
		"""
	
	
		id = None
		"""
		The definition id of the workflow
	
		"""
	
		name = None
		"""
		The name of the workflow
	
		"""
	class WorkflowStatus:
	
		"""
	
		An object of this class provides information on the current status of an SPDRM
		Workflow instance.
	
		"""
	
	
		status = None
		"""
		Describes the current status of the workflow
	
		"""
	
		error_msg = None
		"""
		Provides more information in case of negative status
	
		"""
	
		progress = None
		"""
		Describes the workflow progress as a number between 0.0
		and 1.0
	
		"""
	
		running_nodes = None
		"""
		A list of RunningNode objects, providing details on all
		running workflow nodes.
	
		"""
	class RunningNode:
	
		"""
	
		The objects of this class provide information on a workflow's running nodes.
	
		"""
	
	
		id = None
		"""
		The node's instance id
	
		"""
	
		name = None
		"""
		The name of the node
	
		"""
	
		start_time = None
		"""
		Timestamp when the node started running
	
		"""
	
		progress = None
		"""
		Describes the node progress as a number between 0.0
		and 1.0
	
		"""
	
		user_data = None
		"""
		A string-to-string dictionary holding arbitrary data about
		the progress of the node
	
		"""
	class ActionDefinition:
	
		"""
	
		The objects of this class provide information on SPDRM Actions
	
		"""
	
	
		id = None
		"""
		The definition id of the action
	
		"""
	
		name = None
		"""
		The name of the action
	
		"""
	
		file_path = None
		"""
		The path of the action python script
	
		"""
	
		acls = None
		"""
		The ACLs (Access Control Lists) of the action are provided 
		as an array of dictionaries
	
		"""
	
		script_function = None
		"""
		The function which is used as an entry point for the action
		in the python script
	
		"""
	
		user_id = None
		"""
		The id of the action's owner
	
		"""
	
		gsa_type = None
		"""
		Information on the type of the action (Generic, DMItem,
		LibraryItem, Container, Validation)
	
		"""
	
		dm_item_type = None
		"""
		In case of DM Item scripts, this field provides information on 
		the DM Item types for which the action applies to (Part, Subsystem, etc.)
	
		"""
	
		spdrm_applicable = None
		"""
		Reports whether the specific action is applicable for SPDRM Client
		execution contexts
	
		"""
	
		ansa_applicable = None
		"""
		Reports whether the specific action is applicable for ANSA
		execution contexts
	
		"""
	
		meta_applicable = None
		"""
		Reports whether the specific action is applicable for META
		execution contexts
	
		"""
	
		root_level = None
		"""
		Reports whether the action is shown in root level in the context menu
	
		"""
	
		grouping_path = None
		"""
		The group name under which the specific action is shown in the context menu
	
		"""
	
		overload = None
		"""
		The action name that is overloaded by the current one
	
		"""
	
		generic_like = None
		"""
		Describes whether this action is shown in the main menu as a generic like action
	
		"""
	