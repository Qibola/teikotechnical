import pandas as pd
import matplotlib.pyplot as plt

# lol
data = pd.read_csv('cell-count.csv', sep='\t')

print("has been loaded")

filtered_results = []
for i in range(len(data)):
    if data['treatment'][i] == 'tr1' and data['condition'][i] == 'melanoma' and data['sample_type'][i] == 'PBMC':
        sample_name = data['sample'][i]
        response = data['response'][i]
        b_cell = data['b_cell'][i]
        cd8_t_cell = data['cd8_t_cell'][i] 
        cd4_t_cell = data['cd4_t_cell'][i]
        nk_cell = data['nk_cell'][i]
        monocyte = data['monocyte'][i]
        
        total = b_cell + cd8_t_cell + cd4_t_cell + nk_cell + monocyte
        
        b_cell_pct = (b_cell/total)*100
        cd8_t_cell_pct = (cd8_t_cell/total)*100
        cd4_t_cell_pct = (cd4_t_cell/total)*100
        nk_cell_pct = (nk_cell/total)*100
        monocyte_pct = (monocyte/total)*100
        
        filtered_results.append([sample_name, response, b_cell_pct, cd8_t_cell_pct, cd4_t_cell_pct, nk_cell_pct, monocyte_pct])

print("has been filtered")

# split data
responder_data = []
non_responder_data = []

for row in filtered_results:
    if row[1] == 'y':
        responder_data.append(row)
    else:
        non_responder_data.append(row)

print("has been split")

cell_types = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']

for i, cell_type in enumerate(cell_types):
    resp_values = []
    non_resp_values = []
    
    for row in responder_data:
        resp_values.append(row[i+2])
    
    for row in non_responder_data:
        non_resp_values.append(row[i+2])
    
    plt.boxplot([resp_values, non_resp_values])
    plt.title(cell_type)
    plt.savefig('plot_' + cell_type + '.png')
    plt.clf()

# calculate averages for findings.txt
print("averages:")
for i, cell_type in enumerate(cell_types):
    resp_values = []
    non_resp_values = []
    
    for row in responder_data:
        resp_values.append(row[i+2])
    
    for row in non_responder_data:
        non_resp_values.append(row[i+2])
    
    resp_avg = sum(resp_values) / len(resp_values)
    non_resp_avg = sum(non_resp_values) / len(non_resp_values)
    
    print(cell_type + ":")
    print("  responders:", round(resp_avg, 1))
    print("  non-responders:", round(non_resp_avg, 1)) 