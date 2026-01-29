from odoo import models, fields, api

class Contract(models.Model):
    _name = 'contract'
    _description = 'Bảng chứa thông tin hợp đồng'

    contract_id = fields.Char("Mã hợp đồng", required=True)
    contract_name = fields.Char("Tên hợp đồng")
    customer_id = fields.Many2one('customer', string="Khách hàng", required=True, ondelete='cascade')
    nhan_vien_phu_trach_id = fields.Many2one(
        'nhan_vien',                 # ← MODEL TỪ MODULE NHÂN SỰ
        string="Nhân viên phụ trách"
    )
    start_date = fields.Date("Ngày bắt đầu hợp đồng", required=True)
    end_date = fields.Date("Ngày kết thúc hợp đồng", required=True)
    state = fields.Selection([
        ('active', 'Đang hoạt động'),
        ('ended', 'Đã kết thúc')
    ], string="Trạng thái hợp đồng", required=True)

    # Đặt tên hiển thị cho bản ghi
    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.contract_id}] {record.contract_name}"
            result.append((record.id, name))
        return result
