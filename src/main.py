# import asyncio
from kafka_producer_manager import KafkaProducerManager
from kafka_consumer_manager import KafkaConsumerManager

topic = "topic_py_azdo_tmp_0"
producer = KafkaProducerManager(topic).init()
payload = "{'id': 1}"

consumer_group_id = "py_azdo_tmp_0"
consumer = KafkaConsumerManager(topic, consumer_group_id).init().subscribe()

# if __name__ == "__main__":
#     producer.produce("id", payload)
#     producer.flush()

#     consumer.manage()


# async def main():
#     result = await ...
#     print("", result.text)

# asyncio.run(main())
