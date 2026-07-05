from entities.enemy import Enemy


class Enemy2(Enemy):

    def __init__(self, x, y):

        super().__init__(x, y)

        # -------------------------
        # 기본 정보
        # -------------------------
        self.name = "Orc"

        self.icon = "👹"

        # -------------------------
        # 능력치
        # -------------------------
        self.hp = 80
        self.max_hp = 80

        self.attack = 15
        self.defense = 5

        self.critical = 10
        self.dodge = 5

        # -------------------------
        # 보상
        # -------------------------
        self.exp = 35
        self.gold = 50

        # -------------------------
        # AI
        # -------------------------
        self.view_range = 8

    # -------------------------
    # 특수 공격
    # -------------------------
    def attack_player(self, player):

        import random

        damage = max(1, self.attack - player.defense)

        # 10% 확률로 강공격
        if random.randint(1, 100) <= 10:
            damage *= 2
            print("💥 Orc의 강공격!")

        player.hp -= damage

        if player.hp < 0:
            player.hp = 0

        print(f"👹 {self.name}의 공격!")
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