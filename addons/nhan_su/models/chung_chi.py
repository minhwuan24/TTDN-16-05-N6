from odoo import models, fields


class ChungChi(models.Model):
    _name = 'chung_chi'
    _description = 'Chứng chỉ'
    _order = 'ngay_cap desc, id desc'

    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên", required=True, ondelete='cascade')

    ten_chung_chi = fields.Char(string="Tên chứng chỉ", required=True)
    so_hieu = fields.Char(string="Số hiệu")
    don_vi_cap = fields.Char(string="Đơn vị cấp")
    ngay_cap = fields.Date(string="Ngày cấp")
    ngay_het_han = fields.Date(string="Ngày hết hạn")
    ghi_chu = fields.Text(string="Ghi chú")
