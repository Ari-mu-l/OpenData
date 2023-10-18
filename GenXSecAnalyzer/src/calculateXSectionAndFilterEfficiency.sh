FILE='recid_16421.txt'
DATANAME='Drell-Yan'
EVENTS='10'

#SKIPEXISTING=False

while getopts f:d:n:s option
do
    case "${option}"
    in
            f) FILE=${OPTARG};;
            d) DATANAME=${OPTARG};;
            n) EVENTS=${OPTARG};;
            s) SKIPEXISTING=False;;
    esac
done

echo "python src/compute_cross_section.py -f '${FILE}' -d '${DATANAME}' -n '${EVENTS}' --skipexisting '${SKIPEXISTING}'"
output="$(python src/compute_cross_section.py -f "${FILE}" -d "${DATANAME}" -n "${EVENTS}" --skipexisting "${SKIPEXISTING}")"
output="${output#*.txt}"
output="${output#*.txt}"

if [[ $output == *"cmsRun"* ]]; then
    eval ${output}
else
    echo ${output}
fi
echo ""

python src/output_to_json.py "${FILE}" "${DATANAME}"
