import PySimpleGUI as sg
from Sequence import Sequence

sg.theme('DarkAmber')

train_tab = [
	[sg.Text('Interval Trainer')],
	# TODO: instead of text, show png of notes
	[sg.Text('						',key='-SOLUTION_TEXT-')],      
	[sg.B('New Sequence'), sg.B('Solution'),sg.B('Replay Sequence')]
]

settings_tab = [
	[sg.Text('')],
	[sg.Text('Root Note:')
		,sg.Combo([' C',' C#',' D',' D#',' E',' F',' F#',' G',' G#',' A',' A#',' B'],default_value=' C', key='-RootNote-')],
	[sg.Text('Sequence Length:')
		,sg.Combo([2,3,4,5,6,7,8],default_value=2,key='-SequenceLength-')],	
]

layout = [
	[sg.TabGroup([
		[sg.Tab('Trainer', train_tab), 
		sg.Tab('Settings', settings_tab)]]
	)],    
]    
window = sg.Window('Interval Trainer', layout)      

#################################################################

sequence = None

while True:
	event, values = window.read() 
	print(event, values)       

	if event == sg.WIN_CLOSED or event == 'Exit':
		break

	elif event == 'New Sequence':
		window['-SOLUTION_TEXT-'].update(value='						')
		sequence = Sequence(
			root=window['-RootNote-'].get().strip(), 
			num_notes = window['-SequenceLength-'].get())
		sequence.play()

	elif event == 'Solution':
		if sequence is not None:
			solution = sequence.get_text()
			print(f'solution: {solution}')
			window['-SOLUTION_TEXT-'].update(value=solution)
		
	elif event == 'Replay Sequence':
		if sequence is not None:
			sequence.play()

window.close()