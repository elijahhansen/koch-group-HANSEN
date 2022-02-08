
import numpy as np
import scqubits as scq


#new_approx_array fills an empty np array with NaN and replaces each in a for loop with the appropriate eigenvals
# for each ncut
#then must use those reference eigenvals in each element to have accuracy values (error) for each approximation
#then must find each element that is below the desired accuracy threshold and put them into an array
def get_accuracy_values(tmon, max_ncut, levels_count):
    min_ncut = levels_count/2 -1
    storage_array = np.empty(shape=(max_ncut,2*max_ncut+1))
    storage_array[:] = np.NaN
    ref = tmon.eigenvals(evals_count= 2*max_ncut+1)
    accuracy_values = np.zeros_like(storage_array)
    for row_index, my_ncut in enumerate(range(1,max_ncut+1)):
        tmon.ncut = my_ncut
        approx_value = tmon.eigenvals(evals_count=2 * my_ncut + 1)
        storage_array[row_index, 0:2*my_ncut+1] = approx_value
        relative_deviation_table = (approx_value-ref[2*my_ncut+1])/ref[2*my_ncut+1]
        accuracy_values[row_index, :] = np.abs(relative_deviation_table)

        #now lets add a modified version of the get_indices_array function, but it does its work inside the for
        # loop in which we can ask it if it has satisfied its condition at each iteration
        #want to return a boolean for each eigenvalues' respective accuracy value up to levels count (if all true then
        # good)
        #change the range for the for loop
        # iterate through and give each accuracy a boolean value
        # break when an entire row is satisfactory
        # can do a row per iteration and assign the result to a boolean variable
        # when that variable is true then break and return row index




    # lets try to condense these two for loops so that we can calculate accuracy values on the fly
    # this means calculating accuracy values and chopping off the useless NaNs we dont need


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

tmon = scq.Transmon(EJ=10, EC=1, ng=0, ncut=50)

result = get_accuracy_values(tmon, 50)












#test test

