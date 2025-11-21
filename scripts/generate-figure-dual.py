import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import inquirer
import argparse
import os

def load(name, cpu=4):
    
    data = pd.read_table(
        name,
        sep=":",
        names=["Thread", "Interval", "Latency"],
        
        skiprows=9,
    )

    print(f'Avg:\t{data["Latency"].mean()}')
    print(f'Std:\t{data["Latency"].std()}')
    print(f'95th:\t{data["Latency"].quantile(q=0.95)}')
    print(f'Max:\t{data["Latency"].max()}')
    return data

def vals(data):
    lat = data["Latency"]
    return {"Min": lat.min(), "Avg": lat.mean(), "Max": lat.max(), "Std": lat.std()}

colors = ['#3498db', '#e67e22']  # Bright blue, Orange
sns.set_palette(sns.color_palette(colors))

bins = 100

def save(ax, name, path):
    fig = ax.get_figure()
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)  # Better than mkdir
    fig.savefig(f"{path}/{name}.png", dpi=600, bbox_inches='tight')

def draw_hist(data1, data2, label1="Dataset 1", label2="Dataset 2"):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    _, bin_edges = np.histogram(data1["Latency"], bins=bins)
    

    # Plot first histogram
    sns.histplot(data=data1,
                 x="Latency",
                 bins=bin_edges,
                 color=colors[0],
                 label=label1,
                 ax=ax)
    
    # Plot second histogram on the same axes
    sns.histplot(data=data2,
                 x="Latency",
                 bins=bin_edges,
                 color=colors[1] if len(colors) > 1 else 'orange',
                 label=label2,
                 alpha=0.6,
                 ax=ax)
    
    
    ax.set_yscale("log")
    ax.set_xlabel("Latency (μs)")
    ax.legend()
    
    return ax

if __name__ == "__main__":


    boards = [ "keystone_hybrid"]
    kernels = ["stock","realtime"]
    cpu = 4

    for board in boards:

        print(f'--- {board} ---')
        target_path_stock = f"results/{board}/{kernels[0]}"
        target_name_prefix = f"{board}_{kernels[0]}_1"
        data_stock = load(f"{target_path_stock}/{target_name_prefix}_cyclictest.log", cpu)

        target_path_rt = f"results/{board}/{kernels[1]}"
        target_name_prefix_rt = f"{board}_{kernels[1]}_1"
        data_rt = load(f"{target_path_rt}/{target_name_prefix_rt}_cyclictest.log", cpu)

        ax = draw_hist(data1=data_stock, data2=data_rt, label1= f"{kernels[0]}", label2=f"{kernels[1]}")

        save(ax, f"{board}_histo", f"results/{board}")

        ax.clear()



    exit(0)

    

    


