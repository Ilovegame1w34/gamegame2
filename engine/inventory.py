class Inventory:

    def __init__(self):

        # 아이템 목록
        self.items = []

        # 시작 아이템
        self.potions = 3

        # 장착 무기
        self.weapon = None

        # 장착 방어구
        self.armor = None

    # -------------------------
    # 아이템 추가
    # -------------------------
    def add_item(self, item):

        self.items.append(item)
        print(f"🎁 {item} 획득!")

    # -------------------------
    # 아이템 제거
    # -------------------------
    def remove_item(self, item):

        if item in self.items:
            self.items.remove(item)

    # -------------------------
    # 포션 사용
    # -------------------------
    def use_potion(self):

        if self.potions <= 0:
            return False

        self.potions -= 1
        return True

    # -------------------------
    # 포션 획득
    # -------------------------
    def add_potion(self, amount=1):

        self.potions += amount

    # -------------------------
    # 무기 장착
    # -------------------------
    def equip_weapon(self, weapon):

        self.weapon = weapon
        print(f"⚔️ {weapon} 장착!")

    # -------------------------
    # 방어구 장착
    # -------------------------
    def equip_armor(self, armor):

        self.armor = armor
        print(f"🛡️ {armor} 장착!")

    # -------------------------
    # 인벤토리 출력
    # -------------------------
    def show(self):

        print("\n" + "=" * 35)
        print("🎒 INVENTORY")
        print("=" * 35)

        print(f"🧪 Potion : {self.potions}")

        print()

        if self.weapon:
            print(f"⚔️ Weapon : {self.weapon}")
        else:
            print("⚔️ Weapon : 없음")

        if self.armor:
            print(f"🛡️ Armor  : {self.armor}")
        else:
            print("🛡️ Armor  : 없음")

        print("\n📦 Items")

        if len(self.items) == 0:
            print("없음")
        else:
            for i, item in enumerate(self.items, 1):
                print(f"{i}. {item}")

        print("=" * 35)

    # -------------------------
    # 아이템 존재 여부
    # -------------------------
    def has_item(self, item):

        return item in self.items

    # -------------------------
    # 인벤토리 초기화
    # -------------------------
    def clear(self):

        self.items.clear()
        self.potions = 0
        self.weapon = None
        self.armor = None