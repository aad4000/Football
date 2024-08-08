from marshmallow import Schema, fields, validate, ValidationError

class PlayerSchema(Schema):
    first_name = fields.Str(required=True, validate=validate.Length(min=1))
    last_name = fields.Str(required=True, validate=validate.Length(min=1))
    apt = fields.Int(required=True, validate=validate.Range(min=0))
    set = fields.Int(required=True, validate=validate.Range(min=0))
    position = fields.Str(required=True, validate=validate.OneOf(['defender', 'midfielder', 'attacker']))
    national_association = fields.Str(required=True, validate=validate.OneOf(['England', 'Northern Ireland', 'Scotland', 'Wales']))

# Function to validate player data
def validate_player_data(data):
    schema = PlayerSchema()
    try:
        result = schema.load(data)
        return True, result
    except ValidationError as err:
        return False, err.messages
