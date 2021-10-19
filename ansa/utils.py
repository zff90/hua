def DeckInfo(filename, mode, text_format, active_options, threshold_values, parameter_values):

	"""

	This function saves a deck info report in a file.


	@filename string: The path and the filename to be saved.

	@mode string: Accepted values: 'VISIBLE', 'SELECTED', 'MODEL' or 
	'WHOLE DB'.

	@text_format string: Accepted values: 'HTML', 'TEXT', 'CSV' or 'PDF'.

	@active_options object: (optional)A python list of string items. 
	Accepted string values: the values should be equal to the deck info ansa settings keywords or the gui labels in the deck info window.

	@threshold_values object: (optional)A python dictionary.
	The dictionary key is a string equal to the deck info ansa settings keywords or the gui labels in the deck info window.
	The dictionary value is a csv string with the threshold values.

	@parameter_values object: (optional)A python dictionary.
	This argument is used to set the values parameter values in the Model Tab of deck info
	The dictionary key is a string equal to the deck info ansa settings keyword or the gui labels in Model Info column of the deck info window.
	The dictionary value is a single string value or a csv string.

	@returns integer: Returns 0 on success, or 1 on failure.

	"""

def GetFileInfoFromAnsaDB(ansa_db_file_name):

	"""

	Given the path to an ANSA database, this function extracts its file creation information.
	This information is given by 'tag' parameters and values.


	@ansa_db_file_name string: The file path.

	@returns: Returns a dictionary containing the creation information parameters (parameter's name as key and parameter's value as data) that are defined in an ANSA database.
	The existing tags and their meaning are:
	LEDT: Last Edit Date of the database.
	CRDT: Creation Date of the database.
	VERS: ANSA Version that created the database.
	PRMT: ANSA Parameters in the database.
	HOST: Host on which the database was created.
	CRPL: Platform on with the database was created.
	CMNT: Comment of the database.
	USER: Name of the User that last edited the database.
	IMAG: PNG image of the database. Indicates only its existence.

	"""

def GetParametersFromAnsaDB(ansa_file_name):

	"""

	Creates a map with parameter's name as key and parameter's value as data.


	@ansa_file_name string: A string to declare the file path.

	@returns object: Returns a dictionary containing the ansa-parameters (parameter's name as key and parameter's value as data) that are defined in an ANSA database.

	"""

def Merge(filename, filenames, directory, property_offset, material_offset, set_offset, merge_sets_by_name,paste_nodes_by_name, paste_nodes_by_name_tolerance, paste_cons_by_name, merge_parts,autoposition_parts, create_instances, model_action, coord_offset, node_offset, auto_fit_models, propsection_offset, eos_offset, hourglass_offset, function_offset):

	"""

	This function merges a single ANSA database into an existing one, based on a series
	of user defined arguments.


	@filename string: (optional)Contains the full path to the ANSA database to be
	imported and merged.

	@filenames object: (optional)Contains a list of strings that descibe full paths to
	the ANSA database to be imported and merged.

	@directory string: (optional)Contains the path to a directory, where ANSA will 
	look for any files to be imported and merged.

	@property_offset string: (optional)Determines the action to be taken when property conflicts are noticed 
	during the merge.
	Accepted values: 'offset', 'keep-new' or 'keep-old'.
	(Default: 'keep-old')

	@material_offset string: (optional)Determines the action to be taken when material conflicts are noticed 
	during the merge.
	Accepted values: 'offset', 'keep-new' or 'keep-old'.
	(Default: 'keep-old')

	@set_offset string: (optional)Determines the action to be taken when set conflicts are noticed 
	during the merge.
	Accepted values: 'offset', 'keep-new' or 'keep-old'.
	(Default: 'keep-old')

	@merge_sets_by_name boolean: (optional)Determines whether sets are going to be marged based on their name.
	(Default: False)

	@paste_nodes_by_name boolean: (optional)Determines whether nodes are going to be pasted based on their name.
	(Default: False)

	@paste_nodes_by_name_tolerance float: (optional)Determines the tolerance to be used when nodes are going to be pasted 
	based on their name. (paste_nodes_by_name=True)

	@paste_cons_by_name boolean: (optional)Determines whether cons are going to be pasted based on their name.
	(Default: False)

	@merge_parts boolean: (optional)Determines whether conflicting parts are going to be merged or not.
	(Default: False)

	@autoposition_parts boolean: (optional)Determines whether multi-instantiated parts will be 
	autopositioned or not.
	(Default: 'off')

	@create_instances boolean: (optional)Determines whether two parts with the same Id or name will be merged 
	or a new instance of the part will be created.

	@model_action string: (optional)Accepted values: "overwrite_model", "merge_model", 
	"new_model_in_active_window", "new_model_in_new_window",
	"new_model_in_enabled_windows", "separate_models_in_active_window",
	"separate_models_in_new_window" or
	"separate_models_in_enabled_windows"
	(Default: "merge_model")

	@coord_offset string: (optional)Determines the action to be taken when coordinate system conflicts
	are noticed during the merge.
	Accepted values: 'offset', 'keep-new' or 'keep-old'.
	(Default: 'offset')

	@node_offset string: (optional)Determines the action to be taken when node conflicts
	are noticed during the merge.
	Accepted values: 'offset', 'keep-new' or 'keep-old'.
	(Default: 'offset')

	@auto_fit_models boolean: (optional)Determines whether merge models will be autopositioned or not.
	(Default 'true')

	@propsection_offset string: (optional)Determines the action to be taken when prop/section conflicts
	are noticed during the merge.
	Accepted values: 'offset', 'keep-new' or 'keep-old'.
	(Default: 'offset')

	@eos_offset string: (optional)Accepted values: "offset", "keep-old" or "keep-new" 
	(Default: "offset")

	@hourglass_offset string: (optional)Accepted values: "offset", "keep-old" or "keep-new" 
	(Default: "offset")

	@function_offset string: (optional)Accepted values: "offset", "keep-old" or "keep-new" 
	(Default: "offset")

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def OpenPartManager(view_mode):

	"""
	Deprecated since version 17.0.0. Use function OpenModelBrowser instead.

	Opens the part manager window.


	@view_mode string: (optional)Accepted values: 'list_view', 'tree_view' or 'icon_view'.

	@returns integer: Always returns 0.

	"""

	import warnings; warnings.warn("Deprecated since version 17.0.0. Use function OpenModelBrowser instead.", DeprecationWarning)

def PrintToFile(filename, image_format, red, green, blue, transparent, text_axes, gradient):

	"""
	Deprecated since version 18.0.0. Use function SnapShot instead.

	The PrintToFile function grabs the whole screen of ANSA's graphics window and saves it as an image in the specified file.


	@filename string: The filename to be saved. This argument is mandatory.
	If filename exists, it will be overwritten.

	@image_format string: (optional)'POSTSCRIPT', 'RGB', 'TIFF', 'JPEG', 'PNG', 'BMP'.

	@red integer: (optional)The number of the red component of the background color [0-255].

	@green integer: (optional)The number of the green component of the background color [0-255].

	@blue integer: (optional)The number of the blue component of the background color [0-255].

	@transparent boolean: (optional)True or False, to enable or disable trasparent background.
	(available for png image format only)

	@text_axes boolean: (optional)Text and axes visible or not.

	@gradient boolean: (optional)Leaves gradient visible or not.

	@returns integer: Returns 0 on success and 1 on failure.

	"""

	import warnings; warnings.warn("Deprecated since version 18.0.0. Use function SnapShot instead.", DeprecationWarning)

def SetDrawingAreaColor(r_int, g_int, b_int):

	"""

	Sets the RGB values for the color of drawing area to be r, g and b.


	@r_int integer: The value for red (0 - 255).

	@g_int integer: The value for green (0 - 255).

	@b_int integer: The value for blue (0 - 255).

	@returns integer: Always returns 1.

	"""

def VtrapsBubbles(step_type, forced_step, calculation_angle_rx1, calculation_angle_ry1, calculation_angle_rz1, printout_angle_rx2, printout_angle_ry2, printout_angle_rz2, printout_filename, printout_file_format):

	"""

	Script function for the calculation of bubble traps in VTRAPS tool and a printout of the results. 
	User specifies two positions, one for the calculation and one for the display of the results for 
	the image printout.


	@step_type integer: 0 for imposed step 1 for auto step.

	@forced_step float: The forced step value.

	@calculation_angle_rx1 float: The x coordinate of the calculation angle.

	@calculation_angle_ry1 float: The y coordinate of the calculation angle.

	@calculation_angle_rz1 float: The z coordinate of the calculation angle.

	@printout_angle_rx2 float: The x coordinate of the printout angle.

	@printout_angle_ry2 float: The y coordinate of the printout angle.

	@printout_angle_rz2 float: The z coordinate of the printout angle.

	@printout_filename integer: The path where the printout will be saved.

	@printout_file_format integer: The format of the printout file to save.

	@returns object: Returns the image file.

	"""

def VtrapsPonds(step_type, forced_step, calculation_angle_rx1, calculation_angle_ry1, calculation_angle_rz1, printout_angle_rx2, printout_angle_ry2, printout_angle_rz2, printout_filename, printout_file_format):

	"""

	Function for the calculation of pond traps in VTRAPS tool and a printout of the results.
	User specifies two positions, one for the calculation and one for the display of the results for the image printout.


	@step_type integer: 0 for imposed step, 1 for auto step.

	@forced_step float: The forced step value.

	@calculation_angle_rx1 float: The x coordinate of the calculation angle.

	@calculation_angle_ry1 float: The y coordinate of the calculation angle.

	@calculation_angle_rz1 float: The z coordinate of the calculation angle.

	@printout_angle_rx2 float: The x coordinate of the printout angle.

	@printout_angle_ry2 float: The y coordinate of the printout angle.

	@printout_angle_rz2 float: The z coordinate of the printout angle.

	@printout_filename string: The path where the printout will be saved.

	@printout_file_format string: The format of the printout file to save.

	@returns object: Returns the image file.

	"""

def SnapShot(filename, image_format, red, green, blue, transparent, text_axes, gradient, foreground_red, foreground_green, foreground_blue, auto_text_color, image_size, copy_to_clipboard):

	"""

	The SnapShot function grabs the whole screen of ANSA's graphics window and saves it as an image in the specified file.


	@filename string: The filename to be saved. This argument is mandatory.
	If filename exists, it will be overwritten.

	@image_format string: (optional)One of: ['POSTSCRIPT' | 'RGB' | 'TIFF' | 'JPEG' | 'PNG' | 'BMP'].

	@red integer: (optional)The number of the red component of the background color [0-255].

	@green integer: (optional)The number of the green component of the background color [0-255].

	@blue integer: (optional)The number of the blue component of the background color [0-255].

	@transparent boolean: (optional)Enables/disables trasparent background (available for png image format only).

	@text_axes boolean: (optional)Text and axes visible or not.

	@gradient boolean: (optional)Leaves gradient visible or not.

	@foreground_red integer: (optional)The number of the red component of the foreground color [0-255].se

	@foreground_green integer: (optional)The number of the green component of the foreground color [0-255].

	@foreground_blue integer: (optional)The number of the blue component of the foreground color [0-255].

	@auto_text_color boolean: (optional)Automatically change foreground color if it is similar to the background color.

	@image_size object: (optional)Sets the size of the snapshot image. It must be a tuple of two integers, 
	both set to a value greater or equal to 1.

	@copy_to_clipboard boolean: (optional)Set this option in order to copy the snapped image directly also to the clipboard

	@returns integer: Returns 0 on success and 1 on failure.

	"""

def OpenIncludesManager():

	"""

	Opens the Includes Manager window.


	@returns integer: Always returns 0.

	"""

def MainProgressBarSetValue(value):

	"""

	Progress bar is used to give the user an indication of the progress of an operation 
	and to reassure them that the application is still running.
	In gui mode, main progress bar is located at main ANSA window below gl model.
	Ensure the main progress bar is visible (MainProgressBarSetVisible).
	If you set an invalid value or progress bar is not visible, nothing happens.
	In no-gui mode, the value is printed in the terminal. Function is thread safe.
	Note that main progress bar is shared among several users.


	@value integer: Valid values: 0 - 100.

	@returns integer: Always returns 1.

	"""

def MainProgressBarSetVisible(value):

	"""

	The progress bar is used to give the user an indication of the progress of an operation 
	and to reassure them that the application is still running.
	The main progress bar is located at the main ANSA window below the gl model.
	Show the progress bar and update its value (progress) inside your procedure.
	Remember to hide the progress bar after your procedure has finished. Function is thread safe.
	Note that the main progress bar is shared among several users.


	@value integer: Valid values are 0 to hide and 1 to show the progress bar.

	@returns integer: Always returns 1.

	"""

def MainProgressBarSetText(text):

	"""

	Progress bar is used to give the user an indication of the progress of an operation 
	and to reassure them that the application is still running.
	In gui mode, main progress bar is located at main ANSA window below gl model.
	Ensure that the main progress bar is visible (MainProgressBarSetVisible).
	If the progress bar is not visible, nothing happens.
	Note that the main progress bar is shared among several users.


	@text string: The text that will be displayed on the progress bar.

	@returns integer: Always returns 1.

	"""

def OpenModelBrowser(entity_type, view_mode, main_tabs, current_main_tab, info_tabs, current_info_tab, side_panel, current_side_panel_tab, profile):

	"""

	Opens the Model Browser window.


	@entity_type string: (optional)The Main tab to make current. This argument is obsolete, use current_main_tab
	instead.
	Accepted values:
	- The tab names as they are shown: 'Parts', 'Configurations', 'Subsystems', etc.
	- The ANSA keywords: 'ANSAPART', 'ANSA_CONFIGURATION', 'ANSA_SUBSYSTEM', etc.

	@view_mode string: (optional)The view mode to show in list for the current Main tab.
	Accepted values: tree_view, flat_view, icon_view or the view names as they are shown.

	@main_tabs object: (optional)A list of Main tabs in the order to show them.
	Accepted values:
	- The tab names as they are shown: 'Parts', 'Configurations', 'Subsystems', etc.
	- The ANSA keywords: 'ANSAPART', 'ANSA_CONFIGURATION', 'ANSA_SUBSYSTEM', etc.

	@current_main_tab string: (optional)The Main tab to make current.
	Accepted values:
	- The tab name as it is shown: 'Parts', 'Configurations', 'Subsystems', etc.
	- The ANSA keyword: 'ANSAPART', 'ANSA_CONFIGURATION', 'ANSA_SUBSYSTEM', etc.

	@info_tabs object: (optional)A list of Info tabs in the order to show them.
	Accepted values:
	- The tab names as they are shown: 'Details', 'Contents', 'Connectivity', etc.

	@current_info_tab string: (optional)The Info tab to make current.
	Accepted values:
	- The tab name as it is shown: 'Details', 'Contents', 'Connectivity', etc.

	@side_panel boolean: (optional)The visibility of the Side Panel.
	Accepted values:
	- True: the Side Panel is shown
	- False: the Side Panel is hidden

	@current_side_panel_tab string: (optional)The tab in the Side Panel to make current.
	Accepted values:
	- The tab name as it is shown: 'Table View', 'References'

	@profile string: (optional)The name of the Profile to use.
	Accepted values:
	- Any of the Profile names which exist in the Model Browser Profile settings.

	@returns boolean: Returns True if the Model Browser opened succesfully, otherwise False.

	"""

def CloseModelBrowser():

	"""

	Closes the Model Browser window.


	@returns object: Always returns None.

	"""

def DatabaseBrowserInfo(deck):

	"""

	This function provides a dictionary with the Database Browser structure of the current model.


	@deck constant: The deck for which you get the Database Browser structure.

	@returns object: It returns a dictionary with keys the names of the parent items of the Database Browser 
	and data objects with two members: 'total' and 'children', where total is the number of 
	elements for the item and children is again a dictionary with such objects.
	If an item doesn't have any children, this dictionary is empty.
	
	The example below will print the following:
	
	ANSAPART 3
	EDGE 0
	ELEMENT 420
	        SHELL 420
	                /SH3N 5
	                /SHELL 415
	GEOMETRY 3
	        WPLANE 3
	MATERIAL 1
	        LAW25-ELASTIC-PLASTIC-ORTHOTROPIC 1
	NODE 500
	PROPERTY 1
	        LAMINATE 1
	SOLIDFACET 0
	TO_BE_REMOVED 98
	        ATTRIBUTE 98

	"""

def ReadGUISettings( xml_file_path ):

	"""

	This function applies GUI settings read from the given file.
	WARNING: It will remove any previous settings and custom menus or toolbars.


	@xml_file_path string: The absolute or relative path to a GUI settings file, like ANSA.xml, CFD.xml etc.

	@returns boolean: Returns true on successful application of the read GUI settings, false otherwise.

	"""

def SaveGUISettings( xml_file_path ):

	"""

	This function saves the current GUI settings to a file.


	@xml_file_path string: The absolute or relative path to a GUI settings file, like ANSA.xml, CFD.xml etc.

	@returns boolean: Returns true on successful saving of the current GUI settings to the given file, false otherwise.

	"""

def CurrentGUISettings():

	"""

	This function returns the file path of the current GUI settings file.


	@returns string: The absolute file path of the current GUI settings file.

	"""

def SnapShotWidget(filename, image_format, widget):

	"""

	The SnapShotWidget function grabs widget child of a window and saves it as an image in the specified file.


	@filename string: The filename to be saved. This argument is mandatory.
	If filename exists, it will be overwritten.

	@image_format string: (optional)One of: ['POSTSCRIPT' | 'RGB' | 'TIFF' | 'JPEG' | 'PNG' | 'BMP'].

	@widget object: (optional)The returned value of the function that create the widget.

	@returns integer: Returns 0 on success and 1 on failure.

	"""

def SnapShotWindow(filename, image_format, window_title):

	"""

	The SnapShotWindow function takes a snapshot of a window and saves it as an image in the specified file.


	@filename string: The filename to be saved. This argument is mandatory.
	If filename exists, it will be overwritten.

	@image_format string: (optional)One of: ['POSTSCRIPT' | 'RGB' | 'TIFF' | 'JPEG' | 'PNG' | 'BMP'].

	@window_title string: (optional)The window title.

	@returns integer: Returns 0 on success and 1 on failure.

	"""

def ShowModelBrowserColumn(column_name, position):

	"""

	Shows the column with specific name in the current Tab of Model Browser window in specific position.


	@column_name string: The name of the column to show.

	@position integer: (optional)Determines in which position to show the column.

	@returns object: Always returns None

	"""

def HideModelBrowserColumn(column_name):

	"""

	Hides the column with specific name from the current Tab of Model Browser window.


	@column_name string: The name of the column to hide.

	@returns object: Always returns None

	"""

def SetDrawingForegroundColor(r, g, b):

	"""

	Sets the RGB values of the foreground color of the drawing area to be r, g and b.


	@r integer: The value for red (0 - 255).

	@g integer: The value for green (0 - 255).

	@b integer: The value for blue (0 - 255).

	@returns object: Always returns None.

	"""

def DrawingForegroundColor():

	"""

	Returns the RGB values of the foreground color of the drawing area.


	@returns object: A tuple of three values which are the RGB components of the foreground color.

	"""

def AddCurveToPlot(plot, curve):

	"""

	This function adds new curves to a created plot. 
	Can be used for one curve: AddCurveToPlot(plot, curve)
	or for multiple curves at once: AddCurveToPlot(plot, [curve1, curve2, curve3...])
	
	


	@plot object: This argument is the plot.

	@curve object: This argument is the curve to be added (single one) or a list of curves (for multiple curves).

	@returns: Returns None always.

	"""

def SetCurveProperties(curve, type, color, width, label, marker_style, marker_size, dash_style, offset_on,         curve_attributes, curve_points_attributes):

	"""

	This function sets properties to a created curve. Argument options:
	- type: Line or Bar
	- color: [r,g,b]
	- width
	- label 
	- marker_style: None, Cross, Plus, WhiteSquare, BlackSquare, Diamond, Circle, TriangleUp, TriangleDown
	- marker_size: integer 
	- dash_style: Solid, SparseShortDot, SparseDot, SparseLongDot, Dash, ThickDash, DashDot, ShortDot, Dot, LongDot, 
	        DenseShortDot, DenseDot, DenseLongDot 
	- offset: True or False
	- curve_attributes: {"Module id":"Karosseriegerippe", "CarLine":"LU",...} 
	- curve_points_attributes: { 0:attr_map_for_point0, 1:attr_map_for_point1, 2:attr_map_for_point2 ... }
	
	


	@curve object: This argument is the curve to add properties to.

	@type string: (optional)This argument is the curve type.

	@color object: (optional)This argument is a list of 3 integers (0-255 for r, g, b channels) 
	to define color.

	@width integer: (optional)This argument is the curve width.

	@label string: (optional)This argument is a label (to be seen in legend).

	@marker_style string: (optional)This argument is the marker style.

	@marker_size integer: (optional)This argument is the marker size. Default value is 5.

	@dash_style string: (optional)This argument is the dash style.

	@offset_on boolean: (optional)This argument enables or disables offset (True or False).

	@curve_attributes object: (optional)This argument is a dictionary with attribute name-values.

	@curve_points_attributes object: (optional)This argument is a dictionary with attribute name-values for curve's points. 
	Dictionary has as key an integer and as data a map of name-values.

	@returns: Returns None always.

	"""

def SetYAxisProperties(plot, title, unit, min_max, num_of_steps, step_labels, show_values_on_axis):

	"""

	This function sets properties for the Y axis of a plot. For example: SetYAxisProperties(Plot, title="Mass", unit="kg", 
	min_max=(0,1000), num_of_steps=12, step_labels={index_of_step_1:label_at_step_1, index_of_step_2:label_at_step_2 ...}, 
	show_values_on_axis=True)


	@plot object: This argument is the relevant plot.

	@title string: (optional)This argument is the title shown for Y axis.

	@unit string: (optional)This argument is the unit used for Y axis. It would be shown beside the title.

	@min_max object: (optional)This argument is a pair of 2 numbers (integers or floats) to set minimum and 
	maximum values of Y axis.

	@num_of_steps integer: (optional)This argument sets the number of steps to be used.

	@step_labels object: (optional)This argument is a dictionary of integer:string pairs, where key is the step 
	index and value is the label we want to use for this step. If user hasn't set 
	the number of steps to be used, number of steps is set by the number of given 
	labels plus 1.

	@show_values_on_axis boolean: (optional)This argument is used to set if values should be visible on axis (True or False).

	@returns: Returns None for success,
	        Null otherwise.

	"""

def SetXAxisProperties(plot, title, unit, min_max, num_of_steps, step_labels, show_values_on_axis):

	"""

	This function sets properties for the X axis of a plot. For example: SetXAxisProperties(Plot, title="Mass", unit="kg", 
	min_max=(0,1000), num_of_steps=12, step_labels={index_of_step_1:label_at_step_1, index_of_step_2:label_at_step_2 ...}, 
	show_values_on_axis=True)


	@plot object: This argument is the relevant plot.

	@title string: (optional)This argument is the title shown for X axis.

	@unit string: (optional)This argument is the unit used for X axis. It would be shown beside the title.

	@min_max object: (optional)This argument is a pair of 2 numbers (integers or floats) to set minimum and 
	maximum values of X axis.

	@num_of_steps integer: (optional)This argument sets the number of steps to be used.

	@step_labels object: (optional)This argument is a dictionary of integer:string pairs, where key is the step 
	index and value is the label we want to use for this step. If user hasn't set 
	the number of steps to be used, number of steps is set by the number of given 
	labels plus 1.

	@show_values_on_axis boolean: (optional)This argument is used to set if values should be visible on axis (True or False).

	@returns: Returns None for success,
	        Null otherwise.

	"""

def SetPlotProperties(plot, title, show_legend, legend_position, show_grid):

	"""

	This function sets properties for the given plot. Available values:   
	- legend_position: TopRight, TopLeft, BottomRight, BottomLeft
	- show_legend: True/False
	- show_grid: True/False
	


	@plot object: This argument is the relevant plot to set properties to.

	@title string: (optional)This argument is the title to give to the plot.

	@show_legend boolean: (optional)Flag to set if legend should be shown or not (True/False). Legend is given as 
	curve label (see function utils.SetCurveProperties).

	@legend_position string: (optional)This argument sets the position of legend: TopRight, TopLeft, BottomRight, 
	BottomLeft.

	@show_grid boolean: (optional)Flag to set if grid should be shown or not (True/False).

	@returns: Returns None for success,
	        Null otherwise.

	"""

def CreatePlot():

	"""

	This function creates a new plot.


	@returns: Upon success, it returns a Class object referring to the newly created plot.
	Else, None is returned.

	"""

def DeletePlot(plot):

	"""

	This function deletes the plot object given as argument. 
	


	@plot object: This argument is the plot that is going to be deleted.

	@returns: Returns None on success.
	        Null otherwise.

	"""

def RecentFilesRecordingSetEnabled(enabled):

	"""

	Enables or disables the recording of recent files (that appear in the history of File>Input Recent and File>Open Recent).


	@enabled boolean: set to False in odrer to dsable recording, otherwise True.

	@returns: The function always returns None.

	"""

def RecentFilesRecordingIsEnabled():

	"""

	Checks if the recording of recent files (the ones that appear in the history of File>Input Recent and File>Open Recent) is on or off. When off, any files accessed by File>Open and File>Input actions aren't recorded.


	@returns boolean: True if the recording of recent files is enabled or False otherwise.

	"""

def FringeBarUnpinPosition(type):

	"""

	The FringeBarUnpinPosition function unpins the fringebar of type 'type'. If the fringebar is not previously pinned, this function has no effect.


	@type string: (optional)One of: ['GENERAL' | 'DEFORMATION' | 'SURFACE_INFO' | 'IGA_INFO']
	If empty, 'GENERAL' will be used by default.

	@returns object: Always returns None.

	"""

def FringeBarPinPosition(position, type, coordinates):

	"""

	The FringeBarPinPosition function pins the fringebar of type 'type' to the specified position of the GL area. This will be applied to all GL windows.


	@position constant: The position where fringebar should be pinned:
	- utils.constants.BCPositionDefault : Factory defaults or values read from XML
	- utils.constants.BCPositionTopLeft : The top-left corner of the GL area
	- utils.constants.BCPositionTopRight : The top-right corner of the GL area
	- utils.constants.BCPositionTopHCenter : The top and horizontal-center of the GLarea.
	- utils.constants.BCPositionBottomLeft : The bottom-left corner of the GL area
	- utils.constants.BCPositionBottomRight : The bottom-right corner of the GL area
	- utils.constants.BCPositionBottomHCenter : The bottom and horizontal-center of
	the GL area.
	- utils.constants.BCPositionLeftVCenter : The left and vertical-center of the GL area
	- utils.constants.BCPositionRightVCenter : The right and vertical-center of the GL area
	- utils.constants.BCPositionCenter : The center of the GL area
	- utils.constants.BCPositionCustom : Use this in combination with argument 'coordinates'
	to pin the fringebar to a user-defined position

	@type string: (optional)One of: ['GENERAL' | 'DEFORMATION' | 'SURFACE_INFO' | 'IGA_INFO']
	If empty, 'GENERAL' will be used by default.

	@coordinates object: (optional)User-defined position. It must be a tuple of two real values, both set in range [0., 1]
	which maps the percentage of the GL area. Use this only when argument 'position'
	is set to utils.constants.BCPositionCustom.
	Pin-point of the fringebar is meant the top-left corner of its geometry.
	If custom coordinates cause fringebar geometry to exceed GL area's boundaries the fringebar will be automatically fitted.

	@returns object: Always returns None.

	"""

class UnitSystem():

	"""

	A unit conversion system.

	"""


	length = None
	"""
	The length unit.

	"""

	mass = None
	"""
	The mass unit.

	"""

	time = None
	"""
	The time unit.

	"""

	temperature = None
	"""
	The temperature unit.

	"""

	kinetics_force = None
	"""
	The force unit for kinetics

	"""

	def __init__(length, mass, time, temperature, kinetics_force):

		"""

		UnitSystem object constructor.


		@length string: (optional)The length unit. Valid values are: "meter", millimeter", 
		"inch", "feet", "mile", "kilometer", "mil", "micron", 
		"centimeter", "microinch".
		(Default: "milimeter")

		@mass string: (optional)The mass unit. Valid values are: "kilogram", "gram", 
		"tonne", "pound".
		(Default: "tonne")

		@time string: (optional)The time unit. Valid values are: "second", "millisecond", 
		"minute", "hour".
		(Default: "second")

		@temperature string: (optional)The temperature unit. Valid values are: "kelvin", 
		"degree Celsius", "degree Fahrenheit".
		(Default: "kelvin")

		@kinetics_force string: (optional)The force unit for kinetics

		@returns object: Returns the created UnitSystem object.

		"""


	def set_current(unit_system, apply_to_settings, apply_to_models):

		"""

		Sets ANSA's current unit system


		@unit_system object: A UnitSystem object. If this argument is set to None,
		ANSA's unit system is disabled.

		@apply_to_settings boolean: (optional)If set to True, units will be applied on ANSA settings. If set
		to False settings will not change. True by default.

		@apply_to_models boolean: (optional)If set to True a unit conversion will be performed from the 
		current UnitSystem to the new UnitSystem. If set to 
		False no conversion will take palce. False by default.

		"""


	def get_current():

		"""

		Returns ANSA's current unit system or None if there is none defined


		@returns object: Returns a UnitSystem object

		"""

class FileCacher():

	"""

	The FileCacher object provides access to the application wide File Caching
	service. It allows the addition / lookup / deletion of files from the cache
	store.
	
	Since the cache store has a finite size, older cache entries are evicted (when
	needed) in order to accommodate new ones. If a user wants to be sure that a file
	found in the cache will continue to be available for a certain duration, then
	the corresponding cache entry needs to be supervised using a FileCacherWatchdog.
	
	The ResultCode is an integer that is used by the methods of this class to 
	report the outcome of an operation. The values it holds are:
	
	- 0: Success.
	- 1: Out of disk space.
	- 2: Source file not found.
	- 3: Cache entry already exists.
	- 4: Cache backend failure.
	
	This class employs the following custom Objects:
	
	CacheDmAddResult
	
	This object conveys the result of a DM cache entry addition (i.e. method
	add_dm_file). Its members are:
	
	- result_code: Result of the operation. See ResultCode definition on the meaning of each value.
	- path: Path of the integrated file within the cache store.
	- token: Object of type CacheToken which refers to this specific cache entry in the store.
	
	CacheKeylessAddResult
	
	This object conveys the result of a keyless cache entry addition (i.e. method
	add_keyless_file). Its members are:
	
	- result_code: Result of the operation. See ResultCode definition on the meaning of each value.
	- path: Path of the integrated file within the cache store.
	- identity: Identifies this entry in the cache store; can be used for later lookups.
	- token: Object of type CacheToken which refers to this specific cache entry in the store.
	         
	CacheLookedUpFile
	
	This object returns the information for a single cache entry after a lookup. Its
	members are:
	
	- path: Path of the looked up file within the cache store.
	- timestamp: Time which is considered 'Last Edit' for this file.
	- token: Object of type CacheToken which refers to this specific cache entry in the store.
	         
	CacheLookupResult
	
	This object holds the result of a lookup operation. Its members are:
	
	- result_code: Result of the operation. See ResultCode definition on the meaning of each value.
	- files: Sequence of CacheLookedUpFile objects, one per cache entry returned by the lookup.
	         
	CacheToken
	
	This object points to a specific cache entry and is used to uniquely refer to:
	
	- the cache entry inserted via an add operation.
	- a specific cache entry returned by a lookup operation.
	
	The user is not supposed to create objects of this class, but should provide
	a token return by the File Cacher itself. CacheToken objects are provided as
	arguments to operations that accept references to concrete cache entries (e.g.
	deletion mark or Watchdog supervise --- see also FileCacherWatchdog)

	"""


	def is_up():

		"""

		Checks if the File Caching service is currently active or not.


		@returns boolean: True is returned if File Caching services are available; otherwise (e.g. service deactivated by configuration or couldn't start up due to a fault) False is returned.

		"""


	def add_dm_file(path, server_id, file_type, timestamp, dm_root, importance, gather_siblings, delete_source):

		"""

		Add a file to the store as cached copy of a remote DM file.


		@path string: Path of the file / directory to be added into
		the cache store.

		@server_id string: Server side identifier of the DM Object, to which
		this file relates.

		@file_type string: Describes the file usage / type within the
		specific DM Object.

		@timestamp integer: Last edit timestamp for this file.

		@dm_root string: (optional)Path / URL of the DM root.
		Default value: Current DM root

		@importance string: (optional)Importance level to be attached to the cache
		entry. One of 'NORMAL', 'HIGH' or
		'VERY_HIGH'.
		Default value: 'NORMAL'

		@gather_siblings boolean: (optional)Defines whether the other files coexisting in the
		same folder as the one to be cached will be also
		integrated in the cache store or not.
		Default value: False

		@delete_source boolean: (optional)Defines whether the source file shall be deleted
		after successful addition to the cache store.
		Default value: False

		@returns object: This method returns an object of type CacheDmAddResult (see class description for more details).

		"""


	def lookup_dm_file(server_id, file_type, dm_root, timestamp_policy):

		"""

		Lookup if a cached copy of a remote DM file is available.


		@server_id string: Server side identifier of the DM Object, to which
		this file relates.

		@file_type string: Describes the file usage / type within the
		specific DM Object.

		@dm_root string: (optional)Path / URL of the DM root.
		Default value: Current DM root

		@timestamp_policy string: (optional)Describes which cache entries to return, in case
		entries with different timestamps satisfy the
		lookup. Either 'ALL' or 'LATEST_ONLY'
		Default value: 'LATEST_ONLY'

		@returns object: This method returns an object of type CacheLookupResult (see class description for more details).

		"""


	def add_keyless_file(path, importance, gather_siblings, delete_source):

		"""

		Add a file in the cache store for which no key is available, but the caching service will generate a (unique) key for it.


		@path string: Path of the file / directory to be added into
		the cache store.

		@importance string: (optional)Importance level to be attached to the cache
		entry. One of 'NORMAL', 'HIGH' or
		'VERY_HIGH'.
		Default value: 'NORMAL'

		@gather_siblings string: (optional)Defines whether the other files coexisting in the
		same folder as the one to be cached will be also
		integrated in the cache store or not.
		Default value: False

		@delete_source string: (optional)Defines whether the source file shall be deleted
		after successful addition to the cache store.
		Default value: False

		@returns integer: This method returns an object of type CacheKeylessAddResult (see class description for more details).

		"""


	def lookup_keyless_file(identity):

		"""

		Lookup if a file added as a keyless cache entry is available.


		@identity string: Identifies this entry in the cache store (was
		assigned during addition by the File Cacher
		itself).

		@returns integer: This method returns an object of type CacheLookupResult (see class description for more details).

		"""


	def deletion_mark(token):

		"""

		Mark a cache entry for deletion.


		@token object: Object of type CacheToken, referencing the cache
		entry in the store. This object has been provided
		by the File Cacher after an add / lookup file
		operation.

		@returns integer: This method returns a ResultCode describing the operation result (see class description for more details).

		"""

class FileCacherWatchdog():

	"""

	Since the cache store has a finite size, older cache entries are evicted (when
	needed) in order to accommodate new ones. The FileCacherWatchdog object protects 
	one or more cache entries against getting removed from the cache store. This
	way, a user can be certain that cached files will not disappear when they are
	needed / used.
	
	This class employs the following custom Objects:
	
	CacheToken
	This object points to a specific cache entry and is used to uniquely refer to
	- the cache entry inserted via an add operation
	- a specific cache entry returned by a lookup operation
	The user is not supposed to create objects of this class, but should provide
	a token return by the File Cacher itself. CacheToken objects are provided as
	arguments to operations that accept references to concrete cache entries (e.g.
	supervise or deletion mark --- see also FileCacher)

	"""


	def supervise(token):

		"""

		Add a cache entry reference into the list of supervised ones.


		@token object: Object of type CacheToken, referencing the cache
		entry in the store. This object has been provided
		by the File Cacher after an add / lookup file
		operation.

		@returns object: Always returns None.

		"""


	def clear():

		"""

		Clear the list of protected cache entries.


		@returns object: Always returns None.

		"""

def ShowLog(title_string):

	"""

	This function opens a monitor window and waits for the user to close it. It is similar to
	OpenMonitor only this one waits for the user to close the window before it continues with
	the execution of the script. This makes it useful for displaying a process log and letting
	the user decide if he wants to continue with the execution of the script.


	@title_string string: The log window title to show.

	@returns integer: The function returns 1 if OK is pressed and 0 if Cancel is pressed.

	"""

def XlsxClose(file):

	"""

	Closes the defined ".xlsx" file.


	@file object: A reference to the ".xlsx" file created by XlsxCreate or XlsxOpen.

	@returns integer: Returns 0 if the ".xlsx" is not found, or 1 on success.

	"""

def XlsxCreate():

	"""

	Creates a new empty xlsx_file.


	@returns object: Returns a reference to the xlsx_file that is created, or None on failure.

	"""

def XlsxGetCellValue(file, sheet, row, column):

	"""

	Returns the cell value from the specified row and column, from an .xlsx file ("Sheet1, Sheet2,..").


	@file object: A reference to the .xlsx file created by XlsxCreate or XlsxOpen.

	@sheet object: A string with the sheet name.

	@row integer: The row of the shell.

	@column integer: The column of the cell.

	@returns string: Returns the value as string, or None if the cell is empty.

	"""

def XlsxInsertSheet(file):

	"""

	Inserts a new empty sheet in the xlsx_file given.


	@file object: A reference to ".xlsx" file created by XlsxCreate or XlsxOpen.

	@returns integer: Returns 0 on success, or 1 on failure.

	"""

def XlsxMaxSheetCell(file, sheet):

	"""

	Gets the cell with max row-column in the defined sheet, in the defined file.


	@file object: A reference to ".xlsx" file created by XlsxCreate or XlsxOpen.

	@sheet object: A string with the sheet's name.

	@returns object: Returns a list with 2 elements [row, column], or None if the sheet is empty.

	"""

def XlsxOpen(filename):

	"""

	Opens an existing xlsx_file and gets a reference to it. 
	If the file does not exist, it returns None.


	@filename string: The path to the ".xlsx" filename.

	@returns object: Returns a reference to the xlsx_file object.
	If the file does not exist, it returns None.

	"""

def XlsxSave(file, filename):

	"""

	Saves all changes in an opened xlsx_file.


	@file object: A reference to the ".xlsx" file created by XlsxCreate or XlsxOpen.

	@filename object: (optional)The path where the ".xlsx" file will be saved.

	@returns integer: Returns 0 on success, or 1 on failure.

	"""

def XlsxSetCellValue(file, sheet, row, column, value):

	"""

	Sets a value in a cell, in the specified row and column, from sheet ("Sheet1, Sheet2,..") in the selected .xlsx file.


	@file object: A reference to the .xlsx file created by XlsxCreate or XlsxOpen.

	@sheet object: A string with the sheet name.

	@row integer: The row of the shell.

	@column integer: The column of the shell.

	@value object: A string with the setting value.

	@returns integer: Returns 0 on success, or 1 on failure.

	"""

def XlsxSheetsCount(file):

	"""

	Gets the count of sheets in the file given.


	@file object: A reference to an ".xlsx" file created by XlsxCreate or XlsxOpen.

	@returns integer: Returns the number of sheets, or 0 if the xlsx_file is empty.

	"""

def XlsxGetCellValueByName(file, sheet, index):

	"""

	Gets value from cell with index ("A1, B2"), from sheet ("Sheet1, Sheet2,..").


	@file object: A reference to an ".xlsx" file created by XlsxCreate or XlsxOpen.

	@sheet object: The sheet name.

	@index object: The cell index.

	@returns anything: Returns the value as a string, or 0 if the cell is empty.

	"""

def XlsxSetCellValueByName(file, sheet, index, value):

	"""

	Sets a value in a cell with index ("A1, B2"), from sheet ("Sheet1, Sheet2,..") in the file given.


	@file object: A reference to the ".xlsx" file created by XlsxCreate or XlsxOpen.

	@sheet string: A string with the sheet name.

	@index string: A string with the cell index.

	@value string: A string with the setting value.

	@returns integer: Returns 0 on success, or 1 on failure.

	"""

def ClearMonitor():

	"""

	This function clears the monitor output.


	@returns integer: Always returns 1.

	"""

def CloseMonitor():

	"""

	This function closes the monitor window.


	@returns integer: Always returns 1.

	"""

def LinesOfMonitor():

	"""

	This function returns the lines of text in the monitor window.


	@returns integer: Returns an integer describing the number of lines in the monitor window.

	"""

def OpenMonitor(title):

	"""

	This function opens a monitor window.
	It can be used to redirect the output of a script, ie to create log of a job.
	The window that opens features a text editor where the script can print and then you can 
	add your comments and save the text.


	@title string: (optional)The title of the monitor window.

	@returns integer: Always returns 1.

	"""

def OpenMonitorNoEdit(title):

	"""

	This function opens a monitor window with the edit area in readonly mode.
	It can be used to redirect output of a script, ie to create log of a job.
	The window that opens features a text editor where thescript can print but you 
	cannot add your comments to save with the text.
	There is an optional argument, the title of the monitor window.


	@title string: The title of the monitor window.

	@returns integer: Always returns 1.

	"""

def PrintMonitor(txt, r_int, g_int, b_int):

	"""

	This is an output function for script monitoring.
	It is almost identical to the 'print' function with the addition of the three color arguments.


	@txt string: The text to print.

	@r_int integer: Red color integer.

	@g_int integer: Green color integer.

	@b_int integer: Blue color integer.

	@returns integer: Always returns 1.

	"""

def ReadMonitor(line):

	"""

	This function reads a specific line from monitor window. The line is described by its index, 
	the first line having index 0 and the last LinesOfMonitor()-1.


	@line integer: The line number.

	@returns string: Returns the contents of the 'line' or an empty string if the index is less than 0, 
	or greater than the number of lines.

	"""

def SaveMonitor(filename):

	"""

	This function saves the contents of the monitor window in html format.


	@filename string: The filename of the file to be saved.

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def SelectOpenDir(startin):

	"""

	This function allows the user to select a directory for input.


	@startin string: The path of the starting directory.

	@returns string: Returns the selected directory on success, otherwise an empty string.

	"""

def SelectOpenFile(flag, filters):

	"""

	This function opens the file manager and lets the user select one or more files. 
	If the flag is 0 then a single file selection is permitted, while if it is set to 1 
	a multi selection is performed. 
	The user can also type an optional list of file types for filtering.


	@flag integer: If set to 0, a single file selection is allowed.
	If set to 1, a multi file selection is allowed.

	@filters string: (optional)File types for filtering. (See example)

	@returns object: Returns a list containing the file name(s) selected on success.
	On error, or if ESCAPE is pressed, returns an empty list.

	"""

def SelectOpenFileIn(initdir, flag, filters):

	"""

	This function opens the file manager and lets the user select one or more files.
	You can provide the directory in which to start. 
	If you type an empty string ("") or 0 the argument is ignored and the last accessed directory is used instead.
	If flag is 0 then a single file selection is permitted, if it is set to 1 a multi selection is performed.
	The user can also type an optional list of file types for filtering


	@initdir string: The initial directory where the file manager will open.
	If set to ' ', the last accessed directory will be used.

	@flag integer: If set to 0, a single file selection is allowed.
	If set to 1, a multi file selection is allowed.

	@filters string: (optional)File types for filtering. (See example)

	@returns object: Returns a list containing the file name(s) selected, on success.
	On error, or if ESCAPE was pressed, returns an empty list.

	"""

def SelectSaveDir(startin):

	"""

	This function allows the user to select a directory for output.


	@startin string: The path of the starting directory.

	@returns string: Returns the selected directory on success, otherwise an empty string.

	"""

def SelectSaveFile(filter):

	"""

	This function opens the file manager and lets the user select a file name to save. 
	The 'filter' argument is optional and if provided it is used to filter the displayed files.


	@filter string: (optional)File types for filtering. (See example)

	@returns object: Returns a list containing the file name selected on success.
	On error, or if ESCAPE is pressed, returns an empty list.

	"""

def SelectSaveFileIn(init_dir, filter):

	"""

	This function opens the file manager and lets the user select a file name to save.
	The 'init_dir' argument lets you specify the directory in which the file manager will open.
	An empty string ("") or a 0 can be passed to open the file manager in the last accessed directory.
	The 'filter' argument is optional and if provided it is used to filter the displayed files.


	@init_dir string: The folder to start in.

	@filter string: (optional)File types for filtering. (See example)

	@returns object: Returns a list containing the file name selected, on success.
	On error, or if ESCAPE was pressed, returns an empty list.

	"""

def PrintMonitorHtml(txt, r_int, g_int, b_int):

	"""

	This is an output function for script monitoring. It prints html code in 
	monitor window with the addition of the three color arguments.


	@txt string: The html code to print.

	@r_int integer: Red color integer.

	@g_int integer: Green color integer.

	@b_int integer: Blue color integer.

	@returns integer: Always returns 1.

	"""

def SaveMonitorToTxt(filename):

	"""

	This function saves the contents of the monitor window in plain text format.


	@filename string: The path and the filename where the text will be saved.

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def XlsxMergeCells(file, sheet, row1, column1, row2, column2):

	"""

	Merges the specified cells of an ".xlsx" file.


	@file object: The object of the ".xlsx" file.

	@sheet string: The name of the cells' sheet.

	@row1 integer: The row number of the top left cell.

	@column1 integer: The column number of the top left cell.

	@row2 integer: The row number of the bottom right cell.

	@column2 integer: The column number of the bottom right cell.

	@returns object: Returns None on success and raises an exception on failure.

	"""

def XlsxSetCellBorder(file, sheet, row, column, borders, style, color):

	"""

	Set the borders of a cell.


	@file object: The object of the ".xlsx" file.

	@sheet string: The name of the cell's sheet.

	@row integer: The row number of the cell.

	@column integer: The column number of the cell.

	@borders string: The specified border. The accepted values are "left", "right",
	"top", "bottom", and any combination of them by using the "|"
	(e.g. "top|bottom").

	@style string: The style of the line. The accepted values are "dashdot",
	"dashdotdot", "dashed", "dotted", "double", "hair", "medium",
	"mediumdashdot", "mediumdashdotdot", "mediumdashed", "none",
	"thick", "thin", and "slantdashdot".

	@color string: The RGB color of the line in comma separated string.
	(e.g. "100, 100, 100").

	@returns object: Returns None on success and raises an exception on failure.

	"""

def XlsxSetCellBackgroundColor(file, sheet, row, column, color):

	"""

	Sets the background color of a cell.


	@file object: The object of the ".xlsx" file.

	@sheet string: The name of the cell's sheet.

	@row integer: The row number of the cell.

	@column integer: The column number of the cell.

	@color string: The RGB background color of the cell in a comma separated string.
	(e.g. "100, 100, 100").

	@returns object: Returns None on success and raises an exception on failure.

	"""

def XlsxGetSheetName(file, index):

	"""

	Gets the name of a sheet by its index.


	@file object: The object of the ".xlsx" file.

	@index integer: The index of the sheet of the specified file.

	@returns string: Returns the name of the sheet on success and raises an exception on failure.

	"""

def XlsxAdjustRowHeight(file, sheet, row):

	"""

	Adjusts the height of a row.


	@file object: The object of the ".xlsx" file.

	@sheet string: The name of the cell's sheet.

	@row integer: The row number starting from 0.

	@returns object: Returns None on success and raises an exception on failure.

	"""

def XlsxAdjustColumnWidth(file, sheet, column):

	"""

	Adjusts the width of a column.


	@file object: The object of the ".xlsx" file.

	@sheet string: The name of the cell's sheet.

	@column integer: The column number starting from 0.

	@returns object: Returns None on success and raises an exception on failure.

	"""

def XlsxSetCellFontStyle(file, sheet, row, column, style):

	"""

	Sets the font style in a specified cell.


	@file object: The object of the ".xlsx" file.

	@sheet string: The name of the cell's sheet.

	@row integer: The row number of the cell starting from 0.

	@column integer: The column number of the cell starting from 0.

	@style string: The specified font style. The accepted values are "bold", "italic", "underline" 
	and any combination of them by using the symbol "|". (e.g. "bold|italics")

	@returns object: Returns None on success and raises an exception on failure.

	"""

def XlsxAlignCellVertically(file, sheet, row, column, alignment):

	"""

	Aligns vertically a specified cell.


	@file object: The object of the ".xlsx" file.

	@sheet string: The name of the cell's sheet.

	@row integer: The row number of the cell starting from 0.

	@column integer: The column number of the cell starting from 0.

	@alignment string: The alignment type. The accepted values are "top", "bottom" and "center".

	@returns object: Returns None on success and raises an exception on failure.

	"""

def XlsxAlignCellHorizontally(file, sheet, row, column, alignment):

	"""

	Aligns horizontally a specified cell.


	@file object: The object of the ".xlsx" file.

	@sheet string: The name of the cell's sheet.

	@row integer: The row number of the cell starting from 0.

	@column integer: The column number of the cell starting from 0.

	@alignment string: The alignment type. The accepted values are "left", "right" and "center".

	@returns object: Returns None on success and raises an exception on failure.

	"""

def XlsxSetCellFontColor(file, sheet, row, column, color):

	"""

	Sets the font color in a specified cell.


	@file object: The object of the ".xlsx" file.

	@sheet string: The name of the cell's sheet.

	@row integer: The row number of the cell starting from 0.

	@column integer: The column number of the cell starting from 0.

	@color string: The RGB font color of the cell in a comma separated string. (e.g. "100, 100, 100")

	@returns object: Returns None on success and raises an exception on failure.

	"""

def CreateWindowsLinkFile(target, link_file_path, mount_mapping_table):

	"""

	This function creates a Windows Link file (Shortcut) pointing to an arbitrary
	destination. This function is not necessary to be executed in a Windows
	environment: Windows Link files can be created by a Linux running process, and
	are usable in the Windows domain.
	The condition for this interoperability is that the link target is a path that
	is visible from both Windows / non-Windows environments and paths can be 
	converted across environments by doing prefix substitutions (see description of
	mount_mapping_table below).


	@target string: Destination of the link file, i.e. the path where the created
	shortcut will point to. This path is expressed in its native form,
	i.e. it must be a meaningful path in the environment where this
	python function will be executed.

	@link_file_path string: Path where the Windows Link file will be created. The file name 
	provided with this path must have a '.lnk' extension.

	@mount_mapping_table object: (optional)A sequence of utils.MountMapping objects, which will be used for
	transforming the link target path from its native form into one that 
	is usable in the Windows domain.
	If the function is executed in a non Windows environment, a non empty 
	Mount Mapping Table must be available, so that the unix paths can
	be converted into paths that are meaningful in the Windows domain.
	If the function is executed in a Windows environment, there are no
	requirements for such a Mount Mapping Table. However, if the
	generated Link files are to be used in the Unix domain, then an
	appropriately configured Mount Mapping Table is highly recommended.
	If no Mount Mapping Table is provided as argument, then the global
	Mount Mapping Table configured in the ANSA defaults settings is used.

	@returns boolean: This function returns 'True' if the Link file was succesfully created and 'False'
	if the creation failed.

	"""

def SendEmail(fields):

	"""

	Send an email based on the input arguments.


	@fields object: This is a dictionary that contains all inputs necessary for sending the email.
	Available options for the input dictionary are:
	"email agent": The application used for sending the email, e.g. "thunderbird", "outlook" or "no email agent".
	"email agent path": The path to the application,.
	"thunderbird application path": The path to Thunderbird application.
	"outlook application path": The path to the Outlook application.
	"email attachment folder": All files in this folder will be attached to the message.
	"From:": The sender's email address.
	"To:": The recipients' email addresses.
	"Subject:": The subject of the message.
	"Body:": The actual message that will be the body.
	"signature": If you want a signature to be appended to the body.
	"use gui": If you want a GUI to popup. By default this is "no".
	
	In case of a "no email agent" the following options are needed:
	"server name": The outgoing mail server (SMTP), e.g. "smtp.gmail.com"
	"connection security": Connection security, e.g. "None", "SSL", "STARTTLS"
	"authentication type": The authentication method, e.g. "Plain", "Login", "NTLM"
	"port": The port used for the connection, e.g. 465
	
	In case of authentication, you may need to use a username/password with the "Username" and "Password" keys.

	@returns integer: Returns 1 for success or 0 for failure.

	"""

def AddCurveData(curve, coords):

	"""

	This function adds coordinates data to curve. For example: 
	AddCurveData(curve, [(x1,y1), (x2,y2), (x3,y3), ...])


	@curve object: This argument is the created curve.

	@coords object: (optional)This argument is a list of pairs of floats.

	@returns: Returns None always.

	"""

def CreateCurve():

	"""

	This function creates a new curve object.


	@returns: Upon success, it returns a Class object referring to the newly created curve.
	Else, None is returned.

	"""

def DeleteCurve(curve):

	"""

	This function deletes the curve given as argument.
	
	
	


	@curve object: This argument is the curve given to be deleted.

	@returns: Returns None on success,
	        Null otherwise.

	"""

def GetMaterialPalette():

	"""

	This function gets a dictionary with material names and colors as described in palettes.xml or from a hardcoded palette (if not set in xml file). Dictionary has as keys the material type string and as values a list of 3 integers (r, g, b). 
	
	For example:
	{'N/A Material Name': [100, 100, 100], 'Composite': [255, 165, 0], 'Silicon': [208, 238, 238], 'Steel': [70, 130, 180], 'Glass': [177, 211, 231], 'Multi-Material': [255, 0, 255], 'Plastic': [255, 0, 0], 'Aluminium': [0, 128, 0], 'Rubber': [255, 20, 147], 'Magnesium': [255, 215, 0], 'N/A Material Type': [169, 169, 169]}
	


	@returns: On success, returns a dictionary with material type name and rgb values as list of integers.

	"""

def GetCustomAttributePalette(keyword):

	"""

	This function gets a color palette for the attribute given as argument. It returns a dictionary with attribute names and colors as described in palettes.xml, if available. Otherwise, for some cases, it returns a dictionary from a hardcoded palette (cases like: Subsystem, Material, Diff, Status). Dictionary has as keys the attribute names and as values a list of 3 integers (r, g, b). 
	
	For example:
	{'Doors': [105, 65, 225], 'Roof': [255, 127, 0], 'Unused': [255, 255, 205], 'Frontsystem': [0, 139, 139], 'BiW': [178, 34, 34]}


	@keyword string: This argument is the custom attribute keyword for the palette.

	@returns: On success, returns a dictionary with attribute names and rgb values as list of integers.

	"""

def GetGlobalMountMappingTable():

	"""

	This function returns all the Mount Mappings that are currently stored in the
	global Mount Mapping table.


	@returns object: This function return a list of MountMapping objects

	"""

def SetGlobalMountMappingTable(mount_mapping_table):

	"""

	This function sets the Global Mount Mapping Table with the sequence of Mount
	Mappings received as argument.


	@mount_mapping_table object: Sequence of MountMapping objects that will be stored
	in the Global Mount Mapping Table

	@returns: This functions always returns None

	"""

def LaunchLingeringMLWorker(context_dir, cmd, env, dbg):

	"""

	This function launches a lingering ML Toolkit worker process. The command 
	provided by the user will be launched as a process within an ML Toolkit
	environment and its stdin / stdout channels will be exposed over a TCP socket.
	By reading the details stored within the context directory, clients are able
	to connect to this TCP socket and communicate with the worker process.


	@context_dir string: Path where the context holding directory will be
	created. The context holding directory will be set
	as readable only for the user launching the
	lingering worker, and will hold all information
	(e.g. port / authentication token) necessary for a
	client to connect to it.

	@cmd object: A sequence of strings containing the command plus all 
	arguments describing how the lingering worker is to be
	launched.

	@env string: (optional)Provides the name of the ML Toolkit environment, into
	which the lingering workers should be launched.
	Default value: 'consolidated'

	@dbg boolean: (optional)Describes whether debug mode should be employed. If
	True, then the context directory will not be deleted 
	on worker shut down. Also, the log file will include
	more information, that could assist troubleshooting.
	Default value: False

	@returns boolean: Returns True when the launch was successfully initiated.

	"""

class Messenger():

	"""

	Class for handling messages in python scripts.
	Messenger is a unique object (singleton) in the program, every messenger instance points to the same object.

	"""


	def start_buffering():

		"""

		Starts the messenger's buffering. No action if buffering has already started.


		"""


	def stop_buffering():

		"""

		Stops the messenger's buffering. No action if buffering hasn't started.


		"""


	def print(message, format):

		"""

		Prints a text message in ansa info, stdout (and script editor's output).The message can have one of two formats: txt format or html format.


		@message string: The message we want to print.

		@format string: (optional)The message's format.
		Options are:
		-"txt" (default)
		-"html"

		"""


	def echo(mode):

		"""

		This function affects only the printing messages destination, not the buffering functionality.Setting Echo to true, every message will be printed in ANSA Info (or script Editor output) and in stdout.(Default behavior) Setting Echo to false, messages won't be printed in any output, except of script-error messages that will be printed in stdout.


		@mode boolean: The messengers Echo mode.

		"""


	def pyprint_capture(mode):

		"""

		This function affects only the printing messages destination, not the buffering functionality. Setting capture to true (default setting), every call to Python's native print function, will have the data printed both in ANSA Info (or script Editor output) and in stdout, (provided  Echo is also set to true). When seting capture to false, messages will be printed only in stdout, effectively reverting any changes made to Python's native print statement by ANSA.


		@mode boolean: The messenger's capture mode.

		"""


	def get_buffer():

		"""

		Returns a list of strings with all the buffered messages.


		@returns object: A list of strings with all the buffered messages.

		"""


	def clear():

		"""

		This function clears the messenger's buffer.


		"""

class QualityAssurance():

	"""

	QualityAssurance class is a group of methods that can be used to collect statistical data from your program
	This data can be execution times, memory usage or any kind of values.
	The programmer should create one Quality assurance object and use the methods to collect info from the program.
	
	
	A process stands for a block of code. start_process and stop_process declare the limits of the block. 
	A block can contain other blocks and like that a tree struct of blocks can be created. 
	Execution times are wall-times of these blocks of code. 
	
	Each of these processes can contain also a set of values. These values are stored per line. So at a running block the
	programmer can add a line (with a name) and at the current line can add values(with name also).
	
	Also when the output of this mechanism is used for comparison reasons the programmer can add restrictions to set different
	compare rules per value or process.

	"""


	def start_process(process_name, run_if, compare_val, down_limit, up_limit):

		"""

		Declare the start of a QA process.


		@process_name string: The name of the process.

		@run_if boolean: (optional)Condition to start the process.

		@compare_val float: (optional)A custom compare ratio (decimal) for the time of the 
		process (global value if omitted).

		@down_limit float: (optional)A custom down compare limit value for the time of the 
		process (global value if omitted).

		@up_limit float: (optional)A custom upper compare limit value for the time of the 
		process (global value if omitted).

		@returns object: Returns an object that should be used to declare the stop of the block.

		"""


	def stop_process(running_process):

		"""

		Declare the end of a QA process.


		@running_process object: The object that was returned from start_process.

		"""


	def add_new_line(name, run_if):

		"""

		Add a new line on running process.


		@name string: The name of the line.

		@run_if boolean: (optional)Condition to add the line.

		"""


	def add_value(value_name, value, run_if, compare_val, down_limit, up_limit, compare_val_absolute, decimal_places):

		"""

		add a value on the current line.


		@value_name string: The name of the value.

		@value object: The value. Can be float, integer or string.

		@run_if boolean: (optional)Condition to add the value.

		@compare_val float: (optional)A custom compare ratio (decimal) for the current value 
		(global value if omitted).

		@down_limit float: (optional)A custom down compare limit for the current value 
		(global value if omitted).

		@up_limit float: (optional)A custom upper compare limit for the current value 
		(global value if omitted).

		@compare_val_absolute float: (optional)A custom absolute compare limit for the current value 
		(global value if omitted).

		@decimal_places integer: (optional)Number of decimal places for a float value.

		"""


	def start_recording_to_file(record_times_flag, run_if):

		"""

		Start to record the output of the Quality assurance mechanism to a file.


		@record_times_flag boolean: (optional)If false it would ignore the times for the processes.

		@run_if boolean: (optional)Condition to start recording.

		"""


	def stop_recording_to_file(file_name_to_save, run_if):

		"""

		Stop the recording to file and save a Quality assurance txt file.


		@file_name_to_save string: (optional)A file name for the newly created txt file of quality 
		assurance report.

		@run_if boolean: (optional)Condition to run stop recording.

		"""


	def set_default_values(compare_time, compare_double, compare_int, compare_memory, down_limit_time, down_limit_double, down_limit_ints, down_limit_memory, up_limit_time, up_limit_double, up_limit_ints, up_limit_memory, compare_double_absolute, compare_ints_absolute, compare_time_absolute, compare_memory_absolute):

		"""

		Set the deafault compare values for the quality assurance mechanism.


		@compare_time float: (optional)Set the default compare ratio for times.

		@compare_double float: (optional)Set the default compare ratio for floats.

		@compare_int float: (optional)Set the default compare ratio for integers.

		@compare_memory float: (optional)Set the default compare ratio for memory values.

		@down_limit_time float: (optional)Set the default down limit for comparing times.

		@down_limit_double float: (optional)Set the default down limit for comparing floats.

		@down_limit_ints integer: (optional)Set the default down limit for comparing integers.

		@down_limit_memory float: (optional)Set the default down limit for comparing memory values.

		@up_limit_time float: (optional)Set the default upper limit for comparing times.

		@up_limit_double float: (optional)Set the default upper limit for comparing floats.

		@up_limit_ints integer: (optional)Set the default upper limit for comparing integers.

		@up_limit_memory float: (optional)Set the default upper limit for comparing memory values.

		@compare_double_absolute float: (optional)Set the default absolute limit for comparing doubles.

		@compare_ints_absolute integer: (optional)Set the default absolute limit for comparing integers.

		@compare_time_absolute float: (optional)Set the default absolute limit for comparing times.

		@compare_memory_absolute float: (optional)Set the default absolute limit for comparing memory.

		"""


	def add_current_memory_usage_value(value_name_current_memory, run_if, compare_val, down_limit, up_limit):

		"""

		Add as value the current memory usage of the program. 


		@value_name_current_memory string: The name of the value.

		@run_if boolean: (optional)Condition to add the value.

		@compare_val float: (optional)A custom compare ratio (decimal) for current memory value.

		@down_limit float: (optional)A custom down limit for current memory value.

		@up_limit float: (optional)A custom upper limit for current memory value.

		"""


	def add_peak_memory_usage_value(value_name_peak_memory, run_if, compare_val, down_limit, up_limit):

		"""

		Add as value the peak memory usage of the program.


		@value_name_peak_memory string: The name of the value.

		@run_if boolean: (optional)Condition to add the value.

		@compare_val float: (optional)A custom compare ratio (decimal) for current memory 
		value.

		@down_limit float: (optional)A custom down limit for current memory value.

		@up_limit float: (optional)A custom up limit for current memory value.

		"""


	def freeze(freeze_if):

		"""

		Freeze the quality assurance mechanism. All actions are ignored after that.


		@freeze_if boolean: (optional)Condition to freeze the mechanism.

		"""


	def unfreeze(unfreeze_if):

		"""

		Unfreeze the quality assurance mechanism.


		@unfreeze_if boolean: (optional)Condition to unfreeze the mechanism.

		"""


	def start_lap(clock_name, run_if):

		"""

		A clock will start to run and it will stop at stop_lap.The laps have names.When running process is stoped all times of laps will be added as values to the process. The process will have the numer of times a lap was started and the total time of the laps. 


		@clock_name string: The name of the clock.

		@run_if boolean: (optional)Condition to start the lap.

		@returns object: An object that will be given sto stop_lap method.

		"""


	def stop_lap(running_clock):

		"""

		The method to stop a lap.


		@running_clock object: The object that start_lap had returned.

		"""


	def start_lap_on_master(clock_name, run_if):

		"""

		A clock will start to run and it will stop at stop_lap.The laps have names.When the master process is stoped all times of laps will be added as values to the process. The process will have the numer of times a lap was started and the total time of the laps.


		@clock_name string: The name of the clock.

		@run_if boolean: (optional)Condition to start the lap.

		@returns: An object that will be given sto stop_lap method.

		"""

class MountMapping():

	"""

	The objects of this class describe how paths can be converted between their
	Windows and Unix forms. When network storage is visible from both Windows / Linux 
	workstations, these objects describe how the server shares used in the Windows
	domain correspond to the mount paths used in the Linux domain.

	"""


	unix_mount_path = None
	"""
	The mount path which is used for making the same network
	drive visible in the Linux domain.

	"""

	win_server_share = None
	"""
	The server share with which a specific network drive is
	visible in the Windows domain.

	"""

	def __init__(unix_mount_path, win_server_share):

		"""

		Object constructor of the class


		@unix_mount_path string: The mount path which is used for making the same network drive visible in the Linux domain.

		@win_server_share string: The server share with which a specific network drive is
		visible in the Windows domain.

		"""

class LingeringMLInstance():

	"""

	Objects of this class enable the communication with lingering ML Toolkit worker
	instances, by providing access to their stdin / stdout channels.

	"""


	def __init__(path):

		"""


		@path string: Path to the directory that has been used by the launcher
		of lingering ML Toolkit worker instances to store context
		information.

		"""


	def read(timeout):

		"""

		Reads from the lingering ML Toolkit worker instance's stdout channel. A TimeoutError exception is raised, when the timeout expires and no data were read. An IOError exception is raised, when the WebSocket connection was dropped before any data could be read.


		@timeout integer: (optional)Defines the maximum time interval to block, waiting
		for incoming data. 
		Default value: 0 (non-blocking)

		@returns string: Returns string with the data read

		"""


	def write(data):

		"""

		Write to the Lingering ML Toolkit worker instance's stdin channel.


		@data string: Data to be written

		"""


	def has_error():

		"""

		Checks whether the connection is in erroneous state


		@returns boolean: Returns True when an error has occurred.

		"""


	def disconnect():

		"""

		Disconnects from the Lingering ML Toolkit worker instance


		"""

class LingeringMLClient():

	"""

	Objects of this class enable the communication with lingering ML Toolkit worker
	instances using a higher level protocol, compared to LingeringMLInstance or
	BALStreamsCommunicator objects.
	
	Specifically, instead of providing raw access to the stdin / stdout channels of
	the worker instance, in this case it is possible to exchange python objects. 
	Also, message acknowledgement happens behind the scenes so that no messages get
	lost.
	
	In order to use LingeringMLClient, the worker must implement the Server part of
	this protocol.

	"""


	def __init__(endpoint):

		"""


		@endpoint object: An active LingeringMLInstance or BALStreamsCommunicator object

		"""


	def get_msg(timeout):

		"""

		Read a user message from the Lingering ML Toolkit worker. A TimeoutError exception is raised, when the timeout expires and no message was received.


		@timeout integer: Defines the maximum time interval to block, waiting
		for incoming messages. 
		Default value: 0 (non-blocking)

		@returns object: Returns an arbitrary object, sent by the remote end.

		"""


	def send_msg(user_msg):

		"""

		Send a message to the Lingering ML Toolkit worker instance.


		@user_msg object: Arbitrary object to be transmitted to the remote end. Object must be picklable.

		"""


	def close_worker():

		"""

		Signal the remote Lingering ML Toolkit worker instance to shut down.


		"""

class DMHasher():

	"""

	The DMHasher object provides access to the hasing mechanism that is employed for
	the calculation of hashes in DM Objects.

	"""


	def add_dict(string_dict):

		"""

		Inserts a string-to-string dictionary into the hashcalculation.


		@string_dict object: String-to-string dictionary to be added in the
		hash calculation

		"""


	def get_result():

		"""

		Get the hash string according to the data that have beenadded into the hasher thus far.


		@returns string: String with the hashing result

		"""

class BALStreamsCommunicator():

	"""

	Objects of this class enable the communication with processes running within a 
	Beta Apps Launcher (BAL) environment, by providing an interface to their 
	stdin / stdout channels.

	"""


	def __init__(url, auth_token):

		"""


		@url string: URL to the WebSocket service that BAL has 
		opened for the specific process

		@auth_token string: (optional)Authentication Token to be used for authorizing
		the WebSocket connection

		"""


	def read(timeout):

		"""

		Reads from the stdout channel of the BAL process. A TimeoutError exception is raised, when the timeout expires and no data were read. An IOError exception is raised, when the WebSocket connection was dropped before any data could be read.


		@timeout integer: Defines the maximum time interval to block, waiting
		for incoming data.
		Default value: 0 (non-blocking)

		@returns string: Returns string with the data read

		"""


	def write(data):

		"""

		Write to the stdin channel of the BAL process.


		@data string: Data to be written

		"""


	def has_error():

		"""

		Checks whether the connection is in erroneous state


		@returns boolean: Returns True when an error has occurred.

		"""


	def disconnect():

		"""

		Disconnects from the WebSocket interface towards the process stdin / stdout.


		"""

