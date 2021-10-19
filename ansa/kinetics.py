def CalculateMassProperties(entity):

	"""

	Calculates the mass of KIN_RBODY.


	@entity object: The ANSA entity (type KIN_RBODY), whose mass will be calculated.

	@returns integer: Returns 1 on success and 0 if an invalid entity is given.
	If the KIN_RBODY has type GROUND, then the mass can't be calculated
	(the return value will be 1 and a message will be printed).

	"""

def Dz(to_marker, from_marker, along_marker):

	"""

	Gets the distance from 'from_marker' to 'to_marker' in the Z direction, along the 'along_marker'.


	@to_marker string: The name or the id of the 'to_marker'.

	@from_marker string: (optional)The name or the id of the 'from_marker'.

	@along_marker string: (optional)The name or the id of the 'along_marker'.

	@returns float: Returns the distance along Z (scalar).

	"""

def Dm(to_marker, from_marker):

	"""

	Gets the magnitude of the translational displacement vector from 'from_marker' to 'to_marker'.


	@to_marker string: The name or the id of the 'to_marker'.

	@from_marker string: (optional)The name or the id of the 'from_marker'.

	@returns float: Returns the magnitude of the distance (scalar).

	"""

def Ax(to_marker, from_marker):

	"""

	Gets the rotational displacement (in radians) of 'to_marker' about the x-axis of 'from_marker', 
	and accounts for angle wrapping.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@returns float: Returns the rotational displacement (in radians) about x-axis of 'from_marker' (scalar).

	"""

def Ay(to_marker, from_marker):

	"""

	Gets the rotational displacement (in radians) of 'to_marker' about the y-axis of 'from_marker', and accounts for angle wrapping.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@returns float: Returns the rotational displacement (in radians) about y-axis of 'from_marker' (scalar).

	"""

def Az(to_marker, from_marker):

	"""

	Gets the rotational displacement (in radians) of 'to_marker' about the z-axis of 'from_marker', and accounts for angle wrapping.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@returns float: Returns the rotational displacement (in radians) about z-axis of 'from_marker' (scalar).

	"""

def Vx(to_marker, from_marker, along_marker, reference_marker):

	"""

	Gets the velocity from 'from_marker' to 'to_marker' in the X direction, along the 'along_marker'.
	All velocities are taken in the 'reference_marker' coordinate system. 


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@along_marker string: (optional)Name or id of the 'along_marker'.

	@reference_marker string: (optional)Name or id of the 'reference_marker'.

	@returns float: Returns the velocity along X (scalar).

	"""

def Vy(to_marker, from_marker, along_marker, reference_marker):

	"""

	Gets the velocity from 'from_marker' to 'to_marker' in the Y direction, along the 'along_marker'.
	All velocities are taken in the 'reference_marker' coordinate system.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@along_marker string: (optional)Name or id of the 'along_marker'.

	@reference_marker string: (optional)Name or id of the 'reference_marker'.

	@returns float: Returns the velocity along Y (scalar).

	"""

def Vz(to_marker, from_marker, along_marker, reference_marker):

	"""

	Gets the velocity from 'from_marker' to 'to_marker' in the Z direction, along the 'along_marker'.
	All velocities are taken in the 'reference_marker' coordinate system. 


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@along_marker string: (optional)Name or id of the 'along_marker'.

	@reference_marker string: (optional)Name or id of the 'reference_marker'.

	@returns float: Returns the velocity along Z (scalar).

	"""

def Vm(to_marker, from_marker, reference_marker):

	"""

	Gets the magnitude of the velocity from 'from_marker' to 'to_marker'.
	All velocities are taken in the 'reference_marker' coordinate system. 


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@reference_marker string: (optional)Name or id of the 'reference_marker'.

	@returns float: Returns the velocity magnitude (scalar).

	"""

def Vr(to_marker, from_marker, reference_marker):

	"""

	Gets the radial (separation) velocity from 'from_marker' to 'to_marker'.
	All velocities are taken in the 'reference_marker' coordinate system.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@reference_marker string: (optional)Name or id of the 'reference_marker'.

	@returns float: Returns the radial (separation) velocity (scalar).

	"""

def Wx(to_marker, from_marker, about_marker):

	"""

	Gets the angular velocity from 'from_marker' to 'to_marker' about the X direction of the 'about_marker'.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@about_marker string: (optional)Name or id of the 'about_marker'.

	@returns float: Returns the angular velocity about X (scalar).

	"""

def Wy(to_marker, from_marker, about_marker):

	"""

	Gets the angular velocity from 'from_marker' to 'to_marker' about the Y direction of the 'about_marker'.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@about_marker string: (optional)Name or id of the 'about_marker'.

	@returns float: Returns the angular velocity about Y (scalar).

	"""

def Wz(to_marker, from_marker, about_marker):

	"""

	Gets the angular velocity from 'from_marker' to 'to_marker' about the Z direction of the 'about_marker'.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@about_marker string: (optional)Name or id of the 'about_marker'.

	@returns float: Returns the angular velocity about Z (scalar).

	"""

def Wm(to_marker, from_marker):

	"""

	Gets the magnitude of the angular velocity from 'from_marker' to 'to_marker'.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@returns float: Returns the angular velocity magnitude (scalar).

	"""

def Time():

	"""

	Gets the current simulation time.


	@returns float: Returns the current simulation time (scalar).

	"""

def Mode():

	"""

	Gets the analysis mode.


	@returns float: Returns an integer defining the Analysis mode:
	
	1, For Kinematics analysis.
	3, For IC.
	4, For Dynamics.
	5, For Static equilibrium.

	"""

def AddBodyToContact(kin_contact, kin_body):

	"""

	This function adds a kinetic rigid body (KIN_RBODY) to a kinetic contact (KIN_CONTACT).


	@kin_contact object: The ANSA entity (KIN_CONTACT) that the kinetic rigid body will be added to.

	@kin_body object: The ANSA entity (KIN_RBODY) to be added to the kinetic contact.

	@returns integer: Returns 1 on success.
	An exception is raised if invalid entities are given.

	"""

def FindContact(kin_contact):

	"""

	This function checks collision of given kinetic contact (KIN_CONTACT) and
	returns contacts (points, normal vectors and penetration depth).
	Number of contacts found is printed in ANSA Info & command line.


	@kin_contact object: ANSA entity (KIN_CONTACT) to find contacts.

	@returns object: Returns a tuple of five lists (each of length equal to the number of contacts found):
	1st list element: point (belongs to one of the elements where contact was found).
	2nd list element: normal vector for point of 1st list.
	3rd list element: point (belongs to the other element where contact was found).
	4th list element: normal vector for point of 3rd list.
	5th list element: penetration depth (distance of points of 1st & 3rd list).
	For each contact found an element is added to each list.
	An exception is raised if invalid entity is given.

	"""

def SaveAsInitialPosition(initialize_joints):

	"""

	Saves the current position of the model as initial position.


	@initialize_joints boolean: (optional)True to initialize the Kinetic Joints' displacements to zero or False to not. 
	By default is False.

	@returns integer: Returns 1 on success.

	"""

def MoveToInitialPosition():

	"""

	Moves the model to its initial position.


	@returns integer: Always returns 1.

	"""

def SavePosition(kin_config, name):

	"""

	Saves the current position as KIN_POSITION entity with the given name.


	@kin_config object: (optional)The KIN_CONFIG object, whose bodies' positions will be saved.
	If omitted all bodies' positions will be saved.

	@name string: (optional)The name of the KIN_POSITION entity that will be created.

	@returns object: Returns a reference to the newly created KIN_POSITION object.

	"""

def MoveToPosition(kin_pos):

	"""

	Moves the model to a given position.


	@kin_pos object: The KIN_POSITION entity where the model will be moved to.

	@returns integer: Returns 1 on success.
	An exception is thrown if an invalid entity is given (not KIN_POSITION).

	"""

def MoveByResults(kin_results, time):

	"""

	Move the model by the given kin_results to the given time.


	@kin_results object: The 'KIN_RESULTS' entity where data will be extracted from.

	@time float: (optional)Move to given time. The model will be moved to the iteration 
	step of the simulation, whose reference time is closest to the given time.
	If omitted, the model will be moved to the last iteration of KIN_RESULTS.

	@returns float: Returns a float representing the actual time the model moved to (see time argument above).
	An exception is thrown if invalid KIN_RESULTS entity is given or invalid time 
	(negative or greater than maximum time of KIN_RESULTS).

	"""

def ResultsWriteToXML(kin_result, file_name, output_adams_view, adams_name):

	"""

	Exports (writes) the contents of a KIN_RESULTS entity to a XML file.


	@kin_result object: A kinetics result solver.

	@file_name string: The filepath for the output.

	@output_adams_view boolean: (optional)True to output the related ADAMS/View Command file or False to not. 
	By default is False.

	@adams_name boolean: (optional)Modifies the kinematic entities names according to adams hierarchy rules. 
	The default option is defined in ANSA Defaults.

	@returns integer: Returns 1 on success, 0 otherwise.

	"""

def TableCreate(name,interpolation,items):

	"""

	Creates a KIN_TABLE entity and sets the table values.


	@name string: The name of the KIN_TABLE.

	@interpolation string: The type of the interpolation. Can be 'linear', 'cubic' or 'akima'.

	@items object: A list with the table data.

	@returns object: Returns the created KIN_TABLE on success, 0 otherwise.

	"""

def TableSetData(entity, items):

	"""

	Sets the data of a KIN_TABLE. Will overwrite the data using the new list.


	@entity object: A reference to a KIN_TABLE.

	@items object: A list with the table data.

	@returns integer: Returns 1 on success, 0 otherwise.

	"""

def TableGetData(entity):

	"""

	Retrieves tha data from a KIN_TABLE.


	@entity object: A reference to a KIN_TABLE.

	@returns object: Returns the KIN_TABLE data as a list on success.
	Returns an empty list otherwise.

	"""

def ResultsGetData(res_entity, kin_entity):

	"""

	Gets the results for a kinetics entity from a KIN_RESULTS entity.


	@res_entity object: A KIN_RESULTS entity.

	@kin_entity object: The kinetics entity for which we need the results.

	@returns object: Returns a dictionary with the results of the selected entity.
	If no results are found, the dictionary will be empty.

	"""

def MotionDefine(entity, position1, position2, direction1, direction2, along_x, along_y, along_z, about_x, about_y, about_z, function_dx, function_dy, function_dz, function_rx, function_ry, function_rz, disp_ic_dx, disp_ic_dy, disp_ic_dz, disp_ic_rx, disp_ic_ry, disp_ic_rz, vel_ic_dx, vel_ic_dy, vel_ic_dz, vel_ic_rx, vel_ic_ry, vel_ic_rz):

	"""

	Defines the data of a KIN_MOTION entity. This might be an already existing KIN_MOTION entity, 
	or one that will be created according to the entities given to the 'entity' argument.


	@entity object: Alternative argument:
	a) Reference to a KIN_MOTION entity, whose motion data will be set.
	b) Reference to a KIN_JOINT entity, from which a KIN_MOTION
	   entity will be created and then its motion data will be set.
	c) A sequence (list or tuple) of two (2) KIN_BODYs, from which a KIN_MOTION
	   entity will be created and then its motion data will be set.

	@position1 object: (optional)A sequence (list or tuple) of three(3) floats to determine the position
	 of the 1st marker.

	@position2 object: (optional)A sequence (list or tuple) of three(3) floats to determine the position 
	of the 2nd marker.

	@direction1 object: (optional)A sequence (list or tuple) of three(3) floats to determine the direction 
	of the 1st marker.

	@direction2 object: (optional)A sequence (list or tuple) of three(3) floats to determine the direction 
	of the 2nd marker.

	@along_x string: (optional)'DISP', 'VEL' or 'ACC' to set the x translational motion to 
	the prescribed displacement, velocity or acceleration.

	@along_y string: (optional)'DISP', 'VEL' or 'ACC' to set the y translational motion to 
	the prescribed displacement, velocity or acceleration.

	@along_z string: (optional)'DISP', 'VEL' or 'ACC' to set the z translational motion to 
	the prescribed displacement, velocity or acceleration.

	@about_x string: (optional)'DISP', 'VEL' or 'ACC' to set the x rotational motion to the
	prescribed (rotational) displacement, velocity or acceleration.

	@about_y string: (optional)'DISP', 'VEL' or 'ACC' to set the y rotational motion to the
	prescribed (rotational) displacement, velocity or acceleration.

	@about_z string: (optional)'DISP', 'VEL' or 'ACC' to set the z rotational motion to the
	prescribed (rotational) displacement, velocity or acceleration.

	@function_dx string: (optional)The function for x translational motion.

	@function_dy string: (optional)The function for y translational motion.

	@function_dz string: (optional)The function for x translational motion.

	@function_rx string: (optional)The function for x rotational motion.

	@function_ry string: (optional)The function for y rotational motion.

	@function_rz string: (optional)The function for z rotational motion.

	@disp_ic_dx float: (optional)The x component of displacement initial condition.

	@disp_ic_dy float: (optional)The y component of displacement initial condition.

	@disp_ic_dz float: (optional)The z component of displacement initial condition.

	@disp_ic_rx float: (optional)The x component of rotational initial condition.

	@disp_ic_ry float: (optional)The y component of rotational initial condition.

	@disp_ic_rz float: (optional)The z component of rotational initial condition.

	@vel_ic_dx float: (optional)The x component of initial translational velocity.

	@vel_ic_dy float: (optional)The y component of initial translational velocity.

	@vel_ic_dz float: (optional)The z component of initial translational velocity.

	@vel_ic_rx float: (optional)The x component of initial rotational velocity.

	@vel_ic_ry float: (optional)The y component of initial rotational velocity.

	@vel_ic_rz float: (optional)The z component of initial rotational velocity.

	@returns object: -If a new KIN_MOTION entity was created (cases b and c of entity - 1st argument)
	 a reference to it is returned.
	-Otherwise (case a of entity - 1st argument), returns 1 on success.
	 
	In either case, if an error occurred during motion data setup, an exception is thrown.

	"""

def AddToRigidBody(body, elements, remove_from_other_body):

	"""

	This function adds an element or a list of elements as part of rigid body.


	@body object: The rigid body where the given element will be added to.

	@elements object: A list of elements to be added in the rigid body.

	@remove_from_other_body boolean: (optional)True to remove the added element(s) from the original rigid body (if any) 
	or False to not. By default is False.

	@returns integer: Returns 0 if the element/list of elements was added to BODY. 
	Otherwise, if BODY is invalid, the function returns 1.

	"""

def RemoveFromRigidBody(body, elements):

	"""

	This function removes an element or a list of elements which is or are part of a rigid body.


	@body object: The rigid body that the given element/list of elements will be removed from.

	@elements object: The element or a list of elements to remove from the rigid body.

	@returns integer: Returns 0 if the element/list of elements was removed from the BODY.
	If body is invalid, the function returns 1.
	If element/list of elements is invalid, the return value is 2.

	"""

def ConvertToTransformation(CONFIG, POSITION):

	"""

	This function relates the current position of a given Kinematic Configuration to another Kinematic Position.


	@CONFIG object: A Kinematic Configuration whose current position is to be 
	related to POSITION.

	@POSITION object: The name of the Kinematic Position that CONFIG's current 
	position is to be related. If "Reference Position" is given as the 
	second argument, the CONFIG's current position is related to the 
	reference position.

	@returns integer: Returns 0 if the transformation was calculated successfully.
	In all other cases, it may return the following 
	error codes:
	1 - CONFIG is not a Kinematic Configuration entity.
	2 - CONFIG is invalid.
	3 - POSITION was not found among existing Kinematic Position.

	"""

def SetJointStatus(JOINT, STATUS):

	"""

	This function sets the current status of a kinematic joint entity to either "LOCKED", or "UNLOCKED".
	The status of a newly created joint is set to "UNLOCKED".


	@JOINT object: The reference to the kinematic joint whose status is to be set.

	@STATUS string: Defines the desired status ("LOCKED" or "UNLOCKED").

	@returns string: Returns '0' if the joint's status was altered successfully.
	Returns '1' if JOINT is invalid,'2' if JOINT is not actually a joint entity, 
	'3' if the given STATUS is neither "LOCKED" nor "UNLOCKED" and '4' if the 
	STATUS argument was not a string.

	"""

def AddConfigToConfig(PARENT, CHILD):

	"""

	This function adds a kinematic configuration as child to another
	kinematic configuration. In order for the operation to succeed, CHILD
	must not be already contained to PARENT. CHILD is considered to be
	contained in PARENT, if ANY of the Kinematic Joints and Kinematic
	Configurations that CHILD contains, are already contained in PARENT
	or in any Kinematic Configuration that contains PARENT.


	@PARENT object: A kinematic configuration object.

	@CHILD object: The kinematic configuration to be added to PARENT.

	@returns integer: Returns 0 if CHILD was added to PARENT.
	If PARENT does not exist, the function returns 1.
	If PARENT exists, but CHILD doesn't, the function returns 2.
	Finally, if CHILD cannot be added to PARENT, the return value is 3.

	"""

def AddJointToConfig(CONFIG, JOINT):

	"""

	This function adds a kinematic joint to a kinematic configuration. In
	order for the operation to succeed, JOINT must not be already
	contained in CONFIG. JOINT is considered to be contained in CONFIG if
	it is one of its kinematic joints or it is contained in any kinematic
	hierarchy that also contains CONFIG.


	@CONFIG object: A kinematic configuration entity, where a kinematic joint will be added to.

	@JOINT object: The kinematic joint element to be added to the CONFIG.

	@returns integer: Returns 0 if JOINT was added to CONFIG.
	If CONFIG does not exist, the function returns 1.
	If CONFIG exists, but JOINT doesn't, the function returns 2.
	Finally, if JOINT cannot be added to CONFIG, the return value is 3.

	"""

def MoveConfig():

	"""

	This function performs the actual motion of a kinematic configuration.
	The motion parameters must be set by calling the function ConfigSetParameters, before calling this function.


	@returns object: If the argument move_method of the function ConfigSetParameters is 'BY JOINT' or 'BY ACTUATOR JOINT', 
	then this function returns a 6-entries list with the amount of the performed movement for each 
	dof (the first 3 entries correspond to the translational dofs and the last 3 to the rotational ones).
	If the argument move_method of the function ConfigSetParameters is 'BY TIME' or 'BY MATCHING POINTS',
	then this function returns 1 on success.
	The function returns 0 on failure for all move methods.

	"""

def ConfigSetParameters(kin_config, move_method, kin_joint, displacement, angle, translate_x, translate_y, translate_z, rotate_x, rotate_y, rotate_z, sp, tp, motor_joint, end_time, start_at_equilibrium, step_size_type, step_size, number_of_steps, results_file, max_step_size, translate_x_total, translate_y_total, translate_z_total, rotate_x_total, rotate_y_total, rotate_z_total, displacement_total, angle_total, lock_translate_x, lock_translate_y, lock_translate_z, lock_rotate_x, lock_rotate_y, lock_rotate_z):

	"""

	This function performs the setup of the kinematic parameters for kinematic configuration motion.


	@kin_config integer: The id of the kinematic configuration element that motion is to be applied.
	ANSA SETs to apply mass on.

	@move_method string: One of: "BY JOINT", "BY MATCHING POINTS", "BY ACTUATOR JOINT" or "BY TIME".
	Apply motion to a kinematic joint of a kinematic configuration
	or move a kinematic configuration by matching points or move 
	a kinematic configuration by the actuator joint or move a 
	kinematic configuration by time.

	@kin_joint integer: The id of the kinematic joint of the kinematic configuration 
	that motion is to be applied.

	@displacement float: Amount of translation to be applied to a kinematic joint. 
	Valid only if move_method = "BY JOINT" or "BY ACTUATOR JOINT" 
	and the joint has a translational dof.

	@angle float: Amount of rotation to be applied to a kinematic joint. 
	Valid only if move_method = "BY JOINT" or "BY ACTUATOR JOINT"
	and the joint has a rotational dof.

	@translate_x float: Translation in 'X' axis.

	@translate_y float: Translation in 'Y' axis.

	@translate_z float: Translation in 'Z' axis.

	@rotate_x float: Rotation about 'X' axis.

	@rotate_y float: Rotation about 'Y' axis.

	@rotate_z float: Rotation about 'Z' axis.

	@sp object: Either the id of a node to be used as a source point or an ANSA entity. 
	Valid only if move_method = "BY MATCHING POINTS".
	The node must belong to a rigid body.

	@tp object: Either the id of a node to be used as a target point or an ANSA entity.
	Valid only if move_method = "BY MATCHING POINTS".

	@motor_joint integer: The id of the kinematic joint that will be set 
	as the actuator joint of the kinematic configuration 
	(optional). If another kinematic joint is already 
	defined as the actuator joint of the kinematic 
	configuration, this parameter will override the 
	previous selection. Valid only if 
	move_method = "BY ACTUATOR JOINT".

	@end_time float: Total simulation time.
	Valid only if move_method = "BY TIME".

	@start_at_equilibrium boolean: Valid only if move_method = "BY TIME".

	@step_size_type string: One of: "NONE", "SIZE" or "NUMBER".
	Valid only if move_method = "BY TIME".

	@step_size float: Valid only if move_method = "BY TIME" and
	step_size_type = "SIZE"

	@number_of_steps integer: Valid only if move_method = "BY TIME" and 
	step_size_type = "NUMBER".

	@results_file string: Desired file name (*.xml).
	Valid only if move_method = "BY TIME".

	@max_step_size float: Maximum step size of HHT-I3 Solver.

	@translate_x_total float: Translation in 'X' axis (total).

	@translate_y_total float: Translation in 'Y' axis (total).

	@translate_z_total float: Translation in 'Z' axis (total).

	@rotate_x_total float: Rotation about 'X' axis (total).

	@rotate_y_total float: Rotation about 'Y' axis (total).

	@rotate_z_total float: Rotation about 'Z' axis (total).

	@displacement_total float: Total amount of translation to be applied to a kinematic joint.
	Valid only if "MOVE METHOD" = "BY JOINT" or "BY ACTUATOR JOINT"
	and the joint has a translational dof.

	@angle_total float: Total amount of rotation to be applied to a kinematic joint. 
	Valid only if "MOVE METHOD" = "BY JOINT" or "BY ACTUATOR JOINT"
	and the joint has a rotational dof.

	@lock_translate_x boolean: (optional)Lock translational component X of actuator joint.
	Valid only if "MOVE METHOD" = "BY ACTUATOR JOINT".
	(Default: False)

	@lock_translate_y boolean: (optional)Lock translational component Y of actuator joint.
	Valid only if "MOVE METHOD" = "BY ACTUATOR JOINT".
	(Default: False)

	@lock_translate_z boolean: (optional)Lock translational component Z of actuator joint.
	Valid only if "MOVE METHOD" = "BY ACTUATOR JOINT".
	(Default: False)

	@lock_rotate_x boolean: (optional)Lock rotational component X of actuator joint.
	Valid only if "MOVE METHOD" = "BY ACTUATOR JOINT".
	(Default: False)

	@lock_rotate_y boolean: (optional)Lock rotational component Y of actuator joint.
	Valid only if "MOVE METHOD" = "BY ACTUATOR JOINT".
	(Default: False)

	@lock_rotate_z boolean: (optional)Lock rotational component Z of actuator joint.
	Valid only if "MOVE METHOD" = "BY ACTUATOR JOINT".
	(Default: False)

	@returns integer: Returns 0 on success.
	An exception is thrown if more than one motions are specified for method BY JOINT or BY ACTUATOR JOINT.

	"""

def MotionGetData(entity):

	"""

	Collects all Motion Data from the KIN_MOTION entity.


	@entity object: The KIN_MOTION entity.

	@returns object: Returns a dictionary with the following keys:
	along_x, along_y, along_z,
	about_x, about_y, about_z,
	function_dx, function_dy, function_dz,
	function_rx, function_ry, function_rz,
	disp_ic_dx, disp_ic_dy, disp_ic_dz,
	disp_ic_rx, disp_ic_ry, disp_ic_rz,
	vel_ic_dx, vel_ic_dy, vel_ic_dz,
	vel_ic_rx, vel_ic_ry, vel_ic_rz.

	"""

def RemoveBodyFromContact(kin_contact, kin_body):

	"""

	This function removes a KIN_RBODY from a KIN_CONTACT entity.


	@kin_contact object: The KIN_CONTACT entity that the given KIN_RBODY will be removed from.

	@kin_body object: The KIN_RBODY entity to remove from the KIN_CONTACT.

	@returns integer: Returns 1 on success.
	An exception is raised if either entity is not valid.

	"""

def GetBodiesFromContact(kin_contact):

	"""

	This function returns a list of KIN_RBODYs included in the given KIN_CONTACT.


	@kin_contact object: The KIN_CONTACT whose KIN_RBODYs are requested.

	@returns object: Returns a list containing the requested KIN_RBODY entities, on success. 
	If none of them are included in the defined KIN_CONTACT, the function returns an empty list.
	An exception is raised if the argument is invalid.

	"""

def AddExcludedToContact(kin_contact, elements):

	"""

	This function adds the given elements as excluded to the given KIN_CONTACT.


	@kin_contact object: The KIN_CONTACT entity where elements will be added as excluded.

	@elements object: A list of ANSA entities to be added as excluded to the KIN_CONTACT.

	@returns integer: Returns 1 on success. An exception is raised if either argument is invalid 
	(KIN_CONTACT & list). If any of the list items is not a valid, a warning message 
	is printed, but the procedure is continued.

	"""

def ClearContact(kin_contact, only_excluded):

	"""

	This functions clears all the entities of a KIN_CONTACT entity, or clears only the exluded entities.
	NOTICE: the KIN_CONTACT entity is not deleted.


	@kin_contact object: The KIN_CONTACT entity, whose entities will be removed.

	@only_excluded boolean: (optional)If True, the function clears only the excluded entities.

	@returns integer: Returns 1 on success.
	An exception is raised if kin_contact (1st argument) is invalid.

	"""

def ContactBodySetData(kin_contact, kin_body, shape, thickness, thickness_scale, smooth_subdiv_lev, smooth_feat_ang):

	"""

	This function sets the KIN_RBODY's data in a KIN_CONTACT, such as shape, thickness etc.


	@kin_contact object: A reference to a 'KIN_CONTACT" object, where the "KIN_RBODY" belongs.

	@kin_body object: A reference to the "KIN_RBODY" object, whose data will be modified.

	@shape string: (optional)The "KIN_RBODY" shape.
	Can be on eof the following:
	"Simplified Concave", "Convex", "Box", "Cylinder", 
	"Sphere", "Smooth" or "Concave".

	@thickness float: (optional)The thickness (like with ~ from GUI).

	@thickness_scale float: (optional)The thickness scale (like with no ~ from GUI).

	@smooth_subdiv_lev integer: (optional)Subdivision level for smooth shape (between 1 and 10).

	@smooth_feat_ang float: (optional)Feature angle for smooth shape (between 0 and 180).

	@returns integer: Returns 1 on success.
	An exception is raised if any argument has invalid type or invalid values, 
	or if KIN_RBODY does not belong to KIN_CONTACT.

	"""

def GetModelInfo( kin_config ):

	"""

	Gets the model info of Configurator or Whole Model.


	@kin_config object: (optional)A KIN_CONFIG entity.
	If omitted the whole model is assumed.

	@returns object: This function returns a dictionary with keywords:
	    "rigid_bodies"              : number of Rigid Bodies
	    "joints"                    : number of Joints
	    "dependent_body_dofs"       : number of Dependent Body Dofs
	    "dependent_constraint_dofs" : number of Dependent Constraint Dofs
	    "redundant constraints"     : number of Redundant Constraints
	    "independent_constraints"   : number of Independent Constraints
	    "dofs"                      : number of Dofs
	    "dofs_augment"              : number of Dofs (augment)
	
	An exception is raised if an invalid entity is given.

	"""

def GetJointsFromConfig(kin_config):

	"""

	This function returns a list of KIN_JOINTs included in the given KIN_CONFIG.


	@kin_config object: The KIN_CONFIG whose KIN_JOINTs are requested.

	@returns object: Returns a list containing references to the KIN_JOINT objects found.

	"""

def RemoveJointFromConfig(kin_config, kin_joint):

	"""

	Removes a KIN_JOINT from a KIN_CONFIG.


	@kin_config object: The KIN_CONFIG object.

	@kin_joint object: The KIN_JOINT to be removed from the KIN_CONFIG.

	@returns integer: Returns 1 on success.

	"""

def ConfigsJointSetStatus(kin_config, kin_joint, locked):

	"""

	Sets the status (locked/unlocked) of a "KIN_JOINT" in a "KIN_CONFIG".


	@kin_config object: A reference to the "KIN_CONFIG" object.

	@kin_joint object: A reference to the "KIN_JOINT" object of the "KIN_CONFIG", 
	to set its status as locked or unlocked.

	@locked boolean: True: Set status as locked.
	False: Set status as unlocked.

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def ConfigsJointIsLocked(kin_config, kin_joint):

	"""

	Checks if KIN_JOINT of KIN_CONFIG is locked.


	@kin_config object: A reference to the "KIN_CONFIG" object to check.

	@kin_joint object: A reference to the "KIN_JOINT" object of the defined "KIN_CONFIG".

	@returns boolean: Returns True if "KIN_JOINT" of "KIN_CONFIG" is locked, False otherwise.

	"""

def AddForceToConfig(CONFIG, FORCE):

	"""

	This function adds a kinematic force to a kinematic configuration. In
	order for the operation to succeed, FORCE must not be already
	contained in CONFIG. FORCE is considered to be contained in CONFIG if
	it is one of its kinematic forces or it is contained in any kinematic
	hierarchy that also contains CONFIG.


	@CONFIG object: A kinematic configuration entity that a kinematic force will be added to.

	@FORCE object: The kinematic force to be added to the CONFIG.

	@returns integer: Returns 0 if FORCE was added to CONFIG.
	If CONFIG does not exist, the function returns 1.
	If CONFIG exists, but FORCE doesn't, the function returns 2.
	Finally, if FORCE cannot be added to CONFIG, the return value is 3.

	"""

def ConvertPosition(position, conversion_type, output_directory, locations_type, velocities_type, sets_type, use_position_name, position_prefix_name, include_transform_file_name, include_trasform_full_path_names, morph_nodes_file_name, output_kinetics, deformed_bodies, include_transform_enable_file, morph_nodes_enable_file, output_parameters, parameters_file_name, reference_position, output_foam_ref_geom):

	"""

	The function performs the conversion of Rigid Bodies locations and initial velocities 
	to keywords that are written in deck files. It also takes into account possible 
	deformed bodies through the Dummy Seat depenetration tool as long as the corresponding 
	nodes hold initial foam keywords, and also possible morphed nodes that have been 
	produced through the Kinematics-Morph coupling of ANSA.


	@position object: The KIN_POSITION object or list of objects.

	@conversion_type string: The conversion type.
	Available options: 'locations', 'velocities', 'both'.

	@output_directory string: The directory where the files will be written out.

	@locations_type string: (optional)The available options are:
	LS-DYNA:  '*DEFINE_TRANSFORMATION', '*NODE'
	PAMCRASH: 'TRSFM /', 'NODE /'.
	ABAQUS:   '*NMAP', '*NODE'
	RADIOSS:  '/TRANSFORM', '/NODE'.
	The default option is defined in ANSA Defaults.

	@velocities_type string: (optional)The available options are:
	LSDYNA: '*INITIAL_VELOCITY_SET', 
	        '*INITIAL_VELOCITY_GENERATION',
	        '*INITIAL_VELOCITY_NODE'.
	PAMCRASH: 'INVEL_SET /', 'INVEL_RIGID /', 'INVEL_NODE /'.
	ABAQUS: 'ROTVEL,SET', 'ROTATING_VELOCITY', 'ROTVEL,NODE'.
	RADIOSS: '/INIVEL_SET', '/INIVEL_NODE'.
	The default option is defined in ANSA Defaults.

	@sets_type string: (optional)The available options are:
	LSDYNA: '*SET_NODE_LIST', '*SET_NODE_GENERAL'.
	PAMCRASH: 'NODE', 'GENERAL'.
	The default option is defined in ANSA Defaults.

	@use_position_name boolean: (optional)Use Position's name as prefix for the created file. 
	The default option is defined in ANSA Defaults.

	@position_prefix_name string: (optional)The prefix to be used for the created file.
	The default option is defined in ANSA Defaults.

	@include_transform_file_name string: (optional)LSDYNA: The name of the separate file to write out
	the *INCLUDE_TRANSFORM keywords. 
	The default option is defined in ANSA Defaults.

	@include_trasform_full_path_names boolean: (optional)LSDYNA: If a Rigid Body contains an *INCLUDE, 
	the corresponding *INCLUDE_TRANSFORM that 
	is going to be created will written out by using 
	its FullPathName.
	The default option is defined in ANSA Defaults.

	@morph_nodes_file_name string: (optional)The name of the separate file to write out the 
	morphed nodes.
	The default option is defined in ANSA Defaults.

	@output_kinetics boolean: (optional)Output as ANSA comments the participating 
	Kinetic entities.
	The default option is defined in ANSA Defaults.

	@deformed_bodies object: (optional)A list that contains the names of the Rigid 
	Bodies that have been deformed through
	the Dummy-Seat Depenetration tool and 
	their nodes hold initial foam keywords.
	For each of those nodes a set will be written 
	out and the corresponding transformation keyword.

	@include_transform_enable_file boolean: (optional)LSDYNA: Output *INCLUDE_TRANSFORM 
	keywords in a separate file. In case there are 
	Rigid Bodies that contain *INCLUDEs.
	The default option is defined in ANSA Defaults.

	@morph_nodes_enable_file boolean: (optional)Output Morphed Nodes in a separate file.
	The default option is defined in ANSA Defaults.

	@output_parameters boolean: (optional)Output parameters for transformation keywords values.
	The default option is defined in ANSA Defaults.

	@parameters_file_name string: (optional)The name of the separate file to write out the parameters.
	The default option is defined in ANSA Defaults.

	@reference_position object: (optional)The reference position object. The conversion will be done
	relative to this.

	@output_foam_ref_geom boolean: (optional)LSDYNA: Output *INITIAL_FOAM_REFERENCE_GEOMETRY keywords. 
	The default option is defined in ANSA Defaults.

	@returns integer: Returns 1 on success, 0 on failure.

	"""

def Dy(to_marker, from_marker, along_marker):

	"""

	Gets the distance from 'from_marker' to 'to_marker' in the Y direction, along the 'along_marker'.


	@to_marker string: The name or the id of the 'to_marker'.

	@from_marker string: (optional)The name or the id of the 'from_marker'.

	@along_marker string: (optional)The name or the id of the 'along_marker'.

	@returns float: Returns the distance along Y (scalar).

	"""

def Yaw(to_marker, from_marker):

	"""

	Gets the first angle of a body-fixed 3-2-1 (yaw-pitch-roll) Euler rotation sequence 
	from the coordinate system of 'from_marker' to the coordinate system of 'to_marker'.


	@to_marker string: The name or the id of the 'to_marker'.

	@from_marker string: (optional)The name or the id of the 'from_marker'.

	@returns float: Returns the first angle of a body-fixed 3-2-1 (yaw-pitch-roll) Euler rotation sequence (scalar).

	"""

def Pitch(to_marker, from_marker):

	"""

	Gets the second angle of a body-fixed 3-2-1 (yaw-pitch-roll) Euler rotation sequence from the coordinate 
	system of 'from_marker' to the coordinate system of 'to_marker'.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@returns float: Returns the second angle of a body-fixed 3-2-1 (yaw-pitch-roll) Euler rotation sequence (scalar).

	"""

def Roll(to_marker, from_marker):

	"""

	Gets the third angle of a body-fixed 3-2-1 (yaw-pitch-roll) Euler rotation sequence from the coordinate 
	system of 'from_marker' to the coordinate system of 'to_marker'.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@returns float: Returns the third angle of a body-fixed 3-2-1 (yaw-pitch-roll) Euler rotation sequence (scalar).

	"""

def Psi(to_marker, from_marker):

	"""

	Gets the first angle of a body-fixed 3-1-3 Euler rotation sequence from the coordinate 
	system of 'from_marker' to the coordinate system of 'to_marker'.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@returns float: Returns the first angle of a body-fixed 3-1-3 Euler rotation sequence (scalar).

	"""

def Theta(to_marker, from_marker):

	"""

	Gets the second angle of a body-fixed 3-1-3 Euler rotation sequence from the coordinate 
	system of 'from_marker' to the coordinate system of 'to_marker'.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@returns float: Returns the second angle of a body-fixed 3-1-3 Euler rotation sequence (scalar).

	"""

def Phi(to_marker, from_marker):

	"""

	Gets the third angle of a body-fixed 3-1-3 Euler rotation sequence from the coordinate system 
	of 'from_marker' to the coordinate system of 'to_marker'.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@returns float: Returns the third angle of a body-fixed 3-1-3 Euler rotation sequence (scalar).

	"""

def B1(to_marker, from_marker):

	"""

	Gets the first angle of a body-fixed 1-2-3 Euler rotation sequence from the coordinate system 
	of 'from_marker' to the coordinate system of 'to_marker'.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@returns float: Returns the first angle of a body-fixed 1-2-3 Euler rotation sequence (scalar).

	"""

def B2(to_marker, from_marker):

	"""

	Gets the second angle of a body-fixed 1-2-3 Euler rotation sequence from the coordinate system 
	of 'from_marker' to the coordinate system of 'to_marker'.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@returns float: Returns the second angle of a body-fixed 1-2-3 Euler rotation sequence (scalar).

	"""

def B3( to_marker, from_marker ):

	"""

	Gets the third angle of a body-fixed 1-2-3 Euler rotation sequence from the coordinate system 
	of 'from_marker' to the coordinate system of 'to_marker'.


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@returns float: Returns the third angle of a body-fixed 1-2-3 Euler rotation sequence (scalar).

	"""

def Orient(orientation_system, component, to_marker, from_marker):

	"""

	Gets a rotational value between two markers, from the coordinate system of 'from_marker' 
	to the coordinate system of 'to_marker'. This value is defined with respect to the 
	selected orientation system and component.
	
	- orientation_system: 1 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 1-2-3 Euler rotation sequence respectively.
	- orientation_system: 2 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 2-3-1 Euler rotation sequence respectively.
	- orientation_system: 3 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 3-1-2 Euler rotation sequence respectively.
	- orientation_system: 4 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 1-3-2 Euler rotation sequence respectively.
	- orientation_system: 5 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 2-1-3 Euler rotation sequence respectively.
	- orientation_system: 6 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 3-2-1 Euler rotation sequence respectively.
	- orientation_system: 7 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 1-2-1 Euler rotation sequence respectively.
	- orientation_system: 8 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 1-3-1 Euler rotation sequence respectively.
	- orientation_system: 9 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 2-1-2 Euler rotation sequence respectively.
	- orientation_system: 10 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 2-3-2 Euler rotation sequence respectively.
	- orientation_system: 11 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 3-1-3 Euler rotation sequence respectively.
	- orientation_system: 12 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 3-2-3 Euler rotation sequence respectively.
	- orientation_system: 13 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 1-2-3 Euler rotation sequence respectively.
	- orientation_system: 14 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 2-3-1 Euler rotation sequence respectively.
	- orientation_system: 15 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 3-1-2 Euler rotation sequence respectively.
	- orientation_system: 16 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 1-3-2 Euler rotation sequence respectively.
	- orientation_system: 17 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 2-1-3 Euler rotation sequence respectively.
	- orientation_system: 18 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 3-2-1 Euler rotation sequence respectively.
	- orientation_system: 19 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 1-2-1 Euler rotation sequence respectively.
	- orientation_system: 20 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 1-3-1 Euler rotation sequence respectively.
	- orientation_system: 21 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 2-1-2 Euler rotation sequence respectively.
	- orientation_system: 22 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 2-3-2 Euler rotation sequence respectively.
	- orientation_system: 23 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 3-1-3 Euler rotation sequence respectively.
	- orientation_system: 24 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 3-2-3 Euler rotation sequence respectively.
	- orientation_system: 25 - component: 1, 2, 3
	   Gets ansa.kinetics.Ax(to_marker, from_marker), ansa.kinetics.Ay(to_marker, from_marker) or 
	   ansa.kinetics.Az(to_marker, from_marker) respectively.
	- orientation_system: 26 - component: 1, 2, 3
	   Gets ansa.kinetics.Yaw(to_marker, from_marker), ansa.kinetics.Pitch(to_marker, from_marker) or 
	   ansa.kinetics.Roll(to_marker, from_marker) respectively.
	- orientation_system: 27 - component: 1, 2, 3, 4
	   Gets the first, second, third ot fourth euler parameter respectively.
	- orientation_system: 28 - component: 1, 2, 3
	   Gets the first, second or third rodriguez parameter respectively.
	- orientation_system: 29 - component: 1, 2, 3, 4, 5, 6, 7, 8, 9
	   XiYiZi the coordinate system of 'to marker'
	   XYZ    the coordinate system of 'from marker'
	   component: 1, 2, 3: Gets the direction cosine of Xi axis with respect to X, Y, Z axis respectively. 
	   component: 4, 5, 6: Gets the direction cosine of Yi axis with respect to X, Y, Z axis respectively.
	   component: 7, 8, 9: Gets the direction cosine of Zi axis with respect to X, Y, Z axis respectively.


	@orientation_system float: A value that specifies the orientation system.
	(value: between 1 - 29)

	@component float: A value that specifies the rotation value to be computed.

	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@returns float: Returns a rotational value between 'from_marker' and 'to_marker' (scalar).

	"""

def Accx(to_marker, from_marker, along_marker, reference_marker):

	"""

	Gets the acceleration from 'from_marker' to 'to_marker' in the X direction, along the 'along_marker'.
	All accelerations are taken in the 'reference_marker' coordinate system. 


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@along_marker string: (optional)Name or id of the 'along_marker'.

	@reference_marker string: (optional)Name or id of the 'reference_marker'.

	@returns float: Acceleration along X (scalar).

	"""

def Accy(to_marker, from_marker, along_marker, reference_marker):

	"""

	Gets the acceleration from 'from_marker' to 'to_marker' in the Y direction, along the 'along_marker'.
	All accelerations are taken in the 'reference_marker' coordinate system. 


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@along_marker string: (optional)Name or id of the 'along_marker'.

	@reference_marker string: (optional)Name or id of the 'reference_marker'.

	@returns float: Acceleration along Y (scalar).

	"""

def Accz(to_marker, from_marker, along_marker, reference_marker):

	"""

	Gets the acceleration from 'from_marker' to 'to_marker' in the Z direction, along the 'along_marker'.
	All accelerations are taken in the 'reference_marker' coordinate system. 


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@along_marker string: (optional)Name or id of the 'along_marker'.

	@reference_marker string: (optional)Name or id of the 'reference_marker'.

	@returns float: Acceleration along Z (scalar).

	"""

def Accm(to_marker, from_marker, reference_marker):

	"""

	Gets the magnitude of the acceleration from 'from_marker' to 'to_marker'.
	All accelerations are taken in the 'reference_marker' coordinate system. 


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@reference_marker string: (optional)Name or id of the 'reference_marker'.

	@returns float: Acceleration magnitude (scalar).

	"""

def Wdtx(to_marker, from_marker, along_marker, reference_marker):

	"""

	Gets the angular acceleration from 'from_marker' to 'to_marker' about the X direction of the 'along_marker'.
	All angular accelerations are taken in the 'reference_marker' coordinate system. 


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@along_marker string: (optional)Name or id of the 'along_marker'.

	@reference_marker string: (optional)Name or id of the 'reference_marker'.

	@returns float: Returns the angular acceleration about X (scalar).

	"""

def Wdty(to_marker, from_marker, along_marker, reference_marker):

	"""

	Gets the angular acceleration from 'from_marker' to 'to_marker' about the Y direction of the 'along_marker'.
	All angular accelerations are taken in the 'reference_marker' coordinate system. 


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@along_marker string: (optional)Name or id of the 'along_marker'.

	@reference_marker string: (optional)Name or id of the 'reference_marker'.

	@returns float: Returns the angular acceleration about Y (scalar).

	"""

def Wdtz(to_marker, from_marker, along_marker, reference_marker):

	"""

	Gets the angular acceleration from 'from_marker' to 'to_marker' about the Z direction of the 'along_marker'.
	All angular accelerations are taken in the 'reference_marker' coordinate system. 


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@along_marker string: (optional)Name or id of the 'along_marker'.

	@reference_marker string: (optional)Name or id of the 'reference_marker'.

	@returns float: Returns the angular acceleration about Z (scalar).

	"""

def Wdtm(to_marker, from_marker, reference_marker):

	"""

	Gets the magnitude of the angular acceleration from 'from_marker' to 'to_marker'.
	All angular accelerations are taken in the 'reference_marker' coordinate system. 


	@to_marker string: Name or id of the 'to_marker'.

	@from_marker string: (optional)Name or id of the 'from_marker'.

	@reference_marker string: (optional)Name or id of the 'reference_marker'.

	@returns float: Returns the angular acceleration magnitude (scalar).

	"""

def Varval(algebraic_variable):

	"""

	Gets the current value of a variable.


	@algebraic_variable string: Name or id of the 'algebraic_variable'.

	@returns float: Returns the current value of a variable (scalar).

	"""

def Senval(sensor):

	"""

	Gets the current value of a sensor.


	@sensor string: Name or id of the 'sensor'.

	@returns float: Returns the current value of a sensor (scalar).

	"""

def Joint(joint, computed_at_marker, component, ref_marker):

	"""

	Gets the component of a JOINT force/torque as calculated in the coordinate system of marker 'ref_marker'.


	@joint string: Name or id of the joint under consideration.

	@computed_at_marker string: Value that defines the joint-marker at which the joint-force will be calculated.
	If 0: marker I
	If 1: marker J

	@component string: Value that defines the component of the joint-force.
	If 1: FM (Force Magnitude)
	If 2: Fx
	If 3: Fy
	If 4: Fz
	If 5: TM (Torque Magnitude)
	If 6: Tx
	If 7: Ty
	If 8: Tz

	@ref_marker string: Name or id of the 'ref_marker'.

	@returns float: Returns a component of a JOINT force/torque (scalar).

	"""

def Jprim(jprim, computed_at_marker, component, ref_marker):

	"""

	Gets the component of a JPRIM (Joint PRIMitive) force/torque as calculated in the coordinate system of marker 'ref_marker'.


	@jprim string: Name or id of the jprim under consideration.

	@computed_at_marker string: Value that defines the jprim-marker at which the jprim-force will be calculated.
	If 0: marker I
	If 1: marker J

	@component string: Value that defines the component of the jprim-force.
	If 1: FM (Force Magnitude)
	If 2: Fx
	If 3: Fy
	If 4: Fz
	If 5: TM (Torque Magnitude)
	If 6: Tx
	If 7: Ty
	If 8: Tz

	@ref_marker string: Name or id of the 'ref_marker'.

	@returns float: Returns a component of a JPRIM force/torque (scalar).

	"""

def Ptcv(ptcv, computed_at_marker, component, ref_marker):

	"""

	Gets the component of a PTCV (Point-To-Curve Constraint) force/torque as calculated in the coordinate 
	system of marker 'ref_marker'.


	@ptcv string: Name or id of the ptcv under consideration.

	@computed_at_marker string: A value that defines the ptcv-marker at which the ptcv-force will be calculated.
	If 0: marker I.
	If 1: marker J.

	@component string: A value that defines the component of the ptcv-force.
	If 1: FM (Force Magnitude).
	If 2: Fx.
	If 3: Fy.
	If 4: Fz.
	If 5: TM (Torque Magnitude).
	If 6: Tx.
	If 7: Ty.
	If 8: Tz.

	@ref_marker string: Name or id of the 'ref_marker'.

	@returns float: Returns a component of a PTCV force/torque (scalar).

	"""

def Motion(motion, computed_at_marker, component, ref_marker):

	"""

	Gets the component of a MOTION force/torque as calculated in the coordinate system of marker 'ref_marker'.


	@motion string: Name or id of the motion under consideration.

	@computed_at_marker string: A value that defines the motion-marker at which the motion-force will be calculated.
	If 0: marker I
	If 1: marker J

	@component string: A value that defines the component of the motion-force.
	If 1: FM (Force Magnitude)
	If 2: Fx
	If 3: Fy
	If 4: Fz
	If 5: TM (Torque Magnitude)
	If 6: Tx
	If 7: Ty
	If 8: Tz

	@ref_marker string: Name or id of the 'ref_marker'.

	@returns float: Returns a component of a MOTION force/torque (scalar).

	"""

def Force(force, computed_at_marker, component, ref_marker):

	"""

	Gets a component of a 'force' as calculated in the coordinate system of marker 'ref_marker'.
	The force entity can be: BEAM, BUSH, FIELD, SPRING-DAMPER, SFORCE, VFORCE, VTORQUE, GFORCE.


	@force string: Name or id of the 'force' under consideration.

	@computed_at_marker string: Value that defines the force-marker at which the force will be calculated.
	If 0: marker I.
	If 1: marker J.

	@component string: Value that defines the component of the force.
	If 1: FM (Force Magnitude).
	If 2: Fx.
	If 3: Fy.
	If 4: Fz.
	If 5: TM (Torque Magnitude).
	If 6: Tx.
	If 7: Ty.
	If 8: Tz.

	@ref_marker string: Name or id of the 'ref_marker'.

	@returns float: Returns a component of 'force' (scalar).

	"""

def Akispl(x, z, kin_table, deriv_order):

	"""

	Applies the Akima method of interpolation on the 'kin_table' and gets the iord derivative 
	of the interpolated value. In case of a three dimensional 'kin_table', the interpolation 
	in the x-direction is of Akima type while in the z-direction is linear.


	@x float: First independent variable along x-axis, according to 
	which the Akispl function interpolates y.

	@z float: Second independent variable along z-axis, according to 
	which the Akispl function interpolates y.

	@kin_table string: The id of the 'kin_table'.

	@deriv_order string: (optional)The order of derivation that is taken into account during the 
	interpolation of 'kin_table'. Range: 0 <= 'deriv_order' <= 2.
	Default: 0 (take no derivative).

	@returns float: Returns the iord derivative of the interpolated value (scalar).

	"""

def Cubspl(x, z, kin_table, deriv_order):

	"""

	Applies the Cubic method of interpolation on the 'kin_table' and gets the iord derivative of the interpolated value.
	In case of a three dimensional 'kin_table', the interpolation in the x-direction is of Cubic type while in the z-direction is linear.


	@x float: First independent variable along x-axis, according to which 
	the Cubspl function interpolates y.

	@z float: Second independent variable along z-axis, according to which 
	the Cubspl function interpolates y.

	@kin_table string: The id of the 'kin_table'.

	@deriv_order string: (optional)The order of derivation that is taken into account during the 
	interpolation of 'kin_table'.
	Range: 0 <= 'deriv_order' <= 2.
	(Default: 0 (takes no derivative))

	@returns float: Retrusn the iord derivative of the interpolated value (scalar).

	"""

def Interp(time, degree, kin_table, deriv_order):

	"""

	Evaluates the iord derivative of the interpolated value of the 'kin_table' at time.
	Supports only time-series splines.
	The applied method of interpolation, depends on the value of 'degree'.


	@time float: The independent variable along the x-axis of the time-series spline, 
	according to which the Interp function interpolates y.

	@degree string: A value that specifies the degree of interpolation. 
	If 1: performs linear interpolation.
	If 3: performs cubic interpolation.

	@kin_table string: The id of the 'kin_table'.
	The 'kin_table' must reference time-series data.

	@deriv_order string: (optional)The order of derivation that is taken into account during the 
	interpolation of the 'kin_table'.
	Range: 0 <= 'deriv_order' <= 2.
	(Default: 0 (take no derivative))

	@returns float: Returns the iord derivative of the interpolated value (scalar).

	"""

def Poly(x, x0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30):

	"""

	Evaluates a standard polynomial at a user-specified value x.
	Polynomial:
	  P(x) = a0 + a1 * (x - x0) + a2 * (x - x0)^2 + ... + a30 * (x - x0)^30


	@x float: The independent variable.

	@x0 float: A value that specifies a shift in the polynomial.

	@a0 float: (optional)1st coefficient for the polynomial series.

	@a1 float: (optional)2nd coefficient for the polynomial series.

	@a2 float: (optional)3rd coefficient for the polynomial series.

	@a3 float: (optional)4th coefficient for the polynomial series.

	@a4 float: (optional)5th coefficient for the polynomial series.

	@a5 float: (optional)6th coefficient for the polynomial series.

	@a6 float: (optional)7th coefficient for the polynomial series.

	@a7 float: (optional)8th coefficient for the polynomial series.

	@a8 float: (optional)9th coefficient for the polynomial series.

	@a9 float: (optional)10th coefficient for the polynomial series.

	@a10 float: (optional)11th coefficient for the polynomial series.

	@a11 float: (optional)12th coefficient for the polynomial series.

	@a12 float: (optional)13th coefficient for the polynomial series.

	@a13 float: (optional)14th coefficient for the polynomial series.

	@a14 float: (optional)15th coefficient for the polynomial series.

	@a15 float: (optional)16th coefficient for the polynomial series.

	@a16 float: (optional)17th coefficient for the polynomial series.

	@a17 float: (optional)18th coefficient for the polynomial series.

	@a18 float: (optional)19th coefficient for the polynomial series.

	@a19 float: (optional)20th coefficient for the polynomial series.

	@a20 float: (optional)21st coefficient for the polynomial series.

	@a21 float: (optional)22nd coefficient for the polynomial series.

	@a22 float: (optional)23rd coefficient for the polynomial series.

	@a23 float: (optional)24th coefficient for the polynomial series.

	@a24 float: (optional)25th coefficient for the polynomial series.

	@a25 float: (optional)26th coefficient for the polynomial series.

	@a26 float: (optional)27th coefficient for the polynomial series.

	@a27 float: (optional)28th coefficient for the polynomial series.

	@a28 float: (optional)29th coefficient for the polynomial series.

	@a29 float: (optional)30th coefficient for the polynomial series.

	@a30 float: (optional)31st coefficient for the polynomial series.

	@returns float: Returns the value of the polynomial (scalar).

	"""

def IncAng(first_marker, middle_marker, last_marker):

	"""

	Gets the included angle between the line defined by 'first_marker' and 'middle_marker' and the line 
	defined by 'middle_marker' and 'last_marker'.


	@first_marker string: Name or id of the 'first_marker'.

	@middle_marker string: Name or id of the 'middle_marker'.

	@last_marker string: Name or id of the 'last_marker'.

	@returns float: Returns an angle (scalar).

	"""

def Dx(to_marker, from_marker, along_marker):

	"""

	Gets the distance from 'from_marker' to 'to_marker' in the X direction, along the 'along_marker'.


	@to_marker string: The name or the id of the 'to_marker'.

	@from_marker string: (optional)The name or the id of the 'from_marker'.

	@along_marker string: (optional)The name or the id of the 'along_marker'.

	@returns float: Returns the distance along X (scalar).

	"""

def GetArticulationHistoryFromConfig(kin_config):

	"""

	This function returns a list of the articulation history of the given KIN_CONFIG.


	@kin_config object: The KIN_CONFIG whose articulation history is requested.

	@returns object: Returns a list containing the articulation history.

	"""

def GetMarkers(kin_entity):

	"""

	This function returns a list of KIN_MARKERs of a Kinetic Entity, such as KIN_BODY, KIN_FORCE, KIN_JOINT, KIN_MOTION, KIN_GRAPHIC, KIN_MEASURE and KIN_REQUEST.


	@kin_entity object: The Kinetic Entity whose KIN_MARKERs are requested.

	@returns object: Returns a list containing references to the KIN_MARKER objects found.

	"""

def Aryval(array, component):

	"""

	Returns component 'compoment' of array 'array'.


	@array string: The name or the id of the array.

	@component integer: The component of the array to be returned.

	@returns float: Returns the component of the array that is requested.

	"""

def HBMConfigMove(config, total_angle, step):

	"""

	Moves a Human Body Model Kinetic Configuration 


	@config object: The kinetic configuration of the HBM that will be moved.

	@total_angle float: The total angle in degrees.

	@step float: (optional)The incremental step for applying the total angle. Default is 1.0 degree.

	@returns boolean: Returns True on failure and False on success.

	"""

def HBMTreeJointRotate(joint, total_angle, axis, step):

	"""

	Rotates a Human Body Model Tree Kinetic Joint using geometric transformation combined with morphing.


	@joint object: The Human Body Model Kinetic Joint (it should be spherical or revolute).

	@total_angle float: The total angle in degrees.

	@axis integer: The rotation axis as a number. R" : 1, S' : 2, T : 3.

	@step float: The incremental step for applying the total angle. Default is 1.0 degree.

	@returns boolean: Always returns True.

	"""

class Simulator():

	"""

	It is recommended to construct only one Simulator Object per KIN_CONFIG / whole model (otherwise python warning is thrown) in order to avoid cross-references. For example if 2 Simulator objects refer to the same KIN_CONFIG and a member is changed to one of them, the same will be changed to the other object as well.

	"""


	type = None
	"""
	Solver Type: "Dynamic", "Kinematic", "Contact", "Equilibrium", 
	"Initial Conditions".

	"""

	output = None
	"""
	Output Step Size Type: "All Steps", "Step Size", "Steps", "Step Size/Contact".

	"""

	step_size = None
	"""
	Step size for output type 'Step Size'. (step_size > 0)

	"""

	num_steps = None
	"""
	Number of steps for output type 'Steps'. (num_steps > 0)

	"""

	find_equilibrium_first = None
	"""
	Find equilibrium first.

	"""

	calc_from_zero = None
	"""
	Always calculate from time zero.

	"""

	animate_during_calc = None
	"""
	Animate during calculation.
	(If true, model's position will remain changed after simulation run)

	"""

	end_time = None
	"""
	End time of simulation (end_time > 0).

	"""

	options = None
	"""
	ansa.kinetics.Options() object. It can be accessed in order to modify its members, 
	but no modification of the object itself is permitted (exception is thrown).
	See documentation of kinetics.Options.

	"""

	def __init__(kin_config, type, end_time, find_equilibrium_first, animate_during_calc):

		"""

		Instance creation of Simulator object (constructor).


		@kin_config object: KIN_CONFIG entity that simulation refers to. It can't be 
		changed after object's creation. If omitted whole model is 
		assumed. (optional)

		@type string: Same as object's member.

		@end_time float: Same as object's member.

		@find_equilibrium_first boolean: Same as object's member.

		@animate_during_calc boolean: Same as object's member.

		"""


	def Run(kin_sim_script):

		"""

		Run the simulation. A KIN_RESULTS entity (object) is created by simulation run and returned. If a simulation error occures, None is returned and a Python warning is thrown. 


		@kin_sim_script object: (optional)KIN_SIMULATION_SCRIPT entity that simulation executes its command(s). 
		Any previously defined option(s) (e.g. type, end_time, etc.) will be 
		overridden depending from command(s) content(s).

		"""

