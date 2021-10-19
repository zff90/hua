def CheckIntersectionOfVolumes(volume1, volume2):

	"""

	Calculates the volumes of two ortho-parallelepiped boxes in 3d space and the common volume of them.


	@volume1 object: A list with the coordinates of 8-corners of first ortho-parallelepiped box in 3d space.

	@volume2 object: A list with the coordinates of 8-corners of second ortho-parallelepiped box in 3d space.

	@returns object: Returns a list with three values. The first value of the list is the volume of the first box.
	The second value of the list is the volume of the second box. The last value of the list is the
	common volume of the two boxes. If the value of the common volume is equal to zero, the two boxes are
	not intersected in 3d space.

	"""

def GetCoordTransformMatrix4x3(deck, entity, x0, y0, z0):

	"""

	This function returns a transformation matrix of a coordinate system according to the global coordinate system.


	@deck integer: The deck constant.

	@entity object: The coordinate system whose transformation matrix will be calculated.

	@x0 float: The x-coordinate of the reference point. Needed for the case of cylindrical or 
	spherical coordinate system. In case of rectangular coordinate system, 
	these coordinates do not influence the results.

	@y0 float: The y-coordinate of the reference point. Needed for the case of cylindrical or 
	spherical coordinate system. In case of rectangular coordinate system, 
	these coordinates do not influence the results.

	@z0 float: The z-coordinate of the reference point. Needed for the case of cylindrical or 
	spherical coordinate system. In case of rectangular coordinate system, 
	these coordinates do not influence the results.

	@returns object: On success, it returns a list that contains the 4x3 matrix. 
	The first three rows correspond to the rotation matrix and the fourth row to the translation.
	On failure, it returns None.

	"""

def GetVectorsOfCord(coord):

	"""

	The function computes the three unit-vectors of a given coordinate system.
	The vectors have coordinates at global coordinate-system.


	@coord object: The local coordinate system.

	@returns object: Returns a list containing the three unit-vectors of the given coordinate system.
	
	The order is : 
	a) The first  is (1x3) list with coordinates of the axial 'xx'.
	b) The second is (1x3) list with coordinates of the axial 'yy'.
	c) The third  is (1x3) list with coordinates of the axial 'zz'.

	"""

def GlobalToLocal(cord_id, coordinates, type):

	"""

	The function converts the global-coordinates of one 'point' or 'vector' to the local-coordinates
	for one specific local-cordinate with (id_cord).


	@cord_id integer: The 'id' of the local-coordinate system.

	@coordinates object: A list with the coordinates of a 'point' or a 'vector' at the global-system.

	@type string: The string 'point' or 'vector'.

	@returns object: Returns a list with the local-coordinates of 'point' or 'vector'.

	"""

def HelixSweep(starting_point, period_pitch, CURVE):

	"""

	This function creates points around a main-curve as a helix.


	@starting_point object: A list with the coordinates of the starting point.

	@period_pitch float: The step of the helix along the direction of the main-curve.

	@CURVE object: The object of the curve entity.

	@returns object: Returns a list with the following contents:
	1) At position [0], there is the number of points.
	2) At position [1], there is a list of the x-coordinates of points.
	3) At position [2], there is a list of the y-coordinates of points.
	4) At position [3], there is a list of the z-coordinates of points.

	"""

def LocalSystem(origin, point1, point2):

	"""

	This function creates a local coordinate system.


	@origin object: The list with the coordinates that correspond to the origin.

	@point1 object: A list with the coordinates of a point that lies on the z-axis.

	@point2 object: (optional)A list with the coordinates of a point that lies in the x-z plane.

	@returns object: Returns a list of three vectors representing the axis of local system.
	The output list is: [[Vector1_x,Vector1_y,Vector1_z], [Vector2_x,Vector2_y,Vector2_z], [Vector3_x,Vector3_y,Vector3_z]] 
	The first vector (Vector1) is the local axial xx', the second vector (Vector2) is the local axial yy', 
	and the third vector (Vector3) is the local axial zz'. The vectors are unit.

	"""

def LocalToGlobal(cord_id, coordinates, type):

	"""

	Converts the local-coordinates of one 'point' or 'vector' to the global-coordinates for a specific local cordinate system.


	@cord_id integer: The 'id' of the local-coordinate system.

	@coordinates object: The list (1x3) with coordinate of 'point' or 'vector' 
	at local-system. When the input data is 'vector' on spherical 
	or cylindrical coordinate system, you are able to give the 
	reference point (in which the vector is applied) with the 
	extension of the matrix to (1x6). The three more positions 
	of matrix represent the reference coordinates of local system.

	@type string: 'point' or 'vector'. In general, the return coordinates are 
	different for 'point' and 'vector'.

	@returns object: Returns the global-coordinates of 'point' or 'vector'.
	The output data is a list (1x3) with coordinate of 'point' or 'vector' at global-system.

	"""

def Normalize(vec):

	"""

	This function normalizes a vector (ie. makes it unit long).


	@vec object: A list describing the vector.

	@returns object: Returns a vector (list) of length 1 pointing to the same direction as the original.

	"""

def ProjectPointToCons(x_y_z, cons):

	"""

	This function computes the projection point of one point on 'Cons'.


	@x_y_z object: A list with the coordinates of the point.

	@cons integer: The object of the CONS were the projection will take place.

	@returns object: Returns a list with the result of the projection.
	
	The output list can be: 
	i) 0 - When cons is not valid. 
	ii) A list [ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z] - When the point 
	    to be projected is projected on 'Cons' between end points. 
	iii) A list [ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z, SnapPoint_x,SnapPoint_y,SnapPoint_z] - When the 
	     point to be projected is projected on extension of 'Cons', outside the end points.

	"""

def ProjectPointToContainer(coords, entities):

	"""

	This function finds the projection of a point to a list of faces and shells.
	If no projection can be found the minimum distance is computed.


	@coords object: The point coordinates are given as a list of [x, y, z].

	@entities object: The list of entities. It should contain shells, faces, parts,
	properties or set.

	@returns object: Returns a list that contains:
	a) mat[0][0], mat[0][1], mat[0][2] = the projected point (x,y,z) or the point of the minimum distance.
	b) mat[1] = the found minimum distance d.
	b) mat[2][0], mat[2][1], mat[2][2] = the found minimum distances (dx, dy, dz).
	c) mat[3][0], mat[3][1], mat[3][2] = the normal vector (dx,dy,dz) at the point of projection.
	d) mat[4] = the entity (shell or face) where the projection was found .

	"""

def ProjectPointToShell(point, shell):

	"""

	This function computes the projection of a point on a shell.


	@point object: A list with the coordinates of the point to be projected.

	@shell object: A shell object.

	@returns object: Returns a tuple with the result of the projection.
	
	The output tuple can be : 
	i) (ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z,) - When the point to be projected is projected on 'Shell' between     the boundary edges of 'Shell'. 
	ii)(ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z), (SnapPoint_x,SnapPoint_y,SnapPoint_z)) - When the point to be        projected is projected on extension of 'Shell', out from the boundary edges of 'Shell'. 
	
	The 'Snap Point' is on the boundary of the 'Shell' (on edge or at corner). 
	When the input shell is not a reference to a valid shell, exception is raised.

	"""

def TransformPointMatrix4x3(POINT, TRANSF_MATRIX4x3):

	"""

	This function transforms a point (x,y,z) according to the given TRANSF_MATRIX4x3.
	TRANSF_MATRIX4x3 is the 4x3 transformation matrix.


	@POINT object: A list with the coordinates of the points.

	@TRANSF_MATRIX4x3 object: The 4x3 transformation matrix.

	@returns object: Returns a list with 3 elements [x, y, z] on success and None on error.

	"""

def TransformVectorMatrix4x3(VECTOR, TRANSF_MATRIX4x3):

	"""

	This function transforms a vector (dx,dy,dz) according to the given TRANSF_MATRIX4x3.
	TRANSF_MATRIX4x3 is the 4x3 transformation matrix.


	@VECTOR object: A list of the vector.

	@TRANSF_MATRIX4x3 object: The 4x3 list of the transformation matrix.

	@returns object: Returns a list with 3 elements [dx, dy, dz] on success and 0 on error.

	"""

def TransposeMatrix(matrix):

	"""

	This function is used to transpose a list (matrix).


	@matrix object: A list that will be transposed.

	@returns object: Returns the resulting list, without modifying the input list.

	"""

def CalcAngleOfVectors(vec_1, vec_2, vec_3):

	"""

	This function computes the angle of two or three 3D vectors.


	@vec_1 object: A list defining the first vector.

	@vec_2 object: A list defining the second vector.

	@vec_3 object: (optional)A list defining the third vector.

	@returns float: Returns the angle of the vectors in radians (double), which is computed as follows:
	i) When the input list has two vectors, the angle is mathematically defined to be between '0' and 'PI' (inclusive). 
	ii) When the input list has three vectors the angle is mathematically defined to be between '0' and '2PI' (inclusive). 
	iii) When the input list is not correct the function returns the error value '-PI' .

	"""

def CartesianToCylindrical(coordinates):

	"""

	Converts the cartesian coordinates to cylindrical coordinates.


	@coordinates object: A list with the cartesian coordinates to convert.

	@returns object: Returns a list with the respective cylindrical coordinates.

	"""

def CartesianToSpherical(coordinates):

	"""

	Converts the cartesian coordinates to spherical coordinates.


	@coordinates object: A list with the cartesian coordinates to be converted.

	@returns object: Returns a list with the spherical coordinates.

	"""

def CylindricalToCartesian(coordinates):

	"""

	Converts the cylindrical coordinates to cartesian coordinates.


	@coordinates object: A list with the cylindrical coordinates to be converted.

	@returns constant: Returns a list with the converted cartesian coordinates.

	"""

def CylindricalToSpherical(coordinates):

	"""

	Converts the cylindrical coordinates to spherical coordinates.


	@coordinates object: A list with the cylindrical coordinates to be converted.

	@returns object: Returns a list with the converted spherical coordinates.

	"""

def NormalVec(vec):

	"""

	This function computes a unit normal vector from the input vector 'vec'.
	At the end, the dot product of the vectors must be 0.


	@vec object: A list describing the vector.

	@returns object: Returns a unit vector (list) of the input vector 'vec'.

	"""

def ProjectPointToLineSegment(project_point, line_segment_point_1, line_segment_point_2):

	"""

	This function computes the projection point of a point on a line segment.


	@project_point object: A list of coordinates that define the point to be projected.

	@line_segment_point_1 object: A list of coordinates that define the first end point.

	@line_segment_point_2 object: A list of coordinates that define the second end point.

	@returns object: Returns a tuple with the result of the projection.
	
	The output tuple can be: 
	i) ((ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z),) - When the point is projected on the 
	   line segment between end points. 
	ii)((ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z), (SnapPoint_x,SnapPoint_y,SnapPoint_z)) - When the point 
	   is projected on the extension of the line segment, outside the end points. 
	
	The 'Snap Point' is one of the two end points of the line segment.

	"""

def ProjectPointToTriangle(project_point, triangle_point_1, triangle_point_2, triangle_point_3):

	"""

	This function computes the projection point of a point on a triangle. 
	 
	The input list is of the following format: 
	[ProjectPoint_x,ProjectPoint_y,ProjectPoint_z, TrianglePoint1_x,TrianglePoint1_y,TrianglePoint1_z, 
	TrianglePoint2_x,TrianglePoint2_y,TrianglePoint2_z, TrianglePoint3_x,TrianglePoint3_y,TrianglePoint3_z] 
	The first point is the point to be projected on the triangle and the other three points are the corners of the triangle.


	@project_point object: A list with the coordinates of point to be projected.

	@triangle_point_1 object: A list with the coordinates of the 1st triangle node.

	@triangle_point_2 object: A list with the coordinates of the 2nd triangle node.

	@triangle_point_3 object: A list with the coordinates of the 3rd triangle node.

	@returns object: Returns a list with the result of the projection.
	
	The output list can be : 
	i)  0, When the three corners are collinear or create a degenerate triangle. 
	ii) ((ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z)) - When the point to 
	    be projected is projected in triangle. 
	iii) ((ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z), (SnapPoint_x,SnapPoint_y,SnapPoint_z)) - When the 
	     point to be projected is projected outside the triangle area. The 'Snap Point' is the nearest point of the 
	     triangle to the projected point. The first value of list is a flag with values (0,1 or 2) that represent 
	     the three situations described above.

	"""

def SphericalToCartesian(coordinates):

	"""

	This function converts spherical coordinates to cartesian coordinates.


	@coordinates object: The input data is a list (1x3) with the spherical coordinates to be converted.

	@returns object: Returns a list with the converted cartesian coordinates.

	"""

def SphericalToCylindrical(coordinates):

	"""

	This function converts spherical coordinates to cylindrical coordinates.


	@coordinates object: The input data is a list (1x3) with the spherical coordinates to be converted.

	@returns object: Returns a list (1x3) with the converted cylindrical coordinates.

	"""

def ConvertEulerAnglesToRotationMatrix_XYZ(vector):

	"""

	Converts Euler angles to a rotation matrix. The order of the rotations is as follows:
	 1st) Rotation around existed axial 'X' is the first rotation.
	 2nd) Rotation around a new axial 'Y' is the second rotation.
	 3rd) Rotation around a newest axial 'Z' is the last rotation.
	
	The input data are:
	 1) The first rotation angle around axial 'X' (x).
	 2) The second rotation angle around new axial 'Y' (y).
	 3) The third rotationa angle around newest axial 'Z' (z).
	
	All the above angles are in radians.


	@vector object: A series of floats.

	@returns object: Returns a 3d-rotation matrix (3x3) as a list.
	
	ATTENTION: The rotation matrix is from the source coordinate system to the target coordinate system.

	"""

def ConvertEulerAnglesToRotationMatrix_ZXZ(axis):

	"""

	Converts Euler angles to a rotation matrix. The order of the rotations is as follows:
	 1st) Rotation around existed axial 'Z' is the first rotation.
	 2nd) Rotation around a new axial 'X' is the second rotation.
	 3rd) Rotation around a newest axial 'Z' is the last rotation.
	
	The input data are:
	 1) The first rotation angle around axial 'Z' (zAngle1).
	 2) The second rotation angle around new axial 'X' (xAngle2).
	 3) The third rotationa angle around newest axial 'Z' (zAngle3).
	
	All the above angles are in radians.


	@axis object: A list of floats respresenting the 3 angles.

	@returns object: Returns a 3d-rotation matrix (3x3) as a list.
	
	ATTENTION: The rotation matrix is from the source coordinate system to the target coordinate system.

	"""

def ConvertRotationMatrixToEulerAngles_XYZ(rotationMatrix1, rotationMatrix2, rotationMatrix3):

	"""

	Converts a 3d-rotation matrix to the combination x-y-z of Euler angles. The order of rotations is as follows:
	 1st) Rotation around existing axial 'X' is the first rotation.
	 2nd) Rotation around a new axial 'Y' is the second rotation.
	 3rd) Rotation around a newest axial 'Z' is the last rotation.


	@rotationMatrix1 object: A list with the coordinates of the first rotation matrix.

	@rotationMatrix2 object: A list with the coordinates of the second rotation matrix.

	@rotationMatrix3 object: A list with the coordinates of the third rotation matrix.

	@returns object: Returns a list containing the three Euler angles of the combination x-y-z.
	The first item of the returned list is the Euler angle of rotation around the existing axial 'X'.
	The second item of the returned list is the Euler angle of rotation around the new axial 'Y'.
	The third item of the returned list is the Euler angle of rotation around the newest axial 'Z'.
	All the above angles are in radians.

	"""

def ConvertRotationMatrixToEulerAngles_ZXZ(rotationMatrix1, rotationMatrix2, rotationMatrix3):

	"""

	Converts a 3d-rotation matrix to the combination z-x-z of Euler angles. The order of rotations is as follows:
	 1st) Rotation around the existing axial 'Z' is the first rotation.
	 2nd) Rotation around a new axial 'X' is the second rotation.
	 3rd) Rotation around a newest axial 'Z' is the last rotation.


	@rotationMatrix1 object: A list with the coordinates of the first rotation matrix.

	@rotationMatrix2 object: A list with the coordinates of the first rotation matrix.

	@rotationMatrix3 object: A list with the coordinates of the first rotation matrix.

	@returns object: Returns a list containing the three Euler angles of the combination z-x-z.
	The first item of the list is the Euler angle of rotation around the existing axial 'Z'.
	The second item of the list is the Euler angle of rotation around the new axial 'X'.
	The third item of the list is the Euler angle of rotation around the newest axial 'Z'. 
	All the above angles are in radians.

	"""

def ConvertRotationMatrixToEulerAxisAngle( rotationMatrix1, rotationMatrix2, rotationMatrix3):

	"""

	Converts a 3d-rotation matrix to the Euler axis and angle.


	@rotationMatrix1 object: A list with the coordinates of the first rotation matrix.

	@rotationMatrix2 object: A list with the coordinates of the first rotation matrix.

	@rotationMatrix3 object: A list with the coordinates of the first rotation matrix.

	@returns object: Returns a tuple that has a length of two. The first item is a tuple containing 3 floats 
	and it represents the vector of Euler axis. The second item is a float value representing 
	the Euler rotation angle in radians.

	"""

def ProjectPointsToElements(coordinates, entities, tolerance):

	"""

	Projects a list of points on a list of elements in a given tolerance and gets the projected point, 
	the distance and the projection element.
	
	It works with SHELL, SOLID, SEGMENT, ELSURFACE, RIGID, ACOUSTIC, CAABSF3/4, ASI3D elements.


	@coordinates object: A list with (x, y, z) coordinates of the points to be projected.

	@entities object: A list with the elements to check for projection.

	@tolerance float: The tolerance in which the function checks for a projection.

	@returns object: Returns a list containing objects with the following attributes: projection, distance and entity.
	If no projection is found, entity is None.

	"""

def CrossProduct(vec1, vec2):

	"""

	This function calculates the cross product of the two vectors.


	@vec1 object: A tuple representing vector 1.

	@vec2 object: A tuple representing vector 2.

	@returns object: Returns a new vector (list) representing the cross product.

	"""

def DotProduct(vec1, vec2):

	"""

	This function calculates the dot product of two vectors.


	@vec1 object: A tuple representing Vector 1.

	@vec2 object: A tuple representing Vector 2.

	@returns float: Returns a double precision value representing the dot product.

	"""

def GetDoeStudyExperimentsForParams(parameters, algorithm, level, experiments_number, seed, taguchi_array, reject_duplicates):

	"""

	Function to get the experiments of the input parameters 
	that are defined as named tuples with the fieldnames "min"
	and "max". For the definition of the input parameters the
	"import collections" statement is essential (look at the example).


	@parameters object: list or objects of parameters defined as named 
	tuples with the fieldnames "min" and "max"

	@algorithm string: algorithm used to generate the experiments.
	Supported algorithms are " "Full Factorial", 
	"Uniform Latin Hypercube", "Random", "Taguchi 
	Orthogonal Arrays" and "Linear".

	@level integer: (optional)integer value used for all parameters ("Full 
	Factorial" or "Taguchi Orthogonal Arrays" 
	algorithms). Default value is 2.

	@experiments_number integer: (optional)the number of the generated experiments (used in 
	"Uniform Latin Hypercube", "Random" and "Linear" 
	algorithms).

	@seed integer: (optional)positive number used to initialize the random number generator
	(used in "Uniform Latin Hypercube" and "Random" algorithms).

	@taguchi_array string: (optional)Taguchi array to be used for experiments generation. 
	Taguchi array is related to the level value. 
	For level = 2, supported arrays are "L4", "L8", "L12", 
	"L16", "L20", "L24", "L32", "L64", "L128", "L256".
	For level = 3, supported arrays are "L9", "L18", "L27", 
	"L36", "L54", "L81", "L108".
	For level = 4, supported arrays are "L16", "L32", "L64".
	For level = 5, supported arrays are "L25", "L50".

	@reject_duplicates boolean: (optional)reject duplicate experiments in Taguchi algorithm

	@returns object: Returns a list of lists (every list corresponds to a single experiment).

	"""

