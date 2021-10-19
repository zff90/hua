def UserWarning(prompt):

	"""
	Deprecated since version 18.0.0. Use function BCMessageWindowCreate instead.

	This function opens a dialog box to show a warning message to the user.


	@prompt string: The warning message.

	@returns integer: Always returns 1.

	"""

	import warnings; warnings.warn("Deprecated since version 18.0.0. Use function BCMessageWindowCreate instead.", DeprecationWarning)

def UserError(prompt):

	"""

	This function opens a dialog box to show an error message to the user.


	@prompt string: The error message.

	@returns integer: Always returns 1.

	"""

def UserInput(title, message):

	"""
	Deprecated since version 18.0.0. Use function BCMessageWindowCreate instead.

	This function opens a dialog box to allow the user input a string.


	@title string: The title.

	@message string: (optional)The message to the user.

	@returns string: Returns a string with the value entered by the user.

	"""

	import warnings; warnings.warn("Deprecated since version 18.0.0. Use function BCMessageWindowCreate instead.", DeprecationWarning)

def UserQuestion(prompt):

	"""
	Deprecated since version 18.0.0. Use function BCMessageWindowCreate instead.

	This function opens a dialog box prompting the user and waits for a response.


	@prompt string: The question text.

	@returns integer: Returns 1 on OK, 0 on Cancel.

	"""

	import warnings; warnings.warn("Deprecated since version 18.0.0. Use function BCMessageWindowCreate instead.", DeprecationWarning)

def BCVBoxCreate(p):

	"""

	Creates a Box in parent p having vertical orientation.
	NOTE: BCVBox is actually a widget not a layout, so for example, it cannot be inserted directly into a BCFrame.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@returns: the created Box with vertical orientation.

	"""

def BCHBoxCreate(p):

	"""

	Creates a Box in parent p having horizontal orientation.
	NOTE: BCHBox is actually a widget not a layout, so for example, it cannot be inserted directly into a BCFrame.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@returns: the created Box with horizontal orientation.

	"""

def BCPushButtonCreate(p, text, funct, data):

	"""

	Creates a new BCPushButton in parent p.


	@p object: the parent widget or layout.

	@text string: the text shown on the button.

	@funct callback: the function that will be called when BCPushButton b is activated.
	See BC_BUTTON_CLICKED_FUNCTION for details.
	integer BC_BUTTON_CLICKED_FUNCTION(b, data)
	The function to be called when the BCButton is clicked.
	Note the difference between click and press. Click means first pressed down and then released 
	when the mouse cursor is inside the button. Press operates when button is pressed down.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	b     object    the BCPushButton, or BCToolButton.
	data  anything  anything that may be required by the function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)anything that may be required in funct.

	@returns: the created BCPushButton.

	"""

def BCToolButtonCreate(p, iconname, label, funct, data):

	"""

	Creates a new BCToolButton with parent p.
	BCToolButtons are usually created inside toolbars. BCToolButtons have not been designed to 
	replace BCPushButtons. With a BCToolButton you can have a button operating with a 
	popupMenu without losing its click function. All properties and functions
	of BCPushButtons are valid in BCToolButtons as well. BCToolButtons also support 
	icon with a text beside.


	@p object: the parent widget or layout.

	@iconname string: the iconname of a PNG file that exists in the images directory.

	@label string: the label of the BCToolButton.

	@funct callback: the function that will be called when BCToolButton b is activated.
	See BC_BUTTON_CLICKED_FUNCTION for details.
	integer BC_BUTTON_CLICKED_FUNCTION(b, data)
	The function to be called when the BCButton is clicked.
	Note the difference between click and press. Click means first pressed down and then released 
	when the mouse cursor is inside the button. Press operates when button is pressed down.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	b     object    the BCPushButton, or BCToolButton.
	data  anything  anything that may be required by the function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)another pointer to anything that may be required in funct.

	@returns: the created BCToolButton.

	"""

def BCToolButtonSetDownArrowEnabled(b, enabled):

	"""

	Function is obsolete. Use BCListViewGetSelectedItem() instead.
	This function is not supported under VR mode.
	


	@b object: the BCToolButton.

	@enabled boolean: set True to show or False to hide the down arrow.

	"""

def BCToolButtonDownArrowEnabled(b):

	"""

	Function is obsolete. Use BCToolButtonIsSideArrowEnabled() instead.
	This function is not supported under VR mode.
	


	@b object: the BCToolButton.

	"""

def BCToolButtonSetPopupIndicator(b, draw):

	"""

	Sets the appearance of BCToolButton b when a popup is used and the down-arrow has not been enabled.
	When popup is used, the appearance of tool button can be seen with a small triangle at the bottom right corner of the BCToolButton.
	This function is not supported under VR mode.
	


	@b object: the BCToolButton.

	@draw boolean: set True to show (the default) or False to hide the popup indicator.

	"""

def BCButtonSetClickedFunction(b, funct, data):

	"""

	Sets the function called when an existing button is pressed.


	@b object: the BCPushButton.

	@funct callback: the function that will be called when BCPushButton b is activated.
	See BC_BUTTON_CLICKED_FUNCTION for details.
	integer BC_BUTTON_CLICKED_FUNCTION(b, data)
	The function to be called when the BCButton is clicked.
	Note the difference between click and press. Click means first pressed down and then released 
	when the mouse cursor is inside the button. Press operates when button is pressed down.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	b     object    the BCPushButton, or BCToolButton.
	data  anything  anything that may be required by the function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)another pointer to anything that may be required in funct.

	"""

def BCButtonSetToggleButton(b, toggle):

	"""

	Makes BCPushButton b a toggle button.
	Toggle buttons are BCPushButtons or BCToolButtons that once pressed, remain pressed until the user depresses them.
	It can be seen as On/Off states.


	@b object: the button as returned by BCPushButtonCreate() or BCToolButtonCreate()

	@toggle boolean: if True, the BCPushButton becomes a toggle button, otherwise it becomes a normal button.
	
	NOTE: Any BCButtonSetClickedFunction() set will be disabled by this function. You should also use BCButtonSetToggledFunction().

	"""

def BCButtonToggle(b):

	"""

	Toggles a toggle BCPushButton b.
	This means that the button's state will change (if button b was pressed it
	depresses it, otherwise it presses it).


	@b object: the toggle button to be toggled.
	NOTE: This function should only be called after a call to BCButtonSetToggleButton().

	"""

def BCButtonIsOn(b):

	"""

	Returns True if the BCPushButton b is toggled, otherwise returns False.


	@b object: the BCPushButton or BCToolButton.

	@returns: True if the button b is toggled, otherwise returns False.

	"""

def BCButtonIsToggleButton(b):

	"""

	Returns True if the BCPushButton b is a toggle button, otherwise(normal button) returns False.


	@b object: the BCPushButton.

	@returns: True if the BCPushButton b is a toggle button, otherwise(normal button) returns False.

	"""

def BCButtonSetOn(b, on):

	"""

	Sets whether toggle button b is on (toggled) or not.
	It is meaningful only for toggling buttons.
	This function is not supported under VR mode.
	


	@b object: the button.

	@on boolean: set this parameter to True for the button to be toggled, or False otherwise.

	"""

def BCButtonSetToggledFunction(b, funct, data):

	"""

	Sets the function that will be called when toggle button b is toggled.
	NOTE: this function should only be called after a call to BCButtonSetToggleButton().


	@b object: the toggle button.

	@funct callback: the function that will be called when toggle button b is toggled.
	See BC_BUTTON_TOGGLED_FUNCTION for details.
	integer BC_BUTTON_TOGGLED_FUNCTION(b, state, data)
	The function to be called when the BCButton is toggled.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	b      object    the BCPushButton, or BCToolButton.
	state  integer   the toggle state information: 1 when the button is on (i.e. toggled); 0 otherwise.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any user data required by function funct.

	"""

def BCButtonSetAllowColorChange(b, allow):

	"""

	Function is not supported. For more info, please contact Customer Service department.
	This function is not supported under VR mode.
	


	@b object: the BCToolButton.

	@allow boolean: set this variable to True if you want the toggled button to become red when pressed or to False (the default) if you do not want a color change to take place.

	"""

def BCButtonSetText(b, text):

	"""

	Sets the text displayed on BCPushButton or BCToolButton b.
	If you have set an icon with BCButtonSetIconFileName(), it will be removed.


	@b object: the button of which the text will be set.

	@text string: the new text.

	"""

def BCButtonSetIconFileName(b, iconname):

	"""

	Sets the icon that is displayed on the button to be the one specified by iconname.
	This allows an icon to be displayed next to the button's label, as well as to change the button's size.


	@b object: the button.

	@iconname string: the iconname of a PNG file that exists in the images directory or the absolute filename of a PNG file.

	"""

def BCButtonAddIconFileName(b, fileName, mode, state):

	"""

	Adds an icon to the button's iconSet that will be displayed when the button is in mode mode and state state.
	This function will operate ONLY on buttons for which an icon file has already been set via BCButtonSetIconFileName() or BCToolButtonCreate().


	@b object: the toggle button.

	@fileName string: the file name of a PNG file that exists in the images directory or the absolute filename of a PNG file, that will be displayed under mode and state.

	@mode integer: the mode for which a pixmap is intended to be used. See BCEnumMode property for more details.
	
	guitk.constants BCEnumMode
	This enum type describes a Button's pixmap or a ListViewItem's mode.
	 - guitk.constants.BCNormalMode
	The user does not interact with the Button or the ListViewItem, but their functionality is available.
	 - guitk.constants.BCDisabledMode
	The user cannot interact with the Button.
	 - guitk.constants.BCActiveMode
	Button: The user mouse cursor is over button or button is pressed (only for ToolButtons).
	 - guitk.constants.BCSelectedMode
	Button: Display the pixmap when the item represented by the icon is selected.
	ListViewItem: The item is selected.

	@state integer: the state for which a pixmap is intended to be used. See BCEnumIconState property for more details.
	
	guitk.constants BCEnumIconState
	This enum describes the state for which a pixmap is intended to be used.
	 - guitk.constants.BCOffState
	Display the pixmap when a toggle button is in an "off" state (unpressed)
	 - guitk.constants.BCOnState
	Display the pixmap when a toggle buttons is in an "on" state (pressed)

	"""

def BCButtonSetPopup(b, pm):

	"""

	Binds a BCMenu pm to the BCPushButton or BCToolButton b.
	This function is not supported under VR mode.
	


	@b object: the button.

	@pm object: the BCMenu.

	"""

def BCButtonRunClickFunction(b):

	"""

	Runs the callback function of the button.
	WARNING: Do not use -1 as a valid return value in your callback function. 
	This return value indicates that the function does not exist.


	@b object: the button whose function we want to activate.

	@returns: the result of the button's clickedFunction or -1 if the function was not set.

	"""

def BCButtonAddManagedWidget(b, w, oddClick, evenClick):

	"""

	This function adds a widget w to a list of widgets that are automatically managed
	when the button b is activated.
	This function operates like the corresponding function of BCCheckBox. Use this function
	if you want, for example, to show/hide a widget using a simple BCPushButton. On first
	button activation, oddClick action will operate, on second evenClick action will operate etc.
	This function is not supported under VR mode.
	


	@b object: the button.

	@w object: the widget to manage.

	@oddClick integer: the action to perform when button b activated odd times. See BCEnumManagedAction property for more details.
	
	guitk.constants BCEnumManagedAction
	This enum type defines the action to be taken. The managed action is used with BCCheckBoxAddManagedWidget for example.
	 - guitk.constants.BCManagedEnable
	enables the widget.
	 - guitk.constants.BCManagedDisable
	disables the widget.
	 - guitk.constants.BCManagedHide
	hides the widget.
	 - guitk.constants.BCManagedShow
	shows the widget.

	@evenClick integer: the action to perform when button b activated even times. See BCEnumManagedAction property for more details.
	
	guitk.constants BCEnumManagedAction
	This enum type defines the action to be taken. The managed action is used with BCCheckBoxAddManagedWidget for example.
	 - guitk.constants.BCManagedEnable
	enables the widget.
	 - guitk.constants.BCManagedDisable
	disables the widget.
	 - guitk.constants.BCManagedHide
	hides the widget.
	 - guitk.constants.BCManagedShow
	shows the widget.

	"""

def BCPushButtonSetFlat(b, f):

	"""

	Makes a button flat or 3D.
	This function is not supported under VR mode.
	


	@b object: the BCPushButton whose flat condition we want to change.

	@f boolean: set this to True if you want the button b to look flat or to False for a 3D look.

	"""

def BCButtonText(b):

	"""

	Returns the label of button b.
	This function is not supported under VR mode.
	


	@b object: the button.

	@returns: the button's label.

	"""

def BCButtonPopup(b):

	"""

	Returns the associated popup menu, or 0 if no popup menu has been set.
	This function is not supported under VR mode.
	


	@b object: the button.

	@returns: the button's menu.

	"""

def BCButtonComboBoxCreate(p, val):

	"""

	Creates a new BCButtonComboBox.
	This function is not supported under VR mode.
	


	@p object: the parent Widget or Layout.

	@val object: a list of strings with which the BCButtonComboBox will be populated.

	@returns: the created BCButtonComboBox.

	"""

def BCButtonComboBoxAddLeftButton(bcomb, button):

	"""

	Adds a user created tool button, at the left side of the BCButtonLineEdit which is contained at the BCButtonComboBox bcomb
	This function is not supported under VR mode.
	


	@bcomb object: the BCButtonComboBox.

	@button object: the Toolbutton which will be added at left side of BCButtonLineEdit.

	"""

def BCButtonComboBoxAddRightButton(bcomb, button):

	"""

	Adds a user created tool button, at the right side of the BCButtonLineEdit which is contained at the BCButtonComboBox bcomb
	This function is not supported under VR mode.
	


	@bcomb object: the BCButtonComboBox.

	@button object: the Toolbutton which will be added at right side of BCButtonLineEdit.

	"""

def BCButtonComboBoxRemoveButton(bcomb, button):

	"""

	Removes a button from the BCButtonComboBox bcomb.
	Removes the button from the BCButtonComboBox's layout, while hiding it. To delete it, use BCDestroyLater() after removing it.
	WARNING: the buttons that are left or right of the removed button will change their index by -1 cause of the remove.
	This function is not supported under VR mode.
	


	@bcomb object: the BCButtonComboBox.

	@button object: the BCToolbutton which will be removed.

	"""

def BCButtonComboBoxGetLeftButtonAtIndex(bcomb, index):

	"""

	Returns a tool button which is located at the left side of the BCButtonLineEdit, which is contained at the BCButtonComboBox bcomb.
	This function is not supported under VR mode.
	


	@bcomb object: the BCButtonComboBox.

	@index integer: the position of button in the left side of BCButtonLineEdit. 
	The button with index 0 is located at the left most edge of the BCButtonLineEdit.

	"""

def BCButtonComboBoxGetRightButtonAtIndex(bcomb, index):

	"""

	Returns a tool button which is located at the right side of the BCButtonLineEdit, which is contained at the BCButtonComboBox bcomb.
	This function is not supported under VR mode.
	


	@bcomb object: the BCButtonComboBox.

	@index integer: the position of button in the right side of BCButtonLineEdit. 
	The button with index 0 is located at the right most edge of the BCButtonLineEdit.

	"""

def BCButtonComboBoxGetButtonLineEditWidget(bcomb):

	"""

	Returns the BCButtonLineEdit which is located in the BCButtonComboBox bcomb.
	This function is not supported under VR mode.
	


	@bcomb object: the BCButtonComboBox.

	"""

def BCButtonGroupCreate(p, title, o):

	"""

	Constructs a box frame with a title at the top able to group buttons.
	The new BCButtonGroup provides a box frame with title in the top, grouping child
	widgets with vertical or horizontal orientation. BCButtonGroup can accept buttons
	as well as widgets. Note that if you insert non-button widgets you cannot apply
	functionality for buttons (for example exclusive property). The default button 
	group inserts buttons with exclusive property off (unless you insert BCRadioButtons). 
	BCButtonGroups with mixed buttons and non-buttons is not recommended.
	WARNING: It is highly recommended not to use in the same BCButtonGroup mixed types of
	buttons such as BCCheckBoxes, BCRadioButtons etc. A BCButtonGroup sets by default
	the exclusive property for a group with BCRadioButtons, but not for any other button type.
	BCButtonGroups with button types other than BCRadioButtons have to set the exclusive
	property if needed, it is by default set to off.
	In a case of a BCButtonGroup with mixed types of buttons (although this is not recommended)
	exclusive property does not work for buttons other than BCRadioButtons
	even if it has been set explicitly.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@title string: a text that will be displayed as the title of the BCButtonGroup.

	@o integer: the child orientation. See BCEnumOrientation property for details.
	
	guitk.constants BCEnumOrientation
	This type is used to signify an object's orientation. Orientation is used with BCButtonGroupCreate for example.
	 - guitk.constants.BCHorizontal
	sets horizontal orientation.
	 - guitk.constants.BCVertical
	sets vertical orientation.

	@returns: the created BCButtonGroup.

	"""

def BCButtonGroupCreateHidden(p, title, o):

	"""

	Creates a BCButtonGroup with hidden frame and title (i.e. add radio buttons 
	explicitly anywhere in the main widget).
	A hidden BCButtonGroup is useful when you want to use the callback functions and 
	properties of the BCButtonGroup, but you don't want it to be visible.
	Create your own BCButtons with parent the widget or layout you want as if the 
	BCButtonGroup didn't exist. Then, add them into the created BCButtonGroup by calling 
	BCButtonGroupInsert().
	WARNING: Is only applicable to buttons.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@title string: the text will not be displayed as the title of the BCButtonGroup.

	@o integer: the child orientation. See BCEnumOrientation property for details.
	
	guitk.constants BCEnumOrientation
	This type is used to signify an object's orientation. Orientation is used with BCButtonGroupCreate for example.
	 - guitk.constants.BCHorizontal
	sets horizontal orientation.
	 - guitk.constants.BCVertical
	sets vertical orientation.

	@returns: the created BCButtonGroup.

	"""

def BCButtonGroupSelected(bg):

	"""

	Returns the selected toggle button from BCButtonGroup bg if exactly one is selected; 
	otherwise returns None.
	WARNING: It is only applicable to buttons.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@returns: the selected toggle button if exactly one is selected; otherwise returns None.

	"""

def BCButtonGroupFind(bg, id):

	"""

	Returns the button from BCButtonGroup bg with the specified identifier id, 
	or None if the button was not found.
	WARNING: It is only applicable to buttons.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@id integer: the identifier of the button.

	@returns: the button with the specified identifier id, or None if the button was not found.

	"""

def BCButtonGroupSetExclusive(bg, exclusive):

	"""

	Sets whether the button group is exclusive.
	If exclusive is set to True, then the buttons in the group are toggled, and to untoggle
	a button you must click on another button in the group. The default value is False.
	WARNING: It is only applicable to buttons. In case of a BCButtonGroup with BCRadioButtons this property is set by default.
	In a BCButtonGroup with button types other than BCRadioButtons (see BCPushButton etc) this property has to be set if needed
	(by default it is not set).
	In a BCButtonGroup with mixed types of buttons (which is not recommended) this property has been set for the BCRadioButtons of the group by default,
	but it is not for any other button type, even if this property has been set explicitly.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@exclusive boolean: set this parameter to True to turn exclusive functionality on, or False to turn it off.

	"""

def BCButtonGroupInsert(bg, button, id):

	"""

	Inserts the button button with the identifier id into the BCButtonGroup bg.
	Buttons are normally inserted into a button group automatically by passing the button group as the parent when the button is constructed. 
	So it is not necessary to manually insert buttons that have this button group as their parent widget. 
	An exception is when you want custom identifiers instead of the default 0, 1, 2, etc., or if you want the buttons to have some other parent. Also, when you create a hidden BCButtonGroup (see BCButtonGroupCreateHidden() )
	The button is assigned the identifier id or an automatically generated identifier.
	It works as follows: If id &gt;= 0, this identifier is assigned. 
	If id == -1 (default), the identifier is equal to the number of buttons in the group. 
	If id is any other negative integer, for instance -2, a unique identifier (negative integer &lt;= -2) is generated. 
	No button has an id of -1.
	WARNING: Is only applicable to buttons.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@button object: the button to insert.

	@id integer: the button identifier (set to -1 for default behaviour).

	"""

def BCButtonGroupRemove(bg, button):

	"""

	Removes the button button from the BCButtonGroup bg. 
	WARNING: Is only applicable to buttons.
	NOTE: Does not destroy the button.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@button object: the button to remove.

	"""

def BCButtonGroupSetButton(bg, id):

	"""

	Sets selected the toggle button (BCToolButton, BCPushButton, BCCheckBox or BCRadioButton) of BCButtonGroup bg with id id. 
	WARNING: It is only applicable to buttons.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@id integer: the identifier of the button to set.

	"""

def BCButtonGroupSetPressedFunction(bg, funct, data):

	"""

	Sets the function that will be called when a button is pressed on BCButtonGroup bg (be carefull this function is not applicable to title's checkbox). 
	Pressed is used for radio buttons. If you have push buttons or check boxes use click function.
	Note the difference between click and press on a button. Click is generated when left mouse is pressed down and then released when the mouse cursor is inside the button. Press is generated when button is pressed down (with left mouse click).
	WARNING: It is only applicable to buttons.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@funct callback: the function that will be called when a button is pressed inside BCButtonGroup bg.
	See BC_BUTTONGROUP_PRESSED_FUNCTION for details.
	integer BC_BUTTONGROUP_PRESSED_FUNCTION(bg, id, data)
	The function to be called when a button is pressed on BCButtonGroup bg.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	bg    object    the BCButtonGroup.
	id    integer   the id of the button activated.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)anything that may be required by function funct.

	"""

def BCButtonGroupSetClickedFunction(bg, funct, data):

	"""

	Sets the function that will be called when a button is clicked on BCButtonGroup bg (be carefull this function is not applicable to title's checkbox). 
	Click is used for push buttons and check boxes. If you have radio buttons use press function instead.
	Note the difference between click and press on a button. Click is generated when left mouse is pressed down and then released when the mouse cursor is inside the button. Press is generated when left mouse button is pressed down.
	WARNING: It is only applicable to buttons.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@funct callback: the function that will be called when a button is clicked inside BCButtonGroup bg.
	See BC_BUTTONGROUP_CLICKED_FUNCTION for details.
	integer BC_BUTTONGROUP_CLICKED_FUNCTION(bg, id, data)
	The function to be called when a button is clicked on BCButtonGroup bg.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	bg    object    the BCButtonGroup.
	id    integer   the id of the button clicked.
	data  anything  anything that may be required by the function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)anything that may be required by function funct.

	"""

def BCButtonGroupCount(bg):

	"""

	Returns the number of Buttons in BCButtonGroup bg. 
	WARNING: Only applicable to buttons.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup bg.

	@returns: the number of buttons in BCButtonGroup bg.

	"""

def BCButtonGroupId(bg, button):

	"""

	Returns the identifier of button button from BCButtonGroup bg. 
	WARNING: Is only applicable to buttons.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@button object: the button whose identifier is required.

	@returns: the identifier of button button from BCButtonGroup bg.

	"""

def BCButtonGroupSetBorderMode(bg, f):

	"""

	Sets the BCButtonGroup bg to be painted without frame if f is BCNoBorder, top frame
	if f is BCTopBorder or full frame mode if f is BCBorder.
	By default a BCButtonGroup has a surrounding frame, with the title being placed on the upper
	frame line. In flat mode (f = BCNoBorder) no frame is shown. In top frame mode (f = BCTopBorder) the right, left
	and bottom frame lines are omitted, and only the thin line at the top is drawn.
	If f is set to any value other than BCBorder, BCNoBorder, BCTopBorder, this function will behave as if BCBorder was set.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@f integer: set this parameter to BCNoBorder for no frame, BCTopBorder for top frame mode, or BCBorder for full frame mode.
	See BCEnumButtonGroupBorderMode property for details.
	
	guitk.constants BCEnumButtonGroupBorderMode
	This enum type is used to indicate the BCButtonGroup's surrounding frame mode.
	 - guitk.constants.BCBorder
	Top, bottom, left, right border.
	 - guitk.constants.BCNoBorder
	No border
	 - guitk.constants.BCTopBorder
	Only top border.
	 - guitk.constants.BCNoBorderNoMargin
	Removes border and margin of BCButtonGroup.

	"""

def BCButtonGroupGetSelectedId(bg):

	"""

	Returns the ID of the selected item of bg, or -1 if no item is selected.
	WARNING: Is only applicable to buttons.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@returns: the ID of the selected item.

	"""

def BCButtonGroupSetCheckable(bg, checkable):

	"""

	Sets whether the BCButtonGroup bg has a checkbox in its title to checkable.
	NOTE: This function has no meaning for hidden BCButtonGroups.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@checkable boolean: this property holds whether the BCButtonGroup bg has a checkbox in its title. If
	this property is True, the BCButtonGroup has a checkbox. If the checkbox is checked
	(which is the default), the BCButtonGroup's children are enabled.

	"""

def BCButtonGroupIsCheckable(bg):

	"""

	Returns True if the BCButtonGroup bg has a checkbox in its title, False otherwise.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@returns: True if the BCButtonGroup bg has a checkbox in its title; otherwise returns False.

	"""

def BCButtonGroupIsChecked(bg):

	"""

	Returns True if the BCButtonGroup's checkbox in its title is checked; otherwise returns False.
	NOTE: Use BCButtonGroupSetCheckable() before calling this function.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@returns: True if the BCButtonGroup's checkbox is checked; otherwise returns False.

	"""

def BCButtonGroupSetToggledFunction(bg, funct, data):

	"""

	Sets the function that will be called when the checkbox in the title of the BCButtonGroup bg is
	toggled.
	NOTE: Use BCButtonGroupSetCheckable() before calling this function!
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@funct callback: the function that will be called when the bg 's checkbox is toggled. 
	See BC_BUTTONGROUP_TOGGLED_FUNCTION for details.
	integer BC_BUTTONGROUP_TOGGLED_FUNCTION(bg, state, data)
	The function to be called when the checkBox on the title of ButtonGroup bg is toggled.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	bg     object    the BCButtonGroup.
	state  integer   the toggle state information: 1 when the checkBox is checked; 0 otherwise.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any user data required by function funct.

	"""

def BCButtonGroupSetChecked(bg, checked):

	"""

	Sets the group box's checkbox in the title value to checked.
	NOTE: Use BCButtonGroupSetCheckable() before calling this function!
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@checked boolean: set this parameter to True to set the check box checked; False otherwise.

	"""

def BCButtonGroupSetTitle(bg, title):

	"""

	Sets the BCButtonGroup's bg title text to title.
	NOTE: This function is not meaningful for hidden BCButtonGroups.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@title string: the new title.

	"""

def BCButtonGroupTitle(bg):

	"""

	Returns the BCButtonGroup's bg title.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@returns: the title of the BCButtonGroup.

	"""

def BCButtonLineEditCreateDouble(p, val):

	"""

	Creates a BCButtonLineEdit that only accepts doubles.
	This function is not supported under VR mode.
	


	@p object: the parent widget.

	@val float: (optional)the double value that will be set to the BCButtonLineEdit.

	@returns: the created BCButtonLineEdit.

	"""

def BCButtonLineEditCreateInt(p, val):

	"""

	Creates a BCButtonLineEdit that only accepts integers.
	This function is not supported under VR mode.
	


	@p object: the parent widget.

	@val integer: (optional)the integer value that will be set to the BCButtonLineEdit.

	@returns: the created BCButtonLineEdit.

	"""

def BCButtonLineEditCreate(p, val):

	"""

	Creates a BCButtonLineEdit that accepts any text.
	This function is not supported under VR mode.
	


	@p object: the parent widget.

	@val string: the string that will be set to the BCButtonLineEdit.

	@returns: the created BCButtonLineEdit.

	"""

def BCButtonLineEditGetText(ble):

	"""

	Returns the text of BCButtonLineEdit ble.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@returns: the text of the BCButtonLineEdit.

	"""

def BCButtonLineEditGetSelectedText(ble):

	"""

	Returns the selected text of BCButtonLineEdit ble or None if nothing is selected.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@returns: the selected text of the BCButtonLineEdit or None if nothing is selected.

	"""

def BCButtonLineEditGetInt(ble):

	"""

	Returns the content of BCButtonLineEdit ble in int format.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@returns: the content of the BCButtonLineEdit in int format.

	"""

def BCButtonLineEditGetDouble(ble):

	"""

	Returns the content of BCButtonLineEdit ble in double format.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@returns: the content of the BCButtonLineEdit in double format.

	"""

def BCButtonLineEditSetText(ble, text):

	"""

	Sets the content of BCButtonLineEdit ble to be the string text.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@text string: the new string that will be displayed in BCButtonLineEdit ble.

	"""

def BCButtonLineEditSetInt(ble, val):

	"""

	Sets the integer value val as the content of BCButtonLineEdit ble.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@val integer: the integer value that will be displayed in BCButtonLineEdit ble.

	"""

def BCButtonLineEditSetDouble(ble, val):

	"""

	Sets the double value val to be the content of BCButtonLineEdit ble.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@val float: the double value that will be displayed in BCButtonLineEdit ble.

	"""

def BCButtonLineEditSetQuestionMarkFunction(ble, funct, data):

	"""

	Sets the function that will be called when a question mark (?) is entered in the BCButtonLineEdit.
	NOTE: If BCButtonLineEditSetF1Function() is not set, when pressing F1 the function funct will be called.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@funct callback: the function that will be called. See BC_LINEEDIT_QUESTIONMARK_FUNCTION for details.
	integer BC_LINEEDIT_QUESTIONMARK_FUNCTION(le, data)
	The function to be called when a questionmark (?) is entered in a BCLineEdit.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	le    object    the BCLineEdit.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by function funct.

	"""

def BCButtonLineEditSetF1Function(ble, funct, data):

	"""

	Sets the function that will be called when F1 key is pressed in the BCButtonLineEdit.
	NOTE: If BCButtonLineEditSetQuestionMarkFunction() is not set, when pressing question mark (?) the function funct will be called.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@funct callback: the function that will be called. See BC_LINEEDIT_F1_FUNCTION for details.
	integer BC_LINEEDIT_F1_FUNCTION(le, data)
	The function to be called when F1 key is pressed in BCLineEdit le.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	le    object    the BCLineEdit.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any user data required by function funct.

	"""

def BCButtonLineEditSetTextChangeFunction(ble, funct, data):

	"""

	Sets the function that will be called when the text changes in the BCButtonLineEdit.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@funct callback: the function that will be called. See BC_LINEEDIT_TEXT_CHANGED_FUNCTION for details.
	integer BC_LINEEDIT_TEXT_CHANGED_FUNCTION(le, text, data)
	The function to be called when the text changes in the BCLineEdit.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	le    object    the BCLineEdit.
	text  string    the current text in the BCLineEdit.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCButtonLineEditSetSelectionChangedFunction(ble, funct, data):

	"""

	Sets the function that will be called when the selection changes in the BCButtonLineEdit.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@funct callback: the function that will be called. See BC_LINEEDIT_SELECTION_CHANGED_FUNCTION for details.
	integer BC_LINEEDIT_SELECTION_CHANGED_FUNCTION(le, data)
	The function to be called when selected text inside a BCLineEdit changes.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	le    object    the BCLineEdit.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCButtonLineEditSetEnterPressedFunction(ble, funct, data):

	"""

	Sets the function that will be called when enter is pressed inside ble.
	If this function returns 1, the default behaviour is completely overridden.
	This means that if you return 0, the accept function of the window that ble belongs, will operate (window may close). If you return 1, the accept will NOT operate and it seems like you pressed a regular key inside BCButtonLineEdit ble.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@funct callback: the function that will be called when enter is pressed. See BC_LINEEDIT_ENTER_PRESSED_FUNCTION for details.
	integer BC_LINEEDIT_ENTER_PRESSED_FUNCTION(le, data)
	The function to be called when enter/return key is pressed inside BCLineEdit le.
	If you return 0, the accept function of the window that le belongs, will
	operate (window may close). If you return 1, the accept will NOT operate and
	it seems like you pressed any regular key inside line edit.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	le    object    the BCLineEdit.
	data  anything  anything that may be required in function.
	
	Return: 0 if you want accept function of window to operate, otherwise return 1.

	@data anything: (optional)any user data required by funct.

	"""

def BCButtonLineEditSetMinMaxLimitInt(ble, minVal, maxVal):

	"""

	Sets the minimum and maximum integer values allowed in a BCButtonLineEdit.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@minVal integer: the minimum value.

	@maxVal integer: the maximum value.

	"""

def BCButtonLineEditSetMinMaxLimitDouble(ble, minVal, maxVal):

	"""

	Sets the minimum and maximum double values allowed in a BCButtonLineEdit.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@minVal float: the minimum value.

	@maxVal float: the maximum value.

	"""

def BCButtonLineEditSelectAll(ble):

	"""

	Selects all the content of a BCButtonLineEdit widget.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	"""

def BCButtonLineEditTakeKeyboard(ble):

	"""

	Takes all the keyboard events from the drawing area and sends them to BCButtonLineEdit ble.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	"""

def BCButtonLineEditSetSizePolicy(ble, sizepolicy_h, sizepolicy_v):

	"""

	Sets the default layout behavior of the widget.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@sizepolicy_h integer: the horizontal size policy. See BCEnumSizePolicy for details.
	
	guitk.constants BCEnumSizePolicy
	This enum type holds the default layout behavior of the widget.
	If there is a BCBoxLayout that manages this widget's children, the size policy specified by that layout is used. If there is no such BCBoxLayout, the result of this function is used.
	 - guitk.constants.BCFixed
	this is the default BCWidget policy. The size hint is the only acceptable alternative, so the widget can never grow or shrink (e.g. the vertical direction of a push button).
	 - guitk.constants.BCMinimum
	the size hint is minimal, and sufficient. The widget can be expanded, but there is no advantage to it being larger (e.g. the horizontal direction of a push button). It cannot be smaller than the size provided by size hint.
	 - guitk.constants.BCMaximum
	the size hint is a maximum. The widget can be shrunk any amount without detriment if other widgets need the space (e.g. a separator line). It cannot be larger than the size provided by size hint.
	 - guitk.constants.BCPreferred
	the size hint is best, but the widget can be shrunk and still be useful. The widget can be expanded, but there is no advantage to it being larger than size hint.
	 - guitk.constants.BCExpanding
	the size hint is a sensible size, but the widget can be shrunk and still be useful. The widget can make use of extra space, so it should get as much space as possible (e.g. the horizontal direction of a slider).
	 - guitk.constants.BCMinimumExpanding
	the size hint is minimal, and sufficient. The widget can make use of extra space, so it should get as much space as possible (e.g. the horizontal direction of a slider).
	 - guitk.constants.BCIgnored
	the size hint is ignored. The widget will get as much space as possible.

	@sizepolicy_v integer: the vertical size policy. See BCEnumSizePolicy for
	details.
	
	guitk.constants BCEnumSizePolicy
	This enum type holds the default layout behavior of the widget.
	If there is a BCBoxLayout that manages this widget's children, the size policy specified by that layout is used. If there is no such BCBoxLayout, the result of this function is used.
	 - guitk.constants.BCFixed
	this is the default BCWidget policy. The size hint is the only acceptable alternative, so the widget can never grow or shrink (e.g. the vertical direction of a push button).
	 - guitk.constants.BCMinimum
	the size hint is minimal, and sufficient. The widget can be expanded, but there is no advantage to it being larger (e.g. the horizontal direction of a push button). It cannot be smaller than the size provided by size hint.
	 - guitk.constants.BCMaximum
	the size hint is a maximum. The widget can be shrunk any amount without detriment if other widgets need the space (e.g. a separator line). It cannot be larger than the size provided by size hint.
	 - guitk.constants.BCPreferred
	the size hint is best, but the widget can be shrunk and still be useful. The widget can be expanded, but there is no advantage to it being larger than size hint.
	 - guitk.constants.BCExpanding
	the size hint is a sensible size, but the widget can be shrunk and still be useful. The widget can make use of extra space, so it should get as much space as possible (e.g. the horizontal direction of a slider).
	 - guitk.constants.BCMinimumExpanding
	the size hint is minimal, and sufficient. The widget can make use of extra space, so it should get as much space as possible (e.g. the horizontal direction of a slider).
	 - guitk.constants.BCIgnored
	the size hint is ignored. The widget will get as much space as possible.

	"""

def BCButtonLineEditSetFixedWidth(ble, pixels):

	"""

	Function is obsolete. Use BCButtonLineEditSetFixedPixelWidth() instead.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@pixels integer: the pixels ble will occupy.

	"""

def BCButtonLineEditSetReadOnly(ble, readOnly):

	"""

	Sets the read-only state of BCButtonLineEdit ble (i.e. if input by the user is allowed).
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit that will be affected.

	@readOnly boolean: set this parameter to True to make ble read only.

	"""

def BCButtonLineEditSetValidator(ble, v):

	"""

	Set the validator for BCButtonLineEdit ble to v.
	NOTE: This function also clears the contents of the BCButtonLineEdit!
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@v integer: the validator type. See BCEnumValidatorType for details.
	
	guitk.constants BCEnumValidatorType
	This enum type defines the types of valid input. It can be used with BCLineEditSetValidator for example.
	 - guitk.constants.BCValidatorNone
	free text input.
	 - guitk.constants.BCValidatorInt
	only integer values are permitted.
	 - guitk.constants.BCValidatorDouble
	double/float values are permitted.

	"""

def BCButtonLineEditGetValidator(ble):

	"""

	Returns the validator type of BCButtonLineEdit ble.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@returns: the validator type of the BCButtonLineEdit. See BCEnumValidatorType for details.
	BCEnumValidatorType: This enum type defines the types of valid input. It can be used with BCLineEditSetValidator for example.
	guitk.constants.BCValidatorNone: free text input.
	guitk.constants.BCValidatorInt: only integer values are permitted.
	guitk.constants.BCValidatorDouble: double/float values are permitted.

	"""

def BCButtonLineEditSetMinLimitInt(ble, minVal):

	"""

	Sets the minimum integer value allowed in a BCButtonLineEdit.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@minVal integer: the minimum value.

	"""

def BCButtonLineEditSetMaxLimitInt(ble, maxVal):

	"""

	Sets the maximum integer value allowed in a BCButtonLineEdit.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@maxVal integer: the maximum value.

	"""

def BCButtonLineEditSetMinLimitDouble(ble, minVal):

	"""

	Sets the minimum double value allowed in a BCButtonLineEdit.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@minVal float: the minimum value.

	"""

def BCButtonLineEditSetMaxLimitDouble(ble, maxVal):

	"""

	Sets the maximum double value allowed in a BCButtonLineEdit.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@maxVal float: the maximum value.

	"""

def BCButtonLineEditSetCursorPosition(ble, pos):

	"""

	Sets the current cursor position for BCButtonLineEdit ble.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@pos integer: the position in the BCButtonLineEdit to set the cursor.

	"""

def BCButtonLineEditGetCursorPosition(ble):

	"""

	Returns the current cursor position for BCButtonLineEdit ble.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@returns: the current cursor position.

	"""

def BCButtonLineEditSetSelection(ble, start, length):

	"""

	Selects text from position start and for length characters.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@start integer: the starting position.

	@length integer: the length of the text to be selected.

	"""

def BCButtonLineEditSetMaxLength(ble, length):

	"""

	Sets the maximum permitted content's length of the BCButtonLineEdit ble.
	If the text is too long, it is truncated to the limit. If truncation occurs any selected text will be deselected, the cursor position is set to 0 and the first part of the string is shown.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@length integer: the maximum permitted content's length.

	"""

def BCButtonLineEditMaxLength(ble):

	"""

	Returns the maximum permitted length of the content.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@returns: the maximum permitted length of the content.

	"""

def BCButtonLineEditClear(ble):

	"""

	Clears the contents of the BCButtonLineEdit.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	"""

def BCButtonLineEditSetAlignment(ble, alignment):

	"""

	Sets the alignment of the BCButtonLineEdit's content.
	By definition, numbers are aligned right while strings are aligned left. Use this function if you want for example to design a BCButtonLineEdit that accepts %, or characters for calculations and you want to align the content to the right to show that this is a number.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@alignment integer: specifies the required alignment. See BCEnumAlignment for details.
	
	guitk.constants BCEnumAlignment
	This enum type is used to describe alignment. It contains horizontal and vertical flags. Alignment is used with BCGridLayoutAddMultiCellWidget for example.
	NOTE: You can use at most one horizontal and one vertical flag at a time.
	 - guitk.constants.BCAlignAuto
	aligns according to the language. Left for most, right for Arabic and Hebrew.
	 - guitk.constants.BCAlignLeft
	aligns with the left edge.
	 - guitk.constants.BCAlignRight
	aligns with the right edge.
	 - guitk.constants.BCAlignHCenter
	centers horizontally in the available space.
	 - guitk.constants.BCAlignJustify
	justifies the text in the available space.
	 - guitk.constants.BCAlignTop
	aligns with the top.
	 - guitk.constants.BCAlignBottom
	aligns with the bottom.
	 - guitk.constants.BCAlignVCenter
	centers vertically in the available space.
	 - guitk.constants.BCAlignCenter
	centers in both dimensions (vertically and horizontally).
	 - guitk.constants.BCAlignHorizontal_Mask
	horizontal mask.
	 - guitk.constants.BCAlignVertical_Mask
	vertical mask.
	 - guitk.constants.BCAlignVJustify
	Justifies the text vertically in the available space.

	"""

def BCButtonLineEditValidate(ble):

	"""

	Validates the input of BCButtonLineEdit ble about minimum and maximum value.
	ble is validated if it is created with BCButtonLineEditCreateInt()  or BCButtonLineEditCreateDouble(); otherwise returns 0.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@returns: 1 if the value entered is a valid value, i.e., between minimum and maximum values (if any). In case value is not valid or ble accepts any text, 0 is returned.

	"""

def BCButtonLineEditMaxLimitDouble(ble):

	"""

	Returns the maximum double value allowed in the BCButtonLineEdit ble.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@returns: the maximum double value allowed in a BCButtonLineEdit.

	"""

def BCButtonLineEditMinLimitDouble(ble):

	"""

	Returns the minimum double value allowed in the BCButtonLineEdit ble.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@returns: the minimum double value allowed in a BCButtonLineEdit.

	"""

def BCButtonLineEditSetDecimals(ble, numDecimals):

	"""

	Sets the number of decimal digits to validate in a BCButtonLineEdit which accepts only  doubles.
	NOTE: The value set by this function will affect the number of digits that can be shown into a BCButtonLineEdit.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@numDecimals integer: the number of decimal digits to validate.

	"""

def BCButtonLineEditDecimals(ble):

	"""

	Returns the number of decimal digits to validate in a BCButtonLineEdit which accepts only  doubles.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@returns: the number of decimal digits to validate if BCButtonLineEdit accepts doubles ; -1 in case BCButtonLineEdit accepts any text or integers.

	"""

def BCButtonLineEditApplyValidator(ble):

	"""

	Applies the validator (if any) of BCButtonLineEdit ble.
	If the BCButtonLineEdit has not any validator set, i.e. it accepts any text, this function does nothing.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	"""

def BCButtonLineEditInsertText(ble, text):

	"""

	Deletes any selected text and inserts text in cursor's position.
	It also validates the result. If it is valid, it sets it as the new contents of the BCButtonLineEdit.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@text string: the inserted text.

	"""

def BCButtonLineEditSetAddItemsToPopupMenu(ble, funct, data):

	"""

	Adds custom menu items or sub-popups above the default menu items of BCButtonLineEdit's right-mouse-click popup menu.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@funct callback: the callback function which must be called to create the custom menu.
	See BC_LINEEDIT_ADD_ITEMS_TO_POPUPMENU_FUNCTION for details.
	integer BC_LINEEDIT_ADD_ITEMS_TO_POPUPMENU_FUNCTION(le, popup, data)
	The function to add items to the popup on a right mouse click over the le BCLineEdit.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	le     object    the BCLineEdit.
	popup  object    the BCLineEdit's BCMenu with the default menu items to which you want to add extra items.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any user data required by function funct.

	"""

def BCButtonLineEditAddLeftButton(ble, button):

	"""

	Adds a tool button, which must be created by the developer beforehand, to the left side of BCButtonLineEdit.
	\warning: The button must be created with parent the current BCButtonLineEdit and must be a BCToolButton.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@button object: the button that will be added to the left side of BCButtonLineEdit.

	"""

def BCButtonLineEditAddRightButton(ble, button):

	"""

	Adds a tool button, which must be created by the developer beforehand, to the right side of BCButtonLineEdit.
	\warning: The button must be created with parent the current BCButtonLineEdit and must be a BCToolButton.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@button object: the button that will be added to the right side of BCButtonLineEdit.

	"""

def BCButtonLineEditGetLeftButtonAtIndex(ble, index):

	"""

	Returns a button which is located at the left side of BCButtonLineEdit.
	\warning: The button must be created with parent the current BCButtonLineEdit and must be a BCToolButton.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@index integer: the serial position of the button at the left side of BCButtonLineEdit. The button with 0 index is the button which is located at the left edge of the BCButtonLineEdit.

	"""

def BCButtonLineEditGetRightButtonAtIndex(ble, index):

	"""

	Returns a button which is located at the right side of BCButtonLineEdit.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@index integer: the serial position of button at the right side of BCButtonLineEdit. The button with 0 index is the button which is located at the right edge of the BCButtonLineEdit.

	"""

def BCButtonLineEditRemoveButton(ble, button):

	"""

	Removes a button from the BCButtonLineEdit ble.
	WARNING: the buttons that are left or right of the removed button will change their index by -1 cause of the remove.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@button object: the BCToolbutton which will be removed.

	"""

def BCCalculatorCreate(p):

	"""

	Creates a scientific calculator which can be connected to a BCLineEdit and transfer the result of the calculation on it.
	WARNING: the return value is a BCFrame.
	This function is not supported under VR mode.
	


	@p object: the parent of the BCCalculator, BCWindow recommended.

	@returns: the created BCCalculator as a BCFrame.

	"""

def BCCalculatorGetResult(calc):

	"""

	Returns the result of a BCCalculator.
	This function is not supported under VR mode.
	


	@calc object: the BCCalculator.

	@returns: the string of the calculated result.

	"""

def BCCalculatorSetExpression(calc, expr):

	"""

	Sets an expression as text to expression area of a BCCalculator.
	This function is not supported under VR mode.
	


	@calc object: the BCCalculator.

	@expr string: the string of the expression.

	"""

def BCCalculatorConnectWithButtonLineEdit(calc, ble):

	"""

	With this function you can connect a BCCalculator to a BCButtonLineEdit.
	By pushing the transfer button a copy of the calculated result is set as text at the result area of the BCCalculator.
	This function is not supported under VR mode.
	


	@calc object: the BCCalculator.

	@ble object: the BCButtonLineEdit.

	"""

def BCCheckBoxCreate(p, text):

	"""

	Creates a BCCheckBox with parent p and a text label text on the right.


	@p object: the parent widget or layout.

	@text string: the text that will be displayed.

	@returns: the created BCCheckBox.

	"""

def BCCheckBoxSetText(cb, text):

	"""

	Sets the text label of BCCheckBox cb to be text.


	@cb object: the BCCheckBox.

	@text string: the new text for cb.

	"""

def BCCheckBoxIsChecked(cb):

	"""

	Returns True if the BCCheckBox is checked or False otherwise.


	@cb object: the BCCheckBox.

	@returns: True if the cb is checked or False otherwise.

	"""

def BCCheckBoxSetChecked(cb, check):

	"""

	Sets BCCheckBox cb to be checked or unchecked depending on the value of check.
	If a toggle function was set to cb, it will be called only if the new check state is different from the current one.


	@cb object: the BCCheckBox.

	@check boolean: set this parameter to True to check cb or False to uncheck it.

	"""

def BCCheckBoxSetCheckedNoCallBack(cb, check):

	"""

	Sets BCCheckBox cb to be checked or unchecked depending on the value of check without calling callback.


	@cb object: the BCCheckBox.

	@check boolean: set this parameter to True to check cb or False to uncheck it.

	"""

def BCCheckBoxToggle(cb):

	"""

	Toggle BCCheckBox cb (i.e. change state).


	@cb object: the BCCheckBox.

	"""

def BCCheckBoxSetToggledFunction(cb, funct, data):

	"""

	Set the function funct that will be called when the BCCheckBox cb is toggled.


	@cb object: the BCCheckBox.

	@funct callback: the function that will be called when the BCCheckBox cb is toggled. See
	BC_CHECKBOX_TOGGLED_FUNCTION for details.
	integer BC_CHECKBOX_TOGGLED_FUNCTION(cb, state, data)
	The function to be called when BCCheckBox cb is toggled.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	cb     object    the BCCheckBox.
	state  integer   the toggle state information: 1 when the checkBox is checked; 0 otherwise.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct, or None.

	"""

def BCCheckBoxAddManagedWidget(cb, w, onCheck, onUnCheck):

	"""

	This function adds a widget w to a list of widgets that are automatically managed
	when the BCCheckBox cb is checked or unchecked. 
	The list of possible actions
	are: enable, disable, hide and show. Different actions can be connected 
	to the checked/unchecked state of the BCCheckBox cb.


	@cb object: the BCCheckBox.

	@w object: the widget to manage.

	@onCheck integer: the action to perform when BCCheckBox cb has been checked. See BCEnumManagedAction property for more details.
	
	guitk.constants BCEnumManagedAction
	This enum type defines the action to be taken. The managed action is used with BCCheckBoxAddManagedWidget for example.
	 - guitk.constants.BCManagedEnable
	enables the widget.
	 - guitk.constants.BCManagedDisable
	disables the widget.
	 - guitk.constants.BCManagedHide
	hides the widget.
	 - guitk.constants.BCManagedShow
	shows the widget.

	@onUnCheck integer: the action to perform when BCCheckBox cb has been unchecked. See BCEnumManagedAction property for more details.
	
	guitk.constants BCEnumManagedAction
	This enum type defines the action to be taken. The managed action is used with BCCheckBoxAddManagedWidget for example.
	 - guitk.constants.BCManagedEnable
	enables the widget.
	 - guitk.constants.BCManagedDisable
	disables the widget.
	 - guitk.constants.BCManagedHide
	hides the widget.
	 - guitk.constants.BCManagedShow
	shows the widget.

	"""

def BCCheckBoxText(cb):

	"""

	Returns the label of the check button


	@cb object: the BCCheckBox whose label we want to get.

	@returns: the BCCheckButton's label

	"""

def BCComboBoxCreate(p, val):

	"""

	Creates a ComboBox with val as the list of options.


	@p object: the parent Widget or Layout.

	@val object: a list of strings with which the BCComboBox will be populated.

	@returns: the created ComboBox.

	"""

def BCComboBoxCurrentText(box):

	"""

	Returns the current text of BCComboBox box, or None if box is empty.


	@box object: the BCComboBox.

	@returns: the current text of BCComboBox box, or None if box is empty.

	"""

def BCComboBoxCurrentItem(box):

	"""

	Returns the index of the current item of BCComboBox box.


	@box object: the BCComboBox.

	@returns: the index of the current item of BCComboBox box.

	"""

def BCComboBoxSetActivatedFunction(box, funct, data):

	"""

	Sets the function that will be called when BCComboBox box is activated.
	If you have editable combo boxes use BCComboBoxSetActivatedTextFunction() instead.


	@box object: the BCComboBox.

	@funct callback: the function that will be called when BCComboBox box is activated.
	See BC_COMBOBOX_ACTIVATED_FUNCTION for details.
	integer BC_COMBOBOX_ACTIVATED_FUNCTION(combo, index, data)
	The function to be called when BCComboBox combo is activated.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	combo  object    the BCComboBox.
	index  integer   the index of the activated item.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by function funct. If data is not required, it should be set to None.

	"""

def BCComboBoxSetActivatedTextFunction(box, funct, data):

	"""

	Sets the function that will be called when BCComboBox box is activated. Use this function for editable combo boxes.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@funct callback: the function that will be called when BCComboBox box is activated. 
	See BC_COMBOBOX_ACTIVATED_TEXT_FUNCTION for details.
	integer BC_COMBOBOX_ACTIVATED_TEXT_FUNCTION(combo, text, data)
	The function to be called when ComboBox combo is activated. Use this function for editable combo boxes.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	combo  object    the BCComboBox.
	text   string    the text of the activated item.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by function funct.

	"""

def BCComboBoxSetTextChangedFunction(box, funct, data):

	"""

	Sets the function that will be called when the text changes in the BCComboBox.
	This function will operate only if combo box is editable.
	This function is not supported under VR mode.
	


	@box object: the ComboBox.

	@funct callback: the function that will be called when text changes.
	See BC_COMBOBOX_TEXT_CHANGED_FUNCTION for details.
	integer BC_COMBOBOX_TEXT_CHANGED_FUNCTION(combo, text, data)
	The function to be called when the text changes in the BCComboBox combo.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	combo  object    the BCComboBox.
	text   string    the current text in the BCComboBox.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCComboBoxSetAboutToPopupFunction(box, funct, data):

	"""

	Sets the function that will be called just before the popup opens in the BCComboBox.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@funct callback: the function that will be called when the popup opens. 
	See BC_COMBOBOX_POPUP_FUNCTION for details.
	integer BC_COMBOBOX_POPUP_FUNCTION(combo, data)
	The function to be called when the popup opens in the BCComboBox combo.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	combo  object    the BCComboBox.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCComboBoxSetPopupFunction(box, funct, data):

	"""

	Sets the function that will be called when the popup opens in the BCComboBox.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@funct callback: the function that will be called when the popup opens. 
	See BC_COMBOBOX_POPUP_FUNCTION for details.
	integer BC_COMBOBOX_POPUP_FUNCTION(combo, data)
	The function to be called when the popup opens in the BCComboBox combo.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	combo  object    the BCComboBox.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCComboBoxSetCurrentIndexChangedFunction(box, funct, data):

	"""

	Sets the function to be called when the current index of BCComboBox box changes.
	NOTE: The function set by this function, in contrast with the function set with BCComboBoxSetActivatedFunction, will
	be called either through user interaction or programmatically! If you change the current index programmatically and you
	do not wish the callback to be called, block callback functions by calling BCBlockCallBackFunctions.
	NOTE: In case both BC_COMBOBOX_CURRENT_INDEX_CHANGED_FUNCTION and BC_COMBOBOX_ACTIVATED_FUNCTION are set
	for the same BCComboBox and the current index changes, BC_COMBOBOX_CURRENT_INDEX_CHANGED_FUNCTION will be called first and then
	the BC_COMBOBOX_ACTIVATED_FUNCTION.


	@box object: the BCComboBox.

	@funct callback: the function that will be called when the current index of the BCComboBox changes. See
	BC_COMBOBOX_CURRENT_INDEX_CHANGED_FUNCTION for details.
	integer BC_COMBOBOX_CURRENT_INDEX_CHANGED_FUNCTION(combo, index, data)
	The function to be called when the current index of BCComboBox combo changes either through user interaction or programmatically.
	
	Arguments
	
	combo  object    the BCComboBox.
	index  integer   the new current index. If combo becomes empty index will be -1.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCComboBoxSetCurrentItem(box, index):

	"""

	Sets the current item of the BCComboBox to be the item with index index.
	WARNING: this function doesn't trigger the activated callback set by the user.


	@box object: the BCComboBox.

	@index integer: the index of the item which will be set to current.

	"""

def BCComboBoxInsertItem(box, text, index):

	"""

	Inserts an item with text text, at position index. The item will be appended if index is negative.


	@box object: the BCComboBox.

	@text string: the text that will be inserted.

	@index integer: the index at which text will be inserted (-1 to append).

	"""

def BCComboBoxInsertItemIconFileName(box, fileName, text, index):

	"""

	Inserts an item with text text, at position index, with a pixmap on the left of text.
	The item will be appended if index is negative. Note that the editable property of the text is not affected.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@fileName string: the absolute path of a PNG file.

	@text string: the text that will be inserted.

	@index integer: the index at which text will be inserted (-1 to append).

	"""

def BCComboBoxInsertStrList(box, list, numStrings, index):

	"""

	Inserts the list of strings list at position index in the BCComboBox box.
	
	The numStrings argument is the number of strings.


	@box object: the BCComboBox.

	@list object: the list of strings that will be inserted.

	@numStrings integer: the number of strings in list.

	@index integer: the index at which list will be inserted (-1 to append).

	"""

def BCComboBoxAddManagedWidget(box, w, on, off, index):

	"""

	This function adds a widget w to a list of widgets that are automatically managed when BCComboBox box is activated.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@w object: the widget that will be managed by the box.

	@on integer: defines what will happen to w when index is selected.
	See BCEnumManagedAction property for details.
	
	guitk.constants BCEnumManagedAction
	This enum type defines the action to be taken. The managed action is used with BCCheckBoxAddManagedWidget for example.
	 - guitk.constants.BCManagedEnable
	enables the widget.
	 - guitk.constants.BCManagedDisable
	disables the widget.
	 - guitk.constants.BCManagedHide
	hides the widget.
	 - guitk.constants.BCManagedShow
	shows the widget.

	@off integer: defines what will happen to w when any item of box is selected except index. 
	See BCEnumManagedAction property for details.
	
	guitk.constants BCEnumManagedAction
	This enum type defines the action to be taken. The managed action is used with BCCheckBoxAddManagedWidget for example.
	 - guitk.constants.BCManagedEnable
	enables the widget.
	 - guitk.constants.BCManagedDisable
	disables the widget.
	 - guitk.constants.BCManagedHide
	hides the widget.
	 - guitk.constants.BCManagedShow
	shows the widget.

	@index integer: the number of the item when the on action will be performed on w.

	"""

def BCComboBoxSetEditable(box, editable):

	"""

	Sets whether the combobox is editable.
	When a combobox becomes editable, when click on it, a line edit appears on its first line, so it is possible to add new items by simply entering text into that line edit.
	NOTE: By default a BCComboBox is NOT editable.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@editable boolean: set this parameter to True to make box editable; False otherwise.

	"""

def BCComboBoxSetLineEdit(box, le):

	"""

	Sets the BCLineEdit to use le instead of the current line edit.
	NOTE: This function should be used by editable BCComboBoxes only.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@le object: the BCLineEdit.

	"""

def BCComboBoxGetLineEdit(box):

	"""

	Returns the BCLineEdit, or 0 if there is no BCLineEdit.
	Only editable BCComboBoxes have a BCLineEdit.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@returns: the BCLineEdit of box.

	"""

def BCComboBoxGetListBox(box):

	"""

	Returns the listBox of the BCComboBox box, or 0 if box has no listBox.
	If the BCComboBox is editable then it is assured that it has a listbox. If it is not editable,
	the listbox existence depends on the window style used.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@returns: the listBox of box.

	"""

def BCComboBoxSetDuplicatesEnabled(box, enabled):

	"""

	Allows or forbids duplicates if enabled is True or False respectively. It has sense only for editable BCComboBoxes (default  False).
	WARNING: It is safer to call this function before adding any item to box.
	NOTE: Cannot forbid duplicates that are inserted programmatically.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@enabled boolean: set this parameter to True to enable duplicates, or False otherwise.

	"""

def BCComboBoxSetAutoCompletion(box, enabled):

	"""

	Sets whether auto-completion is enabled.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@enabled boolean: set this parameter to True to enable auto completion, or False otherwise.

	"""

def BCComboBoxContainsLabel(box, label):

	"""

	Returns 1 if label is contained in box, or 0 otherwise.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@label string: the string that will be checked.

	@returns: 1 if label is contained in box, or 0 otherwise.

	"""

def BCComboBoxMaxCount(box):

	"""

	This function returns the maximum number of items allowed in the combobox.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@returns: the maximum number of items allowed in the combobox.

	"""

def BCComboBoxRemoveItem(box, index):

	"""

	Removes the item at index index of BCComboBox box.
	NOTE: Removing the current item does not trigger the BCComboBox callback functions.


	@box object: the BCComboBox.

	@index integer: the index of the combobox item to remove.

	"""

def BCComboBoxClear(box):

	"""

	Removes all combobox items.


	@box object: the BCComboBox.

	"""

def BCComboBoxCount(box):

	"""

	Returns the number of items in the combobox.


	@box object: the BCComboBox.

	@returns: the number of items in the combobox.

	"""

def BCComboBoxGetText(box, index):

	"""

	Returns the item's text of BCComboBox box at position index, or None if index does not exist.


	@box object: the BCComboBox.

	@index integer: the index of the combobox item to remove.

	@returns: the text at position index, or None if item is not a string or index does not exist.

	"""

def BCComboBoxSetSizePolicy(box, sizepolicy_h, sizepolicy_v):

	"""

	Sets the default layout behavior of the widget.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@sizepolicy_h integer: the horizontal size policy. See BCEnumSizePolicy for details.
	
	guitk.constants BCEnumSizePolicy
	This enum type holds the default layout behavior of the widget.
	If there is a BCBoxLayout that manages this widget's children, the size policy specified by that layout is used. If there is no such BCBoxLayout, the result of this function is used.
	 - guitk.constants.BCFixed
	this is the default BCWidget policy. The size hint is the only acceptable alternative, so the widget can never grow or shrink (e.g. the vertical direction of a push button).
	 - guitk.constants.BCMinimum
	the size hint is minimal, and sufficient. The widget can be expanded, but there is no advantage to it being larger (e.g. the horizontal direction of a push button). It cannot be smaller than the size provided by size hint.
	 - guitk.constants.BCMaximum
	the size hint is a maximum. The widget can be shrunk any amount without detriment if other widgets need the space (e.g. a separator line). It cannot be larger than the size provided by size hint.
	 - guitk.constants.BCPreferred
	the size hint is best, but the widget can be shrunk and still be useful. The widget can be expanded, but there is no advantage to it being larger than size hint.
	 - guitk.constants.BCExpanding
	the size hint is a sensible size, but the widget can be shrunk and still be useful. The widget can make use of extra space, so it should get as much space as possible (e.g. the horizontal direction of a slider).
	 - guitk.constants.BCMinimumExpanding
	the size hint is minimal, and sufficient. The widget can make use of extra space, so it should get as much space as possible (e.g. the horizontal direction of a slider).
	 - guitk.constants.BCIgnored
	the size hint is ignored. The widget will get as much space as possible.

	@sizepolicy_v integer: the vertical size policy. See BCEnumSizePolicy for details.
	
	guitk.constants BCEnumSizePolicy
	This enum type holds the default layout behavior of the widget.
	If there is a BCBoxLayout that manages this widget's children, the size policy specified by that layout is used. If there is no such BCBoxLayout, the result of this function is used.
	 - guitk.constants.BCFixed
	this is the default BCWidget policy. The size hint is the only acceptable alternative, so the widget can never grow or shrink (e.g. the vertical direction of a push button).
	 - guitk.constants.BCMinimum
	the size hint is minimal, and sufficient. The widget can be expanded, but there is no advantage to it being larger (e.g. the horizontal direction of a push button). It cannot be smaller than the size provided by size hint.
	 - guitk.constants.BCMaximum
	the size hint is a maximum. The widget can be shrunk any amount without detriment if other widgets need the space (e.g. a separator line). It cannot be larger than the size provided by size hint.
	 - guitk.constants.BCPreferred
	the size hint is best, but the widget can be shrunk and still be useful. The widget can be expanded, but there is no advantage to it being larger than size hint.
	 - guitk.constants.BCExpanding
	the size hint is a sensible size, but the widget can be shrunk and still be useful. The widget can make use of extra space, so it should get as much space as possible (e.g. the horizontal direction of a slider).
	 - guitk.constants.BCMinimumExpanding
	the size hint is minimal, and sufficient. The widget can make use of extra space, so it should get as much space as possible (e.g. the horizontal direction of a slider).
	 - guitk.constants.BCIgnored
	the size hint is ignored. The widget will get as much space as possible.

	"""

def BCComboBoxLabelIndex(box, label):

	"""

	Returns the index of the first combobox item of BCComboBox box having as label label.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@label string: the string that will be searched.

	@returns: the index of the first combobox item; -1 if it is not found.

	"""

def BCName(w):

	"""

	Returns the name of w. 
	NOTE: Do not use this function for BCListViewItems.
	This function is not supported under VR mode.
	


	@w object: the widget whose name is returned.

	@returns: the name of w.

	"""

def BCCaption(w):

	"""

	Returns the caption name of w as set during its construction, e.g. the title of a window.
	
	It is not applicable to BCListViewItems, layouts, BCSpacers e.t.c. and it is meaningful only for windows.
	This function is not supported under VR mode.
	


	@w object: the widget whose caption name is returned.

	@returns: the caption name of w.

	"""

def BCSetCaption(w, caption):

	"""

	Sets the caption for widget w.
	It is not applicable to BCListViewItems, layouts, BCSpacers e.t.c. and it is meaningful only for windows.
	This function is not supported under VR mode.
	


	@w object: the widget.

	@caption string: the caption.

	"""

def BCSetName(w, name):

	"""

	Sets the name for widget w.
	This function is not supported under VR mode.
	


	@w object: the widget whose name will be set by this function.

	@name string: the name to set.

	"""

def BCParent(w):

	"""

	Returns the parent of widget w.
	NOTE: Do not use this function for BCListViewItems etc.
	This function is not supported under VR mode.
	


	@w object: the widget whose parent is returned.

	@returns: the parent widget of widget w.

	"""

def BCSetEnabled(w, enabled):

	"""

	Sets whether widget w is enabled or not. Widgets that are not enabled cannot be edited by the user.


	@w object: the widget.

	@enabled boolean: set this parameter to True to enable widget w, or to False to disable it.

	"""

def BCIsEnabled(w):

	"""

	Checks if widget w is enabled or not. Widgets that are not enabled cannot be edited by the user.


	@w object: the widget.

	@returns: True if the widget w is enabled or False otherwise.

	"""

def BCHide(w):

	"""

	Hides the widget w.
	NOTE: if you want to hide a BCPopupMenu use BCPopupMenuClose() instead of BCHide()


	@w object: the widget to hide.

	"""

def BCShow(w):

	"""

	Shows the widget w if it was hidden.
	 IMPORTANT: If w is a top-level widget (e.g. BCWindow or BCWizard), the code execution will 'wait' at this function, until w closes, either by 'OK' or 'Cancel'. 
	 If you have created the window with BCOnExitDestroy, it will be DESTROYED after the BCShow() execution, together with all its child widgets. 
	 Thus you MUST NOT try to access data through those widgets (e.g. BCLineEditGetText(le) where le is a BCLineEdit created inside w).


	@w object: the widget to show.

	"""

def BCIsShown(w):

	"""

	Returns True if widget w is shown, otherwise False.
	Note the difference between BCIsShown() and BCIsVisible().
	BCIsVisible() will test whether a widget is currently visible or not. 
	BCIsShown() returns False if BCHide() was called for this particular widget and BCShow() has not been called yet. Otherwise, returns True. Thus you may have a widget which is shown but not visible if, for example, you have called BCHide() for its parent.


	@w object: the widget that will be tested whether it is shown.

	@returns: True if w is shown or False if it is not.

	"""

def BCGetBackgroundColor(w):

	"""

	Returns the RGB color values of the background color of widget w.
	This function is not supported under VR mode.
	


	@w object: the widget.

	@returns: A tuple with the [int r, int g, int b] background color values of the widget w.

	"""

def BCGetForegroundColor(w):

	"""

	Returns the RGB color values of the foreground color of widget w.
	This function is not supported under VR mode.
	


	@w object: the widget.

	@returns: A tuple with the [int r, int g, int b] foreground color values of the widget w.

	"""

def BCSetBackgroundColor(w, r, g, b):

	"""

	Sets the RGB values for the background color of widget w to be r, g and b.
	NOTE: This function may not work for certain widgets under some styles.
	This function is not supported under VR mode.
	


	@w object: the widget whose background color will be set.

	@r integer: the value for red (0 - 255).

	@g integer: the value for green (0 - 255).

	@b integer: the value for blue (0 - 255).

	"""

def BCSetForegroundColor(w, r, g, b):

	"""

	Sets the RGB values for the foreground color of widget w to be r, g and b.
	NOTE: This function may not work for certain widgets under some styles.
	This function is not supported under VR mode.
	


	@w object: the widget whose foreground color will be set.

	@r integer: the value for red (0 - 255).

	@g integer: the value for green (0 - 255).

	@b integer: the value for blue (0 - 255).

	"""

def BCHideLater(w, ms):

	"""

	Hides widget w, after ms milliseconds.
	This function is not supported under VR mode.
	


	@w object: the widget to hide.

	@ms integer: milliseconds.

	"""

def BCIsVisible(w):

	"""

	Returns True if widget w is visible, otherwise False.
	Note the difference between BCIsShown() and BCIsVisible().
	BCIsVisible() will test whether a widget is currently visible or not. 
	BCIsShown() returns False if BCHide() was called for this particular widget and BCShow() has not been called yet. Otherwise, returns True. Thus you may have a widget which is shown but not visible if, for example, you have called BCHide() for its parent.
	This function is not supported under VR mode.
	


	@w object: the widget whose visibility is tested.

	@returns: True if w is visible or False if it is not.

	"""

def BCSetVisible(w, visible):

	"""

	Sets the widget to visible status if all its parent widgets up to the window are visible.
	This function is not supported under VR mode.
	


	@w object: the widget.

	@visible boolean: set this parameter to True to sets the widget to visible status, or to False to hides it.

	"""

def BCWidth(w):

	"""

	Returns the width of widget w.
	CAUTION This functions returns the original width of the widget, unless it is a BCWindow.
	This function is not supported under VR mode.
	


	@w object: the widget whose width will be examined.

	@returns: the width of widget w.

	"""

def BCHeight(w):

	"""

	Returns the height of widget w.
	CAUTION This functions returns the original height of the widget, unless it is a BCWindow.
	This function is not supported under VR mode.
	


	@w object: the widget whose height will be examined.

	@returns: the height of widget w.

	"""

def BCDestroy(w):

	"""

	Deletes w immediately (i.e. frees all resources allocated to this object).
	This function should be carefully used.
	WARNING: Do not use this function with BCListViewItem. Use BCListViewItemDestroy instead.
	This function is not supported under VR mode.
	


	@w object: the widget to be destroyed.

	"""

def BCDestroyLater(w):

	"""

	Deletes w (i.e. frees all resources allocated to this object).
	Is more safe than deleting immediately because frees w resources on the next event delivery.
	WARNING: Do not use this function with BCListViewItem or BCPlotCurve. Use BCListViewItemDestroy or BCPlotCurveDestroy instead.
	This function is not supported under VR mode.
	


	@w object: the widget to be destroyed.

	"""

def BCAddToolTip(w, tip):

	"""

	Adds a tooltip (balloon help) to widget w. 
	A tooltip is a piece of text in a small frame that briefly describes the use 
	of the widget. The tooltip is activated when mouse pointer is over widget w.
	This function is not supported under VR mode.
	


	@w object: the widget to which the tooltip will be added by this function.

	@tip string: the text that the tooltip will contain.

	"""

def BCAddToolTipImage(w, fileImage):

	"""

	Adds an image as tooltip (balloon help) to widget w. 
	A tooltip is a piece of text or image in a small frame that briefly describes the use 
	of the widget. The tooltip is activated when mouse pointer is over widget w.
	This function is not supported under VR mode.
	


	@w object: the widget to which the tooltip will be added by this function.

	@fileImage string: the filename of image that the tooltip will contain.

	"""

def BCGetToolTipText(w):

	"""

	Returns the text that the tooltip (balloon help) of widget w contains.
	This function is not supported under VR mode.
	


	@w object: the widget to which the tooltip is added.

	@returns: the text of tooltip.

	"""

def BCLayout(w):

	"""

	Returns the layout engine that manages the geometry of this widget's children. 
	If the widget does not have a layout the BCLayout function returns 0.
	This function is not supported under VR mode.
	


	@w object: any widget.

	"""

def BCGetUserDataKey(o, key):

	"""

	Retrieves user data from widget o using a char key key.
	These data were set by calling BCSetUserData().


	@o object: the object (widget or layout) where data were stored.

	@key string: the key where data was stored.

	"""

def BCSetUserDataKey(o, key, data):

	"""

	Sets user data data for object o using a char key key.
	These data can be retrieved at any time by calling BCGetUserDataKey().
	NOTE: If you want to assign data at ListViewItem use BCListViewItemSetUserData().


	@o object: any object (widget or layout).

	@key string: any key to store data.

	@data anything: (optional)the data to store.

	"""

def BCGetTopWidget(w):

	"""

	Returns the parent widget of w widget provided that the parent is a BCWindow class widget.
	Returns None if parent is not such a type.
	This function is not supported under VR mode.
	


	@w object: any widget.

	@returns: the parent of w provided that parent is a BCWindow.

	"""

def BCSetTabOrder(firstWidget, secondWidget):

	"""

	Modify the order of keyboard focus inside a window.
	Focus changes when the Tab key is pressed. Imagine tab order as a ring. 
	By default keyboard focus order gets the order the widgets are inserted.
	If you decide to change the tab order of a widget, you will have to 
	specify the previous and next focus nodes of the chain.
	This function is not supported under VR mode.
	


	@firstWidget object: any widget.

	@secondWidget object: any widget.

	"""

def BCSetFocusPolicy(w, fpolicy):

	"""

	Sets the focus policy for the widget w to fpolicy.
	This function is not supported under VR mode.
	


	@w object: the widget to affect.

	@fpolicy integer: the focus policy.
	See BCEnumFocusPolicy.
	
	guitk.constants BCEnumFocusPolicy
	This enum defines the various policies a widget can have with respect to acquiring keyboard focus.
	 - guitk.constants.BCNoFocus
	Widget does not accept focus.
	 - guitk.constants.BCTabFocus
	Widget accepts focus by tabbing.
	 - guitk.constants.BCClickFocus
	Widget accepts focus by clicking.
	 - guitk.constants.BCStrongFocus
	Widget accepts focus by both tabbing and clicking.
	 - guitk.constants.BCWheelFocus
	Like BCStrongFocus plus the widget accepts focus by rolling the mouse wheel when widget is under mouse.

	"""

def BCSetApplicationOverrideCursor(cursor):

	"""

	Overrides the cursors set for all BCWindows/widgets of the current application to the one represented by cursor.
	This function adds a cursor to a stack so that for every call to this function a respective call to BCRestoreApplicationOverrideCursor must be made to restore the application's cursor status.
	This function is not supported under VR mode.
	


	@cursor integer: the cursor (see BCEnumCursor). See BCEnumCursor for details.
	
	guitk.constants BCEnumCursor
	The mouse cursor shape.
	 - guitk.constants.BCCursorCross
	Cross pointer used mainly for design areas.
	 - guitk.constants.BCCursorBlank
	A blank cursor has no visualization.
	 - guitk.constants.BCCursorWhatsThis
	A pointer with a questionmark.
	 - guitk.constants.BCCursorWait
	The sandglass pointer used mainly when the application is proccessing.
	 - guitk.constants.BCCursorMouse
	A three button mouse representation in white color.
	 - guitk.constants.BCCursorExclamation
	An exclamation mark in white color.
	 - guitk.constants.BCCursorArrow
	The standard arrow cursor.
	 - guitk.constants.BCCursorSizeVer
	A cursor used for elements that are used to vertically resize top-level windows.
	 - guitk.constants.BCCursorSizeHor
	A cursor used for elements that are used to horizontally resize top-level windows.
	 - guitk.constants.BCCursorSizeBDiag
	A cursor used for elements that are used to diagonally resize top-level windows at their top-right and bottom-left corners.
	 - guitk.constants.BCCursorSizeFDiag
	A cursor used for elements that are used to diagonally resize top-level windows at their top-left and bottom-right corners.
	 - guitk.constants.BCCursorSizeAll
	A cursor used for elements that are used to resize top-level windows in any direction.
	 - guitk.constants.BCCursorSplitV
	A cursor used for vertical splitters, indicating that a handle can be dragged vertically to adjust the use of available space.
	 - guitk.constants.BCCursorSplitH
	A cursor used for horizontal splitters, indicating that a handle can be dragged horizontally to adjust the use of available space.
	 - guitk.constants.BCCursorPointingHand
	A pointing hand cursor that is typically used for clickable elements such as hyperlinks.
	 - guitk.constants.BCCursorForbidden
	A slashed circle cursor, typically used during drag and drop operations to indicate that dragged content cannot be dropped on particular widgets or inside certain regions.
	 - guitk.constants.BCCursorOpenHand
	A cursor representing an open hand, typically used to indicate that the area under the cursor is the visible part of a canvas that the user can click and drag in order to scroll around.
	 - guitk.constants.BCCursorClosedHand
	A cursor representing a closed hand, typically used to indicate that a dragging operation is in progress that involves scrolling.
	 - guitk.constants.BCCursorBusy
	An hourglass or watch cursor, usually shown during operations that allow the user to interact with the application while they are performed in the background.
	 - guitk.constants.BCCursorZoomIn
	A magnifying glass with a plus sign in it.
	 - guitk.constants.BCCursorZoomOut
	A magnifying glass with a minus sign in it.
	 - guitk.constants.BCCursorIBeam
	A caret or ibeam cursor, indicating that a widget can accept and display text input.
	 - guitk.constants.BCCursorUpArrow
	An arrow pointing upwards toward the top of the screen.
	 - guitk.constants.BCCursorRotate
	A cursor indicating that rotation mode is on
	 - guitk.constants.BCCursorZoomRect
	A cursor indicating that zoom reactangle mode is on.
	 - guitk.constants.BCCursorZoom
	A cursor indicating that zoom mode is on.
	 - guitk.constants.BCCursorPanRotateZoom
	A cursor indicating that Pan Rotate Zoom is on.

	"""

def BCRestoreApplicationOverrideCursor():

	"""

	Restores the current cursor of the current application set by BCSetApplicationOverrideCursor().
	This function must be called after BCSetApplicationOverrideCursor() was called to remove the current cursor from the stack.
	This function is not supported under VR mode.
	


	"""

def BCSetSaveSettings(w, name):

	"""

	Set individual widget w to automatically save its settings to xml file on OK (Enter) and discard on Cancel (Esc).
	By default widgets do NOT save their settings. The settings to be saved depends on the nature of w.
	For example checkBox will save on/off status. BCToolBox and BCTabWidget save their settings (current page) on ESC as well.
	Settings are saved using widget name (provide a unique one).
	
	The supported widgets are:
	BCButtonGroup (the index of the selected button in an exclusive group and the state of the checkBox in the title, if any)
	BCCheckBox (checked/unchecked value)
	BCComboBox (the index of the current item)
	BCDoubleSpinBox (the value)
	BCLineEdit (the text)
	BCPushButton (the on/off state)
	BCSpinBox (the value)
	BCTabWidget (the current tab). Saves on Esc
	BCToolBox (the current tab). Saves on Esc
	BCToolButton (the on/off state)
	This function is not supported under VR mode.
	


	@w object: the widget to save its settings.

	@name string: the name of widget.

	"""

def BCUpdateGeometry(w):

	"""

	Notifies the layout system that this widget has changed and may need to change geometry.
	This function is not supported under VR mode.
	


	@w object: the widget.

	"""

def BCSetUpdatesEnabled(w, enabled):

	"""

	Blocks/unblocks widget painting. This is useful for example when making calculations while adding item
	to a listview.
	This function is not supported under VR mode.
	


	@w object: any widget (e.g. a list view)

	@enabled boolean: set this parameter to True to enable widget updating, or to False to disable it.

	"""

def BCIsUpdatesEnabled(w):

	"""

	Returns True if updating is enabled for widget w, or False if it is disabled.
	This function is not supported under VR mode.
	


	@w object: the widget.

	"""

def BCFontHeight(w):

	"""

	Returns the height of the font for widget w.
	This function is not supported under VR mode.
	


	@w object: the widget.

	@returns: the height of the font.

	"""

def BCFontMaxWidth(w):

	"""

	Returns the width of the widest character in the font for widget w.
	This function is not supported under VR mode.
	


	@w object: the widget.

	@returns: the width of the widest character in the font.

	"""

def BCStringWidth(w, str, len):

	"""

	Returns the width of the first len characters of string str for widget w.
	This function is not supported under VR mode.
	


	@w object: the widget.

	@str string: the string.

	@len integer: the number of characters in str for which length will be returned. Set it to -1
	to return the length of the whole string.

	"""

def BCIconIsValid(iconname):

	"""

	This function informs the user whether iconname corresponds to a valid icon, in order to be used in widgets (e.g. BCToolButtons)
	This function is not supported under VR mode.
	


	@iconname string: the absolute path or the filename (for embedded icons) of the icon.

	@returns: True if iconname gives a valid icon or False otherwise.

	"""

def BCGetColor(init_r, init_g, init_b):

	"""

	Opens a modal color picker window for color selection.
	A color can be preselected if the values init_r, init_g, init_b are defined.
	While the color picker window is open no other widget can receive any input, unless it closes.
	This function is not supported under VR mode.
	


	@init_r integer: (optional)is the red value of the preselected color.

	@init_g integer: (optional)is the green value of the preselected color.

	@init_b integer: (optional)is the blue value of the preselected color.

	@returns: A tuple with the [int r, int g, int b] values of the selected color. If the selection is canceled a [-1, -1, -1]  tuple is returned.

	"""

def BCDialogButtonBoxCreate(p):

	"""

	Creates a widget that contains a separator, an "OK" and a "Cancel" BCPushButton 
	laid inside a BCGridLayout.
	
	This widget should be the last one added to a BCWindow.
	The OK and Cancel BCPushButtons are automatically connected to the accept
	and reject function of the parent widget if it is a BCWindow (as recommended).
	BCPushButtons can be added or removed by the use of the rest of the BCDialogButtonBox functions.
	A BCDialogButtonBox displays its buttons in a BCGridLayout that can be retrieved by
	calling BCDialogButtonBoxGetGridLayout(). This function can be used to fully customize
	the BCDialogButtonBox widget.


	@p object: the parent widget (preferably created by BCWindowCreate()) or layout.

	@returns: the created widget.

	"""

def BCDialogButtonBoxGetAcceptButton(dbb):

	"""

	Returns the BCPushButton that is connected to the accept function of the window (i.e. the "OK" button).


	@dbb object: the BCDialogButtonBox.

	@returns: the "OK" BCPushButton.

	"""

def BCDialogButtonBoxGetRejectButton(dbb):

	"""

	Returns the BCPushButton that is connected to the reject function of the window (i.e. the "Cancel" button).


	@dbb object: the BCDialogButtonBox.

	@returns: the "Cancel" BCPushButton.

	"""

def BCDialogButtonBoxAddButton(dbb, b):

	"""

	Adds a BCPushButton b to a BCDialogButtonBox dbb.


	@dbb object: the BCDialogButtonBox.

	@b object: the BCPushButton that will be added.

	"""

def BCDialogButtonBoxRemoveButton(dbb, b, also_delete):

	"""

	Removes a BCPushButton b from a BCDialogButtonBox dbb.


	@dbb object: the BCDialogButtonBox to be affected.

	@b object: the BCPushButton that will be removed from dbb.

	@also_delete boolean: set this parameter to True for the BCPushButton b not only to be removed (hidden), but also deleted (i.e free resources).

	"""

def BCDialogButtonBoxGetGridLayout(dbb):

	"""

	Returns the BCGridLayout of a BCDialogButtonBox dbb.
	A BCDialogButtonBox accommodates its children widgets inside a BCGridLayout.
	This layout is returned by this function in order to make any desirable customization to the BCDialogButtonBox.


	@dbb object: the BCDialogButtonBox.

	@returns: the default BCGridLayout child of the BCDialogButtonBox.

	"""

def BCDialogButtonBoxGetSeparator(dbb):

	"""

	Returns the line separator (BCFrame type) that is displayed by default above the dialog button box BCPushButtons.
	This is useful if you wish to hide the separator with BCHide().


	@dbb object: the BCDialogButtonBox.

	@returns: the default separator of dbb.

	"""

def BCDialogButtonBoxResetSize(dbb):

	"""

	Resets the size of the BCDialogButtonBox to fit its contents. 
	Use this function after you have altered the contents of dbb (for example if you set an icon on a button that requires more height).


	@dbb object: the BCDialogButtonBox.

	"""

def BCDrawerGridCreate(p):

	"""

	Creates a DrawerGrid inside parent p.
	DrawerGrid is a container widget, able to accommodate widgets and manage their visibility. 
	Create manager widgets with parent DrawerGrid and then set/insert. 
	NOTE: DrawerGrid stores widgets visibility state to xml file.
	of managed widgets in xml.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@returns: the created drawer grid.

	"""

def BCDrawerGridInsertWidget(drawer, w, visible, toolTip):

	"""

	Inserts the widget w inside DrawerGrid drawer with a managing button on the left.
	Standard DrawerGrid stores widgets visibility state to xml.
	A push button is provided at the left side of the widget, able to show/hide it. 
	This button will be returned by the function. 
	The widget can be initialized to be hidden or not, depending on visible parameter. 
	A tooltip toolTip can be applied at the button as well.
	WARNING: If you try to manage (show/hide) the widget manually, the behavior is undefined.
	This function is not supported under VR mode.
	


	@drawer object: the DrawerGrid.

	@w object: the widget to be inserted.

	@visible boolean: this indicates how the widget initializes. Set False for your widget 
	to appear hidden when the form created.

	@toolTip string: the text to be displayed as balloon help for the button.

	@returns: the push button that show/hide the widget.

	"""

def BCFlowLayoutCreate(p):

	"""

	Creates a BCFlowLayout.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@returns: the created BCFlowLayout.

	"""

def BCFlowLayoutSetMargin(l, margin):

	"""

	Sets the margin of BCFlowLayout l to margin.
	This function is not supported under VR mode.
	


	@l object: the BCFlowLayout that will be affected by this function.

	@margin integer: the new value for margin.

	"""

def BCFlowLayoutSetSpacing(l, spacing):

	"""

	Sets the spacing of BCFlowLayout l to spacing.
	This function is not supported under VR mode.
	


	@l object: the BCFlowLayout that will be affected by this function.

	@spacing integer: the new value for spacing.

	"""

def BCFlowLayoutInsert(l, item):

	"""

	Inserts item into this flow layout. The item is added at the end.
	This function is not supported under VR mode.
	


	@l object: the layout.

	@item object: the widget that will be inserted to l.

	"""

def BCFlowLayoutRemove(l, item):

	"""

	Remove item item from flow layout l.
	                      
	WARNING: After this call, it is the caller's responsibility to give the item a reasonable geometry or to put the item back into a layout.
	This function is not supported under VR mode.
	


	@l object: the layout.

	@item object: can be a widget (BCButton, BCLabel, BCLineEdit ...).

	"""

def BCFrameCreate(p):

	"""

	Creates a placeholder box with parent p without any contents or layout.
	NOTE: You will need a layout that specifies how child widgets line up inside.


	@p object: the parent widget or layout.

	@returns: the created BCFrame.

	"""

def BCFrameSetShadow(f, shadow):

	"""

	Sets the shadow of the BCFrame f to shadow. It is meant to be used with BCFrameSetShape().
	The affect of this function depends on the applications style.


	@f object: the BCFrame to be affected by this function.

	@shadow integer: the new shadow style of the BCFrame f. See BCEnumShadow property
	for details.
	
	guitk.constants BCEnumShadow
	This enum type defines the 3D effect used for BCFrame's frame. Shadow is used with BCFrameSetShadow for example.
	 - guitk.constants.BCPlain
	the frame and contents appear level with the surroundings; draws using the palette foreground
	color (without any 3D effect).
	 - guitk.constants.BCSunken
	the frame and contents appear sunken; draws a 3D sunken line using the light and dark colors
	of the current color group.
	 - guitk.constants.BCRaised
	the frame and contents appear raised; draws a 3D raised line using the light and dark colors
	of the current color group.

	"""

def BCFrameSetShape(f, shape):

	"""

	Sets the frame shape of BCFrame f to shape.
	The affect of this function depends on the applications style.


	@f object: the BCFrame to be affected by this function.

	@shape integer: the new shape style of BCFrame f. See BCEnumShape property for details.
	
	guitk.constants BCEnumShape
	This enum type defines the shapes of a BCFrame.
	 - guitk.constants.BCNoFrame
	BCFrame draws nothing.
	 - guitk.constants.BCBox
	BCFrame draws a box around its contents.
	 - guitk.constants.BCPanel
	BCFrame draws a panel to make the contents appear raised or sunken.
	 - guitk.constants.BCStyledPanel
	Draws a rectangular panel with a look that depends on the current GUI style. It can be
	raised or sunken.
	 - guitk.constants.BCHLine
	BCFrame draws a horizontal line that frames nothing (useful as separator).
	 - guitk.constants.BCVLine
	BCFrame draws a vertical line that frames nothing (useful as separator).
	 - guitk.constants.BCGroupBoxPanel
	Draws a rectangular panel.
	 - guitk.constants.BCWinPanel
	Draws a rectangular panel that can be raised or sunken like those in Windows 95. Specifying
	this shape sets the line width to 2 pixels. BCWinPanel is provided for compatibility. For
	GUI style independence it is recommended to use BCStyledPanel instead.
	 - guitk.constants.BCLineEditPanel
	It is used to draw a frame suitable for line edits. The look depends upon the current GUI style.
	 - guitk.constants.BCTabWidgetPanel
	It is used to draw a frame suitable for tab widgets. The look depends upon the current GUI style.

	"""

def BCGridLayoutCreate(p, numRows, numCols):

	"""

	Creates a BCGridLayout.


	@p object: the parent widget or layout.

	@numRows integer: (optional)this argument is obsolete. It is kept for compatibility reasons.

	@numCols integer: (optional)this argument is obsolete. It is kept for compatibility reasons.

	@returns: the created layout.

	"""

def BCGridLayoutAddWidget(grid, w, row, col, alignment):

	"""

	Adds a widget (button, checkbox, etc) to a BCGridLayout.


	@grid object: the gridlayout that will be affected by this function.

	@w object: the widget that will be added to the grid.

	@row integer: the row of the gridlayout at which the widget will be added.

	@col integer: the column of the gridlayout at which the widget will be added.

	@alignment integer: the alignment of the widget in the grid cell. See BCEnumAlignment for details.
	NOTE: if you want the child widget to take all vertical space you must set "BCAlignVJustify" alignment.
	
	guitk.constants BCEnumAlignment
	This enum type is used to describe alignment. It contains horizontal and vertical flags. Alignment is used with BCGridLayoutAddMultiCellWidget for example.
	NOTE: You can use at most one horizontal and one vertical flag at a time.
	 - guitk.constants.BCAlignAuto
	aligns according to the language. Left for most, right for Arabic and Hebrew.
	 - guitk.constants.BCAlignLeft
	aligns with the left edge.
	 - guitk.constants.BCAlignRight
	aligns with the right edge.
	 - guitk.constants.BCAlignHCenter
	centers horizontally in the available space.
	 - guitk.constants.BCAlignJustify
	justifies the text in the available space.
	 - guitk.constants.BCAlignTop
	aligns with the top.
	 - guitk.constants.BCAlignBottom
	aligns with the bottom.
	 - guitk.constants.BCAlignVCenter
	centers vertically in the available space.
	 - guitk.constants.BCAlignCenter
	centers in both dimensions (vertically and horizontally).
	 - guitk.constants.BCAlignHorizontal_Mask
	horizontal mask.
	 - guitk.constants.BCAlignVertical_Mask
	vertical mask.
	 - guitk.constants.BCAlignVJustify
	Justifies the text vertically in the available space.

	"""

def BCGridLayoutSetMargin(grid, margin):

	"""

	Sets the margin of the BCGridLayout.


	@grid object: the BCGridLayout that will be affected.

	@margin integer: the size of margin in pixels.

	"""

def BCGridLayoutSetSpacing(grid, spacing):

	"""

	Sets the spacing of the BCGridLayout.


	@grid object: the BCGridLayout that will be affected.

	@spacing integer: the size of spacing in pixels.
	BCGridLayoutSetMargin()

	"""

def BCGridLayoutRows(grid):

	"""

	returns the total number of rows of the BCGridLayout.


	@grid object: the BCGridLayout whose number of rows we want to get.

	@returns: the total number of rows of the BCGridLayout.

	"""

def BCGridLayoutCols(grid):

	"""

	returns the total number of columns of the BCGridLayout.


	@grid object: the BCGridLayout whose number of columns we want to get.

	@returns: the total number of columns of the BCGridLayout.

	"""

def BCGridLayoutRemove(grid, w):

	"""

	Removes widget w from BCGridLayout grid.


	@grid object: the BCGridLayout.

	@w object: the widget that will be removed.

	"""

def BCGridLayoutSetRowStretch(grid, row, val):

	"""

	Sets the stretch factor of row row to val for the BCGridLayout grid.
	The default stretch factor is 0. Stretch factor is relative with other rows in the grid.
	Rows with high stretch factor take more of the available space.
	Stretch factors are used to change how much space widgets are given in proportion to one another.


	@grid object: the BCGridLayout.

	@row integer: the row that will be affected. Recall that the first row has index 0.

	@val integer: the stretch factor.

	"""

def BCGridLayoutSetColStretch(grid, col, val):

	"""

	Sets the stretch factor of column col to val for the BCGridLayout grid.
	The default stretch factor is 0. Stretch factor is relative with other columns in the grid.
	Columns with high stretch factor take more of the available space.
	Stretch factors are used to change how much space widgets are given in proportion to one another.


	@grid object: the BCGridLayout.

	@col integer: the col that will be affected. Recall that the first column has index 0.

	@val integer: the stretch factor.

	"""

def BCGridLayoutFindWidget(grid, w):

	"""

	Searches for widget w in this layout (not including child layouts).


	@grid object: the BCGridLayout.

	@w object: the widget that will be searched.

	@returns: A tuple with 3 items: 
	First item is value True if w is found, otherwise False.
	Second value is the row of the BCGridLayout at which w is found.
	Third values is the column of the BCGridLayout at which w is found.
	If the widget w was not found, the row and column values are -1.

	"""

def BCLabelCreate(p, text):

	"""

	Creates a BCLabel with text text.


	@p object: the parent widget or layout.

	@text string: the text that the BCLabel will display.

	@returns: The created BCLabel.

	"""

def BCLabelTickerCreate(p, text):

	"""

	Creates a BCTicker which is an auto-scrolling label with text text.
	BCTicker has the ability to scroll from left to right if the text can not fit in the widget's width.
	User can also scroll left or right by pressing (and keep pressed) the left mouse button and moving the cursor right or left.
	WARNING: the functions of bc_label BCLabelSelectedText BCLabelSetAlignment , BCLabelSetStylePixmap, 
	BCLabelSetIconFileName , BCLabelSetPixmap are not compatible with BCTicker.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@text string: the text that the BCTicker will display.

	@returns: The created BCTicker.

	"""

def BCLabelText(lab):

	"""

	Returns the text of BCLabel lab.


	@lab object: the BCLabel.

	@returns: the text of the BCLabel.

	"""

def BCLabelSelectedText(lab):

	"""

	Returns the selected text of BCLabel lab.
	This function is not supported under VR mode.
	


	@lab object: the BCLabel.

	@returns: the selected text of the BCLabel.

	"""

def BCLabelSetText(lab, text):

	"""

	Sets the text that will be displayed by BCLabel lab.


	@lab object: the BCLabel.

	@text string: the text that BCLabel lab will display.

	"""

def BCLabelSetAlignment(lab, alignment):

	"""

	Sets the alignment of the label.
	This function is not supported under VR mode.
	


	@lab object: the BCLabel.

	@alignment integer: specifies the required alignment.
	See BCEnumAlignment for details.
	
	guitk.constants BCEnumAlignment
	This enum type is used to describe alignment. It contains horizontal and vertical flags. Alignment is used with BCGridLayoutAddMultiCellWidget for example.
	NOTE: You can use at most one horizontal and one vertical flag at a time.
	 - guitk.constants.BCAlignAuto
	aligns according to the language. Left for most, right for Arabic and Hebrew.
	 - guitk.constants.BCAlignLeft
	aligns with the left edge.
	 - guitk.constants.BCAlignRight
	aligns with the right edge.
	 - guitk.constants.BCAlignHCenter
	centers horizontally in the available space.
	 - guitk.constants.BCAlignJustify
	justifies the text in the available space.
	 - guitk.constants.BCAlignTop
	aligns with the top.
	 - guitk.constants.BCAlignBottom
	aligns with the bottom.
	 - guitk.constants.BCAlignVCenter
	centers vertically in the available space.
	 - guitk.constants.BCAlignCenter
	centers in both dimensions (vertically and horizontally).
	 - guitk.constants.BCAlignHorizontal_Mask
	horizontal mask.
	 - guitk.constants.BCAlignVertical_Mask
	vertical mask.
	 - guitk.constants.BCAlignVJustify
	Justifies the text vertically in the available space.

	"""

def BCLabelSetStylePixmap(lab, style):

	"""

	Sets the specified pixmap of type style to be displayed on the BCLabel according to the desired kind of message.
	This function is not supported under VR mode.
	


	@lab object: the BCLabel.

	@style integer: the required pixmap. See BCEnumStylePixmap for details.
	
	guitk.constants BCEnumStylePixmap
	This enum represents a StylePixmap. A StylePixmap is a pixmap that can follow some
	existing GUI style or guideline. StylePixmap is used with BCLabelSetStylePixmap for example.
	 - guitk.constants.BCMessageBoxWarning
	the 'warning' icon.
	 - guitk.constants.BCMessageBoxCritical
	the 'critical' icon.
	 - guitk.constants.BCMessageBoxInformation
	the 'information' icon.
	 - guitk.constants.BCMessageBoxQuestion
	the 'question' icon.

	"""

def BCLabelSetIconFileName(lab, fileName):

	"""

	Sets the specified iconname pixmap file to be displayed on the BCLabel lab.
	NOTE: If you set a pixmap file to a label, its text will be replaced and vice versa.
	This function is not supported under VR mode.
	


	@lab object: the BCLabel.

	@fileName string: the absolute path of the icon file.

	"""

def BCBoxLayoutCreate(p, o):

	"""

	Creates a BCBoxLayout with horizontal or vertical orientation depending on o.


	@p object: the parent widget or layout.

	@o integer: the orientation. See BCEnumOrientation for details.
	
	guitk.constants BCEnumOrientation
	This type is used to signify an object's orientation. Orientation is used with BCButtonGroupCreate for example.
	 - guitk.constants.BCHorizontal
	sets horizontal orientation.
	 - guitk.constants.BCVertical
	sets vertical orientation.

	@returns: the created BCBoxLayout.

	"""

def BCBoxLayoutSetMargin(l, margin):

	"""

	Sets the margin of BCBoxLayout l to margin.


	@l object: the BCBoxLayout that will be affected by this function.

	@margin integer: the new value for margin.

	"""

def BCBoxLayoutSetSpacing(l, spacing):

	"""

	Sets the spacing of BCBoxLayout l to spacing.


	@l object: the layout that will be affected by this function.

	@spacing integer: the new value for spacing.

	"""

def BCBoxLayoutSetStretchFactor(l, item, stretch):

	"""

	Sets the stretch factor for item to stretch and returns 1 if item is found in this layout (not including child layouts), otherwise returns 0.


	@l object: the layout (either horizontal or vertical).

	@item object: the item for which the stretch factor will be set. Either a widget or a layout.

	@stretch integer: the new stretch factor for item.

	@returns: 1 if item is found in layout l, 0 otherwise.

	"""

def BCBoxLayoutSetDirection(l, d):

	"""

	Sets the direction of layout l to d.


	@l object: the layout (either horizontal or vertical).

	@d integer: the new direction of l. See BCEnumDirection.
	
	guitk.constants BCEnumDirection
	This enum type defines the direction of box layouts. It can be used with BCBoxLayoutSetDirection for example.
	 - guitk.constants.BCLeftToRight
	The new widgets are inserted on the right of previously inserted widgets.
	 - guitk.constants.BCRightToLeft
	The new widgets are inserted on the left of previously inserted widgets.
	 - guitk.constants.BCTopToBottom
	The new widgets are inserted down under the previously inserted widgets.
	 - guitk.constants.BCBottomToTop
	The new widgets are inserted up above the previously inserted widgets.
	 - guitk.constants.BCDown
	same as BCTopToBottom.
	 - guitk.constants.BCUp
	same as BCBottomToTop.

	"""

def BCBoxLayoutDirection(l):

	"""

	Returns the direction of layout l.


	@l object: the layout.

	@returns: the direction of layout (see BCEnumDirection).
	BCEnumDirection: This enum type defines the direction of box layouts. It can be used with BCBoxLayoutSetDirection for example.
	guitk.constants.BCLeftToRight: The new widgets are inserted on the right of previously inserted widgets.
	guitk.constants.BCRightToLeft: The new widgets are inserted on the left of previously inserted widgets.
	guitk.constants.BCTopToBottom: The new widgets are inserted down under the previously inserted widgets.
	guitk.constants.BCBottomToTop: The new widgets are inserted up above the previously inserted widgets.
	guitk.constants.BCDown: same as BCTopToBottom.
	guitk.constants.BCUp: same as BCBottomToTop.

	"""

def BCBoxLayoutInsert(l, item, index):

	"""

	Inserts item into this box layout at position index. If index is negative, the item is added at the end.


	@l object: the layout (either horizontal or vertical).

	@item object: the widget or layout that will be inserted to l.

	@index integer: the index where item will be inserted. If index == -1 item is added at the end of l.

	"""

def BCBoxLayoutRemove(l, item):

	"""

	Remove item item from box layout l.
	WARNING: After this call, it is the caller's responsibility to give the item a reasonable geometry or to put the item back into a layout.


	@l object: the layout (either horizontal or vertical).

	@item object: can be either widget (BCButton, BCLabel, BCLineEdit ...) or layout (either horizontal or vertical).

	"""

def BCLineEditCreateDouble(p, val):

	"""

	Creates a BCLineEdit that only accepts doubles.
	NOTE: Initializing with val value guitk.constants.blank will create an empty-valid double LineEdit.
	This function is not supported under VR mode.
	


	@p object: the parent widget.

	@val float: (optional)the value with which the text of the BCLineEdit will be set (in double format).

	@returns: the created BCLineEdit.

	"""

def BCLineEditCreateInt(p, val):

	"""

	Creates a BCLineEdit that only accepts integers.
	NOTE: Initializing with val value guitk.constants.blank will create an empty-valid int LineEdit.
	This function is not supported under VR mode.
	


	@p object: the parent widget.

	@val integer: (optional)the value with which the text of the BCLineEdit will be set (in int format).

	@returns: the created BCLineEdit.

	"""

def BCLineEditCreate(p, val):

	"""

	Creates a BCLineEdit that accepts any text.


	@p object: the parent widget or layout.

	@val string: the value with which the text of the LineEdit will be set

	@returns: the created BCLineEdit.

	"""

def BCLineEditGetText(le):

	"""

	Returns the text of BCLineEdit le.


	@le object: the BCLineEdit.

	@returns: the text of the BCLineEdit.

	"""

def BCLineEditHasText(le):

	"""

	Checks whether BCLineEdit le has text or not.
	NOTE: Spaces and tabs are also meant as text, so in such cases this function will return 1.


	@le object: the BCLineEdit.

	@returns: 0 in case le is empty; 1 otherwise.

	"""

def BCLineEditGetSelectedText(le):

	"""

	Returns the selected text of BCLineEdit le if any, otherwise returns None.


	@le object: the BCLineEdit.

	@returns: the selected text of the BCLineEdit or None if nothing is selected.

	"""

def BCLineEditGetInt(le):

	"""

	Returns the content of BCLineEdit le in int format.
	NOTE: le should be checked if is empty (i.e. it has no text) with function BCLineEditHasText().
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@returns: the content of the BCLineEdit in int format. If the content is not a valid integer or le is empty, guitk.constants.blank will be returned, indicating that the integer is invalid.

	"""

def BCLineEditGetDouble(le):

	"""

	Returns the content of BCLineEdit le in double format.
	NOTE: le should be checked if is empty (i.e. it has no text) with function BCLineEditHasText().
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@returns: the content of the BCLineEdit in double format. If the content is not a valid double or le is empty, guitk.constants.blank will be returned, indicating that the double is invalid.

	"""

def BCLineEditSetText(le, text):

	"""

	Sets the text of BCLineEdit le to be the text in text.


	@le object: the BCLineEdit.

	@text string: the new text that will be displayed in BCLineEdit le.

	"""

def BCLineEditSetInt(le, val):

	"""

	Sets the integer val to be the content of BCLineEdit le.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@val integer: the integer value that will be displayed in BCLineEdit le.

	"""

def BCLineEditSetDouble(le, val):

	"""

	Sets the text of BCLineEdit le to be a text representation of val.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@val float: the double value that will be displayed in BCLineEdit le.

	"""

def BCLineEditSetQuestionMarkFunction(le, funct, data):

	"""

	Sets the function that will be called when a question mark (?) is entered in the BCLineEdit.
	NOTE: If BCLineEditSetF1Function() is not set, when pressing F1 the function funct will be called.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@funct callback: the function that will be called. See BC_LINEEDIT_QUESTIONMARK_FUNCTION for details.
	integer BC_LINEEDIT_QUESTIONMARK_FUNCTION(le, data)
	The function to be called when a questionmark (?) is entered in a BCLineEdit.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	le    object    the BCLineEdit.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by function funct.

	"""

def BCLineEditSetF1Function(le, funct, data):

	"""

	Sets the function that will be called when F1 key is pressed in the BCLineEdit.
	NOTE: If BCLineEditSetQuestionMarkFunction() is not set, when pressing question mark (?) the function funct will be called.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@funct callback: the function that will be called. See BC_LINEEDIT_F1_FUNCTION for details.
	integer BC_LINEEDIT_F1_FUNCTION(le, data)
	The function to be called when F1 key is pressed in BCLineEdit le.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	le    object    the BCLineEdit.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by function funct.

	"""

def BCLineEditSetF3Function(le, funct, data):

	"""

	Sets the function that will be called when F3 key is pressed in the BCLineEdit.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@funct callback: the function that will be called. See BC_LINEEDIT_F3_FUNCTION for details.
	integer BC_LINEEDIT_F3_FUNCTION(le, data)
	The function to be called when F3 key is pressed in BCLineEdit le.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly
	but with the use of a timer (BCTimerSingleShot). If you are not sure how to do it, please contact GUI Dept for more details.
	
	Arguments
	
	le    object    the BCLineEdit.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by function funct.

	"""

def BCLineEditSetTextChangeFunction(le, funct, data):

	"""

	Sets the function that will be called when the text changes in the BCLineEdit.


	@le object: the BCLineEdit.

	@funct callback: the function that will be called. See BC_LINEEDIT_TEXT_CHANGED_FUNCTION for details.
	integer BC_LINEEDIT_TEXT_CHANGED_FUNCTION(le, text, data)
	The function to be called when the text changes in the BCLineEdit.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	le    object    the BCLineEdit.
	text  string    the current text in the BCLineEdit.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)a pointer to any data required by funct.

	"""

def BCLineEditSetSelectionChangedFunction(le, funct, data):

	"""

	Sets the function that will be called when the selection changes in the BCLineEdit.


	@le object: the BCLineEdit.

	@funct callback: the function that will be called. See BC_LINEEDIT_SELECTION_CHANGED_FUNCTION for details.
	integer BC_LINEEDIT_SELECTION_CHANGED_FUNCTION(le, data)
	The function to be called when selected text inside a BCLineEdit changes.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	le    object    the BCLineEdit.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCLineEditSetEnterPressedFunction(le, funct, data):

	"""

	Sets the function that will be called when enter is pressed inside le.
	If this function returns 1, the default behaviour is completely overridden.
	This means that if you return 0, the accept function of the window that le belongs, will operate (window may close). If you return 1, the accept will NOT operate and it seems like you pressed a regular key inside line edit.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@funct callback: the function that will be called when enter is pressed. See BC_LINEEDIT_ENTER_PRESSED_FUNCTION for details.
	integer BC_LINEEDIT_ENTER_PRESSED_FUNCTION(le, data)
	The function to be called when enter/return key is pressed inside BCLineEdit le.
	If you return 0, the accept function of the window that le belongs, will
	operate (window may close). If you return 1, the accept will NOT operate and
	it seems like you pressed any regular key inside line edit.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	le    object    the BCLineEdit.
	data  anything  anything that may be required in function.
	
	Return: 0 if you want accept function of window to operate, otherwise return 1.

	@data anything: (optional)any user data required by funct.

	"""

def BCLineEditSetMinMaxLimitInt(le, minVal, maxVal):

	"""

	Sets the minimum and maximum integer values allowed in a BCLineEdit.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@minVal integer: the minimum value.

	@maxVal integer: the maximum value.

	"""

def BCLineEditSetMinMaxLimitDouble(le, minVal, maxVal):

	"""

	Sets the minimum and maximum double values allowed in a BCLineEdit.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@minVal float: the minimum value.

	@maxVal float: the maximum value.

	"""

def BCLineEditSelectAll(le):

	"""

	Select all content of BCLineEdit widget.


	@le object: the BCLineEdit.

	"""

def BCLineEditTakeKeyboard(le):

	"""

	Take all the keyboard events from the drawing area and send them to BCLineEdit le.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	"""

def BCLineEditSetFixedWidth(le, numChars):

	"""

	Function is obsolete. Use BCLineEditSetFixedNumCharWidth() instead.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@numChars integer: the number of characters.

	"""

def BCLineEditSetMinimumWidth(le, s):

	"""

	Sets the minimum width of BCLineEdit le according to s.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@s integer: the minimum width for le. See BCEnumSize for details.
	
	guitk.constants BCEnumSize
	This enum type is used to define the size (minimum/fixed/maximum) of a widget, depending on the function, measured in number of characters.
	 - guitk.constants.BCSizeAuto
	the widget's size depends on its contents.
	 - guitk.constants.BCSizeSmall
	sets the widget's size to small.
	 - guitk.constants.BCSizeMedium
	sets the widget's size to medium.
	 - guitk.constants.BCSizeLarge
	sets the widget's size to large.
	 - guitk.constants.BCSizeExtraLarge
	sets the widget's size to extra large.

	"""

def BCLineEditSetReadOnly(le, readOnly):

	"""

	Makes BCLineEdit le readonly (i.e. if input by the user is allowed).


	@le object: the BCLineEdit that will be affected.

	@readOnly boolean: set this parameter to True to make le readonly.

	"""

def BCLineEditSetValidator(le, v):

	"""

	Set the validator for BCLineEdit le to v.
	Validators are used in order to check if the input text is valid according to them.
	
	 There are two kinds of validators: BCValidatorInt for integer values and BCValidatorDouble for double values. Even if a validator
	is set, you can write anything you want in the BCLineEdit as if there was no validator at all! You can check whether or not
	the input text is valid by calling BCLineEditValidate() or BCLineEditApplyValidator().
	WARNING: This function also clears the text of le!
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@v integer: the validator type. See BCEnumValidatorType for details.
	
	guitk.constants BCEnumValidatorType
	This enum type defines the types of valid input. It can be used with BCLineEditSetValidator for example.
	 - guitk.constants.BCValidatorNone
	free text input.
	 - guitk.constants.BCValidatorInt
	only integer values are permitted.
	 - guitk.constants.BCValidatorDouble
	double/float values are permitted.

	"""

def BCLineEditGetValidator(le):

	"""

	Returns the validator type of BCLineEdit le.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@returns: the validator type of the BCLineEdit. See BCEnumValidatorType for details.
	BCEnumValidatorType: This enum type defines the types of valid input. It can be used with BCLineEditSetValidator for example.
	guitk.constants.BCValidatorNone: free text input.
	guitk.constants.BCValidatorInt: only integer values are permitted.
	guitk.constants.BCValidatorDouble: double/float values are permitted.

	"""

def BCLineEditSetMinLimitInt(le, minVal):

	"""

	Sets the minimum integer value allowed in a BCLineEdit.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@minVal integer: the minimum value.

	"""

def BCLineEditSetMaxLimitInt(le, maxVal):

	"""

	Sets the maximum integer value allowed in a BCLineEdit.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@maxVal integer: the maximum value.

	"""

def BCLineEditSetMinLimitDouble(le, minVal):

	"""

	Sets the minimum double value allowed in a BCLineEdit.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@minVal float: the minimum value.

	"""

def BCLineEditSetMaxLimitDouble(le, maxVal):

	"""

	Sets the maximum double value allowed in a BCLineEdit.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@maxVal float: the maximum value.

	"""

def BCLineEditSetExtentionsFilter(le, extensions):

	"""

	Sets what file types to be shown when tab is pressed (i.e. auto completion) into BCLineEdit le.
	If you need to clear the filter, just recall this function passing extensions with None.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@extensions object: a list of strings with which auto completion will be filtered.

	"""

def BCLineEditSetCursorPosition(le, pos):

	"""

	Sets the current cursor position for BCLineEdit le.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@pos integer: the position in the BCLineEdit to set the cursor.

	"""

def BCLineEditGetCursorPosition(le):

	"""

	Returns the current cursor position in BCLineEdit le.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@returns: the current cursor position.

	"""

def BCLineEditSetSelection(le, start, length):

	"""

	Selects text from position start and for length characters.


	@le object: the BCLineEdit.

	@start integer: the starting position.

	@length integer: the length of the text to be selected.

	"""

def BCLineEditSetMaxLength(le, length):

	"""

	Sets the maximum permitted length of the text.
	If the text is too long, it is truncated to the limit. If truncation occurs any selected text will be
	unselected, the cursor position is set to 0 and the first part of the string is shown.
	NOTE: The length set by length it is meant the number of any character. So, in case your line edit
	is of type float/double, keep in mind that every character is counted, this is the dot, the 'E' character
	etc, and not only the number of digits or decimals. If the number you want to set has number of
	characters greater than length, then your number will be truncated. In case of float/double line edit
	the characters to be removed will be the decimals. In any other case the result will be text having removed
	the last characters just to fit length.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@length integer: the maximum permitted length of the text.

	"""

def BCLineEditMaxLength(le):

	"""

	Returns the maximum permitted length of the text.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@returns: the maximum permitted length of the text.

	"""

def BCLineEditClear(le):

	"""

	Clears the contents of the BCLineEdit.


	@le object: the BCLineEdit.

	"""

def BCLineEditSetAlignment(le, alignment):

	"""

	Sets the alignment of the text inside BCLineEdit.
	By definition, numbers are aligned right while texts are aligned left. Use this function if you want for example to design a BCLineEdit that accepts %, or characters for calculations and you want to align the text right to show that this is number.


	@le object: the BCLineEdit.

	@alignment integer: specifies the required alignment. See BCEnumAlignment for details.
	
	guitk.constants BCEnumAlignment
	This enum type is used to describe alignment. It contains horizontal and vertical flags. Alignment is used with BCGridLayoutAddMultiCellWidget for example.
	NOTE: You can use at most one horizontal and one vertical flag at a time.
	 - guitk.constants.BCAlignAuto
	aligns according to the language. Left for most, right for Arabic and Hebrew.
	 - guitk.constants.BCAlignLeft
	aligns with the left edge.
	 - guitk.constants.BCAlignRight
	aligns with the right edge.
	 - guitk.constants.BCAlignHCenter
	centers horizontally in the available space.
	 - guitk.constants.BCAlignJustify
	justifies the text in the available space.
	 - guitk.constants.BCAlignTop
	aligns with the top.
	 - guitk.constants.BCAlignBottom
	aligns with the bottom.
	 - guitk.constants.BCAlignVCenter
	centers vertically in the available space.
	 - guitk.constants.BCAlignCenter
	centers in both dimensions (vertically and horizontally).
	 - guitk.constants.BCAlignHorizontal_Mask
	horizontal mask.
	 - guitk.constants.BCAlignVertical_Mask
	vertical mask.
	 - guitk.constants.BCAlignVJustify
	Justifies the text vertically in the available space.

	"""

def BCLineEditValidate(le):

	"""

	Validates the input of BCLineEdit le about minimum and maximum value.
	le is validated if it is created with BCLineEditCreateInt()  or BCLineEditCreateDouble(); otherwise returns False.
	NOTE: This function does not alter any text. It only does a check against le's validator.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@returns: True if the value entered is a valid value, i.e., between minimum and maximum values (if any). In case a value is not valid or le accepts any text, this function returns False.

	"""

def BCLineEditMaxLimitDouble(le):

	"""

	Returns the maximum double value allowed in a BCLineEdit.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@returns: the maximum double value allowed in a BCLineEdit.

	"""

def BCLineEditMinLimitDouble(le):

	"""

	Returns the minimum double value allowed in a BCLineEdit.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@returns: the minimum double value allowed in a BCLineEdit.

	"""

def BCLineEditSetDecimals(le, numDecimals):

	"""

	Sets the number of decimal digits to validate in a BCLineEdit which accepts only floats or doubles.
	NOTE: The user must call BCLineEditApplyValidator() in order to apply the validator and effectively see
	the number of decimals set by this function.
	WARNING: The value set by this function will affect the number of digits that can be shown into a BCLineEdit.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@numDecimals integer: the number of decimal digits to validate.

	"""

def BCLineEditDecimals(le):

	"""

	Returns the number of decimal digits to validate in a BCLineEdit which accepts only floats or doubles.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@returns: the number of decimal digits to validate if BCLineEdit accepts doubles or floats; -1 in case BCLineEdit accepts any text or integers.

	"""

def BCLineEditApplyValidator(le):

	"""

	Applies the validator (if any) of BCLineEdit le.
	This function validates the text of le and, if necessary, alters it according to the validator previously set.
	If no validator has been set to le (i.e. le has been created with function BCLineEditCreate and
	BCLineEditSetValidator has not been called for le ), this function has no effect.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	"""

def BCLineEditInsertText(le, text):

	"""

	Deletes any selected text, inserts text in cursor's point.
	
	It also validates the result. If it is valid, it sets it as the new content of the BCLineEdit.


	@le object: the BCLineEdit.

	@text string: the inserted text.

	"""

def BCLineEditSetAddItemsToPopupMenu(le, funct, data):

	"""

	Adds custom menu items or sub-popups above the default menu items of BCLineEdit's right-mouse-click popup.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@funct callback: the callback function which must be called to create the custom menu.
	See BC_LINEEDIT_ADD_ITEMS_TO_POPUPMENU_FUNCTION for details.
	integer BC_LINEEDIT_ADD_ITEMS_TO_POPUPMENU_FUNCTION(le, popup, data)
	The function to add items to the popup on a right mouse click over the le BCLineEdit.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	le     object    the BCLineEdit.
	popup  object    the BCLineEdit's BCMenu with the default menu items to which you want to add extra items.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any user data required by function funct.

	"""

def BCLineEditSetInfo(le, info):

	"""

	Function is obsolete. Use BCLineEditSetPlaceholderText() instead.


	@le object: the BCLineEdit.

	@info string: the message.

	"""

def BCLineEditGetInfo(le):

	"""

	Function is obsolete. Use BCLineEditGetPlaceholderText() instead.


	@le object: the BCLineEdit.

	@returns: the text displayed as info.

	"""

def BCLineEditSetEchoMode(le, mode):

	"""

	Sets the line edit's echo mode.


	@le object: the BCLineEdit.

	@mode integer: the echo mode for le. See BCEnumEchoMode for details.
	
	guitk.constants BCEnumEchoMode
	This enum type is used to indicate how the echo on lineedit will appear.
	 - guitk.constants.BCNormalEchoMode
	Display characters as they are entered.
	 - guitk.constants.BCNoEchoMode
	Do not display anything.
	 - guitk.constants.BCPasswordMode
	Display asterisks instead of the characters actually entered.

	"""

def BCLineEditPathCreate(p, type, initial, mode, name):

	"""

	Creates a BCLineEditPath, which is a BCFrame that contains an editable history BCComboBox, a "Browse" BCToolButton and a "Clear history" BCToolButton.
	The BCComboBox of the BCLineEditPath maximum number of recent paths is controlled by the "Maximum file paths" option in the options window. These paths will be available any time ANSA is used. The BCLineEditPath can be a "files", "folders" or "everything" type and it can be used with "open" or "save as" mode.
	The type and mode set for the created BCLineEditPath is used by the filemanager that will be called. This means that the filemanager may be of type "file/folder selection" and "Open/Save as".
	If you want to further customize a BCLineEditPath, you can get  all widgets (BCComboBox, file-dialog and clear-history BCToolButtons) and apply the desired BC function. For example if you want to hide the file-dialog button, use BCLineEditPathGetDialogButton() and apply BCHide() to the returned value.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@type integer: the type of BCLineEditPath. See BCEnumLineEditPathType for details.
	
	guitk.constants BCEnumLineEditPathType
	This enumeration describes the type of BCLineEditPath.
	 - guitk.constants.BCHistoryFolders
	The BCLineEditPath will store folder names (full path)
	 - guitk.constants.BCHistoryFiles
	The BCLineEditPath will store file names (full path)
	 - guitk.constants.BCHistoryAnything
	The BCLineEditPath will store anything that has been typed after enter is pressed.

	@initial string: an inital path. NOTE : It is not necessairy to pass an initial path. If an empty string is passed, then the current working directory is used. Also, note that if initial is set, this overrides any previous history paths. This means, everytime the window is shown, it will first show initial as path.

	@mode integer: the mode of BCLineEditPath. See BCEnumLineEditPathMode for details.
	
	guitk.constants BCEnumLineEditPathMode
	This enumeration describes the mode of the filemanager which will be called from a BCLineEditPath.
	 - guitk.constants.BCHistoryOpen
	The filemanager will open for reading a file or folder (depending on BCEnumLineEditPathType)
	 - guitk.constants.BCHistorySaveAs
	The filemanager will open for saving a file or folder (depending on BCEnumLineEditPathType)
	 - guitk.constants.BCHistorySelect
	The filemanager will open for selecting a file or folder (depending on BCEnumLineEditPathType)

	@name string: the name of the BCLineEditPath which will be used as node into the xml.
	WARNING: Special care must be taken with name. If there's another BCLineEditPath with the same name, they will share the same paths!

	@returns: the newly created BCLineEditPath.

	"""

def BCLineEditPathClearHistory(lip):

	"""

	Clears the history of BCLineEditPath lip.
	NOTE: History can also be cleared by getting the BCComboBox from lip and call
	BCComboBoxClear, but using this method does not assure you clear also the XML!
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath

	"""

def BCLineEditPathGetCombo(lip):

	"""

	Returns the BCComboBox of BCLineEditPath lip.
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath.

	@returns: the combobox of the BCLineEditPath.

	"""

def BCLineEditPathGetDialogButton(lip):

	"""

	Returns the dialog button (i.e. the BCToolButton that opens the file-dialog window) of history-path BCFrame lip.
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath.

	@returns: the dialog button of the history-path BCFrame.

	"""

def BCLineEditPathGetClearButton(lip):

	"""

	Returns the clear button (i.e. the BCToolButton that clears the history) of history-box BCFrame lip.
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath.

	@returns: the clear button of the history-path BCFrame.

	"""

def BCLineEditPathGetLineEditPathFromLineEdit(le):

	"""

	Returns the BCLineEditPath container of BCLineEdit le.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit found in BCLineEditPath.

	@returns: the BCLineEditPath container.

	"""

def BCLineEditPathSetDialogEnterEnabled(lip, enable):

	"""

	This function enables/disables the property of calling the EnterPressedFunction. 
	The latter is automatically called right after a selection from the file dialog or from the combobox of history-box frame lip.
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath.

	@enable boolean: set this parameter to True to enable this feature; False otherwise.

	"""

def BCLineEditPathSetEnterPressedFunction(lip, funct, data):

	"""

	Sets the function to be called when enter/return key is pressed inside the combobox of history-path window lip.
	NOTE: If funct returns 0, then the parent window of history-box BCFrame will be closed. If you don't want this, just return 1.
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath.

	@funct callback: the function to be called when enter/return key is pressed. See BC_LINEEDIT_ENTER_PRESSED_FUNCTION for details.
	integer BC_LINEEDIT_ENTER_PRESSED_FUNCTION(le, data)
	The function to be called when enter/return key is pressed inside BCLineEdit le.
	If you return 0, the accept function of the window that le belongs, will
	operate (window may close). If you return 1, the accept will NOT operate and
	it seems like you pressed any regular key inside line edit.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	le    object    the BCLineEdit.
	data  anything  anything that may be required in function.
	
	Return: 0 if you want accept function of window to operate, otherwise return 1.

	@data anything: (optional)any user data required by function funct.

	"""

def BCLineEditPathAddFilter(lip, groupFilterName, extensions):

	"""

	Adds a filter in the file manager that is called after pressing the file manager button.
	In extensions you should pass only the extensions you're interested in without putting the prefix "*.". It'll
	be automatically prepended.
	In case you want to add a filter as is (i.e. without automatically prepend the "*." string), it must begin
	with two asterisks. The filter will result without the first asterisk. For example, if you want to add
	the filter "*", you must pass "**", or if you want to add the filter "*test*", you must pass "**test*". The
	groupFilterName is not affected.
	After inserting a new filter, the default filter "*.*" will be removed. So, in case you still want this filter,
	you should manually add it (pass in extensions the "*" string).
	NOTE: This function has no effect if the created BCLineEditPath is of directory type, either reading or
	writing.
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath.

	@groupFilterName string: the name for the filter group.

	@extensions object: the extensions to be used for group groupFilterName.

	"""

def BCLineEditPathSetFileDialogModal(lip, modal):

	"""

	Sets whether the filemanager that should show from BCLineEditPath lip will be modal or modeless.
	WARNING: If lip's parent BCWindow is modal, then the filemanager will always be launched as modal, overriding this option!
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath.

	@modal boolean: set this to True for a modal filedialog; False otherwise. The default value is True.

	"""

def BCLineEditPathSetFileDialogTitle(lip, title):

	"""

	Sets the title of the filemanager window.
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath.

	@title string: The title of the filemanager window.

	"""

def BCLineEditPathSetSelectionMode(lip, mode):

	"""

	Sets the selection mode of the file manager which will be launched from lip.
	NOTE: If mode of lip is "save", this function has no effect.
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath.

	@mode integer: the selection mode of the file maanger. See BCEnumSelectionMode
	for details.
	
	guitk.constants BCEnumSelectionMode
	This enum type defines the selection mode. Selection is used with BCListViewSetSelectionMode for example.
	 - guitk.constants.BCMulti
	when the user selects an item in the usual way, the previous selection is cleared and the new item is selected. However, if the user presses the Ctrl key when clicking on an item, the clicked item gets toggled and all other items are left untouched. And if the user presses the Shift key while clicking on an item, all items between the current item and the clicked item get selected or unselected, depending on the state of the clicked item. Also, multiple items can be selected by dragging the mouse over them.
	 - guitk.constants.BCSingle
	the user can select only one item. Any already-selected item becomes unselected.
	 - guitk.constants.BCNoSelection
	items cannot be selected.

	"""

def BCLineEditPathSelectedFilePaths(lip):

	"""

	Returns the selected files/paths from filemanager.
	If lip selection mode is set to BCMulti and more than one file/path is selected, the returned string
	is composed of all the selected files/paths, separated by a double-semicolon (";;").
	This function can be used only in the EnterPressedFunction and the DialogEnter must be enabled.
	NOTE: If an invalid file/path is written, after pressing Enter/Return, this function will return None.
	WARNING: The returned pointer is automatically freed by the bcgui mechanism. If you
	wish to keep a copy to the text, use strdup on this pointer.
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath.

	@returns: the selected files/paths.

	"""

def BCLineEditPathInsertEntry(lip, entry):

	"""

	Inserts entry entry into BCLineEditPath lip.
	The new entry will be successfully inserted only if is valid, i.e. same type/mode. If BCLineEditPathSetDialogEnterEnabled()
	is set to True, then the callback function will also be called after successful insertion.
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath.

	@entry string: the entry to insert.

	@returns: True uppon successful insertion; False otherwise.

	"""

def BCLineEditPathRemoveEntry(lip, index):

	"""

	Removes from BCLineEditPath lip the entry at index index.
	If index is a negative number, the least recent item will be removed. If index is
	greater than lip's items or if lip is empty, this function has no effect and False will be returned.
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath

	@index integer: the index of the entry to be removed

	@returns: True uppon successful removal; False otherwise.

	"""

def BCLineEditPathSetLineEditText(lip, txt):

	"""

	Sets the text of BCLineEditPath lip to txt.
	Unlike BCLineEditPathInsertEntry(), this function changes only the text of lip without inserting it into its history. This is
	useful in various cases where you don't want the current history to be set as the text of lip. For example, you may want
	an empty text to be set or even an invalid path/text because this function does not do any check on the validity of txt.
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath

	@txt string: the text to be set. Pass None or an empty text in order to show an empty space.

	"""

def BCListViewCreate(p, numCols, colNames, sorting):

	"""

	Creates a ListView inside parent p.
	In order to avoid performance issues, it is recommended that sorting is enabled after adding the items into the list.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@numCols integer: the number of columns that this ListView is required to have.

	@colNames object: the column header names.

	@sorting boolean: False to disable or True to enable sorting in first column (index 0).

	@returns: the created ListView.

	"""

def BCListViewItemDestroy(item):

	"""

	Completely deletes ListViewItem item.
	After calling this function access to item will cause undefined behaviour.
	NOTE: If item is selected, the selection change call back of list view where item belongs, will run.
	NOTE: When an item deleted, it also deletes its children (if any).
	This function is not supported under VR mode.
	


	@item object: the ListViewItem that will be deleted.

	"""

def BCListViewTakeItem(lv_or_item, item):

	"""

	Removes ListViewItem item from lv_or_item (ListView or ListViewItem). The item is not deleted.
	Use this function followed by BCListViewInsertItem() to move an item to a new location.
	WARNING: This function does NOT delete the item. Use BCListViewItemDestroy() if you want to delete the item.
	This function is not supported under VR mode.
	


	@lv_or_item object: the ListView or ListViewItem.

	@item object: the ListViewItem that will be taken (removed).

	"""

def BCListViewInsertItem(lv_or_item, item):

	"""

	Inserts ListViewItem item into a ListView or a ListViewItem.
	You do not need to call this unless you've called BCListViewTakeItem() and need to reinsert item elsewhere.
	NOTE: The item position after insert is first.
	This function is not supported under VR mode.
	


	@lv_or_item object: the ListView or ListViewItem.

	@item object: the ListViewItem.

	"""

def BCListViewItemGetParent(item):

	"""

	Returns the parent ListViewItem of item or None if its parent is the ListView (i.e. if item is a top-level ListViewItem).
	This function is not supported under VR mode.
	


	@item object: the ListViewItem of the ListView whose parent is returned.

	@returns: the parent item of ListViewItem item or None if its parent is the ListView.

	"""

def BCListViewItemRoot(item):

	"""

	Return the root of the ListViewItem item or the item itself if it is already root (i.e. if item is a top level item).
	This function is not supported under VR mode.
	


	@item object: the ListViewItem whose root is returned.

	@returns: the root of the ListViewItem or the item itself if it is already root.

	"""

def BCListViewItemGetFirstChild(lv_or_item):

	"""

	Returns the first child of parent lv_or_item.
	This function is not supported under VR mode.
	


	@lv_or_item object: the ListView or ListViewItem.

	@returns: the first child item either of a ListView or of a ListViewItem, or None if there is no first item.

	"""

def BCListViewItemGetPreviousSibling(item):

	"""

	Returns the previous ListViewItem in the ListView that is of the same level as item.
	If you want to iterate to items use BCListViewForEachItem() since is by far faster.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem whose sibling is returned.

	@returns: item's previous sibling, or None if none exist.

	"""

def BCListViewItemGetNextSibling(item):

	"""

	Returns the next ListViewItem in the ListView that is of the same level as item.
	If you want to iterate to items use BCListViewForEachItem() since is by far faster.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem whose sibling is returned.

	@returns: item's next sibling, or None if none exist.

	"""

def BCListViewSetText(lv, row, col, text):

	"""

	Sets the text at column col of ListViewItem at row row to text.
	WARNING: In order to avoid performance issues, it is recommended that sorting in list is disabled on mass items text change.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@row integer: the row.

	@col integer: the column.

	@text string: the new text for column col for the ListViewItem at row row.

	"""

def BCListViewSetSortingColumn(lv, col, ascending):

	"""

	Sets the column according to which sorting will be performed.
	If sorting column is -1, sorting is disabled and the user cannot sort columns by clicking on the column headers. If column is larger than the number of columns the user must click on a column header to sort the ListView. 
	WARNING: In order to avoid performance issues, it is recommended that sorting is disabled on mass items modifications (items text change, adding items etc).
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@ascending boolean: set to True for ascending or to False for descending sorting.

	"""

def BCListViewSortColumn(lv):

	"""

	Returns the column by which the list view is sorted, or -1 if sorting is disabled.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: the index of the sorting column, or -1 if sorting is disabled.

	"""

def BCListViewSortOrder(lv):

	"""

	Returns the sorting order of the list view items.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: 1 if sorting is ascending or 0 if sorting is descending.

	"""

def BCListViewSort(lv):

	"""

	Sorts the ListView using the last sorting configuration (sort column and ascending/descending).
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	"""

def BCListViewItemSetText(item, col, text):

	"""

	Sets the text at column col for ListViewItem item to be text.
	The standard text is aligned left.
	WARNING: In order to avoid performance issues, it is recommended that sorting in list is disabled on mass items text change.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@text string: the new text.

	"""

def BCListViewItemSetDate(item, col, y, m, d):

	"""

	Sets the item item at column col to display date.
	WARNING: Items that provide date (and time) cannot currently be renamed. Item item at column col will be set rename disabled.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@y integer: the year in range 1752-8000.

	@m integer: the month in range 1-12.

	@d integer: the day in range 1-31.

	"""

def BCListViewItemSetDateTime(item, col, y, m, d, h, min, sec):

	"""

	Sets the item item at column col to provide date and time.
	Time format is HH:MM:SS. See an example, assuming the time is 16:45:08. Time is always placed on the right of date.
	WARNING: Items that provide date (and time) cannot currently be renamed. Item item at column col will be set rename disabled.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@y integer: the year in range 1752-8000.

	@m integer: the month in range 1-12.

	@d integer: the day in range 1-31.

	@h integer: the hour in range 0-23.

	@min integer: the minute in range 0-59.

	@sec integer: the seconds in range 0-59.

	"""

def BCListViewAddItem(lv, numCols, text, rename):

	"""

	Adds a top level item to ListView lv.
	
	If you want to insert an item without any data at this point use the much faster BCListViewAddTopLevelItem().
	This convenience function will also
	- set the text as text
	- set the rename type as rename
	- apply contents alignment with respect to BCListViewSetColumnAlignment()
	for each item cell.
	WARNING: If no sorting enabled in the list, the item's position (first or last) depends on BCListViewSetAddItemsInReverseOrderEnabled().
	WARNING: In order to avoid performance issues, it is recommended that sorting in list is disabled on mass adding items.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@numCols integer: the number of columns

	@text object: an array of strings with the text for each column

	@rename object: an array of values with the rename type of each cell. See BCEnumRenameType for details.

	@returns: The created ListViewItem

	"""

def BCListViewItemAddItem(item, numCols, text, rename):

	"""

	Adds an item as a child of item (parent item).
	If you want to insert an item without any data at this point use the much faster BCListViewItemAddChild().
	This convenience function will also
	- set the text as text
	- set the rename type as rename
	- apply contents alignment with respect to BCListViewSetColumnAlignment()
	for each item cell.
	WARNING: If no sorting enabled in the list, the item's position (first or last) depends on BCListViewSetAddItemsInReverseOrderEnabled().
	WARNING: In order to avoid performance issues, it is recommended that sorting in list is disabled on mass adding items.
	This function is not supported under VR mode.
	


	@item object: the parent item

	@numCols integer: the number of columns

	@text object: an array of strings with the text for each column

	@rename object: an array of values with the rename type of each cell. See BCEnumRenameType for details.

	@returns: The created ListViewItem.

	"""

def BCListViewSetIsRootDecorated(lv, decorated):

	"""

	Sets whether the ListView will show controls for expanding/collapsing top level items (default false).
	Makes sense in tree views and is usually a (+) sign for closed items and a (-) sign for expand items.
	Decoration can only be provided in items of the first added column (index 0).
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@decorated boolean: set True to show expand/collapse controls or False otherwise (default).

	"""

def BCListViewGetItem(lv, row):

	"""

	Function is obsolete. Use BCListViewGetTopLevelItem() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@row integer: the row.

	@returns: the top level item at the given row.

	"""

def BCListViewItemGetInt(item, col):

	"""

	Returns the value of ListViewItem item at column col in int format.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: the text of column col of ListViewItem item in int format.

	"""

def BCListViewItemGetDouble(item, col):

	"""

	Returns the value of ListViewItem item at column col in double format.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: the text of column col of ListViewItem item in double format.

	"""

def BCListViewItemGetText(item, col):

	"""

	Returns the value of the ListViewItem item at column col, or None if column col does not exist.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: the text of column col of ListViewItem item, or None if column col does not exist or has no text.

	"""

def BCListViewItemSetUserData(item, data):

	"""

	Assigns user data data to ListViewItem item.
	These data can be retrieved anytime using BCListViewItemGetUserData().
	This function is not supported under VR mode.
	


	@item object: the ListView item of which the user's data will be set.

	@data anything: the user's data.

	"""

def BCListViewItemGetUserData(item):

	"""

	Returns the user's data associated with ListViewItem item.
	These data have been previously assigned using BCListViewItemSetUserData().
	This function is not supported under VR mode.
	


	@item object: the ListViewItem whose user's data will be returned.

	@returns: the user's data associated with ListViewItem item.

	"""

def BCListViewItemIsSelected(item):

	"""

	Returns True if item is selected, or False otherwise.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem that will be checked.

	@returns: True if item is selected; False otherwise

	"""

def BCListViewTopLevelItemCount(lv):

	"""

	Returns the number of top-level (parentless) items in ListView lv.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: The number of top-level items in ListView lv.

	"""

def BCListViewColumns(lv):

	"""

	Returns the number of columns in ListView lv.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: the number of columns in lv.

	"""

def BCListViewItemChildCount(item):

	"""

	Returns the number of immediate children of item.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem whose number of children will be counted.

	@returns: the number of immediate children of item.

	"""

def BCListViewItemSetRectangleColor(item, col, r, g, b):

	"""

	Displays a colored rectangle at col, specified by RGB (red, green and blue) components.
	The color is specified in RGB format by r g and b. If you use invalid values (out of 0..255 range), the rectangle will be cleared.
	The standard rectangle color box is aligned center.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@r integer: the value for red (0 - 255).

	@g integer: the value for green (0 - 255).

	@b integer: the value for blue (0 - 255).

	"""

def BCListViewItemSetSelectable(item, selectable):

	"""

	Sets whether ListViewItem item can be selected or not.
	NOTE: The ListViewItem item can still be selected programatically
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@selectable boolean: set this parameter to True for item to be selectable; False otherwise.

	"""

def BCListViewItemIsSelectable(item):

	"""

	Returns whether ListViewItem item can be selected or not.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@returns: True if item can be selected; False otherwise.

	"""

def BCListViewItemGetListView(item):

	"""

	Returns the ListView to which ListViewItem item belongs.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@returns: the ListView to which item belongs.

	"""

def BCListViewItemMoveItem(item, afterItem):

	"""

	Move the item to be after item afterItem, anywhere in the hierarchy.
	Both items must belong to the same ListView. If you want to append you item at the end 
	do not move after the last item, but use BCListViewSetAddItemsInReverseOrderEnabled().
	NOTE: this function will have no effect if sorting is enabled at the list.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem that will be moved.

	@afterItem object: the ListViewItem after which item will be placed.

	"""

def BCListViewItemSetExpanded(item, expand):

	"""

	Expands or collapses ListViewItem item, depending on the values of expand.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@expand boolean: set this parameter to True to expand item, or to False to collapse it.

	"""

def BCListViewItemIsExpanded(item):

	"""

	Returns True if ListViewItem item is expand (expanded), or False if item is closed (collapsed).
	This function is not supported under VR mode.
	


	@item object: the ListViewItem that is checked.

	@returns: True or False depending on the state of item.

	"""

def BCListViewSetSelected(lv, item, selected):

	"""

	Sets item to be selected or not in ListView lv depending on the value of selected.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@item object: the ListViewItem that will be selected or deselected.

	@selected boolean: set this parameter to False to deselect, or True to select item.

	"""

def BCListViewCountSelected(lv):

	"""

	Counts the number of selected items.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: the number of selected items.

	"""

def BCListViewSetSelectionMode(lv, mode):

	"""

	Sets the selection mode of ListView lv to depend on the value of mode (default BCSingle).
	The options are BCSingle, BCMulti and BCNoSelection.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@mode integer: the selection mode. See BCEnumSelectionMode for details.
	
	guitk.constants BCEnumSelectionMode
	This enum type defines the selection mode. Selection is used with BCListViewSetSelectionMode for example.
	 - guitk.constants.BCMulti
	when the user selects an item in the usual way, the previous selection is cleared and the new item is selected. However, if the user presses the Ctrl key when clicking on an item, the clicked item gets toggled and all other items are left untouched. And if the user presses the Shift key while clicking on an item, all items between the current item and the clicked item get selected or unselected, depending on the state of the clicked item. Also, multiple items can be selected by dragging the mouse over them.
	 - guitk.constants.BCSingle
	the user can select only one item. Any already-selected item becomes unselected.
	 - guitk.constants.BCNoSelection
	items cannot be selected.

	"""

def BCListViewGetSelectionMode(lv):

	"""

	Return the selection mode of ListView lv.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: the selection mode (BCSingle, BCMulti or BCNoSelection).

	"""

def BCListViewGetInt(lv, row, col):

	"""

	Returns the value at row row and column col of ListView lv in int format.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@row integer: the row.

	@col integer: the column.

	@returns: the value at (row, col) of ListView lv.

	"""

def BCListViewGetDouble(lv, row, col):

	"""

	Returns the value at row row and column col of ListView lv in double format.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@row integer: the row.

	@col integer: the column.

	@returns: the value at (row, col) of ListView lv.

	"""

def BCListViewGetText(lv, row, col):

	"""

	Returns the text at row row and column col of ListView lv.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@row integer: the row.

	@col integer: the column.

	@returns: the value at (row, col) of ListView lv.

	"""

def BCListViewSelectedRemove(lv):

	"""

	Removes all selected items of ListView lv.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	"""

def BCListViewSelectedMoveUp(lv):

	"""

	Moves the selected items of ListView lv one step up in the same depth.
	NOTE: this function will have no effect if sorting is enabled at the list view. If you try to sort while you move items you may end up in infinite recursion.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	"""

def BCListViewSelectedMoveDown(lv):

	"""

	Moves the selected items of ListView lv one step down in the same depth.
	NOTE: this function will have no effect if sorting is enabled at the list view. If you try to sort while you move items you may end up in infinite recursion.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	"""

def BCListViewSetSelectedMoveMode(lv, mode):

	"""

	Sets the moving mode of list view for its items (default BCMoveModeSameDepth).
	If you set BCMoveModeNoRestriction mode then you can select different depth items and move them simultaneously.
	NOTE: The selected items will not change their position in the tree hierarchy regardless the moving mode.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@mode integer: the restrictions to be set for moving the items. Default value is BCMoveModeSameDepth.
	See BCEnumSelectedMoveMode for details.
	
	guitk.constants BCEnumSelectedMoveMode
	This enum type describes how the selected items of a Listview will be moved when the appropriate function is called. Items always move in the same depth.
	you can select different depth items and move them simultaneously. Note that the items always move in the same depth.
	 - guitk.constants.BCMoveModeNoRestriction
	Selected items from different depths can move simultaneously (in the same depth).
	 - guitk.constants.BCMoveModeSameDepth
	The selected items with same depth can move (in the same depth).

	"""

def BCListViewSelectedSetColumnDouble(lv, col, val):

	"""

	Sets the text at column col to val for all selected items of ListView lv.
	Optimizes performance compared to set double value item by item.
	Default precision for conversion is 6 digits. You can set with BCListViewSetRenameItemPrecision().
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column.

	@val float: the double value to which the column text will be set.

	"""

def BCListViewSelectedSetColumnInt(lv, col, val):

	"""

	Sets the text at column col to val for all selected items of ListView lv.
	Optimizes performance compared to set integer value item by item.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column.

	@val integer: the integer value to which the column text will be set.

	"""

def BCListViewSelectedSetColumnText(lv, col, text):

	"""

	Sets the text at column col to text for all selected items of ListView lv.
	Optimizes performance compared to set text value item by item.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column.

	@text string: the string to which the column text will be set.

	"""

def BCListViewSetMousePressedFunction(lv, funct, data):

	"""

	Sets the function that will be called when a mouse button is pressed on a ListView.
	WARNING: If you wish to delete a ListViewItem in funct, do so by using a Timer. If you don't use a Timer the result will be undefined.
	Mouse press and click events may change the selected item(s), a user activity discoverable using BCListViewSetSelectionChangedFunction().
	This function is not supported under VR mode.
	


	@lv object: the ListView whose mouse pressed function will be set.

	@funct callback: the function that will be called. See BC_LISTVIEW_MOUSE_PRESSED_FUNCTION for details.
	integer BC_LISTVIEW_MOUSE_PRESSED_FUNCTION(lv, mb, item, col, data)
	The function to be called when a mouse button is pressed on a ListView.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	mb    integer   the mouse button pressed. See BCEnumButtonState for details.
	item  object    the ListViewItem that is selected.
	col   integer   the ListViewItem column where button was pressed.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewSetDoubleClickedFunction(lv, funct, data):

	"""

	Sets the function that will be called when the user double clicks on the ListView.
	
	WARNING: If you wish to delete a ListViewItem in funct, do so by using a Timer. If you don't use a Timer the result will be undefined.
	In funct return 1 if you want to prevent item from expanding (expand) its children if any, otherwise return 0.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called. See BC_LISTVIEW_DOUBLE_CLICK_FUNCTION for details.
	integer BC_LISTVIEW_DOUBLE_CLICK_FUNCTION(lv, item, col, data)
	The function to be called when the user double clicks on the list.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	item  object    the ListViewItem under the mouse.
	col   integer   the ListView column.
	data  anything  anything that may be required in function.
	
	Return: Return 1 if you want to prevent item from expanding its children (if any) otherwise return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewSetDeletePressedFunction(lv, funct, data):

	"""

	Sets the function that will be called when the 'Delete' key is pressed inside ListView.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called. See BC_LISTVIEW_DELETE_PRESSED_FUNCTION for details.
	integer BC_LISTVIEW_DELETE_PRESSED_FUNCTION(lv, data)
	The function to be called whenever the user presses the DEL key in the list view.
	Delete key may change the selection at multi selection list view (when multiple items selected and Delete key pressed).
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	data  anything  anything that may be required in function.
	
	Return: 1 to block the event otherwise return 0 (selection may change).

	@data anything: (optional)any data required by funct.

	"""

def BCListViewClear(lv):

	"""

	Removes and deletes all the items from the list view.
	NOTE: If at least one item is selected, the selection change call back will run.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	"""

def BCListViewSetSelectionChangedFunction(lv, funct, data):

	"""

	Sets a function that will be called when the selection in ListView lv changes.
	That is when items are selected/deselected. Selection may change on a user mouse button click, keyboard press or programmatically.
	WARNING: If you wish to delete a ListViewItem in funct, do so by using a Timer. If you don't use a Timer the result will be undefined.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called when selection changes. See BC_LISTVIEW_SELECTION_CHANGED_FUNCTION for details.
	integer BC_LISTVIEW_SELECTION_CHANGED_FUNCTION(lv, data)
	The function to be called when the selection in ListView lv changes.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by function funct.

	"""

def BCListViewAddColumn(lv, text, width):

	"""

	Adds a column with header text.
	If you set width -1, the column will be automatically adjusted on ListView show and on items insertion (BCMaximumMode).
	It is not a good practice to set a fixed column width (BCManualMode), since font size and header margins are style dependent.
	All columns (apart from the first one) are inserted at the right of the existing ones.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@text string: the text that will be displayed on the header.

	@width integer: the width in pixels. If you use -1 the width is set automatically.

	@returns: the index of the new column.

	"""

def BCListViewSetColumnWidth(lv, col, width):

	"""

	Sets the width of column col to be width pixels.
	It is not a good practice to set a fixed column width (BCManualMode), since font size and header margins are style dependent.
	You can set mode (BCListViewSetColumnWidthMode) to BCMaximumMode for automatically adjust.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@width integer: the new width of col.

	"""

def BCListViewColumnWidth(lv, col):

	"""

	Returns the width of column col.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@returns: the width of col.

	"""

def BCListViewHideColumn(lv, col):

	"""

	Hides the column specified by col.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	"""

def BCListViewShowColumn(lv, col):

	"""

	Shows the column specified by col.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	"""

def BCListViewRemoveColumn(lv, col):

	"""

	Removes the column specified by col.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	"""

def BCListViewSetColumnAlignment(lv, col, alignment):

	"""

	Sets the alignment of ListViewItems for column col to alignment.
	The standard item aligns text/icon left while widgets (check box, radio button and rect color) aligns at center.
	The function will iterate to all items applying the alignment (BCListViewItemSetContentsAlignment).
	Alignment applied to content type
	- text
	- icon only
	- check box
	- radio button
	- rectangle color
	- sibling colors
	NOTE: Alignment consist of horizontal and vertical components. If you only use the horizontal component (BCAlignLeft-BCAlignHCenter-BCAlignRight), 
	the BCAlignVCenter will be attached to ensure uniform behavior. 
	For example, if you apply BCAlignRight the applied value is actually the combination of BCAlignRight | BCAlignVCenter.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@alignment integer: the alignment for the column col. It is an integer value that is composed of BCEnumAlignment OR'ed (i.e. added) together. 
	See BCEnumAlignment for details.
	
	guitk.constants BCEnumAlignment
	This enum type is used to describe alignment. It contains horizontal and vertical flags. Alignment is used with BCGridLayoutAddMultiCellWidget for example.
	NOTE: You can use at most one horizontal and one vertical flag at a time.
	 - guitk.constants.BCAlignAuto
	aligns according to the language. Left for most, right for Arabic and Hebrew.
	 - guitk.constants.BCAlignLeft
	aligns with the left edge.
	 - guitk.constants.BCAlignRight
	aligns with the right edge.
	 - guitk.constants.BCAlignHCenter
	centers horizontally in the available space.
	 - guitk.constants.BCAlignJustify
	justifies the text in the available space.
	 - guitk.constants.BCAlignTop
	aligns with the top.
	 - guitk.constants.BCAlignBottom
	aligns with the bottom.
	 - guitk.constants.BCAlignVCenter
	centers vertically in the available space.
	 - guitk.constants.BCAlignCenter
	centers in both dimensions (vertically and horizontally).
	 - guitk.constants.BCAlignHorizontal_Mask
	horizontal mask.
	 - guitk.constants.BCAlignVertical_Mask
	vertical mask.
	 - guitk.constants.BCAlignVJustify
	Justifies the text vertically in the available space.

	"""

def BCListViewSetColumnWidthMode(lv, col, mode):

	"""

	Sets col column's width mode (how column width responds to contents change) to mode.
	BCManualMode does not automatically change column width. On BCMaximumMode mode the column adjust (on ListView show and on item insertion) to fit the largest item text.
	If column with index 0 has BCMaximumMode and you expand an item, it will adjust its width. Width mode is initialised when adding columns (BCListViewAddColumn()).
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@mode integer: the width mode. See BCEnumWidthMode for details.
	
	guitk.constants BCEnumWidthMode
	This enum describes how the width of a column in a ListView changes.
	 - guitk.constants.BCManualMode
	The column width does not change automatically.
	 - guitk.constants.BCMaximumMode
	The column is always resized to the width of the item with the largest width in the column.

	"""

def BCListViewSetMultipleItemsRenameEnabled(lv, col, enable):

	"""

	Set whether ListView lv enables multiple items renaming for column col.
	If this property is enabled, then the user can select multiple items and if succesfully rename one
	of them, then all renamable non disabled selected items in same column, will get the same text value.
	The default listview column has this property false.
	This property only has a meaning for multi selection lists.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@enable boolean: set 1 to enable or 0 to disable multiple items rename property.

	"""

def BCListViewInvertSelection(lv):

	"""

	Inverts the current item selection on ListView. Turns selected items to unselected and vice versa.
	If ListView is single selection nothing happen.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	"""

def BCListViewItemSetBold(item, enable):

	"""

	Sets the font of ListViewItem item to bold if enable is 1 or to normal if enable is 0.
	This function affects all columns of item. By default a ListViewItem is painted non-bold.
	WARNING: There are some fonts that do not support bold style at all. In these case nothing will happen.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@enable boolean: use True to set current font to bold and False to unset.

	"""

def BCListViewItemBold(item):

	"""

	Returns True if item item is painted in bold font or False otherwise.
	WARNING: There are some fonts that do not support bold fonts at all. In these cases you will not get what you see.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@returns: True if item is painted in bold font, False otherwise.

	"""

def BCListViewItemColumnSetBold(item, col, enable):

	"""

	Sets the font of ListViewItem item column col to bold if enable is 1 or to normal if enable is 0 (default).
	WARNING: There are some fonts that do not support bold style at all. In these case nothing will happen.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@enable boolean: use True to set current font to bold and False to unset.

	"""

def BCListViewItemSetItalic(item, enable):

	"""

	Sets the font of ListViewItem item to italic if enable is 1 or to normal if enable is 0 (default).
	This function affects item in all columns. 
	WARNING: There are some fonts that do not support italic style at all. In these case nothing will happen.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@enable boolean: use True to set current font to italic and False to unset.

	"""

def BCListViewItemItalic(item):

	"""

	Returns True if ListViewItem item is painted in italic font or False otherwise.
	WARNING: There are some fonts that do not support italic fonts at all. In these cases you will not get what you see.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@returns: True if item is painted in italic font, False otherwise.

	"""

def BCListViewItemSetStrikeOut(item, enable):

	"""

	Sets/unsets the text to drawn with a horizontal line through the center of it.
	This function affects item in all columns. A ListViewItem is painted by default with non-strike out font.
	WARNING: There are some fonts that do not support strike out style at all. In these case nothing will happen.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@enable boolean: True to strike out text and False to unset.

	"""

def BCListViewItemStrikeOut(item):

	"""

	Returns True if ListViewItem item is strike out (horizontal line through the center of it) or False otherwise (default).
	WARNING: There are some fonts that do not support strike out at all. In these cases you will not get what you see.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@returns: True if item text is strike out, False otherwise.

	"""

def BCListViewItemSetForegroundColor(item, mode, r, g, b):

	"""

	Sets a foreground (text) color to a ListViewItem.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem whose foreground color will be changed.

	@mode integer: BCNormalMode and BCSelectedMode is only supported. See BCEnumMode for details.
	
	guitk.constants BCEnumMode
	This enum type describes a Button's pixmap or a ListViewItem's mode.
	 - guitk.constants.BCNormalMode
	The user does not interact with the Button or the ListViewItem, but their functionality is available.
	 - guitk.constants.BCDisabledMode
	The user cannot interact with the Button.
	 - guitk.constants.BCActiveMode
	Button: The user mouse cursor is over button or button is pressed (only for ToolButtons).
	 - guitk.constants.BCSelectedMode
	Button: Display the pixmap when the item represented by the icon is selected.
	ListViewItem: The item is selected.

	@r integer: the value of RED of the RGB foreground color.

	@g integer: the value of GREEN of the RGB foreground color.

	@b integer: the value of BLUE of the RGB foreground color.

	"""

def BCListViewItemSetBackgroundColor(item, mode, r, g, b):

	"""

	Sets a custom background color to a ListViewItem.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem whose background color will be changed.

	@mode integer: BCNormalMode and BCSelectedMode is only supported. See BCEnumMode for details.
	
	guitk.constants BCEnumMode
	This enum type describes a Button's pixmap or a ListViewItem's mode.
	 - guitk.constants.BCNormalMode
	The user does not interact with the Button or the ListViewItem, but their functionality is available.
	 - guitk.constants.BCDisabledMode
	The user cannot interact with the Button.
	 - guitk.constants.BCActiveMode
	Button: The user mouse cursor is over button or button is pressed (only for ToolButtons).
	 - guitk.constants.BCSelectedMode
	Button: Display the pixmap when the item represented by the icon is selected.
	ListViewItem: The item is selected.

	@r integer: the value of RED of the RGB background color.

	@g integer: the value of GREEN of the RGB background color.

	@b integer: the value of BLUE of the RGB background color.

	"""

def BCListViewItemResetForegroundColor(item, mode):

	"""

	Resets the foreground color of a ListViewItem to the default one.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem whose foreground color will be reset. The new color will be in accordance with the colors of the parent ListView.

	@mode integer: BCNormalMode and BCSelectedMode is only supported. See BCEnumMode for details.
	
	guitk.constants BCEnumMode
	This enum type describes a Button's pixmap or a ListViewItem's mode.
	 - guitk.constants.BCNormalMode
	The user does not interact with the Button or the ListViewItem, but their functionality is available.
	 - guitk.constants.BCDisabledMode
	The user cannot interact with the Button.
	 - guitk.constants.BCActiveMode
	Button: The user mouse cursor is over button or button is pressed (only for ToolButtons).
	 - guitk.constants.BCSelectedMode
	Button: Display the pixmap when the item represented by the icon is selected.
	ListViewItem: The item is selected.

	"""

def BCListViewItemResetBackgroundColor(item, mode):

	"""

	Resets the background color of a ListViewItem to the default one.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem whose background color will be reset. The new color will be in accordance with the colors of the parent ListView.

	@mode integer: BCNormalMode and BCSelectedMode is only supported. See BCEnumMode for details.
	
	guitk.constants BCEnumMode
	This enum type describes a Button's pixmap or a ListViewItem's mode.
	 - guitk.constants.BCNormalMode
	The user does not interact with the Button or the ListViewItem, but their functionality is available.
	 - guitk.constants.BCDisabledMode
	The user cannot interact with the Button.
	 - guitk.constants.BCActiveMode
	Button: The user mouse cursor is over button or button is pressed (only for ToolButtons).
	 - guitk.constants.BCSelectedMode
	Button: Display the pixmap when the item represented by the icon is selected.
	ListViewItem: The item is selected.

	"""

def BCListViewItemSetEnabled(item, enabled):

	"""

	Enables or disables the ListViewItem item.
	The default ListViewItem is enabled.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@enabled boolean: set to False if you want to disable the item, otherwise True.

	"""

def BCListViewItemIsEnabled(item):

	"""

	Informs the user whether the ListViewItem item is enabled or not.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@returns: True if the item is enabled or False if it is disabled.

	"""

def BCListViewItemSetRenamedFunction(item, funct, data):

	"""

	Sets the function that will be called when renaming of a column of ListViewItem item is completed (data have been committed).
	Use view oriented BCListViewSetRenameItemFinishedFunction() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@funct callback: the function that will be called. See BC_LISTVIEWITEM_RENAMED_FUNCTION for details.
	integer BC_LISTVIEWITEM_RENAMED_FUNCTION(item, col, data)
	The function to be called when renaming of a column of item is completed.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	item  object    the ListViewItem.
	col   integer   the ListViewItem column.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewItemSetRenameCanceledFunction(item, funct, data):

	"""

	Sets the function that will be called when renaming of a column of ListViewItem item has been canceled.
	Use view oriented BCListViewSetRenameItemFinishedFunction() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@funct callback: the function that will be called. See BC_LISTVIEWITEM_RENAME_CANCELED_FUNCTION for details.
	integer BC_LISTVIEWITEM_RENAME_CANCELED_FUNCTION(item, col, data)
	The function to be called when renaming of a column of item is canceled.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	item  object    the ListViewItem.
	col   integer   the ListViewItem column.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewItemSetIconFileName(item, col, fileName):

	"""

	Sets the icon that is displayed on column col of item to be the one specified by fileName.
	Icons are always displayed on the left of text.
	If an empty string is passed into this function, the icon is cleared.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@fileName string: the icon file name (absolute or relative).

	"""

def BCListViewItemHasIcon(item, col):

	"""

	Returns True if item has icon at column col, False otherwise.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: False if there is no icon (default) at column col, True otherwise.

	"""

def BCListViewItemSetCheckable(item, checkable):

	"""

	Sets whether the ListViewItem is user checkable, i.e provides a check box next to the item's text for column index 0.
	The standard item is not checkable.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@checkable boolean: True sets item to be checkable, False sets it to be non checkable.

	"""

def BCListViewItemIsCheckable(item):

	"""

	Returns True if item is checkable, or False otherwise.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@returns: True or False depending on the checkable state of item.

	"""

def BCListViewItemCheckableSetOn(item, on):

	"""

	Sets the ListViewItem checkable to be checked or unchecked, depending on the value of on.
	If item is not checkable nothing happens.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@on boolean: True sets item to checked, False sets it to unchecked.

	"""

def BCListViewItemCheckableIsOn(item):

	"""

	Returns True if item is checked, or False otherwise.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@returns: True or False depending on the state of item.

	"""

def BCListViewItemCheckableSetToggledFunction(item, funct, data):

	"""

	Sets the function to be called when checkable ListViewItem item check state change.
	This function is not supported under VR mode.
	


	@item object: the checkable ListViewItem.

	@funct callback: the function that is called. See BC_LISTVIEWITEM_CHECKABLE_TOGGLED_FUNCTION for details.
	integer BC_LISTVIEWITEM_CHECKABLE_TOGGLED_FUNCTION(item, state, data)
	The function to be called when checkable ListViewItem item is checked or unchecked.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	item   object    the checkable ListViewItem.
	state  integer   the toggle state information: 1 when the BCPushButton is on (i.e. toggled); 0 otherwise.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any user data required by function funct.

	"""

def BCListViewItemGetItemAbove(item):

	"""

	Returns the ListViewItem above item or None if there is no ListViewItem above.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@returns: The ListViewItem above item.

	"""

def BCListViewItemGetItemBelow(item):

	"""

	Returns the ListViewItem below item or None if there is no ListViewItem below.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@returns: The ListViewItem below item.

	"""

def BCListViewItemEnsureVisible(item):

	"""

	Ensures that item item is visible.
	This means scrolling the ListView vertically if necessary and opening (expanding) any parent items if this is required to show the item.
	This function is not supported under VR mode.
	


	@item object: the item.

	"""

def BCListViewItemEnsureVisibleTop(item):

	"""

	Ensures that item item is visible and scrolls the vertical bar (if available), such as item is the top visible item.
	This also means opening (expanding) any parent items if this is required to show the item. 
	NOTE: Top suffix refers to the position in the ListView's viewport, not the level of the item.
	This function is not supported under VR mode.
	


	@item object: the item that will be visible.

	"""

def BCListViewItemIsVisible(item):

	"""

	Returns True if ListViewItem item is visible, False otherwise.
	The return value depends on the attribute that explicitly was set with BCListViewItemSetVisible().
	NOTE: The return value does not depend whether item is physically visible, i.e.
	- an item that currently not drawn at the viewport (you have to scroll down to find it) can be visible.
	- a child item that is collapsed to its parent can be visible.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@returns: True if item is visible, False otherwise.

	"""

def BCListViewItemSetVisible(item, visible):

	"""

	Sets whether ListViewItem item will be visible (default) or not.
	If you want to modify item's selectability, use BCListViewItemSetSelectable().
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@visible boolean: set True to show or False to hide the item.

	"""

def BCListViewItemSetCheckBox(item, col, checked, funct, data):

	"""

	Sets a checkbox to be displayed in the ListViewItem item cell specified by the given column col.
	If you want to set a check box together with text use BCListViewItemSetCheckable().
	You can also use generic item widget functions BCListViewItemWidgetSetVisible(), BCListViewItemWidgetSetEnabled() and BCListViewItemWidgetDestroy().
	The standard check box is aligned center.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@checked boolean: whether the checkBox will be initially set to checked or not ( True for checked, False otherwise ).

	@funct callback: a callback function that will be called every time the checkBox will be checked or unchecked. 
	See BC_LISTVIEWITEM_CHECKBOX_TOGGLED_FUNCTION for details.
	integer BC_LISTVIEWITEM_CHECKBOX_TOGGLED_FUNCTION(item, col, state, data)
	The function to be called everytime the checkBox will be checked or unchecked.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	item   object    the ListViewItem.
	col    integer   the ListViewItem column in which the checkBox is found.
	state  integer   the new value of the checkBox: 1 if checked; 0 otherwise.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewItemCheckBoxSetChecked(item, col, check):

	"""

	Sets the value of the checkBox at item item.
	If you want to change the value without the call back to run, use BCBlockCallBackFunctions() (remember to unblock).
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@check boolean: the value to be set.

	"""

def BCListViewItemCheckBoxIsChecked(item, col):

	"""

	Returns 1 if the checkBox at column col of ListViewItem item is checked, or 0 otherwise.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: 1 if the checkBox at column col of ListViewItem item is checked, or 0 otherwise.

	"""

def BCListViewItemCheckBoxSetDim(item, col, dim):

	"""

	Sets the dim (middle) value of the checked checkBox at item item.
	Check box can be drawn dimmed only when it is checked.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@dim boolean: set 1 to turn it dimmed (middle state), otherwise set 0 for regular check.

	"""

def BCListViewItemIsCheckBox(item, col):

	"""

	Returns True if the ListViewItem item cell displays a check box at given column col, or False otherwise.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem

	@col integer: the column index.

	@returns: True if the ListViewItem item at column col is a checkBox, or False otherwise.

	"""

def BCListViewButtonGroupCreate(lv, col):

	"""

	Creates an non visible object that treats a group of radio button items exclusively.
	Once you create the group insert items in it and they will operate exclusively. Exclusive property means that to untoggle a radio button you must mouse press on another radio button in the group.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@returns: the created BCListViewButtonGroup.

	"""

def BCListViewButtonGroupSetMousePressedFunction(lvbg, funct, data):

	"""

	Set the function to be called when a radio button in the group is pressed.
	This function is not supported under VR mode.
	


	@lvbg object: the ListViewButtonGroup.

	@funct callback: a callback function that will be called every time the radio button inside group lvbg will be toggled. 
	See BC_LISTVIEW_BUTTONGROUP_MOUSE_PRESSED_FUNCTION for details.
	integer BC_LISTVIEW_BUTTONGROUP_MOUSE_PRESSED_FUNCTION(lvbg, item, col, data)
	The function to be called everytime a radio button in the group is pressed.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lvbg  object    the ListViewButtonGroup.
	item  object    the ListViewItem.
	col   integer   the ListViewItem column.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewButtonGroupSetChecked(lvbg, item):

	"""

	Set the selected radio button of button group lvbg to the radio at item.
	This function is not supported under VR mode.
	


	@lvbg object: the ListViewButtonGroup.

	@item object: the ListViewItem.

	"""

def BCListViewButtonGroupInsertItem(lvbg, item):

	"""

	Insert item item to be managed exclusively by button group lvbg.
	This function is not supported under VR mode.
	


	@lvbg object: the ListViewButtonGroup.

	@item object: the ListViewItem.

	"""

def BCListViewButtonGroupRemoveItem(lvbg, item):

	"""

	Removes item item from button group lvbg. Does not delete item item.
	This function is not supported under VR mode.
	


	@lvbg object: the ListViewButtonGroup.

	@item object: the ListViewItem.

	"""

def BCListViewItemSetRadioButton(item, col, checked, funct, data):

	"""

	Sets a radio button to be displayed in the ListViewItem item cell specified by the given column col.
	Radio buttons inside items do not operate exclusively by default. Use ListViewButtonGroup to treat them exclusively.
	You can also use generic item widget functions BCListViewItemWidgetSetVisible(), BCListViewItemWidgetSetEnabled() and BCListViewItemWidgetDestroy().
	The standard radio button aligned center.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@checked boolean: whether the radio button will be initially set to checked or not ( True for on, False otherwise ).

	@funct callback: a callback function that will be called every time the radio button will be toggled. 
	See BC_LISTVIEWITEM_RADIOBUTTON_TOGGLED_FUNCTION for details.
	integer BC_LISTVIEWITEM_RADIOBUTTON_TOGGLED_FUNCTION(item, col, state, data)
	The function to be called everytime the radio button will change status (on/off).
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	item   object    the ListViewItem.
	col    integer   the ListViewItem column.
	state  integer   the new value of the radio button: 1 if turned on; 0 otherwise.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewItemRadioButtonSetChecked(item, col, check):

	"""

	Sets the value (on/off) of the radio button at item item.
	If you want to change the value without the call back to run, use BCBlockCallBackFunctions() (remember to unblock).
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@check boolean: 1 to turn it on or 0 to turn it off.

	"""

def BCListViewItemRadioButtonIsChecked(item, col):

	"""

	Returns 1 if the radio button at column col of ListViewItem item is on, or 0 otherwise.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: 1 if the radio button at column col of ListViewItem item is on, or 0 otherwise.

	"""

def BCListViewItemIsRadioButton(item, col):

	"""

	Returns True if the ListViewItem item cell displays a radio button at given column col, or False otherwise.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: True if the ListViewItem item at column col is a radio button, or False otherwise.

	"""

def BCListViewItemSetButton(item, col, funct, data):

	"""

	Sets a push button to be displayed in the ListViewItem item cell specified by the given column col.
	You can also use generic item widget functions BCListViewItemWidgetSetVisible(), BCListViewItemWidgetSetEnabled() and BCListViewItemWidgetDestroy().
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@funct callback: a callback function that will be called every time the button will be clicked.
	See BC_LISTVIEWITEM_BUTTON_CLICKED_FUNCTION for details.
	integer BC_LISTVIEWITEM_BUTTON_CLICKED_FUNCTION(item, col, data)
	The function to be called everytime the button will be clicked.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	item  object    the ListViewItem.
	col   integer   the ListViewItem column at which the button is found.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewItemButtonSetText(item, col, text):

	"""

	Sets text as label of the button of item at col.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem that contains the button.

	@col integer: the column index.

	@text string: the label of the button.

	"""

def BCListViewItemButtonText(item, col):

	"""

	Returns the button's label of item at col.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem that contains the button.

	@col integer: the column index.

	@returns: the label of the button.

	"""

def BCListViewItemButtonSetIconFileName(item, col, fileName):

	"""

	Sets an icon with file name fileName to the button of item at col.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem that contains the button.

	@col integer: the column index.

	@fileName string: the filename of the icon.

	"""

def BCListViewItemButtonIconFileName(item, col):

	"""

	Returns the file name of the icon that has been set to the button of item at col.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem that contains the button.

	@col integer: the column index.

	@returns: the filename of the icon.

	"""

def BCListViewItemIsButton(item, col):

	"""

	Returns True if the ListViewItem item cell displays a push button at given column col, or False otherwise.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem

	@col integer: the column index.

	@returns: True if the ListViewItem item at column col has button, or False otherwise.

	"""

def BCListViewItemDepth(item):

	"""

	Returns the depth of item item.
	Top level items have depth 0.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem to be tested.

	@returns: the depth of an item.

	"""

def BCListViewItemSetToolTip(item, col, tip):

	"""

	Sets the tooltip (balloon help) for list view item item at column col to the text specified by tip.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@tip string: the text to be displayed at balloon help.

	"""

def BCListViewItemSetRenameType(item, col, type):

	"""

	Defines what data type (integer, string) item accepts for column col when renamed.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@type integer: See BCEnumRenameType for more details.
	
	guitk.constants BCEnumRenameType
	This enum type is used to describe the data type of the editor on ListViewItem rename.
	 - guitk.constants.BCRenameType_None
	The item cannot be renamed by the user.
	 - guitk.constants.BCRenameType_Double
	Rename editor accepts double values.
	 - guitk.constants.BCRenameType_Int
	Rename editor accepts integer values.
	 - guitk.constants.BCRenameType_String
	Rename editor accepts any string value.

	"""

def BCListViewItemRenameType(item, col):

	"""

	Returns what data type (integer, string) item accepts for column col when renamed.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: The rename data type. See BCEnumRenameType for more details.
	BCEnumRenameType: This enum type is used to describe the data type of the editor on ListViewItem rename.
	guitk.constants.BCRenameType_None: The item cannot be renamed by the user.
	guitk.constants.BCRenameType_Double: Rename editor accepts double values.
	guitk.constants.BCRenameType_Int: Rename editor accepts integer values.
	guitk.constants.BCRenameType_String: Rename editor accepts any string value.

	"""

def BCListViewItemRenameEnabled(item, col):

	"""

	Returns True if rename is enabled (rename type different from BCRenameType_None) for column col of ListViewItem item, or False otherwise.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: True if rename is enabled for column (rename type different from BCRenameType_None) col of item; False otherwise.

	"""

def BCListViewSetFilterEnabled(lv, enable):

	"""

	Sets whether the ListView lv provides a filter button on the right of the header or not.
	If you enable this property a (toggle) button at the right of header will be shown.
	This button shows/hides a line below header accommodating widgets able to filter the ListView per column. 
	The default filter provides line edits. If you have column with checkBoxes you will filter with a tristate checkBox. If you have a small finite number of item names you are able to use a comboBox as well.
	While you filter you can see the full query at the bottom of the ListView, comprised by multiple ANDed conditions. Filter operates as you type, but it is recommended to disable this property for ListViews with large number of items, and filter when Enter pressed. You can also set the filter to be case sensitive or not.
	WARNING: If you have columns with numbers or checkBoxes, you have to set the data types for the columns such as the filter to be able to operate correct. See BCListViewSetColumnDataType().
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@enable boolean: set this parameter to True to enable the filter, or to False to disable it.

	"""

def BCListViewIsFilterEnabled(lv):

	"""

	Check if filter is enabled for ListView lv.
	This function is not supported under VR mode.
	


	@lv object: the ListView to check.

	@returns: True if the filter is enabled or False otherwise.

	"""

def BCListViewFilterSetLineEdit(lv, col):

	"""

	Sets the filter at column col to provide line edit (default).
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	"""

def BCListViewFilterSetComboBox(lv, col):

	"""

	Sets the filter at column col to provide comboBox.
	This is useful if you have small finite number of item names, for example all your items may have values 'small', 'medium' and 'large'. The default filter provides line edits.
	WARNING: You are responsible to update the comboBox items (use BCListViewFilterUpdateComboBox()).
	Update it when you finish adding/removing items. An automatic update in a ListView with large number of items would cause really slow behavior.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	"""

def BCListViewFilterSetCheckableMenu(lv, col):

	"""

	Sets whether or not the filter at column col will provide a button with a checkable popup menu.
	It works like the combo box, provided the ability to apply many filter conditions in the same column. First insert your items and then apply the checkable menu because this function will also update the checkable menu.
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	@col integer: the column index.

	"""

def BCListViewFilterUpdateCheckableMenus(lv):

	"""

	Updates all checkable menus (if any) inside filter.
	You will need this function if items inside list view removed dynamically. This function runs a loop to all items, so in lists with large number of items be careful where to use it.
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	"""

def BCListViewSetColumnDataType(lv, col, dataType):

	"""

	Define the data type for column col of your ListView (default BCString).
	This type is used by filter to specify the search method. It is also related with the widget type that will be used inside the filter bar.
	Valid types are
	- BCInt will use a BCLineEditCreateInt() for filtering column col,
	- BCDouble will use a BCLineEditCreateDouble() for filtering column col,
	- BCBool will use a tristate BCCheckBoxCreate() for filtering column col,
	- BCString will use a BCLineEditCreate() for filtering column col,
	- BCDate will use a complex date editor widget for filtering column col.
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	@col integer: the column index.

	@dataType integer: See BCEnumDataType for more details.
	
	guitk.constants BCEnumDataType
	This enum type is used to describe the data type or the widget type of a ListViewItem
	 - guitk.constants.BCInt
	Defines the variant-column as integer.
	 - guitk.constants.BCFloat
	Defines the variant-column as float.
	 - guitk.constants.BCDouble
	Defines the variant-column as double.
	 - guitk.constants.BCString
	Defines the variant-column as string.
	 - guitk.constants.BCStringList
	Defines the variant-column as a list of strings (e.g. possible values of a variant red/green/blue).
	 - guitk.constants.BCBool
	Defines the variant-column as a boolen (e.g. for BCCheckBoxes that only take values 0 or 1).
	 - guitk.constants.BCInvalid
	Defines the variant with an invalid type.
	 - guitk.constants.BCDate
	Defines that the variant-column displays date.

	"""

def BCListViewColumnDataType(lv, col):

	"""

	Returns the data type for column col of ListView lv (default BCString).
	Possible types are
	- BCInt,
	- BCDouble,
	- BCBool,
	- BCString,
	- BCDate.
	This function is not supported under VR mode.
	


	@lv object: the ListView to check.

	@col integer: the column index.

	@returns: the data type of column. See BCEnumDataType.
	BCEnumDataType: This enum type is used to describe the data type or the widget type of a ListViewItem
	guitk.constants.BCInt: Defines the variant-column as integer.
	guitk.constants.BCFloat: Defines the variant-column as float.
	guitk.constants.BCDouble: Defines the variant-column as double.
	guitk.constants.BCString: Defines the variant-column as string.
	guitk.constants.BCStringList: Defines the variant-column as a list of strings (e.g. possible values of a variant red/green/blue).
	guitk.constants.BCBool: Defines the variant-column as a boolen (e.g. for BCCheckBoxes that only take values 0 or 1).
	guitk.constants.BCInvalid: Defines the variant with an invalid type.
	guitk.constants.BCDate: Defines that the variant-column displays date.

	"""

def BCListViewCopyItemsToClipboard(lv, selectedOnly):

	"""

	Copies to application global clipboard the ListViewItems contents of ListView lv.
	Used for copy and paste text data between applications.
	If an item cell contains both text and icon, it will only copy the text.
	If an item cell contains a widget
	- check box and radio button will copy 1 or 0 ragarding its state,
	- button will copy its text (not icon),
	- combo box will copy the text of current item.
	NOTE: If no items are available to for copying, the clipboard remains as is.
	This function is not supported under VR mode.
	


	@lv object: the ListView whose items will be copied.

	@selectedOnly integer: if set to 0, all items will be copied. Only the selected ones, otherwise.

	"""

def BCListViewCopyColumnToClipboard(lv, col, selectedOnly):

	"""

	Copies to application global clipboard the ListViewItem fields of column col, of ListView lv.
	Used for copy and paste text data between applications.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@selectedOnly integer: if set to 0, all item fields will be copied. Only the column fields of the selected items, otherwise.

	"""

def BCListViewFilterButton(lv):

	"""

	Returns the button at the right on the header's ListView that is used to show/hide the filter.
	If filter is not enabled you will get None. 
	WARNING: Do not manage this button (toggle/hide), it operates automatically.
	This function is not supported under VR mode.
	


	@lv object: the ListView to check.

	@returns: The button for show/hide the filter or None otherwise.

	"""

def BCListViewFilterClear(lv):

	"""

	Clears the filter from any condition.
	The widgets of filter are set to their default value (line edits set empty text, checkBoxes to mid state and comboBoxes to 'All'). All ListViewItems will be visible. The cleared function (if any) will operate.
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	"""

def BCListViewFilterCleared(lv):

	"""

	Check if filter of ListView lv is clear (no condition is currently applied).
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: True if filter is clear or  False if at least one condition is currently applied.

	"""

def BCListViewFilterSetFilterAsYouTypeOn(lv, on):

	"""

	Set whether filter is applied while text changes inside line edits (as you type).
	This property can be modified by the menu that popups on the button. In ListViews with large number of items you may need to set off and disable this property (cannot be modified by the user).
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	@on boolean: set True to enable filtering while text changes inside line edits or False otherwise.

	"""

def BCListViewFilterIsFilterAsYouTypeOn(lv):

	"""

	Returns True if the property of applying filter as text changes inside line edits is on or False otherwise.
	This function is not supported under VR mode.
	


	@lv object: the ListView to check.

	@returns: True if filter as you type is on, otherwise returns False.

	"""

def BCListViewFilterSetSelectFilteredOn(lv, on):

	"""

	Sets whether filtered ListViewItems will also be selected.
	This property can be modified by the menu that popups on the button. This is useful if you want to apply a function to the selected items after they have been filtered. Recall that in hierarchical ListViews although an item may be filtered and its parent not, both items will be visible. The default filter has this property on.
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	@on boolean: set True to select the filtered items or False otherwise.

	"""

def BCListViewFilterIsSelectFilteredOn(lv):

	"""

	Returns True if the property of selecting the filtered items is on or False otherwise.
	This function is not supported under VR mode.
	


	@lv object: the ListView to check.

	@returns: True if selecting filtered items is on, otherwise returns False.

	"""

def BCListViewFilterSetCaseSensitiveOn(lv, on):

	"""

	Sets whether filter is case sensitive.
	If case sensitive is on, 'value' matches 'value' but not 'VALUE'. The default filter has this property off. This property can be modified by the menu that popups on the button.
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	@on boolean: set True for case sensitive or False otherwise.

	"""

def BCListViewFilterIsCaseSensitiveOn(lv):

	"""

	Returns True if filter is case sensitive or False otherwise.
	This function is not supported under VR mode.
	


	@lv object: the ListView to check.

	@returns: True if filter is case sensitive, otherwise returns False.

	"""

def BCListViewFilterSetShowChildrenOn(lv, on):

	"""

	Sets whether filter will enforce a filtered item to show and expand its children.
	The children items to be shown is not necessary to agree with filter. The default filter has this property off. This property can be modified by the menu that popups on the button.
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	@on boolean: set True to enforce an item to show its children otherwise set False.

	"""

def BCListViewFilterIsShowChildrenOn(lv):

	"""

	Returns whether filter enforces a filtered item to show and expand its children.
	The default filter has this property off.
	This function is not supported under VR mode.
	


	@lv object: the ListView to check.

	@returns: True if filter enforces filtered items to show and expand their children.

	"""

def BCListViewFilterSetFilterAsYouTypeEnabled(lv, enable):

	"""

	Sets whether the user can modify the filtering when text changes property.
	The default filter has this property on. If you turn off this property, the 'Filter As You Type' option will be disabled in the menu.
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	@enable boolean: set True for enabling the user to have filter as you type property or False otherwise.

	"""

def BCListViewFilterSetSaveListEnabled(lv, enable):

	"""

	Function is not supported. For more info, please contact Customer Service department.
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	@enable boolean: set True for enabling the user to save the ListViews in txt format or False otherwise.

	"""

def BCListViewFilterSetColumnEnabled(lv, col, enable):

	"""

	Sets whether filtering at column col is enabled by the user.
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	@col integer: the column index.

	@enable boolean: set True for enable user input or False otherwise.

	"""

def BCListViewFilterApplyCondition(lv, col, text):

	"""

	Apply a custom condition at a column col.
	The default filter column has a line edit. You can use operators, as well, if you have int or float numbers (for example use '&gt;3'). If filter at column col has a comboBox, the comboBox item with text text will be set as current item and filter will run. If comboBox has not an item with text, nothing happens. If you have checkBox at column col, use '1' or 'true' for checked and '0' or 'false' for unchecked.
	WARNING: Condition cannot be applied in column with checkable menu.
	At the end the function will call filter Applied function.
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	@col integer: the column index.

	@text string: value to filter.

	"""

def BCListViewFilterApply(lv):

	"""

	Apply the current filter.
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	"""

def BCListViewFilterUpdateComboBox(lv, col):

	"""

	Updates the comboBox of filter at column col.
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	@col integer: the column index.

	"""

def BCListViewFilterSetOutputAlwaysHidden(lv, alwaysHidden):

	"""

	Set the filter bottom output to be permanent hidden.
	The default filter has this property false. This means that when filter applied the query 
	is provided on the bottom of the list view.
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	@alwaysHidden boolean: set True to permanent hide the output or False to automatically shown the output if needed.

	"""

def BCListViewSetColumnVisibilityChangedFunction(lv, funct, data):

	"""

	Sets the function to be called on column show/hide.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: is a function that will be called when columns are shown or hidden.
	See BC_LISTVIEW_COLUMN_VISIBILITY_CHANGED_FUNCTION for details.
	integer BC_LISTVIEW_COLUMN_VISIBILITY_CHANGED_FUNCTION(lv, col, visible, data)
	The function to be called when a column was shown/hidden.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv       object    the ListView.
	col      integer   the ListView column.
	visible  integer   1 when column is shown and 0 if was hidden.
	data     anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewSetColumnMovedFunction(lv, funct, data):

	"""

	Sets the function to be called when the user moves column from one position to another.
	When columns are inserted, they obtain a unique unsigned integer identifier. The columns have also a current position in the ListView. Although the columns can move to a different position, column index remains unchanged.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function to be called when the user moves column. See BC_LISTVIEW_COLUMN_MOVED_FUNCTION for details.
	integer BC_LISTVIEW_COLUMN_MOVED_FUNCTION(lv, col, fromPos, toPos, data)
	The function to be called when the user moves column col from position fromPos to position toPos.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv       object    the ListView.
	col      integer   the ListView column to be moved.
	fromPos  integer   the old position of column col.
	toPos    integer   the new position of column col.
	data     anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewSetColumnResizedFunction(lv, funct, data):

	"""

	Sets the function to be called when the user resizes column.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function to be called when the user resizes columns. See BC_LISTVIEW_COLUMN_RESIZED_FUNCTION for details.
	integer BC_LISTVIEW_COLUMN_RESIZED_FUNCTION(lv, col, oldSize, newSize, data)
	The function to be called when the user resizes column col.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv       object    the ListView.
	col      integer   the ListView column that resized.
	oldSize  integer   the old size of resized column col.
	newSize  integer   the new size of resized column col.
	data     anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewSetFilterClearedFunction(lv, funct, data):

	"""

	Set the function to be called when the filter is cleared.
	Filter cleared when no condition left or when clicked the 'Reset' button on the left of the output or untoggle the button that shows/hides filter (on the right of ListView header). 
	NOTE: selected ListViewItems that do not match turn deselected.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function to be called when filter is cleared. See BC_LISTVIEW_FILTER_CLEARED_FUNCTION for details.
	integer BC_LISTVIEW_FILTER_CLEARED_FUNCTION(lv, data)
	The function to be called when filter is cleared.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewAboutToFilterItem(lv, item):

	"""

	Check if item item agrees with the current filter condition of ListView lv.
	Returns True if the item item passes the filter otherwise returns False. This function does not change the visibility of an item, but only indicates if the item will be filtered or not in the default procedure.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@item object: the ListViewItem.

	@returns: True if the item agrees with current filter or False otherwise.

	"""

def BCListViewSetCtrlXFunction(lv, funct, data):

	"""

	Sets the function that will be called when shortcut Ctrl+X key is pressed in the ListView.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called. See BC_LISTVIEW_CTRL_X_FUNCTION for details.
	integer BC_LISTVIEW_CTRL_X_FUNCTION(lv, data)
	The function to be called when Ctrl+X key is pressed in ListView lv.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by function funct.

	"""

def BCListViewSetCtrlCFunction(lv, funct, data):

	"""

	Sets the function that will be called when shortcut Ctrl+C key is pressed in the ListView.
	
	The standard list view on Ctrl+C copies the contents (text) of selected items for all columns to application global clipboard.
	NOTE: If you set your custom function, the default copy to clipboard of selected items' contents (text) will not run. You can manually call BCListViewCopyItemsToClipboard(list, 1) inside your call back to restore the default copy selected items text to clipboard.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called. See BC_LISTVIEW_CTRL_C_FUNCTION for details.
	integer BC_LISTVIEW_CTRL_C_FUNCTION(lv, data)
	The function to be called when Ctrl+C key is pressed in ListView lv.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by function funct.

	"""

def BCListViewSetCtrlVFunction(lv, funct, data):

	"""

	Sets the function that will be called when shortcut Ctrl+V key is pressed in the ListView.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called. See BC_LISTVIEW_CTRL_V_FUNCTION for details.
	integer BC_LISTVIEW_CTRL_V_FUNCTION(lv, data)
	The function to be called when Ctrl+V key is pressed in ListView lv.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by function funct.

	"""

def BCListViewLastItem(lv):

	"""

	Returns the last item of ListView lv.
	
	If you want to append you item at the end do not move after the last item,
	but consider using BCListViewSetAddItemsInReverseOrderEnabled().
	WARNING: this function traverses the whole ListView and thus is slow on long ListViews.
	This function is not supported under VR mode.
	


	@lv object: the ListView of which the last item is returned.

	@returns: the last item of ListView or None if no item exists.

	"""

def BCListViewClearSelection(lv):

	"""

	Deselects all the items in the ListView.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	"""

def BCListViewAdjustColumn(lv, col):

	"""

	Adjusts the column col to its preferred width.
	If you adjust a hidden column it will be first show and then adjust.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	"""

def BCListViewIsColumnHidden(lv, col):

	"""

	Checks if column col of ListView lv is hidden.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@returns: True if the column is hidden; False otherwise.

	"""

def BCListViewBlockUpdates(lv, block):

	"""

	Restricts updates, repaints and info box updates for ListView lv.
	This functions is normally used to disable updates for a short period of time, for instance to avoid screen flicker or long delays during large changes.
	When updates un-blocked, an update will be triggered.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@block boolean: set this parameter to True to block updates, or False otherwise.

	"""

def BCListViewAreUpdatesBlocked(lv):

	"""

	Returns True if updates are blocked for lv, or False otherwise.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@returns: True if updates are blocked for lv, or False otherwise.

	"""

def BCListViewHeaderSetIconFileName(lv, col, fileName):

	"""

	Sets the icon that will be displayed on the header of ListView lv at column col.
	If an item cell contains both icon and text, the icon is always displayed at the left of the text.
	If an empty string is passed into this function, the icon is cleared.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@fileName string: the filename of the icon.

	"""

def BCListViewHeaderSetMovingEnabled(lv, enabled):

	"""

	Sets whether the list view lv columns can be moved by the user.
	The default list view has this property enabled (columns can move).
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@enabled boolean: False to disable moving columns or True to enable it (the default)

	"""

def BCListViewHeaderIsMovingEnabled(lv):

	"""

	Returns True if the columns can be moved by the user (by dragging header sections) otherwise returns False.
	The default list view has this property enabled (columns can move).
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@returns: True if columns can be moved, otherwise returns False.

	"""

def BCListViewSetItemExpandedFunction(lv, funct, data):

	"""

	Sets the function that will be called when an item of ListView lv is expanded.
	This function is not supported under VR mode.
	


	@lv object: the ListView where the expanded item lives.

	@funct callback: the function that will be called. 
	See BC_LISTVIEW_ITEM_EXPANDED_FUNCTION for details.
	integer BC_LISTVIEW_ITEM_EXPANDED_FUNCTION(lv, item, data)
	The function to be called when an item of ListView lv is expanded.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	item  object    the ListViewItem that is expanded.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewSetItemCollapsedFunction(lv, funct, data):

	"""

	Sets the function that will be called when an item of ListView lv is collapsed.
	This function is not supported under VR mode.
	


	@lv object: the ListView where the collapsed item lives.

	@funct callback: the function that will be called. 
	See BC_LISTVIEW_ITEM_COLLAPSED_FUNCTION for details.
	integer BC_LISTVIEW_ITEM_COLLAPSED_FUNCTION(lv, item, data)
	The function to be called when an item of ListView lv is collapsed.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	item  object    the ListViewItem that is collapsed.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewMoveColumn(lv, col, newPos):

	"""

	Moves column col to position newPos.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@newPos integer: the new position where the moved column will be positioned.

	"""

def BCListViewSetItemSelectedFunction(lv, funct, data):

	"""

	Sets the function that will be called when an item of Listview lv is selected (only available in single selection mode).
	If selection changes from an item to another, the deselect function will operate first.
	This function is not supported under VR mode.
	


	@lv object: the ListView where the selected item belongs to.

	@funct callback: the function that will be called. See BC_LISTVIEW_ITEM_SELECTED_FUNCTION for details.
	integer BC_LISTVIEW_ITEM_SELECTED_FUNCTION(lv, item, data)
	The function to be called when an item of Listview lv is selected.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	item  object    the ListViewItem that is selected.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewSetItemDeselectedFunction(lv, funct, data):

	"""

	Sets the function that will be called when an item of Listview lv is deselected (only available in single selection mode).
	If selection changes from an item to another, the deselect function will operate first.
	This function is not supported under VR mode.
	


	@lv object: the ListView which the deselected item belongs to.

	@funct callback: the function that will be called. See BC_LISTVIEW_ITEM_DESELECTED_FUNCTION for details.
	integer BC_LISTVIEW_ITEM_DESELECTED_FUNCTION(lv, item, data)
	The function to be called when an item of Listview lv is deselected.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	item  object    the ListViewItem that is deselected.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewSetSelectableColumn(lv, col, selectable):

	"""

	Set the items of listview lv not to be selected when the user mouse presses on column col.
	The default list view has all columns selectable. If a column is non-selectable, the item is not selected when mouse pressed in specific column but mouse press function operates. Widgets inside column col operates normally. Is useful for switching checkBoxes on/off on a ListView without selection change the item. If heavily used, may produce not so user friendly environments.
	Do not conflict selectable column with the selection mode of a ListView.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@selectable boolean: set False to disable selecting items and True to the default behavior.

	"""

def BCListViewSelectedItem(lv):

	"""

	Function is obsolete. Use BCListViewGetSelectedItem() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: the selected item in BCSingle selection mode.

	"""

def BCListViewFindItem(lv, text, col, mode):

	"""

	Finds the first ListViewItem in column col, that matches text.
	The search starts from the current item, if the current item exists, otherwise it starts from the first ListViewItem. 
	Pass OR-ed together mode values in the BCEnumComparisonMode to control how the matching is performed.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@text string: the text in base of which the search will be performed.

	@col integer: the column index.

	@mode integer: the comparison mode. See BCEnumComparisonMode for details.
	
	guitk.constants BCEnumComparisonMode
	This enum type is used to set the string comparison mode when searching for an item. It can be used by BCListViewFindItem.
	 - guitk.constants.BCCaseSensitive
	The strings must match case sensitively.
	 - guitk.constants.BCBeginsWith
	The target string begins with the search string.
	 - guitk.constants.BCEndsWith
	The target string ends with the search string.
	 - guitk.constants.BCContains
	The target string contains the search string.
	 - guitk.constants.BCExactMatch
	The target and search strings must match exactly.

	@returns: the first ListViewItem that matches text, None otherwise.

	"""

def BCListViewSetMouseClickedFunction(lv, funct, data):

	"""

	Sets the function to be called whenever the user clicks (mouse pressed and mouse released) in ListView lv.
	Mouse press and click events can change the selected item(s), a user activity discoverable using BCListViewSetSelectionChangedFunction().
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function to be called. See BC_LISTVIEW_MOUSE_CLICKED_FUNCTION for details.
	integer BC_LISTVIEW_MOUSE_CLICKED_FUNCTION(lv, mb, item, col, data)
	The function to be called whenever the user clicks (mouse pressed and mouse released) in the list view.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	mb    integer   the mouse button pressed. See BCEnumButtonState for details.
	item  object    the ListViewItem under the mouse when the button was clicked.
	col   integer   the ListView column under the mouse when the button double clicked.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewGetCurrentItem(lv):

	"""

	Returns the current ListViewItem of ListView lv.
	The current item is the one with the focus and it might be None.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: the current item of lv.

	"""

def BCListViewSetCurrentItem(lv, item):

	"""

	Sets the ListViewItem item to be the current item of ListView lv.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@item object: (optional)the ListViewItem.

	"""

def BCListViewSelectAll(lv):

	"""

	Selects all the items of the Listview lv.
	NOTE: This only works in the selection mode BCMulti.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	"""

def BCListViewItemSetComboBox(item, col, vals, funct, data):

	"""

	Sets a combo box to be displayed in the ListViewItem item cell specified by the given column col.
	You can also use generic item widget functions BCListViewItemWidgetSetVisible(), BCListViewItemWidgetSetEnabled() and BCListViewItemWidgetDestroy().
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@vals object: a list of strings with which the ComboBox will be populated.

	@funct callback: a callback function that will be called when the user chooses an item. See BC_LISTVIEWITEM_COMBOBOX_ACTIVATED_FUNCTION for details.
	integer BC_LISTVIEWITEM_COMBOBOX_ACTIVATED_FUNCTION(item, col, index, data)
	The function to be called when the user chooses an item in the combo box.
	Note that the callback will be executed even when the choice is not changed.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	item   object    the ListViewItem.
	col    integer   the ListViewItem column in which the comboBox is found.
	index  integer   the index of the activated item.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewSetComboBoxAlwaysVisible(lv, visible):

	"""

	Sets whether the comboBoxes of the ListView will always be visible or not depending on the value of visible.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@visible boolean: sets this parameter to 1 for the comboBoxes to be always visible, or 0 otherwise.
	If False is set the comboBoxes will only be visible upon ListViewItem selection.

	"""

def BCListViewComboBoxAlwaysVisible(lv):

	"""

	Returns whether the ComboBoxes of ListView lv are always visible or not.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: True if the ComboBoxes are always visible, or False if only their current value is shown.

	"""

def BCListViewSetGridVisible(lv, visible):

	"""

	Paints list view lv with grid lines between item cells (default off).
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@visible boolean: set 1 to show grid lines for lv or to 0 to hide the grid.

	"""

def BCListViewSetHeaderToolButton(lv, toolButton):

	"""

	Inserts a button to the right of the header in ListView lv.
	The ListView takes ownership of the Button. It is recommended that you design and insert a small rectangular button with an icon. Do not use big text because a button with large width may overlap header columns. Your button coexists with header sections. 
	NOTE: The button will be reparented from its previous layout.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@toolButton object: the custom tool button to be incorporated.

	"""

def BCListViewTriggerUpdate(lv):

	"""

	Triggers a size, geometry and content update to ListView lv.
	Designed for special cases when managing large data sets. For example you may block list updates 
	during a loop and trigger updates at certain periods of time.
	NOTE: You might never use this function.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	"""

def BCListViewSetAddItemsInReverseOrderEnabled(lv, enable):

	"""

	Defines where a newly added item will be placed, first (default) or last.
	When adding an item as top level or item's child, it can be placed first (reverse order) or last (normal order).
	Reverse order is slower than normal, since intermediate items will internally update some of their data.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@enable boolean: the standard list has this property true.

	"""

def BCListViewBlockSelectionChangeFunctionOnMouseDragging(lv, single):

	"""

	Set whether selection change function call is blocked, when selecting multiple items by dragging the mouse over them.
	The standard list has this property on. Has a meaning for lists with multiple item selection. 
	Selection change on right mouse press is not affected. Designed for cases where you have set an expensive function 
	in the selection change event and you want to avoid multiple function calls during selecting multiple items using mouse drag. 
	The selection change call back will be executed once when selection finished (mouse button released).
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@single boolean: set True to enable single selection on mouse drag or False (default) otherwise.

	"""

def BCListViewItemComboBoxInsertStrList(item, col, vals):

	"""

	Inserts the array of strings vals in the comboBox.
	NOTE: The comboBox is cleared before inserting any items.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@vals object: the array of strings. If you pass None here, you'll end up with an empty comboBox.

	"""

def BCListViewItemComboBoxSetCurrentText(item, col, text):

	"""

	Sets the text of the combobox's current item to text text;
	If the combobox contains an item with text equal to text, then that item becomes current. If
	not, in case the combobox is editable then it's lineEdit text is set to text without adding any new
	item. If it's not editable then the current item's text is replaced with the new text.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@text string: the new text to be shown.

	"""

def BCListViewItemComboBoxCurrentText(item, col):

	"""

	Returns the current text of the comboBox found at column col of ListViewItem item.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: the current text of the comboBox.

	"""

def BCListViewItemComboBoxText(item, col, index):

	"""

	Returns the text of the ListView's comboBox at position index, or None if index does not exist.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@index integer: the item position.

	@returns: the current text of the comboBox, or None if index does not exist.

	"""

def BCListViewItemComboBoxInsertItem(item, col, text, index):

	"""

	Inserts a comboBox item with text text, at position index to a comboBox that belongs to ListViewItem item.
	The item will be appended if index is negative.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@text string: the text that will be inserted.

	@index integer: the index at which text will be inserted (-1 to append).

	"""

def BCListViewItemComboBoxRemoveItem(item, col, index):

	"""

	Removes the comboBox item at index index of the comboBox found at column col of ListViewItem item.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@index integer: the index of the comboBox item to remove.

	"""

def BCListViewItemComboBoxSetCurrentItem(item, col, index):

	"""

	Sets the current item of the comboBox found at column col of ListViewItem item to be the item with index index.
	WARNING: this function doesn't trigger the activated callback set by the user.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@index integer: the index of the item to which current will be set.

	"""

def BCListViewItemComboBoxCurrentItem(item, col):

	"""

	Returns the index of the current item of the comboBox found at column col of ListViewItem item.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: the index of the current item of the current item of the comboBox; -1 in case of error.

	"""

def BCListViewItemComboBoxCount(item, col):

	"""

	Returns the number of items in the comboBox found at column col of ListViewItem item.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: the number of items in the comboBox.

	"""

def BCListViewItemIsComboBox(item, col):

	"""

	Returns True if the ListViewItem item cell displays a combo box at given column col, or False otherwise.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem

	@col integer: the column index.

	@returns: True if the ListViewItem item at column col is a comboBox, or False otherwise.

	"""

def BCListViewColumnPosition(lv, col):

	"""

	Returns the position of the column with the given index col.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@returns: the position of the column with the given index or -1 if column index is invalid.

	"""

def BCListViewSetSaveColumnsEnabled(lv, enable):

	"""

	Set whether columns visual data will be stored to xml file or not depending on the value of enable.
	The column visual data stored are
	- width
	- position
	- visibility state (shown/hidden)
	Data stored with the given column text. If you have column with icon only (no text) use BCListViewHeaderSetStringRepresentation().
	The data that read from xml will be applied to your ListView just before the window is shown.
	WARNING: The width mode will be changed to "BCManualMode" for all columns.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@enable boolean: set True to enable saving the column widths of ListView lv, otherwise set False.

	"""

def BCListViewIsSaveColumnsEnabled(lv):

	"""

	Returns whether columns visual data will be stored to xml file or not.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: True if the column widths of ListView will be saved, or False if they will not be saved.

	"""

def BCListViewSetRenameItemPrecision(lv, prec):

	"""

	Sets the number of digits after the decimal point (precision) when renaming items that accept double. Default is 6 digits.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@prec integer: the number of digits.

	"""

def BCListViewForEachItem(lv_or_item, flags, funct, data):

	"""

	Provides an easy way to iterate over the items in a ListView or a ListViewItem (children) and execute a callback function for each item.
	Iteration begins from first item and falls through, depending on flags.
	If you need to terminate the iteration return 1 at your callback.
	WARNING: Can not be used to delete items. If you need to delete items, create an array, fill it with the desired items 
	and delete them after iteration finished.
	WARNING: Using it with take/insert operations needs extra care and should be avoided.
	NOTE: This function will be executed even if call back functions are blocked for ListView.
	This function is not supported under VR mode.
	


	@lv_or_item object: the ListView or ListViewItem.

	@flags integer: It is an integer value that is composed of BCEnumItemIteratorFlag OR'ed (i.e. added) together.
	
	guitk.constants BCEnumItemIteratorFlag
	This enum defines which ListView items will be iterated.
	 - guitk.constants.BCIterateAll
	If iterate over ListView these are all items while if iterate over ListViewItem these are all children (no matter the depth).
	 - guitk.constants.BCIterateSelected
	Selected items. Operates exclusive with BCIterateUnselected. A selected item can not be unselected at the same time.
	 - guitk.constants.BCIterateUnselected
	Non selected items. Operates exclusive with BCIterateSelected. A selected item can not be unselected at the same time.
	 - guitk.constants.BCIterateVisible
	Visible items (collapsed items are by default visible). Operates exclusive with BCIterateHidden, A visible item can not be hidden at the same time.
	 - guitk.constants.BCIterateHidden
	Hidden items (for example items that filtered). Note that collapsed items are by default visible. Operates exclusive with BCIterateVisible, A visible item can not be hidden at the same time.
	 - guitk.constants.BCIterateFirstLevel
	If iterate over ListView these are the top level items. If iterate over ListViewItem these are the first level children.

	@funct callback: the function that will be executed for each item during iteration. See BC_LISTVIEW_ITEM_ITERATE_FUNCTION for details.
	integer BC_LISTVIEW_ITEM_ITERATE_FUNCTION(item, data)
	The function to be executed for each item during iteration.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	item  object    the ListViewItem.
	data  anything  anything that may be required in function.
	
	Return: Return 1 to terminate items iteration or 0 to continue iterating.

	@data anything: (optional)any data required by funct.

	@returns: 1 if the iteration terminated by the users' callback, 0 otherwise.

	"""

def BCMessageWindowCreate(type, message, modal):

	"""

	Creates a dialog of type type that contains text message.
	After you created the message window you have to run BCMessageWindowExecute() for window to be shown.
	NOTE: Modal window grabs all input. No other window can be used until this message window is closed.
	This function is not supported under VR mode.
	


	@type integer: the dialog type. See BCEnumStylePixmap for details.
	
	guitk.constants BCEnumStylePixmap
	This enum represents a StylePixmap. A StylePixmap is a pixmap that can follow some
	existing GUI style or guideline. StylePixmap is used with BCLabelSetStylePixmap for example.
	 - guitk.constants.BCMessageBoxWarning
	the 'warning' icon.
	 - guitk.constants.BCMessageBoxCritical
	the 'critical' icon.
	 - guitk.constants.BCMessageBoxInformation
	the 'information' icon.
	 - guitk.constants.BCMessageBoxQuestion
	the 'question' icon.

	@message string: the text of the BCMessageWindow.

	@modal boolean: sets whether the BCMessageWindow will be modal or not.

	@returns: the created BCMessageWindow.

	"""

def BCMessageWindowExecute(messageWindow):

	"""

	Shows the BCMessageWindow messageWindow and waits for the user's response (answer).
	This function is not supported under VR mode.
	


	@messageWindow object: the BCMessageWindow.

	@returns: the user response. See BCEnumMessageWindowResult for details.
	BCEnumMessageWindowResult: This enum represents a BCMessageWindow result code. The result code is returned when the excecution of BCMessageWindow is finished.
	guitk.constants.BCQuitAll: this result code is returned when a non modal BCMessageWindow is forced to quit by an application's action.
	guitk.constants.BCEscKey: this result code is returned when the user rejects the BCMessageWindow (e.g. when pressing the [x] button, the Esc key or the Cancel button).
	guitk.constants.BCRetKey: this result code is returned when the user accepts the BCMessageWindow (e.g. when pressing the Return key or the OK button).

	"""

def BCMessageWindowSetAcceptButtonText(messageWindow, text):

	"""

	Customize accept button text of the dialog (default OK).
	This function is not supported under VR mode.
	


	@messageWindow object: the BCMessageWindow.

	@text string: the text to be displayed (default OK).

	"""

def BCMessageWindowSetRejectButtonText(messageWindow, text):

	"""

	Customize reject button text of the dialog (default Cancel).
	This function is not supported under VR mode.
	


	@messageWindow object: the BCMessageWindow.

	@text string: the text to be displayed (default Cancel).

	"""

def BCMessageWindowSetAcceptButtonVisible(messageWindow, visible):

	"""

	Sets whether the accept button of the dialog will be visible or not (default visible).
	Hiding the accept button is useful if you have cases where the user has no choice, i.e. can only confirm that something happened.
	This function is not supported under VR mode.
	


	@messageWindow object: the BCMessageWindow.

	@visible boolean: set this parameter to 0 for the accept button to be hidden, otherwise 1.

	"""

def BCMessageWindowSetRejectButtonVisible(messageWindow, visible):

	"""

	Sets whether the reject button of the dialog will be visible or not (default visible).
	Hiding the reject button is useful if you have cases where the user has no choice, i.e. can only confirm that something happened.
	This function is not supported under VR mode.
	


	@messageWindow object: the BCMessageWindow.

	@visible boolean: set this parameter to 0 for the reject button to be hidden, otherwise 1.

	"""

def BCPopupMenuCreate(w):

	"""

	Creates a BCMenu with parent w.
	This function is not supported under VR mode.
	


	@w object: the parent widget.

	@returns: The created BCMenu.

	"""

def BCPopupMenuPopup(pm):

	"""

	Pops up the BCMenu (i.e. it makes it visible).
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	"""

def BCPopupMenuPopupToParentWidget(pm):

	"""

	Pops up the BCMenu based on the bottom-left position of its parent Widget (i.e. it makes it visible).
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	"""

def BCPopupMenuSetItemCheckable(pm, id, checkable):

	"""

	Sets item with id of BCMenu pm if as checkable if checkable is not zero, otherwise sets it as uncheckable.
	Checkable items work like toggling buttons, i.e. can be checked and unchecked.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@id integer: the id of the item that will be checkable/uncheckable.

	@checkable boolean: set this parameter to True to make the item checkable, or to False to make it uncheckable.

	"""

def BCPopupMenuIsItemCheckable(pm, id):

	"""

	Returns True if item with id id is a checkable item; False otherwise.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@id integer: the id of the item whose checkable status is required.

	@returns: True if item with id id is checkable; False otherwise.

	"""

def BCPopupMenuSetItemChecked(pm, id, checked):

	"""

	Checks BCMenu item pm at id if checked is not zero, otherwise it unchecks it.
	WARNING: If this function is used on a non-checkable menu, it will first make it checkable and then set its checked status according to checked.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@id integer: the id of the item that will be checked/unchecked.

	@checked boolean: set this parameter to True to check, or to False to uncheck the item.

	"""

def BCPopupMenuIsItemChecked(pm, id):

	"""

	Returns True if item with id id is checked; False otherwise.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@id integer: the id of the item whose check status is required.

	@returns: True if item with id id is checked; False otherwise.

	"""

def BCPopupMenuInsertItem(pm, text, funct, data):

	"""

	Inserts an item in the BCMenu pm.
	WARNING: funct will be called before the function set by BCPopupMenuSetActivatedFunction().
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@text string: the text that will be displayed (can be set to None).

	@funct callback: the function that will be called when the item is activated (can be set to None). See 
	BC_POPUPMENU_INSERT_ITEM_FUNCTION for details.
	integer BC_POPUPMENU_INSERT_ITEM_FUNCTION(pm, id, data)
	The function to be called when the item is activated (can be set to None).
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	pm    object    the BCMenu.
	id    integer   the id of the item.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)pointer to any user data that are required by funct.

	@returns: the allocated id of the inserted item.

	"""

def BCPopupMenuInsertItemWithIcon(pm, text, icon, funct, data):

	"""

	Inserts an item in the BCMenu pm with icon icon.
	WARNING: funct will be called before the function set by BCPopupMenuSetActivatedFunction().
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@text string: the text that will be displayed (can be set to None).

	@icon string: the icon that will be displayed before the text and will be toggled, if this pm is checkable. 
	It is the absolute path (i.e. /home/user/...) of the icon file we want to set and it can be set to None.

	@funct callback: the function that will be called when the item is activated (can be set to None).
	See BC_POPUPMENU_INSERT_ITEM_FUNCTION for details.
	integer BC_POPUPMENU_INSERT_ITEM_FUNCTION(pm, id, data)
	The function to be called when the item is activated (can be set to None).
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	pm    object    the BCMenu.
	id    integer   the id of the item.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any user data that are required by funct.

	@returns: the allocated id of the inserted item.

	"""

def BCPopupMenuInsertWidget(pm, w):

	"""

	Inserts a widget w in the BCMenu pm.
	Theoretically, any widget can be inserted into a popup menu. In practice, this only makes sense with certain widgets.
	WARNING: The ownership of the widget w is transfered to the BCMenu pm. If you clear the BCMenu, the widget will automatically be destroyed. Try not to use the widget w outside the BCMenu pm.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@w object: the widget to be inserted.

	@returns: the allocated id of the inserted widget, if is valid, -1 otherwise.

	"""

def BCPopupMenuInsertPopupMenu(pm, text, menu):

	"""

	Inserts a submenu menu in the BCMenu pm.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@text string: the text that will be displayed.

	@menu object: the BCMenu that is the submenu.

	@returns: the allocated id of the inserted BCMenu.

	"""

def BCPopupMenuInsertPopupMenuWithIcon(pm, text, icon, menu):

	"""

	Inserts a submenu menu in the BCMenu pm with an icon icon.
	The icon is always placed to the left of the text.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@text string: the text that will be displayed.

	@icon string: the icon that will be displayed on the left of text.
	It is the absolute path (i.e. /home/user/...) of the icon file we want to set and it can be set to None.

	@menu object: the BCMenu that is the submenu.

	@returns: the allocated id of the inserted BCMenu.

	"""

def BCPopupMenuRemoveItem(pm, id):

	"""

	Removes the item with ID id from the BCMenu.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@id integer: the id of the item to be removed.

	"""

def BCPopupMenuRemoveItemAt(pm, index):

	"""

	Removes the item with INDEX index from the BCMenu.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@index integer: the index of the item to be removed.

	"""

def BCPopupMenuText(pm, id):

	"""

	Returns the text of the item with ID id, or None if id does not exist.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@id integer: the identifier of the item whose text is returned.

	@returns: the text of the item with ID id, or None if id does not exist.

	"""

def BCPopupMenuTextAt(pm, index):

	"""

	Returns the text of the item of index index, or None if index is NOT in the range [0, BCPopupMenuCount()-1].
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@index integer: the index of the item whose text is returned. Indexes begin from 0.

	@returns: the text of the item with index index, or None if index is out of range.

	"""

def BCPopupMenuSetItemEnabled(pm, id, enabled):

	"""

	Sets whether the item with ID id is enabled or not depending on the value of enabled.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@id integer: the identifier of the item to be enabled/disabled.

	@enabled boolean: set this parameter to True to enable the item or False to disable it.

	"""

def BCPopupMenuIsItemEnabled(pm, id):

	"""

	Returns True if item with id id is enabled; False otherwise.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@id integer: the identifier of the item whose enabled/disabled status is asked.

	@returns: True if item with id id is enabled; False otherwise.

	"""

def BCPopupMenuSetItemVisible(pm, id, vis):

	"""

	Sets whether the item with ID id is visible or not depending on the value of vis.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@id integer: the identifier of the item to be visible or not.

	@vis boolean: set this parameter to True for the item to become visible or False otherwise.

	"""

def BCPopupMenuIsItemVisible(pm, id):

	"""

	Returns True if item with id id is visible; False otherwise.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@id integer: the identifier of the item whose visibility status is asked.

	@returns: True if item with id id is visible; False otherwise.

	"""

def BCPopupMenuClear(pm):

	"""

	Clears the BCMenu pm from all its items.
	If you have sub menus inside pm, they will NOT be destroyed or cleared. You will have to remove/clear them manually.
	A good practice to handle sub menus is to create them with parent pm and destroy pm when needed (it will automatically destroy all children sub menus).
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	"""

def BCPopupMenuDestroyItems(pm):

	"""

	Destroys the BCMenu pm all its items.
	If you have sub menus inside pm, they will  be destroyed or cleared.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	"""

def BCPopupMenuSetActivatedFunction(pm, funct, data):

	"""

	Set the function that will be called when the BCMenu is activated (i.e. when an item is selected).
	Note that ActivatedFunction function will operate after AboutToHideFunction and the item's function.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu

	@funct callback: the function that will be called when the BCMenu pm is activated. See BC_POPUPMENU_ACTIVATED_FUNCTION for details.
	integer BC_POPUPMENU_ACTIVATED_FUNCTION(pm, id, data)
	The function to be called when BCMenu pm is activated.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	pm    object    the BCMenu.
	id    integer   the id of the selected item.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)anything that may be required in funct.

	"""

def BCPopupMenuSetAboutToShowFunction(pm, funct, data):

	"""

	Set the function that will be called just before the BCMenu is displayed.
	This function can be used to set up the popup menu dynamically.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@funct callback: the function to be called. See BC_POPUPMENU_ABOUTTOSHOW_FUNCTION for details.
	integer BC_POPUPMENU_ABOUTTOSHOW_FUNCTION(pm, data)
	The function to be called just before BCMenu pm is displayed.
	
	Use this function if you want to set up your menu dynamically.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	pm    object    the BCMenu.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)anything that may be required in funct.

	"""

def BCPopupMenuSetAboutToHideFunction(pm, funct, data):

	"""

	Set the function that will be called just before the BCMenu is hidden.
	Note that aboutToHide function operates (when an item is selected) just before an item's function.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@funct callback: the function to be called. See BC_POPUPMENU_ABOUTTOHIDE_FUNCTION for details.
	integer BC_POPUPMENU_ABOUTTOHIDE_FUNCTION(pm, data)
	The function to be called just before BCMenu pm is hidden.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	pm    object    the BCMenu.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)anything that may be required in funct.

	"""

def BCPopupMenuInsertSeparator(pm):

	"""

	Inserts a separator at the end of the BCMenu.
	A separator is simply a line that separates the items on the BCMenu.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@returns: the allocated id of the inserted separator.

	"""

def BCPopupMenuItemId(pm, label):

	"""

	Returns the id of the item with label label if pm contains label, or -1 otherwise.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@label string: the label that will be checked.

	@returns: the id of item with label label if pm contains it, or -1 otherwise.

	"""

def BCPopupMenuIdAt(pm, index):

	"""

	Returns the id of the BCMenu item at position index, or -1 if index is out of range.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@index integer: the index of the BCMenu item.

	"""

def BCPopupMenuCount(pm):

	"""

	Returns the number of items in the menu.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@returns: the number of items.

	"""

def BCPopupMenuSetHideOnCheckEnabled(pm, enabled):

	"""

	Enable popup menu pm to remain open while you mouse toggle checkable items.
	If you disable this property the activated function for the item (if one was set) will run, but the menu will remain open. This property only operates for checkable menus and makes sense for large list of items. If the menu is not checkable, nothing happens. The default menu has this property true (hides when you check/uncheck an item).
	This function is not supported under VR mode.
	


	@pm object: the BCMenu to affect.

	@enabled boolean: set False to enable checking without menu to hide.

	"""

def BCPopupMenuSetDeletionFunction(pm, funct, data):

	"""

	Sets the function to be called when the highlighted popup item of BCMenu pm is deleted by
	pressing the delete key.
	NOTE: The callback function set by this function will be called only if deletion is enabled, which can
	be done by calling BCPopupMenuSetDeletionEnabled(). The default behaviour is to not allow the deletion.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@funct callback: the function to be called. See BC_POPUPMENU_DELETION_FUNCTION for details.
	integer BC_POPUPMENU_DELETION_FUNCTION(pm, id, data)
	The function to be called when the item with id id of BCMenu pm is deleted by pressing the delete key.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	pm    object    the BCMenu.
	id    integer   the id of the item to be deleted.
	data  anything  anything that may be required in function.
	
	Return: Return 1 to proceed with deletion of the item; 0 to deny it.

	@data anything: (optional)a pointer to anything that may be required in funct.

	"""

def BCPopupMenuSetDeletionEnabled(pm, enable):

	"""

	Enable or disable the deletion of the highlighted popup item by pressing the delete key.
	If this option is enabled, a callback function can be set to be called uppon delete-key press. Set
	this function with BCPopupMenuSetDeletionFunction().
	NOTE: This property will reset to default (i.e. the item deletion is disabled), after BCPopupMenuClear() is called.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@enable boolean: set this to True to enable this option; False otherwise.

	"""

def BCPopupMenuDeletionEnabled(pm):

	"""

	Returns True if deletion of the highlighted popup menu item is enabled by pressing the delete key. If not, returns False.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@returns: True if deletion is enabled; False otherwise.

	"""

def BCPopupMenuActivateItem(pm, id):

	"""

	Activates the callback of the item with id id of the BCMenu pm.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@id integer: the id of the item to be activated.

	"""

def BCProgressBarCreate(p, steps):

	"""

	Creates a new BCProgressBar with parent p, and total steps steps.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@steps integer: the totals steps

	@returns: the created BCProgressBar.

	"""

def BCProgressBarSetProgress(pb, progress):

	"""

	Sets the progress of the progress bar.
	This is the function that should be called inside the calculating loop.
	This function is not supported under VR mode.
	


	@pb object: the BCProgressBar.

	@progress integer: the number of steps completed.

	"""

def BCProgressBarReset(pb):

	"""

	Resets the progress bar to show 0 completed steps. This function does not affect the total steps previously set.
	This function is not supported under VR mode.
	


	@pb object: the BCProgressBar.

	"""

def BCProgressBarSetTotalSteps(pb, steps):

	"""

	Sets the total steps of the progress bar.
	This function is not supported under VR mode.
	


	@pb object: the BCProgressBar.

	@steps integer: the total number of steps.

	"""

def BCProgressBarTotalSteps(pb):

	"""

	Returns the total steps of pb.
	This function is not supported under VR mode.
	


	@pb object: the BCProgressBar.

	"""

def BCProgressBarProgress(pb):

	"""

	Returns the progress (completed steps) of pb.
	This function is not supported under VR mode.
	


	@pb object: the BCProgressBar.

	"""

def BCProgressBarSetPercentageVisible(pb, visible):

	"""

	Sets whether the percentage of the completed steps will be displayed on the progress bar or not, depending on the value of visible.
	The percentage is visible by default.
	This function is not supported under VR mode.
	


	@pb object: the BCProgressBar.

	@visible boolean: set this to True to show the percentage, or to False to hide it.

	"""

def BCRadioButtonCreate(p, text, funct, data):

	"""

	Creates a BCRadioButton with parent p.
	It is recommended to be created with a BCButtonGroup as parent. RadioButtons by their nature are designed to operate exclusively 
	(when toggled, untoggle another radio button inside the same group). It is useless 
	to design multiple radio buttons and then try to copy the exclusive behaviour that 
	BCButtonGroup safely and easily provides. If you are trying to design radio buttons 
	outside of a BCButtonGroup, then probably you do not need to use BCRadioButtons at 
	all. When BCRadioButtons inserted to a BCButtonGroup they obtain exclusive property
	automatically. BCRadioButtons support pixmap as well as text.
	NOTE: In a ButtonGroup with mixed type of buttons (RadioButton, BCPushButton etc), a case which is not recommended,
	the exclusive property will be set for RadioButtons and not for any other type of button, even if we had
	set this property explicitly.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout

	@text string: the text

	@funct callback: This callback is obsolete. Please avoid setting this callback.
	The proper way is to set the BCButtonGroupSetPressedFunction().
	
	
	
	Return:

	@data anything: (optional)Obsolete parameter. Please pass None

	@returns: the created BCRadioButton.

	"""

def BCRadioButtonAddManagedWidget(rb, w, onAction, offAction):

	"""

	This function adds a widget to a list of widgets that are automatically managed when the radio button rb is set to on or off.
	This function is not supported under VR mode.
	


	@rb object: the RadioButton

	@w object: the widget to manage.

	@onAction integer: the action to perform when the RadioButton is on.

	@offAction integer: the action to perform when the RadioButton is off.
	See BCEnumManagedAction property for details about actions.
	
	guitk.constants BCEnumManagedAction
	This enum type defines the action to be taken. The managed action is used with BCCheckBoxAddManagedWidget for example.
	 - guitk.constants.BCManagedEnable
	enables the widget.
	 - guitk.constants.BCManagedDisable
	disables the widget.
	 - guitk.constants.BCManagedHide
	hides the widget.
	 - guitk.constants.BCManagedShow
	shows the widget.

	"""

def BCRadioButtonSetChecked(rb, checked):

	"""

	Sets RadioButton rb check state to checked.
	If you have placed RadioButtons into a ButtonGroup (recommended), 
	consider using BCButtonGroupSetButton() that also triggers respective ButtonGroup callbacks.
	This function is not supported under VR mode.
	


	@rb object: the RadioButton

	@checked boolean: set this parameter to True to set the radio button checked; False otherwise.

	"""

def BCRadioButtonIsChecked(rb):

	"""

	Returns True if RadioButton rb is checked; otherwise returns False.
	If you have placed RadioButtons into a ButtonGroup (recommended),
	consider using BCButtonGroupId() that actually gets the id of the current selected RadioButton.
	This function is not supported under VR mode.
	


	@rb object: the RadioButton

	@returns: the check state of the RadioButton rb

	"""

def BCRadioButtonSetIconFileName(rb, fileName):

	"""

	Sets the icon of the RadioButton rb.
	Icon is displayed between the check indicator and the text.
	This function is not supported under VR mode.
	


	@rb object: the RadioButton

	@fileName string: the absolute path of the iconfile.

	"""

def BCRadioButtonSetText(rb, text):

	"""

	Sets the text displayed on RadioButton rb.
	This function is not supported under VR mode.
	


	@rb object: the RadioButton

	@text string: the text

	"""

def BCRadioButtonText(rb):

	"""

	Returns the text of button rb.
	This function is not supported under VR mode.
	


	@rb object: the RadioButton

	@returns: the text.

	"""

def BCSeparatorCreate(p):

	"""

	Creates a styled line to visually separate controls on a window.


	@p object: the parent widget or layout.

	@returns: the newly created separator frame.

	"""

def BCSeparatorSetOrientation(s, o):

	"""

	Sets the orientation of the Separator s to o.


	@s object: the separator.

	@o integer: the orientation of the separator. See BCEnumOrientation for details.
	
	guitk.constants BCEnumOrientation
	This type is used to signify an object's orientation. Orientation is used with BCButtonGroupCreate for example.
	 - guitk.constants.BCHorizontal
	sets horizontal orientation.
	 - guitk.constants.BCVertical
	sets vertical orientation.

	"""

def BCSliderCreate(p, min, max, step, value, o):

	"""

	Creates a BCSlider.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@min integer: the minimum allowed value for the slider.

	@max integer: the maximum allowed value for the slider.

	@step integer: the step for the slider.

	@value integer: the initial value to which the slider will be set.

	@o integer: the orientation of the slider. See BCEnumOrientation for details.
	
	guitk.constants BCEnumOrientation
	This type is used to signify an object's orientation. Orientation is used with BCButtonGroupCreate for example.
	 - guitk.constants.BCHorizontal
	sets horizontal orientation.
	 - guitk.constants.BCVertical
	sets vertical orientation.

	@returns: the newly created BCSlider

	"""

def BCSliderSetValue(sl, value):

	"""

	Sets the current value of slider sl to value.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@value integer: the new value to which the slider will be set.

	"""

def BCSliderSetValueNoCallback(sl, value):

	"""

	Sets the current value of slider sl to value without calling the callback.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@value integer: the new value to which the slider will be set.

	"""

def BCSliderValue(sl):

	"""

	Returns the current value of the slider sl.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@returns: the value of the slider.

	"""

def BCSliderSetMinValue(sl, min):

	"""

	Sets the minimum value of the slider.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@min integer: the minimum value of the slider.

	"""

def BCSliderMinValue(sl):

	"""

	Gets the minimum value of the slider.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@returns: the minimum value of the slider

	"""

def BCSliderSetMaxValue(sl, max):

	"""

	Sets the maximum value of the slider.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@max integer: the maximum value of the slider.

	"""

def BCSliderMaxValue(sl):

	"""

	Gets the maximum value of the slider.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@returns: the maximum value of the slider

	"""

def BCSliderSetLineStep(sl, step):

	"""

	Sets the line step.
	The line step is the smaller of two natural steps by which the slider position changes.
	Typically corresponds to the user pressing an arrow key.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@step integer: the line step of the slider.

	"""

def BCSliderLineStep(sl):

	"""

	Returns the line step.
	The line step is the smaller of two natural steps by which the slider position changes.
	Typically corresponds to the user pressing an arrow key
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@returns: the line step of slider.

	"""

def BCSliderSetPageStep(sl, step):

	"""

	Sets the page step.
	The page step is the larger of two natural steps by which the slider position changes.
	Typically corresponds to the user pressing the PageUp or PageDown keys.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@step integer: the page step of the slider.

	"""

def BCSliderPageStep(sl):

	"""

	Returns the page step.
	The page step is the larger of two natural steps by which the slider position changes.
	Typically corresponds to the user pressing the PageUp or PageDown keys.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@returns: the page step of slider.

	"""

def BCSliderSetValueChangedFunction(sl, funct, data):

	"""

	Sets the function that will be called every time the value of the slider changes.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@funct callback: the function that will be called when the value of the slider changes. 
	See BC_SLIDER_VALUE_CHANGED_FUNCTION for details.
	integer BC_SLIDER_VALUE_CHANGED_FUNCTION(sl, val, data)
	The function to be called every time the value of the slider changes.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	sl    object    the BCSlider.
	val   integer   the new slider value.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct. If data is not required,
	it should be set to None.

	"""

def BCSliderSetTickmarks(sl, ticks):

	"""

	Sets tickmarks setting for BCSlider sl.
	This function is not supported under VR mode.
	


	@sl object: the BCSlider.

	@ticks integer: the tickmark setting. See BCEnumTickmarks property for details.
	
	guitk.constants BCEnumTickmarks
	This enum specifies where the tickmarks of a BCSlider are to be drawn relative to the slider's groove and the handle the user
	moves. It is used in BCSliderSetTickmarks.
	 - guitk.constants.BCTicksNoMarks
	No tickmarks are drawn.
	 - guitk.constants.BCTicksAbove
	Draw tickmarks above the (horizontal) slider.
	 - guitk.constants.BCTicksBelow
	Draw tickmarks below the (horizontal) slider.
	 - guitk.constants.BCTicksLeft
	Draw tickmarks to the left of the (vertical) slider.
	 - guitk.constants.BCTicksRight
	Draw tickmarks to the right of the (vertical) slider.
	 - guitk.constants.BCTicksBoth
	Draw tickmarks on both sides of the groove.

	"""

def BCSliderSetTickmarksInterval(sl, interval):

	"""

	Sets the interval between tickmarks.
	NOTE: This is a value interval, not a pixel interval. If it is 0, the BCSlider will choose between line step and page step. The initial value of the interval is 0.
	This function is not supported under VR mode.
	


	@sl object: the BCSlider.

	@interval integer: the interval between tickmarks.

	"""

def BCSliderEnableBoundaries(sl, enable):

	"""

	Enables the boundaries for BCSlider sl.
	This function is not supported under VR mode.
	


	@sl object: the BCSlider.

	@enable integer: 0 or 1 whether boundaries for BCSlider sl should be enabled.

	"""

def BCSliderSetStartBoundValue(sl, val):

	"""

	Sets the starting boundary value for BCSlider sl.
	This function is not supported under VR mode.
	


	@sl object: the BCSlider.

	@val integer: the new value to which the starting boundary for BCSlider sl will be set.

	"""

def BCSliderSetEndBoundValue(sl, val):

	"""

	Sets the ending boundary value for BCSlider sl.
	This function is not supported under VR mode.
	


	@sl object: the BCSlider.

	@val integer: the new value to which the ending boundary for BCSlider sl will be set.

	"""

def BCSliderStartBoundValue(sl):

	"""

	Gets the starting boundary value of the slider.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@returns: the starting boundary value of the slider.

	"""

def BCSliderEndBoundValue(sl):

	"""

	Gets the ending boundary value of the slider.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@returns: the ending boundary value of the slider.

	"""

def BCSliderSetExceedBounds(sl, exceed):

	"""

	Sets the slider to exceed the boundaries.
	This function is not supported under VR mode.
	


	@sl object: the BCSlider.

	@exceed integer: set 1 to exceed the boundaries, or 0 otherwise.

	"""

def BCSliderExceedBounds(sl):

	"""

	Returns whether the slider can exceed the boundaries or not.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@returns: 1 if the slider can exceed the boundaries, or 0 otherwise.

	"""

def BCSliderSetStartBoundChangedFunction(sl, funct, data):

	"""

	Sets the function that will be called every time the starting boundary value of the slider changes.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@funct callback: the function that will be called when the starting boundary value of the slider changes. 
	See BC_SLIDER_START_BOUND_CHANGED_FUNCTION for details.
	integer BC_SLIDER_START_BOUND_CHANGED_FUNCTION(sl, val, data)
	The function to be called every time the starting boundary value of the slider changes.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	sl    object    the BCSlider.
	val   integer   the new slider starting boundary value.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct. If data is not required,
	it should be set to None.

	"""

def BCSliderSetEndBoundChangedFunction(sl, funct, data):

	"""

	Sets the function that will be called every time the ending boundary value of the slider changes.
	This function is not supported under VR mode.
	


	@sl object: the slider.

	@funct callback: the function that will be called when the ending boundary value of the slider changes. 
	See BC_SLIDER_END_BOUND_CHANGED_FUNCTION for details.
	integer BC_SLIDER_END_BOUND_CHANGED_FUNCTION(sl, val, data)
	The function to be called every time the ending boundary value of the slider changes.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	sl    object    the BCSlider.
	val   integer   the new slider ending boundary value.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct. If data is not required,
	it should be set to None.

	"""

def BCSpacerCreate(p):

	"""

	Creates a blank space, with minimum width and height equal to 5 pixels.
	Spacer is not a widget.
	Spacer inside a horizontal layout gets expanding horizontal policy. Geometry and size policy can be modified any time using BCSpacerChangeSize().
	WARNING: Spacer should be placed inside a layout or inside a widget that has a layout. If you pass widget without a layout as spacer parent, the behaviour is undefined.


	@p object: layout or widget with a layout.

	@returns: the created Spacer.

	"""

def BCSpacerChangeSize(spc, w, h, sizepolicy_h, sizepolicy_v):

	"""

	Changes Spacer spc to have preferred width w, height h, horizontal size policy sizepolicy_h and vertical size policy sizepolicy_v.


	@spc object: the Spacer.

	@w integer: the preferred width.

	@h integer: the preferred height.

	@sizepolicy_h integer: the horizontal SizePolicy (default: BCExpanding).

	@sizepolicy_v integer: the vertical SizePolicy (default: BCExpanding).
	See BCEnumSizePolicy for details about size policy.
	
	guitk.constants BCEnumSizePolicy
	This enum type holds the default layout behavior of the widget.
	If there is a BCBoxLayout that manages this widget's children, the size policy specified by that layout is used. If there is no such BCBoxLayout, the result of this function is used.
	 - guitk.constants.BCFixed
	this is the default BCWidget policy. The size hint is the only acceptable alternative, so the widget can never grow or shrink (e.g. the vertical direction of a push button).
	 - guitk.constants.BCMinimum
	the size hint is minimal, and sufficient. The widget can be expanded, but there is no advantage to it being larger (e.g. the horizontal direction of a push button). It cannot be smaller than the size provided by size hint.
	 - guitk.constants.BCMaximum
	the size hint is a maximum. The widget can be shrunk any amount without detriment if other widgets need the space (e.g. a separator line). It cannot be larger than the size provided by size hint.
	 - guitk.constants.BCPreferred
	the size hint is best, but the widget can be shrunk and still be useful. The widget can be expanded, but there is no advantage to it being larger than size hint.
	 - guitk.constants.BCExpanding
	the size hint is a sensible size, but the widget can be shrunk and still be useful. The widget can make use of extra space, so it should get as much space as possible (e.g. the horizontal direction of a slider).
	 - guitk.constants.BCMinimumExpanding
	the size hint is minimal, and sufficient. The widget can make use of extra space, so it should get as much space as possible (e.g. the horizontal direction of a slider).
	 - guitk.constants.BCIgnored
	the size hint is ignored. The widget will get as much space as possible.

	"""

def BCSpinBoxCreate(p):

	"""

	Creates a SpinBox in parent p that accepts integers with minimum 0, maximum 100 and line step 1.


	@p object: The parent widget or layout.

	@returns: The created BCSpinBox.

	"""

def BCSpinBoxCreateDouble(p, min, max, step, decimals):

	"""

	Creates a SpinBox in parent p, that accepts float/double values.


	@p object: The parent widget or layout.

	@min float: The minimum allowed value.

	@max float: The maximum allowed value.

	@step float: The step.

	@decimals integer: the number of displayed decimals.

	@returns: The created BCSpinBox.

	"""

def BCSpinBoxGetText(sb):

	"""

	Returns the text of BCSpinBox sb.


	@sb object: the BCSpinBox.

	@returns: the text of the BCSpinBox without any prefix or suffix.

	"""

def BCSpinBoxGetInt(sb):

	"""

	Returns the text of the BCSpinBox sb in int format.


	@sb object: the BCSpinBox.

	@returns: the value of the BCSpinBox.

	"""

def BCSpinBoxGetDouble(sb):

	"""

	Returns the text of the BCSpinBox sb in double format.


	@sb object: the BCSpinBox.

	@returns: the value of the BCSpinBox.

	"""

def BCSpinBoxSetDoubleValue(sb, value):

	"""

	Sets the double value of spin box sb to value value.


	@sb object: the BCSpinBox.

	@value float: the new double value of the BCSpinBox.

	"""

def BCSpinBoxSetMinValueDouble(sb, min):

	"""

	Sets the minimum double value of the spin box.


	@sb object: the BCSpinBox.

	@min float: the minimum double value of the spin box.

	"""

def BCSpinBoxMinValueDouble(sb):

	"""

	Gets the minimum double value of the spin box.


	@sb object: the BCSpinBox.

	@returns: the minimum double value of the spin box.

	"""

def BCSpinBoxSetMaxValueDouble(sb, max):

	"""

	Sets the maximum double value of the spin box.


	@sb object: the BCSpinBox.

	@max float: the maximum double value of the spin box.

	"""

def BCSpinBoxMaxValueDouble(sb):

	"""

	Gets the maximum double value of the spin box.


	@sb object: the BCSpinBox.

	@returns: the maximum double value of the spin box

	"""

def BCSpinBoxSetStepAndDigits(sb, step, digits):

	"""

	Sets the stepping value of the spin box and the number of digits to display.


	@sb object: the BCSpinBox.

	@step float: the stepping in double format

	@digits integer: the number of digits to display

	"""

def BCSpinBoxGetDigits(sb):

	"""

	Returns the number of digits to display.


	@sb object: the BCSpinBox.

	@returns: the number of digits to display.

	"""

def BCSpinBoxSetMinValue(sb, min):

	"""

	Sets the minimum integer value of the spin box (default 0).


	@sb object: the BCSpinBox.

	@min integer: the minimum integer value of the spin box.

	"""

def BCSpinBoxMinValue(sb):

	"""

	Gets the minimum integer value of the spin box.


	@sb object: the BCSpinBox.

	@returns: the minimum integer value of the spin box.

	"""

def BCSpinBoxSetMaxValue(sb, max):

	"""

	Sets the maximum integer value of the spin box (default 100).


	@sb object: the BCSpinBox.

	@max integer: the maximum integer value of the spin box.

	"""

def BCSpinBoxMaxValue(sb):

	"""

	Gets the maximum integer value of the spin box.


	@sb object: the BCSpinBox.

	@returns: the maximum integer value of the spin box

	"""

def BCSpinBoxSetLineStep(sb, step):

	"""

	Sets the line step to step (default 1).
	When the user uses the arrows to change the spin box's value the value will be incremented/decremented by the amount of the line step.


	@sb object: the BCSpinBox.

	@step integer: the line step of spinbox.

	"""

def BCSpinBoxGetLineStep(sb):

	"""

	Returns the line step of BCSpinBox sb.
	When the user uses the arrows to change the spin box's value the value will be incremented/decremented by the amount of the line step.


	@sb object: the BCSpinBox.

	@returns: the line step of BCSpinBox.

	"""

def BCSpinBoxSetWrapping(sb, on):

	"""

	Sets whether it is possible to step the value from the highest value to the lowest value and vice versa to on.
	If you have a range of 0..100 and wrapping is off when the user reaches 100 and presses the Up Arrow nothing will happen; but if wrapping is on the value will change from 100 to 0, then to 1, etc. When wrapping is on, navigating past the highest value takes you to the lowest and vice versa.


	@sb object: the BCSpinBox.

	@on boolean: holds whether it is possible to step the value from the highest value to the lowest value and vice versa.By default, wrapping is turned off.

	"""

def BCSpinBoxWrapping(sb):

	"""

	Returns the wrapping behavior of BCSpinBox sb.


	@sb object: the BCSpinBox.

	@returns: True if it is possible to step the value from the highest value to the lowest value and vice versa; otherwise returns False.

	"""

def BCSpinBoxSetValueChangedFunction(sb, funct, data):

	"""

	Sets the function that will be called every time the value of the spin box changes.
	Use this function when you have integer values.


	@sb object: the BCSpinBox

	@funct callback: the function that will be called when the value of the BCSpinBox changes. See BC_SPINBOX_VALUE_CHANGED_FUNCTION for details.
	integer BC_SPINBOX_VALUE_CHANGED_FUNCTION(sb, val, data)
	The function to be called every time the integer value of the spinbox changes.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	sb    object    the BCSpinBox.
	val   integer   the new spinbox value.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)anything required by funct. If data is not required, it should be set to None.

	"""

def BCSpinBoxSetDoubleValueChangedFunction(sb, funct, data):

	"""

	Sets the function that will be called every time the value of the spin box changes.
	Use this function when you have double values.


	@sb object: the BCSpinBox

	@funct callback: the function that will be called when the value of the BCSpinBox changes. 
	See BC_SPINBOX_DOUBLE_VALUE_CHANGED_FUNCTION for details.
	integer BC_SPINBOX_DOUBLE_VALUE_CHANGED_FUNCTION(sb, val, data)
	The function to be called every time the double value of the spinbox changes.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	sb    object    the BCSpinBox.
	val   float     the new spinbox value.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct. 
	If data is not required, it should be set to None.

	"""

def BCSpinBoxSetValueChangedOnMouseRelease(sb, onMouseRelease):

	"""

	Sets whether BCSpinBox's sb value changed callback will be called only on mouse release or not.
	This function is not supported under VR mode.
	


	@sb object: the BCSpinBox.

	@onMouseRelease boolean: set this parameter to True for sb so that value changed callback will be called only on mouse release, or False otherwise.

	"""

def BCSpinBoxValueChangedOnMouseRelease(sb):

	"""

	Returns whether BCSpinBox's sb value changed callback will be called only on mouse release or not.
	This function is not supported under VR mode.
	


	@sb object: the BCSpinBox.

	@returns: True if value changed callback will be called only on mouse release, or False otherwise.

	"""

def BCSpinBoxSetValue(sb, value):

	"""

	Sets the value of spin box sb to value value.


	@sb object: the BCSpinBox.

	@value integer: the new value of the BCSpinBox.

	"""

def BCSpinBoxSetSuffix(sb, text):

	"""

	Sets the suffix of BCSpinBox sb to text.
	The suffix is appended at the end of the displayed value. Typical use is to display a unit of measurement or a currency symbol. For example: 
	sb-&gt;setSuffix( " km" );
	To turn off the suffix display, set this property to an empty string. The default is no suffix.


	@sb object: the BCSpinBox.

	@text string: the new suffix.

	"""

def BCSpinBoxSetPrefix(sb, text):

	"""

	Sets the prefix of BCSpinBox sb to text.
	The prefix is prepended to the start of the displayed value. Typical use is to display a unit of measurement or a currency symbol. For example:
	sb-&gt;setPrefix( "$" );
	To turn off the prefix display, set this property to an empty string. The default is no prefix.


	@sb object: the BCSpinBox.

	@text string: the new prefix.

	"""

def BCSpinBoxSetFixedDigitsNumber(sb, numDigits):

	"""

	Sets the width of the spinbox sb to the width that numDigits hold.
	Use this function if you want for example to design a spinBox with sensible width that accepts only two digits (values from 0 to 99).


	@sb object: the BCSpinBox.

	@numDigits integer: the number of characters.

	"""

def BCSplitterCreate(p, o):

	"""

	Creates a new BCSplitter.
	Note that BCSplitter automatically saves the sizes of the managed widgets in xml file.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout of the BCSplitter.

	@o integer: the orientation of the BCSplitter. See BCEnumOrientation for details.
	
	guitk.constants BCEnumOrientation
	This type is used to signify an object's orientation. Orientation is used with BCButtonGroupCreate for example.
	 - guitk.constants.BCHorizontal
	sets horizontal orientation.
	 - guitk.constants.BCVertical
	sets vertical orientation.

	@returns: the created BCSplitter.

	"""

def BCSplitterSetCollapsible(sp, w, collapse):

	"""

	Checks whether a widget w is a child of BCSplitter sp and sets it collapsible or not.
	This function is not supported under VR mode.
	


	@sp object: the BCSplitter.

	@w object: the widget, child of sp.

	@collapse boolean: values are False if the widget should not be collapsible, otherwise True (default).

	"""

def BCSplitterMoveToFirst(sp, w):

	"""

	Moves to the beginning (top or left, depending on the orientation of the BCSplitter) a certain widget.
	This function is not supported under VR mode.
	


	@sp object: the BCSplitter.

	@w object: the widget, child of sp.

	"""

def BCSplitterMoveToLast(sp, w):

	"""

	Moves to the end (bottom or right, depending on the orientation of the BCSplitter) a certain widget.
	This function is not supported under VR mode.
	


	@sp object: the BCSplitter.

	@w object: the widget, child of sp.

	"""

def BCSplitterSetHandleWidth(sp, width):

	"""

	Sets the width of the handle of the BCSplitter
	This function is not supported under VR mode.
	


	@sp object: the BCSplitter.

	@width integer: the new width in pixels.

	"""

def BCSplitterSetResizeMode(sp, w, mode):

	"""

	Function is obsolete. Use BCSplitterSetWidgetStretchFactor() instead, using stretch: 0 for BCKeepSize, 1 otherwise.
	This function is not supported under VR mode.
	


	@sp object: the BCSplitter.

	@w object: the widget, child of sp.

	@mode integer: the resize mode. See BCEnumResizeMode for details.
	
	guitk.constants BCEnumResizeMode
	This enum type describes how BCSplitter will resize each of its child widgets. Resize mode is used with BCSplitterSetResizeMode().
	 - guitk.constants.BCResizeAuto
	the widget will be resized according to the stretch factors set in its sizePolicy().
	 - guitk.constants.BCResizeStretch
	the widget will be resized when the splitter itself is resized.
	 - guitk.constants.BCResizeKeepSize
	BCSplitter will try to keep the widget's size unchanged.
	 - guitk.constants.BCResizeFollowSizeHint
	BCSplitter will resize the widget when the widget's size hint changes.

	"""

def BCSplitterSetOrientation(sp, o):

	"""

	Sets the orientation of BCSplitter vertical or horizontal with the BCVertical and BCHorizontal respectively.
	This function is not supported under VR mode.
	


	@sp object: the BCSplitter whose the orientation changes

	@o integer: the orientation, BCVertical or BCHorizontal

	"""

def BCStatusBarCreate(p):

	"""

	Creates a StatusBar with parent p.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@returns: the created StatusBar.

	"""

def BCStatusBarAddWidget(sb, w, permanent):

	"""

	Adds widget w to StatusBar sb.
	w is permanently visible if permanent is True and may be obscured by temporary messages if permanent is False.
	Most of times it should be set to False. Also, if permanent is set to True, w is located at the far right of the status bar.
	If permanent is False (the default), widget is located just to the left of the first permanent widget.
	This function is not supported under VR mode.
	


	@sb object: the StatusBar.

	@w object: the widget that will be added.

	@permanent boolean: set this parameter to True or False for setting if the widget w should be permanently visible or not, respectively.

	"""

def BCStatusBarRemoveWidget(sb, w):

	"""

	Removes widget w from StatusBar sb.
	This function is not supported under VR mode.
	


	@sb object: the StatusBar.

	@w object: the widget that will be removed.

	"""

def BCStatusBarMessage(sb, message):

	"""

	Shows message on the status bar sb.
	This function is not supported under VR mode.
	


	@sb object: the StatusBar.

	@message string: the text that will be displayed.

	"""

def BCStatusBarTimedMessage(sb, message, ms):

	"""

	Shows message on the status bar sb for ms milliseconds. Then message is removed.
	This function is not supported under VR mode.
	


	@sb object: the StatusBar.

	@message string: the text that will be displayed.

	@ms integer: the time period for which message will be displayed in milliseconds.

	"""

def BCStatusBarClear(sb):

	"""

	Removes any message is currently being shown.
	This function is not supported under VR mode.
	


	@sb object: the StatusBar.

	"""

def BCStatusBarSetSizeGripEnabled(sb, enabled):

	"""

	Sets whether size grip (arrow at bottom right that resize window) is enabled.
	This function is not supported under VR mode.
	


	@sb object: the StatusBar.

	@enabled boolean: set False to hide the size grip or True to show it (default).

	"""

def BCTableCreate(p, numRows, numCols):

	"""

	Creates a BCTable (like spreadsheet).
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@numRows integer: the number of rows.

	@numCols integer: the number of columns.

	@returns: the created BCTable.

	"""

def BCTableSetCellValueDouble(t, row, col, val):

	"""

	Inserts the double value val in BCTable t at row row and column col.
	This function is not supported under VR mode.
	


	@t object: the BCTable where the value will be inserted.

	@row integer: the row.

	@col integer: the column.

	@val float: the double value.

	"""

def BCTableGetCellValueDouble(t, row, col):

	"""

	Gets the value of the BCTable t at row row and column col.
	This function is not supported under VR mode.
	


	@t object: the BCTable from which the value will be extracted.

	@row integer: the row.

	@col integer: the column.

	@returns: A tuple with two items:
	First item is value True on success False otherwise.
	Second item is the requested double value. On failure it will be 0.

	"""

def BCTableNumCols(t):

	"""

	Returns the number of columns in BCTable t.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@returns: the number of columns for the given BCTable.

	"""

def BCTableNumRows(t):

	"""

	Returns the number of rows in BCTable t.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@returns: the number of rows for the given BCTable.

	"""

def BCTableSetNumCols(t, numCols):

	"""

	Sets the number of columns in BCTable t.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@numCols integer: the number of columns for the given BCTable.

	"""

def BCTableSetNumRows(t, numRows):

	"""

	Sets the number of rows in BCTable t.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@numRows integer: the number of rows for the given BCTable.

	"""

def BCTableSetCellWidget(t, row, col, w):

	"""

	Sets widget w to occupy the space of cell at row row and column col.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row.

	@col integer: the column.

	@w object: the widget (BCComboBox, BCCheckBox, BCButton etc.).

	"""

def BCTableGetCellWidget(t, row, col):

	"""

	Returns the widget that was set with BCTableSetCellWidget() at row row and column col. If no widget exists None is returned.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row.

	@col integer: the column.

	@returns: the widget at row row and column col or None if no widget is found.

	"""

def BCTableClearCellWidget(t, row, col):

	"""

	Removes the widget (if there is one) set for the cell at row, col.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row.

	@col integer: the column.

	"""

def BCTableSetRowHeight(t, row, height):

	"""

	Sets the height of row row in BCTable t to height pixels.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row.

	@height integer: the new height for row row.

	"""

def BCTableRowHeight(t, row):

	"""

	Returns the height of row row in BCTable t in pixels.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row.

	@returns: the height of row row in BCTable t.

	"""

def BCTableSetColumnWidth(t, col, width):

	"""

	Sets the width of column col in BCTable t, to width pixels.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@col integer: the column.

	@width integer: the new width for column col

	"""

def BCTableColumnWidth(t, col):

	"""

	Returns the width of column col in BCTable t in pixels.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@col integer: the column.

	@returns: the width of column col in BCTable t.

	"""

def BCTableShowColumn(t, col, show):

	"""

	Shows or hides column col, depending on the value of show.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@col integer: the column.

	@show boolean: set this parameter to False to hide, or True to show the column col.

	"""

def BCTableSetColumnsSorting(t, sort, wholeRows):

	"""

	Sorts a column when clicked on columns header, depending on the value of sort.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@sort boolean: set this parameter to True and the sort indicator is shown. After a click on the header of a column sorts that column.

	@wholeRows boolean: if set this parameter to True entire rows are sorted otherwise only cells in the column are sorted.

	"""

def BCTableIsColumnHidden(t, col):

	"""

	Returns True if column col is hidden, otherwise returns False.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@col integer: the column.

	@returns: True in case col is hidden; False otherwise.

	"""

def BCTableShowRow(t, row, show):

	"""

	Shows or hides row row, depending on the value of show.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row.

	@show boolean: set this parameter to False to hide, or True to show the row row.

	"""

def BCTableIsRowHidden(t, row):

	"""

	Returns True if row row is hidden, otherwise returns False.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row.

	@returns: True in case row is hidden; False otherwise.

	"""

def BCTableSelectRow(t, row):

	"""

	Selects row row from BCTable t.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row to be selected.

	"""

def BCTableIsRowSelected(t, row, full):

	"""

	Returns True if row row is selected, otherwise returns False.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row.

	@full boolean: set this parameter to False if at least one cell in the row needs to be selected to consider the row selected, or True if every cell in the row need to be selected to consider the row selected.

	@returns: True if row row is selected, otherwise returns False.

	"""

def BCTableSelectColumn(t, col):

	"""

	Selects column col from BCTable t.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@col integer: the column to be selected.

	"""

def BCTableIsColumnSelected(t, col, full):

	"""

	Returns True if column col is selected, otherwise returns False.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@col integer: the column.

	@full boolean: set this parameter to False if at least one cell in the column needs to be selected to consider the column selected, or True if every cell in the column needs to be selected to consider the column selected.

	@returns: True if column col is selected, otherwise returns False.

	"""

def BCTableSetRowStretchable(t, row, stretchable):

	"""

	Sets whether row row should be stretchable or not, depending on the value of stretchable.
	NOTE: If stretchable is set to True, then row row will not be resizable by the user and all available space will be filled.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row.

	@stretchable boolean: set this parameter to True for row row to be stretchable, or to False (default) otherwise.

	"""

def BCTableSetColumnStretchable(t, col, stretchable):

	"""

	Sets whether column col should be stretchable or not, depending on the value of stretchable.
	NOTE: If stretchable is set to True, then column col will not be resizable by the user and all available space will be filled.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@col integer: the column.

	@stretchable boolean: set this parameter to True for column col to be stretchable, or to False (default) otherwise.

	"""

def BCTableSetRowLabels(t, labels):

	"""

	Sets the labels labels show on the left header of the table.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@labels object: array of strings that will be displayed on the header.

	"""

def BCTableSetColumnLabels(t, labels):

	"""

	Sets the labels labels show on the top header of the table.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@labels object: array of strings that will be displayed on the header.

	"""

def BCTableHeaderSetLabel(t, o, section, text):

	"""

	Sets the label of a specific section of a header of BCTable t.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@o integer: specifies the header by its orientation. See BCEnumOrientation for details.
	
	guitk.constants BCEnumOrientation
	This type is used to signify an object's orientation. Orientation is used with BCButtonGroupCreate for example.
	 - guitk.constants.BCHorizontal
	sets horizontal orientation.
	 - guitk.constants.BCVertical
	sets vertical orientation.

	@section integer: the section of the header of which the label will be set.

	@text string: the text that the label will be set to.

	"""

def BCTableHeaderLabel(t, o, section):

	"""

	Returns the label displayed at section section of the header of the BCTable t specified by the orientation o.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@o integer: specifies the header by its orientation. See BCEnumOrientation for details.
	
	guitk.constants BCEnumOrientation
	This type is used to signify an object's orientation. Orientation is used with BCButtonGroupCreate for example.
	 - guitk.constants.BCHorizontal
	sets horizontal orientation.
	 - guitk.constants.BCVertical
	sets vertical orientation.

	@section integer: the section of the header of which the label will be returned.

	@returns: the label displayed at section section of the header of BCTable t specified by the orientation o.

	"""

def BCTableHeaderSetClickEnabled(t, o, section, enabled):

	"""

	Sets whether section section of header of BCTable t can be clicked or not, depending on the value enabled.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@o integer: specifies the header by its orientation. See BCEnumOrientation for details.
	
	guitk.constants BCEnumOrientation
	This type is used to signify an object's orientation. Orientation is used with BCButtonGroupCreate for example.
	 - guitk.constants.BCHorizontal
	sets horizontal orientation.
	 - guitk.constants.BCVertical
	sets vertical orientation.

	@section integer: the section of the header that will be set.

	@enabled boolean: set this parameter to True to enable click on section section, or False to disable it.

	"""

def BCTableHeaderSetResizeEnabled(t, o, section, enabled):

	"""

	Sets whether section section of the header of the BCTable t with orientation o can be resized by the user or not.
	WARNING: Do not use this function for sections that are not already created!
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@o integer: specifies the header by its orientation.
	See BCEnumOrientation for details.
	
	guitk.constants BCEnumOrientation
	This type is used to signify an object's orientation. Orientation is used with BCButtonGroupCreate for example.
	 - guitk.constants.BCHorizontal
	sets horizontal orientation.
	 - guitk.constants.BCVertical
	sets vertical orientation.

	@section integer: the section of the header that will be set.

	@enabled boolean: set this parameter to True (default) to enable resizing on the section section, or False to disable it.

	"""

def BCTableHeaderSetResizeEnabledAllSections(t, o, enabled):

	"""

	Sets whether the sections of the header of the BCTable t with orientation o can be resized by the user or not.
	NOTE: This function applies for the whole header, this is, all the sections that are already created and the sections that
	will be created in the future.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@o integer: specifies the header by its orientation. See BCEnumOrientation for details.
	
	guitk.constants BCEnumOrientation
	This type is used to signify an object's orientation. Orientation is used with BCButtonGroupCreate for example.
	 - guitk.constants.BCHorizontal
	sets horizontal orientation.
	 - guitk.constants.BCVertical
	sets vertical orientation.

	@enabled boolean: set this parameter to True to enable resizing on the section section, or False to disable it.

	"""

def BCTableShowHeader(t, o, show):

	"""

	Shows or hides either the horizontal or vertical header of BCTable t, depending on the value of show.
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@o integer: use this parameter to specify which header to show/hide by its orientation.
	See BCEnumOrientation for details.
	
	guitk.constants BCEnumOrientation
	This type is used to signify an object's orientation. Orientation is used with BCButtonGroupCreate for example.
	 - guitk.constants.BCHorizontal
	sets horizontal orientation.
	 - guitk.constants.BCVertical
	sets vertical orientation.

	@show boolean: set this parameter to True to show a header, or to False to hide it.

	"""

def BCTableSetLeftMargin(t, pixels):

	"""

	Sets the left margin to be pixels wide.
	WARNING: This function is obsolete! It works only for pixels set to zero, which hides the
	vertical header on the left of the table. Use BCTableShowHeader() function.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@pixels integer: the new width in pixels.

	"""

def BCTableSetTopMargin(t, pixels):

	"""

	Sets the top margin to be pixels high.
	WARNING: This function is obsolete! It works only for pixels set to zero, which hides the
	horizontal header on the top of the table. Use BCTableShowHeader() function.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@pixels integer: the new height in pixels.

	"""

def BCTableSetMouseClickedFunction(t, funct, data):

	"""

	Sets the function that will be called when mouse button clicked inside table t (will not run if click on empty area).
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@funct callback: the function that will be called on mouse button click.
	See BC_TABLE_MOUSE_CLICKED_FUNCTION for details.
	integer BC_TABLE_MOUSE_CLICKED_FUNCTION(t, mb, row, col, data)
	The function to be called when the mouse button is clicked inside table cell.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	t     object    the BCTable.
	mb    integer   the mouse button clicked (left is 1, right is 2 and middle is 4).
	row   integer   the row of the table clicked.
	col   integer   the column of the table clicked.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCTableSetMousePressedFunction(t, funct, data):

	"""

	Sets the function that will be called when mouse button pressed inside table t (operates on empty area as well).
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@funct callback: the function that will be called on mouse button press.
	See BC_TABLE_MOUSE_PRESSED_FUNCTION for details.
	integer BC_TABLE_MOUSE_PRESSED_FUNCTION(t, mb, row, col, data)
	The function to be called when the mouse button pressed inside table (operates on empty area as well).
	If you press on empty area below last row you will receive -1 (the same for column).
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	t     object    the BCTable.
	mb    integer   the mouse button pressed (left is 1, right is 2 and middle is 4).
	row   integer   the row of the table pressed.
	col   integer   the column of the table pressed.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCTableSetHeaderMousePressedFunction(t, funct, data):

	"""

	Sets the function that will be called when the horizontal header of the table mouse pressed.
	The default table behavior (row or col selection) on left click on header will operate as well.
	This function is not supported under VR mode.
	


	@t object: the BCTable to affect.

	@funct callback: the function that will be called on mouse button press on header.
	See BC_TABLE_HEADER_MOUSE_PRESSED_FUNCTION for details.
	integer BC_TABLE_HEADER_MOUSE_PRESSED_FUNCTION(t, mb, columnIndex, data)
	The function to be called when the left mouse button is clicked on the header of the column with index columnIndex.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	t            object    the BCTable.
	mb           integer   the mouse button pressed (left is 1, right is 2 and middle is 4).
	columnIndex  integer   the index of the column clicked.
	data         anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCTableSetSelectionMode(t, mode):

	"""

	Sets the current selection mode to mode.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@mode integer: the selection mode. See BCEnumTableSelectionMode 
	for details.
	
	guitk.constants BCEnumTableSelectionMode
	This enum type defines the selection mode of the cells of a BCTable. Selecton is used
	at BCTableSetSelectionMode().
	 - guitk.constants.BCTableNoSelection
	no cell can be selected by the user.
	 - guitk.constants.BCTableMulti
	When the user selects an item in the usual way, the selection is cleared and the new item selected. However, if the user presses the Ctrl key when clicking on an item, the clicked item gets toggled and all other items are left untouched. If the user presses the Shift key while clicking on an item, all items between the current item and the clicked item are selected or unselected, depending on the state of the clicked item. Multiple items can be selected by dragging the mouse over them
	 - guitk.constants.BCTableSingle
	the user may only select a single range of cells.
	 - guitk.constants.BCTableContiguous
	When the user selects an item in the usual way, the selection is cleared and the new item selected. However, if the user presses the Shift key while clicking on an item, all items between the current item and the clicked item are selected or unselected, depending on the state of the clicked item.
	 - guitk.constants.BCTableSingleRow
	The user may select one row at once.
	 - guitk.constants.BCTableMultiRow
	The user may select multiple rows.

	"""

def BCTableSetColumnReadOnly(t, col, readOnly):

	"""

	Sets whether column col is read only or not.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@col integer: the column.

	@readOnly boolean: set this parameter to True to set column col as read only, or False to set it editable.

	"""

def BCTableIsColumnReadOnly(t, col):

	"""

	Returns True if column col is read only, otherwise returns False.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@col integer: the column.

	@returns: True if col is read-only; False otherwise.

	"""

def BCTableSetRowReadOnly(t, row, readOnly):

	"""

	Sets whether row row is read only or not.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row.

	@readOnly boolean: set this parameter to True to set row row as read only, or False to set it editable.

	"""

def BCTableRowReadOnly(t, row):

	"""

	Returns True if row row is read only, otherwise returns False.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row.

	@returns: True if row is read-only; False otherwise.

	"""

def BCTableInsertColumns(t, col, count):

	"""

	Inserts count empty columns at column col. Also clears the selection(s).
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@col integer: the column where the new columns will be added.

	@count integer: the number of new columns that will be added.

	"""

def BCTableInsertRows(t, row, count):

	"""

	Inserts count empty rows at row index row. Also clears the selection(s).
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row index where the new rows will be added.

	@count integer: the number of new rows that will be added.

	"""

def BCTableRemoveRow(t, row):

	"""

	Removes the row row from table t.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the section number of the row that will be removed.

	"""

def BCTableRemoveColumn(t, col):

	"""

	Removes column col from table t.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@col integer: the section number of the column that will be removed.

	"""

def BCTableAdjustColumn(t, col):

	"""

	Resizes column col so that the column width is wide enough to display the widest visible item in the column.
	NOTE: Like when double-clicking a header handler in a BCTable, the width of the column will become wide enough to
	fully display all visible items but not all items col contains!
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@col integer: the number of the column that will be adjusted.

	"""

def BCTableAdjustRow(t, row):

	"""

	Resizes row row so that the row height is tall enough to display the tallest item the row contains.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the number of the row that will be adjusted.

	"""

def BCTableBlockAutoAdjustColumns(t, block):

	"""

	Blocks/unblocks the auto-adjust of the columns of BCTable t after altering the text of a cell.
	This function is very useful in case you want to alter the text of many cells in a loop without losing in performance.
	NOTE: Keep in mind that after unblocking the auto-adjust feature, you are responsible to re-adjust the columns
	affected, either by calling BCTableAdjustColumn or by moving/double-clicking the corresponding header handler.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@block boolean: set this to 1 to block auto-adjust columns feature; 0 otherwise. By default, this value is 0.

	"""

def BCTableIsBlockedAutoAdjustColumns(t):

	"""

	Returns whether auto-adjust of the columns of BCTable t is blocked.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@returns: 1 if auto-adjust of the columns of BCTable t is blocked; 0 otherwise.

	"""

def BCTableSetText(t, row, col, text):

	"""

	Sets the text in the cell at row row and column col to text.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row.

	@col integer: the column.

	@text string: the text that the cell will display.

	"""

def BCTableText(t, row, col):

	"""

	Returns the text at row row and column col, or None if row/col does not exist.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row.

	@col integer: the column.

	@returns: the text at row row and column col, or None if row/col does not exist.

	"""

def BCTableHeaderSetIndexChangedFunction(t, o, funct, data):

	"""

	Sets the function that will be called when the index of a header section changes.
	
	NOTE: Currently the moving/swaping of rows and columns is not available. Using this function has no effect.
	This function is not supported under VR mode.
	


	"""

def BCTableCurrentColumn(t):

	"""

	Returns the index number of the current column of BCTable t.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@returns: the index number of the current column.

	"""

def BCTableCurrentRow(t):

	"""

	Returns the index number of the current row of BCTable t.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@returns: the index number of the current row.

	"""

def BCTableSetBeginEditFunction(t, funct, data):

	"""

	Set a function to be called when editing of a cell starts.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@funct callback: the function that will be called. See BC_TABLE_BEGIN_EDIT_FUNCTION for details.
	integer BC_TABLE_BEGIN_EDIT_FUNCTION(t, row, col, replace, data)
	The function to be called when in-place editing of the cell at row row and column col starts.
	Note that each cell has an editor (something like a lineEdit) which is used as a medium for editing the cell.
	If replace is 1 editor initializes empty (for example when you are moving with arrow keys in a table and edit an already full cell). If replace is 0 this means that the editor will be initialized with the cell's content, if any (for example if you mouse doubleClick an already full cell). Editor's contents will be copied to the cell if for example you press Enter (or mouse click outside table), and will not be copied if you cancel by pressing Esc.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	t        object    the BCTable.
	row      integer   the row of the cell.
	col      integer   the column of the cell.
	replace  integer   if 1 the editor will start empty; otherwise it will be initialized with the cell's content (if any).
	data     anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCTableSetEndEditFunction(t, funct, data):

	"""

	Sets the function to be called when editing of a cell ends.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@funct callback: the function that will be called. See BC_TABLE_END_EDIT_FUNCTION for details.
	integer BC_TABLE_END_EDIT_FUNCTION(t, row, col, accept, replace, data)
	This function will be called when in-place editing of the cell at row row and column col ends.
	Note that each cell has an editor (something like a lineEdit) which is used as a medium for editing the cell.
	If accept is 1 the editor's text considered valid and will be copied to the current cell. If the user cancels the editor accept is 0 and the contents of the cell are left unchanged. If replace is 1 this editor initializes empty (for example when you are moving with arrow keys in a table and edit an already full cell). If replace is 0 this means that the editor will be initialized with the cell's content, if any (for example if you mouse doubleClick an already full cell). 
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	t        object    the BCTable.
	row      integer   the row of the cell.
	col      integer   the column of the cell.
	accept   integer   1 if the entered text has considered valid and will be copied to the cell, or 0 otherwise.
	replace  integer   if 1 the editor will start empty; otherwise it will be initialized with the cell's content (if any).
	data     anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCTableSetNumberOfRowsChangedFunction(t, funct, data):

	"""

	Set a function to be called when the number of rows has been changed.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@funct callback: the function that will be called. See BC_TABLE_NUMBER_OF_ROWS_CHANGED_FUNCTION for details.
	integer BC_TABLE_NUMBER_OF_ROWS_CHANGED_FUNCTION(t, data)
	The function to be called when the number of BCTable's rows has been changed.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	t     object    the BCTable.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCTableSetNumberOfColumnsChangedFunction(t, funct, data):

	"""

	Set a function to be called when the number of columns has been changed.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@funct callback: the function that will be called. See BC_TABLE_NUMBER_OF_COLUMNS_CHANGED_FUNCTION for details.
	integer BC_TABLE_NUMBER_OF_COLUMNS_CHANGED_FUNCTION(t, data)
	The function to be called when the number of BCTable's columns has been changed.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	t     object    the BCTable.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCTableSetCurrentCellChangedFunction(t, funct, data):

	"""

	Set the function to run when the current cell of t has changed.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@funct callback: the function that will be called when cell has changed. See BC_TABLE_CURRENT_CELL_CHANGED_FUNCTION for details.
	integer BC_TABLE_CURRENT_CELL_CHANGED_FUNCTION(t, row, col, data)
	The function to be called when the current cell has changed.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	t     object    the BCTable.
	row   integer   the new current row.
	col   integer   the new current column.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCTableSetRowInsertEnabled(t, enable):

	"""

	Set if the user will be able to insert new rows using keyboard events.
	The default table enables the user to insert new rows.
	New rows in BCTables can be inserted by pressing Tab when current focused cell is the bottom right most cell, or by pressing Return when the current focused is on the last (bottom) row of the table.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@enable boolean: set False to disable inserting new rows, otherwise set True.

	"""

def BCTableSetMaxRows(t, maxRows):

	"""

	Sets the maximun number of rows allowed to be inserted in BCTable t.
	Rows can be inserted when pressing Enter and current cell is at last row.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@maxRows integer: the maximun number of rows for the given BCTable.

	"""

def BCTableSetMaxCols(t, maxCols):

	"""

	Sets the maximun number of columns allowed to be inserted in BCTable t.
	One way to insert columns is via column menu (add item enabled).
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@maxCols integer: the maximun number of columns for the given BCTable.

	"""

def BCTableSetReadOnly(t, readOnly):

	"""

	Sets whether the BCTable t is to be read-only to readOnly.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@readOnly boolean: True to set BCTable t to be read-only, otherwise False to set BCTable t to be editable.

	"""

def BCTableSetValueChangedFunction(t, funct, data):

	"""

	Sets the function that will be called when the user changes the value in a cell.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@funct callback: the function that will be called on value changed event.
	See BC_TABLE_VALUE_CHANGED_FUNCTION for details.
	integer BC_TABLE_VALUE_CHANGED_FUNCTION(t, row, col, data)
	The function to be called when the user changes the value in the cell.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	t     object    the BCTable.
	row   integer   the row of the cell in which the user changed the value.
	col   integer   the column of the cell in which the user changed the value.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)a pointer to any data required by funct.

	"""

def BCTableSetColumnAcceptsText(t, col, val):

	"""

	Sets the ability to enter non numeric text in the tables' fields.
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@col integer: the column.

	@val boolean: set this parameter to True to enable text entry, or False to disable text entry.

	"""

def BCTableColumnAcceptsText(t, col):

	"""

	Returns True if text entry is enabled for the field of BCTable t, or False otherwise.
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@col integer: the column index

	@returns: True if text entry is enabled, False if text entry is disabled.

	"""

def BCTableGetPopupMenu(t):

	"""

	Returns the popup menu created.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@returns: the default popup menu created.

	"""

def BCTableSetColumnMenuActivatedFunction(t, funct, data):

	"""

	Sets the function to be called when the column popup menu is activated, i.e. an item is selected.
	The function will be called right after the change of visibility status of the column.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@funct callback: the function that will be called. See
	BC_TABLE_COLUMN_MENU_ACTIVATED_FUNCTION for details.
	integer BC_TABLE_COLUMN_MENU_ACTIVATED_FUNCTION(t, column, data)
	The function to be called when the user activates the column popup menu of the table.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	t       object    the BCTable.
	column  integer   the column which will show/hide on activation of popup menu.
	data    anything  anything that may be required in this function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)a pointer to any data required by funct.

	"""

def BCTableSetColumnAlignment(t, col, alignment):

	"""

	Sets the cells alignment of the column col to alignment.
	NOTE: Column alignment has higher priority than row's one. This means that if, for a cell, has been set
	row and column alignment, then its column alignment will be used, independetly of which one has been set most recently!
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@col integer: the column.

	@alignment integer: the alignment that will be set. It is an integer value that is composed of
	BCEnumAlignment OR'ed together. See BCEnumAlignment for details. For convenience, if
	alignment doesn't contains any vertical-type value (i.e. BCAlignTop or BCAlignBottom), alignment gets OR'ed with BCAlignVCenter.
	
	guitk.constants BCEnumAlignment
	This enum type is used to describe alignment. It contains horizontal and vertical flags. Alignment is used with BCGridLayoutAddMultiCellWidget for example.
	NOTE: You can use at most one horizontal and one vertical flag at a time.
	 - guitk.constants.BCAlignAuto
	aligns according to the language. Left for most, right for Arabic and Hebrew.
	 - guitk.constants.BCAlignLeft
	aligns with the left edge.
	 - guitk.constants.BCAlignRight
	aligns with the right edge.
	 - guitk.constants.BCAlignHCenter
	centers horizontally in the available space.
	 - guitk.constants.BCAlignJustify
	justifies the text in the available space.
	 - guitk.constants.BCAlignTop
	aligns with the top.
	 - guitk.constants.BCAlignBottom
	aligns with the bottom.
	 - guitk.constants.BCAlignVCenter
	centers vertically in the available space.
	 - guitk.constants.BCAlignCenter
	centers in both dimensions (vertically and horizontally).
	 - guitk.constants.BCAlignHorizontal_Mask
	horizontal mask.
	 - guitk.constants.BCAlignVertical_Mask
	vertical mask.
	 - guitk.constants.BCAlignVJustify
	Justifies the text vertically in the available space.

	"""

def BCTableSetRowAlignment(t, row, alignment):

	"""

	Sets the cells alignment of the row row to alignment.
	NOTE: Column alignment has higher priority than row's one. This means that if, for a cell, has been set
	row and column alignment, then its column alignment will be used, independetly of which one has been set most recently!
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row.

	@alignment integer: the alignment that will be set. It is an integer value that is composed of
	BCEnumAlignment OR'ed together. See BCEnumAlignment for details. For convenience, if
	alignment doesn't contains any vertical-type value (i.e. BCAlignTop or BCAlignBottom), alignment gets OR'ed with BCAlignVCenter.
	
	guitk.constants BCEnumAlignment
	This enum type is used to describe alignment. It contains horizontal and vertical flags. Alignment is used with BCGridLayoutAddMultiCellWidget for example.
	NOTE: You can use at most one horizontal and one vertical flag at a time.
	 - guitk.constants.BCAlignAuto
	aligns according to the language. Left for most, right for Arabic and Hebrew.
	 - guitk.constants.BCAlignLeft
	aligns with the left edge.
	 - guitk.constants.BCAlignRight
	aligns with the right edge.
	 - guitk.constants.BCAlignHCenter
	centers horizontally in the available space.
	 - guitk.constants.BCAlignJustify
	justifies the text in the available space.
	 - guitk.constants.BCAlignTop
	aligns with the top.
	 - guitk.constants.BCAlignBottom
	aligns with the bottom.
	 - guitk.constants.BCAlignVCenter
	centers vertically in the available space.
	 - guitk.constants.BCAlignCenter
	centers in both dimensions (vertically and horizontally).
	 - guitk.constants.BCAlignHorizontal_Mask
	horizontal mask.
	 - guitk.constants.BCAlignVertical_Mask
	vertical mask.
	 - guitk.constants.BCAlignVJustify
	Justifies the text vertically in the available space.

	"""

def BCTabWidgetCreate(p):

	"""

	Creates a BCTabWidget.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@returns: the created BCTabWidget.

	"""

def BCTabWidgetAddTab(tw, w, label):

	"""

	Adds a tab with the given widget w as a page and label label to the BCTabWidget tw.
	Newly added tab becomes the current tab.
	If you add tab after show, you may cause flicker.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@w object: the widget to append as a page to the added tab.

	@label string: the title of the new tab.

	"""

def BCTabWidgetInsertTab(tw, w, label, index):

	"""

	Inserts a tab with the given widget w as a page to the BCTabWidget at position index.
	Newly inserted tab becomes the current tab.
	If you insert tab after show, you may cause flicker.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@w object: the widget to insert as a page to the inserted tab.

	@label string: the title of the new tab.

	@index integer: If index is out of range, the tab is simply appended. Otherwise it is inserted at the specified position.

	"""

def BCTabWidgetRemoveTab(tw, w):

	"""

	Removes the tab containing the page widget w from the BCTabWidget tw.
	
	NOTE: The page widget w itself is not deleted. Use BCDestroy() if you want to delete it.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@w object: the page widget contained in the tab that we want to remove from the stack.

	"""

def BCTabWidgetSetTabMovingEnabled(tw, enable):

	"""

	Enables or disables (default) tab repositioning.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@enable boolean: set value True to enable repositioning or False to disable it.

	"""

def BCTabWidgetSetCurrentTab(tw, w):

	"""

	Sets the tab containing the page widget w as the current tab of the BCTabWidget tw.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@w object: the page widget contained by the tab we want to focus on.

	"""

def BCTabWidgetGetCurrentTab(tw):

	"""

	Gets the page widget contained by the current tab of the BCTabWidget.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@returns: the page widget of the current tab of the BCTabWidget.

	"""

def BCTabWidgetSetTabLabel(tw, w, label):

	"""

	Sets the title of tab containing the page widget w of the BCTabWidget tw to label.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@w object: the page widget contained by the tab whose title we want to set.

	@label string: the string of the title (label) that will be set.

	"""

def BCTabWidgetGetTabLabel(tw, w):

	"""

	Gets the title of the tab containing page widget w of the BCTabWidget.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@w object: the page widget of the tab whose title we want to get.

	@returns: a string of the title (label) of the tab.

	"""

def BCTabWidgetSetCurrentChangedFunction(tw, funct, data):

	"""

	Sets the function that will be called when the current tab changes.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@funct callback: the function that will be called. See BC_TABWIDGET_CURRENT_CHANGED_FUNCTION for details.
	integer BC_TABWIDGET_CURRENT_CHANGED_FUNCTION(tw, oldTab, newTab, data)
	The function to be called when the current tab changes.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	tw      object    the BCTabWidget.
	oldTab  object    the old tab widget.
	newTab  object    the new tab widget.
	data    anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any user data required by function funct.

	"""

def BCTabWidgetCount(tw):

	"""

	Returns the number of tabs in BCTabWidget tw.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@returns: the number of tabs in a BCTabWidget.

	"""

def BCTabWidgetIndexOf(tw, w):

	"""

	Returns the index position of the tab containing the page widget w in BCTabWidget tw or -1 if widget cannot be found.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@w object: the page widget.

	@returns: the index position of the tab containing the page widget w, or -1 if the widget cannot be found.

	"""

def BCTabWidgetGetTab(tw, index):

	"""

	Returns the page widget of the tab at index index of BCTabWidget or None if index is out of range.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@index integer: the index.

	@returns: the page widget of tab at index index.

	"""

def BCTabWidgetTabGetTabWidget(w):

	"""

	Returns the BCTabWidget of page widget w.
	This function is not supported under VR mode.
	


	@w object: the page widget contained in a tab of a BCTabWidget.

	@returns: the parent BCTabWidget.

	"""

def BCTabWidgetSetTabBarAutoHideEnabled(tw, enable):

	"""

	Use this function to enable or disable auto hide feature of the tab bar when only one tab exists.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@enable boolean: set this parameter to True to enable the auto hide feature, False to disable it.

	"""

def BCTabWidgetSetTabButtonFunctionAndIcons(tw, act, funct, data, enabledIcon, disabledIcon, focusedIcon, pressedIcon):

	"""

	Function is obsolete. Use BCTabWidgetSetTabsClosableEnabled() instead.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@act integer: the action to be taken when an icon is clicked and the user function returns 1 (e.g. you can hide or delete the tab).

	@funct callback: the user function that will be called. See BC_TABWIDGET_BUTTON_SET_FUNCTION for details.
	integer BC_TABWIDGET_BUTTON_SET_FUNCTION(tw, tab, data)
	The function to be called when a pixmap with a callback function is needed to be created on a tab of a BCTabWidget.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	tw    object    the BCTabWidget.
	tab   object    the current tab (i.e. the created widget that made tab).
	data  anything  anything that may be required in function.
	
	Return: Return 1 in case you want to run the action set; 0 otherwise.

	@data anything: any user data that will be used by funct.

	@enabledIcon string: the icon that will be shown on the tab when the tab is selected.

	@disabledIcon string: the icon that will be shown on the tab when the tab is not selected.

	@focusedIcon string: the icon that will be shown on the tab when the mouse is over that icon (highlighted).

	@pressedIcon string: the icon that will be shown on the tab when the mouse is pressed on that icon.

	"""

def BCTabWidgetSetTabIconFileName(tw, w, fileName):

	"""

	Sets the icon that will be displayed on the tab containing page widget w to be the one specified by fileName.
	
	This icon is shown on the left of the tab's title and it may be different for different tabs.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@w object: the page widget contained by the tab, in which the icon will be shown.

	@fileName string: the absolute path of a PNG file . If you pass an empty string here, the icon (if any) will not show any more.

	"""

def BCTabWidgetShowTabBar(tw, show):

	"""

	Shows or hides the tabBar of a BCTabWidget.
	NOTE: If the auto hide-tabBar feature is enabled and there is only one tab left, calling this function to show the tabBar has no effect.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@show boolean: set this to True to show the tabBar; False to hide it.

	"""

def BCTabWidgetSetTabEnabled(tw, w, enabled):

	"""

	Enables or disables the tab of BCTabWidget tw, containing the page widget w.
	Note that even a disabled tab may be visible. If the tab is visible already, BCTabWidget will not hide it; if all tabs are disabled, BCTabWidget will show one of them.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@w object: the page widget contained by the tab to be enabled/disabled.

	@enabled boolean: set True to enable or False to disable.

	"""

def BCTabWidgetIsTabEnabled(tw, w):

	"""

	Returns True if the tab containing page widget w is enabled or False otherwise.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@w object: the page widget contained by the tab to be checked.

	@returns: True if the tab tab is enabled or False otherwise.

	"""

def BCTabWidgetEnableMiddleClickCloseTab(tw, enable):

	"""

	Enables or disables closing tabs of BCTabWidget tw using mouse middle click.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@enable boolean: set True to enable or False to disable.

	"""

def BCTabWidgetIsEnabledMiddleClickCloseTab(tw):

	"""

	Returns 1 if closing tabs with mouse middle click is enabled or 0 otherwise.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@returns: 1 if closing tabs with mouse middle click is enabled or 0 otherwise.

	"""

def BCTabWidgetSetToolTip(tw, index, tip):

	"""

	Sets the tool tip (balloon help) for the tab at index position index to tip.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@index integer: the index of tab.

	@tip string: the text to be displayed at balloon help.

	"""

def BCTextBrowserCreate(p):

	"""

	Creates a BCTextBrowser, i.e. a BCTextEdit in read-only mode with hypertext navigation.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@returns: The created BCTextBrowser

	"""

def BCTextBrowserSource(tb):

	"""

	Returns the name of the displayed document of BCTextBrowser tb.
	This function is not supported under VR mode.
	


	@tb object: the BCTextBrowser.

	@returns: the BCTextBrowser's name of the displayed document.

	"""

def BCTextBrowserSetSource(tb, name):

	"""

	Sets the name of the displayed document of BCTextBrowser tb to name.
	This function is not supported under VR mode.
	


	@tb object: the TextBrowser.

	@name string: the name of the displayed document.

	"""

def BCTextBrowserBackward(tb):

	"""

	Changes the document displayed to the previous document in the list of documents built by navigating links.
	Does nothing if there is no previous document.
	This function is not supported under VR mode.
	


	@tb object: the TextBrowser.

	"""

def BCTextBrowserForward(tb):

	"""

	Changes the document displayed to the next document in the list of documents built by navigating links.
	Does nothing if there is no next document.
	This function is not supported under VR mode.
	


	@tb object: the TextBrowser.

	"""

def BCTextBrowserHome(tb):

	"""

	Changes the document displayed to be the first document the browser displayed.
	This function is not supported under VR mode.
	


	@tb object: the TextBrowser.

	"""

def BCTextBrowserReload(tb):

	"""

	Reloads the current set source.
	This function is not supported under VR mode.
	


	@tb object: the TextBrowser.

	"""

def BCTextBrowserGetText(tb):

	"""

	Returns the text of BCTextBrowser tb.
	This function is not supported under VR mode.
	


	@tb object: the TextBrowser.

	@returns: the text of the BCTextBrowser.

	"""

def BCTextBrowserGetParagraphText(tb, paragraph):

	"""

	Returns the text of paragraph with index paragraph for tb.
	This function is not supported under VR mode.
	


	@tb object: the BCTextBrowser.

	@paragraph integer: the index of the paragraph to be tested.

	@returns: The text of paragraph with index paragraph.

	"""

def BCTextBrowserGetSelectedText(tb):

	"""

	Returns the selected text within TextBrowser tb.
	This function is not supported under VR mode.
	


	@tb object: the BCTextBrowser.

	@returns: the selected text.

	"""

def BCTextBrowserSetLinkClickedFunction(tb, funct, data):

	"""

	Set a function that will be called when the user clicks an anchor in the BCTextBrowser tb.
	This function is not supported under VR mode.
	


	@tb object: the BCTextBrowser.

	@funct callback: the callback function that is called when the link is clicked.
	See BC_TEXTBROWSER_LINK_CLICKED_FUNCTION for details.
	integer BC_TEXTBROWSER_LINK_CLICKED_FUNCTION(tb, link, data)
	The function to be called when the user clicks a link.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	tb    object    the BCTextBrowser.
	link  string    the value of the href.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)anything that may be required in function funct.

	"""

def BCTextEditCreate(p, text):

	"""

	Creates a new BCTextEdit.
	BCTextEdits are used to display and/or edit multiple lines of text. If only one line of
	text is required, consider using BCLineEditCreate().
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@text string: the initial text that the BCTextEdit will display.

	@returns: The created BCTextEdit

	"""

def BCTextEditGetText(te):

	"""

	Returns the text of BCTextEdit te.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@returns: the text of the BCTextEdit.

	"""

def BCTextEditSetText(te, text):

	"""

	Sets the text of BCTextEdit te to be text.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@text string: the new text that will be displayed in BCTextEdit te.

	"""

def BCTextEditInsert(te, text):

	"""

	Inserts text at the current cursor position of BCTextEdit te.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@text string: the new text that will be inserted in BCTextEdit te.

	"""

def BCTextEditInsertAt(te, text, para, index):

	"""

	Inserts text in the paragraph para of BCTextEdit te at position index.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@text string: the new text that will be inserted in paragraph of BCTextEdit te.

	@para integer: the index of the paragraph which the text will be inserted.

	@index integer: the position in the paragraph which the text will be inserted.

	"""

def BCTextEditSetBold(te, val):

	"""

	If val is not zero, this function sets the current format to bold.
	When this function is called with val set to 1, any text appended to the text of te will be displayed in bold format.
	If it is called later with val set to 0, bold format is disabled, and any text appended is displayed normally.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@val boolean: True to set bold format, or False to unset bold format.

	"""

def BCTextEditSetItalic(te, val):

	"""

	If val is not zero, this function sets the current format to italic.
	When this function is called with val set to 1, any text appended to the text of te will be displayed in italic format. 
	If it is called later with val set to False, italic format is disabled, and any text appended is displayed normally.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@val boolean: True to set italic format, or False to unset italic format.

	"""

def BCTextEditSetUnderline(te, val):

	"""

	If val is not zero, this function sets the current format to underline.
	When this function is called with val set to True, any text appended to the text of te will be displayed in underline format.
	If it is called later with val set to False, underline format is disabled, and any text appended is displayed normally.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@val boolean: True to set underline format, or False to unset underline format.

	"""

def BCTextEditGetSelectedText(te):

	"""

	Returns the selected text within BCTextEdit te.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@returns: the selected text.

	"""

def BCTextEditSetReadOnly(te, readOnly):

	"""

	Sets the text of the BCTextEdit te as read-only or not according to readOnly.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@readOnly boolean: set it to False if you don't want the BCTextEdit to be Read-Only. Otherwise set it to True.

	"""

def BCTextEditIsReadOnly(te):

	"""

	informs about the readOnly state of the BCTextEdit te.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@returns: True if the BCTextEdit is readOnly, False otherwise.

	"""

def BCTextEditFind(te, expr, cs, wo, forward, para, index):

	"""

	Finds the next occurrence of the string, expr. Returns True if expr was found; otherwise returns False.
	If para and index are both 0 the search begins from the current cursor position. If para and index are both not 0, the search begins from the index character position in the para paragraph.
	Please note that this function will make the next occurrence of the string (if found) the current selection, and will thus modify the cursor position.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@expr string: the string to find in te.

	@cs boolean: if cs is True the search is case sensitive, otherwise it is case insensitive.

	@wo boolean: if wo is True the search looks for whole word matches only; otherwise it searches for any matching text.

	@forward boolean: if forward is True the search works forward from the starting position to the end of the text, otherwise it works backwards to the beginning of the text.

	@para int: (optional)the BCTextEdit's paragraph where the cursor will start the search from.

	@index int: (optional)the position in para where the cursor will be start the search from.

	@returns: The function returns a tupple with 3 items:
	ret[0] can be True or False whether the expression was found or not. 
	ret[1] is the number of the paragraph in which the first character of the match was found. 
	ret[2] is the index position of that character within the paragraph.
	
	WARNING: If expr is not found, the returned index and paragraph are undefined.

	"""

def BCTextEditSetCursorPosition(te, paragraph, index):

	"""

	Sets the cursor to position index in paragraph paragraph.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@paragraph integer: the BCTextEdit's paragraph where the cursor will be set.

	@index integer: the position in paragraph where the cursor will be set.

	"""

def BCTextEditSetCursorPositionChangedFunction(te, funct, data):

	"""

	Set a function that will be called when the cursor of the BCTextEdit te changes position. The te may also be a read-only BCTextEdit.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@funct callback: the callback function that is called when the cursor changes position.
	See BC_TEXTEDIT_CURSOR_POS_CHANGED_FUNCTION for details.
	integer BC_TEXTEDIT_CURSOR_POS_CHANGED_FUNCTION(te, para, pos, data)
	The function to be called when the position of the cursor changes.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	te    object    the BCTextEdit.
	para  integer   the current paragraph.
	pos   integer   the character position within the paragraph.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)anything that may be required in function funct.

	"""

def BCTextEditEnsureCursorVisible(te):

	"""

	Ensures that the cursor is visible by scrolling the text edit if necessary.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	"""

def BCTextEditClear(te):

	"""

	Deletes all the text in the BCTextEdit te.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	"""

def BCTextEditSetWordWrap(te, wordWrap):

	"""

	Sets the word wrap mode of the BCTextEdit te to wordWrap.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@wordWrap integer: the word wrap mode.
	See BCEnumWordWrap for details.
	
	guitk.constants BCEnumWordWrap
	This enum defines the BCTextEdit's word wrap modes
	 - guitk.constants.BCNoWrap
	Do not wrap the text. This is the default.
	 - guitk.constants.BCWidgetWidth
	Wrap the text at the current width of the widget. Wrapping is at whitespace by default; this can be changed with BCTextEditSetWrapPolicy().
	 - guitk.constants.BCFixedPixelWidth
	Wrap the text at a fixed number of pixels from the widget's left side. The number of pixels is set with BCTextEditSetWrapColumnOrWidth()
	 - guitk.constants.BCFixedColumnWidth
	Wrap the text at a fixed number of character columns from the widget's left side. The number of characters is set with BCTextEditSetWrapColumnOrWidth(). This is useful if you need formatted text that can also be displayed gracefully on devices with monospaced fonts, for example a standard VT100 terminal, where you might set wrapColumnOrWidth() to 80.

	"""

def BCTextEditSetWrapPolicy(te, wrapPolicy):

	"""

	Sets the word wrap policy of the BCTextEdit te to wrapPolicy (default BCWrapAtWordBoundaryOrAnywhere).
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@wrapPolicy integer: the word wrap policy.
	See BCEnumWrapPolicy for details.
	
	guitk.constants BCEnumWrapPolicy
	This enum defines where text can be wrapped in word wrap mode.
	 - guitk.constants.BCManualWrap
	Text is not wrapped at all.
	 - guitk.constants.BCWordWrap
	Text is wrapped at word boundaries.
	 - guitk.constants.BCWrapAnywhere
	Text can be wrapped at any point on a line, even if it occurs in the middle of a word.
	 - guitk.constants.BCWrapAtWordBoundaryOrAnywhere
	If possible, wrapping occurs at a word boundary; otherwise it will occur at the appropriate point on the line, even in the middle of a word.

	"""

def BCTextEditSetWrapColumnOrWidth(te, wrapPos):

	"""

	Sets the position (in pixels or columns depending on the BCEnumWordWrap mode) where text will be wrapped.
	This function is applicable when BCTextEditSetWordWrap() has been called with either BCFixedPixelWidth or
	BCFixedColumnWidth as wrap mode, setting the pixel or column position of wrap width respectively.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@wrapPos integer: The position in pixels or columns, where the text will be wrapped.

	"""

def BCTextEditScrollToBottom(te):

	"""

	Scrolls to the bottom of the document and does formatting if required.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	"""

def BCTextEditGetVisibleWidth(te):

	"""

	Returns the visible width of BCTextEdit te.
	Recall that BCTextEdit may obtain horizontal scrollbar, if applied text exceeds visible limits. 
	When scrollbar is hidden, visible width equals to the width of the BCTextEdit's BCScrollView.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit to be measured.

	@returns: the BCTextEdit's visible width.

	"""

def BCTextEditGetVisibleHeight(te):

	"""

	Returns the visible height of BCTextEdit te.
	Recall that BCTextEdit may obtain vertical scrollbar, if applied text exceeds visible limits. 
	When scrollbar is hidden, visible height equals to the height of the BCTextEdit's BCScrollView.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit to be measured.

	@returns: the BCTextEdit's visible height.

	"""

def BCTextEditGetContentsWidth(te):

	"""

	Returns the contents width of BCTextEdit te.
	This is the least width where horizontal scrollbar is not visible.
	Imagine you have a BCTextEdit with horizontal scrollbar visible.
	In order to find out how much your widget have to grow for the horizontal scrollbar to disappear, calculate contentsWidth-visibleWidth.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit to be measured.

	@returns: the horizontal total amount of content.

	"""

def BCTextEditGetContentsHeight(te):

	"""

	Returns the contents height of BCTextEdit te.
	This is the height in pixels where vertical scrollbar is not visible.
	Imagine you have a BCTextEdit with vertical scrollbar visible.
	In order to find out how much your widget have to grow for the vertical scrollbar to disappear, calculate contentsWidth-visibleWidth.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit to be measured.

	@returns: the vertical total amount of content.

	"""

def BCTextEditSetInfo(te, info):

	"""

	Function is obsolete. Use BCTextEditSetPlaceholderText() instead.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@info string: the text to be displayed.

	"""

def BCTextEditAppendParagraph(te, txt):

	"""

	Appends a new paragraph with text txt to the end of the BCTextEdit te.
	The difference with insertParagraph is that undo/redo history in BCTextEdit is cleared by this function, and no history is kept for appends, which makes them faster.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@txt string: the text to be appended.

	"""

def BCTextEditInsertParagraph(te, txt, paragraph):

	"""

	Inserts a new paragraph with text txt after the paragraph paragraph.
	The difference with appendParagraph is that undo/redo history in BCTextEdit is kept by
	this function, which makes it slower.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@txt string: the text to be inserted.

	@paragraph integer: the index of the paragraph after which the text will be inserted.

	"""

def BCTextEditRemoveParagraph(te, paragraph):

	"""

	Removes the paragraph paragraph.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@paragraph integer: the index of the paragraph to be removed.

	"""

def BCTextEditSetParagraphBackgroundColor(te, paragraph, r, g, b):

	"""

	Sets the RGB values for the background color of paragraph paragraph to be r, g and b.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@paragraph integer: the index of the paragraph to be affected.

	@r integer: the value for red (0 - 255).

	@g integer: the value for green (0 - 255).

	@b integer: the value for blue (0 - 255).

	"""

def BCTextEditClearParagraphBackgroundColor(te, paragraph):

	"""

	Sets the background color of paragraph paragraph to the default.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@paragraph integer: the index of the paragraph to be affected.

	"""

def BCTextEditGetParagraphs(te):

	"""

	Returns the number of paragraphs in the te.
	Recall that an empty textedit is always considered to have one paragraph, so 1 is returned in this case.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@returns: The number of paragraphs.

	"""

def BCTextEditGetLinesOfParagraph(te, paragraph):

	"""

	Returns the number of lines that paragraph paragraph has.
	The function returns -1 if there is no paragraph with index paragraph.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@paragraph integer: the index of the paragraph to be affected.

	@returns: The number of lines for paragraph.

	"""

def BCTextEditGetParagraphText(te, paragraph):

	"""

	Returns the text of paragraph with index paragraph for te.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@paragraph integer: the index of the paragraph to be tested.

	@returns: The text of paragraph with index paragraph.

	"""

def BCTextEditGetSelection(te):

	"""

	Provides information about the selected text inside BCTextEdit.
	If there is no selection, all ints are set to -1.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@returns: A tuple with 4 items:
	First item is the number of the paragraph in which the selection begins.
	Second item is the index at which the selection begins within the beginning paragraph.
	Third item is the number of the paragraph in which the selection ends.
	Fourth item is the index at which the selection ends within the ending paragraph.

	"""

def BCTextEditBlockUpdates(te, block):

	"""

	Restricts updates and repaints for BCTextEdit te.
	This function is normally used to disable updates for a short period of time, for instance to avoid screen flicker or long delays during setting a large text.
	NOTE: Does not block callback functions. To do so, use BCBlockCallBackFunctions()
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@block boolean: set this parameter to True to block updates, or False otherwise.

	"""

def BCTextEditAreUpdatesBlocked(te):

	"""

	Returns True if updates are blocked for te, or False otherwise.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit

	@returns: True if updates are blocked for te, or False otherwise.

	"""

def BCTextEditSetMonospaceFont(te, mono):

	"""

	This function forces the BCTextEdit te to display its text with the application's current monospace font.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit

	@mono boolean: set this parameter to True to force the BCTextEdit to display its text with the application's current monospace font.

	"""

def BCTextEditMonospaceFont(te):

	"""

	Informs whether the BCTextEdit te displays currently its text with monospace font.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit

	@returns: True if BCTextEdit te displays currently its text with monospace font or False otherwise.

	"""

def BCTimerCreate(p):

	"""

	Creates a Timer.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@returns: the newly created Timer.

	"""

def BCTimerStart(timer, ms, singleShot):

	"""

	Starts the timer and lets it run for ms milliseconds.
	This function is not supported under VR mode.
	


	@timer object: the timer.

	@ms integer: the timer interval that the timer is required to run.

	@singleShot boolean: set this parameter to True for the timer to be a single shot timer, or False otherwise. If singleShot is True, the timer will be activated only once; otherwise it will continue until it is stopped.

	@returns: the id of the timer.

	"""

def BCTimerIsActive(timer):

	"""

	Returns True if timer timer is active, or False otherwise.
	This function is not supported under VR mode.
	


	@timer object: the timer.

	@returns: True if timer is active, or False if it is not.

	"""

def BCTimerChangeInterval(timer, ms):

	"""

	Changes the time interval for the given timer.
	This function is not supported under VR mode.
	


	@timer object: the timer

	@ms integer: the new interval in milliseconds.

	"""

def BCTimerStop(timer):

	"""

	Stops timer timer.
	This function is not supported under VR mode.
	


	@timer object: the timer

	"""

def BCTimerSetTimeoutFunction(timer, funct, data):

	"""

	Sets the function that will be executed on timer timeout.
	This function is not supported under VR mode.
	


	@timer object: the timer.

	@funct callback: the function that will be executed on timer timeout. See BC_TIMER_TIMEOUT_FUNCTION for details.
	integer BC_TIMER_TIMEOUT_FUNCTION(timer, data)
	The function to be called on timer timeout.
	
	Arguments
	
	timer  object    the timer.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCTimerSingleShot(ms, funct, data):

	"""

	Fires a single shot timer for ms milliseconds and runs funct when it times out.
	It is very convenient to use this function because you do not need to bother with a Timer object.
	This function is heavily used when GUI objects are deleted inside a callback function.
	This function is not supported under VR mode.
	


	@ms integer: the interval for which the timer will run (in milliseconds). As a special case, a BCTimer with timeout 0 times out as soon as all the events in the window system's event queue have been processed.

	@funct callback: the function that will run on timer timeout. 
	See BC_TIMER_SINGLE_SHOT_FUNCTION for details.
	integer BC_TIMER_SINGLE_SHOT_FUNCTION(data)
	The function to be called on a given time interval.
	
	Arguments
	
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCToolBoxCreate(p):

	"""

	Creates a new BCToolBox with parent p.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@returns: the created BCToolBox.

	"""

def BCToolBoxAddItem(tb, w, label):

	"""

	Adds item w which is a widget to the end of BCToolBox tb and sets its
	label to label.
	This function is not supported under VR mode.
	


	@tb object: the BCToolBox.

	@w object: the widget that will be added to tb.

	@label string: the label of the added item.

	"""

def BCToolBoxInsertItem(tb, w, label, index):

	"""

	Inserts item w into BCToolBox tb at index index. It also sets its label to label.
	This function is not supported under VR mode.
	


	@tb object: the BCToolBox.

	@w object: the widget that will be inserted to tb.

	@label string: the label of the inserted item.

	@index integer: the index at which w will be inserted.if index is out of range then the widget will be inserted at the bottom of the BCToolbox tb.

	"""

def BCToolBoxRemoveItem(tb, w):

	"""

	Removes item w from BCToolBox tb.
	NOTE: The item w is not deleted. To delete it, use BCDestroyLater() after removing it.
	This function is not supported under VR mode.
	


	@tb object: the BCToolBox.

	@w object: the widget that will be removed from tb.

	"""

def BCToolBoxSetItemEnabled(tb, index, enabled):

	"""

	Sets whether the item at index index is enabled or not.
	This function is not supported under VR mode.
	


	@tb object: the BCToolBox.

	@index integer: the index of the item that will be set.

	@enabled boolean: set this parameter to True to enable the item, or False to disable it.

	"""

def BCToolBoxSetItemToolTip(tb, index, tip):

	"""

	Sets the tool tip of the item at index index to tip.
	This function is not supported under VR mode.
	


	@tb object: the BCToolBox.

	@index integer: the index of the item that will be set.

	@tip string: the text that will be displayed as the item's tool tip.

	"""

def BCToolBoxSetItemLabel(tb, item, label):

	"""

	Sets the title of toolBoxItem w of the BCToolBox tb to label.
	This function is not supported under VR mode.
	


	@tb object: the BCToolBox.

	@item object: the toolBoxItem whose title we want to set.

	@label string: the string that will be set as title to the toolBoxItem item.

	"""

def BCToolBoxCurrentItem(tb):

	"""

	Returns the current item of BCToolBox tb.
	This function is not supported under VR mode.
	


	@tb object: the BCToolBox.

	@returns: the current item of tb.

	"""

def BCToolBoxCurrentIndex(tb):

	"""

	Returns the index of the current item of BCToolBox tb.
	This function is not supported under VR mode.
	


	@tb object: the BCToolBox.

	@returns: the index of the current item.

	"""

def BCToolBoxSetCurrentItem(tb, w):

	"""

	Sets the current item of BCToolBox tb to be w.
	This function is not supported under VR mode.
	


	@tb object: the BCToolBox.

	@w object: the new current item.

	"""

def BCToolBoxItem(tb, index):

	"""

	Returns the item of BCToolBox tb at index.
	This function is not supported under VR mode.
	


	@tb object: the BCToolBox.

	@index integer: the index of the item that this function will return.

	@returns: the item at index index.

	"""

def BCToolBoxIndexOf(tb, w):

	"""

	Returns the index of item w of BCToolBox tb.
	This function is not supported under VR mode.
	


	@tb object: the BCToolBox.

	@w object: the item of which the index will be returned.

	@returns: the index of w.

	"""

def BCToolBoxCount(tb):

	"""

	Returns the number of items in BCToolBox tb.
	This function is not supported under VR mode.
	


	@tb object: the BCToolBox.

	@returns: the number of items.

	"""

def BCToolBoxSetCurrentIndex(tb, index):

	"""

	Sets the current item of BCToolBox tb to be the one with index index.
	This function is not supported under VR mode.
	


	@tb object: the BCToolBox.

	@index integer: the index of the new current item.

	"""

def BCToolBoxSetCurrentChangedFunction(tb, funct, data):

	"""

	Sets the function that will be called when the current item of BCToolBox tb
	is changed.
	This function is not supported under VR mode.
	


	@tb object: the BCToolBox.

	@funct callback: the function. See BC_TOOLBOX_CURRENT_CHANGED_FUNCTION for details.
	integer BC_TOOLBOX_CURRENT_CHANGED_FUNCTION(tb, index, data)
	The function to be called when the current item of BCToolBox tb is changed.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	tb     object    the BCToolBox.
	index  integer   the index of the item.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)a pointer to any user data required by funct.

	"""

def BCWidgetExpandCreate(p):

	"""

	Creates a container able to rapid expand the managed widget.
	Operates by pressing Shift+MiddleMouse and move mouse pointer to the desired expanding direction. 
	One widget can be managed at the time.
	NOTE: Create the managed widget with parent the WidgetExpand.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@returns: the created WidgetExpand.

	"""

def BCWidgetExpandSetWidget(wex, managedWidget):

	"""

	Connect widgetExpand wex and managedWidget to be managed.
	Managed widget should be something with scroll bars (i.e. list, text edit etc).
	NOTE: Create the managed widget with parent the WidgetExpand.
	This function is not supported under VR mode.
	


	@wex object: the WidgetExpand.

	@managedWidget object: the managed widget.

	"""

def BCWidgetExpandClear(wex):

	"""

	Disconnect widgetExpand wex from its managed widget.
	The managed widget will NOT be deleted. Its your responsibility to give the managed widget a 
	reasonable geometry or to put it back into a layout.
	This function is not supported under VR mode.
	


	@wex object: the WidgetExpand.

	"""

def BCWidgetStackCreate(p):

	"""

	Creates a new BCWidgetStack with parent p.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@returns: the created BCWidgetStack.

	"""

def BCWidgetStackAddWidget(ws, w, id):

	"""

	Adds a widget to the BCWidgetStack.
	This function is not supported under VR mode.
	


	@ws object: the BCWidgetStack where w will be added.

	@w object: the widget that will be added to the BCWidgetStack.

	@id integer: the id that will be assigned to w (-1 for auto indexing).

	"""

def BCWidgetStackRemoveWidget(ws, w):

	"""

	Removes a widget from the BCWidgetStack.
	This function is not supported under VR mode.
	


	@ws object: the BCWidgetStack.

	@w object: the widget that will be removed from the BCWidgetStack.

	"""

def BCWidgetStackWidget(ws, id):

	"""

	Returns the widget of id id.
	This function is not supported under VR mode.
	


	@ws object: the BCWidgetStack that contains the required widget.

	@id integer: the id of the required widget.

	@returns: the widget of id id or None if the BCWidgetStack does not manage a widget with id id.

	"""

def BCWidgetStackId(ws, w):

	"""

	Returns the id of widget w within BCWidgetStack ws.
	This function is not supported under VR mode.
	


	@ws object: the BCWidgetStack that contains widget w.

	@w object: the widget whose id is required.

	@returns: the id of the widget w or -1 if the BCWidgetStack does not manage widget w.

	"""

def BCWidgetStackVisibleWidget(ws):

	"""

	Returns the currently visible widget of BCWidgetStack ws.
	This function is not supported under VR mode.
	


	@ws object: the BCWidgetStack.

	@returns: the currently visible widget (the one at the top of the stack), or None if nothing is currently being shown.

	"""

def BCWidgetStackRaiseWidget(ws, w):

	"""

	Brings widget w to the top of BCWidgetStack ws.
	This function is not supported under VR mode.
	


	@ws object: the BCWidgetStack that contains widget w.

	@w object: the widget that will be raised.

	"""

def BCWidgetStackRaiseId(ws, id):

	"""

	Brings the widget with id to the top of BCWidgetStack ws.
	This function is not supported under VR mode.
	


	@ws object: the BCWidgetStack that will be checked.

	@id integer: the id of the widget that will be raised.

	"""

def BCWindowCreate(name, a):

	"""

	Creates an empty window.
	The Window created contains by default a vertical BoxLayout (get with BCLayout()), 
	so everything placed on this Window is stacked from top to bottom.


	@name string: the name of the new window. It primarily serves as the window's xml tag, under which gui data will be stored when window closes and loaded when window is shown. Take care that name is a unique string. You can use BCSetCaption to change the window's caption (title).

	@a integer: describes what will happen to the window when its filter returns 1 (i.e. on exit). See BCEnumExitAction for details.
	
	guitk.constants BCEnumExitAction
	This enum type defines what will happen to the window when its filter returns 1 (i.e. on
	exit). Exit action is used with BCWindowCreate for example.
	 - guitk.constants.BCOnExitHide
	hides the window.
	
	WARNING: var BCOnExitHide take no action when script ends.After script ends the window destroyed with var BCOnExitDestroy.
	var BCOnExitHide has action only if script not ends.
	
	WARNING: Take special care when you use this enumerator.
	You should destroy the window yourself in order to free the memory it holds.
	 - guitk.constants.BCOnExitDestroy
	destroys the window.

	@returns: The created widget.

	"""

def BCWindowIsDocked(wid):

	"""

	Use this function to check if docking BCWindow wid is docked.
	This function is not supported under VR mode.
	


	@wid object: the BCWindow to be checked.

	@returns: True in case wid is docked; False otherwise.

	"""

def BCWindowSetSaveSettings(w, save):

	"""

	Sets whether BCWindow settings are saved when win is closed or not depending on the value of save.
	This function is not supported under VR mode.
	


	@w object: the BCWindow.

	@save boolean: True to enable saving settings or False to disable.

	"""

def BCWindowAddSeparator(w):

	"""

	Adds a Separator on BCWindow w.
	This function is not supported under VR mode.
	


	@w object: the BCWindow.

	"""

def BCWindowAddSpacer(w, l):

	"""

	Adds a Spacer on BCWindow w.
	This function is not supported under VR mode.
	


	@w object: the BCWindow.

	@l object: a layout whose parent is the BCWindow w.

	"""

def BCWindowSetAcceptFunction(w, funct, data):

	"""

	Sets the Accept Function of BCWindow w.
	The Accept Function of a BCWindow is the function called when Enter key is pressed on the BCWidget. Use this if you don' want OK Button visible in the widget but you need a function to be called on Enter. Also, if there is an OK Button in a dialog box in this BCWindow, when pressing OK Button this function will be called.
	IMPORTANT: Do not delete the BCWindow inside this function. If you return 1 and BCOnExitDestroy has been set, it will be deleted automatically after funct has run.


	@w object: the BCWindow.

	@funct callback: the function that will be called on accept (enter key pressed). See BC_WINDOW_ACCEPT_FUNCTION for details.
	integer BC_WINDOW_ACCEPT_FUNCTION(w, data)
	The function to be called when Enter key is pressed on the BCWindow.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	w     object    the BCWindow.
	data  anything  anything that may be required in function.
	
	Return: 1 for normally closing your window or 0 if you want your window to remain open on Return Key.

	@data anything: (optional)anything that may be required in funct.

	"""

def BCWindowSetRejectFunction(w, funct, data):

	"""

	Sets the Reject Function of widget w.
	The Reject Function of a widget is the function called when Escape key is pressed on the BCWindow. Use this if you don't want Cancel Button visible in the BCWindow but you need a function to be called on Escape. Also if there is a cancel button in a dialog box in this window when pressing cancel button this function will be called.
	IMPORTANT:  Do not delete the BCWindow inside this function. If you return 1 and BCOnExitDestroy has been set, it will be deleted automatically after funct has run.


	@w object: the BCWindow.

	@funct callback: the function that will be called on reject (escape pressed). See BC_WINDOW_REJECT_FUNCTION for details.
	integer BC_WINDOW_REJECT_FUNCTION(w, data)
	The function to be called when Escape key is pressed on the BCWindow.
	This function operates when you press ESC (or QUITALL) and before your window is destroyed.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	w     object    the widget.
	data  anything  anything that may be required in function.
	
	Return: Return 1 for normally closing your window or 0 if you want your window to remain open on ESC. Before you return 0, be sure that the latter window behavior is necessary.

	@data anything: (optional)anything that may be required in funct.

	"""

def BCWindowSetSize(w, width, height):

	"""

	Sets the width and height of BCWindow w.
	This function is not supported under VR mode.
	


	@w object: the BCWindow.

	@width integer: the new width for BCWindow w.

	@height integer: the new height for BCWindow w.
	NOTE: If hide a children of BCWindow then before call BCWindowSetSize , you must call BCWindowUpdateGeometry

	"""

def BCWindowUpdateGeometry(w):

	"""

	Notifies the layout system that the BCWindow w has changed and may need to change geometry.
	This function is not supported under VR mode.
	


	@w object: the BCWindow.

	"""

def BCWindowSetMousePressFunction(w, funct, data):

	"""

	Sets the function that will be called when a mouse button is pressed on BCWindow widget w.
	This function is not supported under VR mode.
	


	@w object: the BCWindow widget.

	@funct callback: the function that will be called when a mouse button is pressed on the BCWindow widget. 
	See BC_WINDOW_MOUSE_PRESS_FUNCTION for details.
	integer BC_WINDOW_MOUSE_PRESS_FUNCTION(w, mb, data)
	The function to be called when a mouse button is pressed on the BCWindow w.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	w     object    the BCWindow.
	mb    integer   the mouse-button pressed. See BCEnumButtonState for details.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data that may be required in funct.

	"""

def BCWindowAccept(w):

	"""

	Calls the BCWindow's accept function.
	If no custom accept function has been set, a default one will be called.
	Normally this function is called when we press the 'OK' button to close the BCWindow.


	@w object: the BCWindow whose accept function will be called.

	"""

def BCWindowReject(w):

	"""

	Calls the BCWindow's reject function.
	If no custom reject function has been set, a default one will be called.
	Normally this function is called when we press the 'Cancel' button to close the BCWindow.


	@w object: the BCWindow whose reject function will be called.

	"""

def BCWindowSetCheckFunction(w, funct, data):

	"""

	Sets the checkFunction of BCWindow w.
	The checkFunction can be used to check the data entered by the user on a BCWindow. If a checkFunction returns None, the data are considered correct, and the BCWindow is accepted (i.e. the accept function is called). If it returns a string, this means that some wrong data have been entered and thus the window remains active and showing, while a text message is displayed containing the returned string.
	NOTE: The checkFunction is called on BCWindow accept, BCComboBox activated, BCRadioButton toggled and BCCheckBox state changes.
	This function is not supported under VR mode.
	


	@w object: the BCWindow whose the checkFunction will be set.

	@funct callback: the checkFunction. See BC_WINDOW_CHECK_FUNCTION for details.
	string BC_WINDOW_CHECK_FUNCTION(w, data)
	The function to be called when check of data entered is needed.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	w     object    the BCWindow.
	data  anything  anything that may be required in function.
	
	Return: If you return a text, a warning dialog window with this text as a short message will appear. If you return an empty string nothing happens.

	@data anything: (optional)any data required by funct.

	"""

def BCWindowSetOnCloseFunction(win, funct, data):

	"""

	Sets the function that will be called when the [x] close button of the typical BCWindow is pressed.
	
	WARNING: funct will be called ONLY when the [x] button is pressed and NOT if the window is destroyed by any other way!
	This function is not supported under VR mode.
	


	@win object: the BCWindow.

	@funct callback: the function that will be called. See BC_WINDOW_ON_CLOSE_FUNCTION for details
	integer BC_WINDOW_ON_CLOSE_FUNCTION(w, data)
	The function to be called when the [x] button of BCWindow w is pressed.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	w     object    the BCWindow.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)a pointer to any data required by funct.

	"""

def BCWindowSaveControlSettings(win):

	"""

	On demand save the settings for children of window win to xml file, if children widgets support this functionality.
	BCSetSaveSettings() must first be called with the desired children using unique names.
	On demand save for individual widget is not supported. If you want to auto save settings for individual widget
	use BCSetSaveSettings(). If window win does not accommodate widgets which save their settings, nothing happens.
	This function is not supported under VR mode.
	


	@win object: the BCWindow.

	"""

def BCWindowReadControlSettings(win):

	"""

	On demand read the settings for all children from xml file, if children widgets support this functionality.
	On demand read for individual widget is not supported. If you want to auto save settings for individual widget
	use BCSetSaveSettings(). If window win does not accommodate widgets which save their settings, nothing happens.
	This function is not supported under VR mode.
	


	@win object: the BCWindow.

	"""

def BCWindowSetOnPlaceChangedFunction(win, funct, data):

	"""

	Sets a callback function funct which will be called every time window win is docked or undocked.
	This function is not supported under VR mode.
	


	@win object: the BCWindow.

	@funct callback: the callback function. See BC_WINDOW_ON_PLACE_CHANGED_FUNCTION for details.
	integer BC_WINDOW_ON_PLACE_CHANGED_FUNCTION(w, p, data)
	The function to be called when the BCWindow w is docked or undocked.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	w     object    the BCWindow.
	p     integer   the new place of the BCWindow. Can be either BCInDock or BCOutsideDock.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCWindowSetPosition(win, x, y):

	"""

	Sets the position of BCWindow win.
	This function is not supported under VR mode.
	


	@win object: the BCWindow.

	@x integer: the x coordinate where wid will be displayed.

	@y integer: the y coordinate where wid will be displayed.

	"""

def BCWindowShowTitleBarButtons(w, buttons):

	"""

	Sets which titlebar buttons will be shown (close, minimize, maximize).
	This function is not supported under VR mode.
	


	@w object: the BCWindow

	@buttons integer: BCEnumTitleBarButton values. Multiple values can be ored together. See BCEnumTitleBarButton for details.
	
	guitk.constants BCEnumTitleBarButton
	This enum type is used to describe which buttons (close, minimize or maximize) will be active on a toolbar.
	 - guitk.constants.BCNothing
	No buttons will be active on the toolbar
	 - guitk.constants.BCCloseButton
	Close button will be active on the toolbar
	 - guitk.constants.BCMaximizeButton
	Maximize button will be active on the toolbar
	 - guitk.constants.BCMinimizeButton
	Minimize button will be active on the toolbar

	"""

def BCWindowIsMinimizedToTitleBar(win):

	"""

	Returns True if BCWindow win is minimized to title bar, otherwise False.
	This function is not supported under VR mode.
	


	@win object: the BCWindow that will be tested whether it is minimized to title bar or not.

	@returns: True if win is minimized to title bar or False if it is not.

	"""

def BCWindowAdjustSize(win):

	"""

	Adjusts the width and height of BCWindow win so that it takes up the minimum space while
	showing all of its contents.
	This function is not supported under VR mode.
	


	@win object: the BCWindow whose size will be adjusted.

	"""

def BCWindowSetInitSize(win, initWidth, initHeight):

	"""

	Set the init width and init height of BCWindow win, if there are not any declaration for wins size in xml.
	Should be called before BCShow of win. Window win takes this init size only at the first show.
	This function is not supported under VR mode.
	


	@win object: the BCWindow whose size will be adjusted.

	@initWidth integer: the init width for win.

	@initHeight integer: the init height for win.

	"""

def BCWindowSetInitGeometry(win, initX, initY, initWidth, initHeight):

	"""

	Set the init x, y, width and height of BCWindow win, if there are not any declaration for wins geometry in xml.
	Should be called before BCShow of win. Window win takes this init size only at the first show.
	This function is not supported under VR mode.
	


	@win object: the BCWindow whose size will be adjusted.

	@initX integer: the init x position for win.

	@initY integer: the init y position for win.

	@initWidth integer: the init width for win.

	@initHeight integer: the init height for win.

	"""

def BCWizardCreate(name, a):

	"""

	Creates an empty wizard dialog with name name, which is used for window title as well.
	All BCWindow functions can be used for Wizard as well, for example BCWindowSetAcceptFunction().
	This function is not supported under VR mode.
	


	@name string: the name of the new widget (also its caption).

	@a integer: describes what will happen to the window when its filter returns 1 (i.e. on exit). See BCEnumExitAction for details.
	
	guitk.constants BCEnumExitAction
	This enum type defines what will happen to the window when its filter returns 1 (i.e. on
	exit). Exit action is used with BCWindowCreate for example.
	 - guitk.constants.BCOnExitHide
	hides the window.
	
	WARNING: var BCOnExitHide take no action when script ends.After script ends the window destroyed with var BCOnExitDestroy.
	var BCOnExitHide has action only if script not ends.
	
	WARNING: Take special care when you use this enumerator.
	You should destroy the window yourself in order to free the memory it holds.
	 - guitk.constants.BCOnExitDestroy
	destroys the window.

	@returns: The created wizard.

	"""

def BCWizardAddPage(wiz, w, navigation, title, info):

	"""

	Adds widget w at wizard wiz as a new page with navigation text navigation, title and info text.
	
	Empty navigation text or title is not allowed.
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@w object: the widget to be added as a page.

	@navigation string: the text to be shown at the left side navigation list (usually compact size).

	@title string: (optional)the text to be shown bold on the top of the page (main instruction to explain user's objective with the page).

	@info string: (optional)the text to be used as additional help to the user (displayed below contents at the bottom and is prefixed with an info icon).

	@returns: the newly inserted page widget.

	"""

def BCWizardPageAt(wiz, index):

	"""

	Returns the widget that used as a page at index or 0 if index is out of range.
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@index integer: the page index. The valid range is from 0 to BCWizardPageCount()-1.

	@returns: the page widget at index.

	"""

def BCWizardAddUserButton(wiz, b):

	"""

	Add an extra button at the bottom left area of wizard (in the same line with Back Next buttons).
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@b object: can be a PushButton or a ToolButton.

	"""

def BCWizardSetCurrentPageChangedFunction(wiz, funct, data):

	"""

	Set the function to be called each time a page has changed.
	Wizard pages change by the user, by clicking Back or Next buttons. Previous pages can be accessed through the page title list.
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@funct callback: the function that will be called when a page has changed.
	See BC_WIZARD_CURRENT_PAGE_CHANGED_FUNCTION for details.
	integer BC_WIZARD_CURRENT_PAGE_CHANGED_FUNCTION(wiz, oldIndex, newIndex, data)
	The function to be called when wizard wiz page has changed.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	wiz       object    the wizard.
	oldIndex  integer   the index of previous page.
	newIndex  integer   the index of new page.
	data      anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)anything that may be required in funct.

	"""

def BCWizardSetNextButtonEnabled(wiz, enabled):

	"""

	Set whether Next button of wizard is enabled.
	By default Next button is enabled for all pages. If current page is the last, this function affects Finish button.
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@enabled boolean: set False to disable or True to enable.

	"""

def BCWizardIsNextButtonEnabled(wiz):

	"""

	Returns 1 if Next button of wizard is enabled (default), otherwise returns 0.
	If current page is the last, this function checks Finish button.
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	"""

def BCWizardCurrentIndex(wiz):

	"""

	Returns the index of the current page.
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@returns: the index of current page.

	"""

def BCWizardPageCount(wiz):

	"""

	Returns the number of pages in the wizard wiz.
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@returns: the number of pages.

	"""

def BCApplicationClipboardSetText(text):

	"""

	Sets the text to application's Clipboard.
	This function is not supported under VR mode.
	


	@text string: text to be set to application's Clipboard.

	"""

def BCApplicationClipboardGetText():

	"""

	Returns the application's Clipboard text or an empty string if there is no text
	This function is not supported under VR mode.
	


	@returns: the text of application's Clipboard.

	"""

def BCItemViewInfoBoxCreate(p, view):

	"""

	Creates a horizontal line with 3 labels able to provide useful information about item views (ListView ).
	The middle and right label updates automatically while the left most label can be used for customized information.
	InfoBox shows the total and the selected items of a view (multi selection).
	If the view is single selection mode, infoBox shows visible items. 
	When view is a tree, standard ItemViewInfoBox counts the total top level items, but this can be customized with BCItemViewInfoBoxSetTotalCounterMode(). 
	You can also provide custom texts to ItemViewInfoBox using BCItemViewInfoBoxBlockAutoUpdates() and BCItemViewInfoBoxSetText().
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@view object: the ListView for which the created ItemViewInfoBox will display info.

	@returns: the created ItemViewInfoBox.

	"""

def BCItemViewInfoBoxUpdate(infoBox):

	"""

	Updates the information displayed on the ItemViewInfoBox of ListView lv.
	You will need this function if you modify the views programmatically.
	This function is not supported under VR mode.
	


	@infoBox object: the ItemViewInfoBox

	"""

def BCItemViewInfoBoxBlockAutoUpdates(infoBox, index, block):

	"""

	Sets the section with index index of the ItemViewInfoBox associated with ListView lv to be updated automatically or manually.
	This function actually blocks/unblocks automatic updates. InfoBox has 3 sections given indices from 0 to 2 starting from the left most section. By default, the middle section provides information about "Total" items. The right most displays "Selected" items when BCMulti selection is applied to the managed ListView or "Visible" items when BCSingle selection is applied.
	WARNING: If you use this function with block 1 you will disable automatic update for the specific field. Thus you are responsible for the correct information that is displayed.
	This function is not supported under VR mode.
	


	@infoBox object: the ItemViewInfoBox

	@index integer: set 0 to manually update left most field, 1 for the middle one and 2 for the field on the right.

	@block boolean: set True for manual updates or False for auto updates.

	"""

def BCItemViewInfoBoxSetText(infoBox, index, text):

	"""

	Sets the text text to be displayed on the section with index index of the ItemViewInfoBox.
	Left most section can be modified directly with this function. Middle and right field can be set after you block auto updates using BCItemViewInfoBoxBlockAutoUpdates().
	This function is not supported under VR mode.
	


	@infoBox object: the ItemViewInfoBox

	@index integer: set 0 for the left most field, 1 for the middle one and 2 for the field on the right.

	@text string: the message to be displayed.

	"""

def BCItemViewInfoBoxSetTotalCounterMode(infoBox, mode):

	"""

	Sets whether the ItemViewInfoBox counts as total, all (children) or only the top level items.
	Standard ItemViewInfoBox counts top level items.
	This mode only makes sense for trees.
	This function is not supported under VR mode.
	


	@infoBox object: the ItemViewInfoBox.

	@mode integer: set 1 to count all items of tree ListViews or 0 for top-level items only.

	"""

def BCListViewSetColumnResizeEnabled(lv, col, enable):

	"""

	Enables or disables the resize property by the user of column col for the ListView lv.
	When header is hidden (and resize is enabled), columns can be resized with dragging inside viewport (between item cells).
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@enable boolean: True if the column should be allowed to be resized (the default), otherwise False.

	"""

def BCListViewHeaderSetToolTip(lv, col, tip):

	"""

	Set tooltip tip for the header section for column col of ListView lv.
	If you want to remove a tooltip just set an empty text.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@tip string: the tooltip.

	"""

def BCListViewSetViewportText(lv, text):

	"""

	Displays a text at viewport instead of painting items.
	Message is displayed centered and wrapped (breaks lines at appropriate points to fit whole text), but you can provide break line (\n) as well inside your message.
	Items will not be deleted. To clear the message use the function with empty text. 
	NOTE: All events on items continue to operate normally (click, select, etc)
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@text string: the text to be displayed centered.

	"""

def BCListViewSetUniformRowHeights(lv, uniform):

	"""

	This property defines whether all items in the ListView have the same height (default true).
	If property is true, the height is obtained from the first item in the view and is updated when the text data changes on that item.
	If property is false, each row has its own height related on its text data (for example item with text "a\nb" will be higher than item with text "ab")
	WARNING: ListView with non uniform row heights degrades performance.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@uniform boolean: if you set 0 each item height depends on its data, while 1 indicates that the uniform height is obtained from the first item in the view.

	"""

def BCTableSetCellsBackgroundColor(t, startRow, endRow, startColumn, endColumn, r, g, b):

	"""

	Changes the background color of given cells of BCTable t.
	Starting and ending row/column must be a number between zero and row/column count respectively. Also, the starting row/column must be
	a number less or equal to the ending one.
	If you want to reset the color to the default one, use the function BCTableResetCellsBackgroundColor().
	NOTE: This function sets the background color of the existing cells. Any new cells created by adding new rows/columns
	will be ignored. In case you want to keep the new color, see functions BCTableSetRowsCellsBackgroundColor() and BCTableSetColumnsCellsBackgroundColor().
	WARNING: This function sets the background color of given cells currently on the table. This means that, if previously
	BCTableSetRowsCellsBackgroundColor() or BCTableSetColumnsCellsBackgroundColor() has been called for those cells, on the next
	row/column addition, the background color of those cells will be set again to the color set by the latter functions!
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@startRow integer: the starting row

	@endRow integer: the ending row

	@startColumn integer: the starting column

	@endColumn integer: the ending column

	@r integer: the red component of the color to be set

	@g integer: the green component of the color to be set

	@b integer: the blue component of the color to be set

	"""

def BCTableResetCellsBackgroundColor(t, startRow, endRow, startColumn, endColumn):

	"""

	Resets the background color of given cells of BCTable t.
	If no color is set, this function does nothing.
	WARNING: This function resets the background color of given cells currently on the table. This means that, if previously
	BCTableSetRowsCellsBackgroundColor() or BCTableSetColumnsCellsBackgroundColor() has been called for those cells, on the next
	row/column addition, the background color of those cells will be set again to the color set by the latter functions!
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@startRow integer: the starting row

	@endRow integer: the ending row

	@startColumn integer: the starting column

	@endColumn integer: the ending column

	"""

def BCTableSetRowsCellsBackgroundColor(t, startRow, endRow, r, g, b):

	"""

	Sets the background color of cells, like BCTableSetCellsBackgroundColor(), but for whole rows.
	This function, in opposition to BCTableSetCellsBackgroundColor(), keeps track of the rows, so, any new cells
	added by adding new columns which belong to the range from startRow to endRow will also be colored
	with the given color.
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@startRow integer: the starting row

	@endRow integer: the ending row

	@r integer: the red component of the color to be set

	@g integer: the green component of the color to be set

	@b integer: the blue component of the color to be set

	"""

def BCTableSetColumnsCellsBackgroundColor(t, startColumn, endColumn, r, g, b):

	"""

	Sets the background color of cells, like BCTableSetCellsBackgroundColor(), but for whole columns.
	This functions does exactly what BCTableSetRowsCellsBackgroundColor() does but applies for columns.
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@startColumn integer: the starting column

	@endColumn integer: the ending column

	@r integer: the red component of the color to be set

	@g integer: the green component of the color to be set

	@b integer: the blue component of the color to be set

	"""

def BCTableResetRowsCellsBackgroundColor(t, startRow, endRow):

	"""

	Resets the background color of the cells of BCTable t found between rows from startRow to endRow.
	In opposition to BCTableResetCellsBackgroundColor(), this function resets the colors and forgets the color setting.
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@startRow integer: the starting row

	@endRow integer: the ending row

	"""

def BCTableResetColumnsCellsBackgroundColor(t, startColumn, endColumn):

	"""

	Resets the background color of the cells of BCTable t found between columns from startColumn to endColumn.
	This functions does exactly what BCTableResetRowsCellsBackgroundColor() does but applies for columns.
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@startColumn integer: the starting column

	@endColumn integer: the ending column

	"""

def BCWindowSetInitDockedPosition(w, neighbourName, dockPosition):

	"""

	Docked a BCWindow.
	This function overrides the window's position in xml file.
	If neighbourName is empty or invalid nothing happens.
	
	NOTE: For Script use must called with BCTimerSingleShot just before BCShow of BCWindow w.
	This function is not supported under VR mode.
	


	@w object: the BCWindow.

	@neighbourName string: the name of the dockarea("LeftDockArea" or "TopDockArea" or "RightDockArea" or "BottomDockArea") or the name of neighbour Window.

	@dockPosition integer: the positions where the BCWindow will be allowed to dock. See BCEnumDockType for details).
	
	guitk.constants BCEnumDockType
	This enum type defines the docking supported by a BCWindow. It can be used with BCWidgetDockCreate().
	 - guitk.constants.BCDockNone
	No docking.
	 - guitk.constants.BCDockLeft
	The widget is allowed to dock to the left hand side of the main window.
	 - guitk.constants.BCDockRight
	The widget is allowed to dock to the right hand side of the main window.
	 - guitk.constants.BCDockTop
	The widget is allowed to dock to the top of the main window.
	 - guitk.constants.BCDockBottom
	The widget is allowed to dock to the bottom of the main window.

	"""

def BCWindowSetInitTabbedPosition(w, neighbourName, tabPosition):

	"""

	Defines where the window w will be positioned (tabbed).
	This function overrides the window's position in xml file.
	If neighbourName is empty or invalid nothing happens.
	
	NOTE: For Script use must called with BCTimerSingleShot just before BCShow of BCWindow w.
	This function is not supported under VR mode.
	


	@w object: the BCWindow.

	@neighbourName string: the name of the neighbour Window.

	@tabPosition integer: the position where the BCWindow will be tabbed. Only BCLeftSide or BCRightSide are valid. See BCEnumHorizontalPosition for details).
	
	guitk.constants BCEnumHorizontalPosition
	This generic enum type defines a horizontal position.
	 - guitk.constants.BCLeftSide
	The left position.
	 - guitk.constants.BCRightSide
	The right position.
	 - guitk.constants.BCHorizontalCenter
	The middle position.

	"""

def BCListViewItemColumnSetForegroundColor(item, col, mode, r, g, b):

	"""

	Sets a custom foreground color to a ListViewItem for column col.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem whose background color will be changed.

	@col integer: the column index.

	@mode integer: BCNormalMode and BCSelectedMode is only supported. See BCEnumMode for details.
	
	guitk.constants BCEnumMode
	This enum type describes a Button's pixmap or a ListViewItem's mode.
	 - guitk.constants.BCNormalMode
	The user does not interact with the Button or the ListViewItem, but their functionality is available.
	 - guitk.constants.BCDisabledMode
	The user cannot interact with the Button.
	 - guitk.constants.BCActiveMode
	Button: The user mouse cursor is over button or button is pressed (only for ToolButtons).
	 - guitk.constants.BCSelectedMode
	Button: Display the pixmap when the item represented by the icon is selected.
	ListViewItem: The item is selected.

	@r integer: the value of RED of the RGB background color.

	@g integer: the value of GREEN of the RGB background color.

	@b integer: the value of BLUE of the RGB background color.

	"""

def BCListViewItemColumnResetForegroundColor(item, col, mode):

	"""

	Resets the foreground color of a ListViewItem for column col to the default one.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem whose background color will be reset. The new color will be in accordance with the colors of the parent ListView.

	@col integer: the column index.

	@mode integer: BCNormalMode and BCSelectedMode is only supported. See BCEnumMode for details.
	
	guitk.constants BCEnumMode
	This enum type describes a Button's pixmap or a ListViewItem's mode.
	 - guitk.constants.BCNormalMode
	The user does not interact with the Button or the ListViewItem, but their functionality is available.
	 - guitk.constants.BCDisabledMode
	The user cannot interact with the Button.
	 - guitk.constants.BCActiveMode
	Button: The user mouse cursor is over button or button is pressed (only for ToolButtons).
	 - guitk.constants.BCSelectedMode
	Button: Display the pixmap when the item represented by the icon is selected.
	ListViewItem: The item is selected.

	"""

def BCListViewItemColumnSetBackgroundColor(item, col, mode, r, g, b):

	"""

	Sets a custom background color to a ListViewItem for column col.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem whose background color will be changed.

	@col integer: the column index.

	@mode integer: BCNormalMode and BCSelectedMode is only supported. See BCEnumMode for details.
	
	guitk.constants BCEnumMode
	This enum type describes a Button's pixmap or a ListViewItem's mode.
	 - guitk.constants.BCNormalMode
	The user does not interact with the Button or the ListViewItem, but their functionality is available.
	 - guitk.constants.BCDisabledMode
	The user cannot interact with the Button.
	 - guitk.constants.BCActiveMode
	Button: The user mouse cursor is over button or button is pressed (only for ToolButtons).
	 - guitk.constants.BCSelectedMode
	Button: Display the pixmap when the item represented by the icon is selected.
	ListViewItem: The item is selected.

	@r integer: the value of RED of the RGB background color.

	@g integer: the value of GREEN of the RGB background color.

	@b integer: the value of BLUE of the RGB background color.

	"""

def BCListViewItemColumnResetBackgroundColor(item, col, mode):

	"""

	Resets the background color of a ListViewItem for column col to the default one.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem whose background color will be reset. The new color will be in accordance with the colors of the parent ListView.

	@col integer: the column index.

	@mode integer: BCNormalMode and BCSelectedMode is only supported. See BCEnumMode for details.
	
	guitk.constants BCEnumMode
	This enum type describes a Button's pixmap or a ListViewItem's mode.
	 - guitk.constants.BCNormalMode
	The user does not interact with the Button or the ListViewItem, but their functionality is available.
	 - guitk.constants.BCDisabledMode
	The user cannot interact with the Button.
	 - guitk.constants.BCActiveMode
	Button: The user mouse cursor is over button or button is pressed (only for ToolButtons).
	 - guitk.constants.BCSelectedMode
	Button: Display the pixmap when the item represented by the icon is selected.
	ListViewItem: The item is selected.

	"""

def BCListViewSetTextEllipsisPosition(lv, col, pos):

	"""

	Set where ellipsis (...) should be added for text that is too long to fit into an item for column col (default right).
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@pos integer: the position of '...' in the text. See BCEnumHorizontalPosition for details.
	
	guitk.constants BCEnumHorizontalPosition
	This generic enum type defines a horizontal position.
	 - guitk.constants.BCLeftSide
	The left position.
	 - guitk.constants.BCRightSide
	The right position.
	 - guitk.constants.BCHorizontalCenter
	The middle position.

	"""

def BCComboBoxSetItemIconFileName(cb, file, index):

	"""

	Sets the pixmap file file as icon into the item of BCComboBox cb found at index index.
	This function is not supported under VR mode.
	


	@cb object: the BCComboBox

	@file string: the pixmap file to be set to the item

	@index integer: the index of the item

	"""

def BCListViewTopLevelItemExists(lv, col, text):

	"""

	Searches for top level item that matches string text into column col.
	The search is case sensitive.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@text string: the string.

	@returns: True if text matches ; False otherwise.

	"""

def BCListViewIsSelected(lv, item):

	"""

	Returns True if item is selected, or False otherwise.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@item object: the ListViewItem that will be checked.

	@returns: True if item is selected; False otherwise

	"""

def BCListViewSetEnterPressedFunction(lv, funct, data):

	"""

	Sets the function that will be called when the 'Return' (Enter) key is pressed inside ListView.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called. See BC_LISTVIEW_ENTER_PRESSED_FUNCTION for details.
	integer BC_LISTVIEW_ENTER_PRESSED_FUNCTION(lv, item, data)
	The function to be called when the Enter (or Return) keyboard button is pressed on a ListView or a BCIconView.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView or the BCIconView.
	item  object    the current item.
	data  anything  anything that may be required in function.
	
	Return: 0 to block the event otherwise return 1.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewSetCurrentItemChangedFunction(lv, funct, data):

	"""

	Sets a function that will be called when the current item in ListView lv has changed.
	The current item indicates keyboard focus in list view. Only one item can be the current at a time. You can shift the current item (without to change selected) by pressing Ctrl and Up/Down arrows.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called when current item has changed. See BC_LISTVIEW_CURRENT_ITEM_CHANGED_FUNCTION for details.
	integer BC_LISTVIEW_CURRENT_ITEM_CHANGED_FUNCTION(lv, item, data)
	The function to be called when the current item in ListView lv has changed.
	The current item indicates keyboard focus in list view.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	item  object    the new current ListViewItem.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by function funct.

	"""

def BCListViewHeaderSetText(lv, col, text):

	"""

	Sets the text displayed on the header of lv at column col to be text.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@text string: the text that will be displayed.

	"""

def BCListViewHeaderGetText(lv, col):

	"""

	Returns the text of the header of ListView lv at column col.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@returns: the text of the header of lv at col.

	"""

def BCListViewItemSetAboutToRenameFunction(item, funct, data):

	"""

	Sets a function that will be called when renaming of a column of ListViewItem item starts.
	Use view oriented BCListViewSetAboutToRenameItemFunction() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@funct callback: the function that will be called. See BC_LISTVIEWITEM_ABOUT_TO_RENAME_FUNCTION for details.
	integer BC_LISTVIEWITEM_ABOUT_TO_RENAME_FUNCTION(item, col, data)
	The function to be called when renaming of a column of item starts.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	item  object    the ListViewItem.
	col   integer   the ListViewItem column.
	data  anything  anything that may be required in function.
	
	Return: 1 to cancel the rename action, or 0 to proceed.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewStartRename(lv, item, col):

	"""

	Starts renaming ListViewItem item at column col.
	If rename is not allowed (item rename type at col is BCRenameType_None) editing will not start.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@item object: the ListViewItem.

	@col integer: the column index.

	"""

def BCListViewSetHeaderMenuColumnVisibilityChangeEnabled(lv, enable):

	"""

	Shows a button on the right of the horizontal header that pops up a menu that enabled the user to show/hide columns.
	If you have column with empty header text (for example icon only), customize the display menu text with BCListViewHeaderSetStringRepresentation().
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@enable boolean: set to True to enable the header button with menu that show/hide columns, or False to hide it.

	"""

def BCListViewHeaderMenuBlockColumnVisibilityChange(lv, col, block):

	"""

	Sets whether column col can be show/hide through column menu.
	It is useful when you have, for example, a visible column and you want it to remain visible (the user cannot hide it through column menu).
	The column where its visibility cannot change, displayed as a disabled item in the column menu.
	The default ListView column menu enables all columns to be shown/hidden.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@block boolean: set True for col to block visibility change or False (default) to enable the user to show/hide it.

	"""

def BCListViewSetColumnVisibilityChangeMenu(lv, pm):

	"""

	Set a custom popup menu to replace the menu which allows the user to hide/show columns.
	The default popup menu enables show/hide ability for all columns of the ListView. If you wish to have some columns unable to be hidden use a custom menu. After you use this function it is your responsibility to show/hide the columns.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@pm object: (optional)the custom menu to replace the default one.

	"""

def BCListViewAcceptRename(lv):

	"""

	Confirm the renaming procedure of the editing item inside list lv.
	If no item is at rename procedure, nothing happens.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	"""

def BCListViewSetItemsSortedFunction(lv, funct, data):

	"""

	Sets the function to be called right after items sorted at ListView.
	Items can be sorted if you mouse click on the header of each column (and sorting property is enabled). Sorting can be ascending or descending.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: is a function that will be called when the user mouse click on the column header.
	See BC_LISTVIEW_ITEMS_SORTED_FUNCTION for details.
	integer BC_LISTVIEW_ITEMS_SORTED_FUNCTION(lv, col, ascending, data)
	The function to be called right after items sorted into the list (for example mouse click at a column header).
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv         object    the ListView.
	col        integer   the ListView column.
	ascending  integer   1 for ascending and 0 for descending order.
	data       anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewSetFilterAboutToApplyFunction(lv, funct, data):

	"""

	Set the function to be called just before filter condition is applied.
	Return 1 in your callback funct to stop the default filtering procedure otherwise return 0.
	If you return 1 you are responsible for which items to be visible or not. If you decide to block the default procedure you may need BCListViewAboutToFilterItem().
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function to be called when filter applied. See BC_LISTVIEW_FILTER_ABOUT_TO_APPLY_FUNCTION for details.
	integer BC_LISTVIEW_FILTER_ABOUT_TO_APPLY_FUNCTION(lv, data)
	The function to be called when filter is applied.
	Return 1 to block the default process otherwise return 0.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	data  anything  anything that may be required in function.
	
	Return: 1 to block the default process otherwise return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewSetColumnResizeMode(lv, mode):

	"""

	Define how the ListView's columns will behave when the width of the ListView change.
	Set if none (default), all or only the last column of the ListView automatically resize when the ListView width change.
	Horizontal scrollbar will be never shown if you set BCAllColumns or BCLastColumn.
	WARNING: This function should be applied after all necessary columns have been added on the ListView (otherwise the behaviour is undefined).
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@mode integer: the column resize mode. See BCEnumColumnResizeMode for details.
	
	guitk.constants BCEnumColumnResizeMode
	This enum type describes how the columns of a list view adjust to resize events on the width of the list.
	 - guitk.constants.BCNoColumn
	The columns are not resized when listview width change.
	Horizontal scrollbar will be shown when items content is too large to fit.
	 - guitk.constants.BCAllColumns
	Columns automatically and equally resize to fill the available viewport width.
	Columns width cannot be changed by the user or programmatically.
	Horizontal scrollbar will be never shown.
	 - guitk.constants.BCLastColumn
	Last column automatically resize to fill the available viewport width.
	Horizontal scrollbar will be never shown.

	"""

def BCListViewHeaderSetVisible(lv, visible):

	"""

	Sets whether the header will be visible (default) or not depending on the value of visible.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@visible boolean: set 0 for the header to be hidden, or 1 otherwise.

	"""

def BCListViewSetRenameItemMode(lv, mode):

	"""

	Define which user actions will initiate ListView's item editing.
	The modes are BCDelayedOnSelectedClicked (default) and BCDirectOnClicked.
	Mode BCDirectOnClicked can be used to rename non selectable items.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@mode integer: the rename mode. See BCEnumListRenameItemMode for details.
	
	guitk.constants BCEnumListRenameItemMode
	This property holds which actions will initiate ListViewItem rename.
	 - guitk.constants.BCDelayedOnSelectedClicked
	Rename starts delayed, when clicking on an already selected item.
	 - guitk.constants.BCDirectOnClicked
	Rename starts direct, when clicking on an item (no need to be selected).

	"""

def BCListViewItemSetProgressBar(item, col):

	"""

	Sets a progress bar to be displayed in the ListViewItem item cell specified by the given column col.
	
	You can also use generic item widget functions BCListViewItemWidgetSetVisible(), BCListViewItemWidgetSetEnabled() and BCListViewItemWidgetDestroy().
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	"""

def BCListViewItemProgressBarSetProgress(item, col, progress):

	"""

	Sets progress bar current value at item at column col to be progress.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@progress integer: the current value.

	"""

def BCListViewItemProgressBarProgress(item, col):

	"""

	Returns the current value of progress bar item at column col.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: The current value.

	"""

def BCListViewItemProgressBarSetPercentageVisible(item, col, visible):

	"""

	Sets whether the current progress value (text) is displayed as a percentage (default visible).
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@visible integer: set 0 to hide the percentage (text) or 1 to show it (default).

	"""

def BCListViewItemIsProgressBar(item, col):

	"""

	Returns True if the ListViewItem item cell displays a progress bar at given column col, or False otherwise.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem

	@col integer: the column index.

	@returns: True if the ListViewItem item at column col is a progress bar, or False otherwise.

	"""

def BCListViewItemCheckBoxSetCheckedNoCallBack(item, col, check):

	"""

	This is a convenience function. Sets the value of the checkBox at ListViewItem item at column col without the callback function of item to run (if any).
	Use BCBlockCallBackFunctions() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column.

	@check integer: the new value.

	"""

def BCMDIMainWindowShowMaximized(mdiWindow):

	"""

	Show the BCMDIMainWindow maximized.
	This function is not supported under VR mode.
	


	@mdiWindow object: (optional)Currently unused. It is recommended to not pass anything.

	"""

def BCMDIMainWindowShowMinimized(mdiWindow):

	"""

	Show the BCMDIMainWindow minimized.
	This function is not supported under VR mode.
	


	@mdiWindow object: (optional)Currently unused. It is recommended to not pass anything.

	"""

def BCMDIMainWindowShowRestored(mdiWindow):

	"""

	Show the BCMDIMainWindow normal.
	This function is not supported under VR mode.
	


	@mdiWindow object: (optional)Currently unused. It is recommended to not pass anything.

	"""

def BCWidgetStackCurrentId(ws):

	"""

	Returns id of the currently visible widget of BCWidgetStack ws.
	This function is not supported under VR mode.
	


	@ws object: the BCWidgetStack.

	@returns: the id of the currently visible widget (the one at the top of the stack).

	"""

def BCListViewHeaderSetAlternativeText(lv, col, text):

	"""

	Function is obsolete. Use BCListViewHeaderSetStringRepresentation() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@text string: the text to be displayed at respective header menu item that indicates column col.

	"""

def BCWizardRemovePage(wiz, index):

	"""

	Removes the widget at page index index from wizard (the removed page-widget will NOT deleted).
	NOTE: After this call, it is the caller's responsibility to put the removed widget back into a layout or to delete it.
	NOTE: Page indexing will change (the valid range is from 0 to BCWizardPageCount()-1).
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@index integer: the index of the page that will be removed. The valid range is from 0 to BCWizardPageCount()-1.

	@returns: 1 if page removed succesfully, otherwise 0.

	"""

def BCWizardInsertPage(wiz, index, w, navigation, title, info):

	"""

	Inserts the widget with navigation text t at the given page index index (position) into wizard.
	Designed for special cases. For almost all cases BCWizardAddPage() is needed.
	
	Empty navigation text or title is not allowed.
	If index if negative, equal or higher than the total number of pages the page is NOT inserted.
	NOTE: Page indexing will change (the valid range is from 0 to BCWizardPageCount()-1).
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@index integer: the index (position) to be inserted. The valid range is from 0 to BCWizardPageCount()-1.

	@w object: the widget to be added as a page.

	@navigation string: the text to be shown at the left side navigation list (usually compact size).

	@title string: (optional)the text to be shown bold on the top of the page (main instruction to explain user's objective with the page).

	@info string: (optional)the text to be used as additional help to the user (displayed below contents at the bottom and is prefixed with an info icon).

	@returns: the inserted page.

	"""

def BCListViewSetColumnDataTypes(lv, dataTypes):

	"""

	Define the data type for each column of your ListView (default BCString).
	These data are used by the filter to define the filtering method. If you have for example a column with checkBoxes you have to set this column to BCBool.
	This function is not supported under VR mode.
	


	@lv object: the ListView to set.

	@dataTypes object: a list of data types. See BCEnumDataType for details.

	"""

def BCItemViewInfoBoxSetView(infoBox, view):

	"""

	Set the view for which the information will be displayed.
	This function is not supported under VR mode.
	


	@infoBox object: the ItemViewInfoBox.

	@view object: the ListView for which the ItemViewInfoBox will display info.

	"""

def BCListViewHeaderMenuSetAboutToShowFunction(lv, funct, data):

	"""

	Customize the right mouse header menu of a ListView lv.
	You can add some menu items here with BCPopupMenuInsertItem().
	Standard menu provides some 'Copy items content' functionality that can be turn off with BCListViewHeaderMenuSetCopyEnabled().
	Standard ListView actions (copy and rename) are provided right after your actions (with a separator).
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called when right mouse button pressed on a header section. See BC_LISTVIEW_HEADER_MENU_ABOUTTOSHOW_FUNCTION for details.
	integer BC_LISTVIEW_HEADER_MENU_ABOUTTOSHOW_FUNCTION(lv, pm, col, data)
	The function to be called when mouse right button pressed to the header of ListView lv.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	pm    object    the provided pull down menu.
	col   integer   the ListView column. .
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewHeaderSetTextChangedFunction(lv, funct, data):

	"""

	Sets the function that will be called when the text changes in the ListView header for column col.
	Text at a header section can change programmatically with BCListViewHeaderSetText()
	or through the header right mouse menu editor that is activated with BCListViewHeaderMenuSetAboutToShowFunction().
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called after text has changed. See BC_LISTVIEW_HEADER_TEXT_CHANGED_FUNCTION for details.
	integer BC_LISTVIEW_HEADER_TEXT_CHANGED_FUNCTION(lv, col, oldText, newText, data)
	The function to be called after ListView header section text has changed.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv       object    the ListView.
	col      integer   the ListView column.
	oldText  string    the old text at ListView header section.
	newText  string    the new text at ListView header section.
	data     anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewHeaderMenuSetRenameColumnEnabled(lv, col, enable):

	"""

	Function is not supported. For more info, please contact Customer Service department.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@enable boolean: If enable is set to True, then the first item after the custom ones, of the returned Menu will be an item having text "Rename", with which it is possible to rename the section of the header clicked.

	"""

def BCListViewHeaderMenuSetCopyEnabled(lv, col, enable):

	"""

	Set whether header menu provides 'Copy items content' options.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@enable boolean: If disable is set to True, then the 'Copy column' and 'Copy selected in column' items, of the returned Menu will not be shown. Otherwise these items will be shown (the default).

	"""

def BCListViewHeaderSetColumnSideButton(lv, col, b):

	"""

	Set a custom tool button aligned at the right of the text at header section for column col.
	
	The list view gets ownership of the tool button. 
	If you want to clear the button use this function with b None.
	If you orient header column text vertically (BCListViewHeaderSetTextVerticalOrientationEnabled) the button is positioned above vertically oriented text.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@col integer: the column index.

	@b object: (optional)the custom tool button.

	"""

def BCLineEditPathLineEditText(lip):

	"""

	Convenient function that returns the current text of BCLineEditPath lip.
	Alternatively, in order to get the current text, you should do the following steps:
	- Get the BCComboBox from lip using BCLineEditPathGetCombo()
	- Get the BCLineEdit from BCComboBox using BCComboBoxGetLineEdit()
	- Get the text from BCLineEdit.
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath

	@returns: the current text

	"""

def BCListViewHeaderSetColorLine(lv, col, r, g, b):

	"""

	Draw a color line at header section for column with index col.
	The color line is drawn at section bottom below text.
	To clear the line just set an invalid color (for example -1, -1, -1).
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@r integer: the value for red (0 - 255).

	@g integer: the value for green (0 - 255).

	@b integer: the value for blue (0 - 255).

	"""

def BCListViewColumnSetUserData(lv, col, data):

	"""

	Assigns user data data to ListView column index col.
	These data can be retrieved anytime using BCListViewColumnGetUserData().
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@data anything: the user's data.

	"""

def BCListViewColumnGetUserData(lv, col):

	"""

	Retrieves user data from ListView column with index col.
	These data have been set by calling BCListViewColumnSetUserData().
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@returns: the user's data.

	"""

def BCLineEditSetState(le, state, force):

	"""

	Sets the state of BCLineEdit le to state.
	This state corresponds to setting a certain pair of foreground and background color for the BCLineEdit. This is useful when
	you want to draw the user's attention to that BCLineEdit. So, depending on state, BCLineEdit background and/or foreground color
	will be set accordingly.
	If the colors to be set are similar to the existing ones (either because of application settings or widget one),
	the colors will not be changed, unless force is set to 1. In this case, no matter what the existing color is,
	the colors set will be the default ones for that state.


	@le object: the BCLineEdit.

	@state integer: the state to be set. See BCEnumWidgetState for
	details.
	
	guitk.constants BCEnumWidgetState
	This enumeration indicates the state (i.e. the color or icon used) for a widget
	 - guitk.constants.BCWidgetStateNone
	No state. Indicates the standard widget display.
	 - guitk.constants.BCWidgetStateInformation
	Indicates an info nothing out of the ordinary.
	 - guitk.constants.BCWidgetStateWarning
	Indicates a state that can be dealt with.
	 - guitk.constants.BCWidgetStateError
	Indicates a critical problem.
	 - guitk.constants.BCWidgetStateReadOnly
	Indicates that the widget cannot be edited.

	@force boolean: set this to 1 in order to force using the default color for state state; 0 otherwise (i.e. check versus pre-existing color).

	"""

def BCWizardSetPageId(wiz, index, id):

	"""

	Set a unique integer number (identifier) for WizardPage with index.
	Ids are useful when you insert/remove pages dynamically since they do not change automatically like index does.
	NOTE: The valid index range is from 0 to BCWizardPageCount()-1.
	Id is unique for each wizard page. If you do not set the page id, this is equal with index.
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@index integer: the page index. The valid range is from 0 to BCWizardPageCount()-1.

	@id integer: any unique integer number.

	"""

def BCWizardPageId(wiz, index):

	"""

	Returns the unique integer number (identifier) for WizardPage with index.
	NOTE: The valid index range is from 0 to BCWizardPageCount()-1.
	Id is unique for each wizard page. If you do not set the page id, this is equal with index.
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@index integer: the page index. The valid range is from 0 to BCWizardPageCount()-1.

	@returns: the index of current page.

	"""

def BCWizardPageIdToIndex(wiz, id):

	"""

	Returns the index for WizardPage with identifier id.
	If id does not exist function returns -1.
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@id integer: any unique integer number.

	@returns: the index of id or -1 if id does not exist.

	"""

def BCListViewHeaderSetForegroundColor(lv, col, r, g, b):

	"""

	Sets a foreground (text) color at header section for column with index col.
	To reset the foreground to standard, just set an invalid color (for example -1, -1, -1).
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@r integer: the value for red (0 - 255).

	@g integer: the value for green (0 - 255).

	@b integer: the value for blue (0 - 255).

	"""

def BCListViewItemWidgetSetVisible(item, col, visible):

	"""

	Sets whether the cell widget at column col will be visible or not depending on the value of visible.
	Supported item widgets are
	- Button (BCListViewItemSetButton()),
	- Checkbox (BCListViewItemSetCheckBox()),
	- ComboBox (BCListViewItemSetComboBox()),
	- ProgressBar (BCListViewItemSetProgressBar()),
	- RadioButton (BCListViewItemSetRadioButton())
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@visible boolean: set this parameter to 1 for the widget to be visible, or 0 otherwise.

	"""

def BCListViewItemWidgetIsVisible(item, col):

	"""

	Returns whether the cell widget of item item at column col is visible or not.
	Supported item widgets are
	- Button (BCListViewItemSetButton()),
	- Checkbox (BCListViewItemSetCheckBox()),
	- ComboBox (BCListViewItemSetComboBox()),
	- ProgressBar (BCListViewItemSetProgressBar()),
	- RadioButton (BCListViewItemSetRadioButton())
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: True if the cell widget is visible, or False otherwise.

	"""

def BCListViewItemWidgetSetEnabled(item, col, enable):

	"""

	Sets whether the cell widget at column col will be enabled or not depending on the value of enable.
	A disabled item widget does not interact with user events. By default, all item widgets are enabled.
	Supported item widgets are
	- Button (BCListViewItemSetButton()),
	- Checkbox (BCListViewItemSetCheckBox()),
	- ComboBox (BCListViewItemSetComboBox()),
	- ProgressBar (BCListViewItemSetProgressBar()),
	- RadioButton (BCListViewItemSetRadioButton())
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@enable boolean: set 0 for the widget to be disabled, or 1 to enable (default).

	"""

def BCListViewItemWidgetIsEnabled(item, col):

	"""

	Returns whether the cell widget of item item at column col is enabled or not.
	Supported item widgets are
	- Button (BCListViewItemSetButton()),
	- Checkbox (BCListViewItemSetCheckBox()),
	- ComboBox (BCListViewItemSetComboBox()),
	- ProgressBar (BCListViewItemSetProgressBar()),
	- RadioButton (BCListViewItemSetRadioButton())
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: True if the cell widget is enabled, or False otherwise.

	"""

def BCListViewSetColumnSeparatorEnabled(lv, col, enable):

	"""

	Set whether a vertical line (separator) is drawn at the right of column col.
	Separator is drawn at the viewport, aligned right of column col. Function can be used to visually group columns.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@enable boolean: True to show the separator, False otherwise (default).

	"""

def BCWindowSetScrollViewEnabled(w, enableScrollView):

	"""

	Enable scrollbars in the BCWindow.
	This function is not supported under VR mode.
	


	@w object: the BCWindow.

	@enableScrollView boolean: set True to enable scrollview or False to disable scrollview.

	"""

def BCGridLayoutAddMultiCellWidget(grid, w, fromRow, toRow, fromCol, toCol, alignment):

	"""

	Adds the widget w to BCGridLayout grid, spanning multiple rows/columns.
	The cell will span from (fromRow, fromCol ) to (toRow, toCol ). Alignment is specified by alignment. Use BCAlignAuto as default, which fills the entire cell.


	@grid object: the BCGridLayout

	@w object: the widget that will be added.

	@fromRow integer: the start row number.

	@toRow integer: the end row number.

	@fromCol integer: the start column.

	@toCol integer: the end column.

	@alignment integer: the alignment. For valid values see BCEnumAlignment.
	
	guitk.constants BCEnumAlignment
	This enum type is used to describe alignment. It contains horizontal and vertical flags. Alignment is used with BCGridLayoutAddMultiCellWidget for example.
	NOTE: You can use at most one horizontal and one vertical flag at a time.
	 - guitk.constants.BCAlignAuto
	aligns according to the language. Left for most, right for Arabic and Hebrew.
	 - guitk.constants.BCAlignLeft
	aligns with the left edge.
	 - guitk.constants.BCAlignRight
	aligns with the right edge.
	 - guitk.constants.BCAlignHCenter
	centers horizontally in the available space.
	 - guitk.constants.BCAlignJustify
	justifies the text in the available space.
	 - guitk.constants.BCAlignTop
	aligns with the top.
	 - guitk.constants.BCAlignBottom
	aligns with the bottom.
	 - guitk.constants.BCAlignVCenter
	centers vertically in the available space.
	 - guitk.constants.BCAlignCenter
	centers in both dimensions (vertically and horizontally).
	 - guitk.constants.BCAlignHorizontal_Mask
	horizontal mask.
	 - guitk.constants.BCAlignVertical_Mask
	vertical mask.
	 - guitk.constants.BCAlignVJustify
	Justifies the text vertically in the available space.

	"""

def BCListViewItemSetInactive(item, inactive):

	"""

	Sets whether a ListViewItem is inactive or active (default).
	Inactive item is only drawn as disabled but can handle all user events.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@inactive boolean: 1 to display inactive; 0 otherwise.

	"""

def BCListViewItemInactive(item):

	"""

	Returns 1 if ListViewItem item is inactive or 0 otherwise.
	The default ListViewItem is active.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@returns: 1 if item is inactive, 0 otherwise.

	"""

def BCListViewItemComboBoxIndexOf(item, col, text):

	"""

	Returns the index of the first occurence of /a text inside ListViewItemComboBox, otherwise -1.
	The search is case insensitive.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@text string: the string to search.

	@returns: the index of the first item with string /a text; -1 otherwise.

	"""

def BCSplitterSetStretchFactor(sp, index, stretch):

	"""

	Sets the size policy of the widget at position index to have a stretch factor of stretch.
	Initializes the relative size of the widget at position index with regard to their sibling widgets.
	Setting stretch 0 will initialize the widget at position index to occupy minimum fixed size.
	NOTE: The stretch factor cannot change dynamically, except from 0 to positive and vice-versa (with weird results). To change the widget sizes dynamically use BCSplitterSetWidgetSizes.
	This function is not supported under VR mode.
	


	@sp object: the BCSplitter.

	@index integer: the index of the item for which the stretch factor will be set.

	@stretch integer: the new stretch factor.

	"""

def BCTextEditSetTextChangedFunction(te, funct, data):

	"""

	Set a function that will be called when the text of the BCTextEdit te changes. The te may also be a read-only BCTextEdit.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@funct callback: the callback function that is called when the cursor changes position.
	See BC_TEXTEDIT_TEXT_CHANGED_FUNCTION for details.
	integer BC_TEXTEDIT_TEXT_CHANGED_FUNCTION(te, data)
	The function to be called when the text changes.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	te    object    the BCTextEdit.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)anything that may be required in function funct.

	"""

def BCTextEditSetParagraphForegroundColor(te, paragraph, r, g, b):

	"""

	Sets the RGB values for the foreground color of paragraph paragraph to be r, g and b.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@paragraph integer: the index of the paragraph to be affected.

	@r integer: the value for red (0 - 255).

	@g integer: the value for green (0 - 255).

	@b integer: the value for blue (0 - 255).

	"""

def BCTextEditClearParagraphForegroundColor(te, paragraph):

	"""

	Sets the foreground color of paragraph paragraph to the default.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@paragraph integer: the index of the paragraph to be affected.

	"""

def BCTextEditSetClearOptionVisible(te, visible):

	"""

	Control the availability of the 'Clear' option on BCTextEdit's right mouse click menu.
	If visible is set to True, the 'Clear' option will appear after the 'Select all' option. It will be disabled if the BCTextEdit te has no text.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@visible boolean: set this parameter to True to make the 'Clear' option visible on right mouse click menu, or False otherwise.

	"""

def BCTextEditClearOptionVisible(te):

	"""

	Informs whether the 'Clear' option will be visible on a BCTextEdit right mouse click menu.
	This function will return True even if the option is currently disabled.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit

	@returns: True if the 'Clear' option is visible on te's right mouse click menu, or False otherwise.

	"""

def BCPopupMenuClose(pm):

	"""

	Closes this BCMenu. Returns true if the BCMenu pm was closed; otherwise returns false.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@returns: true if the BCMenu pm was closed; otherwise returns false.

	"""

def BCComboBoxInsertSeparator(box, index):

	"""

	Insert a separator at position index.
	Separator will be appended if index is negative or greater than the number of items in the combo box.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@index integer: the index at which separator will be inserted (-1 to append).

	"""

def BCComboBoxIsSeparator(box, index):

	"""

	Returns whether combo box item at position index is a separator or not.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@index integer: the index.

	@returns: 1 if item at position index is separator or 0 otherwise.

	"""

def BCLabelSetLinkActivatedFunction(lb, funct, data):

	"""

	Sets the function that will be called when a link is clicked inside lb.
	This function is not supported under VR mode.
	


	@lb object: the BCLabel.

	@funct callback: the function that will be called when enter is pressed. See BC_LABEL_LINK_ACTIVATED_FUNCTION for details.
	integer BC_LABEL_LINK_ACTIVATED_FUNCTION(lb, link, data)
	The function to be called when the link link is clicked inside BCLabel lb.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lb    object    the BCLabel.
	link  string    the link that has been activated.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any user data required by funct.

	"""

def BCListViewItemCheckableSetDrawAsRadioButton(item, drawAsRadioButton):

	"""

	Sets the checkable ListViewItem to display radio button instead of check box indicator, depending on the value of radio.
	If item is not checkable nothing happens. You are responsible to operate the mutual exclusive property in the group of items.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@drawAsRadioButton boolean: 1 sets item to be displayed as radio button, 0 otherwise (default)

	"""

def BCListViewSetItemSpacing(lv, pixels):

	"""

	Defines the item density in pixels (default 2).
	Spacing between items is calculated with respect to font size and style parameters but this function provides some extra space. 
	Use even integers to ensure same pixels above and below item contents. Negative pixels number is not allowed.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@pixels integer: the extra empty space between items in pixels (default 2).

	"""

def BCListViewItemSetExpandMode(item, mode):

	"""

	Sets when the tree branch control ([+] and [-] in some styles) for item is visible and expand/collapse action is enabled.
	The standard item displays expand/collapse controls and enables action when contains at least one child (BCDontShowIndicatorWhenChildless).
	You can force show controls even when contains no children or force hide controls when children.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@mode integer: See BCEnumItemExpandMode for more details.
	
	guitk.constants BCEnumItemExpandMode
	This mode decides how the ListViewItem tree branch expand/collapse indicator is shown.
	 - guitk.constants.BCShowIndicator
	The controls for expanding and collapsing will be shown for this item even if there are no children.
	 - guitk.constants.BCDontShowIndicator
	The controls for expanding and collapsing will never be shown even if there are children. If the node is forced open the user will not be able to expand or collapse the item.
	 - guitk.constants.BCDontShowIndicatorWhenChildless
	The controls for expanding and collapsing will be shown if the item contains children.

	"""

def BCListViewItemExpandMode(item):

	"""

	Returns the item children expand mode (default BCDontShowIndicatorWhenChildless).
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	"""

def BCListViewSaveSortStateAndDisableSorting(lv):

	"""

	Saves the current sort state (column and order) of ListView lv and then disables sorting.
	When adding items or modifying their data (text, icons etc) in a ListView where sorting applied, the performance is low.
	It is recommended that you disable sorting first, then make mass data modifications and restore sorting again.
	NOTE: do not forget to BCListViewRestoreSortState() when mass modification finished.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	"""

def BCListViewRestoreSortState(lv):

	"""

	Restores the last saved sort state (column and order) of the ListView lv.
	If last saved sort state is not found, function does nothing.
	When adding items or modifying their data (text, icons etc) in a ListView where sorting applied, the performance is low.
	It is recommended that you disable sorting first, then make mass data modifications and restore sorting again.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	"""

def BCMenuBarCreate(p):

	"""

	Creates a BCMenuBar in parent p.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.
	NOTE: BCMenuBars are meant to be created with BCWindow parents.

	@returns: the created BCMenuBar

	"""

def BCMenuBarAddMenuItem(mb, text, menu):

	"""

	Adds menu menu in BCMenuBar mb under text.
	This function is not supported under VR mode.
	


	@mb object: the BCMenuBar where the BCMenu will be added.

	@text string: the name of the item that will hold BCMenu menu.

	@menu object: the BCMenu that will be added

	@returns: the id of the item that holds BCMenu menu.

	"""

def BCWizardSetPageInfo(wiz, index, info, state):

	"""

	Sets the text and the icon with a type (for example warning, error etc) for page index.
	Page info displayed below contents (at the bottom) with an icon (default information).
	To hide both text and icon use BCWizardClearPageInfo().
	Valid icon states are 
	- BCWidgetStateNone no icon,
	- BCWidgetStateInformation an icon indicating that the message is nothing out of the ordinary (default) or maybe a small tip,
	- BCWidgetStateWarning an icon indicating that the message is a warning, but can be dealt with,
	- BCWidgetStateError an icon indicating that the message represents a critical problem
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@index integer: the page index. The valid range is from 0 to BCWizardPageCount()-1.

	@info string: (optional)the text at the bottom of the page to be displayed.

	@state integer: (optional)the icon next to text at the bottom of the page to be displayed as info. See BCEnumWidgetState for details.
	
	guitk.constants BCEnumWidgetState
	This enumeration indicates the state (i.e. the color or icon used) for a widget
	 - guitk.constants.BCWidgetStateNone
	No state. Indicates the standard widget display.
	 - guitk.constants.BCWidgetStateInformation
	Indicates an info nothing out of the ordinary.
	 - guitk.constants.BCWidgetStateWarning
	Indicates a state that can be dealt with.
	 - guitk.constants.BCWidgetStateError
	Indicates a critical problem.
	 - guitk.constants.BCWidgetStateReadOnly
	Indicates that the widget cannot be edited.

	"""

def BCWizardClearPageInfo(wiz, index):

	"""

	Hides the information text and icon for page index.
	Page info displayed below contents (at the bottom) with an icon (default information).
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@index integer: the page index. The valid range is from 0 to BCWizardPageCount()-1.

	"""

def BCListViewSetItemsExpanded(lv, expand):

	"""

	Expands or collapses all ListViewItems, depending on the value of expand.
	Optimizes performance and eliminates flicker compared with expanding items one by one.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@expand boolean: set 1 to expand or 0 to collapse items.

	"""

def BCListViewItemSetInfo(item, col, text):

	"""

	Function is obsolete. Use BCListViewItemSetPlaceholderText() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem

	@col integer: the column index.

	@text string: the message to be displayed.

	"""

def BCResetForegroundColor(w):

	"""

	Resets the foreground color of widget w to the values defined by the current style.
	This function is not supported under VR mode.
	


	@w object: the widget whose foreground color will be reset.

	"""

def BCListViewHeaderSetTextVerticalOrientationEnabled(lv, col, enable):

	"""

	Set whether list header at column col draws text in vertical orientation (default horizontal).
	
	Text is drawn vertically from bottom to top (rotated by -90). Icon is positioned below text without to be rotated. 
	Vertical header has a maximum height 3 times bigger than the regular horizontal orienation header.
	If text does not fit the maximum height, it is drawn truncated (...) and a tooltip for whole text is 
	provided (if no user tooltip).
	Header text vertical orientation turns ListViews really compact when header text is long and items content is short, 
	for example checkboxes, icons only or short text
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@col integer: the column index.

	@enable boolean: set 1 to draw text vertical or 0 otherwise (default).

	"""

def BCPopupMessageCreate(p, a):

	"""

	Creates a box container enabled to provides short piece of text together with a widget. 
	The message is not shown until you call BCPopupMessageShowText() or BCPopupMessageShowTextTimeout().
	Message is displayed at the bottom of parent widget and can be aligned left or right.
	Message is provided with a close button but you can also hide it with BCPopupMessageSetClosable().
	You can define the close behavior (hide or destroy) when Message cleared with [x] or timed-out.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@a integer: (optional)describes what will happen to the widget when closed (cleared with [x]). See BCEnumExitAction for details.
	
	guitk.constants BCEnumExitAction
	This enum type defines what will happen to the window when its filter returns 1 (i.e. on
	exit). Exit action is used with BCWindowCreate for example.
	 - guitk.constants.BCOnExitHide
	hides the window.
	
	WARNING: var BCOnExitHide take no action when script ends.After script ends the window destroyed with var BCOnExitDestroy.
	var BCOnExitHide has action only if script not ends.
	
	WARNING: Take special care when you use this enumerator.
	You should destroy the window yourself in order to free the memory it holds.
	 - guitk.constants.BCOnExitDestroy
	destroys the window.

	@returns: The created message container.

	"""

def BCPopupMessageShowText(popupMsg, text):

	"""

	Animates the PopupMessage and text text is displayed.
	If you pass an empty text, PopupMessage will be cleared.
	This function is not supported under VR mode.
	


	@popupMsg object: the popup message.

	@text string: the short piece of text to be displayed.

	"""

def BCPopupMessageShowTextTimeout(popupMsg, text, ms):

	"""

	Animates the PopupMessage and text text is displayed for ms milli seconds and then message is cleared.
	If you pass an empty text, PopupMessage will be cleared.
	This function is not supported under VR mode.
	


	@popupMsg object: the popup message.

	@text string: the short piece of text to be displayed.

	@ms integer: the number of milliseconds after which the message will be cleared.

	"""

def BCPopupMessageClear(popupMsg):

	"""

	Clears (hides) the PopupMessage.
	Standard PopupMessage is provided with a close button.
	This function is not supported under VR mode.
	


	@popupMsg object: the popup message.

	"""

def BCPopupMessageSetWidget(popupMsg, w):

	"""

	Sets the given widget w to be displayed at the right of the text.
	PopupMessage takes ownership of the widget. If you set a None widget, any previous 
	widget will be deleted. If you set another widget the previous will be deleted (replace).
	NOTE: Theoretically, any widget can be inserted into the PopupMessage. In practise, this only makes sense with certain widgets (buttons, checkboxes etc)
	This function is not supported under VR mode.
	


	@popupMsg object: the popup message.

	@w object: (optional)the widget.

	"""

def BCPopupMessageSetAlignment(popupMsg, align):

	"""

	Aligns PopupMessage bottom left (default) or right.
	Message is located at the bottom of its parent geometry.
	This function is not supported under VR mode.
	


	@popupMsg object: the popup message.

	@align integer: BCAlignLeft or BCAlignRight is only enabled.

	"""

def BCPopupMessageSetClosable(popupMsg, closable):

	"""

	Sets whether the close action (button [x]) is enabled to the user (default is enabled).
	This function is not supported under VR mode.
	


	@popupMsg object: the popup message.

	@closable boolean: set 0 to hide the button or 1 to show it (default).

	"""

def BCWidgetExpandGetWidget(wex):

	"""

	Get the widget managed by wex.
	This function is not supported under VR mode.
	


	@wex object: the WidgetExpand.

	@returns: the widget managed by wex.

	"""

def BCListViewHasSelected(lv):

	"""

	Returns False if ListView lv has no item selected, or True otherwise.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: False if ListView has no item selected; True otherwise.

	"""

def BCComboBoxSetCurrentItemExecuteActivatedCallBack(box, index):

	"""

	Sets the current item of the BCComboBox to be the item with index index plus calls the activated function, if any.
	NOTE: This function is meant to be used by non-editable BCComboBoxes.


	@box object: the BCComboBox.

	@index integer: the index of the item to which current will be set.

	"""

def BCListViewItemComboBoxSetCurrentItemExecuteActivatedCallBack(item, col, index):

	"""

	Sets the current item of the comboBox found at column col of ListViewItem item to be the item with index index plus executes the activated function (if any).
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column where comboBox is found.

	@index integer: the index of the item to which current will be set.

	"""

def BCRepaint(w):

	"""

	Repaints the widget immediately.
	In all cases widgets get paint correct when you set a value to them. 
	This function is useful in the case you un-block widget updates with BCSetUpdatesEnabled().
	Is also useful when you want to force a widget paint (for example a Label text change) inside a loop.
	This function is not supported under VR mode.
	


	@w object: the widget to be repainted.

	"""

def BCBlockCallBackFunctions(w, block):

	"""

	Stops executing all user call back functions of widget w.
	NOTE: BCListViewItemSetAboutToDestroyFunction() cannot be blocked.
	The supported widgets are:
	ListView (also applied at ListViewItem, ListViewItemWidget and ListViewFilter)
	IconView
	CheckBox
	ComboBox
	DateEdit
	LineEdit
	SpinBox
	DoubleSpinBox
	PushButton
	ToolButton
	ButtonGroup
	TextEdit


	@w object: the widget to block its user call backs functions.

	@block boolean: True to block all call back functions of Widget or False to un-block (default).

	"""

def BCCallBackFunctionsBlocked(w):

	"""

	Returns True if callback functions of Widget w are blocked, False otherwise (default).
	The supported widgets are:
	ListView (also applied at ListViewItem, ListViewItemWidget and ListViewFilter)
	IconView
	CheckBox
	ComboBox
	DateEdit
	LineEdit
	SpinBox
	DoubleSpinBox
	PushButton
	ToolButton
	ButtonGroup
	TextEdit
	This function is not supported under VR mode.
	


	@w object: the widget whose functions checked whether are blocked.

	@returns: True if call back functions are blocked, False otherwise.

	"""

def BCLineEditPathSetTextChangeFunction(lip, funct, data):

	"""

	Convenient function that sets function funct to be called when the current text of BCLineEditPath lip is changed.
	Alternatively, in order to set a text-changed function, you should do the following steps:
	- Get the BCComboBox from lip using BCLineEditPathGetCombo()
	- Get the BCLineEdit from BCComboBox using BCComboBoxGetLineEdit()
	- Set the callback function using BCLineEdit's function BCLineEditSetTextChangeFunction()
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath

	@funct callback: the function to be called. See BC_LINEEDIT_TEXT_CHANGED_FUNCTION for details.
	integer BC_LINEEDIT_TEXT_CHANGED_FUNCTION(le, text, data)
	The function to be called when the text changes in the BCLineEdit.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	le    object    the BCLineEdit.
	text  string    the current text in the BCLineEdit.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any user data required by function funct

	"""

def BCLineEditPathSetFilter(lip, filter):

	"""

	Set the filters on the popup FileDialog
	  *
	  *
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath
	 *

	@filter string: the file filters that will be used in file dialog.
	 * WARNING: Use only the following format: "label1 (*.extension1 *.extension2 ...);;label2 (*.extension1 *.extension2 ...);;...".
	 * e.g. "Script files (*.bs *.c);;Python files (*.py);;All files (*)
	 *

	"""

def BCLineEditPathClearFilter(lip):

	"""

	Clears the filter (if any) of the filedialog of BCLineEditPath lip
	The filter of the filedialog reverts back to its default, this is "All files (*)"
	This function is not supported under VR mode.
	


	@lip object: the BCLineEditPath

	"""

def BCDateEditCreate(p):

	"""

	Creates a BCDateEdit. This is a field which accepts only dates.
	On the right side of the widget there is an arrow which pops up a calendar for selecting the date.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@returns: the created BCDateEdit.

	"""

def BCDateEditGetDay(dtEdit):

	"""

	Returns the content's day of BCDateEdit dtEdit
	This function is not supported under VR mode.
	


	@dtEdit object: the BCDateEdit.

	@returns: the content's day of BCDateEdit dtEdit

	"""

def BCDateEditGetMonth(dtEdit):

	"""

	Returns the content's month of BCDateEdit dtEdit
	This function is not supported under VR mode.
	


	@dtEdit object: the BCDateEdit.

	@returns: the content's month of BCDateEdit dtEdit

	"""

def BCDateEditGetYear(dtEdit):

	"""

	Returns the content's year of BCDateEdit dtEdit
	This function is not supported under VR mode.
	


	@dtEdit object: the BCDateEdit.

	@returns: the content's year of BCDateEdit dtEdit

	"""

def BCDateEditSetDateYMD(dtEdit, year, month, day):

	"""

	Sets the day, month and year to the content of BCDateEdit dtEdit.
	This function is not supported under VR mode.
	


	@dtEdit object: the BCDateEdit.

	@year integer: the day of the date

	@month integer: the day of the date

	@day integer: the day of the date

	"""

def BCWizardGoToNextPage(wiz):

	"""

	Goes to the next wizard wiz page.
	Avoid using programmatical ways to fall through pages when not necessary; 
	let the user decide if and when will continue to next page.
	Wizard will go to next page, even if next button is disabled.
	Continuous sequential calls will not forward wizard to subsequent pages since 
	when (changing page) animation is in progress, the function does nothing.
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	"""

def BCApplicationIsGuiMode():

	"""

	Informs whether the current Application has started in GUI mode or not.
	This function is not supported under VR mode.
	


	@returns: True if application has started in GUI mode, False otherwise.

	"""

def BCListViewItemSetSideButton(item, col, funct, data):

	"""

	Sets a tiny push button to be displayed aligned at the right of the cell at item for column col together with other content (text, icon).
	The standard side button displays "..." as text but you can set icon with BCListViewItemSideButtonSetIconFileName().
	
	WARNING: Side button and cell widgets (combo box, push button, check box, progress bar) in the same cell is not supported.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@funct callback: a callback function that will be called every time the button clicked.
	See BC_LISTVIEWITEM_BUTTON_CLICKED_FUNCTION for details.
	integer BC_LISTVIEWITEM_BUTTON_CLICKED_FUNCTION(item, col, data)
	The function to be called everytime the button will be clicked.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	item  object    the ListViewItem.
	col   integer   the ListViewItem column at which the button is found.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewItemSideButtonSetIconFileName(item, col, fileName):

	"""

	Sets an icon with file name fileName to the side button of item at col.
	Side button cannot display both icon and text.
	Images larger than item height will be scaled down.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem that contains the button.

	@col integer: the column index.

	@fileName string: the filename of the icon.

	"""

def BCListViewItemSideButtonSetToolTip(item, col, tip):

	"""

	Sets the tooltip (balloon help) for side button item item at column col to the text specified by tip.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem that contains the side button.

	@col integer: the column index.

	@tip string: the text to be displayed at balloon help.

	"""

def BCListViewItemHasSideButton(item, col):

	"""

	Returns True if the ListViewItem item cell contains a side button aligned right at given column col, or False otherwise.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem

	@col integer: the column index.

	@returns: True if the ListViewItem item at column col contains a side button, or False otherwise.

	"""

def BCListViewItemSideButtonSetVisible(item, col, visible):

	"""

	Sets whether the side button at column col will be visible or not depending on the value of visible.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@visible boolean: set this parameter to 1 for the widget to be visible, or 0 otherwise.

	"""

def BCListViewItemSideButtonIsVisible(item, col):

	"""

	Returns whether the side button of item item at column col is visible or not.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: True if the side button is visible, or False otherwise.

	"""

def BCListViewItemSideButtonSetEnabled(item, col, enable):

	"""

	Sets whether the side button at column col will be enabled or not depending on the value of enable.
	A disabled item widget does not interact with user events. By default, all side buttons are enabled.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@enable boolean: set 0 for the side button to be disabled, or 1 to enable (default).

	"""

def BCListViewItemSideButtonIsEnabled(item, col):

	"""

	Returns whether the side button of item item at column col is enabled or not.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@returns: True if the side button is enabled, or False otherwise.

	"""

def BCListViewSetAboutToRenameItemFunction(lv, funct, data):

	"""

	Sets a function that will be called when renaming of a column of ListViewItem item is about to start.
	You have access to rename editor here (type BCLineEdit).
	If you want to block renaming items use BCListViewItemSetRenameType(item, col, BCRenameType_None) after constructed them.
	If you want to validate the rename data use BCListViewSetAboutToCommitRenameEditorDataFunction().
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called. See BC_LISTVIEW_ABOUT_TO_RENAME_ITEM_FUNCTION for details.
	integer BC_LISTVIEW_ABOUT_TO_RENAME_ITEM_FUNCTION(lv, item, col, editor, data)
	The function to be called when renaming of an item cell starts.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv      object    the ListView.
	item    object    the ListViewItem.
	col     integer   the ListViewItem column.
	editor  object    the LineEdit used as an editor.
	data    anything  anything that may be required in function.
	
	Return: 1 to cancel the rename action, or 0 to proceed.

	@data anything: (optional)any data required by funct.

	"""

def BCMessageWindowSetTextAlignment(messageWindow, alignment):

	"""

	Sets the alignment of the text message (default BCAlignCenter).
	This function is not supported under VR mode.
	


	@messageWindow object: the BCMessageWindow.

	@alignment integer: specifies the alignment of the text message.
	See BCEnumAlignment for details.
	
	guitk.constants BCEnumAlignment
	This enum type is used to describe alignment. It contains horizontal and vertical flags. Alignment is used with BCGridLayoutAddMultiCellWidget for example.
	NOTE: You can use at most one horizontal and one vertical flag at a time.
	 - guitk.constants.BCAlignAuto
	aligns according to the language. Left for most, right for Arabic and Hebrew.
	 - guitk.constants.BCAlignLeft
	aligns with the left edge.
	 - guitk.constants.BCAlignRight
	aligns with the right edge.
	 - guitk.constants.BCAlignHCenter
	centers horizontally in the available space.
	 - guitk.constants.BCAlignJustify
	justifies the text in the available space.
	 - guitk.constants.BCAlignTop
	aligns with the top.
	 - guitk.constants.BCAlignBottom
	aligns with the bottom.
	 - guitk.constants.BCAlignVCenter
	centers vertically in the available space.
	 - guitk.constants.BCAlignCenter
	centers in both dimensions (vertically and horizontally).
	 - guitk.constants.BCAlignHorizontal_Mask
	horizontal mask.
	 - guitk.constants.BCAlignVertical_Mask
	vertical mask.
	 - guitk.constants.BCAlignVJustify
	Justifies the text vertically in the available space.

	"""

def BCLineEditSetF2Function(le, funct, data):

	"""

	Sets the function that will be called when F2 key is pressed in the BCLineEdit.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@funct callback: the function that will be called. See BC_LINEEDIT_F2_FUNCTION for details.
	integer BC_LINEEDIT_F2_FUNCTION(le, data)
	The function to be called when F2 key is pressed in BCLineEdit le.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly
	but with the use of a timer (BCTimerSingleShot). If you are not sure how to do it, please contact GUI Dept for more details.
	
	Arguments
	
	le    object    the BCLineEdit.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by function funct.

	"""

def BCLineEditSetEditingFinishedFunction(le, funct, data):

	"""

	Sets the function to be called when editing of BCLineEdit le is finished.
	Editing of a BCLineEdit is finished by pressing the Return or Enter key or when le loses focus. If the text
	is unchanged though, funct will not be called!
	NOTE: If BCLineEditSetEnterPressedFunction is set for le and enter is pressed, the enter-pressed-function callback will be called first.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@funct callback: the function to be called. See BC_LINEEDIT_EDITING_FINISHED_FUNCTION for details.
	integer BC_LINEEDIT_EDITING_FINISHED_FUNCTION(le, data)
	The function to be called when the editing on BCLineEdit le is finished.
	Editing is finished by pressing the Return or Enter key or when le loses focus. If the text is unchanged though, this function will not be called.
	
	Arguments
	
	le    object    the BCLineEdit.
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by function funct.

	"""

def BCDrawerGridSetStableWidget(drawer, w):

	"""

	Set the stable widget (cannot hidden with buttons) w inside DrawerGrid drawer.
	The widget will be nested inside the grid.
	Stable widget cannot be shown/hidden with buttons, i.e. is always visible.
	This function is not supported under VR mode.
	


	@drawer object: the DrawerGrid.

	@w object: the widget to be inserted.
	NOTE: Recall that each drawer grid is designed to accommodate one and only one stable widget.

	"""

def BCComboBoxSetMaxVisibleItems(box, maxItems):

	"""

	Sets the maximum on screen size of the BCComboBox in number of items (default is 10).
	NOTE: If maxItems is exceeded, a vertical scrollbar is displayed.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@maxItems integer: the on screen number of items.

	"""

def BCListViewSetAboutToCommitRenameEditorDataFunction(lv, funct, data):

	"""

	Sets the function that will be called just before list rename editor's data committed to item.
	You can check and validate the rename data (string or number) inserted from user.
	At this point the user decided to modify the ListViewItem text (for example pressed Enter key), but value was not applied yet.
	Editor rename data can be discarded or accepted according to return value of call back.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called. See BC_LISTVIEW_ABOUT_TO_COMMIT_RENAME_EDITOR_DATA_FUNCTION for details.
	integer BC_LISTVIEW_ABOUT_TO_COMMIT_RENAME_EDITOR_DATA_FUNCTION(lv, item, col, editor, reason, data)
	The function to be called just before list rename editor data committed to ListViewItem.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv      object    the ListView.
	item    object    the ListViewItem.
	col     integer   the ListViewItem column.
	editor  object    the LineEdit used as an editor.
	reason  integer   the user response that triggered commit data (KeyEnter, KeyTab, MouseButtonPress etc).
	data    anything  anything that may be required in function.
	
	Return: 1 to discard editor's data from committing, or 0 to accept the data.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewIsMultipleItemsRenameEnabled(lv, col):

	"""

	Returns 1 if column col at ListView lv enables multiple items renaming; otherwise returns 0 (default).
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@returns: 1 if column col enables multiple items renaming, otherwise 0.

	"""

def BCListViewSetRenameItemFinishedFunction(lv, funct, data):

	"""

	Sets the function that will be called after ListViewItem rename finished (data accepted or discarded).
	The editor is not active at this point since item is not in editing state anymore.
	If you want to validate the rename data use BCListViewSetAboutToCommitRenameEditorDataFunction().
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called. See BC_LISTVIEW_RENAME_ITEM_FINISHED_FUNCTION for details.
	integer BC_LISTVIEW_RENAME_ITEM_FINISHED_FUNCTION(lv, item, col, dataCommitted, text, data)
	The function to be called after ListViewItem rename finished.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv             object    the ListView.
	item           object    the ListViewItem.
	col            integer   the ListViewItem column.
	dataCommitted  integer   the LineEdit used as an editor.
	text           string    the user response that triggered commit data (KeyEnter, KeyTab, MouseButtonPress etc).
	data           anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewSetExpandItemsButtonEnabled(lv, enable):

	"""

	Shows a button at the right of the header that when clicked expand or collapse the items of (tree) list view lv.
	Makes sense for tree views.
	NOTE: If you execute BCListViewSetItemsExpanded(), button state is adjusted.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@enable boolean: set 1 to enable the button or 0 to disable (default).

	"""

def BCTableIsCellSelected(t, row, col):

	"""

	Returns 1 if cell at column col and row row is selected, otherwise returns 0.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@row integer: the row.

	@col integer: the column.

	@returns: True if the requested cell is selected, False otherwise.

	"""

def BCSliderSetValueChangedOnMouseOrKeyRelease(sl, enable):

	"""

	Sets whether BCSlider's sb value changed callback will be called only on mouse or key (Right, Left, Up, Down Arrow, Page Up, Page Down) release or not.
	This function is not supported under VR mode.
	


	@sl object: the BCSlider.

	@enable integer: set this parameter to 1 so that value changed callback will be called only on mouse or key release, or 0 otherwise.

	"""

def BCWindowSetModal(win, modal):

	"""

	Sets whether win will be shown as modal or modeless to modal
	While in modal state, a window grabs all input. No other window can be used until win is closed.
	NOTE: BCWindowSetModal function must be called before the BCShow function.
	NOTE: If from BCWindow win created an other BCWindow win2 then function BCWindowSetModal must be called and for win2 and so on.
	This function is not supported under VR mode.
	


	@win object: the BCWindow.

	@modal boolean: the new value for modal state

	"""

def BCSplitterGetWidgetSizes(sp):

	"""

	Returns an IntArray of the size parameters of all the widgets in splitter sp.
	If the splitter's orientation is horizontal, the array is a list of widget widths.
	If the orientation is vertical, the array is a list of widget heights.
	This function is not supported under VR mode.
	


	@sp object: the BCSplitter whose children's sizes you want to get.

	@returns: an IntArray of the size parameters of all the widgets in splitter sp.

	"""

def BCSplitterSetWidgetSizes(sp, sizes):

	"""

	Sets the size parameters of splitter's widgets to the values given in the sizes array.
	If the BCSplitter is horizontal, the values set the widths of each widget going from left
	to right. If the BCSplitter is vertical, the values set the heights of each widget going
	from top to bottom. Extra values in the list are ignored. If the integer array contains
	too few values, the result is undefined but the program will still be well-behaved.
	Note that the values in list should be the height/width that the widgets should be resized to.
	Take care that the setting of the new values is done after the window which the BCSplitter
	belongs to, has been created.
	This function is not supported under VR mode.
	


	@sp object: the BCSplitter whose children's sizes you want to set.

	@sizes object: the IntArray with the sizes you want to set for every BCSplitter's child.

	"""

def BCSplitterSetSplitterMovedFunction(sp, funct, data):

	"""

	Sets the function that will be called every time a splitter handle is moved.
	This function is not supported under VR mode.
	


	@sp object: the BCSplitter.

	@funct callback: the function that will be called when a splitter handle is moved.
	See BC_SPLITTER_MOVED_FUNCTION for details.
	integer BC_SPLITTER_MOVED_FUNCTION(splitter, data)
	The function to be called when splitter areas have been resized (i.e. a handle of the splitter has been moved).
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	splitter  object    the BCSplitter.
	data      anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any user data required by function funct.

	"""

def BCComboBoxSetMouseWheelEnabled(cb, enable):

	"""

	Enables or disables scrolling though combobox items with mouse wheel according to enable.
	By default, when a BCComboBox has the focus, the mouse wheel scrolls though its items, even if its popup is hidden.
	Calling this function with enable set to False, the mouse wheel is disabled. Disabling mouse wheel may come in handy
	in cases where you want to scroll only the container (like a scrollview) into which the combobox is placed but not
	the very same combobox.
	This function is not supported under VR mode.
	


	@cb object: the BCComboBox

	@enable boolean: set this to False in order to disable mouse wheel; True otherwise. By default, mouse wheel is enabled

	"""

def BCScrollAreaCreate(p):

	"""

	Creates a BCScrollArea widget.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout of the created BCScrollArea.

	@returns: the created BCScrollArea.

	"""

def BCScrollAreaSetWidget(sa, w):

	"""

	Sets widget w to BCScrollArea sa.
	The widget becomes a child of the BCScrollArea, and will be destroyed when the BCScrollArea is deleted or when a new widget is set.
	If the BCScrollArea is visible when the widget is added, you must show() it explicitly.
	Note that you must add the layout of widget before you call this function.
	if you add it later, the widget will not be visible - regardless of when you show() the scroll area. In this case, you can also not show() the widget later.
	This function is not supported under VR mode.
	


	@sa object: the BCScrollArea.

	@w object: the widget that will be set in the BCScrollArea.

	"""

def BCScrollAreaSetWidgetResizable(sa, resizable):

	"""

	Sets whether the BCScrollArea should resize its set widget.
	If this property is set to to False (the default), the BCScrollArea honors the size of its widget.
	
	If this property is set to to True, the BCScrollArea will automatically resize the widget in order to avoid scroll bars where they can be avoided,
	or to take advantage of extra space.
	This function is not supported under VR mode.
	


	@sa object: the BCScrollArea.

	@resizable boolean: the boolean value of the property.

	"""

def BCScrollAreaWidgetResizable(sa):

	"""

	Returns the value of the resizable property of BCScrollArea sa.
	This function is not supported under VR mode.
	


	@sa object: the BCScrollArea.

	@returns: the boolean value of the property.

	"""

def BCComboBoxMouseWheelEnabled(cb):

	"""

	Returns True or False if mouse wheel is enabled or not for BCComboBox cb.
	This function is not supported under VR mode.
	


	@cb object: the BCComboBox

	@returns: True if mouse wheel is enabled; False otherwise

	"""

def BCListViewSetFixedItemIconSize(lv, w, h):

	"""

	Sets the size of the items' icons to be width /a w and height /a h.
	Icons size can only scaled down from their actual (physical) icons size.
	All items have same size icons for readability and performance reasons.
	The icons size (when not fixed) depends on the largest icon set with BCListViewItemSetIconFileName().
	To clear the fixed icons size just use an invalid size, i.e. width or height to -1.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@w integer: the icon size width in pixels

	@h integer: the icon size height in pixels

	"""

def BCListViewSetPredefinedContentsIconFileNames(lv, col, fileNames):

	"""

	Set ListView filter to use specific (fixed) icon options for filter widgets that provide a menu (ComboBox and CheckableMenu).
	You can customize the options for the drop down menus of ComboBox and CheckableMenu.
	NOTE: The standard ListView filter ComboBox or CheckableMenu builds its drop down menu from the contents of ListViewItems.
	If your filter does not provide ComboBox or CheckableMenu for column col, nothing happens. Duplicates are removed.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@fileNames object: the icon file names (absolute or relative) None terminated.

	"""

def BCListViewItemWidgetDestroy(item, col):

	"""

	Deletes the cell widget that was set at item column col.
	Supported item widgets are
	- Button (BCListViewItemSetButton()),
	- Checkbox (BCListViewItemSetCheckBox()),
	- ComboBox (BCListViewItemSetComboBox()),
	- ProgressBar (BCListViewItemSetProgressBar()),
	- RadioButton (BCListViewItemSetRadioButton())
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	"""

def BCFlash(w):

	"""

	Highlight widget w with animation.
	Use it when you want to draw user's attention to a specific window component.
	This function is not supported under VR mode.
	


	@w object: the widget.

	"""

def BCSetFocusColor(w, r, g, b):

	"""

	Sets the color (r, g and b values) to highlight widget \w while it has the focus (i.e. after making it current either by pressing Tab or by mouse click)
	NOTE: Some widgets by design don't get focus or the get focus only by Tab or only by mouse click.
	WARNING: Avoid using this function and respect the current style to achieve a coherent appearance of your GUI.
	WARNING: This function may become disabled or its result may be overridden in the future or by applications that use their own style or stylesheet.
	This function is not supported under VR mode.
	


	@w object: the widget whose background color will be set while it has focus.

	@r integer: the value for red (0 - 255).

	@g integer: the value for green (0 - 255).

	@b integer: the value for blue (0 - 255).

	"""

def BCListViewItemRepaint(item):

	"""

	Function is not supported. For more info, please contact Customer Service department.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	"""

def BCListViewItemSetRenameEnabled(item, col, enable):

	"""

	Function is obsolete. Use BCListViewItemSetRenameType() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column.

	@enable integer: set one of the possible values (for example, set to 0 to disable renaming).
	Possible values are :
	- 0 : no renaming (default).
	- 1 : double values are accepted.
	- 2 : integers are accepted.
	- 3 : anything goes.

	"""

def BCListViewItemColumnRenameType(item, col):

	"""

	Function is obsolete. Use BCListViewItemRenameType() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column.

	@returns: the rename type of the column for in place edit :text, int, double, no renaming.
	Possible values are :
	- 0 : no renaming (default).
	- 1 : double values are accepted.
	- 2 : integers are accepted.
	- 3 : anything goes.

	"""

def BCListViewItemSetRadioButtonValueNoCallBack(item, col, check):

	"""

	Function is obsolete. Use BCBlockCallBackFunctions() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column.

	@check integer: the new value.

	"""

def BCListViewItemSetCheckBoxValueNoCallBack(item, col, check):

	"""

	Function is obsolete. Use BCBlockCallBackFunctions() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column.

	@check integer: the new value.

	"""

def BCListViewSetColumnAlwaysVisible(lv, col, visible):

	"""

	Function is obsolete. Use BCListViewHeaderMenuBlockColumnVisibilityChange() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column.

	@visible boolean: set True for col to stay always visible or False to enable show/hide it.

	"""

def BCTextEditAppendMonoFont(te, txt):

	"""

	Function is not supported. For more info, please contact Customer Service department.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@txt string: the text that the BCTextEdit will display.

	"""

def BCPopupMenuSetCheckable(pm, checkable):

	"""

	Function is obsolete. Use BCPopupMenuSetItemCheckable() instead.
	This function is not supported under VR mode.
	


	@pm object: the Menu.

	@checkable boolean: set 1 for checkable, 0 otherwise.

	"""

def BCTextEditSetTextFormat(te, bcf):

	"""

	Function is not supported. For more info, please contact Customer Service department.
	This function is not supported under VR mode.
	


	@te object: the TextEdit.

	@bcf integer: the format.

	"""

def BCButtonGroupSetFlat(bg, f):

	"""

	Function is obsolete. Use BCButtonGroupSetBorderMode() instead.
	This function is not supported under VR mode.
	


	@bg object: the BCButtonGroup.

	@f integer: set this parameter to 1 for no frame, 2 for flat mode, or 0 for full frame mode.

	"""

def BCListViewInsertToolButtonToHeader(lv, toolButton):

	"""

	Function is obsolete. Use BCListViewSetHeaderToolButton() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@toolButton object: the custom tool button to be incorporated.

	"""

def BCWizardSetPage(wiz, index, w):

	"""

	Function is not supported. For more info, please contact Customer Service department.
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@index integer: the index of the page that will change.

	@w object: the widget to be set as a page.

	"""

def BCListViewItemSetOpen(item, open):

	"""

	Function is obsolete. Use BCListViewItemSetExpanded() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@open boolean: set this parameter to True to expand item, or to False to collapse it.

	"""

def BCListViewItemIsOpen(item):

	"""

	Function is obsolete. Use BCListViewItemIsExpanded() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem that is checked.

	@returns: True or False depending on the state of item.

	"""

def BCListViewItemGetCheckBoxValue(item, col):

	"""

	Function is obsolete. Use BCListViewItemCheckBoxIsChecked() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column.

	@returns: 1 if the checkBox at column col of ListViewItem item is checked, or 0 otherwise.

	"""

def BCListViewItemSetCheckBoxValue(item, col, check):

	"""

	Function is obsolete. Use BCListViewItemCheckBoxSetChecked() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column.

	@check integer: the value to be set.

	"""

def BCListViewItemSetRadioButtonValue(item, col, check):

	"""

	Function is obsolete. Use BCListViewItemRadioButtonSetChecked() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column.

	@check integer: 1 to turn it on or 0 to turn it off.

	"""

def BCListViewItemGetRadioButtonValue(item, col):

	"""

	Function is obsolete. Use BCListViewItemRadioButtonIsChecked() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column.

	@returns: 1 if the radio button at column col of ListViewItem item is on, or 0 otherwise.

	"""

def BCListViewCount(lv):

	"""

	Function is obsolete. Use BCListViewTopLevelItemCount() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: The number of top-level items in ListView lv.

	"""

def BCListViewItemCount(item):

	"""

	Function is obsolete. Use BCListViewItemChildCount() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem whose number of children will be counted.

	@returns: the number of immediate children of item.

	"""

def BCCheckListItemSetOn(item, on):

	"""

	Function is obsolete. Use BCListViewItemCheckableSetOn() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@on boolean: True sets item to checked, False sets it to unchecked.

	"""

def BCCheckListItemIsOn(item):

	"""

	Function is obsolete. Use BCListViewItemCheckableIsOn() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@returns: True or False depending on the state of item.

	"""

def BCListViewAddCheckItem(lv, numCols, strl, rename):

	"""

	Function is obsolete. Use BCListViewItemSetCheckable() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@numCols integer: the number of columns in lv.

	@strl object: the strings that will be displayed in the new item.

	@rename object: an array of integers denoting which column texts may be renamed. Possible
	values are:
		- 0 : no renaming (default).
		- 1 : double values are accepted.
		- 2 : integers are accepted.
		- 3 : anything goes.

	@returns: the created ListViewItem.

	"""

def BCListViewItemAddCheckItem(item, numCols, strl, rename):

	"""

	Function is obsolete. Use BCListViewItemSetCheckable() instead.
	This function is not supported under VR mode.
	


	@item object: the parent item where the new CheckListItem will be added.

	@numCols integer: the number of columns.

	@strl object: the text that will be displayed for each column.

	@rename object: an array on integers denoting which column texts may be renamed.
		- 0 : no renaming (default).
		- 1 : double values are accepted.
		- 2 : integers are accepted.
		- 3 : anything goes.

	@returns: The created ListViewItem.

	"""

def BCCheckListItemSetStateChangedFunction(item, funct, data):

	"""

	Function is obsolete. Use BCListViewItemCheckableSetToggledFunction() instead.
	This function is not supported under VR mode.
	


	@item object: the CheckListItem.

	@funct callback: the function that is called. See BC_LISTVIEWITEM_CHECKABLE_TOGGLED_FUNCTION for details.
	integer BC_LISTVIEWITEM_CHECKABLE_TOGGLED_FUNCTION(item, state, data)
	The function to be called when checkable ListViewItem item is checked or unchecked.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	item   object    the checkable ListViewItem.
	state  integer   the toggle state information: 1 when the BCPushButton is on (i.e. toggled); 0 otherwise.
	data   anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any user data required by function funct.

	"""

def BCListViewHeaderSetIcon(lv, col, filename):

	"""

	Function is obsolete. Use BCListViewHeaderSetIconFileName() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the header section of column where the icon will be set.

	@filename string: the filename of the icon.

	"""

def BCListViewItemPixmap(item, col):

	"""

	Function is obsolete. Use BCListViewItemHasIcon() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column of the ListViewItem.

	@returns: False if there is no pixmap (default) at column col, True otherwise.

	"""

def BCListViewItemButtonSetPixmapFile(item, col, pixFile):

	"""

	Function is obsolete. Use BCListViewItemButtonSetIconFileName() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem that contains the button.

	@col integer: the column where the button is set.

	@pixFile string: the filename of the pixmap.

	"""

def BCListViewItemButtonPixmapFile(item, col):

	"""

	Function is obsolete. Use BCListViewItemButtonIconFileName() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem that contains the button.

	@col integer: the column where the button is set.

	@returns: the filename of the pixmap.

	"""

def BCRadioButtonSetPixmapFile(rb, iconname):

	"""

	Function is obsolete. Use BCRadioButtonSetIconFileName() instead.
	This function is not supported under VR mode.
	


	@rb object: the BCRadioButton.

	@iconname string: the absolute path of the iconfile.

	"""

def BCComboBoxInsertItemPixmapFile(box, filename, text, index):

	"""

	Function is obsolete. Use BCComboBoxInsertItemIconFileName() instead.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@filename string: the absolute path of a PNG file.

	@text string: the text that will be inserted.

	@index integer: the index at which text will be inserted (-1 to append).

	"""

def BCListViewItemSetPixmapFile(item, col, pixFile):

	"""

	Function is obsolete. Use BCListViewItemSetIconFileName() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column of the ListViewItem.

	@pixFile string: the absolute path to the PNG file that we want to use.

	"""

def BCTabWidgetSetTabIconFile(tw, w, iconname):

	"""

	Function is obsolete. Use BCTabWidgetSetTabIconFileName() instead.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget.

	@w object: the page widget contained by the tab, in which the icon will be shown.

	@iconname string: the absolute path of a PNG file . If you pass an empty string here, the icon (if any) will not show any more.

	"""

def BCWindowSetTitleBarIcon(win, iconName):

	"""

	Function is obsolete. Use BCWindowSetTitleBarIconFileName() instead.
	This function is not supported under VR mode.
	


	@win object: the BCWindow.

	@iconName string: the absolute path of the icon file.

	"""

def BCLabelSetPixmapFile(lab, iconname):

	"""

	Function is obsolete. Use BCLabelSetIconFileName() instead.
	This function is not supported under VR mode.
	


	@lab object: the BCLabel.

	@iconname string: the absolute path of the icon file.

	"""

def BCButtonSetPixmapFile(b, pixname):

	"""

	Function is obsolete. Use BCButtonSetIconFileName() instead.
	This function is not supported under VR mode.
	


	"""

def BCButtonGetPixmapFile(b):

	"""

	Function is obsolete. Use BCButtonSetIconFileName() instead.
	This function is not supported under VR mode.
	


	@b object: the button.

	"""

def BCButtonSetIconFile(b, iconname):

	"""

	Function is obsolete. Use BCButtonSetIconFileName() instead.
	This function is not supported under VR mode.
	


	@b object: the button.

	@iconname string: the iconname of a PNG file that exists in the images directory or the absolute filename of a PNG file.

	"""

def BCButtonAddIconFile(b, iconname, mode, state):

	"""

	Function is obsolete. Use BCButtonAddIconFileName() instead.
	This function is not supported under VR mode.
	


	@b object: the toggle button.

	@iconname string: the iconname of a PNG file that exists in the images directory or the absolute filename of a PNG file, that will be displayed under mode and state.

	@mode integer: the mode for which a pixmap is intended to be used. See BCEnumMode property for more details.
	
	guitk.constants BCEnumMode
	This enum type describes a Button's pixmap or a ListViewItem's mode.
	 - guitk.constants.BCNormalMode
	The user does not interact with the Button or the ListViewItem, but their functionality is available.
	 - guitk.constants.BCDisabledMode
	The user cannot interact with the Button.
	 - guitk.constants.BCActiveMode
	Button: The user mouse cursor is over button or button is pressed (only for ToolButtons).
	 - guitk.constants.BCSelectedMode
	Button: Display the pixmap when the item represented by the icon is selected.
	ListViewItem: The item is selected.

	@state integer: the state for which a pixmap is intended to be used. See BCEnumIconState property for more details.
	
	guitk.constants BCEnumIconState
	This enum describes the state for which a pixmap is intended to be used.
	 - guitk.constants.BCOffState
	Display the pixmap when a toggle button is in an "off" state (unpressed)
	 - guitk.constants.BCOnState
	Display the pixmap when a toggle buttons is in an "on" state (pressed)

	"""

def BCListViewSetResizeEnabled(lv, col, enable):

	"""

	Function is obsolete. Use BCListViewSetColumnResizeEnabled() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column.

	@enable boolean: True if the column should be allowed to be resized (the default), otherwise False.

	"""

def BCListViewHeaderAddToolTip(lv, col, tip):

	"""

	Function is obsolete. Use BCListViewHeaderSetToolTip() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the header section for column col.

	@tip string: the tooltip.

	"""

def BCListViewDisplayMessageInViewport(lv, message):

	"""

	Function is obsolete. Use BCListViewSetViewportText() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@message string: the message to be displayed centered vertically and horizontally.

	"""

def BCListViewInfoBoxCreate(p, lv):

	"""

	Function is obsolete. Use BCItemViewInfoBoxCreate() instead.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@lv object: the ListView for which the created ListInfoBox will display info.

	@returns: the created ListInfoBox.

	"""

def BCListViewInfoBoxUpdate(lv):

	"""

	Function is obsolete. Use BCItemViewInfoBoxUpdate() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView that ItemViewInfoBox manages.

	"""

def BCListViewInfoBoxSetManualUpdateEnabled(lv, fieldIndex, enable):

	"""

	Function is obsolete. Use BCItemViewInfoBoxBlockAutoUpdates() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView that ItemViewInfoBox manages.

	@fieldIndex integer: set 0 to manually update left most field, 1 for the middle one and 2 for the field on the right.

	@enable boolean: set True for manual updates or False for auto updates.

	"""

def BCListViewInfoBoxSetMessage(lv, fieldIndex, message):

	"""

	Function is obsolete. Use BCItemViewInfoBoxSetText() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView that ItemViewInfoBox manages.

	@fieldIndex integer: set 0 for the left most field, 1 for the middle one and 2 for the field on the right.

	@message string: the message to be displayed.

	"""

def BCListViewInfoBoxSetHierarchy(info, hierarchy):

	"""

	Function is obsolete. Use BCItemViewInfoBoxSetTotalCounterMode() instead.
	This function is not supported under VR mode.
	


	@info object: the ItemViewInfoBox.

	@hierarchy boolean: set True to count all items of hierarchical ListViews or False for top-level items.

	"""

def BCListViewSetColumnMenuVisibilityChangeEnabled(lv, col, enable):

	"""

	Function is obsolete. Use BCListViewHeaderMenuBlockColumnVisibilityChange() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column.

	@enable boolean: set False for col to block visibility change or True (default) to enable show/hide it.

	"""

def BCListViewSetColumnMenuAlternativeName(lv, col, altName):

	"""

	Function is obsolete. Use BCListViewHeaderSetStringRepresentation() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column.

	@altName string: the alternative name to be shown in column menu.

	"""

def BCListViewShowColumnMenuButton(lv, show):

	"""

	Function is obsolete. Use BCListViewSetHeaderMenuColumnVisibilityChangeEnabled() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@show boolean: set this parameter to True to show the column button, or False to hide it.

	"""

def BCListViewColumnMenuButtonIsShown(lv):

	"""

	Function is obsolete. Use BCListViewSetHeaderMenuColumnVisibilityChangeEnabled() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: True if button is visible or False otherwise.

	"""

def BCListViewSetColumnMenu(lv, pm):

	"""

	Function is obsolete. Use BCListViewSetColumnVisibilityChangeMenu() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@pm object: the custom menu to replace the default one.

	"""

def BCListViewSetColumnMenuAddItemEnabled(lv, enable, funct, data):

	"""

	Function is not supported. For more info, please contact Customer Service department.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@enable boolean: set this parameter to True to enable adding columns to ListView t, or to False to disable it.

	@funct callback: is a function that will be called when the user presses the enter key in the LineEdit. See BC_LISTVIEW_ADD_COLUMN_MENU_FUNCTION for details.
	integer BC_LISTVIEW_ADD_COLUMN_MENU_FUNCTION(lv, newCol, name, data)
	The function to be called when the user presses the enter key in the BCLineEdit of the popup menu.
	This means when the user has finished entering a name for the new column. 
	This function can be used to check if the name entered is applicable to the listview or not. If it returns 1, the name is applicable and the column is added to the right side of the listview, otherwise the name is not applicable and the operation is cancelled.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv      object    the ListView.
	newCol  integer   the index of the new column.
	name    string    the name for the new column.
	data    anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewSetReturnPressedFunction(lv, funct, data):

	"""

	Function is obsolete. Use BCListViewSetEnterPressedFunction() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called. See BC_LISTVIEW_ENTER_PRESSED_FUNCTION for details.
	integer BC_LISTVIEW_ENTER_PRESSED_FUNCTION(lv, item, data)
	The function to be called when the Enter (or Return) keyboard button is pressed on a ListView or a BCIconView.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView or the BCIconView.
	item  object    the current item.
	data  anything  anything that may be required in function.
	
	Return: 0 to block the event otherwise return 1.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewHeaderSetLabel(lv, col, text):

	"""

	Function is obsolete. Use BCListViewHeaderSetText() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the header section for column.

	@text string: the text that will be displayed.

	"""

def BCListViewHeaderGetLabel(lv, col):

	"""

	Function is obsolete. Use BCListViewHeaderGetText() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the header section for column of which the label is required.

	@returns: the label of the header of lv at col.

	"""

def BCListViewHeaderHide(lv):

	"""

	Function is obsolete. Use BCListViewHeaderSetVisible() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	"""

def BCListViewHeaderShow(lv):

	"""

	Function is obsolete. Use BCListViewHeaderSetVisible() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView whose header we want to show.

	"""

def BCListViewSetCurrentChangedFunction(lv, funct, data):

	"""

	Function is obsolete. Use BCListViewSetCurrentItemChangedFunction() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called when current item has changed.
	
	
	
	Return:

	@data anything: (optional)any data required by function funct.

	"""

def BCListViewItemOkRename(item, col):

	"""

	Function is obsolete. Use BCListViewAcceptRename() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column.

	"""

def BCListViewItemStartRename(item, col):

	"""

	Function is obsolete. Use BCListViewStartRename() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column.

	"""

def BCListViewSetResizeMode(lv, mode):

	"""

	Function is obsolete. Use BCListViewSetColumnResizeMode() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@mode integer: the column resize mode. See BCEnumColumnResizeMode for details.
	
	guitk.constants BCEnumColumnResizeMode
	This enum type describes how the columns of a list view adjust to resize events on the width of the list.
	 - guitk.constants.BCNoColumn
	The columns are not resized when listview width change.
	Horizontal scrollbar will be shown when items content is too large to fit.
	 - guitk.constants.BCAllColumns
	Columns automatically and equally resize to fill the available viewport width.
	Columns width cannot be changed by the user or programmatically.
	Horizontal scrollbar will be never shown.
	 - guitk.constants.BCLastColumn
	Last column automatically resize to fill the available viewport width.
	Horizontal scrollbar will be never shown.

	"""

def BCListViewItemExists(lv, col, text):

	"""

	Function is obsolete. Use BCListViewTopLevelItemExists() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column.

	@text string: the string that will be searched.

	@returns: True if text is found within the ListView; False otherwise.

	"""

def BCListViewSetFilterAppliedFunction(lv, funct, data):

	"""

	Function is obsolete. Use BCListViewSetFilterAboutToApplyFunction() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function to be called when filter applied. See BC_LISTVIEW_FILTER_ABOUT_TO_APPLY_FUNCTION for details.
	integer BC_LISTVIEW_FILTER_ABOUT_TO_APPLY_FUNCTION(lv, data)
	The function to be called when filter is applied.
	Return 1 to block the default process otherwise return 0.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	data  anything  anything that may be required in function.
	
	Return: 1 to block the default process otherwise return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewItemSetRenameStartedFunction(item, funct, data):

	"""

	Function is obsolete. Use BCListViewItemSetAboutToRenameFunction() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@funct callback: the function that will be called. See BC_LISTVIEWITEM_ABOUT_TO_RENAME_FUNCTION for details.
	integer BC_LISTVIEWITEM_ABOUT_TO_RENAME_FUNCTION(item, col, data)
	The function to be called when renaming of a column of item starts.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	item  object    the ListViewItem.
	col   integer   the ListViewItem column.
	data  anything  anything that may be required in function.
	
	Return: 1 to cancel the rename action, or 0 to proceed.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewSetSortingFunction(lv, funct, data):

	"""

	Function is obsolete. Use BCListViewSetItemsSortedFunction() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: is a function that will be called when the user mouse click on the column header. See BC_LISTVIEW_ITEMS_SORTED_FUNCTION for details.
	integer BC_LISTVIEW_ITEMS_SORTED_FUNCTION(lv, col, ascending, data)
	The function to be called right after items sorted into the list (for example mouse click at a column header).
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv         object    the ListView.
	col        integer   the ListView column.
	ascending  integer   1 for ascending and 0 for descending order.
	data       anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewHeaderPopupSetFunction(lv, funct, data):

	"""

	Function is obsolete. Use BCListViewHeaderMenuSetAboutToShowFunction() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called when right mouse button pressed. See BC_LISTVIEW_HEADER_MENU_ABOUTTOSHOW_FUNCTION for details.
	integer BC_LISTVIEW_HEADER_MENU_ABOUTTOSHOW_FUNCTION(lv, pm, col, data)
	The function to be called when mouse right button pressed to the header of ListView lv.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv    object    the ListView.
	pm    object    the provided pull down menu.
	col   integer   the ListView column. .
	data  anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	"""

def BCListViewHeaderPopupShowPopupUnderColumn(lv, show):

	"""

	Function is obsolete. Use BCListViewHeaderMenuPopupBelowHeader() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@show boolean: set True for showing the header popup immediately under the column header, or False for showing it on mouse cursor's position.

	"""

def BCListViewHeaderPopupSetRenameEnabled(lv, col, enable):

	"""

	Function is obsolete. Use BCListViewHeaderMenuSetRenameColumnEnabled() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@enable boolean: If enable is set to True, then the first item after the custom ones, of the returned Menu will be an item having text "Rename", with which it is possible to rename the section of the header clicked.

	"""

def BCListViewHeaderPopupSetCopyDisabled(lv, col, disable):

	"""

	Function is obsolete. Use BCListViewHeaderMenuSetCopyEnabled() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the header section for column col.

	@disable boolean: If disable is set to True, then the 'Copy column' and 'Copy selected in column' items, of the returned Menu will not be shown. Otherwise these items will be shown (the default).

	"""

def BCRadioButtonSetPressFunction(rb, funct, data):

	"""

	Function is obsolete. Use BCRadioButtonCreate() instead.
	This function is not supported under VR mode.
	


	@rb object: the BCRadioButton.

	@funct callback: the function that will be called when the BCRadioButton is pressed. See BC_RADIOBUTTON_PRESS_FUNCTION for details.
	integer BC_RADIOBUTTON_PRESS_FUNCTION(rb, data)
	The function to be called when an existing BCRadioButton is pressed.
	 DEPRECATED: Do not use this callback.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	rb    object    the BCRadioButton.
	data  anything  anything that may be required by the function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)anything that may be required in funct.

	"""

def BCListViewHeaderMenuPopupBelowHeader(lv, below):

	"""

	Function is not supported. For more info, please contact Customer Service department.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@below boolean: set True for showing the header popup immediately under the column header, or False for showing it on mouse cursor's position.

	"""

def BCMessageWindowAddExtraButton(messageWindow, text, returnedValue):

	"""

	Function is obsolete. Use BCMessageWindowSetExtraButton() instead.
	This function is not supported under VR mode.
	


	@messageWindow object: the BCMessageWindow.

	@text string: the text of button.

	@returnedValue integer: the value that will be returned from BCMessageWindowExecute() if extra button pressed.

	"""

def BCPlotModelItemName(plotItem):

	"""

	Function is obsolete. Use BCPlotModelCurveName() instead.
	This function is not supported under VR mode.
	


	@plotItem object: the Curve.

	@returns: the name of plotItem.

	"""

def BC3DBarChartPlotModelItemCreate(chart, name, x, y, z, pointsCount, r, g, b):

	"""

	Function is obsolete. Use BC3DBarChartPlotModelCurveCreate() instead.
	This function is not supported under VR mode.
	


	@chart object: the BCPlot3DBar.

	@name string: the name of plot item.

	@x double []: the array of x values.

	@y double []: the array of y values.

	@z double []: the array of z values.

	@pointsCount integer: the number of points.

	@r integer: the red value.

	@g integer: the green value.

	@b integer: the blue value.

	@returns: the created bar item.

	"""

def BCListViewItemComboBoxSetCurrentItemIntActivatedFunction(item, col, id):

	"""

	Function is not supported. For more info, please contact Customer Service department.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column where comboBox is found.

	@id integer: the id of the item to which current will be set.

	"""

def BCWidgetExpandManagedWidget(wex):

	"""

	Function is obsolete. Use BCWidgetExpandGetWidget() instead.
	This function is not supported under VR mode.
	


	@wex object: the WidgetExpand.

	@returns: the widget controlled by wex.

	"""

def BCListViewItemComboBoxSetCurrentItemActivatedFunction(item, col, index):

	"""

	Function is obsolete. Use BCListViewItemComboBoxSetCurrentItemExecuteActivatedCallBack() instead.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column where comboBox is found.

	@index integer: the index of the item to which current will be set.

	"""

def BCComboBoxSetCurrentItemActivatedFunction(box, index):

	"""

	Function is obsolete. Use BCComboBoxSetCurrentItemExecuteActivatedCallBack() instead.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@index integer: the index of the item to which current will be set.

	"""

def BCListViewBlockCallBackFunctions(lv, block):

	"""

	Function is obsolete. Use BCBlockCallBackFunctions() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@block boolean: True to block all call back functions of ListView, ListViewItem and ListViewFilter, or False to un-block (default).

	"""

def BCListViewCallBackFunctionsBlocked(lv):

	"""

	Function is obsolete. Use BCCallBackFunctionsBlocked() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: True if call back functions are blocked, False otherwise.

	"""

def BCComboBoxBlockCallBackFunctions(cb, block):

	"""

	Function is obsolete. Use BCBlockCallBackFunctions() instead.
	This function is not supported under VR mode.
	


	@cb object: the BCComboBox.

	@block integer: set 1 to block all callback functions of BCComboBox; 0 otherwise.

	"""

def BCComboBoxCallBackFunctionsBlocked(cb):

	"""

	Function is obsolete. Use BCCallBackFunctionsBlocked() instead.
	This function is not supported under VR mode.
	


	@cb object: the BCComboBox.

	@returns: 1 if call back functions are blocked; 0 otherwise.

	"""

def BCLineEditBlockCallBackFunctions(le, block):

	"""

	Function is obsolete. Use BCBlockCallBackFunctions() instead.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@block boolean: set 1 to block all callback functions of BCLineEdit; 0 otherwise.

	"""

def BCLineEditCallBackFunctionsBlocked(le):

	"""

	Function is obsolete. Use BCCallBackFunctionsBlocked() instead.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@returns: 1 if call back functions are blocked; 0 otherwise.

	"""

def BCListViewSetDateFormat(lv, format, sep):

	"""

	Function is not supported. For more info, please contact Customer Service department.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@format string: supported date formats are 
	- d : day as number (1 to 31),
	- dd : day as number with leading zero (01 to 31),
	- ddd : the sort localized day name (Mon to Sun),
	- M : the month as number (1 to 12)
	- MM : the month as number with leading zero (01 to 12)
	- MMM : the sort localized month name (Jan to Dec),
	- yy : the year as two digit number (00-99),
	- yyyy : the year as four digit number,
	For example the 18th day of March 2014 can be displayed as 18-3-2010, 3-18-2010 or 18-Mar-2010 etc.

	@sep string: the separator can also be specified in the format string (format).

	"""

def BCDrawerGridInsertStableWidget(dg, w):

	"""

	Function is obsolete. Use BCDrawerGridSetStableWidget() instead.
	This function is not supported under VR mode.
	


	@dg object: the BCDrawerGrid.

	@w object: the widget to be inserted.

	"""

def BCComboBoxSetSizeLimit(box, limit):

	"""

	Function is obsolete. Use BCComboBoxSetMaxVisibleItems() instead.
	This function is not supported under VR mode.
	


	@box object: the BCComboBox.

	@limit integer: the limit of line number to be displayed.

	"""

def BCListViewFilterSetFixedOptionIconFileNames(lv, col, fileNames):

	"""

	Function is obsolete. Use BCListViewSetPredefinedContentsIconFileNames() instead.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@fileNames object: the icon file names (absolute or relative) None terminated.

	"""

def BCWindowFlash(wid):

	"""

	Function is obsolete. Use BCFlash() instead.
	This function is not supported under VR mode.
	


	@wid object: the Window.

	"""

def BCFrameFlash(f):

	"""

	Function is obsolete. Use BCFlash() instead.
	This function is not supported under VR mode.
	


	@f object: the BCFrame.

	"""

def BCPopupMenuSetItemCurrent(pm, id):

	"""

	Makes current and highlights the item with id id.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@id integer: the id of the item to become current. If id is invalid nothing will happen.

	"""

def BCPopupMenuWidgetItemId(pm, w):

	"""

	Returns the id of the item to which widget w has been inserted, or -1 otherwise.
	This function is not supported under VR mode.
	


	@pm object: the BCMenu.

	@w object: the widget that will be checked.

	@returns: the id of item with widget w, or -1 otherwise.

	"""

def BCApplicationProcessNonUserInputEvents():

	"""

	Processes pending events for the calling thread (normally the main/GUI thread) or until there are no more events to process, whichever is shorter.
	You can call this function occasionally when your program is busy performing a long operation (e.g. copying a file).
	This function is useful when you are doing graphical changes while performing a heavy job and you want to visualize these changes immediately.
	E.g. when you want to update a BCProgressBar while performing a heavy calculation or importing a large file.
	WARNING: Your loop may become slower if you decide to process pending events several times. Call this function with caution, as few times as possible.
	NOTE: This function will not process any user input events, e.g. moving or resizing windows, writing in a BCTextEdit, mouse clicks on buttons etc
	This function is not supported under VR mode.
	


	"""

def BCListViewGetSelectedItem(lv):

	"""

	Returns the single selected item from ListView lv (only one item is selected), otherwise returns None.
	You will get None if more than one items are selected.
	NOTE: This function is much faster than running a loop to find the selected item.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@returns: the selected item.

	"""

def BCWindowCaptionReject(caption):

	"""

	Calls the reject function of the BCWindow with caption.
	If no custom accept function has been set, a default one will be called.
	Normally this function is called when we press the 'Cancel' button to close the BCWindow.
	This function is not supported under VR mode.
	


	@caption string: the caption (title) of the BCWindow whose reject function will be called.

	"""

def BCMessageWindowSetExtraButton(messageWindow, text, returnedValue):

	"""

	Adds a custom user button between the accept and reject buttons with text text.
	WARNING: Do NOT use the numbers 4, 66 or 68 for your custom return value, since they are used internally for OK, Cancel and QuitAll.
	This function is not supported under VR mode.
	


	@messageWindow object: the BCMessageWindow.

	@text string: the text of button.

	@returnedValue integer: the value that will be returned from BCMessageWindowExecute() if extra button pressed.

	"""

def BCWizardSetFinishButtonText(wiz, text):

	"""

	Customize the text for the finish button (default text is Finish).
	Avoid text that may confuse the user and conflict with standard buttons text, for example avoid text Back, Previous, Next, Cancel etc.
	Finish button will be visible when user navigates to the last Wizard page
	This function is not supported under VR mode.
	


	@wiz object: the wizard.

	@text string: the new text.

	"""

def BCToolButtonSetSideArrowEnabled(b, enabled):

	"""

	Sets whether a separated side arrow button is used when ToolButton provides a popup menu (default enabled).
	When side arrow is enabled the tool button displays a special arrow at the right side to indicate that a menu is present.
	When side arrow is not enabled the menu popups instant while the button's own action (click function) is not triggered.
	This function is not supported under VR mode.
	


	@b object: the BCToolButton.

	@enabled boolean: set True to show or False to hide the down arrow.

	"""

def BCToolButtonIsSideArrowEnabled(b):

	"""

	Returns True if separated side arrow button indicates that the menu is present, or False otherwise.
	When side arrow is not enabled the menu popups instant while the button's own action (click function) is not triggered.
	This function is not supported under VR mode.
	


	@b object: the BCToolButton.

	"""

def BCListViewItemComboBoxSetItemEnabled(item, col, index, enable):

	"""

	Sets whether the combobox item with index /a index is enabled. Standard combo box items are enabled.
	Disabled combo box items do not respond to user actions.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@index integer: the index of drop menu item.

	@enable boolean: set 0 disable the combo box item or 1 to enable.

	"""

def BCListViewItemComboBoxIsItemEnabled(item, col, index):

	"""

	Returns 1 in case the combobox item with index /a index is enabled (default enabled).
	NOTE: If there is no comboBox at item at column col, this function returns 0.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem.

	@col integer: the column index.

	@index integer: the index of drop menu item.

	@returns: 1 in case the comboBox item in ListViewItem item, found in column col with index is enabled, 0 otherwise.

	"""

def BCActionCreate(p, name, funct, data):

	"""

	Creates an BCAction object with parent p, a name name and a callback function fun with data data.
	This function is not supported under VR mode.
	


	@p object: the parent widget or layout.

	@name string: the object name of the action and the text that will be displayed in widgets added with BCActionAddWidget(), together with the shortcut combination set with BCActionSetShortcut().

	@funct callback: the function that will be called when the created BCAction is triggered. See
	BC_ACTION_CALLBACK_FUNCTION for details.
	integer BC_ACTION_CALLBACK_FUNCTION(action, data)
	The function to be called when a BCAction is triggered.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	action  object    the BCAction.
	data    anything  anything that may be required in function.
	
	Return: Reserved for future use. We recommend you always return 0.

	@data anything: (optional)any data required by funct.

	@returns: the created BCAction.

	"""

def BCActionSetCheckable(action, checkable):

	"""

	Makes BCAction action checkable or uncheckable.
	A checkable action supports on/off states. By default, a BCAction is not checkable.
	Note that the callback of a checkable BCAction will be triggered after the checked state is changed manually (e.g. by pressing a BCPushButton added to BCAction), but not by calling BCActionSetChecked().
	Also, BCActionTrigger() will change the checked state of a checkable BCAction.
	This function is not supported under VR mode.
	


	@action object: the BCAction.

	@checkable boolean: set this parameter to True to give a checkable property to action or False to remove it.

	"""

def BCActionIsCheckable(action):

	"""

	Returns True if the BCAction is checkable or False otherwise.
	This function is not supported under VR mode.
	


	@action object: the BCAction.

	@returns: True if the action is checkable or False otherwise.

	"""

def BCActionSetChecked(action, check):

	"""

	Changes the checked (on/off) state of BCAction action, if it is checkable.
	It will also change the checked state of any widget added to action
	Note that the callback of action will not be triggered. Also, this function will do nothing if action is not checkable.
	This function is not supported under VR mode.
	


	@action object: the BCAction.

	@check boolean: set this parameter to True to check (set on) action or False to uncheck it.

	"""

def BCActionIsChecked(action):

	"""

	Returns the current checked state of BCAction. If action is not checkable this function will always return  False .
	This function is not supported under VR mode.
	


	@action object: the BCAction.

	@returns: True if currently the action is checked or False otherwise.

	"""

def BCActionTrigger(action):

	"""

	Executes the callback function of action, set with BCActionCreate().
	If action is checkable, its checked state will also change, along with the check state of any widget added to it.
	This function is not supported under VR mode.
	


	@action object: the BCAction.

	"""

def BCActionSetShortcut(action, key):

	"""

	Sets shortcut key to action.
	A shortcut key is a combination of keyboard buttons (e.g. Ctrl+O), which on press, they will trigger the BCAction.
	Note that shortcut keys set with this function will have a global (application-wide) scope.
	You cannot assign the same shortcut key to different actions. If you do so the shortcut key will first be removed by the previous action.
	In case the shortcut key was already used by an application non-script action, it will be assigned back to it when the script ends.
	This function is not supported under VR mode.
	


	@action object: the BCAction.

	@key string: the shortcut key. Valid shortcut keys are composed by:
	- one or more modifier keys: Ctrl, Alt, Shift, Meta (i.e. the Win key)
	- one and only one key: [0,9], [A,Z], [F1,F12], Space, Insert, Delete, Home, End, Page Up, Page Down, Left, Up, Right, Down (arrow keys)
	Syntax: &lt;Modifier&gt;[+&lt;Modifier&gt;+&lt;Modifier&gt;]+Key. Exception to this rule are the [F1,F12] keys, which can also be used without a modifier.
	Examples: "Ctrl+P", "Ctrl+Alt+Space", "F2"

	@returns: True if shortcut key is valid and set successfully to action or False otherwise.

	"""

def BCActionAddWidget(action, widget):

	"""

	Adds widget under the control of action.
	This means that:
	- The widget will call the action's callback. If a function was already set to the widget, it will be replaced.
	- The widget will adopt the checkable property of action and follow its checked state.
	- The action's tooltip will be set to the widget, displaying the name and any shortcut that was set.
	WARNING: The widget cannot have any functionality that BCAction cannot handle. For example, a BCPopupMenu added to the widget, will be removed after action takes control of it.
	This function is not supported under VR mode.
	


	@action object: the BCAction.

	@widget object: the widget to add to action's control. Supported widgets are:
	- BCPushButton
	- BCToolButton
	- BCCheckBox

	@returns: True if widget was added successfully to action or False otherwise.

	"""

def BCListViewSetItemCompareFunction(lv, funct, data):

	"""

	Sets the function that will be called during items get sorted inside the ListView.
	Use this function for custom sorting. This function will only run if sorting is enabled.
	NOTE: This function will run multiple times during sorting (avoid complex calculations in here). For example if you have four items A, B, C and D, the function will run 6 times.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@funct callback: the function that will be called. See BC_LISTVIEW_ITEM_COMPARE_FUNCTION for details.
	integer BC_LISTVIEW_ITEM_COMPARE_FUNCTION(lv, item, other, col, ascOrder, data)
	The function that enables custom sorting in list view items.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	lv        object    the ListView.
	item      object    the ListViewItem currently compared.
	other     object    the other ListViewItem currently compared with.
	col       integer   the ListViewItem column index where sorting takes place.
	ascOrder  integer   the sorting order (1 when ascending, 0 when descending).
	data      anything  anything that may be required in function.
	
	Return: 1 if item is less than other, -1 if item is NOT less than other or 0 for default implementation.

	@data anything: (optional)any data required by function funct.

	"""

def BCLineEditSetPlaceholderText(le, text):

	"""

	Set the message to display when le is empty and does not have keyboard focus.
	When the user sets focus inside line edit info dissapears. If you want to remove the info set an empty text.


	@le object: the BCLineEdit.

	@text string: the message.

	"""

def BCLineEditGetPlaceholderText(le):

	"""

	Returns the info message (when is empty and does not have keyboard focus) that is displayed in le or None if no info set.


	@le object: the BCLineEdit.

	@returns: the text displayed as info.

	"""

def BCListViewItemSetPlaceholderText(item, col, text):

	"""

	Set the message to display when item cell text at col is empty.
	Message usually provide guidance for the contents type of an editable cell, like "Type here", "Integers are only allowed" etc.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem

	@col integer: the column index.

	@text string: the message to be displayed.

	"""

def BCTextEditSetPlaceholderText(te, text):

	"""

	Set the message to display when te has no text inside and not keyboard focus.
	Message is displayed wrapped (breaks lines at appropriate points to fit whole text), but you can provide break line (\n) as well inside your message.
	When the user set focus inside text edit info dissapears. Use empty text to clear.
	Text is aligned centered horizontally and vertically in edit area.
	This function is not supported under VR mode.
	


	@te object: the BCTextEdit.

	@text string: the text to be displayed.

	"""

def BCListViewAddTopLevelItem(lv):

	"""

	Appends a top level item to ListView lv.
	
	WARNING: If no sorting enabled in the list, the item is appended.
	WARNING: In order to avoid performance issues, it is recommended that sorting in list is disabled on mass adding items.
	This function is not supported under VR mode.
	


	@lv object: the ListView

	@returns: The created ListViewItem

	"""

def BCListViewItemAddChild(item):

	"""

	Appends a child item item to ListViewItem item.
	
	WARNING: If no sorting enabled in the list, the child item is appended.
	WARNING: In order to avoid performance issues, it is recommended that sorting in list is disabled on mass adding items.
	This function is not supported under VR mode.
	


	@item object: the ListViewItem

	@returns: The created ListViewItem

	"""

def BCListViewGetTopLevelItem(lv, row):

	"""

	Returns the item at row row of ListView lv.
	NOTE: If sorting is enabled the items order change.
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@row integer: the row.

	@returns: the top level ListViewItem at the given row.

	"""

def BCComboBoxSetMinimumContentsLength(cb, numChars):

	"""

	Sets the minimum number of characters that should fit into BCComboBox cb.
	If numChars is set to BCSizeAuto, the minimum width of the combobox is set to
	be equal to the largest containing string.
	NOTE: The minimum width in pixels depends on the current font used by the application.
	This function is not supported under VR mode.
	


	@cb object: the BCComboBox

	@numChars integer: the number of characters that should fit into the combobox. The default
	value is BCSizeMedium. See See BCEnumSize for details.
	
	guitk.constants BCEnumSize
	This enum type is used to define the size (minimum/fixed/maximum) of a widget, depending on the function, measured in number of characters.
	 - guitk.constants.BCSizeAuto
	the widget's size depends on its contents.
	 - guitk.constants.BCSizeSmall
	sets the widget's size to small.
	 - guitk.constants.BCSizeMedium
	sets the widget's size to medium.
	 - guitk.constants.BCSizeLarge
	sets the widget's size to large.
	 - guitk.constants.BCSizeExtraLarge
	sets the widget's size to extra large.

	"""

def BCTableSetCellsForegroundColor(t, startRow, endRow, startColumn, endColumn, r, g, b):

	"""

	Changes the foreground color (i.e. the text) of given cells of BCTable t.
	Starting and ending row/column must be a number between zero and row/column count respectively. Also, the starting row/column must be
	a number less or equal to the ending one.
	If you want to reset the color to the default one, use the function BCTableResetCellsForegroundColor().
	NOTE: This function sets the foreground color of the existing cells. Any new cells created by adding new rows/columns
	will be ignored. In case you want to keep the new color, see functions BCTableSetRowsCellsForegroundColor() and BCTableSetColumnsCellsForegroundColor().
	WARNING: This function sets the foreground color of given cells currently on the table. This means that, if previously
	BCTableSetRowsCellsForegroundColor() or BCTableSetColumnsCellsForegroundColor() has been called for those cells, on the next
	row/column addition, the foreground color of those cells will be set again to the color set by the latter functions!
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@startRow integer: the starting row

	@endRow integer: the ending row

	@startColumn integer: the starting column

	@endColumn integer: the ending column

	@r integer: the red component of the color to be set

	@g integer: the green component of the color to be set

	@b integer: the blue component of the color to be set

	"""

def BCTableResetCellsForegroundColor(t, startRow, endRow, startColumn, endColumn):

	"""

	Resets the foreground color of given cells of BCTable t.
	If no color is set, this function does nothing.
	WARNING: This function resets the foreground color of given cells currently on the table. This means that, if previously
	BCTableSetRowsCellsForegroundColor() or BCTableSetColumnsCellsForegroundColor() has been called for those cells, on the next
	row/column addition, the foreground color of those cells will be set again to the color set by the latter functions!
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@startRow integer: the starting row

	@endRow integer: the ending row

	@startColumn integer: the starting column

	@endColumn integer: the ending column

	"""

def BCTableSetRowsCellsForegroundColor(t, startRow, endRow, r, g, b):

	"""

	Sets the foreground color of cells, like BCTableSetCellsForegroundColor(), but for whole rows.
	This function, in opposition to BCTableSetCellsForegroundColor(), keeps track of the rows, so, any new cells
	added by adding new columns which belong to the range from startRow to endRow will also be colored
	with the given color.
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@startRow integer: the starting row

	@endRow integer: the ending row

	@r integer: the red component of the color to be set

	@g integer: the green component of the color to be set

	@b integer: the blue component of the color to be set

	"""

def BCTableSetColumnsCellsForegroundColor(t, startColumn, endColumn, r, g, b):

	"""

	Sets the foreground color of cells, like BCTableSetCellsForegroundColor(), but for whole columns.
	This functions does exactly what BCTableSetRowsCellsForegroundColor() does but applies for columns.
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@startColumn integer: the starting column

	@endColumn integer: the ending column

	@r integer: the red component of the color to be set

	@g integer: the green component of the color to be set

	@b integer: the blue component of the color to be set

	"""

def BCTableResetRowsCellsForegroundColor(t, startRow, endRow):

	"""

	Resets the foreground color of the cells of BCTable t found between rows from startRow to endRow.
	In opposition to BCTableResetCellsForegroundColor(), this function resets the colors and forgets the color setting.
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@startRow integer: the starting row

	@endRow integer: the ending row

	"""

def BCTableResetColumnsCellsForegroundColor(t, startColumn, endColumn):

	"""

	Resets the foreground color of the cells of BCTable t found between columns from startColumn to endColumn.
	This functions does exactly what BCTableResetRowsCellsForegroundColor() does but applies for columns.
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@startColumn integer: the starting column

	@endColumn integer: the ending column

	"""

def BCListViewHeaderSetStringRepresentation(lv, col, text):

	"""

	Set the string representation for column with index col.
	String representation text is not displayed at header section.
	It is useful for columns with no text (for example icon only) at header.
	String representation is used when regular text is empty at 
	- header menu that show/hide columns
	- filter output query bottom bar
	This function is not supported under VR mode.
	


	@lv object: the ListView.

	@col integer: the column index.

	@text string: the text to be used as string representation.

	"""

def BCButtonLineEditSetFixedPixelWidth(ble, pixels):

	"""

	Sets both the minimum and maximum width of the widget to pixels width without changing the heights.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@pixels integer: the pixels ble will occupy.

	"""

def BCLineEditSetFixedNumCharWidth(le, numChars):

	"""

	Sets both the minimum and maximum width of the widget to numChars width without changing the heights.
	This function is not supported under VR mode.
	


	@le object: the BCLineEdit.

	@numChars integer: the number of characters.

	"""

def BCSplitterSetWidgetStretchFactor(sp, w, stretch):

	"""

	Sets the size policy of the widget w to have a stretch factor of stretch.
	Initializes the relative size of the widget w with regard to their sibling widgets.
	Setting stretch to 0 will initialize the widget w to occupy minimum fixed size.
	NOTE: The stretch factor cannot change dynamically, except from 0 to positive and vice-versa (with weird results). To change the widget sizes dynamically use BCSplitterSetWidgetSizes.
	This function is not supported under VR mode.
	


	@sp object: the BCSplitter.

	@w object: the widget for which the stretch factor will be set.

	@stretch integer: the new stretch factor.

	"""

def BCTableEnableRightPressMenu(t, options):

	"""

	Sets what will be displayed in the popupmenu that is shown on right press on BCTable t.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@options integer: this parameter specifies which options will be displayed.
	The enumerators can be OR'ed (added) together. The default value is BCNoMenu.
	See BCEnumTablePopupContents for details.
	
	guitk.constants BCEnumTablePopupContents
	This enum defines the options that will be displayed in the popupmenu shown on right click on BCTable.
	 - guitk.constants.BCNoMenu
	no popup menu will be displayed.
	 - guitk.constants.BCInsertRow
	options that allow row insertion will be displayed.
	 - guitk.constants.BCInsertColumn
	options that allow column insertion will be displayed.
	 - guitk.constants.BCDeleteRow
	option that allows row deletion will be displayed.
	 - guitk.constants.BCDeleteColumn
	option that allows column deletion will be displayed.
	 - guitk.constants.BCClipboardFunctions
	cut, copy and paste options will be displayed.
	 - guitk.constants.BCAll
	all above options will be displayed.

	"""

def BCButtonLineEditSetFixedNumCharWidth(ble, numChars):

	"""

	Sets both the minimum and maximum width of the widget to numChars width without changing the heights.
	This function is not supported under VR mode.
	


	@ble object: the BCButtonLineEdit.

	@numChars integer: the number of characters.

	"""

def BCTabWidgetSetTabsClosableEnabled(tw, closable, act, funct, data):

	"""

	Sets the tabs of BCTabWidget tw to be closable according to closable.
	Setting closable to 1 makes the tabs to show a little button with 'X' icon. The tab will close or not according to
	act and the return value of funct.
	This function is not supported under VR mode.
	


	@tw object: the BCTabWidget

	@closable boolean: set this to 1 in order to show the 'X' button; 0 otherwise. By default, the 'X' button is not visible

	@act integer: the action to be taken when the 'X' button is clicked and the user function returns 1 (e.g. you can hide or delete the tab)

	@funct callback: the user function that will be called. See BC_TABWIDGET_BUTTON_SET_FUNCTION for details
	integer BC_TABWIDGET_BUTTON_SET_FUNCTION(tw, tab, data)
	The function to be called when a pixmap with a callback function is needed to be created on a tab of a BCTabWidget.
	WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
	
	Arguments
	
	tw    object    the BCTabWidget.
	tab   object    the current tab (i.e. the created widget that made tab).
	data  anything  anything that may be required in function.
	
	Return: Return 1 in case you want to run the action set; 0 otherwise.

	@data anything: any user data that will be used by funct

	"""

def BCTableRemoveRows(t, rows, numOfRows):

	"""

	Removes the rows which are stored at array rows with size numOfRows from table t.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@rows object: the array of the row indexes that will be removed.

	@numOfRows integer: the size of the array rows.

	"""

def BCTableRemoveColumns(t, cols, numOfColumns):

	"""

	Removes the columns which are stored at array cols with size numOfColumns from table t.
	This function is not supported under VR mode.
	


	@t object: the BCTable.

	@cols object: the array of the column indexes that will be removed.

	@numOfColumns integer: the size of the array cols.

	"""

def BCTableSetAboutToInsertRemoveRowsFunction(t, funct, data):

	"""

	Sets the function to be called right before rows are about to be inserted or removed.
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@funct callback: the function to call. See BC_TABLE_ABOUT_TO_INSERT_REMOVE_ROWS_FUNCTION for details.
	boolean BC_TABLE_ABOUT_TO_INSERT_REMOVE_ROWS_FUNCTION(t, indexes, count, inserted, data)
	The function to be called just before inserting or removing rows from BCTable t.
	
	Arguments
	
	t         object    the BCTable
	indexes   object    array of indexes of rows that are about to be inserted or removed. indexes is valid only for this callback function
	count     integer   the number of rows that will be inserted or removed
	inserted  boolean   1 if rows are about to be inserted; 0 otherwise
	data      anything  anything that may be required in function
	
	Return: 1 if you want to cancel the row insertion/removal; 0 for normal insertion/removal

	@data anything: (optional)any data required by function funct

	"""

def BCTableSetAboutToInsertRemoveColumnsFunction(t, funct, data):

	"""

	Sets the function to be called right before columns are about to be inserted or removed.
	This function is not supported under VR mode.
	


	@t object: the BCTable

	@funct callback: the function to call. See BC_TABLE_ABOUT_TO_INSERT_REMOVE_COLUMNS_FUNCTION for details.
	boolean BC_TABLE_ABOUT_TO_INSERT_REMOVE_COLUMNS_FUNCTION(t, indexes, count, inserted, data)
	The function to be called just before inserting or removing columns from BCTable t.
	
	Arguments
	
	t         object    the BCTable
	indexes   object    array of indexes of colunms that are about to be inserted or removed. indexes is valid only for this callback function.
	count     integer   the number of colunms that will be inserted or removed
	inserted  boolean   1 if colunms are about to be inserted; 0 otherwise
	data      anything  anything that may be required in function
	
	Return: 1 if you want to cancel the colunm insertion/removal; 0 for normal insertion/removal

	@data anything: (optional)any data required by function funct

	"""


class constants():

	BCAlignAuto = int

	BCAlignLeft = int

	BCAlignRight = int

	BCAlignHCenter = int

	BCAlignJustify = int

	BCAlignHorizontal_Mask = int

	BCAlignTop = int

	BCAlignBottom = int

	BCAlignVCenter = int

	BCAlignVJustify = int

	BCAlignVertical_Mask = int

	BCAlignCenter = int

	BCTty = int

	BCGuiClient = int

	BCGuiServer = int

	BCBorder = int

	BCNoBorder = int

	BCTopBorder = int

	BCNoBorderNoMargin = int

	BCNoButton = int

	BCLeftButton = int

	BCRightButton = int

	BCMiddleButton = int

	BCMouseButtonMask = int

	BCShiftButton = int

	BCControlButton = int

	BCAltButton = int

	BCMetaButton = int

	BCKeypad = int

	BCKeyButtonMask = int

	BCNoColumn = int

	BCAllColumns = int

	BCLastColumn = int

	BCCommitDataOtherReason = int

	BCCommitDataKeyEnterReason = int

	BCCommitDataKeyTabReason = int

	BCCommitDataKeyBackTabReason = int

	BCCaseSensitive = int

	BCBeginsWith = int

	BCEndsWith = int

	BCContains = int

	BCExactMatch = int

	BCCursorInvalid = int

	BCCursorCross = int

	BCCursorBlank = int

	BCCursorWhatsThis = int

	BCCursorWait = int

	BCCursorMouse = int

	BCCursorExclamation = int

	BCCursorArrow = int

	BCCursorSizeVer = int

	BCCursorSizeHor = int

	BCCursorSizeBDiag = int

	BCCursorSizeFDiag = int

	BCCursorSizeAll = int

	BCCursorSplitV = int

	BCCursorSplitH = int

	BCCursorPointingHand = int

	BCCursorForbidden = int

	BCCursorOpenHand = int

	BCCursorClosedHand = int

	BCCursorBusy = int

	BCCursorZoomIn = int

	BCCursorZoomOut = int

	BCCursorIBeam = int

	BCCursorUpArrow = int

	BCCursorRotate = int

	BCCursorZoomRect = int

	BCCursorZoom = int

	BCCursorPanRotateZoom = int

	BCInt = int

	BCFloat = int

	BCDouble = int

	BCString = int

	BCStringList = int

	BCBool = int

	BCInvalid = int

	BCDate = int

	BCLeftToRight = int

	BCRightToLeft = int

	BCTopToBottom = int

	BCBottomToTop = int

	BCDown = int

	BCUp = int

	BCDockAuto = int

	BCDockHorizontal = int

	BCDockVertical = int

	BCDockNone = int

	BCDockLeft = int

	BCDockRight = int

	BCDockTop = int

	BCDockBottom = int

	BCNoDrag = int

	BCCopy = int

	BCMove = int

	BCAuto = int

	BCInvalidPosition = int

	BCAboveTarget = int

	BCBelowTarget = int

	BCOnTarget = int

	BCBoth = int

	BCNone = int

	BCNormalEchoMode = int

	BCNoEchoMode = int

	BCPasswordMode = int

	BCEventNone = int

	BCEventTimer = int

	BCEventMouseButtonPress = int

	BCEventMouseButtonRelease = int

	BCEventMouseButtonDblClick = int

	BCEventMouseMove = int

	BCEventKeyPress = int

	BCEventKeyRelease = int

	BCEventFocusIn = int

	BCEventFocusOut = int

	BCEventEnter = int

	BCEventLeave = int

	BCEventPaint = int

	BCEventMove = int

	BCEventResize = int

	BCEventCreate = int

	BCEventDestroy = int

	BCEventShow = int

	BCEventHide = int

	BCEventClose = int

	BCEventQuit = int

	BCEventReparent = int

	BCEventShowMinimized = int

	BCEventShowNormal = int

	BCEventWindowActivate = int

	BCEventWindowDeactivate = int

	BCEventShowToParent = int

	BCEventHideToParent = int

	BCEventShowMaximized = int

	BCEventShowFullScreen = int

	BCEventWheel = int

	BCEventAccelerator = int

	BCEventShortcut = int

	BCEventShortcutOverride = int

	BCEventWindowEnabled = int

	BCEventWindowDisabled = int

	BCEventQuitAll = int

	BCOnExitHide = int

	BCOnExitDestroy = int

	BCEquals = int

	BCNotEquals = int

	BCContain = int

	BCNotContain = int

	BCLess = int

	BCLessOrEqual = int

	BCGreater = int

	BCGreaterOrEqual = int

	BCBetween = int

	BCOpen = int

	BCSave = int

	BCSelect = int

	BCDefaultOptions = int

	BCNoOverwriteWarning = int

	BCShowModal = int

	BCSelectFilesAndDirs = int

	BCSelectExistingFiles = int

	BCCheckForPermissions = int

	BCCheckForReadAccess = int

	BCCheckForWriteAccess = int

	BCMultiSelection = int

	BCSingleSelection = int

	BCAnyFile = int

	BCFilesOnly = int

	BCDirectory = int

	BCFilesAndDirs = int

	BCDirsOnly = int

	BCNoFocus = int

	BCTabFocus = int

	BCClickFocus = int

	BCStrongFocus = int

	BCWheelFocus = int

	BCLeftSide = int

	BCRightSide = int

	BCHorizontalCenter = int

	BCIconsFixed = int

	BCAdjust = int

	BCAutomatic = int

	BCSmall = int

	BCLarge = int

	BCOffState = int

	BCOnState = int

	BCShowIndicator = int

	BCDontShowIndicator = int

	BCDontShowIndicatorWhenChildless = int

	BCIterateAll = int

	BCIterateSelected = int

	BCIterateUnselected = int

	BCIterateVisible = int

	BCIterateHidden = int

	BCIterateFirstLevel = int

	BCBesideIcon = int

	BCBelowIcon = int

	BCHistoryOpen = int

	BCHistorySaveAs = int

	BCHistorySelect = int

	BCHistoryFolders = int

	BCHistoryFiles = int

	BCHistoryAnything = int

	BCDelayedOnSelectedClicked = int

	BCDirectOnClicked = int

	BCManagedEnable = int

	BCManagedDisable = int

	BCManagedShow = int

	BCManagedHide = int

	BCMsgWinIgnore = int

	BCMsgWinAccept = int

	BCMsgWinReject = int

	BCMsgWinCustom = int

	BCQuitAll = int

	BCEscKey = int

	BCRetKey = int

	BCNormalMode = int

	BCDisabledMode = int

	BCActiveMode = int

	BCSelectedMode = int

	BCClick = int

	BCPress = int

	BCNotOpen = int

	BCReadOnly = int

	BCWriteOnly = int

	BCReadWrite = int

	BCAppend = int

	BCTruncate = int

	BCText = int

	BCUnbuffered = int

	BCVertical = int

	BCHorizontal = int

	BCInDock = int

	BCOutsideDock = int

	BCPlot3DX = int

	BCPlot3DY = int

	BCPlot3DZ = int

	BCIdlePriority = int

	BCLowestPriority = int

	BCLowPriority = int

	BCNormalPriority = int

	BCHighPriority = int

	BCHighestPriority = int

	BCTimeCriticalPriority = int

	BCInheritPriority = int

	BCRecordingManagerFilterIncoming = int

	BCRecordingManagerFilterOutgoing = int

	BCRecursive = int

	BCNonRecursive = int

	BCRenameType_None = int

	BCRenameType_Double = int

	BCRenameType_Int = int

	BCRenameType_String = int

	BCResizeAuto = int

	BCResizeStretch = int

	BCResizeKeepSize = int

	BCResizeFollowSizeHint = int

	BCMoveModeNoRestriction = int

	BCMoveModeSameDepth = int

	BCMulti = int

	BCSingle = int

	BCNoSelection = int

	BCPlain = int

	BCSunken = int

	BCRaised = int

	BCNoFrame = int

	BCBox = int

	BCPanel = int

	BCStyledPanel = int

	BCHLine = int

	BCVLine = int

	BCGroupBoxPanel = int

	BCWinPanel = int

	BCToolBarPanel = int

	BCMenuBarPanel = int

	BCPopupPanel = int

	BCLineEditPanel = int

	BCTabWidgetPanel = int

	BCSizeAuto = int

	BCSizeSmall = int

	BCSizeMedium = int

	BCSizeLarge = int

	BCSizeExtraLarge = int

	BCFixed = int

	BCMinimum = int

	BCMaximum = int

	BCPreferred = int

	BCExpanding = int

	BCMinimumExpanding = int

	BCIgnored = int

	BCMessageBoxWarning = int

	BCMessageBoxCritical = int

	BCMessageBoxInformation = int

	BCMessageBoxQuestion = int

	BCNoMenu = int

	BCInsertRow = int

	BCInsertColumn = int

	BCDeleteRow = int

	BCDeleteColumn = int

	BCClipboardFunctions = int

	BCAll = int

	BCTableNoSelection = int

	BCTableMulti = int

	BCTableSingle = int

	BCTableContiguous = int

	BCTableSingleRow = int

	BCTableMultiRow = int

	BCPlainText = int

	BCRichText = int

	BCAutoText = int

	BCLogText = int

	BCTicksNoMarks = int

	BCTicksAbove = int

	BCTicksLeft = int

	BCTicksBelow = int

	BCTicksRight = int

	BCTicksBoth = int

	BCNothing = int

	BCCloseButton = int

	BCMaximizeButton = int

	BCMinimizeButton = int

	BCValidatorNone = int

	BCValidatorInt = int

	BCValidatorDouble = int

	BCWidgetStateNone = int

	BCWidgetStateInformation = int

	BCWidgetStateWarning = int

	BCWidgetStateError = int

	BCWidgetStateReadOnly = int

	BCManualMode = int

	BCMaximumMode = int

	BCNoWrap = int

	BCWidgetWidth = int

	BCFixedPixelWidth = int

	BCFixedColumnWidth = int

	BCManualWrap = int

	BCWordWrap = int

	BCWrapAnywhere = int

	BCWrapAtWordBoundaryOrAnywhere = int

	blank = int
