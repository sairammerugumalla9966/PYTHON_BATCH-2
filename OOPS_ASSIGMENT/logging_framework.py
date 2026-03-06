class FileLogger:
    def log(self, message):
        print(f"Writing to file: {message}")


class ConsoleLogger:
    def log(self, message):
        print(f"Printing to console: {message}")


def log_message(logger):
    logger.log("System started")


file_logger = FileLogger()
console_logger = ConsoleLogger()

log_message(file_logger)
log_message(console_logger)