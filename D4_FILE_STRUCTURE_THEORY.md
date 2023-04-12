# D4 檔案架構現況之推論 : 

![img]( https://i.imgur.com/JI7KIMf.png )

為何說這是推論，因為我不是暴雪遊戲開發團隊的啊。

裡面提到的一些論述基本上不會超出高中計算機概論的範圍。

有幾位巴哈網友提到我貼的那張圖( https://i.imgur.com/JI7KIMf.png ) 裡面的內容是壓縮檔或資料加殼跟架構無關。

程式加殼不是什麼黑科技，我們公司經銷的商用軟體就有用到，不知道什麼是程式加殼的網友去 Google 或問 ChatGPT 就有解答，不想回覆是因為這種不是簡單幾句就能講完的。

-----

為什麼我說這個就是暴雪遊戲的檔案架構，你可以去下載暴雪英霸(它是免費的，架構類似且不像D4目前不能測的)，然後試玩幾把看看，玩過之後你把程式關閉去看一下裡面的那些壓縮檔有沒有解壓到硬碟裡面，就我測試(超過五年)並觀察的結果，它就是執行後會把整個網友所謂的加殼過的資料讀到記憶體裡面，脫殼跟後續的程式如何存取資源都在記憶體裡面處理，一個不小心是可能造成記憶體洩漏的問題，這在英霸跟D3都有玩家反應過，例如下列官網論壇討論 :

HOTS 的 討論 : 
* [https://us.forums.blizzard.com/en/heroes/t/hots-insane-ram-usage-up-to-10gb/38036/10](https://us.forums.blizzard.com/en/heroes/t/hots-insane-ram-usage-up-to-10gb/38036/10)

D3 的 討論 : 
* [https://us.forums.blizzard.com/en/d3/t/increased-memory-usage/39946](https://us.forums.blizzard.com/en/d3/t/increased-memory-usage/39946)
* [https://eu.forums.blizzard.com/en/d3/t/diablo-3-ram-memory-spikes/2895](https://eu.forums.blizzard.com/en/d3/t/diablo-3-ram-memory-spikes/2895)

D3 跟 HOTS 都是地圖固定場景規模不算大的遊戲，D4 要做開放世界自然會遇到更大的挑戰。例如在 D3 或 HOTS 過圖就是換房間重新載入需要的資源，但在 D4 的開放世界裡角色在逛來逛去的同時，它必須同時不斷預載玩家接下來可能需要的資源包，原本有問題的部份就會放大，變成大問題。 (相關議題可以閱讀最下方參考資料)

想想你在公測時角色走在大地圖上，逛到某些地方會有累似空氣牆，擋住不能過，等一會兒又能過了，推斷這有可能就是程式判斷某些資源還沒處理好，不想讓玩家直接跑過去看到低畫質甚至是空白的場景所做的限制機制。

公測不給座騎也可能出於同樣因素，不然你想想座騎明明是10-12級就能取得的(據封測玩家回報)，座騎也是 D4 才有的特色，公開測試不給試，硬要玩家用腳逛大陸，這個在我來看就很不合理。

可能有人會說"拉南的贈禮"任務是第二章才有，對的，但是那個任務是第二章開始就可以解的，公測大地圖左上角跑不過去那邊就是，如果官方要給玩家體驗座騎那解到拉南那邊鎖住後面的部份會很難嗎? 甚至直接就開啟座騎讓玩家從開始就能體驗不就行了，劇情裡他一開始是有騎馬的耶( 睡個覺起來馬死了 )，怎麼會到後面有錢有裝連世界王都能殺了，在馬廄買不起一匹馬? 

-----

參考資料 : 
* [https://www.techbang.com/posts/51627-player-perspectives-why-the-read-speed-so-slow](https://www.techbang.com/posts/51627-player-perspectives-why-the-read-speed-so-slow)
* [https://www.techbang.com/posts/51627-player-perspectives-why-the-read-speed-so-slow?page=2](https://www.techbang.com/posts/51627-player-perspectives-why-the-read-speed-so-slow?page=2)


