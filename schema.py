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

    def resolve_hello(self, info):
        return 'Mabuhay! Welcome to Netong\'s Bahay Kubo!'

    # TODO: Create resolver for something here


# TODO: Define our root type Mutation here and add it to our schema!


schema = graphene.Schema(query=Query)
