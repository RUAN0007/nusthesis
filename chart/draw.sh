#!/bin/bash

# 1>filename # Redirect stdout to file "filename."
# 1>>filename # Redirect and append stdout to file "filename."
# 2>filename # Redirect stderr to file "filename."
# 2>>filename # Redirect and append stderr to file "filename."
# 2>&1 # Redirects stderr to stdout.
# >>filename 2>&1 # Error messages get sent to same place as standard output.
# timeout --foreground 60m "$cmd" | tee "$logFile" # Run a cmd with 60 min to timout. Show in console and Redirect the stdout to write to $logFile. Preserve status code of $cmd to $?. --foreground to allow for interrupt

# "$cmd" > >(tee stdout.log) 2> >(tee stderr.log >&2) Show in console both stdout and stderr while directing them to direct log files.

# set -e # exit when a cmd fails
set -u # exit when using undeclared env var
set -o pipefail # Save exit code after pipelining to tee
# set -x # trace what gets executed

# Double brackets for testing condition without the need for double quotes for the interpolated variable
# if [[ $# -ne 1 ]]; then
#     echo "Illegal number of parameters"
#     exit 1
# fi


prevDir=$(pwd)

# Double quotes around every parameter expansion "$var"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

# . env.sh  # for any environment variable

trap ctrl_c INT
function ctrl_c() {
  echo "** Trapped CTRL-C. Revert back to calling directory $prevDir"
  cd "$prevDir"
}

function main() {
  if [ "${1:-all}" = "all" ]; then
    chapters=("intro" "provenance" "txn") # the twin study script is managed separately
  else
    chapters=("$@")
  fi

  for chapter in ${chapters[@]}; do
    for script_path in script/${chapter}_*.py; do
        # echo $script_path
        chart_path=$(echo $script_path | cut -d'_' -f2-) # exclude the chapter prefix
        chart_name=$(basename $chart_path .py)
        echo "Drawing $chart_name for Chapter $chapter"

        python script/${chapter}_${chart_name}.py ${chapter}/${chart_name}.pdf
    done
  done
}

main "$*"
status="$?"

cd "$prevDir"  # Revert back to the calling directory
exit "$status"