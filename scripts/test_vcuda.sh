set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

pushd "$(dirname "$0")/.." >/dev/null

python3 worker.py --trace config/test_vcuda.csv --log_path results/test_vcuda_results.csv 2>&1 | tee backup_logs/test_vcuda.log

popd >/dev/null