class DosDontsUI:

    def __init__(self, myOp):
        self.Myop = myOp

    def Set_html(self, selectedRow):
        html_path = self.Myop.op('null_ref_data')[selectedRow + 1, 'html_file']
        self.Myop.op('container_web').par.Url = html_path
        pass