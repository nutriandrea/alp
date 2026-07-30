---
type: alp-practice
id: setup-environment
title: Set Up Your Environment
concepts-covered: [encoding]
---
## Steps

1. Install dependencies:
   ```bash
   pip install sentence-transformers numpy faiss-cpu
   ```

2. Verify installation:
   ```bash
   python -c "
   from sentence_transformers import SentenceTransformer
   import numpy as np
   m = SentenceTransformer('all-MiniLM-L6-v2')
   v = m.encode('hello world')
   print(f'OK — embedding dim: {len(v)}')
   "
   ```

## Expected Output
```
OK — embedding dim: 384
```
