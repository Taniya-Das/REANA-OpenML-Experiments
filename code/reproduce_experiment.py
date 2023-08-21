import openml
import warnings
import numpy as np

openml.config.start_using_configuration_for_example()
warnings.simplefilter(action='ignore', category=FutureWarning)


MAX_EXP = 10
runs = openml.runs.list_runs(size = MAX_EXP)

for key, run_ in runs.items():
    run_id = run_['run_id']
    
    # breakpoint()
    # Run original
    run_original = openml.runs.get_run(run_id)
    
    print('Experiment number : ', key)
    
    # Download the flow and solve the same task again.
    setup_id = run_['setup_id']
    model_duplicate = openml.setups.initialize_model(setup_id)
    
    #flow = openml.flows.get_flow(run_['flow_id'])
    task = openml.tasks.get_task(run_['task_id'])

    run_duplicate = openml.runs.run_model_on_task(model_duplicate, task = task, avoid_duplicate_runs=False)
    
    # results already published. No need to publish again  
    # myrun = run_duplicate.publish()
    
    print(run_duplicate)
    print(f"Run was uploaded to {run_original.openml_url}")
    
    
    # # the run has stored all predictions in the field data content
    # np.testing.assert_array_equal(run_original.data_content, run_duplicate.data_content)
    # print("Predictons: ", run_duplicate.data_content)
    
    
openml.config.stop_using_configuration_for_example()
    
    