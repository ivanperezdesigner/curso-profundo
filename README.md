# Item Packing Optimizer

A command-line tool that finds the optimal combination of size-50 and size-30 items to fill a given length, minimizing unused space.

## Requirements

- Python 3.10+

## Usage

```bash
python item_packing.py
```

When prompted, enter the total length:

```
Enter the total length: 386.08
```

### Example output

```
==================================================
  PACKING RESULT
==================================================
  Total length      : 386.08
  Items size 50     : 1  (50 units)
  Items size 30     : 11  (330 units)
  Total items       : 12
  Items coverage    : 380 / 386.08  (98.42%)
  Remainder         : 6.080000
  Internal gap      : 0.506667  (11 gaps between items)
  Edge gap (×2)     : 0.253333  (start + end = 1 internal gap)
==================================================

Layout  ( [gap] [item] [gap] ... ):

  [0.2533] [50] [0.5067] [30] [0.5067] ... [30] [0.2533]

  #     Size        Start        End     Center
  ----- ------ ---------- ---------- ----------
  1     50          0.2533    50.2533    25.2533
  2     30         50.7600    80.7600    65.7600
  ...
```

## How it works

- **Minimum gap first**: all combinations of size-50 and size-30 items are evaluated; the one with the smallest remainder (unused space) is selected.
- **Tie-break**: if multiple combinations result in zero remainder (perfect fit), the one with the fewest items is preferred.
- **Gap distribution**: the remaining space is split into equal internal gaps between items, with half-gaps at each end.

## Input constraints

- Length must be a positive number.
- Length must be at least 30 (the minimum item size).
