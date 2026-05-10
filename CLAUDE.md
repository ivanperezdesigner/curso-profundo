# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Project

```bash
python item_packing.py
```

The script is interactive — it prompts for a total length value at runtime.

## Project Overview

Single-file Python optimization tool (`item_packing.py`) that solves a 1D bin-packing problem: given a total length, find the best combination of size-50 and size-30 items that minimizes unused space, then distribute remaining space as equal gaps.

## Core Logic (`item_packing.py`)

- `find_best_packing(length)` — brute-force search over all valid (n50, n30) combinations; minimizes remainder, tie-breaks by preferring more total items
- `format_layout(n50, n30, gap_unit, edge_gap)` — returns a string visualization of the layout
- `main()` — CLI entry point with input validation and a detailed position table output

## Known Issues

- Unicode checkmark character on line 104 causes a `UnicodeEncodeError` on Windows (cp1252 encoding). Replace with ASCII `[OK]` or use `chcp 65001` in the terminal before running.

## Environment

Python 3.14, no external dependencies (standard library only). Virtual environment at `venv/`.
