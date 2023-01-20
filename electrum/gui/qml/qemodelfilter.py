from PyQt5.QtCore import QSortFilterProxyModel

from electrum.logging import get_logger

class QEFilterProxyModel(QSortFilterProxyModel):
    _logger = get_logger(__name__)

    _filter_value = None

    def __init__(self, parent_model, parent=None):
        super().__init__(parent)
        self.setSourceModel(parent_model)

    def isCustomFilter(self):
        return self._filter_value is not None

    def setFilterValue(self, filter_value):
        self._filter_value = filter_value

    def filterAcceptsRow(self, s_row, s_parent):
        if not self.isCustomFilter:
            return super().filterAcceptsRow(s_row, s_parent)

        parent_model = self.sourceModel()
        d = parent_model.data(parent_model.index(s_row, 0, s_parent), self.filterRole())
        # self._logger.debug(f'DATA in FilterProxy is {repr(d)}')
        return True if self._filter_value is None else d == self._filter_value