from logcheck import LogCheck

work_dir = '/home/dylan/Downloads/pbs_server_logs/'
file_name = '20160614'

l = LogCheck()
l.readfile(work_dir + file_name)

for log in l.nodes['comp147']:
    print(log)
