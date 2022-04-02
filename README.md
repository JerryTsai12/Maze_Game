# Maze_Game 迷宮遊戲
## 此專案為 **選修課程–進階程式設計** 的 **課程學習成果**
## 作者：阿瑋、阿暐
### 在此專案中，有四個.py檔案，一個.json檔案，其中   
* Maze_game_main.py 為 **主程式碼** ，下載後執行此程式碼以進入遊戲
* Maze_Auto.py 三種 **迷宮尋路演算法** 的程式碼，分別為  
    * 標準答案（程式內函式名稱為**standard_answer**）
    * 深度優先搜尋法（程式內函式名稱為**dfs**）
    * 廣度優先搜尋法（程式內函式名稱為**bfs**）
* Maze_Class.py 為**迷宮生成演算法**的程式碼
* Maze_Page.py 為**與玩家互動頁面**的程式碼（包含主畫面、設定等等頁面）
* Maze_Commend.json 為存放**玩家自訂設定**的檔案  
### 遊戲說明
#### （一）設定：
1.  進入設定畫面後，可以選擇要刪除、增加的操作按鍵，每種增加的操作按鍵只能為一個字元，如：「ww」不能作為一種操作按鍵設定，但「w」可以。
2.  一項操作可同時有不只一種的按鍵設定，如：可以設定向上的指令同時有「w」和「i」，輸入兩字母都會向上移動。
3.  若操控的按鍵刪除後沒有設定（即沒有設定操作按鍵），將會無法開始遊戲。

#### （二）遊玩：
1. 開始遊戲：
在主畫面（menu）輸入要遊玩的難度，即可開始遊戲，難度指令列表如下。
<table>
  <tr>
    <td>難度</td>
    <td>指令</td>
  </tr>
  <tr>
    <td>Easy</td>
    <td>「e」</td>
  </tr>
  <tr>
    <td>Normal</td>
    <td>「n」</td>
  </tr>
  <tr>
    <td>Hard</td>
    <td>「h」</td>
  </tr>
  <tr>
    <td>隱藏1：Hard地圖大小＋開啟迷霧</td>
    <td>「HHEELLOO」</td>
  </tr>
  <tr>
    <td>隱藏2：加大地圖大小＋開啟迷霧</td>
    <td>「HHEELLOOHHEELLOO」</td>
  </tr>
</table>
	  
2. 移動指令：
預設指令如下，指令可在設定頁面進行更改，每次操作時可不只輸入一個字母，如：若輸入「ww」則會向上走兩步。
<table>
  <tr>
    <td>移動</td>
    <td>指令</td>
  </tr>
  <tr>
    <td>向上</td>
    <td>依玩家設定，預設為「w」</td>
  </tr>
  <tr>
    <td>向下</td>
    <td>依玩家設定，預設為「s」</td>
  </tr>
  <tr>
    <td>向左</td>
    <td>依玩家設定，預設為「a」</td>
  </tr>
  <tr>
    <td>向右</td>
    <td>依玩家設定，預設為「d」</td>
  </tr>
</table>

3. 其他指令：
<table>
  <tr>
    <td>功能</td>
    <td>指令</td>
    <td>設定成功提示</td>
  </tr>
  <tr>
    <td>設定瞬移位置（遊戲中符號#）</td>
    <td>「set」</td>
    <td>「Set the Teleport Position」</td>
  </tr>
  <tr>
    <td>移動至瞬移位置	</td>
    <td>「tp」</td>
    <td>「Teleport」</td>
  </tr>
  <tr>
    <td>迷霧開／關</td>
    <td>「mist」</td>
    <td>無</td>
  </tr>
  <tr>
    <td>設定自動模式為：深度優先（DFS）</td>
    <td>「dfs」</td>
    <td>「auto.method = BFS」</td>
  </tr>
  <tr>
    <td>設定自動模式為：廣度優先（BFS）</td>
    <td>「bfs」</td>
    <td>「auto.method = BFS」</td>
  </tr>
    <tr>
    <td>設定自動模式為：標準答案（Standard）</td>
    <td>「ans」</td>
    <td>「auto.method = Standard」</td>
  </tr>
    <tr>
    <td>使用自動模式走迷宮</td>
    <td>「auto」</td>
    <td>無，備註：自動模式預設為標準答案</td>
  </tr>
</table>

