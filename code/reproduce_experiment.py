# -*- coding: utf-8 -*-

"""REANA-Demo-Run OpenML experiment"""

import os
import openml
import warnings
import errno


def run_exp(outputfile="results/output.txt"):
    
    
    # ensure output directory exists:
    # influenced by http://stackoverflow.com/a/12517490
    if not os.path.exists(os.path.dirname(outputfile)):
        try:
            os.makedirs(os.path.dirname(outputfile))
        except OSError as exc:  # guard against race condition
            if exc.errno != errno.EEXIST:
                raise
            
    # write greetings:
    with open(outputfile, "at") as f:
        
        openml.config.start_using_configuration_for_example()
        warnings.simplefilter(action='ignore', category=FutureWarning)
        
        MAX_EXP = 2
        runs = openml.runs.list_runs(size = MAX_EXP)

        for key, run_ in runs.items():
            run_id = run_['run_id']
        
            # Run original
            run_original = openml.runs.get_run(run_id)
            
            print('Running Experiment number ', key)
            
            # Download the flow and solve the same task again.
            setup_id = run_['setup_id']
            model_duplicate = openml.setups.initialize_model(setup_id)
            
            #flow = openml.flows.get_flow(run_['flow_id'])
            task = openml.tasks.get_task(run_['task_id'])

            run_duplicate = openml.runs.run_model_on_task(model_duplicate, task = task, avoid_duplicate_runs=False)
            predictions = run_duplicate.data_content
            
            entry = f"\n Experiment number {key}: {run_duplicate}\n"
            f.write("{}".format(entry))
            # f.write("{}".format(predictions))
            f.flush()
            
        openml.config.stop_using_configuration_for_example()
    f.close()
    
    return 

if __name__ == '__main__':
    
    run_exp(outputfile="results/output.txt")
    
    


   
    
    

    
    