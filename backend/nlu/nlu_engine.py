import io
import json

from snips_nlu import SnipsNLUEngine, load_resources

SEED = 32
nlu_engine = SnipsNLUEngine(resources=load_resources("snips_nlu_en"), random_state=SEED)


with io.open("nlu/dataset.json", 'r') as f:
    dataset = json.load(f)

nlu_engine.fit(dataset)


