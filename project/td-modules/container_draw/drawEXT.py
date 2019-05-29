class Draw:
	'''
		The Project class is used to set-up the project for seamless start.

		Configuration:

		Major considerations here are that the system JSON file is
		used to load all of the pertinent information on start and load 
		a dictionary in storage called local_store with machine relivant 
		information. This information is then used in the rest of the project.
	'''

	def __init__(self, myOp):

		self.myOp 			= myOp

		self.Nodes_table 	= op('container_start_up_config/table_nodes')

		init_msg 		= "Draw init from {}".format(myOp)
		print(init_msg)

		return

	def Touch_start(self):
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
		print("Draw Start Up")
		return