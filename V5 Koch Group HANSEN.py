
import numpy as np
import scqubits as scq



def get_approx_evals(min_range,max_range,energy_level_count,transmon):
    ncut_vals = np.arange(min_range,max_range)
    specdata = transmon.get_spectrum_vs_paramvals('ncut', ncut_vals, evals_count = energy_level_count)
    return specdata.energy_table

def get_accuracy_values(approx_evals,reference_evals):
    accuracy_values=np.zeros_like(approx_evals)
    for i,rows in enumerate(approx_evals):
        relative_deviation_table=(rows-reference_evals)/reference_evals
        accuracy_values[i,:]=np.abs(relative_deviation_table)
    return accuracy_values

def get_indices_array(approx_evals, reference_evals, desired_accuracy_threshold,offset):
    # energy_level starts at 0 (ground state)
    # reference_evals = get_reference_evals(user_ej,user_ec,user_ng,reference_ncut,levels_count)
    # approx_evals = get_approx_evals(min_range,max_range,energy_level_count)
    accuracy_values = get_accuracy_values(approx_evals, reference_evals)
    column_count = approx_evals.shape[1]
    locations = np.empty(column_count)
    for i, column in enumerate(accuracy_values.T):
        column_locations = np.argwhere(column < desired_accuracy_threshold).flatten()
        locations[i] = column_locations[0]
    return locations + offset

# to obtain the 15 eigenvalues, need at least ncut=7 because dim=2ncut+1

def get_required_ncut(ej, ec, ng, levels_count, desired_accuracy_threshold=1e-06):
    reference_ncut = 50
    min_ncut = int(np.ceil((levels_count - 1) / 2))
    max_ncut = 50
    tmon = scq.Transmon(ej, ec, ng, reference_ncut)
    reference_evals = tmon.eigenvals(evals_count=levels_count)
    approx_evals = get_approx_evals(min_ncut, max_ncut, levels_count, tmon)
    accuracy_values = get_accuracy_values(approx_evals, reference_evals)
    indices_array = get_indices_array(approx_evals, reference_evals, desired_accuracy_threshold, min_ncut)
    return indices_array



#new_reference_array fills an empty np array with NaN and replaces each in a for loop with the appropriate eigenvals
# for each ncut
#then must use those reference eigenvals in each element to have accuracy values (error) for each approximation
#then must find each element that is below the desired accuracy threshold and put them into an array
def new_reference_array(tmon, m):
    storage_array = np.empty(shape=(m,2*m+1))
    storage_array[:] = np.NaN
    for row_index, my_ncut in enumerate(range(1,m+1)):
        tmon.ncut = my_ncut
        storage_array[row_index, 0:2*my_ncut+1] = tmon.eignvals(evals_count = 2*my_ncut+1)

    return storage_array






#test test

