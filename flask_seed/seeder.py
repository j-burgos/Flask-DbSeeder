

from base import BaseSeeder

class Seeder:

    db = None
    seeds = None
    delete = None

    def __init__(self, db, delete=True):
        self.db = db
        self.seeds = []
        self.delete = delete

    def add_seed(self, seed):
        self.seeds.append(seed)

    def add_seeds(self, seeds):
        for seed in seeds:
            self.seeds.append(seed)

    def run(self):
        for seed in self.seeds:
            entity_class = seed[0].__class__
            seeder = BaseSeeder(self.db.session, entity_class, self.delete)
            seeder.seed(seed)
