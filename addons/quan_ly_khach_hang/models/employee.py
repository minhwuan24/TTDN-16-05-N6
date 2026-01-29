from odoo import models, fields, api

class Employee(models.Model):
    _name = 'employee'
    _description = 'Bảng chứa thông tin nhân viên'

    # Các trường cơ bản
    employee_id = fields.Char("Mã nhân viên", required=True, index=True, copy=False)
    name = fields.Char("Tên nhân viên", required=True)
    email = fields.Char("Email")
    phone = fields.Char("Số điện thoại")
    address = fields.Char("Địa chỉ")
    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác')
    ], string="Giới tính")
    date_of_birth = fields.Date("Ngày sinh")
    job_title = fields.Char("Chức vụ")
    active = fields.Boolean("Active", default=True)

    # Trường liên kết với các model khác
    marketing_campaign_ids = fields.One2many('marketing_campaign', 'employee_id', string="Chiến dịch Marketing")
    note_ids = fields.One2many('note', 'employee_id', string="Ghi chú")
    project_task_ids = fields.One2many('project_task', 'employee_id', string="Nhiệm vụ dự án")
    crm_interact_ids = fields.One2many('crm_interact', 'employee_id', string="Tương tác khách hàng")

    # Tạo mã nhân viên tự động
    @api.model
    def create(self, vals):
        if vals.get('employee_id', 'New') == 'New':
            vals['employee_id'] = self.env['ir.sequence'].next_by_code('employee.sequence') or 'New'
        return super(Employee, self).create(vals)

    # Đặt tên hiển thị cho bản ghi
    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.employee_id}] {record.name}"
            result.append((record.id, name))
        return result