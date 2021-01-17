#import automatic
#import manual

# def main():
for i in range(2):
    fileToRun = input('Manual or automatic checking: ')
    if fileToRun.lower() == 'manual':
        with open('./class1/manual.py') as f:
            code = compile(f.read(), './class1/manual.py', 'exec')
            exec(code)
    elif fileToRun.lower() == 'automatic':
        with open('./class1/automatic.py') as f:
            code = compile(f.read(), './class1/automatic.py', 'exec')
            exec(code)
    else:
        print('That file/option does not exist!')