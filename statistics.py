import randomize_item_table
import item_lot_formatter       #used to convert id number to text
from collections import defaultdict

start_seed = 0
NUM_SEEDS = 10000   #how many seeds to gen
stats_dir = "statistics/"
required_keys = ['lordvessel', 'lord_soul_shard_seath', 'lord_soul_shard_four_kings', 'lord_soul_bed_of_chaos', 'lord_soul_nito']

def save(combined, d, seed):
#pretty print locations            
    with open(stats_dir+"combined_stats.txt", 'w') as f:
        for k,v in sorted(combined.items(), key=lambda x:x[1], reverse=True):
            f.write("{0} ; {1} ; {2}\n".format(k, item_lot_formatter.LOCATION_DESCRIPTIONS[k], v))

    for k,v in d.items():
        with open(stats_dir+k+".txt", 'w') as f:
            for vk,vv in sorted(v.items(), key=lambda x:x[1], reverse=True):
                f.write(" {0} ; {1} ; {2}\n".format(vk, item_lot_formatter.LOCATION_DESCRIPTIONS[vk], vv))

    with open(stats_dir+"seeds.txt", 'w') as f:
        f.write(str(seed))

def seed_gen(seed, combined, d):
    key_locs = randomize_item_table.testing(str(seed))
    for k,v in key_locs.items():
        if k in required_keys:
            combined[v.location_id] +=1
            d[k][v.location_id] += 1
    return combined, d

def seed_loop():
    #initialize counting dicts
    combined = defaultdict(int)
    d = {}
    for k in required_keys:
        d[k] = defaultdict(int)

    #gen seeds and count locs
    for seed in range(start_seed, NUM_SEEDS+start_seed):
        combined, d = seed_gen(seed, combined, d)
        if (seed+1) % 10 == 0:
            save(combined, d, seed+1)
    save(combined, d, seed+1)

if __name__ == "__main__":
    seed_loop()
