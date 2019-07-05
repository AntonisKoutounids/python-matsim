# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Event(google___protobuf___message___Message):

    @property
    def actEnd(self) -> ActivityEndEvent: ...

    @property
    def actStart(self) -> ActivityStartEvent: ...

    @property
    def linkEnter(self) -> LinkEnterEvent: ...

    @property
    def linkLeave(self) -> LinkLeaveEvent: ...

    @property
    def personArrival(self) -> PersonArrivalEvent: ...

    @property
    def personDeparture(self) -> PersonDepartureEvent: ...

    @property
    def personEntersVehicle(self) -> PersonEntersVehicleEvent: ...

    @property
    def personLeavesVehicle(self) -> PersonLeavesVehicleEvent: ...

    @property
    def personMoney(self) -> PersonMoneyEvent: ...

    @property
    def personStuck(self) -> PersonStuckEvent: ...

    @property
    def transitDriverStarts(self) -> TransitDriverStartsEvent: ...

    @property
    def vehicleAborts(self) -> VehicleAbortsEvent: ...

    @property
    def vehicleEntersTraffic(self) -> VehicleEntersTrafficEvent: ...

    @property
    def vehicleLeavesTraffic(self) -> VehicleLeavesTrafficEvent: ...

    @property
    def genericEvent(self) -> GenericEvent: ...

    def __init__(self,
        actEnd : typing___Optional[ActivityEndEvent] = None,
        actStart : typing___Optional[ActivityStartEvent] = None,
        linkEnter : typing___Optional[LinkEnterEvent] = None,
        linkLeave : typing___Optional[LinkLeaveEvent] = None,
        personArrival : typing___Optional[PersonArrivalEvent] = None,
        personDeparture : typing___Optional[PersonDepartureEvent] = None,
        personEntersVehicle : typing___Optional[PersonEntersVehicleEvent] = None,
        personLeavesVehicle : typing___Optional[PersonLeavesVehicleEvent] = None,
        personMoney : typing___Optional[PersonMoneyEvent] = None,
        personStuck : typing___Optional[PersonStuckEvent] = None,
        transitDriverStarts : typing___Optional[TransitDriverStartsEvent] = None,
        vehicleAborts : typing___Optional[VehicleAbortsEvent] = None,
        vehicleEntersTraffic : typing___Optional[VehicleEntersTrafficEvent] = None,
        vehicleLeavesTraffic : typing___Optional[VehicleLeavesTrafficEvent] = None,
        genericEvent : typing___Optional[GenericEvent] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Event: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"actEnd",u"actStart",u"event_type",u"genericEvent",u"linkEnter",u"linkLeave",u"personArrival",u"personDeparture",u"personEntersVehicle",u"personLeavesVehicle",u"personMoney",u"personStuck",u"transitDriverStarts",u"vehicleAborts",u"vehicleEntersTraffic",u"vehicleLeavesTraffic"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"actEnd",u"actStart",u"event_type",u"genericEvent",u"linkEnter",u"linkLeave",u"personArrival",u"personDeparture",u"personEntersVehicle",u"personLeavesVehicle",u"personMoney",u"personStuck",u"transitDriverStarts",u"vehicleAborts",u"vehicleEntersTraffic",u"vehicleLeavesTraffic"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"actEnd",b"actEnd",u"actStart",b"actStart",u"event_type",b"event_type",u"genericEvent",b"genericEvent",u"linkEnter",b"linkEnter",u"linkLeave",b"linkLeave",u"personArrival",b"personArrival",u"personDeparture",b"personDeparture",u"personEntersVehicle",b"personEntersVehicle",u"personLeavesVehicle",b"personLeavesVehicle",u"personMoney",b"personMoney",u"personStuck",b"personStuck",u"transitDriverStarts",b"transitDriverStarts",u"vehicleAborts",b"vehicleAborts",u"vehicleEntersTraffic",b"vehicleEntersTraffic",u"vehicleLeavesTraffic",b"vehicleLeavesTraffic"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"actEnd",b"actStart",b"event_type",b"genericEvent",b"linkEnter",b"linkLeave",b"personArrival",b"personDeparture",b"personEntersVehicle",b"personLeavesVehicle",b"personMoney",b"personStuck",b"transitDriverStarts",b"vehicleAborts",b"vehicleEntersTraffic",b"vehicleLeavesTraffic"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"event_type",b"event_type"]) -> typing_extensions___Literal["actEnd","actStart","linkEnter","linkLeave","personArrival","personDeparture","personEntersVehicle","personLeavesVehicle","personMoney","personStuck","transitDriverStarts","vehicleAborts","vehicleEntersTraffic","vehicleLeavesTraffic","genericEvent"]: ...

class GenericEvent(google___protobuf___message___Message):
    type = ... # type: typing___Text
    time = ... # type: float

    @property
    def attrVal(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[AttrVal]: ...

    def __init__(self,
        type : typing___Optional[typing___Text] = None,
        time : typing___Optional[float] = None,
        attrVal : typing___Optional[typing___Iterable[AttrVal]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GenericEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"attrVal",u"time",u"type"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"attrVal",b"time",b"type"]) -> None: ...

class AttrVal(google___protobuf___message___Message):
    attribut = ... # type: typing___Text
    value = ... # type: typing___Text

    def __init__(self,
        attribut : typing___Optional[typing___Text] = None,
        value : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AttrVal: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"attribut",u"value"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"attribut",b"value"]) -> None: ...

class ActivityEndEvent(google___protobuf___message___Message):
    time = ... # type: float
    actType = ... # type: typing___Text

    @property
    def linkId(self) -> LinkId: ...

    @property
    def facilityId(self) -> ActivityFacilityId: ...

    @property
    def persId(self) -> PersonId: ...

    def __init__(self,
        time : typing___Optional[float] = None,
        linkId : typing___Optional[LinkId] = None,
        facilityId : typing___Optional[ActivityFacilityId] = None,
        persId : typing___Optional[PersonId] = None,
        actType : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ActivityEndEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"facilityId",u"linkId",u"persId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"actType",u"facilityId",u"linkId",u"persId",u"time"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"facilityId",b"facilityId",u"linkId",b"linkId",u"persId",b"persId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"actType",b"facilityId",b"linkId",b"persId",b"time"]) -> None: ...

class ActivityStartEvent(google___protobuf___message___Message):
    time = ... # type: float
    actType = ... # type: typing___Text

    @property
    def linkId(self) -> LinkId: ...

    @property
    def facilityId(self) -> ActivityFacilityId: ...

    @property
    def persId(self) -> PersonId: ...

    def __init__(self,
        time : typing___Optional[float] = None,
        linkId : typing___Optional[LinkId] = None,
        facilityId : typing___Optional[ActivityFacilityId] = None,
        persId : typing___Optional[PersonId] = None,
        actType : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ActivityStartEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"facilityId",u"linkId",u"persId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"actType",u"facilityId",u"linkId",u"persId",u"time"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"facilityId",b"facilityId",u"linkId",b"linkId",u"persId",b"persId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"actType",b"facilityId",b"linkId",b"persId",b"time"]) -> None: ...

class LinkEnterEvent(google___protobuf___message___Message):
    time = ... # type: float

    @property
    def linkId(self) -> LinkId: ...

    @property
    def vehId(self) -> VehicleId: ...

    def __init__(self,
        time : typing___Optional[float] = None,
        linkId : typing___Optional[LinkId] = None,
        vehId : typing___Optional[VehicleId] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LinkEnterEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"linkId",u"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"linkId",u"time",u"vehId"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"linkId",b"linkId",u"vehId",b"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"linkId",b"time",b"vehId"]) -> None: ...

class LinkLeaveEvent(google___protobuf___message___Message):
    time = ... # type: float

    @property
    def linkId(self) -> LinkId: ...

    @property
    def vehId(self) -> VehicleId: ...

    def __init__(self,
        time : typing___Optional[float] = None,
        linkId : typing___Optional[LinkId] = None,
        vehId : typing___Optional[VehicleId] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LinkLeaveEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"linkId",u"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"linkId",u"time",u"vehId"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"linkId",b"linkId",u"vehId",b"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"linkId",b"time",b"vehId"]) -> None: ...

class PersonArrivalEvent(google___protobuf___message___Message):
    time = ... # type: float
    legMode = ... # type: typing___Text

    @property
    def linkId(self) -> LinkId: ...

    @property
    def persId(self) -> PersonId: ...

    def __init__(self,
        time : typing___Optional[float] = None,
        linkId : typing___Optional[LinkId] = None,
        legMode : typing___Optional[typing___Text] = None,
        persId : typing___Optional[PersonId] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PersonArrivalEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"linkId",u"persId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"legMode",u"linkId",u"persId",u"time"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"linkId",b"linkId",u"persId",b"persId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"legMode",b"linkId",b"persId",b"time"]) -> None: ...

class PersonDepartureEvent(google___protobuf___message___Message):
    time = ... # type: float
    legMode = ... # type: typing___Text

    @property
    def linkId(self) -> LinkId: ...

    @property
    def persId(self) -> PersonId: ...

    def __init__(self,
        time : typing___Optional[float] = None,
        linkId : typing___Optional[LinkId] = None,
        legMode : typing___Optional[typing___Text] = None,
        persId : typing___Optional[PersonId] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PersonDepartureEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"linkId",u"persId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"legMode",u"linkId",u"persId",u"time"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"linkId",b"linkId",u"persId",b"persId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"legMode",b"linkId",b"persId",b"time"]) -> None: ...

class PersonEntersVehicleEvent(google___protobuf___message___Message):
    time = ... # type: float

    @property
    def persId(self) -> PersonId: ...

    @property
    def vehId(self) -> VehicleId: ...

    def __init__(self,
        time : typing___Optional[float] = None,
        persId : typing___Optional[PersonId] = None,
        vehId : typing___Optional[VehicleId] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PersonEntersVehicleEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"persId",u"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"persId",u"time",u"vehId"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"persId",b"persId",u"vehId",b"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"persId",b"time",b"vehId"]) -> None: ...

class PersonLeavesVehicleEvent(google___protobuf___message___Message):
    time = ... # type: float

    @property
    def persId(self) -> PersonId: ...

    @property
    def vehId(self) -> VehicleId: ...

    def __init__(self,
        time : typing___Optional[float] = None,
        persId : typing___Optional[PersonId] = None,
        vehId : typing___Optional[VehicleId] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PersonLeavesVehicleEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"persId",u"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"persId",u"time",u"vehId"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"persId",b"persId",u"vehId",b"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"persId",b"time",b"vehId"]) -> None: ...

class PersonMoneyEvent(google___protobuf___message___Message):
    time = ... # type: float
    amount = ... # type: float

    @property
    def persId(self) -> PersonId: ...

    def __init__(self,
        time : typing___Optional[float] = None,
        persId : typing___Optional[PersonId] = None,
        amount : typing___Optional[float] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PersonMoneyEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"persId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"amount",u"persId",u"time"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"persId",b"persId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"amount",b"persId",b"time"]) -> None: ...

class PersonStuckEvent(google___protobuf___message___Message):
    time = ... # type: float
    legMode = ... # type: typing___Text

    @property
    def persId(self) -> PersonId: ...

    @property
    def linkId(self) -> LinkId: ...

    def __init__(self,
        time : typing___Optional[float] = None,
        persId : typing___Optional[PersonId] = None,
        linkId : typing___Optional[LinkId] = None,
        legMode : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PersonStuckEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"linkId",u"persId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"legMode",u"linkId",u"persId",u"time"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"linkId",b"linkId",u"persId",b"persId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"legMode",b"linkId",b"persId",b"time"]) -> None: ...

class TransitDriverStartsEvent(google___protobuf___message___Message):
    time = ... # type: float

    @property
    def driverId(self) -> PersonId: ...

    @property
    def vehId(self) -> VehicleId: ...

    @property
    def transitRouteId(self) -> TransitRouteId: ...

    @property
    def transitLineId(self) -> TransitLineId: ...

    @property
    def departureId(self) -> DepartureId: ...

    def __init__(self,
        time : typing___Optional[float] = None,
        driverId : typing___Optional[PersonId] = None,
        vehId : typing___Optional[VehicleId] = None,
        transitRouteId : typing___Optional[TransitRouteId] = None,
        transitLineId : typing___Optional[TransitLineId] = None,
        departureId : typing___Optional[DepartureId] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> TransitDriverStartsEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"departureId",u"driverId",u"transitLineId",u"transitRouteId",u"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"departureId",u"driverId",u"time",u"transitLineId",u"transitRouteId",u"vehId"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"departureId",b"departureId",u"driverId",b"driverId",u"transitLineId",b"transitLineId",u"transitRouteId",b"transitRouteId",u"vehId",b"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"departureId",b"driverId",b"time",b"transitLineId",b"transitRouteId",b"vehId"]) -> None: ...

class VehicleAbortsEvent(google___protobuf___message___Message):
    time = ... # type: float

    @property
    def vehId(self) -> VehicleId: ...

    @property
    def linkId(self) -> LinkId: ...

    def __init__(self,
        time : typing___Optional[float] = None,
        vehId : typing___Optional[VehicleId] = None,
        linkId : typing___Optional[LinkId] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> VehicleAbortsEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"linkId",u"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"linkId",u"time",u"vehId"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"linkId",b"linkId",u"vehId",b"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"linkId",b"time",b"vehId"]) -> None: ...

class VehicleEntersTrafficEvent(google___protobuf___message___Message):
    time = ... # type: float
    networkMode = ... # type: typing___Text
    relPosOnLink = ... # type: float

    @property
    def driverId(self) -> PersonId: ...

    @property
    def linkId(self) -> LinkId: ...

    @property
    def vehId(self) -> VehicleId: ...

    def __init__(self,
        time : typing___Optional[float] = None,
        driverId : typing___Optional[PersonId] = None,
        linkId : typing___Optional[LinkId] = None,
        vehId : typing___Optional[VehicleId] = None,
        networkMode : typing___Optional[typing___Text] = None,
        relPosOnLink : typing___Optional[float] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> VehicleEntersTrafficEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"driverId",u"linkId",u"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"driverId",u"linkId",u"networkMode",u"relPosOnLink",u"time",u"vehId"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"driverId",b"driverId",u"linkId",b"linkId",u"vehId",b"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"driverId",b"linkId",b"networkMode",b"relPosOnLink",b"time",b"vehId"]) -> None: ...

class VehicleLeavesTrafficEvent(google___protobuf___message___Message):
    time = ... # type: float
    networkMode = ... # type: typing___Text
    relPosOnLink = ... # type: float

    @property
    def driverId(self) -> PersonId: ...

    @property
    def linkId(self) -> LinkId: ...

    @property
    def vehId(self) -> VehicleId: ...

    def __init__(self,
        time : typing___Optional[float] = None,
        driverId : typing___Optional[PersonId] = None,
        linkId : typing___Optional[LinkId] = None,
        vehId : typing___Optional[VehicleId] = None,
        networkMode : typing___Optional[typing___Text] = None,
        relPosOnLink : typing___Optional[float] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> VehicleLeavesTrafficEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"driverId",u"linkId",u"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"driverId",u"linkId",u"networkMode",u"relPosOnLink",u"time",u"vehId"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"driverId",b"driverId",u"linkId",b"linkId",u"vehId",b"vehId"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"driverId",b"linkId",b"networkMode",b"relPosOnLink",b"time",b"vehId"]) -> None: ...

class DepartureId(google___protobuf___message___Message):
    id = ... # type: typing___Text

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DepartureId: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"id"]) -> None: ...

class TransitRouteId(google___protobuf___message___Message):
    id = ... # type: typing___Text

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> TransitRouteId: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"id"]) -> None: ...

class TransitLineId(google___protobuf___message___Message):
    id = ... # type: typing___Text

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> TransitLineId: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"id"]) -> None: ...

class DapartureId(google___protobuf___message___Message):
    id = ... # type: typing___Text

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DapartureId: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"id"]) -> None: ...

class VehicleId(google___protobuf___message___Message):
    id = ... # type: typing___Text

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> VehicleId: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"id"]) -> None: ...

class LinkId(google___protobuf___message___Message):
    id = ... # type: typing___Text

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LinkId: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"id"]) -> None: ...

class PersonId(google___protobuf___message___Message):
    id = ... # type: typing___Text

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PersonId: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"id"]) -> None: ...

class ActivityFacilityId(google___protobuf___message___Message):
    id = ... # type: typing___Text

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ActivityFacilityId: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"id"]) -> None: ...