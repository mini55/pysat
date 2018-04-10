import os
from pkg.pysat import solver
solver.logger.setLevel('INFO')

expected_count = 0
actual_sat_count = 0
actual_unsat_count = 0

time = 0

directory = os.path.abspath('uuf50-218')
dirs = sorted(os.listdir(directory))
for file in dirs:
    filename = os.path.abspath(os.path.join(directory, file))
    solv = solver.Solver(filename)
    is_sat, t = solv.run()
    time += t
    if is_sat:
        actual_sat_count += 1
    else:
        actual_unsat_count += 1
    expected_count += 1

print(f'Correct results: {actual_unsat_count}/{expected_count}')
print(f'False positive: {actual_sat_count}')
print(f'Average time used: {time / expected_count:.2f} s')