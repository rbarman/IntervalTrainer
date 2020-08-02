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
		sequence = Sequence(
			root=window['-RootNote-'].get().strip(), 
			num_notes = window['-SequenceLength-'].get())
		sequence.play()

		# TODO: hide -SolutionImage- ?
		# instead of programatically hiding, could display a static img of empty measure
			# The following don't work, but docs state that a blank update() should delete the image
			# window['-SolutionImage-'].update()
			# window['-SolutionImage-'].Update()
			# window['-SolutionImage-'].update(data=None)
			# window['-SolutionImage-'].update(visible = False)
			# window['-SolutionImage-'].update(filename=None)

	elif event == 'Solution':
		if sequence is not None:
			window['-SolutionImage-'].update(filename=sequence.get_png())
		
	elif event == 'Replay Sequence':
		if sequence is not None:
			sequence.play()

window.close()