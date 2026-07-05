class Player:

    def __init__(self):

        # -------------------------
        # 기본 정보
        # -------------------------
        self.name = "Hero"

        self.icon = "🧍"

        self.x = 1
        self.y = 1

        # -------------------------
        # 레벨
        # -------------------------
        self.level = 1

        self.exp = 0
        self.need_exp = 100

        # -------------------------
        # 능력치
        # -------------------------
        self.hp = 100
        self.max_hp = 100

        self.atk = 10
        self.defense = 2

        self.critical = 5      # %
        self.dodge = 5          # %

        self.speed = 1

        # -------------------------
        # 재화
        # -------------------------
        self.gold = 0

        # -------------------------
        # 상태
        # -------------------------
        self.alive = True

    # -------------------------
    # 이동
    # -------------------------
    def move(self, dx, dy):

        self.x += dx
        self.y += dy

    # -------------------------
    # 데미지 받기
    # -------------------------
    def take_damage(self, damage):

        damage = max(1, damage - self.defense)

        self.hp -= damage

        if self.hp <= 0:
            self.hp = 0
            self.alive = False

        return damage

    # -------------------------
    # 회복
    # -------------------------
    def heal(self, amount):

        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    # -------------------------
    # 경험치 획득
    # -------------------------
    def add_exp(self, amount):

        self.exp += amount

        while self.exp >= self.need_exp:

            self.exp -= self.need_exp

            self.level += 1

            self.need_exp += 25

            self.max_hp += 20
            self.hp = self.max_hp

            self.atk += 3
            self.defense += 1

            self.critical += 1
            self.dodge += 1

            print("\n⭐ LEVEL UP!")
            print(f"LV {self.level}")

    # -------------------------
    # 골드 획득
    # -------------------------
    def add_gold(self, amount):

        self.gold += amount

    # -------------------------
    # 사망 여부
    # -------------------------
    def is_alive(self):

        return self.alive

    # -------------------------
    # 정보
    # -------------------------
    def info(self):

        return {
            "name": self.name,
            "level": self.level,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "atk": self.atk,
            "defense": self.defense,
            "critical": self.critical,
            "dodge": self.dodge,
            "gold": self.gold,
            "exp": self.exp
        }