import json
import os

# Path provided by user state info
path = '/Users/anteqkois/Desktop/Learn/Studies/5_semester/ilościowe_miary_ryzyka_rynkowego/project/ex_2.ipynb'

if not os.path.exists(path):
    # Try relative path if CWD is correct
    if os.path.exists('ex_2.ipynb'):
        path = 'ex_2.ipynb'
    else:
        print(f"Error: File not found at {path} or ./ex_2.ipynb")
        exit(1)

print(f"Modifying file: {path}")

with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# The new source code for the cell
new_source = [
    "fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))\n",
    "\n",
    "# Wykres kursu zamknięcia (Liniowa)\n",
    "ax1.plot(\n",
    "    data_btcusdt_frame_daily.index,\n",
    "    data_btcusdt_frame_daily['close'],\n",
    "    label='Wykres kursu zamknięcia (Liniowa)',\n",
    "    color='green',\n",
    "    linewidth=1.3\n",
    ")\n",
    "\n",
    "ax1.set_title('Bitcoin dzienne notowania (2015-2025) - Liniowa', fontsize=14)\n",
    "ax1.set_xlabel('Data')\n",
    "ax1.set_ylabel('Kurs zamknięcia')\n",
    "ax1.legend()\n",
    "\n",
    "# Wykres kursu zamknięcia (Logarytmiczna)\n",
    "ax2.plot(\n",
    "    data_btcusdt_frame_daily.index,\n",
    "    data_btcusdt_frame_daily['close'],\n",
    "    label='Wykres kursu zamknięcia (Logarytmiczna)',\n",
    "    color='blue',\n",
    "    linewidth=1.3\n",
    ")\n",
    "\n",
    "ax2.set_yscale('log')\n",
    "ax2.set_title('Bitcoin dzienne notowania (2015-2025) - Logarytmiczna', fontsize=14)\n",
    "ax2.set_xlabel('Data')\n",
    "ax2.set_ylabel('Kurs zamknięcia')\n",
    "ax2.legend()\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
]

target_cell_id = "e8a27344"
modified = False

for cell in nb['cells']:
    if cell.get('id') == target_cell_id:
        cell['source'] = new_source
        modified = True
        break

if not modified:
    print("Cell with ID e8a27344 not found. Trying heuristic match.")
    for cell in nb['cells']:
        src_str = "".join(cell.get('source', []))
        if "label='Wykres kursu zamknięcia'" in src_str and "plt.subplots" in src_str:
            cell['source'] = new_source
            modified = True
            break

if modified:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print("Notebook updated successfully.")
else:
    print("Error: Target cell could not be found.")
    exit(1)
