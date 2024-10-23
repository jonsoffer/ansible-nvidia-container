from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display
from aptsources.sourceslist import SourceEntry, SourcesList

class LookupModule(LookupBase):
    def run(self, terms, Variables=None, **kwargs):
        ...
