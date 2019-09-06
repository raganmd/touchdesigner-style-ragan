class PlatesChans:

    def __init__(self, myOp):
        self.Myop = myOp

    def Set_html(self, selectedRow):
        html_path = self.Myop.op('null_ref_data')[selectedRow, 'html_file']
        self.Myop.op('container_web').par.Url = html_path
        pass
    
    def Set_display(self, selectedRow):
        container_path = self.Myop.op('null_ref_data')[selectedRow, 'path']
        op.DisplayTarget.par.selectpanel = container_path
        pass
    
    def Update_ui(self, selectedRow):
        self.Set_html(selectedRow)
        self.Set_display(selectedRow)
        pass