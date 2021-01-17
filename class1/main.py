import automatic
import manual

# def main():
for i in range(2):
    fileToRun = input('Manual or automatic checking: ')
    if fileToRun.lower() == 'manual':
        '''
        with open('./manual.py') as f:
            code = compile(f.read(), './manual.py', 'exec')
            exec(code)
        '''
        manual.main()
    elif fileToRun.lower() == 'automatic':
        '''
        with open('./automatic.py') as f:
            code = compile(f.read(), './automatic.py', 'exec')
            exec(code)
        '''
        automatic.main()

    else:
        print('That file/option does not exist!')