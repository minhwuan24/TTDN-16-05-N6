from odoo import models, fields, api


class PhongBan(models.Model):
    _name = 'phong_ban'
    _description = 'Bảng phòng ban'
    _rec_name = 'ten_phong'

    ten_phong = fields.Char("Tên phòng ban", required=True)
    ma_phong = fields.Char("Mã phòng ban", required=True)
    mo_ta = fields.Text("Mô tả phòng ban")

    nhan_vien_id = fields.Many2many(
        comodel_name='nhan_vien', string ='Nhân viên')