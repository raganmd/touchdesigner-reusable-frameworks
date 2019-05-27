projectEXT 		= mod('projectEXT').Project

class Installation(projectEXT):
	'''
		The Installation class is used to address the needs of a specific installation.

		Configuration:

		Major considerations here are that the system JSON file is
		used to load all of the pertinent information on start and load 
		a dictionary in storage called local_store with machine relivant 
		information. This information is then used in the rest of the project.
	'''
	def __init__(self, myOp):

		self.myOp 		= myOp
		projectEXT.__init__(self, myOp)

		init_msg 		= "Installation init from {}".format(myOp)
		print(init_msg)

		return

	def Install_start(self):
		'''
			Stands in place of an execute dat - ensures all elements start-up correctly

			Notes
			---------

			Args
			---------
			none
			
			Returns
			---------
			none		
		'''

		return