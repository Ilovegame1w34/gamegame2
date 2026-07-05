from engine.save import SaveSystem
from entities.player import Player
from engine.world import World
from engine.renderer import Renderer
from engine.combat import Combat
from engine.inventory import Inventory
from systems.quests import QuestManager


class Game:

    def __init__(self):

        # 플레이어
        self.player = Player()

        # 인벤토리
        self.inventory = Inventory()

        # 월드
        self.world = World()

        # 렌더러
        self.renderer = Renderer()

        # 전투
        self.combat = Combat(
            self.player,
            self.inventory
        )

        # 퀘스트
        self.quests = QuestManager()

        # 실행 여부
        self.running = True
        # 저장 시스템
        self.save_system = SaveSystem()

    # ----------------------------------
    # 게임 시작
    # ----------------------------------
    def run(self):

        while self.running:

            self.renderer.draw(
                self.world,
                self.player,
                self.inventory
            )

            self.update()

        print("\n게임이 종료되었습니다.")

    # ----------------------------------
    # 입력
    # ----------------------------------
    def update(self):

        command = input(
            "\nWASD 이동 | I 인벤토리 | Q 퀘스트 | M 미니맵 | X 종료 > "
        ).lower()

        # 종료
        if command == "x":
            self.running = False
            return

        # 인벤토리
        if command == "i":
            self.inventory.show()
            input("\n엔터...")
            return

        # 퀘스트
        if command == "q":
            self.quests.show()
            input("\n엔터...")
            return

        # 미니맵 ON/OFF
        if command == "m":
            self.renderer.toggle_minimap()
            return

        dx = 0
        dy = 0

        if command == "w":
            dy = -1

        elif command == "s":
            dy = 1

        elif command == "a":
            dx = -1

        elif command == "d":
            dx = 1

        else:
            return

        new_x = self.player.x + dx
        new_y = self.player.y + dy

        # 벽
        if self.world.is_wall(new_x, new_y):
            return

        # 몬스터
        enemy = self.world.get_enemy_at(new_x, new_y)

        if enemy:

            result = self.combat.start_battle(enemy)

            # 승리
            if result == "win":

                if enemy in self.world.enemies:
                    self.world.enemies.remove(enemy)

                # 퀘스트 갱신
                self.quests.monster_killed(self.player)
                self.quests.gold_update(self.player)
                self.quests.level_update(self.player)

            # 사망
            elif result == "dead":

                self.renderer.game_over()
                self.running = False
                return

            # 도망
            elif result == "escape":
                return

        # 플레이어 이동
        self.player.move(dx, dy)

        # 월드 업데이트
        self.world.update(self.player)