# Fast Api 學習機會

## 專案環境
python 3.12

## 章節
1. 下載學習資料
2. 建立虛擬環境，啟動開發環境
3. 安裝 fastapi 套件
4. 第一支 API Hello World

## 第 1 節 下載學習資料
1.1 有兩種下載方式

1.1.1 可使用指令下載

開啟指令模式，window cmd 或 mac terminal，貼上（指令1.1.1）。

指令 1.1.1：git 遠端 git 倉儲指令
```
git clone https://github.com/qnsak/fastapi_tutorial.git
```

1.1.2 使用瀏覽器下載。

開啟預覽器貼上 "https://github.com/qnsak/fastapi_tutorial"，點擊按鈕【code】，再點擊按鈕【Download ZIP】進行下載。

1.2 下載完成之後，會出現 fastapi_tutorial 專案目錄。

目錄結構 1.2.1
```
fastapi_tutorial
├── README.md
├── app
│   ├── __init__.py
│   └── main.py
├── pytest.ini
├── requirements.txt
└── tests
    ├── __init__.py
    ├── test_greet.py
    └── test_main.py
```

## 第 2 節 建立虛擬環境，啟動開發環境。
使用 python 內建的虛擬環境 venv

2.1 啟動虛擬環境
在指令模式進入 fastapi_tutorial 目錄。

2.1.1 指令：進入指令 cd
```
cd fastapi_tutorial
```

在目錄內，下達初始化虛擬環境指令 python3 -m venv 【環境名稱】。

2.1.2 指令：初始化虛擬環境
```
python3 -m venv tutorial-env
```

啟動虛擬環境。

2.1.3 指令：開啟虛擬環境
```
source tutorial-env/bin/activate
```

離開虛擬環境。

2.1.4 指令：離開虛擬環境
```
deactivate
```

第 3 節 安裝 fastapi 套件
3.1 使用 requirements.txt 安裝專案相關套件。

3.1.1 指令：安裝相關套件
```
pip install -r requirements.txt
```

第 4 節 第一支 API Hello World
4.1 編寫 Hello World API 
開啟 app 目錄內的 main.py，輸入【4.1.1 程式】並儲存。

4.1.1 程式：Hello World API 的 python 程式
``` python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello World"

```

4.2 啟動 FastApi 伺服器。
4.2.1 指令：啟動 FastApi 伺服器
```
uvicorn app.main:app --reload 
```


