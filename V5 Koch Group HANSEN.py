
import numpy as np
import scqubits as scq


#new_approx_array fills an empty np array with NaN and replaces each in a for loop with the appropriate eigenvals
# for each ncut
#then must use those reference eigenvals in each element to have accuracy values (error) for each approximation
#then must find each element that is below the desired accuracy threshold and put them into an array
def float_helper(values, q):
    px = np.ceil(np.log10(abs(values)))
    ix = (values * 10 ** (-px + q)).astype(int)
    return ix

def get_required_ncut(tmon, max_ncut, levels_count): #for example here it could be 6 significant digits)
    min_ncut = int(np.ceil((levels_count-1)/2))
    ##storage_array = np.empty(shape=(max_ncut, 2*max_ncut+1))
    ##storage_array[:] = np.NaN
    ref = float_helper(tmon.eigenvals(evals_count=levels_count), 6)
    ## we want to format the ref and approx values into strings, divide by the exponent in sci notation.
    ##accuracy_values = np.zeros_like(storage_array)
    for row_index, my_ncut in enumerate(range(min_ncut, max_ncut)):
        tmon.ncut = my_ncut
        approx_value = float_helper(tmon.eigenvals(evals_count=levels_count), 6)
        if np.array_equal(ref,approx_value):
            return my_ncut


tmon = scq.Transmon(EJ=100, EC=1, ng=0, ncut=50)

result = get_required_ncut(tmon, 50, 10)
print(result)


        ####TODO#####
        #reformat code to find number of significant digits instead of relative accuracy valuesm - will need to reformat eigen-energies and find appropriate number
        # of significant digits
        # debug and manually inspect code line by line accuracy values array for a sanity check of threshold values
        # generalize code to work with other 1-dimensional systems (fluxonium) and 0 pi
        # can give a condition based on whether user gives transmon or fluxonium
        # try to get values for a plot
        # explore floxonium
        # explore integration with tunable transmon


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
    #





#this is a transmon hamiltonian with three levels truncated to ncut=10











#test test

