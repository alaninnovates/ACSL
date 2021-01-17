import os
classToRun = input('What class: ')
os.chdir('class' + classToRun)
os.system('python main.py')
'''
with open('./class' + classToRun + '/main.py') as f:
    code = compile(f.read(), './class' + classToRun + '/main.py', 'exec')
    exec(code)



import runpy
runpy.run_path('./class' + classToRun',   'main.py')
'''