# -*- encoding: utf-8 -*-

from models.auth import Role

class BaseSeeder:

    db_session = None
    entity_class = None
    delete = None

    def __init__(self, db_session, entity_class, delete=True):
        self.db_session = db_session
        self.entity_class = entity_class
        self.delete = delete

    def seed(self, new_entities):

        if self.delete:
            self.entity_class.query.delete()

        for new_entity in new_entities:

            print 'Creating new {}'.format(self.entity_class.__name__)
            print unicode(new_entity)

            mapped_columns = [column for column in new_entity.__dict__ if column[:4] != '_sa_']

            for mapped_column in mapped_columns:
                column_value = getattr(new_entity, mapped_column)

                if hasattr(column_value, '__iter__'):

                    new_relation = []
                    for related_object in column_value:

                        print 'Related object <{}>'.format(related_object.__class__.__name__)
                        if related_object.id is None:

                            columns_with_value = [
                                (col, getattr(related_object, col)) \
                                for col in related_object.__dict__ \
                                if col[:4] != '_sa_' \
                                    and not hasattr(getattr(related_object, col),'__iter__') \
                                    and getattr(related_object, col) is not None
                            ]

                            related_object_class = related_object.__class__
                            filter = dict(columns_with_value)
                            print filter
                            obj = related_object_class.query.filter_by(**filter).first()
                            print 'Found object: {}'.format(unicode(obj))
                            new_relation.append(obj or related_object)

                    setattr(new_entity, mapped_column, new_relation)

                else:
                    if hasattr(column_value, '__dict__'):
                        columns_with_value = [
                            (col, getattr(column_value, col)) \
                            for col in column_value.__dict__ \
                            if col[:4] != '_sa_' \
                                and not hasattr(getattr(column_value, col),'__iter__') \
                                and getattr(column_value, col) is not None
                        ]
                        related_object_class = column_value.__class__
                        filter = dict(columns_with_value)
                        print filter
                        obj = related_object_class.query.filter_by(**filter).first()
                        print 'Found object: {}'.format(unicode(obj))

                        setattr(new_entity, mapped_column, obj)

            if hasattr(new_entity, 'round'):
                print 'round'
                print new_entity.round.tournament_id

            self.db_session.add(new_entity)
            self.db_session.commit()
            print


