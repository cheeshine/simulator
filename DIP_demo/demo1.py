import abc

class CriticalFeature:
    def __init__(self):
        self._step1 = None
        self._step2 = None

    def run(self):
        # 执行第一步
        self._step1.execute()
        # 执行第二步
        self._step2.execute()


class MessageSender(abc.ABC):
    def send(self, message: Message):
        ...


class KafkaProducer(MessageSender):




class Handler:
    def __init__(self):
        self._producer: KafkaProducer = None

    def execute(self):
        ...
        message: Message = ...
        self._producer.send()
