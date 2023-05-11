# Diablo IV LocalPrefs.txt 修改程式

## 目錄
 
-----
 
### Diablo IV LocalPrefs.txt 修改程式(.EXE 可執行檔) 下載點
[https://www.web3d.url.tw/tmp/D4_Pref_Switcher.zip](https://www.web3d.url.tw/tmp/D4_Pref_Switcher.zip)
 
下載完成將它解壓縮到 桌面 或 任何資料夾都可以，請注意 'need_fix_setting.txt' 與 'MY_DOCUMENT_LOCATION.txt' 要跟 主程式 'D4_Pref_Switcher.exe' 放在一起，程式執行時的相關設定就是從這個檔案讀取的。
 
-----
 
### Diablo IV LocalPrefs.txt 修改程式 使用說明

1. 先執行一次 Diablo IV ，進到登入畫面就可以按左下角 [ 離開  ]  (這裡的用意是讓 Diablo IV 自動生成新的 LocalPrefs.txt )

2. 開啟檔案總管，進到我的文件 裡面的 Diablo IV 資料夾，然後點 資料夾路徑欄位，並對它按右鍵選"複制"，然後用記事本開啟 "MY_DOCUMENT_LOCATION.txt"，將剛才複制的路徑覆蓋掉原有內容並存檔，然後關閉記事本。(如下圖所示)

![img](https://www.web3d.url.tw/images/d4_pref_switcher/02.png)
 
 
 
 3. 執行 D4_Pref_Switcher.exe ，然後按 1 再按 Enter 會看到如下訊息:
 
 ![img](https://i.imgur.com/7YFHMDK.png)
 
這時設定檔已經修改成"視窗模式、最低特效、最低畫質"

4. 我們重行執行 Diablo IV，會看到目前已經是視窗化的狀態，表示設定有正確套用。

![img](https://i.imgur.com/3CbeyU4.png)

以經驗法則來說，玩暴雪遊戲設定視窗模式，解析度在1024x768或往上一階，特效全關，畫質調到最低，通常可以用較低的硬體來遊玩。

5. 如果要恢復預設，先確定  Diablo IV 關閉，重新執行 D4_Pref_Switcher.exe ，然後按 2 再按 Enter 會看到如下訊息:

![img](https://i.imgur.com/ZgUqvJI.png)
 
 這個動作用意是把修改過的 LocalPrefs.txt 刪除，然後在重新執行 Diablo IV 時就會自動生成新的(預設)  LocalPrefs.txt
 
 ### 免責聲明
* 本程式僅為學習測試使用，若有任何未遇期狀況發生，本人概不負責。
* 主程式 EXE 是在 windows 11 沙箱編譯，在三部不同電腦測試過，沒有安全問題，如果對程式安全有疑慮的話，也可以在自己的電腦安裝 git 及 python3.7+ 的版本，然後用
`git clone https://github.com/ccutmis/diablo4.git` 把這個 儲存庫拉到本地端，用 Python 執行 D4_Pref_Switcher.py ，它就是 D4_Pref_Switcher.exe 的原始檔。
