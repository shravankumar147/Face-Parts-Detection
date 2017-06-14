import os

flist = os.listdir("results/")

print(flist)

with open("result_write.txt","w") as f:
	for i in flist:
		# ![Alt](results/face0_mouth.png)
		f.write("![Alt](results/{})\n".format(i))
