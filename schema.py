from datetime import datetime

import graphene


# TODO: Define our Month object type here

""" Month object type

enum Month {
    JANUARY
    FEBRUARY
    AND_SO_ON
}

"""


class Months(graphene.Enum):
    JANUARY = 'January'
    FEBRUARY = 'February'
    MARCH = 'March'
    APRIL = 'April'
    MAY = 'May'
    JUNE = 'June'
    JULY = 'July'
    AUGUST = 'August'
    SEPTEMBER = 'September'
    OCTOBER = 'October'
    NOVEMBER = 'November'
    DECEMBER = 'December'


# TODO: Define our Vegetable object type here

""" Vegetable object type

type Vegetable {
    id: ID!
    name: String!
    pickingMonth: Month!    # A bit of a challenge!
    fee: Float!
    isOrganic: Boolean!    # Let's give a default value of False
}

"""


class Vegetable(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    picking_month = graphene.Field(Months, required=True)
    fee = graphene.Float(required=True)
    is_organic = graphene.Boolean(default_value=False)


# TODO: Define our BahayKubo object type here

""" Bahay Kubo object type

type BahayKubo {
    id: ID!
    name: String!
    owner: String
    address: String
    hasParking: boolean!    # Let's give a default value of False
    vegetables: [Vegetable!]!    # A bit of a challenge!
}

"""


class BahayKubo(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    owner = graphene.String()
    address = graphene.String()
    has_parking = graphene.Boolean(default_value=False)
    vegetables = graphene.List(graphene.NonNull(Vegetable), required=True)

    def resolve_vegetables(self, info):
        from data import get_vegetable

        return [get_vegetable(veg) for veg in self.vegetables]


# TODO: Define our FeedBack object type here

""" Feedback object type

type Feedback {
    id: ID!
    rate: Int!    # Let's give a default value of 0
    comment: String
    will_recommend: boolean!    # Let's give a default value of False
    created_at: DateTime!
}

"""

# TODO: Define our CreateFeedBack mutation here

""" CreateFeedback mutation

type Mutation {
    createFeedback(rate: Int!, comment: String, willRecommend: Boolean): Feedback
}

"""


class Query(graphene.ObjectType):
    hello = graphene.String()
    # TODO: Add something here
    bahay_kubo = graphene.Field(BahayKubo, id=graphene.NonNull(graphene.ID))

    def resolve_hello(self, info):
        return 'Mabuhay! Welcome to Netong\'s Bahay Kubo!'

    # TODO: Create resolver for something here
    def resolve_bahay_kubo(self, info, id):
        from data import get_bahay_kubo

        return get_bahay_kubo(id)


# TODO: Define our root type Mutation here and add it to our schema!


schema = graphene.Schema(query=Query)
