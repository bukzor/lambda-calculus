#!/bin/sh
set -eu
HERE="$(cd "$(dirname "$0")"; pwd)"
TOP="$(cd "$HERE/../.."; pwd)"

set -x
cd "$TOP"

python3 -m lambda_calculi.system_f.grammar_definition |
  tee lambda_calculi/system_f/grammar_definition.md
