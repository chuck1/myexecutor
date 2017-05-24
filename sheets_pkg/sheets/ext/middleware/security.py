
import sheets.middleware

class SecurityTest1(object):
    def call_book_globals(self, book, res):
        #print('called '+repr(self)+' call_book_globals g='+str(res._globals))
    
        self.MODULES_APPROVED = book.settings.MIDDLEWARE_SECURITY_MODULES_APPROVED
        self.BUILTINS_APPROVED = book.settings.MIDDLEWARE_SECURITY_BUILTINS_APPROVED
        
        res._globals['__builtins__'].update(
                dict((name, __builtins__[name]) for name in self.BUILTINS_APPROVED))

        res._globals['__builtins__']['__import__'] = self.builtin___import__
                 
        #"sheets": dict((k, s.cells_strings()) for k, s in self.sheets.items()),
         
        res._globals['book'] = book
  
    def builtin___import__(
            self, 
            name, 
            globals=None, 
            locals=None, 
            fromlist=(), 
            level=0):
        
        name_split = name.split('.')
        
        if not name_split[0] in self.MODULES_APPROVED:
            raise ImportError("module '{}' is not allowed".format(name_split[0]))

        return __import__(name, globals, locals, fromlist, level)

    def builtin_open(self, file, mode='r'):
        logger.warning("invoking Book.builtin_open({}, {})".format(file, mode))

        #file = open(file, mode)

        test_fs = fs.osfs.OSFS(os.path.join(os.environ['HOME'], 'web_sheets','filesystems','test'))
        file = test_fs.open(file, mode)

        return WrapperFile(file)

    def builtin_getattr(self, *args):
        logger.warning("invoking Book.builtin_getattr({})".format(args))
        obj = args[0]
        logger.warning("obj={}".format(obj))
        
        # temporarily removed for teting of special helper module importing
        """
        import sheets.helper
        if isinstance(obj, sheets.helper.CellsHelper):
            raise sheets.exception.NotAllowedError(
                    "For security, getattr not allowed for CellsHelper objects")
        """

        return getattr(*args)

    def call_book_method_decorator(self, book, f, args):
        pass
        
        #raise sheets.exception.NotAllowedError('stopped by protector')




