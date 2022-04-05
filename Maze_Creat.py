import json
import random
import string
import os

def Clear():
    """
    清除畫面
    """
    os.system("cls" if os.name == "nt" else "clear")

class Node:
    """
    用來記錄位置：可紀錄目前座標、前後聯通節點的型別
    
    Attributes:
        self : 此位置座標
        parent: 此位置前一個聯通的Node
        child: 此位置下一格
    Method:
        append_child -> None : 將一節點，放入目前節點的child中
        __call__ : 座標回傳
        
    """
    def __init__(self, position_self: list[int], position_parent: "Node",child: list["Node"]):
        """
        Args:
            position_self (list[int]): 此節點的位置座標
            position_parent (Node): 此節點前一聯通的節點
            child (list["Node"]): 此節點與後面聯通的節點
        """
        self.self = position_self
        self.parent = position_parent
        self.children = [child]

    def append_child(self, child: "Node"):
        """
        將一節點，放入child中紀錄
        
        Args:
            child (Node): 要放入與此節點聯通的下一節點
        """
        self.children.append(child)

    def __call__(self):
        """
        座標回傳
        
        Returns:
            list[int]: 此節點座標
        """
        return self.self

class Maze:
    """
    迷宮資訊
    
    Attributes:
        maze(list): 迷宮
        mist(list): 迷霧
        width(int): 迷宮(迷霧)寬度
        height(int): 迷宮(迷霧)高度
        path(list[Node]): 所有玩家可到達位置
        end(node): 終點位置
        start(node): 起點位置
        position(dict): 位置
            key: "start", "end", "coin"
        symbol(dict): 代表符號
            key: "wall", "backgroun", "end", "coin", "mist"
        size(dict): 不同難度的地圖大小
            key: "easy", "normal", "hard", "hheelloo", "hheelloohheelloo"
    Method:
        draw(show = False) -> None : 顯示迷宮於畫面
        create(animation = True)-> None: 生成迷宮
    """
    def __init__(self, difficulty: str):
        """
        根據難度，從json讀取迷宮基本設定
        
        Args:
            difficulty (str): 選擇的遊戲難度
        """
        # 從json檔案讀取資料
        with open("Maze_Commend.json","r") as file:
            data = json.load(file)
        
        self.symbol = data["maze"]["symbol"]    # 讀取遊戲中的各種代表符號
        # 讀取並設定遊戲中的迷宮寬、高
        self.size = data["maze"]["size"]
        self.width = self.size[str(difficulty)][0]
        self.height = self.size[str(difficulty)][1]
        
        self.path = []
        self.end = None
        self.start = None
        self.position = {
            "start":None,
            "end":None,
            "coin":None
        }
        
        self.maze = [[self.symbol["wall"] for w in range(self.width)] for h in range(self.height)] # 預設迷宮所有位置皆為牆
        self.mist = [[self.symbol["mist"] for w in range(self.width)] for h in range(self.height)] # 預設迷霧所有位置皆為霧
    
    def draw(self, show = False): 
        """
        顯示迷宮畫面

        Args:
            show (bool, optional): 是否顯示所有迷宮（無迷霧）. Defaults to False.
        """
        if show == True:
            display = "MAZE GAME\n"
            for line in self.maze:  # 無迷霧版本
                display += "".join(line) + "\n"
            Clear()
            print(display)
        else:
            display = "MAZE GAME\n"
            for line in self.mist:  # 有迷霧版本
                display += "".join(line) + "\n"
            Clear()
            print(display)

    
    def create(self, animation = True):
        """
        生成迷宮

        Args:
            animation (bool, optional): 是否要顯示，生成迷宮的動畫. Defaults to True.
        """
        def is_wall(worker: list[int], direction: list[int]):   # 確認欲前往位置是否為牆壁
            """
            確認欲前往的座標，是否為牆壁

            Args:
                worker (list[int]): 目前位置的座標
                direction (list[int]): 欲前往的方向 [y,x]

            Returns:
                bool: 欲前往方向的座標，是否為牆壁
            """
            try_worker = [worker[0]+direction[0],worker[1]+direction[1]]    #嘗試位置
            out_boundary =    try_worker[0] < 0 or \
                                try_worker[0] > self.width-1 or \
                                try_worker[1] < 0 or \
                                try_worker[1] > self.height-1      #確認是否抵達邊界
            if not out_boundary:
                check_maze = self.maze[try_worker[1]][try_worker[0]] == self.symbol["wall"]     #確認是否為牆壁
                if check_maze:
                    return True
            
            return False
        
        def is_neighbor_wall(worker: list[int], direction: list[int]):  # 確認欲前往位置是否會與其他道路聯通
            """
            確認欲前往座標，是否會與其他道路聯通（走欲嘗試方向後的座標，它的四周是否為牆壁）

            Args:
                worker (list[int]): 目前位置的座標
                direction (list[int]): 欲前往方向 [y, x]

            Returns:
                bool: 欲前往位置，是否會與其他道路聯通
            """
            try_worker = [worker[0] + direction[0], worker[1] + direction[1]]
            check_direction = [[1,0],[-1,0],[0,1],[0,-1]]   # 欲檢查方向
            i = 0
            while i < len(check_direction):
                is_opposite_direction = check_direction[i][0] * direction[0] +\
                                        check_direction[i][1] * direction[1] == -1  # 是否為反方向
                if is_opposite_direction == True:
                    check_direction.pop(i)
                else:
                    i += 1
                    
            for d in check_direction:   # 檢查是否為牆壁
                if is_wall(try_worker, d) == False:
                    return False
            return True
        
        def choose_random_position(path: list[Node]):  
            """
            從路徑名單，隨機選擇一個可分岔的位置

            Args:
                path (list[Node]): 還沒檢查過，是否可分岔的路徑

            Returns:
                Node: 可以分岔的位置之Node（ 若無，則回傳 Node(-1,0,0) ）
            """
            try_direction = [[1,0],[-1,0],[0,1],[0,-1]] # 要嘗試的方向
            i = 0
            while i < len(path):
                p = path[i]()
                check = False
                for d in try_direction:
                    if is_wall(p,d) and is_neighbor_wall(p,d):
                        check = True
                        break

                if check == True:
                    i += 1
                else:
                    path.pop(i) # 如果不可分岔就從可能選項中刪除
            
            if path == []:
                return Node(-1,0,0)
            else:
                return random.choice(path) # 從路徑中，隨機選擇可分岔位置，並回傳
        def choose_random_direction(worker: list[int]):
            """
            從目前位置的座標，隨機選擇一個可分岔的方向

            Args:
                worker (list[int]): 目前位置的座標

            Returns:
                list[int]: 可分岔的方向（ 若無則為空list ）
            """
            try_direction = [[1,0],[-1,0],[0,1],[0,-1]]     # 要嘗試的方向

            i = 0
            #   確認欲嘗試方向，是否為牆壁
            #   若非，則將此可能嘗試方向刪除
            while i < len(try_direction):   
                if is_wall(worker,try_direction[i]):
                    i += 1
                else:
                    try_direction.pop(i)

            i = 0
            #   確認欲嘗試方向，是否為會與其他道路聯通（欲嘗試座標的四周，是否為牆壁）
            #   若非，則將此可能嘗試方向刪除 
            while i < len(try_direction):
                if is_neighbor_wall(worker, try_direction[i]):      # 如果欲嘗試的方向不是牆壁，就把此方向從名單刪除
                    i += 1
                else:
                    try_direction.pop(i)
                
            if try_direction == []:
                return []
            else:
                return random.choice(try_direction)  # 從方向名單中，隨機選擇可分岔方向並回傳          
        
        worker = Node([random.randint(1,self.width-2), random.randint(1,self.height-2)], None, None)# 工人[x, y], 隨機在地圖中，選擇欲拆除的位置
        self.maze[worker()[1]][worker()[0]] = self.symbol["background"]      # 拆除工人所在位置的牆（將原本牆壁的位置設定成背景）
        
        path: list[Node] = []   # 紀錄可能的分岔點
        path_all: list[Node] = []       # 紀錄所有的路徑
        self.path = path_all
        path.append(worker)
        path_all.append(worker)
        
        end_point = []  # 紀錄路徑的盡頭
        
        while True:
            if animation:
                self.draw(show = True)
                
            direction = choose_random_direction(worker())
            
            if direction == []:         # 如果附近無處可拆
                tmp_position = choose_random_position(path)     # 隨機找一個可以拆的位置
                if tmp_position() == -1:     # 如果找不到
                    break       # 結束迷宮生成
                else:
                    end_point.append(worker)      # 將此座標加入路徑盡頭
                    worker = tmp_position     # 從隨機選擇的位置繼續進行迷宮生成
            
            else:       # 如果附近有牆可拆
                next_worker = Node([worker()[0]+direction[0],worker()[1]+direction[1]], worker, None)
                worker.append_child(next_worker)
                self.maze[next_worker()[1]][next_worker()[0]] = self.symbol["background"]       #拆除新工人所在位置的牆
                path.append(next_worker)       # 紀錄移動後的工人位置於可能的分岔點
                path_all.append(next_worker)
                worker = next_worker    # 更新目前位置

            
        self.position["coin"] = random.choice(path_all)       # 於所有的路徑中，隨機選擇一個位置，設定為硬幣位置
        self.maze[self.position["coin"]()[1]][self.position["coin"]()[0]]  # 於選擇的硬幣位置放硬幣
        
        # 從所有的路徑盡頭中，決定迷宮遊戲起點、終點
        index = random.randint(0,len(end_point)-1)  # 隨機在路徑名單中，尋找一個索引
        self.start = (end_point[index]) # 根據索引，設定起點
        self.position["start"] = list(self.start())
        end_point.pop(index)    # 將起點位置，從路徑盡頭名單中刪除，為了讓終點不會和起點位置相同

        self.end = random.choice(end_point)
        self.position["end"] = list(self.end())     # 設定終點
        
        self.maze[self.end()[1]][self.end()[0]] = self.symbol["end"]   # 標示出口位置
        
        self.draw(show = True)      # 顯示迷宮生成的結果  
   
class Player:
    """
    玩家資訊
    
    Attributes:
        position(list) : [ y, x ] 玩家起始位置
        symbol(dict): 代表符號
            keys: "player", "tp"
        control(dict) : 控制遊戲的指令
            key: "up", "down", "left", "right"
    
    Method:
        move(commend: string, maze: maze)->None : 根據指令，移動玩家位置
    """
    
    def __init__(self,position: list[int]):
        """
        從json讀取檔案資料，設定按鍵、玩家代表符號
        
        Args:
            position (list[int]): [x,y] 玩家起始位置
        """
        
        with open("Maze_Commend.json","r") as file:
            data = json.load(file)
        
        self.symbol = data["player"]["symbol"]   # 從檔案讀取player裡的資料
        self.control = data["player"]["control"]     # 從檔案讀取控制的方式(按鍵)

        self.position = position
        self.tp = position # tp（瞬移）位置
        
    def move(self, commend: str, maze: Maze):
        """
        根據指令移動玩家，若指令不在指令字典中，則不移動

        Args:
            commend (string): 輸入指令
            maze (maze): 將玩家觸發的事件(吃到硬幣)，反應在迷宮地圖中
        """
        def set_next_position(now_position: list[int], try_position: list[int], maze: "Maze"):
            """
            如果「嘗試位置」可移動，則回傳「嘗試位置」，否則回傳「目前位置」
            
            Args:
                now_position (list[int]): 目前位置
                next_position (list[int]): 嘗試移動位置
                maze (maze): 迷宮

            Returns:
                list[int]: 位置
            """
            x = try_position[0]
            y = try_position[1]
            if maze.maze[y][x] != maze.symbol["wall"]:    #如果位置不是牆壁
                if maze.maze[y][x] == maze.symbol["coin"]:
                    maze.maze[y][x] = maze.symbol["background"]     # 將coin消除
                    maze.mist = maze.maze   # 將迷霧全部消除
                return try_position
            else:
                return now_position
        
        if commend in self.control["up"]:
            next_position = [self.position[0], self.position[1] - 1]    # 向上走一步
        elif commend in self.control["down"]:
            next_position = [self.position[0], self.position[1] + 1]    # 向下走一步
        elif commend in self.control["left"]:
            next_position = [self.position[0] - 1, self.position[1]]    # 向左走一步
        elif commend in self.control["right"]:
            next_position = [self.position[0] + 1, self.position[1]]    # 向右走一步
        else:
            return None

        self.position = set_next_position(self.position, next_position, maze)   # 更新目前位置

class Auto_node:
    """
    給尋路演算用的node，紀錄目前座標、前一聯通的node
    
    Attributes:
        position : 目前位置的座標
        parent: 此位置前一個聯通的 Auto_ode
    Method:
        __call__ : 座標回傳
    """
    def __init__(self,position:list[int], parent: "Auto_node"):
        """
        紀錄目前座標、前一聯通位置的 Auto_node

        Args:
            position (list[int]): 目前座標
            parent (Auto_node): 前一聯通位置的 Auto_node
        """
        self.position = list(position)
        self.parent = parent
    def __call__(self):
        """
        目前座標回傳

        Returns:
            list[int]: 目前座標
        """
        return self.position
