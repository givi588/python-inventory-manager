# Python Inventory Manager

A small Python tool for reviewing inventory levels, calculating stock value, and exporting a CSV report that can be opened in spreadsheet software.

## Features

- Read product names, prices, and quantities from `inventory.csv`
- Calculate inventory value and total units in stock
- Identify products at or below a configurable low-stock threshold (default: 5)
- Print a summary in the terminal
- Export product quantities, stock values, and statuses to `inventory_report.csv`
- Reject missing CSV columns, empty names, and negative prices or quantities
- Run unit tests for calculations and CSV export

## Requirements

Python 3. No third-party packages required.

## Run

Download or clone the repository, then open a terminal in the project folder.

On Windows:

```powershell
py inventory.py
```

On macOS or Linux:

```bash
python3 inventory.py
```

The script reads `inventory.csv` and creates or overwrites `inventory_report.csv` in the same folder. The source CSV is not modified.

## Input format

```csv
name,price,quantity
Keyboard,30,12
Mouse,25,3
Monitor,150,7
Headphones,60,2
USB Cable,10,4
```

Prices and quantities are currently handled as integers.

## Example terminal output

```text
=== INVENTORY REPORT ===
Keyboard | Qty: 12 | Value: $360 | OK
Mouse | Qty: 3 | Value: $75 | LOW STOCK
Monitor | Qty: 7 | Value: $1050 | OK
Headphones | Qty: 2 | Value: $120 | LOW STOCK
USB Cable | Qty: 4 | Value: $40 | LOW STOCK
------------------------
Total Inventory Value: $1645
Total Units: 28
Low Stock Products: 3
CSV report exported successfully.
```

## Exported CSV

`inventory_report.csv` contains these columns:

```csv
name,quantity,stock_value,status
Keyboard,12,360,OK
Mouse,3,75,LOW STOCK
Monitor,7,1050,OK
Headphones,2,120,LOW STOCK
USB Cable,4,40,LOW STOCK
```

## Tests

Run:

```powershell
py -m unittest -v
```

There are nine unit tests covering inventory calculations, low-stock thresholds, unit counts, and CSV export. The export test uses a temporary directory and checks the output file's content.

## Files

- `inventory.py` — inventory calculations, reporting, and CSV export
- `inventory.csv` — sample input data
- `test_inventory.py` — automated unit tests
- `inventory_report.csv` — generated output (created when the script runs)

## Limitations

This is a learning project, not a production inventory system. It expects integer prices and quantities, uses a fixed CSV structure, and does not support editing stock or tracking transactions. Running the script again overwrites the previously exported report.
