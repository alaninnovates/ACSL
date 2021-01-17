import automatic
import manual

for i in range(2):
    fileToRun = input('Manual or automatic checking: ')
    if fileToRun.lower() == 'manual':
        manual.main()
    elif fileToRun.lower() == 'automatic':
        automatic.main()
    else:
        print('That file/option does not exist!')