# Navegante Card Reader

## What is this?

This is basic console client that able to read the content from the Navegante (Lisboa) smartcard and structure it in a way that can be translated by the decoding API (https://navegante.rijo.io/). 

The output is a human readable json with the card content info.

## Software Requirements
 - [Python 3.7+](https://www.python.org/downloads/)
 - [pyscard](https://github.com/LudovicRousseau/pyscard/blob/master/INSTALL.md)
 
## Hardware Requirements

A PC/SC compliant smart card reader.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install -r requirements
```

## Usage

```bash
python main.py
```

## API Request Sample

```
{
    "atr": "3b6f0000805a2d0608101002782bdb35829000",
    "icc": null,
    "environment": "0000988008a7ca55d178b504bc0cc38892000000000316a00000000000",
    "contracts": {
        "0": "3e071444ba3aa098021512e81400000e0031e0214477b010b89b031098",
        "1": "3f067044fe27005c1c21880beffc003a60000000ec780210b89b03102c",
        "2": "3e0708421839a4000215086014257ff60011e04207c188819de2801098",
        "3": null
    },
    "history": {
        "0": "b631bd995b18d7820257d88d041000000480180192bae61af589440000",
        "1": "b631bd995b18d7820257d88d041000000480180192bae61af589240000",
        "2": "b631bd995b18d7820257d88d041000000480180192bae61af589240000"
    },
    "counters": {
        "0": "0000000000000000000000ffffff000000000000000000000000000000",
        "1": "0000820000000000000000ffffff000000000000000000000000000000",
        "2": "0000000000000000000000ffffff000000000000000000000000000000",
        "3": "0000000000000000000000ffffff000000000000000000000000000000",
        "4": "0000000000000000000000ffffff000000000000000000000000000000",
        "5": "0000000000000000000000ffffff000000000000000000000000000000",
        "6": "0000000000000000000000ffffff000000000000000000000000000000",
        "7": "0000000000000000000000ffffff000000000000000000000000000000",
        "8": "0000000000000000000000ffffff000000000000000000000000000000",
        "9": "0000000000820000000000000000000000000000000000000000000000"
    }
}
```

## Output Sample

```
{
    "atr": {
        "card_serial_number": 2016140085
    },
    "contracts": [
        {
            "id": 0,
            "temporal_amount_months": 1,
            "temporal_validity_type": "Months",
            "tick_class": "Normal",
            "tick_description": "Nav. Lisboa - Normal",
            "tick_interchange": false,
            "tick_load_operator": "Metropolitano de Lisboa",
            "tick_operator": "MultiModal",
            "tick_period_type": "No Restrictions",
            "tick_reload_daily_counter": 19,
            "tick_reload_date": "Mon, 01 Feb 2021 00:00:00 GMT",
            "tick_start_datetime": "Mon, 01 Feb 2021 00:00:00 GMT",
            "tick_utilizaton": "Transport",
            "trip_limit_type": "No counter",
            "validity_duration_type": "End of Exploitation",
            "version": 0
        },
        {
            "id": 1,
            "temporal_validity_type": "No Limit",
            "tick_class": "Normal",
            "tick_description": "ZAPPING",
            "tick_interchange": true,
            "tick_load_operator": "Metropolitano de Lisboa",
            "tick_operator": "MultiModal",
            "tick_period_type": "No Restrictions",
            "tick_reload_daily_counter": 11,
            "tick_reload_date": "Sun, 07 Mar 2021 00:00:00 GMT",
            "tick_utilizaton": "Transport",
            "trip_limit_amount": 130,
            "trip_limit_type": "1 Cent",
            "validity_duration": 0,
            "validity_duration_type": "Hours",
            "version": 0
        },
        {
            "id": 2,
            "temporal_amount_months": 1,
            "temporal_validity_type": "Months",
            "tick_class": "Normal",
            "tick_description": "Nav. Metropolitano - Normal",
            "tick_interchange": false,
            "tick_load_operator": "Metropolitano de Lisboa",
            "tick_operator": "MultiModal",
            "tick_period_type": "No Restrictions",
            "tick_reload_daily_counter": 128,
            "tick_reload_date": "Sun, 01 Mar 2020 00:00:00 GMT",
            "tick_start_datetime": "Sun, 01 Mar 2020 00:00:00 GMT",
            "tick_utilizaton": "Transport",
            "trip_limit_type": "No counter",
            "validity_duration_type": "End of Exploitation",
            "version": 0
        }
    ],
    "datetime": "Fri, 05 Nov 2021 18:34:30 GMT",
    "environment": {
        "card_number": "002 2749077",
        "country": "Portugal",
        "currency": "Euro",
        "expire_date": "Mon, 31 May 2021 00:00:00 GMT",
        "holder_birthdate": "Tue, 24 Nov 1987 00:00:00 GMT",
        "issue_date": "Tue, 23 May 2017 00:00:00 GMT",
        "issuer": "Metropolitano de Lisboa",
        "network": 2,
        "profile_code_1": "Normal",
        "profile_expire_date_1": "Mon, 31 May 2021 00:00:00 GMT",
        "version": 0
    },
    "history": [
        {
            "contract_1_expired": false,
            "contract_1_priority": 5,
            "contract_2_expired": false,
            "contract_2_priority": 7,
            "contract_3_expired": true,
            "contract_3_priority": 5,
            "contract_4_expired": true,
            "contract_4_priority": 0,
            "contract_5_expired": true,
            "contract_5_priority": 0,
            "contract_6_expired": true,
            "contract_6_priority": 5,
            "contract_id": 2,
            "contract_id_2": 3,
            "contracts_mask": 2,
            "datetime": "Sat, 20 Mar 2021 15:44:38 GMT",
            "first_entrance_datetime": "Sat, 20 Mar 2021 15:29:05 GMT",
            "first_entrance_datetime_2": "Fri, 06 Mar 2020 09:16:06 GMT",
            "id": 0,
            "interchanging": false,
            "operator_code": 2,
            "rfu_contract_1": 9,
            "rfu_contract_2": 17,
            "route_code": 3,
            "run_code": 3,
            "stop_index": 9,
            "stop_sub_index": 1,
            "tick_event_type": "Exit",
            "validator_id": 144
        },
        {
            "contract_1_expired": false,
            "contract_1_priority": 5,
            "contract_2_expired": false,
            "contract_2_priority": 7,
            "contract_3_expired": true,
            "contract_3_priority": 5,
            "contract_4_expired": true,
            "contract_4_priority": 0,
            "contract_5_expired": true,
            "contract_5_priority": 0,
            "contract_6_expired": true,
            "contract_6_priority": 5,
            "contract_id": 2,
            "contract_id_2": 3,
            "contracts_mask": 2,
            "datetime": "Sat, 20 Mar 2021 15:44:38 GMT",
            "first_entrance_datetime": "Sat, 20 Mar 2021 15:29:05 GMT",
            "first_entrance_datetime_2": "Fri, 06 Mar 2020 09:16:06 GMT",
            "id": 1,
            "interchanging": false,
            "operator_code": 2,
            "rfu_contract_1": 9,
            "rfu_contract_2": 9,
            "route_code": 3,
            "run_code": 3,
            "stop_index": 9,
            "stop_sub_index": 1,
            "tick_event_type": "Exit",
            "validator_id": 144
        },
        {
            "contract_1_expired": false,
            "contract_1_priority": 5,
            "contract_2_expired": false,
            "contract_2_priority": 7,
            "contract_3_expired": true,
            "contract_3_priority": 5,
            "contract_4_expired": true,
            "contract_4_priority": 0,
            "contract_5_expired": true,
            "contract_5_priority": 0,
            "contract_6_expired": true,
            "contract_6_priority": 5,
            "contract_id": 2,
            "contract_id_2": 3,
            "contracts_mask": 2,
            "datetime": "Sat, 20 Mar 2021 15:44:38 GMT",
            "first_entrance_datetime": "Sat, 20 Mar 2021 15:29:05 GMT",
            "first_entrance_datetime_2": "Fri, 06 Mar 2020 09:16:06 GMT",
            "id": 2,
            "interchanging": false,
            "operator_code": 2,
            "rfu_contract_1": 9,
            "rfu_contract_2": 9,
            "route_code": 3,
            "run_code": 3,
            "stop_index": 9,
            "stop_sub_index": 1,
            "tick_event_type": "Exit",
            "validator_id": 144
        }
    ],
    "id": "03a5ab36-3e67-11ec-a26b-1b2a442e7904"
}


```
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## References / Inspirations

[mobib-reader](https://github.com/bparmentier/mobib-reader)

[Metrodroid](https://github.com/metrodroid/metrodroid)

[CardPeek](https://github.com/L1L1/cardpeek)

## License
[MIT](https://choosealicense.com/licenses/mit/)


