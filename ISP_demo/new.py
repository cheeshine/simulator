import abc
import typing as t


class TransactionRequest(abc.ABC):
    def get_type(self) -> str:
        ...


class DepositRequest(TransactionRequest, abc.ABC):
    @abc.abstractmethod
    def get_deposit_amount(self) -> float:
        ...


class WithdrawRequest(TransactionRequest, abc.ABC):
    @abc.abstractmethod
    def get_withdraw_amount(self) -> float:
        ...


class TransferRequest(TransactionRequest, abc.ABC):
    @abc.abstractmethod
    def get_transfer_amount(self) -> float:
        ...


class LivingPaymentRequest(TransactionRequest, abc.ABC):
    @abc.abstractmethod
    def get_living_payment_amount(self) -> float:
        ...


class ActualTransactionRequest(DepositRequest, WithdrawRequest, TransferRequest, LivingPaymentRequest):
    def get_type(self) -> str:
        ...

    def get_deposit_amount(self) -> float:
        ...

    def get_withdraw_amount(self) -> float:
        ...

    def get_transfer_amount(self) -> float:
        ...

    def get_living_payment_amount(self) -> float:
        ...


class TransactionHandler(abc.ABC):
    @abc.abstractmethod
    def handle(self, request: TransactionRequest):
        ...


class DepositHandler(TransactionHandler):
    def handle(self, request: DepositRequest):
        amount: float = request.get_deposit_amount()
        ...


class WithdrawHandler(TransactionHandler):
    def handle(self, request: WithdrawRequest):
        amount: float = request.get_withdraw_amount()
        ...


class TransferHandler(TransactionHandler):
    def handle(self, request: TransferRequest):
        amount: float = request.get_transfer_amount()
        ...


class LivingPaymentHandler(TransactionHandler):
    def handle(self, request: LivingPaymentRequest):
        amount: float = request.get_living_payment_amount()
        ...


def main():
    handlers: t.Dict[str, TransactionHandler] = {}
    request: ActualTransactionRequest = ActualTransactionRequest()
    # 业务分发
    handler: TransactionHandler = handlers.get(request.get_type())
    if handler is not None:
        handler.handle(request)


if __name__ == '__main__':
    main()
