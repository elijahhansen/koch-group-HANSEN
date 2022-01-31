
import numpy as np
import scqubits as scq
import matplotlib.pyplot as plt


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

def get_indices_array(approx_evals, reference_evals, desired_accuracy_threshold, offset):
    # energy_level starts at 0 (ground state)
    # reference_evals = get_reference_evals(user_ej,user_ec,user_ng,reference_ncut,levels_count)
    # approx_evals = get_approx_evals(min_range,max_range,energy_level_count)
    accuracy_values = get_accuracy_values(approx_evals, reference_evals)
    column_count = approx_evals.shape[1]
    locations = np.empty(column_count)
    for i, column in enumerate(accuracy_values.T):
        column_locations = np.argwhere(column < desired_accuracy_threshold).flatten()
        locations[i] = column_locations[0]
    return locations #+offset

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

result = get_required_ncut(5,1,0,15)
print(0)






