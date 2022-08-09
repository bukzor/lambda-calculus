#!/bin/sh
set -eu
HERE="$(cd "$(dirname "$0")"; pwd)"
TOP="$(cd "$HERE/../.."; pwd)"

set -x
cd "$TOP"

python3 -m lambda_calculi.system_f_omega.grammar_definition |
  tee lambda_calculi/system_f_omega/grammar_definition.md

python3 -m lambda_calculi.system_f_omega.inference.type_formation |
  tee lambda_calculi/system_f_omega/inference_definition.md
