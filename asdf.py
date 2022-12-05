import pygame
import enum
import os

class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 32
        self.height = 32
        self.image = pygame.image.load(os.path.join('Assets', 'placeholdertile.png'))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.inflate(1.5, 1.5)
        self.rect.x = 0
        self.rect.y = 400
        self.rect.center = self.rect.x + 24, self.rect.y + 24

class Goal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 32
        self.height = 32
        self.image = pygame.image.load(os.path.join('Assets', 'placeholderfinish.png'))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 268

class Key(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 32
        self.height = 32
        self.image = pygame.image.load(os.path.join('Assets', 'placeholderkey.png'))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 300

class Door(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 32
        self.height = 32
        self.image = pygame.image.load(os.path.join('Assets', 'placeholderdoor.png'))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = 850
        self.rect.y = 300

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 32
        self.height = 32
        self.image = pygame.image.load(os.path.join('Assets', 'placeholderguy.png'))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.inflate(1.4, 1.4)
        self.x = 605
        self.y = 320
        self.rect.x = self.x
        self.rect.y = self.y
        self.rxvel = 0
        self.lxvel = 0
        self.yvel = 0
        self.initx = 0
        self.inity = 0
    
    def update(self):
        self.x += self.rxvel
        self.x -= self.lxvel
        self.y += self.yvel
        self.rect.x = self.x
        self.rect.y = self.y

class TileType(enum.Enum):
    EMPTY = None
    BLOCK = 1
    DOOR = 2
    KEY = 3
    GOAL = 4
    PLAYER = 5

    @classmethod
    def getClassMap(cls) -> dict:
        return {
            TileType.BLOCK: Block,
            TileType.DOOR: Door,
            TileType.KEY: Key,
            TileType.GOAL: Goal,
            TileType.PLAYER: Player
        }
    
    @classmethod
    def convertTileNum(cls):
        return {
            1: TileType.BLOCK,
            2: TileType.DOOR,
            3: TileType.KEY,
            4: TileType.GOAL,
            5: TileType.PLAYER
        }

class LevelPalette(enum.Enum):
    MEDIVAL = 0
    INDUSTRIAL = 1

class LevelMapData:
    L_1 = {
        "id": 0,
        "size": "40x20",
        "data": [
            [TileType.BLOCK for _ in range(40)],
            *[[TileType.BLOCK, *[TileType.EMPTY for _ in range(38)], TileType.BLOCK] for _ in range(18)],
            [TileType.BLOCK for _ in range(40)]
        ]
    }
    L_2 = {
        "id": 1,
        "size": "40x20",
        "data": [
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 4, 0, 1, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    }

class LevelMap:
    def __init__(self, window: pygame.display, levelMapTileMap: LevelMapData) -> None:
        self.window = window
        self.levelMapTileMap = levelMapTileMap

    def draw(self, groups):
        groupMap = {
            TileType.BLOCK: groups[1],
            TileType.DOOR: groups[2],
            TileType.KEY: groups[3],
            TileType.GOAL: groups[4],
            TileType.PLAYER: groups[5]
        }
        data = self.levelMapTileMap["data"]
        classMap = TileType.getClassMap()
        rowOffset = 0
        playerPos = ()
        for row in data:
            colOffset = 0
            for tile in row:
                if tile != TileType.EMPTY:
                    obj = classMap[tile]()
                    obj.rect.x = rowOffset
                    obj.rect.y = colOffset
                    if tile == TileType.PLAYER:
                        # TODO: implement initx
                        pass
                    # groups[0].add(obj)
                    # groupMap[tile].add(obj)
                colOffset += 32
            rowOffset += 32
    
    def getActionTiles(self) -> list[tuple[int, int, TileType]]:
        tilePositions = []
        for indx, row in enumerate(self.levelMapTileMap["data"]):
            for i, tile in enumerate(row):
                if tile in (TileType.EMPTY, TileType.BLOCK): continue
                tilePositions.append((indx, i, tile))
        return tilePositions

    def get(self):
        return self.levelMapTileMap
    
    def getID(self) -> int:
        return self.levelMapTileMap['id']

class Level:
    def __init__(
        self,
        window: pygame.display,
        levelMap: LevelMap,
        palette: LevelPalette,
        timer: float
    ):
        self.window = window
        self.levelMap = levelMap
        self.palette = palette
        self.timer = timer



w = pygame.display.set_mode((1280, 720)) # 256 offset from map on each side
lm = LevelMap(w, LevelMapData.L_1)
l = Level(w, lm, LevelPalette.MEDIVAL, 30)
w.fill((20, 0, 0))

l.levelMap.draw([0, 0, 0, 0, 0, 0])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
