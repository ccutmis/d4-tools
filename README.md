# Diablo IV LocalPrefs.txt 修改程式

 ## 目錄
 
 
 -----
 
 ### Diablo IV LocalPrefs.txt 修改程式(.EXE 可執行檔) 下載點
 [http://www.web3d.url.tw/diablo4/D4_Pref_Switcher.zip](http://www.web3d.url.tw/diablo4/D4_Pref_Switcher.zip)
 
 下載完成將它解壓縮到 桌面 或 任何資料夾都可以，請注意 'need_fix_setting.txt' 要跟 程式放在一起，程式執行時的相關設定就是從這個檔案讀取的。
 
 -----
 
 ### Diablo IV LocalPrefs.txt 修改程式 使用說明
 1. 下載完成將它解壓縮到 桌面 或 任何資料夾都可以，若先前仍未執行過 Diablo IV 就執行 D4_Pref_Switcher.exe 會看到如下訊息:
 
 ![img](https://i.imgur.com/O7HQof0.png)
 
 2. 我們先執行 Diablo IV ，進到登入畫面就可以按左下角 [ 離開  ]  (這裡的用意是讓 Diablo IV 自動生成新的 LocalPrefs.txt )
 
 ![img ](https://i.imgur.com/0rQkYVo.png)
 
 3. 確定 Diablo IV 關閉後，重新執行 D4_Pref_Switcher.exe ，然後按 1 再按 Enter 會看到如下訊息:
 
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
