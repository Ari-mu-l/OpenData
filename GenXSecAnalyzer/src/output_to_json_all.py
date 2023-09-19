import os, sys
import json

file_list = ["logs/"+f for f in os.listdir("logs") if f.startswith("xsec") and f.endswith(".log")]

fields = ['totX_beforeMat', 'totX_beforeMat_err', 'totX_afterMat', 'totX_afterMat_err', 'matchingEff', 'matchingEff_err', 'filterEff(weights)', 'filterEff(weights)_err', 'filterEff(event)', 'filterEff(event)_err', 'totX_final', 'totX_final_err', 'negWeightFrac', 'negWeightFrac_err', 'equivLumi', 'equivLumi_err']

metadata = [{"metadata":{"totX_beforeMat":"Total cross section before matching (pb)",
                         "totX_afterMat":"Total cross section after matching (pb)",
                         "matchingEff":"Matching efficiency",
                         "filterEff(weights)":"Filter efficiency (taking into account weights)",
                         "filterEff(event)":"Filter efficiency (event-level)",
                         "totX_final":"Final cross senction after filter (pb)",
                         "negWeightFrac":"Final fraction of events with negative weights after filter",
                         "equivLumi":"Final equivalent lumi for 1M events (1/fb)", }}]

for fname in sorted(file_list):

    with open(fname) as f:
        contents = f.read().split("\n")

        try:
            dset = fname.split("xsec_")[-1].split(".")[0] # dataset name

            totX_beforeMat = [c for c in contents if "Before matching: total cross section" in c][0].split("= ")[-1].split() # val and err
            totX_afterMat = [c for c in contents if "After matching: total cross section" in c][0].split("= ")[-1].split()
            matchingEff = [c for c in contents if "Matching efficiency" in c][0].split("= ")[-1].split()
            filterEffWeights = [c for c in contents if "Filter efficiency (taking into account weights)" in c][0].split("= ")[-1].split()
            filterEffEvent = [c for c in contents if "Filter efficiency (event-level)" in c][0].split("= ")[-1].split()
            totX_final = [c for c in contents if "After filter: final cross section" in c][0].split("= ")[-1].split()
            negWeightFrac = [c for c in contents if "After filter: final fraction of events with negative weights" in c][0].split("= ")[-1].split()
            equivLumi = [c for c in contents if "final equivalent lumi for 1M events (1/fb)" in c][0].split("= ")[-1].split()

            rows = ['0.0']*16

            rows[0] = totX_beforeMat[0]
            rows[1] = totX_beforeMat[2]

            rows[2] = totX_afterMat[0]
            rows[3] = totX_afterMat[2]

            rows[4] = matchingEff[0]
            rows[5] = matchingEff[2]

            rows[6] = filterEffWeights[0]
            rows[7] = filterEffWeights[2]

            rows[8] = filterEffEvent[0]
            rows[9] = filterEffEvent[2]

            rows[10] = totX_final[0]
            rows[11] = totX_final[2]

            rows[12] = negWeightFrac[0]
            rows[13] = negWeightFrac[2]

            rows[14] = equivLumi[0]
            rows[15] = equivLumi[2]

            data = dict(zip(fields, rows))

            metadata.append(data)

            outfile = '/eos/user/s/sxiaohe/OpenData/MC2015/StandardModelPhysics/{}/recid_{}.json'.format(sys.argv[1], dset)
            with open(outfile, 'w') as jsonfile:
                json.dump(metadata, jsonfile)
            print("Saved to {}".format(outfile))
            
        except:
	    print("Save to json failed {}".format(fname))
