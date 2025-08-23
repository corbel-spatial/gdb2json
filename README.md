# gdb2json

A proof-of-concept script that extracts information from a geodatabase simply by looking at its XML.

```python
import gdb2json
js = gdb2json.parse(gdb_path)
print(js)
```

