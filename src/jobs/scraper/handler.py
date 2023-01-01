from aws_lambda_typing.context import Context
from aws_lambda_typing.events import CloudWatchEventsMessageEvent


def handler(event: CloudWatchEventsMessageEvent, context: Context):
    raise NotImplementedError()
