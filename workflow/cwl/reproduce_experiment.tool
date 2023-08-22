#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool

requirements:
  DockerRequirement:
    dockerPull:
      openml/openml-python:develop

baseCommand: python

inputs:
  reproduce_experiment:
    type: File
    inputBinding:
      position: 0
  outputfile:
    type: string
    inputBinding:
      prefix: --outputfile

outputs:
  result:
    type: File
    outputBinding:
      glob: $(inputs.outputfile)