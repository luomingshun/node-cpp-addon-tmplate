from optparse import OptionParser
import zipfile
import os

DST_DIR=None
PROJECT_NAME=None


def parseOpt():
    global DST_DIR,PROJECT_NAME
    try:
        opt=OptionParser()
        opt.add_option("--dst-dir",dest="dst_dir",type=str,help="where to put the project,recomend a empty dir")
        opt.add_option("--prj-name",dest="prj_name",type=str,help="your project name")
        options,args=opt.parse_args()

        DST_DIR=options.dst_dir
        PROJECT_NAME=options.prj_name

        if not DST_DIR or not PROJECT_NAME:
            opt.print_help()
            exit()
    except:
        opt.print_help()
        exit()

if __name__=="__main__":

	parseOpt()
	
	template = zipfile.ZipFile("tmplate.zip")
	for file in template.namelist():

		template.extract(file,DST_DIR)
		file_path=DST_DIR+os.sep+file
		if not os.path.isfile(file_path) or file_path.endswith(".txt"):
			continue
		src=open(file_path,"r")
		content=src.readlines()
		src.close()
		dst=open(file_path,"w")
		for line in content:
			dst.write(line.replace("$$PROJECT_NAME$$",PROJECT_NAME))
		dst.close()

