import hazelcast


def task3():
    hz = hazelcast.HazelcastClient(cluster_name="dev", cluster_members=[])

    try:
        map = hz.get_map("distributed-map").blocking()
        map.put_all({i: i for i in range(1, 1001)})
        print("Sent: from 1 to 1000")
    finally:
        hz.shutdown()

task3()

