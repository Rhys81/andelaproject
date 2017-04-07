def presentation():
	alist=out_put(username,day)
	name=alist[0]
	day=alist[1]
	taskdone=alist[2:]

	print('********************************************\n'\
				"Progress report for %s" %name) 
	print('********************************************')
	print('DAY: %s:\tTasks done:\t'%day)
	print('*********************************************')
	print taskdone