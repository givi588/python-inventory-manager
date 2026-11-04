# Python Inventory Manager

A Python inventory analysis tool that reads CSV files, calculates stock value, detects low-stock products, and includes automated unit tests.

## Features

- Read inventory data from a CSV file
- Calculate total inventory value in USD
- Detect low-stock products
- Count the number of low-stock products
- Configure the low-stock threshold in code
- Calculate the total number of stock units
- Validate basic CSV input data
- Run automated tests with unittest

## Technologies

- Python 3
- csv
- pathlib
- unittest

No external dependencies are required.

## Project Structure

- `inventory.py` - Main inventory application
- `inventory.csv` - Sample inventory data
- `test_inventory.py` - Automated unit tests

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the inventory report:

    py inventory.py

## Example Output

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

## Automated Testing

Run:

    py -m unittest -v

The project includes eight unit tests covering inventory calculations, stock thresholds, total unit counts, and low-stock product counts.

Expected summary:

    Ran 8 tests
    OK

## Future Improvements

- Export reports to CSV
- Support decimal prices
- Add more input validation tests
- Provide interactive inventory management
- Build a web dashboard

## Project Status

Educational prototype. Not yet intended for production inventory management.

## Author

GitHub: [givi588](https://github.com/givi588)
