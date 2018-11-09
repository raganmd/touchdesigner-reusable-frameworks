class Project:
	'''
		The Project class is used to set-up the project for seamless start.

		Configuration:

		Major considerations here are that the system JSON file is
		used to load all of the pertinent information on start and load 
		a dictionary in storage called local_store with machine relivant 
		information. This information is then used in the rest of the project.
	'''
	def __init__(self, myOp):

		self.myOp 		= myOp

		init_msg 		= "Project init from {}".format(myOp)
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

		return

	def Save_tox(self, current_loc):
		'''
			Stands in place of an execute dat - ensures all elements start-up correctly

			Notes
			---------

			Args
			---------
			current_loc (str):
			> the operator that's related to the currently focused 
			> pane object. This is required to ensure that we correctly
			> grab the appropriate COMP and check to see if needs to be saved
					
			Returns
			---------
			none		
		'''
		# check if external
		if current_loc.par.externaltox != "":
			# save external file
			external_path 		= current_loc.par.externaltox
			current_loc.save(external_path)

			# create and print log message
			log_msg 		= "{} saved to {}/{}".format(current_loc, 
														project.folder, 
														external_path)
			print(log_msg)
		
		# skip if the file isn't externalized already
		else:
			pass
		return