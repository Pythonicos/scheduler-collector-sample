def handler(f):
    def wrapper(*args, **kwargs):
        if args[1].status_code == 200:
            return f(*args, **kwargs)
        else:
            return "Content offline"

    return wrapper


class ParserList:

    class GoogleParser:
        @handler
        def parse(self, response):
            return "Google", "Google content"

    class UolParser:
        @handler
        def parse(self, response):
            return "Uol", "Uol content"


def get_parser(parser_name):
    target_class = getattr(ParserList, "{}Parser".format(parser_name))
    return target_class()
