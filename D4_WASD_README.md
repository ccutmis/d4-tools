# WASD MAPPER 使用說明

## 目錄
1. 下載並安裝 WASD MAPPER
2. 執行 WASD MAPPER
3. 常用快捷鍵
4. 如何修改 設定檔 ( d4_wasd_setting.txt )
5. 參考資源
6. 免責聲明

-----

### 1. 下載並安裝 WASD MAPPER : 
1. 開啟 Google 瀏覽器 在網址列複制貼上 https://www.web3d.url.tw/tmp/d4wasd.zip 開始下載 ( 或直接點[連結](https://www.web3d.url.tw/tmp/d4wasd.zip)下載)
2. 下載完成將壓縮檔內容(dist資料夾)解壓縮到電腦桌面上，dist資料夾的內容為:
    * D4_WASD.exe (WASD 主程式)
    * d4_wasd_setting.txt (設定檔)

![dist資料夾的內容](https://www.web3d.url.tw/images/d4wasd/1-2.png)

-----

### 2. 執行 WASD MAPPER : 
1. 雙擊 D4_WASD.exe 執行主程式，出現如下畫面表示 WASD 程式正常執行。

![dist資料夾的內容](https://www.web3d.url.tw/images/d4wasd/2-1.png)

-----

### 3. 常用快捷鍵 : 
* 上下左右 : 控制 游標往上下左右位移一個單位(UNIT)，並點擊滑鼠左鍵或右鍵。
* 〕 : 增加位移單位。
* 〔 : 減少位移單位。
* ＼ : 位移後點左鍵或右鍵切換，比如預設是 LM ，按一下變成 RM ，再按一下變回 LM。
* ＝ : 切換游標設定 由畫面中心點 或 由游標當前位置 往上下左右位移
* － : 暫停或啟動 WASD 程式
* 上列的快捷鍵都可以透過修改 設定檔 ( d4_wasd_setting.txt ) 調成你喜歡的快捷鍵。

-----

### 4. 如何修改 設定檔 ( d4_wasd_setting.txt ) :
d4_wasd_setting.txt 是一個文字檔，你可以使用記事本或任何純文字編輯軟體(例如: Notepad++ 或 visual studio code)開啟它，並依照自己的需求修改設定內容，請注意在修改時只能修改 '值' 不要修改裡面的格式，不清楚的地方不要做任何修改。

下面是 d4_wasd_setting.py 裡面可以修改 '值' 的部份:

```
# 井字符號之後的所有文字為註解，程式運作時不會執行

# 監控視窗的部份標題
ACTIVE_WIN_TITLE = ""

# 方向鍵的鍵盤映射(MAP)設定
ARROW_KEY_MAP = {
    'up':'up',
    'down':'down',
    'left':'left',
    'right':'right'
}

# 滑鼠左右鍵的鍵盤映射(MAP)設定
SKILL_KEY_MAP = {
    'LM':'v',
    'RM':'b',
    'UNIT_ADD':']',
    'UNIT_SUB':'[',
    'LMRM_SWITCH':'\\',
    'CURSOR_CENTER_SWITCH':'+',
    'APP_ON_OFF':'-'
}

# 移動游標後按左鍵(LM)或右鍵(RM)的設定，留空白則移動游標後不做任何動作
MOVE_AND_CLICK_LR = 'RM'

```

接下簡單示範 '值' 可以怎麼改，例如:

```
# 監控視窗的部份標題
ACTIVE_WIN_TITLE = ""
```

ACTIVE_WIN_TITLE 的值若為空白，程式執行時會無差別的監控輸入並執行對應的動作，如果我們希望它只對特定的程式/視窗監控，比如說只監控暗黑破壞神III 的主程式，那就把 上面的程式片段改成:

```
# 監控視窗的部份標題
ACTIVE_WIN_TITLE = "暗黑破壞神III"
```
修改'值'後記得存檔再重啟 WASD 程式，當游標焦點放在桌面或是瀏覽器時(這個通常稱作設為前景)，按上下左右就不會移動游標，當暗黑破壞神III程式設為前景時，按上下左右游標才會移動。

控制角色上下左右的按鍵預設是 方向鍵的上下左右，要把它設為 wasd 只需要這樣改:

```
ARROW_KEY_MAP = {
    'up':'w',
    'down':'s',
    'left':'a',
    'right':'d'
}
```


-----

### 5. 參考資源
* [keyboard 模組官方文件](https://github.com/boppreh/keyboard/blob/master/README.md)
* [YT影片 WASD 的由來 : 第一位電競選手DENNIS FENG](https://www.youtube.com/watch?v=D7PJ7rliYZk)
* [壹讀: WASD，何時成了遊戲操作的主流？](https://read01.com/a32x86.html#.ZFNaNHZBy3A)
* [壹讀: PC遊戲鍵位研究：傳統WASD是否最合理](https://read01.com/KB5E4J.html#.ZFNfDHZBy3B)

-----

### 6. 免責聲明:
1. 本程式僅提供使用者進行測試學習之用，並不對使用者的行為負責，也不對使用者所儲存的資料內容負責。
2. 使用者使用本程式的風險由使用者自行承擔。對於因使用者違反相關法律法規而引起的任何損失或損害，本服務不承擔任何責任。
3. 本程式及使用說明可能隨時根據市場情況和用戶需求進行變更和調整。使用者應當仔細閱讀相關服務條款和使用規則。使用者同意並遵守所有相關法律法規及服務條款和使用規則。