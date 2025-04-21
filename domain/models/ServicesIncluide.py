class ServiceIncluide:

    def __init__(self, reception, toilet,food,security,tecnology):
        self._reception = reception
        self._toilet = toilet
        self._food = food
        self._security = security
        self._tecnology = tecnology

    @property
    def reception(self):
        return self._reception

    @reception.setter
    def reception(self,reception):
        self._reception = reception

    @property
    def toilet(self):
        return self._toilet

    @toilet.setter
    def toilet(self, toilet):
        self._toilet = toilet

    @property
    def food(self):
        return self._food

    @food.setter
    def food(self, food):
        self._food = food

    @property
    def security(self):
        return self._security
    @security.setter
    def security(self,security):
        self._security = security

    @property
    def tecnology(self):
        return self._tecnology

    @tecnology.setter
    def tecnology(self,tecnology):
        self._tecnology = tecnology

