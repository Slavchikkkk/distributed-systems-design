import hazelcast
import time


def task4_1():
    hz = hazelcast.HazelcastClient(cluster_name="dev", cluster_members=[])
    try:
        topic = hz.get_topic("my-distributed-topic")
        for i in range(1, 101):
            topic.publish(i)
            print("The message " + str(i) + " sent!")
            time.sleep(0.01)
    finally:
        hz.shutdown()

task4_1()

