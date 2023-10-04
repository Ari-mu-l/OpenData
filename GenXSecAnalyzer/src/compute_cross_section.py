# EXAMPLE ON HOW TO RUN
# python ./compute_cross_section.py -f datasets.txt -d process

from optparse import OptionParser
import os
import sys
import commands
import re
import datetime
from time import sleep

def str_to_bool(s):
    if s == 'True':
         return True
    elif s == 'False':
         return False

if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option('-f', '--file'        , dest="inputFilelist",      default='',       help='input text file of root files')
    parser.add_option('-d', '--dataset'     , dest='datasetName',   default='',       help='name of the dataset')
    parser.add_option('-n', '--events'      , dest="events",        default=int(1e6), help='number of events to calculate the cross section')
    parser.add_option('-s', '--skipexisting', dest="skipexisting",  default=False,    help='skipexisting existing output files containing xsec results')

    (args, opts) = parser.parse_args(sys.argv)

    skipexisting = str_to_bool(str(args.skipexisting))
    
    if skipexisting and os.path.isfile("xsec_"+str(args.datasetName)+".log"): 
        print "xsec_"+str(args.datasetName)+".log existing and NO skipexisting asked, skipping"
    else:
        filelist = open(args.inputFilelist, 'r').read().split('\n')
        inputFiles = ""
        for rootfile in filelist:
            if('root' in rootfile):
                inputFiles += ' inputFiles='+rootfile + ' '
   
        # compute cross section
        recId = args.inputFilelist.split('_')[1].split('.')[0]

        command = 'cmsRun src/genXSecAnalyzer_cfg.py {} maxEvents={} 2>&1 | tee logs/{}/xsec_{}.log'.format(inputFiles, str(args.events), args.datasetName, recId)
        #command = 'cmsRun src/genXSecAnalyzer_cfg.py'+inputFiles+' maxEvents='+str(args.events)+" 2>&1 | tee logs/"+args.datasetName+"/xsec_"+recId+".log"
        print command