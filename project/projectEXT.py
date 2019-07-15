import json

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

		self.myOp 			= myOp
		self.System_json 	= 'data/system.json'
		self.Config 		= 'data/config.json'

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
		# load system json on start
		self.myOp.Load_system_json()

		# load and store system config
		self.Load_store_json(self.Config, op.Project, 'nodes', 'nodes')

		# start-up sequence for modules
		op.Com.Touch_start()
		op.Output.Touch_start()
		return

	def Save_system_json(self):
		''' 
			Save the contents of the System Pars to file
		
			Args
			---------------
			None
									
			Returns
			---------------
			None
		'''
		system_pars_dict 	= self.System_pars_to_dict()

		for key, val in system_pars_dict.items():
			op.Project.store(key, val)

		self.Write_dict_to_json('data/system.json', system_pars_dict)


	def Load_system_json(self):
		list_of_custom_pages 	= [each_page.name for each_page in op.Project.customPages]
		
		for each_page in list_of_custom_pages:
			# load from file
			self.Load_store_json(self.System_json, op.Project, each_page, each_page)
			
			# grab the recently loaded storage
			load_pars = op.Project.fetch(each_page)

			# loop through pars and set vals
			for each_key, each_value, in load_pars.items():
				try:
					op.Project.pars(each_key)[0].val = each_value
				except:
					pass

		return

	def System_pars_to_dict(self):
		''' 
			Create a dictionary from op.Project's system pars
		
			Args
			---------------
			None
									
			Returns
			---------------
			par_dict (dict)
			> a dictionary a dictionary of page names, pars, and values.
		'''
		list_of_custom_pages 	= [each_page.name for each_page in op.Project.customPages]
		par_dict = {}

		# set up our data struct 
		for each_page in list_of_custom_pages:
			par_dict[each_page] = {}
		
		# loop through pars
		for each_par in op.Project.pars():
			if each_par.isCustom and not each_par.isPulse:
				par_dict[each_par.page.name][each_par.name] = each_par.val
		
		return par_dict

	def Page_to_dict(self, target_op, target_page, p_name, ignore_list):
		''' 
			A reusable method for capturing parameters on a single page of a COMP
		
			Args
			---------------
			target_op (TouchDesigner COMP):
			> a ToughDesigner COMP that has custom parameters you would like to convert
			> into a python dictionary.
			
			target_page (str):
			> the string name of the page whose parameters you would like to
			> convert into a python dictionary.
		
			p_name (str):
			> a name for the preset / cue.
			
			ignore_list (list):
			> a list of parameters you do not want to include.
									
			Returns
			---------------
			par_dict (dict)
			> a dictionary containing a preset name and dictionary of parameters.
		'''
	
		# create empty par_dict with input name as the preset_name value
		par_dict = {
			"preset_name"   : p_name,
			"preset_vals"   : {}
		}
	
		# loop through each parameter in the target_op and capture its name and
		# value only if its custom page matches the input string for target_page, 
		# and the pars are not on the ignore_list
		for each_par in target_op.pars():
			if each_par.isCustom and each_par.page == target_page and each_par.name not in ignore_list:
				par_dict["preset_vals"][each_par.name] = each_par.val
	
		return par_dict

	def Dict_to_storage(self, target_op, storage_dict_key, preset_name, dict_to_store):
		''' 
			A reusable method for capturing parameters on a single page of a COMP
		
			Args
			---------------
			target_op (TouchDesigner COMP):
			> a ToughDesigner COMP that has custom parameters you would like to convert
			> into a python dictionary.
			
			storage_dict_key (str):
			> the string name of the storage dictionary you'd like to add
			> your preset / cue to.
		
			preset_name (str):
			> a name for the preset / cue.
			
			dict_to_store (dict):
			> a python dictionary to put into storage.
									
			Returns
			---------------
			None
		'''
		# grab the dictionary from storage
		all_presets                 = target_op.fetch(storage_dict_key)
	
		# create a new entry
		all_presets[preset_name]    = dict_to_store
	
		# put dictionary back into storage
		target_op.store(storage_dict_key, all_presets)

	def Load_store_json(self, target_file, storage_op, target_key, storage_name):
		''' 
			A Helper function that reads JSON from disk
		
			Args
			---------------
			target_file (file path):
			> a path to a .json file on disk. This is where the file will
			> be read from.
			
			storage_op (TouchDesigner operator):
			> the target operator where we will store the dictionary.
			target_key (str):
			> the string key we want to pull from our JSON file.
			storage_name (str):
			> the string name we want to use for storage.
									
			Returns
			---------------
			None
		'''

		# open the json file as json_file
		with open(target_file) as json_file:

			# create a dictionary out of our json file
			json_dict               = json.load(json_file).get(target_key)

			# store our dictionary in the target op
			storage_op.store(storage_name, json_dict)


	def Write_dict_to_json(self, target_file, dict_to_save):
		''' 
			A Helper function that writes JSON file to disk
		
			Args
			---------------
			target_file (file path):
			> a path to a .json file on disk. This is where the file will
			> be written.
			
			dict_to_save (dict):
			> the dictionary to save as json.
									
			Returns
			---------------
			None
		'''

		# open the json file
		with open(target_file, 'w') as json_file:

			# ensure the format for the json is human readable
			pretty_json 			= json.dumps(dict_to_save, indent=4)

			# write the json to file
			json_file.write(pretty_json)