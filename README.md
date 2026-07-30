# Swedish Tax Table Lookup Program 🇸🇪

A Python program that looks up local tax rates for Swedish municipalities and lets you run income/vacation-pay calculations against them, with simple charting of results.

The program reads from a CSV file of municipal tax data and separates data handling, business logic, and the menu-driven CLI into distinct modules for clarity.

---

## Project Structure

- `mitt_program_main.py` – Program entry point
- `mitt_program_funktioner.py` – Core logic and helper functions
- `skattetabell.csv` – Tax table data for Swedish municipalities
- `README.md` – Project documentation

---

## How it Works

- Loads tax data from `skattetabell.csv`
- Lets you look up a municipality and its tax rate
- Runs calculations (e.g. income after tax, vacation days) based on the selected rate
- Plots results with matplotlib

---

## Technologies Used

- **Python 3**
- **matplotlib** / **numpy**
- CSV data handling
- Modular program design

---

## How to Run

1. Make sure you have Python 3 installed
2. Install dependencies:

```bash
pip install matplotlib numpy
```

3. Run the program:

```bash
python mitt_program_main.py
```

---

## Purpose

This project demonstrates:
- Data processing with CSV files
- Clean, modular program structure in Python
- Practical problem-solving using real-world public data (Swedish municipal tax rates)
