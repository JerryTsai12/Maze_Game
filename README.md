# Maze_Game 迷宮遊戲
## 作者：新竹高中  [許宸瑋(aawilliamaa)](https://github.com/aawilliamaa)、[蔡朝暐(JerryTsai12)](https://github.com/JerryTsai12)
## 此專案為 **「 選修課程–進階程式設計 」** 的 **「 課程學習成果 」**
### 在此專案中，有四個 .py 檔案，一個 .json 檔案，其中

* [`Maze_game_main.py`](https://github.com/JerryTsai12/Maze_Game/blob/main/Maze_Game_main.py)  為 **「主程式碼」**，下載後執行此程式碼以進入遊戲
* [`Maze_Creat.py`](https://github.com/JerryTsai12/Maze_Game/blob/main/Maze_Creat.py) 為 **「迷宮生成演算法」** 的程式碼
* [`Maze_Auto.py`](https://github.com/JerryTsai12/Maze_Game/blob/main/Maze_Auto.py) 為三種 **「迷宮尋路演算法」** 的程式碼，分別為  
    * 標準答案（程式內函式名稱為 **standard_answer** ）
    * 深度優先搜尋法（程式內函式名稱為 **dfs** ）
    * 廣度優先搜尋法（程式內函式名稱為 **bfs** ）
* [`Maze_Page.py`](https://github.com/JerryTsai12/Maze_Game/blob/main/Maze_Pages.py)  為 **「與玩家互動頁面」** 的程式碼（包含主畫面、設定等等頁面）
* [`Maze_Commend.json`](https://github.com/JerryTsai12/Maze_Game/blob/main/Maze_Commend.json)  存放 **「玩家自訂設定」** 以及 **「地圖基本設定」** （如地圖大小、牆壁代表符號等）
### 遊戲說明
#### （一）設定：
1.  進入設定畫面後，可以選擇要刪除、增加的操作按鍵，每種增加的操作按鍵只能為一個字元，如：「ww」不能作為一種操作按鍵設定，但「w」可以。
2.  一項操作可同時有不只一種的按鍵設定，如：可以設定向上的指令同時有「w」和「i」，輸入兩字母都會向上移動。
3.  若操控的按鍵刪除後沒有設定（即沒有設定操作按鍵），將會無法開始遊戲。

#### （二）遊玩：
1. 開始遊戲：  
將所有檔案放在同一資料夾後，執行[`Maze_game_main.py`](https://github.com/JerryTsai12/Maze_Game/blob/main/Maze_Game_main.py)檔案即可開始。  
進入後在主畫面（menu）輸入要遊玩的難度，即可開始遊玩迷宮，難度指令列表如下。    

|**難度** |**指令**|
|:-----:|:--------:|
|Easy|「e」|
|Normal|「n」|
|Hard|「h」|
|隱藏1：Hard地圖大小＋開啟迷霧|「HHEELLOO」|
|隱藏1：Hard地圖大小＋開啟迷霧|「HHEELLOOHHEELLOO」|
	  
2. 移動指令：
預設指令如下，指令可在設定頁面進行更改，每次操作時可不只輸入一個字母，如：若輸入「ww」則會向上走兩步。

|**移動** |**指令**|
|:-----:|:--------:|
|向上|依玩家設定，預設為「w」|
|向下|依玩家設定，預設為「s」|
|向左|依玩家設定，預設為「a」|
|向右|依玩家設定，預設為「d」|


3. 其他指令：

|**功能** |**指令**|**設定成功提示**|
|:-----|:--------:|:--------|
|設定瞬移位置（遊戲中符號#）|「set」|「Set the Teleport Position」|
|移動至瞬移位置	|「tp」|「Teleport」|
|迷霧開／關|「mist」|無|
|設定自動模式為：深度優先（DFS）|「dfs」|「auto.method = DFS」|
|設定自動模式為：廣度優先（BFS）|「bfs」|「auto.method = BFS」|
|設定自動模式為：標準答案（Standard）|「ans」|「auto.method = Standard」|
|使用自動模式走迷宮|「auto」|無，備註：自動模式預設為標準答案| 
