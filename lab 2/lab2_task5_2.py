import hazelcast


def task5_2():
    hz = hazelcast.HazelcastClient(cluster_name="dev",cluster_members=[])
    try:
        queue = hz.get_queue("bounded-queue").blocking()
        while True:
            item = queue.take()
            print("The message "+str(item)+" received!")
    finally:
        hz.shutdown()

task5_2()

