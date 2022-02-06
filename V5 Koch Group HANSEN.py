
import numpy as np
import scqubits as scq


#new_approx_array fills an empty np array with NaN and replaces each in a for loop with the appropriate eigenvals
# for each ncut
#then must use those reference eigenvals in each element to have accuracy values (error) for each approximation
#then must find each element that is below the desired accuracy threshold and put them into an array
def new_approx_array(tmon, max_ncut):
    storage_array = np.empty(shape=(max_ncut,2*max_ncut+1))
    storage_array[:] = np.NaN
    ref = tmon.eigenvals(evals_count= max_ncut)
    for row_index, my_ncut in enumerate(range(1,max_ncut+1)):
        tmon.ncut = my_ncut
        storage_array[row_index, 0:2*my_ncut+1] = tmon.eigenvals(evals_count = 2*my_ncut+1)
    accuracy_values = np.zeros_like(storage_array)
    for i,rows in enumerate(storage_array):
        relative_deviation_table=(rows-ref)/ref
        accuracy_values[i,:]=np.abs(relative_deviation_table)
    return storage_array

def get_indices_array(storage_array, desired_accuracy_threshold, offset):
    # energy_level starts at 0 (ground state)
    # reference_evals = get_reference_evals(user_ej,user_ec,user_ng,reference_ncut,levels_count)
    # approx_evals = get_approx_evals(min_range,max_range,energy_level_count)
    #accuracy_values = get_accuracy_values(approx_evals, reference_evals)
    column_count = storage_array.shape[1]
    locations = np.empty(column_count)
    for i, column in enumerate(storage_array.T):
        column_locations = np.argwhere(column < desired_accuracy_threshold).flatten()
        locations[i] = column_locations[0]
    print(locations)
    return locations + offset












#test test

