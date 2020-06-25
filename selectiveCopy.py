import os, pathlib, shutil

for dir, sub, files in os.walk('D:\website_michael_dev'):
    for f in files:
        if f.endswith('html'):
            shutil.copy(os.path.join('D:\website_michael_dev', f),'D:\\testFolder')
