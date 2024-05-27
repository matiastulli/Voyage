import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_excel('wf_dependencies.xlsx')

source_df = df['source']
wf_name_df = df['wf_name']

G = nx.DiGraph()

for source, wf_name in zip(source_df, wf_name_df):
    G.add_edge(source, wf_name)

sources = set(source_df)
workflows = set(wf_name_df)

pos = nx.spring_layout(G)

for node in pos:
    if node in sources:
        pos[node][0] = -1  
    else:
        pos[node][0] = 1   

plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True, arrowstyle='-|>', arrowsize=20, edge_color='gray')

plt.title("Workflow Dependencies", fontsize=15)

plt.show()
