from models.ornament import Ornament


class OrnamentService:

    @staticmethod
    def create_ornament(params):
        name = params.get('name')
        weight = params.get('weight')
        wastage = params.get('wastage')
        making_charge = params.get('making_charge')
        category_id = params.get('category_id')
        Ornament.add_stock(
            name=name,
            weight=weight,
            wastage=wastage,
            making_charge=making_charge,
            category_id=category_id
        )

    @staticmethod
    def get_all_ornaments():
        ornaments = Ornament.get_all_ornaments()
        data = []
        for ornament in ornaments:
            final_note = dict(
                id=ornament.id,
                name=ornament.name,
                weight=ornament.weight,
                wastage=ornament.wastage,
                making_charge=ornament.making_charge
            )
            data.append(final_note)
        return data

    @staticmethod
    def update_ornaments(ornament):
        Ornament.modify_ornament(
            _id=ornament.get('id'),
            name=ornament.get('name'),
            weight=ornament.get('weight'),
            wastage=ornament.get('wastage'),
            making_charge=ornament.get('making_charge'),

        )

    @staticmethod
    def delete_ornament(_id):
        Ornament.delete_ornament(_id)
