from entities.enemy import Enemy


class Boss(Enemy):

    def __init__(self, x, y):

        super().__init__(x, y)

        self.name = "Demon King"

        self.icon = "👑"

        self.hp = 1000
        self.max_hp = 1000

        self.attack = 40

        self.defense = 15

        self.exp = 500

        self.gold = 1000

        self.critical = 15

        self.dodge = 5

        self.phase = 1

    # -------------------------
    # 보스 AI
    # -------------------------
    def update(self, player, world):
        pass

    # -------------------------
    # 체력에 따른 페이즈
    # -------------------------
    def check_phase(self):

        if self.hp <= self.max_hp * 0.5 and self.phase == 1:

            self.phase = 2

            self.attack += 15
            self.defense += 5

            print("🔥 Demon King가 분노했습니다!")

        if self.hp <= self.max_hp * 0.2 and self.phase == 2:

            self.phase = 3

            self.attack += 20
            self.defense += 10

            print("💀 Demon King 최종 형태!")

    # -------------------------
    # 특수 공격
    # -------------------------
    def special_attack(self, player):

        damage = self.attack * 2

        player.hp -= damage

        if player.hp < 0:
            player.hp = 0

        print(f"💥 {self.name}의 필살기!")
        print(f"{damage} 데미지!")

    # -------------------------
    # 일반 공격
    # -------------------------
    def normal_attack(self, player):

        damage = max(1, self.attack - player.defense)

        player.hp -= damage

        if player.hp < 0:
            player.hp = 0

        print(f"{self.name} 공격!")
        print(f"{damage} 데미지!")

    # -------------------------
    # 공격 선택
    # -------------------------
    def attack_player(self, player):

        self.check_phase()

        import random

        if random.randint(1, 100) <= 20:
            self.special_attack(player)
        else:
            self.normal_attack(player)