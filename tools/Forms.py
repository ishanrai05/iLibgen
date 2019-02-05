import npyscreen as nps
import json 
import warnings
warnings.filterwarnings("ignore")

from utils.vl import download_data, get_data
from tools.button import ExitButton, SearchButton, GoBackToSearchButton, SearchAgainButton, DownloadButton, GetMirrorLinks
from utils import getMirrors


class DownloadForm(nps.FormBaseNew):
    def create(self):
        self.add(ExitButton, name='Exit',relx=0, rely=0)

class SearchForm(nps.FormBaseNew):
    def create(self):
        # self.show_atx = 50
        # self.show_aty = 5
        self.search = self.add(SearchTitle, name='Search', begin_entry_at = 10)
        self.nextrely += 1
        self.button = self.add(SearchButton, name = 'Search!!')
        self.exitButton = self.add(ExitButton, name='Exit', relx=0, rely=0)
        self.add(nps.BoxBasic, name = "", relx=10, max_height=3)

    def afterEditing(self):
        # time.sleep(10)
        value = self.search.value
        download_data(value)
        self.parentApp.switchForm('SEARCH')
        # pass

    def change_forms(self, *args, **kwargs):
        self.parent.parentApp.change_form('SEARCH')

class MirrorLinks(nps.FormBaseNew):
    
    def create(self):
        
        self.add(ExitButton, name='Exit',relx=0, rely=0)
        self.add(DownloadButton, name='Download',relx=10, rely=0)
        try:
            with open('data/mirrors.json', 'r') as fp:
                data = json.load(fp)
            value_list = data
            for i in value_list:
                self.add(nps.TitleText, name=i, value=str(value_list[i]), editable=False, hidden=False)
        except Exception:
            pass

class BookDetail(nps.FormBaseNew):

    def create(self):
        pass

    def afterEditing(self):
        # self.parentApp.switchForm('BOOK')
        pass


        # self.parentApp.getForm('EXIT').search.value = self.search.value
        # self.exitButton = self.add(ExitButton, name='Exit', relx=-11, rely=-11)
        

class DisplaySearchResults(nps.AnnotateTextboxBase):
    ANNONATE_WIDTH = 20
    def getAnnontationAndColor(self):
        if self.value:
            return(self.value[0][0:self.ANNOTATE_WIDTH-2], self.annotation_color)
        else:
            return ''

    # def format_string(self, st):
    #     len1 = len(st[0])
    #     len2 = len(st[1])

    #     st1 = st[0] + ' '*(20-len1)
    #     st2 = st[1] + ' '*(10-len2)
    #     A = (st1, st2)
    #     return A

    def display_value(self, vl):
        a = ''
        # auth = vl['author']
        # id = vl['id']
        # st = (line, num)
        # st = self.format_string(st)
        a = f"""{vl['Title']} | {vl['Author']}"""
        return a

class ListBooks(nps.MultiLineAction):
    _contained_widgets = DisplaySearchResults
    _contained_widget_height = 2
    def display_value(self, vl):
        return (vl)
    
    def actionHighlighted(self, act_on_this, key_press):
        # self.parent.parentApp.getForm('BOOK').add(nps.TitleText, name='Title', value=act_on_this['Title'], editable=False, hidden=False)
        try:
            with open('data/downloadlink.json', 'w') as f:
                json.dump(act_on_this,f)
            for i in act_on_this:
                self.parent.parentApp.getForm('BOOK').add(nps.TitleText, name=i, value=str(act_on_this[i]), editable=False, hidden=False)
            
            self.parent.parentApp.getForm('DOWNLOAD').add(nps.TitleText, name='Download Link', value=str(act_on_this[i]), editable=False, hidden=False)
            self.parent.parentApp.getForm('DOWNLOAD').add(nps.DownloadButton, name='Download', relx=10, rely=0)
            
        except Exception:
            pass
        
        self.parent.parentApp.getForm('BOOK').add(ExitButton, name='Exit',relx=0, rely=0)
        self.parent.parentApp.getForm('BOOK').add(GoBackToSearchButton, name='Go Back',relx=10, rely=0)
        # self.parent.parentApp.getForm('BOOK').add(SearchAgainButton, name='Search Again',relx=23, rely=0)
        self.parent.parentApp.getForm('BOOK').add(GetMirrorLinks, name='Get Mirror Links',relx=42, rely=0)

        
        # value_list = (act_on_this)
        # with open('../data/data1.json', 'w') as fp:
        #     json.dump(value_list, fp)
        self.parent.parentApp.switchForm('BOOK')


class SearchResultForm(nps.FormBaseNew):
    def create(self):
        # self.show_atx = 50
        # self.title = self.add(nps.Textfield, name='Thank You', value="Form 2")
        vl = get_data()
        self.add(ListBooks,
                        values=vl, 
                        show_scroll=True,
                        use_two_lines=True)
        self.add(ExitButton, name='Exit',relx=0, rely=0)
        # self.add(SearchAgainButton, name='Search Again',relx=10, rely=0)
        
    # def afterEditing(self):
    #     self.parentApp.switchForm('BOOK')


class SearchTitle(nps.TitleText):
    def funcname(self, parameter_list):
        pass

