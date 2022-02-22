
import numpy as np
import scqubits as scq


#new_approx_array fills an empty np array with NaN and replaces each in a for loop with the appropriate eigenvals
# for each ncut
#then must use those reference eigenvals in each element to have accuracy values (error) for each approximation
#then must find each element that is below the desired accuracy threshold and put them into an array
def get_required_ncut(tmon, max_ncut, levels_count, desired_accuracy_threshold = 1e-06):
    min_ncut= int(levels_count/2 -1)
    storage_array = np.empty(shape=(max_ncut,2*max_ncut+1))
    storage_array[:] = np.NaN
    ref = tmon.eigenvals(evals_count= 2*max_ncut+1)
    accuracy_values = np.zeros_like(storage_array)
    for row_index, my_ncut in enumerate(range(min_ncut,max_ncut)):
        tmon.ncut = my_ncut
        approx_value = tmon.eigenvals(evals_count=2 * my_ncut + 1)
        storage_array[row_index, 0:2*my_ncut+1] = approx_value
        relative_deviation_table = (approx_value-ref[0:2*my_ncut+1]) / ref[0:2*my_ncut+1]

        accuracy_values[row_index, 0:2*my_ncut+1] = np.abs(relative_deviation_table)
        threshold_array = np.ones(levels_count)*desired_accuracy_threshold
        if (accuracy_values[row_index, 0:levels_count-1] < threshold_array[0:levels_count-1]).all():
            return my_ncut

tmon = scq.Transmon(EJ=10, EC=1, ng=0, ncut=100)

result = get_required_ncut(tmon, 100, 100)
print(result)

        ####TODO#####
        # debug and manually inspect code line by line accuracy values array for a sanity check of threshold values
        #generalize code to work with other 1-dimensional systems (fluxonium) and 0 pi
        # can give a condition based on whether user gives transmon or fluxonium
        #try to get values for a plot
        #explore floxonium


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
















#test test

