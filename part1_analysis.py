import pandas as pd

# load data lol its a csv file pasted and separted by tabs #stackoverflow
data = pd.read_csv('cell-count.csv', sep='\t')

print("loaded data")

results = []

for i in range(len(data)):
    sample_name = data['sample'][i]
    b_cell = data['b_cell'][i]
    cd8_t_cell = data['cd8_t_cell'][i] 
    cd4_t_cell = data['cd4_t_cell'][i]
    nk_cell = data['nk_cell'][i]
    monocyte = data['monocyte'][i]
    
    total = b_cell + cd8_t_cell + cd4_t_cell + nk_cell + monocyte
    
    results.append([sample_name, total, 'b_cell', b_cell, (b_cell/total)*100])
    results.append([sample_name, total, 'cd8_t_cell', cd8_t_cell, (cd8_t_cell/total)*100])
    results.append([sample_name, total, 'cd4_t_cell', cd4_t_cell, (cd4_t_cell/total)*100])
    results.append([sample_name, total, 'nk_cell', nk_cell, (nk_cell/total)*100])
    results.append([sample_name, total, 'monocyte', monocyte, (monocyte/total)*100])

output = pd.DataFrame(results, columns=['sample', 'total_count', 'population', 'count', 'percentage'])
output.to_csv('relative_frequencies.csv', index=False)

print("saved results")
print(output.head()) 