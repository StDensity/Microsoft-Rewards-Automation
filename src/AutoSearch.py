import configparser


class AutoSearch:
    def __init__(self):
        self.total_searches = None
        self.search_delay = None
        self.inspect_element_delay = None
        self.browser_open_delay = None

        self.get_config_data()

    def get_config_data(self):
        config = configparser.ConfigParser()
        
        config.read('../config.ini')

        self.browser_open_delay = config.get('default_values', 'browser_open_delay')
        self.inspect_element_delay = config.get('default_values', 'inspect_element_delay')
        self.search_delay = config.get('default_values', 'search_delay')
        self.total_searches = config.get('default_values', 'total_searches')

    def start_search(self):
        pass

    def close_app(self):
        pass