import hazelcast
import time


def task5_1():
    hz = hazelcast.HazelcastClient(cluster_name="dev",cluster_members=[])
    try:
        queue = hz.get_queue("bounded-queue")
        for i in range(1, 101):
            queue.put(i)
            print("The message "+str(i)+" sent!")
            time.sleep(0.01)
    finally:
        hz.shutdown()

task5_1()

