class DosDontsUI:

    def __init__(self, myOp):
        self.Myop = myOp

    def Set_html(self, selectedRow):
        html_path = self.Myop.op('null_ref_data')[selectedRow, 'html_file']
        self.Myop.op('container_web').par.Url = html_path
        pass
    
    def Set_panes(self, selectedRow):
    
        selected_module     = self.Myop.op('null_ref_data')[selectedRow, 'path']
        do_pane             = '{}/base_do'.format(selected_module)
        dont_pane           = '{}/base_dont'.format(selected_module)

        td_do_pane          = ui.panes[1]
        td_dont_pane        = ui.panes[2]
        td_do_pane.owner    = op(do_pane)
        td_do_pane.home()
        
        td_dont_pane.owner  = op(dont_pane)
        td_dont_pane.home()
        pass