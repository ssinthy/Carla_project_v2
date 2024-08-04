# import requests

from operating_conditions import OpCondImply, OpCondRange, OpCondSet, OpCondAnd, OpCondOr, init_opcond_from_json
from odd import OperationalDesignDomain, Taxonomy

INFINITY = 1000000000
odd = OperationalDesignDomain()

# def get_data_from_api(id):
#     response = requests.get(f"http://127.0.0.1:5000/api/odd/{id}")
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Failed to get data. Status code: {response.status_code}")
#         return None

# Instances of OpCondSet, OpCondRange, OpCondImply, etc., are created to represent specific conditions.

odd.add_in_operating_condition(OpCondSet(taxonomies=[Taxonomy.RAIN], 
                                         boundset=["light", "moderate"]))

# odd.add_out_operating_condition(OpCondSet(taxonomies=[Taxonomy.RAIN], 
                                        #   boundset=["heavy", "violent", "burst"]))

odd.add_in_operating_condition(OpCondSet(taxonomies=[Taxonomy.TIME_OF_DAY], 
                                         boundset=["day", "evening"]))

# odd.add_out_operating_condition(OpCondSet(taxonomies=[Taxonomy.TIME_OF_DAY], 
#                                           boundset=["night"]))

# In collector road, EGO must have speed 5-60
odd.add_in_operating_condition(OpCondImply(opcond_if=OpCondSet(taxonomies=[Taxonomy.EGO_VEHICLE, Taxonomy.ROADTYPE], 
                                                              boundset=["collector"]),
                                         opcond_then=OpCondRange(taxonomies=[Taxonomy.EGO_VEHICLE, Taxonomy.SPEED], 
                                                                 min=5.0, 
                                                                 max=60.0)))

# In motorway, EGO must have speed 5-70
odd.add_in_operating_condition(OpCondImply(opcond_if=OpCondSet(taxonomies=[Taxonomy.EGO_VEHICLE, Taxonomy.ROADTYPE], 
                                                              boundset=["motorway"]),
                                         opcond_then=OpCondRange(taxonomies=[Taxonomy.EGO_VEHICLE, Taxonomy.SPEED], 
                                                                 min=5.0, 
                                                                 max=70.0)))

# EMV on motoway must maintain a safe distance of 50m
# EMV has different safe distance based on the speed
odd.add_in_operating_condition(OpCondImply(opcond_if=OpCondAnd(
                                                        opconds=[
                                                            OpCondSet(taxonomies=[Taxonomy.EGO_VEHICLE, Taxonomy.ROADTYPE], boundset=["motorway"]),
                                                            OpCondSet(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.ROADTYPE], boundset=["motorway"]),
                                                        ]),
                                           opcond_then=OpCondAnd(
                                                        opconds=[
                                                            OpCondRange(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.DISTANCE], min=50, max=INFINITY),
                                                            OpCondRange(taxonomies=[Taxonomy.EGO_VEHICLE, Taxonomy.SPEED], min=0.0, max=70.0),
                                                            OpCondRange(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.SPEED], min=0.5, max=INFINITY)
                                                        ])))

# EMV on motoway must maintain a safe distance of 50m
odd.add_in_operating_condition(OpCondImply(opcond_if=OpCondAnd(
                                                        opconds=[
                                                            OpCondSet(taxonomies=[Taxonomy.EGO_VEHICLE, Taxonomy.ROADTYPE], boundset=["motorway"]),
                                                            OpCondSet(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.ROADTYPE], boundset=["motorway"]),
                                                            OpCondSet(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.RELATIVE_POSITION], boundset=["subject_lane"]),
                                                        ]),
                                           opcond_then=OpCondAnd(
                                                        opconds=[
                                                            OpCondRange(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.DISTANCE], min=4, max=INFINITY),
                                                            OpCondRange(taxonomies=[Taxonomy.EGO_VEHICLE, Taxonomy.SPEED], min=0.0, max=70.0),
                                                            OpCondRange(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.SPEED], min=0.0, max=0.0)
                                                        ])))


# EMV on motoway must maintain a safe distance of 50m
odd.add_in_operating_condition(OpCondOr(opconds=[OpCondImply(opcond_if=OpCondAnd(
                                                                opconds=[
                                                                    OpCondSet(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.RELATIVE_POSITION], boundset=["subject_lane"]),
                                                                ]),
                                                            opcond_then=OpCondAnd(
                                                                opconds=[
                                                                    OpCondRange(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.DISTANCE], min=50, max=INFINITY),
                                                                    OpCondRange(taxonomies=[Taxonomy.EGO_VEHICLE, Taxonomy.SPEED], min=0.0, max=70.0),
                                                                    OpCondRange(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.SPEED], min=1.0, max=INFINITY)
                                                                ])),
                                                OpCondImply(opcond_if=OpCondAnd(
                                                                opconds=[
                                                                    OpCondSet(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.RELATIVE_POSITION], boundset=["opposite_lane"]),
                                                                ]),
                                                                opcond_then=OpCondAnd(
                                                                opconds=[
                                                                    OpCondRange(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.DISTANCE], min=20, max=INFINITY),
                                                                    OpCondRange(taxonomies=[Taxonomy.EGO_VEHICLE, Taxonomy.SPEED], min=0.0, max=70.0),
                                                                    OpCondRange(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.SPEED], min=1.0, max=INFINITY)
                                                                ])),
                                                OpCondImply(opcond_if=OpCondAnd(
                                                                opconds=[
                                                                    OpCondSet(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.RELATIVE_POSITION], boundset=["subject_lane"]),
                                                                    OpCondRange(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.SPEED], min=0.0, max=0.0)
                                                                ]),
                                                                opcond_then=OpCondAnd(
                                                                opconds=[
                                                                    OpCondRange(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.DISTANCE], min=10, max=INFINITY),
                                                                    OpCondRange(taxonomies=[Taxonomy.EGO_VEHICLE, Taxonomy.SPEED], min=0.0, max=70.0)
                                                                ])),
                                                OpCondImply(opcond_if=OpCondAnd(
                                                                opconds=[
                                                                    OpCondSet(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.RELATIVE_POSITION], boundset=["opposite_lane"]),
                                                                    OpCondRange(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.SPEED], min=0.0, max=0.0)
                                                                ]),
                                                                opcond_then=OpCondAnd(
                                                                opconds=[
                                                                    OpCondRange(taxonomies=[Taxonomy.EMERGENCY_VEHICLE, Taxonomy.DISTANCE], min=3, max=INFINITY),
                                                                    OpCondRange(taxonomies=[Taxonomy.EGO_VEHICLE, Taxonomy.SPEED], min=0.0, max=70.0)
                                                                ]))
                                                ]))


avdata = {
    Taxonomy.RAIN: "light",
    Taxonomy.TIME_OF_DAY: "day",

    Taxonomy.EGO_VEHICLE: {
        Taxonomy.ROADTYPE: "motorway",
        Taxonomy.SPEED: 30.0,
    },
    Taxonomy.EMERGENCY_VEHICLE: {
        Taxonomy.SPEED: 10.0,
        Taxonomy.ROADTYPE: "motorway",
        Taxonomy.DISTANCE: 51
    }
}

# data = get_data_from_api("667d781827704e647964a282")
# if data:
#     init_opcond_from_json(data)

is_within_odd = odd.check_within_odd(avdata)
if is_within_odd:
    print("Within ODD")
else:
    print("Out of ODD")