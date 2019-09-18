import coreapi
import coreschema
from rest_framework.schemas import AutoSchema


class DonationsSchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'GET':
            return 'Информация по запросу'
        if method == 'POST':
            return 'Создание запроса'
        return None

    def get_encoding(self, path, method):
        return 'application/json'

    def get_serializer_fields(self, path, method):
        fields = []
        if method == 'POST':
            fields = [
                coreapi.Field(
                    name='name',
                    required=False,
                    location="form",
                    schema=coreschema.String(title='name',
                                             default=None,
                                             description='name'),
                    description='name'
                ),
                coreapi.Field(
                    name='source',
                    required=True,
                    location="form",
                    schema=coreschema.String(title='source',
                                             default=None,
                                             description='source'),
                    description='source'
                ),
                coreapi.Field(
                    name='details',
                    required=True,
                    location="form",
                    schema=coreschema.String(title='details',
                                             default=None,
                                             description='details'),
                    description='details'
                ),
                coreapi.Field(
                    name='summ',
                    required=True,
                    location="form",
                    schema=coreschema.Integer(title='summ',
                                             default=None,
                                             description='summ'),
                    description='summ'
                ),
            ]
        return fields


class EventSchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'GET':
            return 'Информация по запросу'
        if method == 'POST':
            return 'Создание запроса'
        return None

    def get_encoding(self, path, method):
        return 'application/json'

    def get_serializer_fields(self, path, method):
        fields = []
        if method == 'POST':
            fields = [
                coreapi.Field(
                    name='target',
                    required=False,
                    location="form",
                    schema=coreschema.Integer(title='target',
                                             default=None,
                                             description='target'),
                    description='target'
                ),
            ]
        return fields