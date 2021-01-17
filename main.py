
classToRun = input('What class: ')
'''
import os
command = 'cd class' + classToRun + ' && python main.py'
print(command)
os.system(command)
'''
'''
with open('./class' + classToRun + '/main.py') as f:
    code = compile(f.read(), './class' + classToRun + '/main.py', 'exec')
    exec(code)
'''

import runpy
runpy.run_path('./class' + classToRun + '/main.py')