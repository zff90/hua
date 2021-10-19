def ApplicationInformation():

	"""

	This function reports build and runtime information of the running ANSA process.
	
	This includes the ANSA version, its build date, and information about the
	architecture of the application and the underling operating system
	The function takes no arguments.
	The report is similar to:
	------------------------------------------------------------
	 A N S A 
	 version: 12.2, compiled on: Jan 11 2007, 13:02:45
	 built: 64-bit
	 platform: Linux x86_64 2.4.21-209-smp little-endian
	------------------------------------------------------------


	@returns string: Returns a string containing the build/runtime information.

	"""

def DeckName(deck):

	"""

	This function returns the deck name as string, given the integer deck constant.


	@deck integer: The integer deck constant.

	@returns string: Returns a string of the Deck name on success. On failure, it raises a ValueError Exception.

	"""

def New(option):

	"""

	This function instructs the program to create a new file.


	@option string: Accepted values:  "blank", "discard", "active" or "all".

	@returns integer: Returns 0 in all cases.

	"""

def Quit(status):

	"""

	This function quits the current file and exits the program.


	@status integer: (optional)The exit code status of ANSA. (Default = 0)

	@returns integer: Returns 0 in all cases.

	"""

def defbutton(group, label, tip):

	"""

	A decorator that adds a menu button.
	It must be placed above the definition of the function which you want to be executed
	when the created button pressed.


	@group string: The name of the group in which the button will be created.

	@label string: (optional)The label of the button.
	(If nothing is declared, the label will be the name of function).

	@tip string: (optional)The button's tip.
	(The text that is shown when the user rolls the mouse pointer over the button)

	"""

def BenchmarkFPS(frames, ctrl_flag, shift_flag, times_to_press_benchmark):

	"""

	Returns a list of size the "times_to_press_benchmark", which contains the results of FPS, 
	same as if you had pressed in ANSA Settings>Graphics>Benchmark button having checkboxes 
	CTRL and SHIFT as per arguments and settings frames set 20(default value).


	@frames integer: Value that sets the number of frames that will be checked.

	@ctrl_flag integer: Options are 0 and 1. Value 0 sets the ctrl flag as unchecked and 
	value 1 sets the flag as checked.

	@shift_flag integer: Options are 0 and 1. Value 0 sets the shift flag as unchecked and 
	value 1 sets the flag as checked.

	@times_to_press_benchmark integer: Value that sets how many times the benchmark is called.

	@returns object: Returns a list of size times_to_press_benchmark with the float values of FPS.

	"""

def SaveSettings():

	"""
	Deprecated since version 20.0.0. Use function BCSettingsWriteFile instead.

	Saves the current settings of ANSA in the defaults file.


	@returns integer: It returns 0 in all cases.

	"""

	import warnings; warnings.warn("Deprecated since version 20.0.0. Use function BCSettingsWriteFile instead.", DeprecationWarning)

def SaveSettingsAs(filename):

	"""
	Deprecated since version 20.0.0. Use function BCSettingsWriteFile instead.

	This function gives the option to save the current settings used in ANSA, with a different file name.


	@filename string: the full pathname of the file where current settings (.defaults) will be saved.

	@returns integer: It returns 0 on success, 1 otherwise.

	"""

	import warnings; warnings.warn("Deprecated since version 20.0.0. Use function BCSettingsWriteFile instead.", DeprecationWarning)

def GetReadyForNewTask():

	"""

	This function is invoked when the currently running ANSA instance is to be 
	declared as available for running new tasks. The actual effect will depend on
	the configuration / state of the ANSA at the time. Specifically, on invocation
	of this command:
	* The currently open database is discarded
	* Python Exception with string 'ReadyForNewTask' as argument is raised. This is
	  equivalent as if the following Python statement was invoked:
	  raise Exception('ReadyForNewTask')
	
	When the execution engine detects that the script terminated with such an 
	exception, then the following courses of action are possible:
	* If ANSA is not running as a worker (i.e. the listen port has not been
	  configured), then the process is terminated.
	* If ANSA is running as a worker, but script execution was not triggered by the
	  connected entity, then an Event Report message is sent with Event Code 
	  'Ready for New Task'
	* If ANSA is running as a worker and script execution was triggered by the 
	  connected entity, then nothing happens.
	  


	@returns: This function always raises an exception / never returns a value

	"""

def PrintMemoryUsage(prefix):

	"""

	Will print the application's current memory usage.


	@prefix string: (optional)If the prefix argument is given, then it will precede the printed text.

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def ProgramArguments():

	"""

	This function retrieves the command line arguments of the program.


	@returns object: Returns a list containing the program arguments.

	"""

def GetFreePhysicalMemory():

	"""

	Returns the free physical memory at the time of this function's call in kilobytes (1024 bytes).


	@returns integer: Returns the free physical memory on success and 0 on failure.

	"""

def BetaClearVariable(name):

	"""

	This function frees the memory from the given beta variable.


	@name string: The name of the beta variable.

	@returns boolean: True if operation was successful, False otherwise.

	"""

def BetaGetVariable(name, match):

	"""

	Ansa script can store user data and address them by a name.
	These data are NOT volatile as script variables and can be accessed either from different scripts or whenever a script is run.
	This function allows the user to retrieve data stored under a user specified name.
	Wildcards can also be used ("*", "?", "[...]").


	@name string: The name of the beta variable to be retrieved.

	@match constant: (optional)Control the matching mode of the name lookup.
	Values are:
	-constants.ENM_EXACT: an exact match (default)
	-constants.ENM_WILDCARD: a wildcard match

	@returns object: The function returns the Beta Variable if the variable is found. It returns None otherwise.
	
	If match=constants.ENM_WILDCARD is used, it returns a dictionary with key the variable name and data the variable value.
	The dictionary is empty if no variables matching the wildcard expression were found.

	"""

def BetaSetVariable(name, value):

	"""

	Ansa script can store user data and address them by a name.
	These data are NOT volatile as script variables and can be accessed either from 
	different scripts or whenever a script is run.
	This function allows the user to store data under a user specified name.


	@name string: The name of the beta variable.

	@value object: A bytes object of the data to store.

	@returns boolean: Returns True on success, or False on failure.

	"""

def GetMemoryUsage():

	"""

	Returns the application's physical memory consumption in kilobytes(1024 bytes).


	@returns object: Returns the application's physical memory consumption on success and None on failure.

	"""

def AcquireFeature(feature):

	"""

	It registers license token found in a BETA LM license.


	@feature string: The feature to acquire license tokens for. 
	The list of available feature names for a specific license server can be found 
	with the command beta_lm_stat -h server. BETA CAE Systems issues license 
	keys to application developers upon request.

	@returns integer: 1: When the feature has been acquired successfully.
	-1: When an incompatible feature is given (ex: ANSA).
	-10: When an invalid feature is given.
	-12: When no credit is available.

	"""

def ReleaseFeature(feature):

	"""

	Releases a previously acquired feature through session.AcquireFeature.


	@feature string: The feature to release the tokens from.

	@returns integer: 1: When a previously acquired feature is succesfully released.
	-1: When an incompatible feature, unknown or a non acquired feature is given.

	"""

def setPluginInfos(classInstance):

	"""

	Sets an instance of a user-defined class, as plugin's information.


	@classInstance object: An Instance of a user-defined class with specific variable names.
	The main Variable names are:
	- filepath: Set as string the path of actual main file. (mandatory)
	- Buttons: A dict in which you set your buttons with key:button's label and 
	           values: tuple(function name, tooltip, help, path for image of button).
	- title: Set title of plugin as string.
	- author: Set author of plugin as string.
	- hostApplication: Set host application of plugin as string.
	- minHostApplicationVersion: Set minimmum host application version of plugin as string.
	- description: Set description of plugin as string.

	"""

