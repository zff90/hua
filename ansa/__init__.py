def ImportCode(path):

	"""

	This function imports the code from another python module (py or pyb).


	@path string: The name of the script file to import.

	@returns integer: Returns 0 on success, else an exception is raised.

	"""

def ScriptCurrentDir():

	"""

	Returns the current working directory path.


	@returns string: Returns the current working directory.

	"""

def ScriptHomeDir():

	"""

	Returns the ANSA/META Home directory path


	@returns string: Returns the ANSA/META Home directory path.

	"""

def ScriptUserDir():

	"""

	Returns the BetaHome directory path.


	@returns string: Returns the BetaHome directory path.

	"""

def CompileScript(fileInput, fileOutput, moduleName, mode):

	"""

	Creates a compiled (pyb/bsx) file from the given script path.


	@fileInput string: The path of the script that we want to compile.

	@fileOutput string: The destination path of the created compiled file.

	@moduleName string: The name of the module.

	@mode boolean: (optional)It has effect only for Python scripts.
	The option to include script's imported modules
	inside the compiled file. (only if it is imported with the ansa.ImportCode function) 
	-True, to include dependencies in the compiled script. (Default)
	-False, otherwise.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def PybImport(module_name, script_file_path):

	"""

	A function that imports python scripts (pyb).
	Returns the imported module.


	@module_name string: The name of the module.

	@script_file_path string: The filepath of the script.

	@returns object: Returns the imported module.

	"""

def ReadingFile():

	"""

	Function that returns the currently reading physical file on disk.


	@returns string: Returns the currently reading physical file on disk.

	"""

