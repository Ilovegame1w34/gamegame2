import random


class Enemy:

    def __init__(self, x, y):

        # -------------------------
        # 기본 정보
        # -------------------------
        self.name = "Zombie"

        self.icon = "🧟"

        self.x = x
        self.y = y

        # -------------------------
        # 능력치
        # -------------------------
        self.hp = 40
        self.max_hp = 40

        self.attack = 8
        self.defense = 2

        self.critical = 5
        self.dodge = 3

        # -------------------------
        # 보상
        # -------------------------
        self.exp = 15
        self.gold = 20

        # -------------------------
        # AI
        # -------------------------
        self.view_range = 6
        self.move_delay = 0

    # -------------------------
    # 살아있는가?
    # -------------------------
    def is_alive(self):

        return self.hp > 0

    # -------------------------
    # 데미지 받기
    # -------------------------
    def take_damage(self, damage):

        damage = max(1, damage - self.defense)

        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        return damage

    # -------------------------
    # 공격
    # -------------------------
    def attack_player(self, player):

        damage = max(1, self.attack - player.defense)

        if random.randint(1, 100) <= self.critical:
            damage *= 2
            print("💥 Zombie 크리티컬!")

        player.hp -= damage

        if player.hp < 0:
            player.hp = 0

        print(f"🧟 Zombie의 공격!")
        print(f"{damage} 데미지!")

    # -------------------------
    # 이동
    # -------------------------
    def move(self, dx, dy, world):

        nx = self.x + dx
        ny = self.y + dy

        if world.is_walkable(nx, ny):

            if world.get_enemy_at(nx, ny) is None:

                self.x = nx
                self.y = ny

    # -------------------------
    # AI
    # -------------------------
    def update(self, player, world):

        dx = player.x - self.x
        dy = player.y - self.y

        distance = abs(dx) + abs(dy)

        # 플레이어 추적
        if distance <= self.view_range:

            if abs(dx) > abs(dy):

                self.move(
                    1 if dx > 0 else -1,
                    0,
                    world
                )

            else:

                self.move(
                    0,
                    1 if dy > 0 else -1,
                    world
                )

        # 랜덤 이동
        else:

            if random.randint(1, 100) <= 30:

                dx = random.choice([-1, 0, 1])
                dy = random.choice([-1, 0, 1])

                self.move(dx, dy, world)

    # -------------------------
    # 정보
    # -------------------------
    def info(self):

        return {
            "name": self.name,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "attack": self.attack,
            "defense": self.defense,
            "exp": self.exp,
            "gold": self.gold
        }