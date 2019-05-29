# me - this DAT
# 
# frame - the current frame
# state - True if the timeline is paused
# 
# Make sure the corresponding toggle is enabled in the Execute DAT.

def onStart():
	# start-up procedure
	op.Project.Touch_start()
	return

def onExit():
	# shut down procedure
	return
	