環境
python3.12

建立虛擬環境
```
python3 -m venv tutorial-env
```
啟動虛擬環境
source tutorial-env/bin/activate

離開
deactivate

pip install "fastapi[standard]"

https://fastapi.tiangolo.com/#installation


``` python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello World"

```

fastapi dev main.py

```
project/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_main.py
│
├── pytest.ini
└── requirements.txt

```

uvicorn app.main:app --reload