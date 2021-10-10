import logging

from locators.videos_locators import VideoLocators as Locators

DF_LINK = "https://www.digitalfoundry.net/"

logger = logging.getLogger('scraping.videos_parser')


class VideoParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"{self.title}%{DF_LINK}{self.link}"

    @property
    def title(self):
        logger.debug('Finding title')
        locator = Locators.VIDEO_TITLE
        item_name = self.parent.select_one(locator).text
        logger.info(f'Found title name, `{item_name}`.')
        return item_name

    @property
    def link(self):
        logger.debug('Finding link')
        locator = Locators.VIDEO_LINK
        item_name = self.parent.select_one(locator).attrs["href"]
        logger.info(f'Found link, `{item_name}`.')
        return item_name
