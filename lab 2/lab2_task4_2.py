import hazelcast


def message_listener(event):
    print("The message "+str(event)+" received!")


def task4_2():
    hz = hazelcast.HazelcastClient(cluster_name="dev", cluster_members=[])
    try:
        topic = hz.get_topic("my-distributed-topic")
        listener = topic.add_listener(message_listener)
        input("Press Enter to exit...\n")
        topic.remove_listener(listener)
    finally:
        hz.shutdown()

task4_2()

