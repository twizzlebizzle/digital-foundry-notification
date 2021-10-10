import logging

from bs4 import BeautifulSoup
from parsers.videos import VideoParser
from locators.all_videos_page import AllVideosLocators as Locators

logger = logging.getLogger('scraping.all_videos_page')


class AllVideoPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")

    @property
    def videos(self):
        logger.debug("Finding all video links in the page using '" + Locators.VIDEO_LIST + "'")
        return [VideoParser(e) for e in self.soup.select(Locators.VIDEO_LIST)]
