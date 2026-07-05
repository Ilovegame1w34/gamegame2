from entities.enemy import Enemy


class Enemy3(Enemy):

    def __init__(self, x, y):

        super().__init__(x, y)

        # -------------------------
        # 기본 정보
        # -------------------------
        self.name = "Troll"

        self.icon = "🧌"

        # -------------------------
        # 능력치
        # -------------------------
        self.hp = 150
        self.max_hp = 150

        self.attack = 22
        self.defense = 8

        self.critical = 15
        self.dodge = 8

        # -------------------------
        # 보상
        # -------------------------
        self.exp = 70
        self.gold = 100

        # -------------------------
        # AI
        # -------------------------
        self.view_range = 10

    # -------------------------
    # 특수 공격
    # -------------------------
    def attack_player(self, player):

        import random

        damage = max(1, self.attack - player.defense)

        # 20% 확률로 강타
        if random.randint(1, 100) <= 20:
            damage = int(damage * 1.8)
            print("💥 Troll의 내려찍기!")

        player.hp -= damage

        if player.hp < 0:
            player.hp = 0

        print(f"🧌 {self.name}의 공격!")
        print(f"{damage} 데미지!")

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