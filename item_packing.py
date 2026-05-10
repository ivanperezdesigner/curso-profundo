#!/usr/bin/env python3
"""
Item packing optimizer.

Given a total length, finds the best combination of size-50 and size-30 items
that minimizes unused space. The remaining space is then distributed as equal
gaps: one before the first item, one between each pair, and one after the last.
"""


def find_best_packing(length: float) -> tuple[int, int, float]:
    """
    Return (n50, n30, remainder) minimizing remainder.
    Tie-break: prefer the combination with more total items.
    """
    best_n50, best_n30 = 0, 0
    min_remainder = length

    for n50 in range(int(length // 50) + 1):
        space_after_50s = length - n50 * 50
        n30 = int(space_after_50s // 30)
        remainder = space_after_50s - n30 * 30

        is_better = remainder < min_remainder
        is_equal_but_fewer_items = (
            remainder == 0
            and min_remainder == 0
            and (n50 + n30) < (best_n50 + best_n30)
        )

        if is_better or is_equal_but_fewer_items:
            min_remainder = remainder
            best_n50, best_n30 = n50, n30

    return best_n50, best_n30, min_remainder


def format_layout(n50: int, n30: int, gap_unit: float, edge_gap: float) -> str:
    items = ["50"] * n50 + ["30"] * n30
    eg = f"[{edge_gap:.4f}]"
    ig = f"[{gap_unit:.4f}]"
    parts = [eg]
    for i, size in enumerate(items):
        parts.append(f"[{size}]")
        parts.append(eg if i == len(items) - 1 else ig)
    return " ".join(parts)


def main() -> None:
    try:
        length = float(input("Enter the total length: "))
    except ValueError:
        print("Error: please enter a valid number.")
        return

    if length <= 0:
        print("Error: length must be a positive number.")
        return

    if length < 30:
        print(f"Length {length:.4f} is smaller than the minimum item size (30).")
        print("No items can be placed.")
        return

    n50, n30, remainder = find_best_packing(length)
    total_items = n50 + n30
    gap_unit = remainder / total_items if total_items > 0 else 0
    edge_gap = gap_unit / 2

    items_length = n50 * 50 + n30 * 30

    print()
    print("=" * 50)
    print("  PACKING RESULT")
    print("=" * 50)
    print(f"  Total length      : {length}")
    print(f"  Items size 50     : {n50}  ({n50 * 50} units)")
    print(f"  Items size 30     : {n30}  ({n30 * 30} units)")
    print(f"  Total items       : {total_items}")
    print(f"  Items coverage    : {items_length} / {length}  ({items_length/length*100:.2f}%)")
    print(f"  Remainder         : {remainder:.6f}")
    print(f"  Internal gap      : {gap_unit:.6f}  ({total_items - 1} gaps between items)")
    print(f"  Edge gap (×2)     : {edge_gap:.6f}  (start + end = 1 internal gap)")
    print("=" * 50)
    print()
    print("Layout  ( [gap] [item] [gap] ... ):")
    print()
    print("  " + format_layout(n50, n30, gap_unit, edge_gap))
    print()

    # Position table
    items = [50] * n50 + [30] * n30
    print(f"  {'#':<5} {'Size':<6} {'Start':>10} {'End':>10} {'Center':>10}")
    print(f"  {'-'*5} {'-'*6} {'-'*10} {'-'*10} {'-'*10}")
    cursor = edge_gap
    for i, size in enumerate(items):
        start = cursor
        end = cursor + size
        center = (start + end) / 2
        print(f"  {i+1:<5} {size:<6} {start:>10.4f} {end:>10.4f} {center:>10.4f}")
        cursor = end + (gap_unit if i < len(items) - 1 else 0)
    print()

    reconstructed = items_length + gap_unit * (total_items - 1) + edge_gap * 2
    print(f"  Verification: {items_length} + {gap_unit:.6f}×{total_items - 1} + {edge_gap:.6f}×2 = {reconstructed:.6f}  ✓")
    print()


if __name__ == "__main__":
    main()
