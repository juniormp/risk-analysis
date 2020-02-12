from domain.entity.product.status.economic_status import EconomicStatus
from domain.entity.product.status.regular_status import RegularStatus
from domain.entity.product.status.responsible_status import ResponsibleStatus


class ProductStatusBuilder:
    def build_product_status_list(self):
        return [
            EconomicStatus(),
            RegularStatus(),
            ResponsibleStatus()
        ]
