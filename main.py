import os, shutil
src=os.path.join(os.path.dirname(os.path.abspath(__file__)),'entry.png')
o=os.environ.get('MAKEFUN_OUTPUT_DIR','/output')
os.makedirs(o,exist_ok=True)
shutil.copyfile(src,os.path.join(o,'entry.png'))
