""" Coding style

* CamelCase for classes
* snake_case for field names, arguments, resolvers (this will be automatically translated to camelCase by Graphene)

"""

import graphene

""" 
SCALAR TYPES
"""

int = graphene.ID()
float = graphene.Float()
boolean = graphene.Boolean()
string = graphene.String()
id = graphene.ID()
date_time = graphene.DateTime()


""" 
OBJECT TYPE
"""

class MyObject(graphene.ObjectType):
    # TODO: Declare your fields here
    # my_field = graphene.String(required=True, default='default value')
    pass


"""
ENUM TYPE
"""

class MyEnum(graphene.Enum):
    # TODO: Declare your set of values here
    # MEMBER_NAME = 'member value'
    pass


"""
Modifiers
"""

List = graphene.List(graphene.Int)
NonNull = graphene.NonNull(graphene.List)


"""
Resolver
"""

def resolve_lovelife(self, info):
    # TODO: Do your data fetching here
    pass


"""
Mutation
"""

class MyMutation(graphene.Mutation):
    class Arguments:
        # TODO: Declare your arguments here
        # my_argument = graphene.String(required=True, default='default value')
        pass

    # TODO: Declare your return fields here
    # created = graphene.Boolean()
    # person = graphene.Field(Person)

    def mutate(self, info):
        # TODO: Do your mutation magics here
        # person = Person(my_argument=my_argument)
        # return MyMutation(created=True, person=person)
        return MyMutation()


""" Mutation Example:
type Mutation {
    createPerson(name: String!, age: Int): Person
}
"""
