from data.crawling import Crawling
from console.console_writer import ConsoleWriter


class Application:
    def __init__(self):
        self.__running = True

    def run(self):
        if self.__running:
            crawling = Crawling()
            try:
                crawling.crawl()
                # db()
                # display()
            except:
                ConsoleWriter().print_error()
            finally:
                crawling.stop()


if __name__ == "__main__":
    Application().run()
