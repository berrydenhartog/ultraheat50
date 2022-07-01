"""classes for UH50"""
from datetime import datetime
from typing import Optional

from dateutil import parser
from pydantic import BaseModel

from .helpers import is_date, is_float


class UHResponse(BaseModel):
    """response class for UH 50"""

    QuantityOfHeat: float = ...  # 6.8(0203.649*GJ)
    Volume: float = ...  # 6.26(02058.00*m3)
    MeterDateTime: Optional[datetime]  # 9.36(2022-06-03&20:45:07)
    OwnershipNumber: Optional[int]  # 9.21(00000000)
    VolumePreviousYear: Optional[float]  # 6.26*01(01968.44*m3)
    QuantityofHeatPreviousyear: Optional[float]  # 6.8*01(0192.076*GJ)
    ErrorNumber: Optional[int]  # F(0)
    HeatEquipmentId: Optional[int]  # 0.0(00000000)
    DeviceNumber: Optional[int]  # 9.20(00000000)
    MeasurementPeriode: Optional[int]  # 6.35(60*m) -
    PowerMax: Optional[float]  # 6.6(0013.0*kW) -
    PowerMaxPreviousYear: Optional[float]  # 6.6*01(0013.0*kW) -
    FlowrateMax: Optional[float]  # 6.33(000.528*m3ph) -
    OperatingHours: Optional[int]  # 6.31(0111423*h) -
    FaultHours: Optional[int]  # 6.32(0000339*h)
    FaultHoursPreviousYear: Optional[int]  # 6.32*01(0000339*h) -
    FlowrateMaxPreviousYear: Optional[float]  # 6.33*01(000.528*m3ph)
    MeasuringRange: Optional[float]  # 9.24(1.5*m3ph) -
    FlowHours: Optional[int]  # 9.31(0012689*h)
    # 9.4(082.2*C&079.6*C) Flow Temperature Max / Return Temperature Max
    # 9.6(000&00000000&0&000&00000000&0) - Eneco settings
    # 6.36(01-01&00:00) - Yearly set Day
    # 9.4*01(082.2*C&079.6*C) - Flow Temperature Max / Return Temperature Max Previous Year
    # 6.36.1(2012-02-19) - Time Poiny
    # 6.36.1*01(2012-02-19) - Time Poiny
    # 6.36.2(2019-12-22) - Time Poiny
    # 6.36.2*01(2019-12-22) - Time Poiny
    # 6.36.3(2018-02-27) - Time Poiny
    # 6.36.3*01(2018-02-27) - Time Poiny
    # 6.36.4(2019-10-25) - Time Poiny
    # 6.36.4*01(2019-10-25) - Time Poiny
    # 6.36.5() - Time Poiny
    # 6.36*02(01&00:00) - Monthly Set Day
    # 9.1(0&0&0&0000&0000&0000&0&0.00&0.00&0&000008&000000&00&0) - settings and firmware

    @staticmethod
    def from_uh50_data(heat_data):
        """convert data to model"""

        # prepare data for easy usage
        my_list = "".join(heat_data).replace("()", "( )").split(")")
        my_list.pop()
        my_list_of_list = [i.split("(") for i in my_list]
        item_dict = {item[0]: item[1].split("*", 1)[0] for item in my_list_of_list}

        # convert datatypes automaticly
        for key in item_dict:
            if item_dict[key].isdigit():
                item_dict[key] = int(item_dict[key])
            elif is_float(item_dict[key]):
                item_dict[key] = float(item_dict[key])
            elif is_date(item_dict[key]):
                item_dict[key] = parser.parse(item_dict[key])
            elif key == "9.36":
                item_dict[key] = parser.parse(item_dict[key].replace("&", " "))

        return UHResponse(
            QuantityOfHeat=item_dict["6.8"],
            Volume=item_dict["6.26"],
            MeterDateTime=item_dict["9.36"],
            OwnershipNumber=item_dict["9.21"],
            VolumePreviousYear=item_dict["6.26*01"],
            QuantityofHeatPreviousyear=item_dict["6.8*01"],
            ErrorNumber=item_dict["F"],
            HeatEquipmentId=item_dict["0.0"],
            DeviceNumber=item_dict["9.20"],
            MeasurementPeriode=item_dict["6.35"],
            PowerMax=item_dict["6.6"],
            PowerMaxPreviousYear=item_dict["6.6*01"],
            FlowrateMax=item_dict["6.33"],
            OperatingHours=item_dict["6.31"],
            FaultHours=item_dict["6.32"],
            FaultHoursPreviousYear=item_dict["6.32*01"],
            FlowrateMaxPreviousYear=item_dict["6.33*01"],
            MeasuringRange=item_dict["9.24"],
            FlowHours=item_dict["9.31"],
        )
