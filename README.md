# PAQ: Python bingding for paq9a

## Install

```bash
pip install paq
```

## Usage

```python
import paq
assert b'1234' == paq.decompress(paq.compress(b'1234'))
```