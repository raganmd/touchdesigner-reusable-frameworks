# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

def onValueChange(par, prev):
	return

def onPulse(par):
	if par.name == "Savesystem":
		op.Project.Save_system_json()

	elif par.name == "Loadsystem":
		op.Project.Load_system_json()

	return