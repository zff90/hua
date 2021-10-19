def AnnotationThickness():

	"""

	This function returns the thickness value found within the annotations of CATIA files (if any).
	It can be used only in an ANSA_TRANSL file.
	Warning: The function is obsolete.


	@returns float: Returns the thickness, or -1.0 if no thickness information is found in the annotations.

	"""

def LayerThickness():

	"""

	This function checks if Layer thickness lines were found in the file. It can be used only in an ANSA_TRANSL file.


	@returns integer: Returns 1 if found or 0 if not found.

	"""

def MatVecThickness():

	"""

	This function returns the thickness calculated by the Material Vector. It can be used only in an ANSA_TRANSL file.


	@returns float: Returns the thickness (1.2 for example) or -1.0 if no material vector was present in the file.

	"""

def MaterialVector():

	"""

	This function checks if a material vector was found in the file. It can be used only in an ANSA_TRANSL file.


	@returns integer: Returns 1 if found or 0 if not found.

	"""

def OrientSingleWithLine(Curve_ref, Face_id):

	"""

	This function orients a single face according to the direction of a line.


	@Curve_ref object: A reference to the curve line.

	@Face_id integer: The ID of the face to be oriented.

	@returns float: Returns the 1/100 of the curve's length.

	"""

def OrientWithLine(curve, elements):

	"""

	This function orients the faces or PIDs found in the second argument according to 
	the direction of the line. The curve reference is given as the first argument.
	The orientation is applied as well to all the faces that are topologically connected 
	to the face closest to the orientation vector.


	@curve object: A curve entity.

	@elements object: A list of faces or an integer that represents a property id.

	@returns float: Returns the 1/100 of the curve's length.

	"""

def OrientationVector():

	"""

	This function checks if an orientation vector was found in the file. It can be used only in an ANSA_TRANSL file.


	@returns integer: Returns 1 if found or 0 if not found.

	"""

def PartContainsGeometry():

	"""

	This function returns if there is at least one geometric element in the file. 
	It counts either points, curves, surfaces, faces and shell elements. 
	It can be used only in an ANSA_TRANSL file.


	@returns integer: Returns 1 if at least one of the entities is found, or 0 if the resultant file is empty.

	"""

def ThinPartThickness():

	"""

	This function returns the thickness value found within the Thin Part attribute of CATIA files (if any).
	It can only be used in an ANSA_TRANSL file.


	@returns float: Returns the thickness value (float), or -1.0 if no Thin Part attribute was present in the file.

	"""

def TranslatorLogFileAppend(info):

	"""

	The function writes information in the translator log file.


	@info: The text to be written in the log file.

	@returns integer: Returns the length of the text 'info', that the user has given as argument.

	"""

def VolumesCreated():

	"""

	This function returns the number of volumes created from solids during the translation process.
	It can be used only in an ANSA_TRANSL file.


	@returns integer: Returns the number of volumes, or 0 if no volumes were created.

	"""

def GetNextFileLine(data):

	"""

	This function is used when 'translating' a CAD file.
	CAD files are handled in a special way which identifies the file type and performs
	the appropriate operations to read the next line and put the result in the string
	variable argument.
	It is only available when reading in a neutral CAD file (iges, step, vda).


	@data string: A string where the result will be placed.

	@returns integer: Returns 1 on success and 0 on failure.

	"""

def ExtraOptions():

	"""

	This function returns the extra options that are supplied through the 
	"Extra options" field in the Translators settings card.


	@returns object: Rreturns a list that contains the arguments specified in the field.

	"""

