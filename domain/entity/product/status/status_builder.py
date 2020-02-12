from domain.entity.product.status.economic_status import EconomicStatus
from domain.entity.product.status.regular_status import RegularStatus
from domain.entity.product.status.responsible_status import ResponsibleStatus


class StatusBuilder:
    def build_list_product_status(self):
        return [
            EconomicStatus(),
            RegularStatus(),
            ResponsibleStatus()
        ]
