import PySimpleGUI as sg
from Sequence import Sequence
from gui_layout import get_layout

sg.theme('DarkAmber')
window = sg.Window('Interval Trainer', get_layout()) 

sequence = None
while True:
	event, values = window.read() 
	print(event, values)       

	if event == sg.WIN_CLOSED:
		break

	elif event == 'New Sequence':
		window['-SOLUTION_TEXT-'].update(value='						')
		sequence = Sequence(
			root=window['-RootNote-'].get().strip(), 
			num_notes = window['-SequenceLength-'].get())
		sequence.play()

	elif event == 'Solution':
		if sequence is not None:
			window['-SOLUTION_TEXT-'].update(value=sequence.get_text())
		
	elif event == 'Replay Sequence':
		if sequence is not None:
			sequence.play()

window.close()