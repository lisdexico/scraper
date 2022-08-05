from peer import Peer
import time

frequency_in_minutes = 6

peer_domains_and_names = [("peer-ec1.decentraland.org", "hephaestus"),
                ("peer-ec2.decentraland.org", "hela"),
                ("peer-wc1.decentraland.org", "heimdallr"),
                ("peer-eu1.decentraland.org", "baldr"),
                ("peer-ap1.decentraland.org", "artemis"),
                ("interconnected.online", "loki"),
                ("peer.decentral.io", "dg"),
                ("peer.melonwave.com", "odin"),
                ("peer.kyllian.me", "unicorn"),
                ("peer.uadevops.com", "marvel"),
                ("peer.dclnodes.io", "athena")]

peers = [Peer(peer[0], peer[1]) for peer in peer_domains_and_names]


while True:

    for peer in peers:
        try:
            print(f"{peer}: {peer.count_users()} at {time.time()}")
        except:
            print("Ops")

    time.sleep(frequency_in_minutes*60)