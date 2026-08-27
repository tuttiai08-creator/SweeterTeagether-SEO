#!/usr/bin/env python3
"""CLI: WordPress draft handoff. Default is dry-run (no network)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import wordpress_handoff as handoff

if __name__ == "__main__":
    sys.exit(handoff.main())
