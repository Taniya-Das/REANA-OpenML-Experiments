#!/usr/bin/env cwl-runner


cwlVersion: v1.0
class: Workflow

inputs:
  reproduce_experiment: File
  inputfile: File
  outputfile:
    type: string
    default: results/output.txt

outputs:
  result:
    type: File
    outputSource: first/result

steps:
  first:
    run: reproduce_experiment.tool
    in:
      reproduce_experiment: reproduce_experiment
      outputfile: outputfile
    out: [result]