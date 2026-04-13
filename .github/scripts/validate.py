#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / 'tiwen-skill'
DIST = ROOT / 'dist'
FORGE = ROOT / '.github' / 'scripts' / '_vendor'


def run(cmd, cwd=ROOT):
    print('+', ' '.join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def main():
    quick_validate = ROOT / '.github' / 'scripts' / '_vendor' / 'quick_validate.py'
    package_skill = ROOT / '.github' / 'scripts' / '_vendor' / 'package_skill.py'
    if not quick_validate.exists() or not package_skill.exists():
        print('Missing vendored validation scripts.', file=sys.stderr)
        return 1
    DIST.mkdir(exist_ok=True)
    run(['python3', str(quick_validate), str(SKILL)])
    run(['python3', str(package_skill), str(SKILL), str(DIST)])
    pkg = DIST / 'tiwen-skill.skill'
    if not pkg.exists():
        print('Expected packaged skill not found.', file=sys.stderr)
        return 1
    print('Validation complete:', pkg)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
