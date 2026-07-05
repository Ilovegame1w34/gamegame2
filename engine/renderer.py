import os


class Renderer:

    def __init__(self):

        # 플레이어 기준 화면 크기
        self.view_width = 21
        self.view_height = 15

        # 미니맵 표시 여부
        self.show_minimap = True

    # ---------------------------------
    # 화면 지우기
    # ---------------------------------
    def clear(self):

        os.system("cls" if os.name == "nt" else "clear")

    # ---------------------------------
    # 메인 출력
    # ---------------------------------
    def draw(self, world, player, inventory):

        self.clear()

        half_w = self.view_width // 2
        half_h = self.view_height // 2

        start_x = max(0, player.x - half_w)
        end_x = min(world.width, player.x + half_w + 1)

        start_y = max(0, player.y - half_h)
        end_y = min(world.height, player.y + half_h + 1)

        print("=" * 55)
        print("         TerminalLegends v0.3.3-1")
        print("=" * 55)

        for y in range(start_y, end_y):

            line = ""

            for x in range(start_x, end_x):

                # 플레이어
                if player.x == x and player.y == y:
                    line += player.icon
                    continue

                # 몬스터
                enemy = world.get_enemy_at(x, y)

                if enemy:
                    line += enemy.icon
                    continue

                # 벽
                if world.map[y][x] == 1:
                    line += "🧱"
                else:
                    line += "  "

            print(line)

        self.draw_status(player)
        self.draw_equipment(inventory)

        if self.show_minimap:
            self.draw_minimap(world, player)

    # ---------------------------------
    # 플레이어 정보
    # ---------------------------------
    def draw_status(self, player):

        hp_bar = self.make_bar(player.hp, player.max_hp, 20)
        exp_bar = self.make_bar(player.exp, player.need_exp, 20)

        print()
        print("=" * 55)
        print(f"이름 : {player.name}")
        print(f"레벨 : {player.level}")
        print(f"HP   : {hp_bar} {player.hp}/{player.max_hp}")
        print(f"EXP  : {exp_bar} {player.exp}/{player.need_exp}")
        print(f"ATK  : {player.atk}")
        print(f"DEF  : {player.defense}")
        print(f"GOLD : {player.gold}")
        print("=" * 55)

    # ---------------------------------
    # 장비
    # ---------------------------------
    def draw_equipment(self, inventory):

        print("\n장비")

        print(f"⚔️ 무기 : {inventory.weapon if inventory.weapon else '없음'}")
        print(f"🛡️ 방어구 : {inventory.armor if inventory.armor else '없음'}")
        print(f"🧪 포션 : {inventory.potions}")

    # ---------------------------------
    # 미니맵
    # ---------------------------------
    def draw_minimap(self, world, player):

        print("\n🗺️ MINI MAP")

        scale = 5

        for y in range(0, world.height, scale):

            line = ""

            for x in range(0, world.width, scale):

                if player.x // scale == x // scale and player.y // scale == y // scale:
                    line += player.icon
                    continue

                enemy_found = None

                # 해당 칸 안에 몬스터가 있는지 검사
                for yy in range(y, min(y + scale, world.height)):
                    for xx in range(x, min(x + scale, world.width)):

                        enemy_found = world.get_enemy_at(xx, yy)

                        if enemy_found:
                            break

                    if enemy_found:
                        break

                if enemy_found:
                    line += enemy_found.icon

                elif world.map[y][x] == 1:
                    line += "🧱"

                else:
                    line += "⬜"

            print(line)

    # ---------------------------------
    # 미니맵 ON/OFF
    # ---------------------------------
    def toggle_minimap(self):

        self.show_minimap = not self.show_minimap

    # ---------------------------------
    # 진행바
    # ---------------------------------
    def make_bar(self, value, maximum, size):

        if maximum <= 0:
            maximum = 1

        filled = int((value / maximum) * size)

        if filled > size:
            filled = size

        return "🟩" * filled + "⬜" * (size - filled)

    # ---------------------------------
    # 게임 오버
    # ---------------------------------
    def game_over(self):

        self.clear()

        print()
        print(" ██████   █████  ███    ███ ███████")
        print("██       ██   ██ ████  ████ ██")
        print("██   ███ ███████ ██ ████ ██ █████")
        print("██    ██ ██   ██ ██  ██  ██ ██")
        print(" ██████  ██   ██ ██      ██ ███████")
        print()
        print("          💀 GAME OVER 💀")
        print()

    # ---------------------------------
    # 승리
    # ---------------------------------
    def victory(self):

        print("\n🏆 VICTORY!")

    # ---------------------------------
    # 레벨업
    # ---------------------------------
    def level_up(self, player):

        print("\n⭐ LEVEL UP!")
        print(f"현재 레벨 : {player.level}")