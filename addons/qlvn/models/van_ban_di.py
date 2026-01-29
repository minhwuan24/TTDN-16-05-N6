from odoo import models, fields
from odoo.exceptions import UserError


class VanBanDi(models.Model):
    _name = 'qlvn.van_ban_di'
    _description = 'Văn bản đi'

    name = fields.Char(string="Tên văn bản", required=True)
    so_van_ban = fields.Char(string="Số văn bản")
    
    loai_van_ban_id = fields.Many2one(
        'qlvn.loai_van_ban',
        string="Loại văn bản",
        required=True
    )

    ngay_ban_hanh = fields.Date(string="Ngày ban hành")
    noi_nhan = fields.Char(string="Nơi nhận")

    nguoi_ky_id = fields.Many2one(
        'nhan_vien',
        string='Người ký',
        domain="[('chuc_vu_id.ten_chuc_vu', 'in', ['Giám đốc', 'Trưởng phòng', 'Phó giám đốc'])]"
    )  

    customer_id = fields.Many2one(
    'customer',
    string='Khách hàng',
    ondelete='set null'
    )

    file_dinh_kem = fields.Binary(string="File đính kèm")
    ten_file = fields.Char(string="Tên file")

    mo_ta = fields.Text(string="Mô tả")

    # ===== TRẠNG THÁI =====
    state = fields.Selection(
        [
            ('draft', 'Soạn thảo'),
            ('signed', 'Đã ký'),
            ('issued', 'Đã ban hành'),
            ('archived', 'Lưu trữ'),
        ],
        string="Trạng thái",
        default='draft'
    )

    active = fields.Boolean(default=True)

    # ===== ACTION =====
    def action_sign(self):
        for rec in self:
            if not rec.nguoi_ky_id:
                raise UserError("Vui lòng chọn người ký trước khi ký văn bản.")
        self.write({'state': 'signed'})

    def action_issue(self):
        self.write({'state': 'issued'})

    def action_archive(self):
        self.write({
            'state': 'archived',
            'active': False
        })
