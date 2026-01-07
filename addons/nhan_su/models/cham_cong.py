from odoo import models, fields, api


class ChamCong(models.Model):
    _name = 'cham_cong'
    _description = 'Chấm công'
    _rec_name = 'name'
    _order = 'nam desc, thang desc, id desc'

    name = fields.Char(string="Kỳ công", compute='_compute_name', store=True)

    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên", required=True, ondelete='cascade')

    thang = fields.Integer(string="Tháng", required=True)
    nam = fields.Integer(string="Năm", required=True)

    so_cong = fields.Float(string="Số công", required=True, default=0.0)

    # related để nhìn thấy ngay trên bản ghi chấm công
    luong_don_gia = fields.Float(string="Lương (đơn giá)", related='nhan_vien_id.luong', store=True, readonly=True)
    he_so_chuc_vu = fields.Float(string="Hệ số chức vụ", related='nhan_vien_id.chuc_vu_id.he_so', store=True, readonly=True)

    luong_thuc_nhan = fields.Float(string="Lương thực nhận", compute='_compute_luong_thuc_nhan', store=True)

    @api.depends('thang', 'nam')
    def _compute_name(self):
        for r in self:
            if r.thang and r.nam:
                r.name = f"{r.thang:02d}/{r.nam}"
            else:
                r.name = "Chấm công"

    @api.depends('so_cong', 'luong_don_gia', 'he_so_chuc_vu')
    def _compute_luong_thuc_nhan(self):
        for r in self:
            r.luong_thuc_nhan = (r.so_cong or 0.0) * (r.luong_don_gia or 0.0) * (r.he_so_chuc_vu or 0.0)

    _sql_constraints = [
        ('unique_ky_cong_nv', 'unique(nhan_vien_id, thang, nam)', 'Nhân viên đã có chấm công kỳ này!'),
    ]
