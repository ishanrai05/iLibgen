import npyscreen as nps

from tools.Forms import BookDetail, SearchResultForm, SearchForm, MirrorLinks, DownloadForm


class App(nps.NPSAppManaged):

    # search = None
    def onStart(self):
        self.addFormClass('MAIN', SearchForm)
        self.addFormClass('SEARCH', SearchResultForm)
        self.registerForm('BOOK', BookDetail())
        self.addForm('MIRRORS', MirrorLinks)
        self.addFormClass('DOWNLOAD', DownloadForm)
        
                # self.NEXT_ACTIVE_FORM = None
    
    def onCleanExit(self):
        nps.notify_wait("Goodbye!")
        # self.addForm('EXIT', ExitForm)
    
    def change_form(self, name):
        # Switch forms.
        self.switchForm(name)
        
        # By default the application keeps track of every form visited.
        # There's no harm in this, but we don't need it so:        
        self.resetHistory()

if __name__ == '__main__':
    testApp = App().run()