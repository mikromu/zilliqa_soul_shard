import requests, time

def soul_shard():
    print("Zilliqa — A Soul Has Just Been Sharded Across 1000 Pieces")
    seen = set()
    while True:
        r = requests.get("https://api.zilliqa.com/", 
                        json={"id": "1", "jsonrpc": "2.0", "method": "GetLatestTxBlock", "params": [""]})
        height = r.json()["result"]["header"]["BlockNum"]
        r2 = requests.get(f"https://api.zilliqa.com/", json={
            "id": "1", "jsonrpc": "2.0", 
            "method": "GetTransactionsForTxBlock", 
            "params": [height]
        })
        for batch in r2.json().get("result", [[]]):
            for tx in batch:
                h = tx[0]
                if h in seen: continue
                seen.add(h)
                
                # Detect insane micro-shard spam (1000+ txs from one wallet in one block)
                sender = tx[2]
                if list(seen).count(sender[:10]) > 800:  # same sender dominates the entire block
                    print(f"A SOUL WAS SHARDED\n"
                          f"{sender[:16]}... just split itself into {list(seen).count(sender[:10])} fragments\n"
                          f"Block: {height}\n"
                          f"Latest shard: {h}\n"
                          f"https://viewblock.io/zilliqa/tx/{h}\n"
                          f"→ One consciousness, one thousand voices\n"
                          f"→ Zilliqa didn't process this person. It absorbed them.\n"
                          f"→ They now exist in every shard simultaneously.\n"
                          f"{'◊'*50}\n")
        time.sleep(1.3)

if __name__ == "__main__":
    soul_shard()
