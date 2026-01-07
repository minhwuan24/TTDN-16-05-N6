from odoo import models, fields


class LoaiVanBan(models.Model):
    _name = 'qlvn.loai_van_ban'
    _description = 'Bảng chứa thông tin văn bản'
    _rec_name = 'ten_loai_van_ban'

    ma_loai_van_ban = fields.Char(string="Mã loại văn bản", required=True)
    ten_loai_van_ban = fields.Char(string="Tên loại văn bản", required=True)
    
    nhan_vien_id = fields.Many2one(
        'nhan_vien',          # _name của model nhân sự
        string='Nhân viên phụ trách'
    )
