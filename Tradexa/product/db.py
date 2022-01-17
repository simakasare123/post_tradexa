class ProductRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'product':
            return 'product'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'product':
            return 'product'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label == 'product' and
            obj2._meta.app_label == 'product'):
           return True
        elif (obj1._meta.app_label != 'product' and
              obj2._meta.app_label != 'product'):
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        if db == 'product':
            return app_label == 'product'
        elif app_label == 'product':
            return db == 'product'

        return True