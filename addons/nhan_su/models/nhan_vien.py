from odoo import models, fields, api


class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'
    _rec_name = 'ho_ten'
    _order = 'ngay_sinh asc'

    ma_dinh_danh = fields.Char(string="Mã định danh", required=True)
    ho_ten = fields.Char(string="Họ và tên", required=True)
    ngay_sinh = fields.Date(string="Ngày sinh")
    que_quan = fields.Char(string="Quê quán")
    dia_chi = fields.Char(string="Địa chỉ")

    email = fields.Char(string="Email")
    so_dien_thoai = fields.Char(string="Số điện thoại")

    so_bhxh = fields.Char(string="Số BHXH")
    luong = fields.Float(string="Lương (đơn giá)", help="Lương/đơn giá tính theo công")

    phong_ban_ids = fields.Many2many(
        comodel_name='phong_ban', string='Phòng ban'
    )

    chuc_vu_id = fields.Many2one(
        comodel_name='chuc_vu', string='Chức vụ'
    )

    lich_su_cong_tac_ids = fields.One2many(
        comodel_name='lich_su_cong_tac', inverse_name='nhan_vien_id',
        string='Lịch sử công tác'
    )

    chung_chi_ids = fields.One2many(
        comodel_name='chung_chi', inverse_name='nhan_vien_id',
        string='Chứng chỉ'
    )

    cham_cong_ids = fields.One2many(
        comodel_name='cham_cong', inverse_name='nhan_vien_id',
        string='Chấm công'
    )

    _sql_constraints = [
        ('ma_dinh_danh_unique', 'unique(ma_dinh_danh)', 'Mã định danh đã tồn tại!'),
    ]
