import PySimpleGUI as sg

'''
One tab for interval training
	- new sequence button
	- replay button
	- solution button
	- area to display solution

One Tab for settings
	- Root Note drop down list
	- Sequence Length drop down list
	- Note duration (?)
'''

# TODO: initial fixed layout?
	# -SolutionImage- can take on variable widths based on -SequenceLength-
def get_layout():

	train_tab = [
		[sg.Text('Interval Trainer')],
		[sg.Image(key='-SolutionImage-')],
		[sg.B('New Sequence'), sg.B('Solution'),sg.B('Replay Sequence')]
	]

	settings_tab = [
		[sg.Text('')],
		[sg.Text('Root Note:')
			,sg.Combo([' C',' C#',' D',' D#',' E',' F',' F#',' G',' G#',' A',' A#',' B'],default_value=' C', key='-RootNote-')],
		[sg.Text('Sequence Length:')
			,sg.Combo([2,3,4,5,6,7,8],default_value=2,key='-SequenceLength-')],	
		[sg.Text('Note Duration:')
			,sg.Combo([.25,.5,1,2,4],default_value=4,key='-NoteDuration-')],
	]

	layout = [
		[sg.TabGroup([
			[sg.Tab('Trainer', train_tab), 
			sg.Tab('Settings', settings_tab)]]
		)],    
	]

	return layout