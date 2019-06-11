#This is a Nipype generator. Warning, here be dragons.
#!/usr/bin/env python

import sys
import nipype
import nipype.pipeline as pe

import nipype.interfaces.freesurfer as freesurfer

#Wraps the executable command ``mri_segment``.
freesurfer_SegmentWM = pe.Node(interface = freesurfer.SegmentWM(), name='freesurfer_SegmentWM')
freesurfer_SegmentWM.inputs.in_file = 'brain.nii'

#Wraps the executable command ``mris_volsmooth``.
freesurfer_Smooth = pe.Node(interface = freesurfer.Smooth(), name='freesurfer_Smooth')

#Create a workflow to connect all those nodes
analysisflow = nipype.Workflow('MyWorkflow')
analysisflow.connect(freesurfer_SegmentWM, "out_file", freesurfer_Smooth, "in_file")

#Run the workflow
plugin = 'MultiProc' #adjust your desired plugin here
plugin_args = {'n_procs': 1} #adjust to your number of cores
analysisflow.write_graph(graph2use='flat', format='png', simple_form=False)
analysisflow.run(plugin=plugin, plugin_args=plugin_args)
