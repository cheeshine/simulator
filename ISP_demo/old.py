import abc
import typing as t


class TransactionRequest(object):
    def get_type(self) -> str:
        ...

    def get_deposit_amount(self) -> float:
        ...

    def get_withdraw_amount(self) -> float:
        ...

    def get_transfer_amount(self) -> float:
        ...


class TransactionHandler(abc.ABCMeta):
    @abc.abstractmethod
    def handle(cls, request: TransactionRequest):
        ...


class DepositHandler(TransactionHandler):
    def handle(cls, request: TransactionRequest):
        amount: float = request.get_deposit_amount()
        ...


class WithdrawHandler(TransactionHandler):
    def handle(cls, request: TransactionRequest):
        amount: float = request.get_withdraw_amount()
        ...


class TransferHandler(TransactionHandler):
    def handle(cls, request: TransactionRequest):
        amount: float = request.get_transfer_amount()
        ...


def main():
    handlers: t.Dict[str, TransactionHandler] = {}
    request: TransactionRequest = TransactionRequest()
    # 业务分发
    handler: TransactionHandler = handlers.get(request.get_type())
    if handler is not None:
        handler.handle(request)


if __name__ == '__main__':
    main()
