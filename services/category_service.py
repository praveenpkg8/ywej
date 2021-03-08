from models.category import Category


class CategoryService:

    @staticmethod
    def add_category(category):
        name = category.get('name')
        Category.create_category(name)

    @staticmethod
    def get_all_categories():
        ornaments = Category.get_all_category()
        data = []
        for ornament in ornaments:
            _category = dict(
                id=ornament.id,
                name=ornament.name,
            )
            data.append(_category)
        return data

    @staticmethod
    def update_category(category):
        Category.modify_ornament(
            _id=category.get('id'),
            name=category.get('name'),

        )

    @staticmethod
    def delete_category(_id):
        Category.delete_category(_id)

