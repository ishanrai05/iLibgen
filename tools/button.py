import npyscreen as nps
import sys

from utils import Download


class ExitButton(nps.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchForm(None)
        nps.notify_wait("Goodbye!")
        sys.exit(0)

class SearchButton(nps.ButtonPress):   
    def whenPressed(self):
        # self.parent.parentApp.switchForm(None)
        nps.notify_wait("Searching ...")
        self.parent.parentApp.switchForm('MAIN')
        # pass

class SearchAgainButton(nps.ButtonPress):   
    def whenPressed(self):
        # self.parent.parentApp.switchForm(None)
        self.parent.parentApp.resetHistory()
        self.parent.parentApp.switchForm('MAIN')
        # pass

class GoBackToSearchButton(nps.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.resetHistory()
        self.parent.parentApp.switchForm('SEARCH')

class GetMirrorLinks(nps.ButtonPress):
    def whenPressed(self):
        # nps.notify_wait("Downloading")
        self.parent.parentApp.switchForm('MIRRORS')

class DownloadButton(nps.ButtonPress):
    def whenPressed(self):
        nps.notify_wait("Downloading")
        # with open('downloadLink.json', 'r') as fp:
        #     data = json.load(fp)
        Download.main()
        self.parent.parentApp.switchForm('DOWNLOAD')