# D4_WASD 使用說明

![D4_WASD](https://www.web3d.url.tw/images/d4wasd/D4_WASD_LOGO.png)

## 目錄 : 
1. 下載並安裝 D4_WASD
2. 執行 D4_WASD
3. 常用快捷鍵
4. 如何修改 設定檔 ( d4_wasd_setting.txt )
5. 建立新的 設定檔 適配不同的遊戲做使用
6. 參考資源
7. 免責聲明

-----

### 1. 下載並安裝 D4_WASD : 
1. 開啟 Google 瀏覽器 在網址列複制貼上 https://www.web3d.url.tw/tmp/d4wasd.zip 開始下載 ( 或直接點[連結](https://www.web3d.url.tw/tmp/d4wasd.zip)下載)
2. 檔案下載時可能遇到的瀏覽器封鎖解決方法:
    * Google Chrome: [圖片說明](https://www.web3d.url.tw/images/d4wasd/download_d4wasd_from_chrome.png)
    * Microsoft Edge: [圖片說明](https://www.web3d.url.tw/images/d4wasd/download_d4wasd_from_edge.png)
3. 下載完成將壓縮檔內容(dist資料夾)解壓縮到電腦桌面上，dist資料夾的內容為:
    * D4_WASD.exe (WASD 主程式)
    * d4_wasd_setting.txt (預設設定檔)
    * D3_wasd_setting.txt (D3用範例設定檔)
    * HOTS_wasd_setting.txt (HOTS用範例設定檔)
    * ![dist資料夾的內容](https://www.web3d.url.tw/images/d4wasd/1-2b.png)
4. D4_WASD.exe 的 MD5 驗證碼:
    * D4_WASD.exe (VERSION: 0.1B) MD5 驗證碼 : AEA2E56170A9D3599A21A39BB87D16CA
    * D4_WASD.exe (VERSION: 0.1A) MD5 驗證碼 : 41C2FC73FC8C3A74EAAB1CFA37193746
    * 與 MD5驗證相關的資訊請至下方:"6. 參考資源" 查閱。
    * 主程式版本有更新時 MD5 驗證碼會隨之變更，以本頁公告為準。

-----

### 2. 執行 D4_WASD : 
1. 雙擊 D4_WASD.exe 執行主程式，出現如下畫面表示 WASD 程式正常執行。

![執行 D4_WASD](https://www.web3d.url.tw/images/d4wasd/2-1i.png)

-----

### 3. 常用快捷鍵 : 

![常用快捷鍵](https://www.web3d.url.tw/images/d4wasd/3-1a.png)

* 參考上圖淺綠色的按鍵。
* 上下左右 : 控制 游標往上下左右位移一個單位(UNIT)，並點擊滑鼠左鍵或右鍵。
* &gt; : 增加位移單位。
* &lt; : 減少位移單位。
* / : 位移後點"左鍵或右鍵或無動作"的切換，比如預設是 LM ，按一下變成 RM ，再按一下變成 FORCE_MOVE(需設好對應到遊戲內的強制移動按鍵)，再按一下變成 無動作。
* ＝ : ㊉鎖定中心 切換游標設定 由畫面中心點 或 由游標當前位置 往上下左右位移
* － : 暫停或啟動
* 上列的快捷鍵都可以透過修改 設定檔 ( d4_wasd_setting.txt ) 調成你慣用的快捷鍵。
* "游標移動後:尚未指派" 搭配  "㊉鎖定中心:False" 就可以用方向鍵控制游標移動而不是控制角色移動。
* 若要強制結束程式可按住組合鍵: Ctrl + Alt + x (eXit)
* 程式最小化的組合鍵: Ctrl + Alt + b (Back)
* 程式置頂的組合鍵: Ctrl + Alt + t (Top)
* 在你要監控的遊戲要先設好強制移動按鍵，例如設為 9 (優先選擇不會跟現有按鍵衝突的) 如果強制移動不是設為 9 ，要記得修改 SKILL_KEY_MAP 字典裡面 FORCE_MOVE 的值。

-----

### 4. 如何修改 設定檔 ( d4_wasd_setting.txt ) :
d4_wasd_setting.txt 是一個文字檔，你可以使用記事本或任何純文字編輯軟體(例如: Notepad++ 或 visual studio code)開啟它，並依照自己的需求修改設定內容，請注意在修改時只能修改 '值' 不要修改裡面的格式，不清楚的地方不要做任何修改。修改完成後記得要存檔再重開 D4_WASD.exe 新的設定才會有作用。

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

# 滑鼠左右鍵及快捷鍵的鍵盤映射(MAP)設定
SKILL_KEY_MAP = {
    'LM':'v',
    'RM':'b',
    'FORCE_MOVE':'9',
    'UNIT_ADD':'.',
    'UNIT_SUB':',',
    'AAM_SWITCH':'/',
    'CURSOR_CENTER_SWITCH':'+',
    'APP_ON_OFF':'-'
}

# 移動游標後按左鍵(LM)或右鍵(RM)的設定，留空白則移動游標後不做任何動作
ACTION_AFTER_MOVE = ''

```

接下簡單示範 '值' 可以怎麼改，例如:

```
# 監控視窗的部份標題
ACTIVE_WIN_TITLE = ""
```

ACTIVE_WIN_TITLE 的值若為空白，程式執行時會監控目前游標所在位置視窗的輸入並執行對應的動作，如果我們希望它只對特定的程式/視窗監控，比如說只監控暗黑破壞神III 的主程式，那就把 上面的程式片段改成:

```
# 監控視窗的部份標題
ACTIVE_WIN_TITLE = "暗黑破壞神III"
```
修改'值'後記得存檔再重啟 WASD 程式，當游標焦點放在桌面或是瀏覽器時(這個通常稱作設為前景)，按上下左右就不會移動游標，當暗黑破壞神III程式設為前景時，按上下左右游標才會移動。這邊舉的 "暗黑破壞神III" 字串範例要以實際程式運行時的顯示的標題做設定，比如說有的電腦執行記事本，顯示的是"記事本-未命名1"，有的則是顯示"Notepad-Untitled"，如果是要監控記事本，那字串就要設為"記事本"或"Notepad"(視你的電腦上面顯示的標題為何)，只需要輸入部份的標題即可，不需要完整標題。

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

### 5. 建立新的 設定檔 適配不同的遊戲做使用 : 
用滑鼠雙擊 D4_WASD.exe 執行 'D4_WASD' 時，會讀取設定檔 'd4_wasd_setting.txt' 作為程式各項參數來源，這是程式預設的運作機制。 

在現實生活中，比較常見的時會輪流玩不同的遊戲，因些 D4_WASD 支援了 "將新的設定檔拖放到 D4_WASD.exe 即可動態指定程式參數來源"。

以下用 "暗黑破壞神III" 及 "暴雪英霸" 作個示範 :

1. 開啟檔案總管，目錄切到 D4_WASD 程式所在的位置， 點選 'd4_wasd_setting.txt' ，複制貼上 2 次，並將新增的 2 個檔案命名為 'D3_wasd_setting.txt' 及 'HOTS_wasd_setting.txt'。
2. 以純文字編輯程式開啟 'D3_wasd_setting.txt'，並修改下列內容(請注意不要改到其它地方) :
    ```
    ACTIVE_WIN_TITLE = "暗黑破壞神III"
    
    ...略...

    # 移動游標後按左鍵(LM)或右鍵(RM)的設定，留空白則移動游標後不做任何動作
    ACTION_AFTER_MOVE = 'FORCE_MOVE'
    ```
    
    * 修改完成記得存檔，從上面的設定可以得知， D4_WASD 執行時，如果游標焦點視窗標題包含 "暗黑破壞神III" 程式才會運作，玩家按'5'的時候，程式會模擬滑鼠左鍵點擊，按'space'(空白鍵)時，程式會模擬滑鼠右鍵點擊，而強制移動對應的按鍵是'9'，因此在 暗黑破壞神III 遊戲中，我們需要進到按鍵設定頁面，把強制移動設為 '9'。
    * 預設的 ACTION_AFTER_MOVE 值是 "" (無動作)，可以通過按 "\"進行 "左鍵,右鍵,強制移動,無動作" 切換，這個設定檔的作用是給 暗黑破壞神III 使用，因此把它的值改為 "FORCE_MOVE"，程式在執行時預設就是強制移動了。(在 暗黑破壞神III 遊戲中，我們需要進到按鍵設定頁面，把強制移動設為 '9')
    * 左鍵設為 'v' 是因為它用左手姆指按很容易，這個按鍵在遊戲的作用主要是用來拾取地上物品或是開祭壇之類的動作，例如有寶物掉在地上，就用左手姆指按住 'v'，再用右手控制方向鍵移動角色，游標經過的地方如果有物品就會拾取，沒有要拾取就放開 'v' 讓角色移動是以強制移動的方式進行。
3. 以純文字編輯程式開啟 'HOTS_wasd_setting.txt'，並修改下列內容(請注意不要改到其它地方) :
    ```
    ACTIVE_WIN_TITLE = "暴雪英霸"
    
    ...略...

    # 移動游標後按左鍵(LM)或右鍵(RM)的設定，留空白則移動游標後不做任何動作
    ACTION_AFTER_MOVE = 'FORCE_MOVE'
    ```

    * 修改完成記得存檔，從上面的設定可以得知， D4_WASD 執行時，如果游標焦點視窗標題包含 "暴雪英霸" 程式才會運作，玩家按 '5' 時程式會模擬滑鼠左鍵點擊，按 '6' 時程式會模擬滑鼠右鍵點擊，而強制移動對應的按鍵是 '9' ，因此在 暴雪英霸 遊戲中，我們需要進到熱鍵設定頁面，把強制移動設為 '9'。另外我習慣把遊戲中的普攻 'A' 加設 'F'，只是個人喜好，平時左手食指放在 'F' 其它指頭放在 'EWQ' ，另外快速施放設為開啟，進遊戲後按一下L(角色設為鏡頭中心)，大概這樣就可以了。
    * 使用 D4_WASD 玩暴雪英霸時 最好是能熟悉一些其它快捷鍵的使用，例如要點第二個天賦就是按 Ctrl+2，要開天賦選擇小視窗按 N，按 ESC 關掉小視窗等等。當然有些情況下還是要滑鼠操作了，這裡只是示範用它來玩英霸在戰場中的使用。
    
-----

### 6. 參考資源 : 
* [keyboard 模組官方文件](https://github.com/boppreh/keyboard/blob/master/README.md)
* [YT影片 WASD 的由來 : 第一位電競選手DENNIS FENG](https://www.youtube.com/watch?v=D7PJ7rliYZk)
* [MD5 驗證機制為何](https://www.dgbas.gov.tw/public/data/dgbas03/bs5/expuse/106MD5%E6%AA%A2%E6%9F%A5%E6%AD%A5%E9%A9%9F.pdf)
* [MD5 驗證軟體下載](http://getmd5checker.com/download.html)

-----

### 7. 免責聲明 :
1. 本程式僅提供使用者進行測試學習之用，並不對使用者的行為負責，也不對使用者所儲存的資料內容負責。
2. 使用者使用本程式的風險由使用者自行承擔。對於因使用者違反相關法律法規而引起的任何損失或損害，本服務不承擔任何責任。
3. 本程式及使用說明可能隨時根據市場情況和用戶需求進行變更和調整。使用者應當仔細閱讀相關服務條款和使用規則。使用者同意並遵守所有相關法律法規及服務條款和使用規則。