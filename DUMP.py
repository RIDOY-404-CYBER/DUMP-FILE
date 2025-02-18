import os,platform  #os.system('xdg-open https://facebook.com/groups/770617227293870/')
os.system('git pull')
rmx = platform.architecture()[0]
if rmx=='64bit':
    import DMP3
elif rmx=='32bit':
    print("[×] your Device not Supported");exit()
