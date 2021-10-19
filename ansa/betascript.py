def CurrentModule():

	"""

	This function is used to get the currently executing module.


	@returns object: Returns the internal reference to the current module.

	"""

def ExecuteFunc(module, function_name, function_arguments):

	"""

	This function is used to run BETA Script code from within Python Code.
	This function executes a function found in a dynamically loaded BETA scripting language script.
	'module' was returned by the 'LoadModule' function.
	'function_name' is the name of the function to call, followed by the arguments you would normally pass to it.


	@module object: A reference to the module.

	@function_name string: The name of the function.

	@function_arguments anything: (optional)Arguments to be passed to the function.

	@returns anything: Returns the return value of the called function. 
	It is safe to call this function even if 'LoadModule' failed.

	"""

def LoadExecuteFunc(script_name, function_name, function_arguments):

	"""

	This function loads the 'script_name' script and calls the 'function_name' function passing it 
	the 'function_arguments' arguments and finally unloads the script. It is a simple shortcut to 
	the Load/Execute/Unload combination. This function is used to run BETA Script code from within Python Code.


	@script_name string: The name of the script.

	@function_name string: The name of the function.

	@function_arguments anything: (optional)The arguments to be passed to the function.

	@returns anything: Returns whatever the invoked function returns.

	"""

def LoadModule(module_name):

	"""

	This function is used to run BETA Script code from within Python Code.
	This function loads a BETA scripting language script file into memory. The new script is 
	in separate memory from the executing script and the user CANNOT call functions from it. 
	You can call functions from this script using the 'ExecuteFunc' function. It is usefull 
	to have this dynamic load feature because you can decide in runtimewhich script to load
	depending on the operation you perform.


	@module_name string: The name of the module to be loaded.

	@returns object: Returns an object containing internal information about the loaded script, or None if it fails to load.
	This element is passed to the 'ExecuteFunc' to execute a function from that script.

	"""

def SetCurrentModule(module):

	"""

	Set the current module (the first in the loaded module list).
	


	@module object: The module object to be set as current.

	@returns integer: Returns 1 on success and 0 on faillure.

	"""

def UnloadModule(module):

	"""

	This function is used to run BETA Script code from within Python Code.
	This function unloads a dynamically loaded BETA scripting language script from memory.
	The 'module' argument is whatever the 'LoadModule' returned when you called to load the module.
	It is safe to call this function even if 'LoadModule' failed.


	@module object: A reference to the module.

	@returns integer: Always returns 0.

	"""

def CheckBreak():

	"""

	A function to check, in execution time, if the Escape(ANSA)/Pause(META) button is pushed.


	@returns integer: Returns:
	0, If the specific button is not pushed.
	1, If the specific button is pushed.

	"""

def RunPluginFunction(plugin_module_name, group_name, button_label):

	"""

	This function is used to call a plugin function from script.


	@plugin_module_name string: The name of the plugin [ppl/bpl] without suffix.

	@group_name string: The group name. An empty string if there is no group.

	@button_label string: The label of the specified button in plugins toolbar.

	"""

def FindModule(module_name):

	"""

	This function returns the module object of a loaded script.
	Takes as argument the name of the wanted module.


	@module_name string: The name of the wanted module.

	@returns object: Returns the module object with the given module name.

	"""

