import random

from entities.enemy import Enemy
from entities.enemy2 import Enemy2
from entities.enemy3 import Enemy3


class World:

    # ----------------------------------
    # 생성
    # ----------------------------------
    def __init__(self):

        self.chunk_size = 10

        self.chunk_x = 10
        self.chunk_y = 10

        self.width = self.chunk_size * self.chunk_x
        self.height = self.chunk_size * self.chunk_y

        self.map = [
            [0 for _ in range(self.width)]
            for _ in range(self.height)
        ]

        self.enemies = []

        self.generate_world()

        self.spawn_initial_enemies()

    # ----------------------------------
    # 월드 생성
    # ----------------------------------
    def generate_world(self):

        for y in range(self.height):

            for x in range(self.width):

                if (
                    x == 0 or
                    y == 0 or
                    x == self.width - 1 or
                    y == self.height - 1
                ):
                    self.map[y][x] = 1

                elif random.random() < self.get_obstacle_rate(x, y):
                    self.map[y][x] = 1

    # ----------------------------------
    # 장애물 생성 확률
    # ----------------------------------
    def get_obstacle_rate(self, x, y):

        chunk = x // self.chunk_size

        if chunk <= 2:
            return 0.04

        elif chunk <= 5:
            return 0.07

        else:
            return 0.10

    # ----------------------------------
    # 초기 몬스터
    # ----------------------------------
    def spawn_initial_enemies(self):

        for _ in range(30):
            self.spawn_enemy()

    # ----------------------------------
    # 몬스터 생성
    # ----------------------------------
    def spawn_enemy(self):

        while True:

            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)

            if self.map[y][x] == 1:
                continue

            if self.get_enemy_at(x, y):
                continue

            enemy = random.choice([
                Enemy,
                Enemy2,
                Enemy3
            ])(x, y)

            self.enemies.append(enemy)

            break

    # ----------------------------------
    # 몬스터 삭제
    # ----------------------------------
    def remove_enemy(self, enemy):

        if enemy in self.enemies:
            self.enemies.remove(enemy)

    # ----------------------------------
    # 몬스터 찾기
    # ----------------------------------
    def get_enemy_at(self, x, y):

        for enemy in self.enemies:

            if enemy.x == x and enemy.y == y:
                return enemy

        return None

    # ----------------------------------
    # 벽 여부
    # ----------------------------------
    def is_wall(self, x, y):

        if (
            x < 0 or
            y < 0 or
            x >= self.width or
            y >= self.height
        ):
            return True

        return self.map[y][x] == 1

    # ----------------------------------
    # 이동 가능 여부
    # ----------------------------------
    def is_walkable(self, x, y):

        return not self.is_wall(x, y)

    # ----------------------------------
    # 월드 업데이트
    # ----------------------------------
    def update(self, player):

        for enemy in self.enemies:

            if hasattr(enemy, "update"):
                enemy.update(player, self)

    # ----------------------------------
    # 청크 반환
    # ----------------------------------
    def get_chunk(self, x, y):

        return (
            x // self.chunk_size,
            y // self.chunk_size
        )

    # ----------------------------------
    # 현재 청크의 몬스터
    # ----------------------------------
    def get_chunk_enemies(self, chunk_x, chunk_y):

        enemies = []

        for enemy in self.enemies:

            ex = enemy.x // self.chunk_size
            ey = enemy.y // self.chunk_size

            if ex == chunk_x and ey == chunk_y:
                enemies.append(enemy)

        return enemies

    # ----------------------------------
    # 주변 청크 로드
    # ----------------------------------
    def loaded_chunks(self, player):

        cx, cy = self.get_chunk(player.x, player.y)

        chunks = []

        for y in range(cy - 2, cy + 3):

            for x in range(cx - 2, cx + 3):

                if (
                    0 <= x < self.chunk_x and
                    0 <= y < self.chunk_y
                ):
                    chunks.append((x, y))

        return chunks

    # ----------------------------------
    # 청크 이름
    # ----------------------------------
    def get_chunk_name(self, chunk_x, chunk_y):

        return f"Chunk ({chunk_x}, {chunk_y})"

    # ----------------------------------
    # 몬스터 수
    # ----------------------------------
    def enemy_count(self):

        return len(self.enemies)

    # ----------------------------------
    # 랜덤 리스폰
    # ----------------------------------
    def respawn_enemy(self):

        if len(self.enemies) < 30:
            self.spawn_enemy()

    # ----------------------------------
    # 월드 정보
    # ----------------------------------
    def info(self):

        return {
            "width": self.width,
            "height": self.height,
            "chunks_x": self.chunk_x,
            "chunks_y": self.chunk_y,
            "chunk_size": self.chunk_size,
            "enemy_count": len(self.enemies)
        }