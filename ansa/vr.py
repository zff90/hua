class VR():

	"""

	A VR object allows you to access tracking data of VR devices as well as set callbacks for the vr controllers buttons press and release.

	"""


	is_running = None
	"""
	Query if vr is running.

	"""

	def __init__():

		"""

		VR object constructor.


		@returns object: Returns the created VR object.

		"""


	def device_type(device):

		"""

		Get the class of a VR Device.Possible classes are: "HMD", "Controller", "GenericTracker", "TrackingReference", "DisplayRedirect", "Invalid".


		@device integer: The index of a tracked device

		@returns string: Return the class name of the VR Device.

		"""


	def device_status(device):

		"""

		Get the status of a VR Device.Possible values are: "Unknown", "Idle", "UserInteraction", "UserInteractionTimeout", "Standby".


		@device integer: The index of a tracked device

		"""


	def device_position(device):

		"""

		Get the position of a VR Device.


		@device integer: The index of a tracked device.

		@returns object: Returns a tuple with the coordinates of the device position in 3D space.

		"""


	def devices():

		"""

		Get a list of indices of all Devices


		@returns object: Returns a list containing the indices of all connected vr devices.

		"""


	def tracked_devices():

		"""

		Get a list of indices of tracked devices.


		@returns object: Returns a list containing the indices of all tracked vr devices.

		"""


	def tracking_update(callback):

		"""

		Set callback for tracking data update.


		@callback object: A callback object which is called on each tracking update.

		@returns object: Always returns None.

		"""


	def track_devices(device_types):

		"""

		Select which class of devices to track.


		@device_types object: Possible values : "HMD", "Controller", "GenericTracker", "TrackingReference", "DisplayRedirect", "All"

		@returns object: Always returns None.

		"""


	def device_pose(device):

		"""

		Get the pose of a VR Device.


		@device integer: The index of a tracked device.

		@returns object: Returns a dictionary containing a pose frame of a device. It consists of the following fields:"pose" : a column major 4x4 matrix of the device pose in 3D space."valid" : a boolean flag, true if the tracking pose data are valid."device_connected" : a boolean flag, true if device with the given index is connected.

		"""


	def display_notification(message, persistent):

		"""

		Display a notification message


		@message string: A text message to display.

		@persistent boolean: (optional)If set to true, the notification is persistent, it is dismissable by a button press. If set to false the notification will disappear automatically after a few seconds. Default is false.

		@returns object: Always returns None.

		"""


	def show_devices(devices, visible):

		"""

		Toggle drawing of a device class


		@devices object: Possible values : "HMD", "Controller", "GenericTracker", "TrackingReference", "DisplayRedirect", "All"

		@visible boolean: Boolean to show/hide the drawing of the devices of the specified class.

		@returns object: Always returns None.

		"""


	def enable_callbacks(name):

		"""

		Enable vr controllers buttons callbacks


		@name string

		@returns object: Always returns None.

		"""


	def disable_callbacks():

		"""

		Disable vr controllers buttons callbacks


		@returns object: Always returns None.

		"""


	def button_press_callback(action, primary, callback, tooltip):

		"""

		Set press callback for a vr controller button


		@action string: The button for which the callback will be set. The available buttons are: 
		"VR_BUTTON_TOUCHPAD"
		"VR_BUTTON_GRIP"
		"VR_BUTTON_TRIGGER"
		"VR_BUTTON_LEFT"
		"VR_BUTTON_RIGHT"
		"VR_BUTTON_UP"
		"VR_BUTTON_DOWN"

		@primary boolean: Select primary or secondary controller

		@callback object: The callable object which will be called on button press.

		@tooltip string: (optional)The tooltip to display next to the controller button, when script callbacks are enabled.

		@returns object: Always returns None.

		"""


	def button_release_callback(action, primary, callback, tooltip):

		"""

		Set release callback for a vr controller button


		@action string: The button for which the callback will be set. The available buttons are: 
		"VR_BUTTON_TOUCHPAD"
		"VR_BUTTON_GRIP"
		"VR_BUTTON_TRIGGER"
		"VR_BUTTON_LEFT"
		"VR_BUTTON_RIGHT"
		"VR_BUTTON_UP"
		"VR_BUTTON_DOWN"

		@primary boolean: Select primary or secondary controller.

		@callback object: The callable object which will be called on button release.

		@tooltip string: (optional)The tooltip to display next to the controller button, when script callbacks are enabled.

		@returns object: Always returns None.

		"""


	def move_head(x, y, z, offset):

		"""

		Move the head to a specified position in world coordinates


		@x float: X coordinate of the position to move the head.

		@y float: Y coordinate of the position to move the head.

		@z float: Z coordinate of the position to move the head.

		@offset float: (optional)an offset from the position to move the head.

		@returns object: Always returns None.

		"""

