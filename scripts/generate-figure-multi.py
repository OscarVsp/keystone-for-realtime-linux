import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import inquirer
import argparse
import os

def load(name):
    
    data = pd.read_table(
        name,
        sep=":",
        names=["Thread", "Interval", "Latency"],
        
        skiprows=0,
    )

    print(f'Avg:\t{data["Latency"].mean()}')
    print(f'Std:\t{data["Latency"].std()}')
    print(f'95th:\t{data["Latency"].quantile(q=0.95)}')
    print(f'Max:\t{data["Latency"].max()}')
    return data

def vals(data):
    lat = data["Latency"]
    return {"Min": lat.min(), "Avg": lat.mean(), "Max": lat.max(), "Std": lat.std()}

colors = ['#3498db', '#e67e22', "#5eff3a"]  # Bright blue, Orange
sns.set_palette(sns.color_palette(colors))

bins = 100

def save(ax, name, path):
    fig = ax.get_figure()
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)  # Better than mkdir
    fig.savefig(f"{path}/{name}.png", dpi=600, bbox_inches='tight')

def draw_hist(datas, labels=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    _, bin_edges = np.histogram(datas[-1]["Latency"], bins=bins)
    
    if labels == None:
        labels = [f"dataset_{i}" for i in range(len(datas))]

    for i in range(len(datas)):

        sns.histplot(data=datas[i],
                    x="Latency",
                    bins=bin_edges,
                    color=colors[i],
                    label=labels[i],
                    ax=ax)
    
    
    ax.set_yscale("log")
    ax.set_xlabel("Latency (μs)")
    ax.legend()
    
    return ax

if __name__ == "__main__":


    board = "keystone_hybrid"

    datas = []
    labels = []

    target_path = f"results/{board}/realtime"
    target_name_prefix = f"{board}_realtime_1"
    datas.append(load(f"{target_path}/{target_name_prefix}_cyclictest.log"))
    labels.append(f"1 thread")

    target_name_prefix = f"{board}_realtime_2"
    datas.append(load(f"{target_path}/{target_name_prefix}_cyclictest.log"))
    labels.append(f"2 threads")

    """target_path = f"results/{board}/realtime"
    target_name_prefix = f"{board}_realtime_3"
    datas.append(load(f"{target_path}/{target_name_prefix}_cyclictest.log"))
    labels.append(f"rt (3 threads)")  """      
    
       
    ax = draw_hist(datas=datas, labels=labels)

    save(ax, f"{board}_realtime_histo_1-{len(datas)}", f"results/{board}/realtime")

    ax.clear()


    

    


