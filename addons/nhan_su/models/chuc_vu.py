from odoo import models, fields


class ChucVu(models.Model):
    _name = 'chuc_vu'
    _description = 'Bảng chức vụ'
    _rec_name = 'ten_chuc_vu'

    ma_chuc_vu = fields.Char(string="Mã chức vụ", required=True)
    ten_chuc_vu = fields.Char(string="Tên chức vụ", required=True)
    he_so = fields.Float(string="Hệ số", required=True, default=1.0)

    mo_ta = fields.Text(string="Mô tả")

    _sql_constraints = [
        ('ma_chuc_vu_unique', 'unique(ma_chuc_vu)', 'Mã chức vụ đã tồn tại!'),
    ]
