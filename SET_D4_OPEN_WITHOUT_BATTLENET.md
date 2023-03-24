# 直接執行 Diablo IV 無需通過 Battle.Net 的設定

 1. 開啟檔案總管，進到 Diablo IV 的安裝資料夾，找到 Diablo IV.exe 對它按右鍵選 "新增"→"捷徑" 。
 
 ![img](https://i.imgur.com/yZtpjC1.png)
 
 2. 在桌面找到剛才新增的 Diablo IV.exe 的捷徑圖示，對它按右鍵選 "內容" 。
 
 ![img ](https://i.imgur.com/lH780Bw.png)
 
 3. 在目標欄位內容的最後面加上" -launch"，注意在 " 與 - 中間要有一個空格，不然會出錯。 最後按" 套用"再按"確定"即完成設定，從桌面上雙擊 Diablo IV.exe 的捷徑即可直接開啟遊戲。
 
 ![img](https://i.imgur.com/OP8eWU1.png)
 
 步驟 3 的欄位最後面還可以加上連線地區的設定例如:
 ```
 -launch OnlineService.Matchmaking.ServerPool=AU1
 ```
 這個寫法除了原本的功能之外(不用透過Battle.Net登入器直接開啟遊戲，可雙開但不保證電腦效能頂不頂的住)，連線地區會變成是澳洲分流，懂的都懂就不解釋了。
 