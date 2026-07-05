import random


class Combat:

    def __init__(self, player, inventory=None):
        self.player = player
        self.inventory = inventory

    # -------------------------
    # 전투 시작
    # -------------------------
    def start_battle(self, enemy):

        print("\n" + "=" * 40)
        print(f"⚔️ {enemy.name} 등장!")
        print("=" * 40)

        while self.player.hp > 0 and enemy.hp > 0:

            print("\n----------------------------")
            print(f"🧍 HP : {self.player.hp}/{self.player.max_hp}")
            print(f"{enemy.icon} {enemy.name} HP : {enemy.hp}/{enemy.max_hp}")
            print("----------------------------")

            print("1. 공격")
            print("2. 포션")
            print("3. 도망")

            command = input("> ")

            if command == "1":

                damage = self.calculate_damage(
                    self.player.atk,
                    getattr(enemy, "defense", 0)
                )

                critical = self.critical_hit()

                if critical:
                    damage *= 2
                    print("💥 크리티컬!")

                enemy.hp -= damage

                if enemy.hp < 0:
                    enemy.hp = 0

                print(f"⚔️ {enemy.name}에게 {damage} 데미지!")

            elif command == "2":

                if self.inventory:

                    if self.inventory.use_potion():

                        heal = 50

                        self.player.hp += heal

                        if self.player.hp > self.player.max_hp:
                            self.player.hp = self.player.max_hp

                        print(f"🧪 포션 사용 (+{heal})")

                    else:
                        print("❌ 포션이 없습니다.")

                else:
                    print("❌ 인벤토리가 없습니다.")

            elif command == "3":

                if self.try_escape():
                    print("🏃 도망쳤습니다.")
                    return "escape"

                print("❌ 도망 실패!")

            else:
                continue

            if enemy.hp <= 0:
                break

            if self.dodge(self.player.dodge):

                print("💨 공격 회피!")

            else:

                damage = self.calculate_damage(
                    enemy.attack,
                    self.player.defense
                )

                self.player.hp -= damage

                if self.player.hp < 0:
                    self.player.hp = 0

                print(f"{enemy.icon} {enemy.name}의 공격!")
                print(f"💢 {damage} 데미지!")

        if self.player.hp <= 0:

            print("\n===================")
            print("💀 GAME OVER")
            print("===================")

            return "dead"

        print(f"\n🎉 {enemy.name} 처치!")

        self.player.exp += enemy.exp
        self.player.gold += enemy.gold

        print(f"+{enemy.exp} EXP")
        print(f"+{enemy.gold} GOLD")

        self.level_up()

        return "win"

    # -------------------------
    # 데미지 계산
    # -------------------------
    def calculate_damage(self, attack, defense):

        damage = attack - defense

        if damage < 1:
            damage = 1

        damage += random.randint(0, 3)

        return damage

    # -------------------------
    # 크리티컬
    # -------------------------
    def critical_hit(self):

        return random.randint(1, 100) <= self.player.critical

    # -------------------------
    # 회피
    # -------------------------
    def dodge(self, chance):

        return random.randint(1, 100) <= chance

    # -------------------------
    # 도망
    # -------------------------
    def try_escape(self):

        return random.randint(1, 100) <= 35

    # -------------------------
    # 레벨업
    # -------------------------
    def level_up(self):

        while self.player.exp >= self.player.need_exp:

            self.player.exp -= self.player.need_exp

            self.player.level += 1

            self.player.need_exp += 20

            self.player.max_hp += 20
            self.player.hp = self.player.max_hp

            self.player.atk += 2
            self.player.defense += 1
            self.player.critical += 1
            self.player.dodge += 1

            print("\n====================")
            print("⭐ LEVEL UP!")
            print(f"LV {self.player.level}")
            print("====================")
            print("+20 HP")
            print("+2 ATK")
            print("+1 DEF")
            print("+1 CRI")
            print("+1 DODGE")