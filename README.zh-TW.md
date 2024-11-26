# 靠程式自動拿 PTCG pocket 得卡挑戰免費獎勵

**中文** | [English](./README.md)

## Demo

<https://youtu.be/_HCzIw4KItQ?si=ukEn5CIr8AiH3eqZ>

## 流程

<https://www.figma.com/board/Jem3eUxo5RHtoZ4rqxfdPO/PTCG-Pocket-Auto?node-id=0-1&t=eW8BAwfemIBwVBzB-1>

## 簡易說明

此專案主要是透過雷電模擬器錄製操作 + Python OCR
來完成自動抽得卡挑戰

以下行為靠鍵盤完成:

- 啟動(切換到模擬器) alt+tab
- 雷電模擬器截圖 ctrl+0
- Game 回首頁並進入得卡 ctrl+G
- Game 得卡往下滑動 ctrl+H
- Game 選卡並抽 ctrl+J
- Game 首頁刷新 ctrl+K

---

各程式的測試功能放在 `Practice`

## 使用



先開啟雷電模擬器，進入 PTCG pocket 首頁
再開啟 CMD 執行:

```sh
# 假設此專案放在 py 資料夾; 使用者叫做 YOUR_USER
cd "C:\Users\YOUR_USER\Desktop\py"
python main.py
```

## 注意

0. 程式是透過 AI 撰寫，筆者只負責想流程，還有很多優化空間

- 缺點:
  - 每天 14.更新會導致程式中斷，要手動進入首頁
  - 版本更新也會導致中斷
  - 每個人電腦環境不同，會有不同程度卡頓，程式中有撰寫很多延遲秒數的部分要自己調整

1. Config 路徑請自行設定為正確路徑

```md
假設使用者是 YUAN
將程式中 YOUR_USER 替換掉
ex:
SCREENSHOTS_INPUT_PATH = r"C:\Users\YUAN\Documents\XuanZhi9\Pictures\Screenshots"
```

2. 請自行安裝 PYTHON 依賴套件

3. 自行匯入操作檔案

錄製操作放在 `LdplayerAction`
不知道在哪邊匯入請看流程文件

4. 雷電模擬器環境

<https://www.ldplayer.tw/>

```md
作業系統: Microsoft Windows 10 64 位元 22H2
OpenGL: 4.6.0 Compatibility Profile Context 24.10.27.01.240827
VT: On
HyperV: Off
以系統管理員身分執行: No
安裝磁碟: 磁碟 C(SSD-NTFS) 可用空間(52GB) 總空間(465GB)
模擬器版本: 9.1.26.0(64)
執行參數: CPU(4 核) 記憶體(4096M) 解析度(900x1600 DPI 320) FPS(60)
多開參數: 當前編號(0) 正在執行(1) 高速模式(1) FPS 限制(60) 極致多開(0)
硬碟訊息: 類型(自動擴充) 可用空間(22GB) 總空間(25GB)
機型: 品牌(samsung) 型號(SM-X710N)
Root 權限: Off
模擬器路徑: C:\LDPlayer\LDPlayer9\
日誌路徑: C:\Users\User\AppData\Roaming\XuanZhi9\log
```

5. 程式環境

```md
Python 3.11.3

"C:\Program Files\Tesseract-OCR\tesseract.exe" --version
tesseract v5.5.0.20241111
leptonica-1.85.0
libgif 5.2.2 : libjpeg 8d (libjpeg-turbo 3.0.4) : libpng 1.6.44 : libtiff 4.7.0 : zlib 1.3.1 : libwebp 1.4.0 : libopenjp2 2.5.2
Found AVX2
Found AVX
Found FMA
Found SSE4.1
Found libarchive 3.7.7 zlib/1.3.1 liblzma/5.6.3 bz2lib/1.0.8 liblz4/1.10.0 libzstd/1.5.6
Found libcurl/8.11.0 Schannel zlib/1.3.1 brotli/1.1.0 zstd/1.5.6 libidn2/2.3.7 libpsl/0.21.5 libssh2/1.11.0
```
