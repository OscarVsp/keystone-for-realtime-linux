import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator
import numpy as np
import pandas as pd
import seaborn as sns
import os

def load(name, start_skip = 0, skiprows=9):
    
    data = pd.read_table(
        name,
        sep=":",
        names=["Thread", "Interval", "Latency"],
        
        skiprows=skiprows,
    )

    if start_skip > 0:
        data = data.iloc[start_skip:]

    print(f'N:\t{len(data['Latency'])}')
    print(f'Avg:\t{data["Latency"].mean()}')
    print(f'Std:\t{data["Latency"].std()}')
    print(f'95th:\t{data["Latency"].quantile(q=0.95)}')
    print(f'Max:\t{data["Latency"].max()}')
    return data


def draw_hist(datas, labels=None, alphas=None, bins=100, colors = ["#1053cf", "#e69822", "#818181"], unit='us', x_log = False, bin_edges=None):
    plt.rcParams.update({
        'font.size': 20,           # Base font size
        'axes.labelsize': 22,      # Axis labels
        'axes.titlesize': 22,      # Title
        'xtick.labelsize': 20,     # X-axis tick labels
        'ytick.labelsize': 20,     # Y-axis tick labels
        'legend.fontsize': 20,     # Legend
        'figure.titlesize': 24     # Figure title
    })

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.set_palette(sns.color_palette(colors))

    datas_plot = []

    for i, data in enumerate(datas):
        data_temp = data.copy()
        if unit.lower() == 'ms':
            data_temp["Latency"] = data_temp["Latency"] / 1000
        datas_plot.append(data_temp)

    if unit.lower() == 'ms':
        unit_label = "Latency (ms)"
    else:  # default to microseconds
        unit_label = "Latency (μs)"
        
    min_sample_size = min(len(datas_plot[i]["Latency"]) for i in range(len(datas_plot)))     
    combined_min = min(datas_plot[i]["Latency"].min() for i in range(len(datas_plot)))
    combined_max = max(datas_plot[i]["Latency"].max() for i in range(len(datas_plot)))

    if bin_edges is None:
        if x_log:
            bin_edges = np.logspace(np.log10(combined_min), np.log10(combined_max), bins + 1)
        else:
            bin_edges = np.linspace(combined_min, combined_max, bins + 1)

    if alphas == None:
        alphas = [0.8 for _ in range(len(datas))]

    if labels == None:
        labels = [f"dataset_{i}" for i in range(len(datas))]

    for i in range(len(datas)):
        normalization_factor = len(datas_plot[i]["Latency"]) / min_sample_size
        
        counts, _ = np.histogram(datas_plot[i]["Latency"], bins=bin_edges)
        normalized_counts = counts / normalization_factor
        
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
        bin_width = bin_edges[1:] - bin_edges[:-1]
        ax.bar(bin_centers, normalized_counts, width=bin_width, 
               color=colors[i], label=labels[i], alpha=alphas[i])
    
    ax.set_yscale("log")
    if x_log:
        ax.set_xscale("log")
    ax.set_xlabel(unit_label, fontsize=22)
    ax.set_ylabel("Count", fontsize=22)
    if len(datas) > 1:
        ax.legend(fontsize=20)


    ax.tick_params(axis='both', which='major', labelsize=18)
    
    return ax

def save(ax, name, path):
    fig = ax.get_figure()
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)
    fig.savefig(f"{path}/{name}.png", dpi=1200, bbox_inches='tight')

if __name__ == "__main__":

    x_log = True
    figure_dir = "results/figures"

    # Hifive Unmtached
    print(f'--- Linux ---')
    print(" stock")
    data_hifive_unmatched_stock = load(f"results/hifive_unmatched/stock/hifive_unmatched_stock_cyclictest.log", start_skip=1000)
    print(" realtime")
    data_hifive_unmatched_rt = load(f"results/hifive_unmatched/realtime/hifive_unmatched_realtime_cyclictest.log", start_skip=1000)

    ax = draw_hist(datas=[data_hifive_unmatched_stock, data_hifive_unmatched_rt], labels= [f"stock",f"preempt-rt"], bins=50, unit='us', x_log=x_log)
    save(ax, f"linux_stock_vs_realtime_normalized", figure_dir)
    ax.clear()

    # Keystone mixted
    print(f'--- keystone Mixted ---')
    print(" stock")
    data_keystone_mixted_stock = load(f"results/keystone_mixted/stock/keystone_mixted_stock_cyclictest.log", start_skip=1000)
    print(" realtime")
    data_keystone_mixted_rt = load(f"results/keystone_mixted/realtime/keystone_mixted_realtime_cyclictest.log", start_skip=1000)

    ax = draw_hist(datas=[data_keystone_mixted_stock, data_keystone_mixted_rt], labels=[f"stock", f"preempt-rt"], bins=50, unit='us', x_log=x_log)
    save(ax, f"keystone_mixted_stock_vs_realtime_normalized", figure_dir)
    ax.clear()

    ax = draw_hist(datas=[data_hifive_unmatched_rt, data_keystone_mixted_rt], labels=[f"w/o keystone", f"w/ keystone"], bins=50, unit='us', x_log=x_log)
    save(ax, f"realtime_linux_vs_keystone_mixted_normalized", figure_dir)
    ax.clear()

    # Enclave startup
    print(f'--- keystone enclave startup ---')
    print(" stock")
    data_keystone_enclave_startup = load(f"results/enclave-startup.log", start_skip=0,skiprows=0)
    ax = draw_hist(datas=[data_keystone_enclave_startup], labels=[f"startup"], bins=50, unit='us', x_log=x_log, bin_edges=np.logspace(np.log10(740000), np.log10(790000), 51))
    save(ax, f"keystone_enclave_startup", figure_dir)
    ax.clear()

    # Keystone hybrid
    print(f'--- keystone Hybrid ---')
    print(" stock 1th")
    data_keystone_hybrid_1_stock = load(f"results/keystone_hybrid/stock/keystone_hybrid_stock_1_cyclictest.log", start_skip=0)
    print(" stock 2th")
    data_keystone_hybrid_2_stock = load(f"results/keystone_hybrid/stock/keystone_hybrid_stock_2_cyclictest.log", start_skip=0)
    print(" realtime 1th")
    data_keystone_hybrid_1_rt = load(f"results/keystone_hybrid/realtime/keystone_hybrid_realtime_1_cyclictest.log", start_skip=0)
    print(" realtime 2th")
    data_keystone_hybrid_2_rt = load(f"results/keystone_hybrid/realtime/keystone_hybrid_realtime_2_cyclictest.log", start_skip=0)

    ax = draw_hist(datas=[data_keystone_hybrid_1_stock, data_keystone_hybrid_1_rt], labels=[f"stock", f"preempt-rt"], bins=50, unit='us', x_log=x_log)
    save(ax, f"keystone_hybrid_stock_vs_realtime_1t_normalized", figure_dir)
    ax.clear()

    ax = draw_hist(datas=[data_keystone_hybrid_2_stock, data_keystone_hybrid_2_rt], labels=[f"stock", f"preempt-rt"], bins=50, unit='us', x_log=x_log)
    save(ax, f"keystone_hybrid_stock_vs_realtime_2t_normalized", figure_dir)
    ax.clear()

    ax = draw_hist(datas=[data_keystone_hybrid_1_rt, data_keystone_hybrid_2_rt], labels=[f"1 thread", f"2 threads"], bins=50, unit='us', x_log=x_log)
    save(ax, f"keystone_hybrid_realtime_1t_vs_2t_normalized", figure_dir)
    ax.clear()

    ax = draw_hist(datas=[data_keystone_hybrid_1_stock, data_keystone_hybrid_2_stock], labels=[f"1 thread", f"2 threads"], bins=50, unit='us', x_log=x_log)
    save(ax, f"keystone_hybrid_stock_1t_vs_2t_normalized", figure_dir)
    ax.clear()

    ax = draw_hist(datas=[data_keystone_mixted_stock, data_keystone_hybrid_1_stock], labels=[f"Linux process", f"Keystone enclave"], bins=50, unit='us', x_log=x_log)
    save(ax, f"keystone_stock_mixted_vs_hybrid_normalized", figure_dir)
    ax.clear()

    ax = draw_hist(datas=[data_keystone_mixted_rt, data_keystone_hybrid_1_rt], labels=[f"Linux process", f"Keystone enclave"], bins=50, unit='us', x_log=x_log)
    save(ax, f"keystone_realtime_mixted_vs_hybrid_normalized", figure_dir)
    ax.clear()

    exit(0)