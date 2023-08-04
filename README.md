# OpenData
GenXSecAnalyzer for OpenData

Takes a list of root files (.txt) and outputs the interesting values as a numpy array by one single command line.

### Setup instruction
cmsrel CMSSW_10_6_0
cd CMSSW_10_6_0/src
cmsenv

### To run the GenXSecAnalyhzer:
./calculateXSectionAndFilterEfficiency.sh -f <list_of_root_files.txt> -d <name_of_the_dataset/process> -n <maximum_num_of_events> 

e.g.: ./calculateXSectionAndFilterEfficiency.sh -f DYJetsToLL.txt -d DYJetsToLL -n 10000
Set maximum number of events to -1 to run all the events in each root file
In the example, DYJetsToLL.txt contains a list of root files in the format of "root://eospublic.cern.ch//eos/opendata/"

If you get an error saying "Permisson denied", type "chmod 777 calculateXSectionAndFilterEfficiency.sh" to give the permission to the .sh file first and then rerun the above command.

If we already have .log files, we can run "python output_to_numpy.py" by itself to get the numpy arrays, but the name of the .log file should have the format of xsec_<dataset_name>.log

### To use the outputs:
One .log file and one .npy file for each input filelist (irrelevant unless debugging)
By default, the .json file is automatically generated from the .log file

There are other output formats available, which can be realized by running output_to_csv.py or output_to_numpy.py instead of the dafualt output_to_json.py.

#### For numpy outputs:
To use the output of the GenXSecAnalyzer, we only need to do:
import numpy as np
result = np.load("<dataset_name>.npy")

To access the columns:
result["<column_name>"][0] for value
result["<column_name>"][1] for error
e.g. result["totX_final"][0] gives the value of the final total cross section
     result["totX_final"][0] gives its error

To check all the metadata:
print(result.dtype.metadata)

To check the metadata for a specific column:
print(xsec_arr.dtype.metadata["<column_name>"])
e.g.: print(xsec_arr.dtype.metadata["equivLumi"])

### Column names of the numpy array:
  - 'totX_beforeMat': total cross sections before matchhing 'totX_beforeMat'                                         
  - 'totX_afterMat' : total cross sections after matching                                                                                  
  - 'matchingEff' : matching efficiency                                                                                                                   
  - 'filterEff(weights)' : filter efficiency (weights)                                                                                    
  - 'filterEff(event)' : filter efficiency (event)                                                                                          
  - 'totX_final' : final total cross section                                                                                                 
  - 'negWeightFrac' : negative weight fraction                                                                                              
  - 'equivLumi' : equivalent luminosity 

### Compatible CMSSW versions
Tested with CMSSW_10_6_0

Will test it with other versions soon
