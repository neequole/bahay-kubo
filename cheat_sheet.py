""" Coding style

* CamelCase for classes
* snake_case for field names, arguments, resolvers (this will be automatically translated to camelCase by Graphene)

"""

import graphene

""" 
SCALAR TYPES
"""

Int = graphene.ID()
Float = graphene.Float()
Boolean = graphene.Boolean()
String = graphene.String()
ID = graphene.ID()
Datetime = graphene.DateTime()


""" 
OBJECT TYPE
"""

class MyObject(graphene.ObjectType):
    # TODO: Declare your fields here
    pass


"""
ENUM TYPE
"""

class MyEnum(graphene.Enum):
    # TODO: Declare your set of values here
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
        pass

    # TODO: Declare your return fields here

    def mutate(self, info):
        # TODO: Do your mutation magics here
        return MyMutation()


""" Mutation Example:
type Mutation {
    createPerson(name: String!, age: Int): Person
}
"""
