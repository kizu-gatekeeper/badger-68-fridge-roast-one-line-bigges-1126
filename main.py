"""Entry for make.fun's Fridge Roast: one line roasting a very smart fridge."""

import os

ENTRY = "My smart fridge has a camera, an app and strong opinions about my milk, yet still needs a human to notice the leftovers have formed a government."
MAX_CHARS = 200


def main() -> None:
    # Validate the format: exactly one line, within the gate limit.
    assert "\n" not in ENTRY and "\r" not in ENTRY
    assert 1 <= len(ENTRY) <= MAX_CHARS, len(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
