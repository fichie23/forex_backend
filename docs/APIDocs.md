# API Documentation

## Currency Endpoints

Use this endpoint to add and delete currency data

### Add New Currency
> Default URL: `/forex/currency/`

> Method: `POST`

> Request:
```
{
  "base": "GBP",
  "target": "IDR"
}
```
> Response:

- Success:
  - Status Code: 200
```
{
    "id": 1,
    "base": "GBP",
    "target": "IDR"
}
```

- Error: Currency already exists
  - Status Code: 400
```
{
    "non_field_errors": [
        "The fields base, target must make a unique set."
    ]
}
```

### Delete Currency
> Default URL: `/forex/currency/delete/`

> Method: `DELETE`

> Request:
```
{
  "base": "GBP",
  "target": "IDR"
}
```
> Response:

- Success:
  - Status Code: 204 No Content


- Error: Data Currency Not Found
  - Status Code: 404
```
{
    "detail": "Not found."
}
```

### Add Daily Exchange Rate
> Default URL: `/forex/exchange/`

> Method: `POST`

> Request:
```
{
	"currency":{
		"base": "USD",
    	"target": "IDR"
	},
    "date": "2018-01-08",
    "rate": 0.4
}
```
> Response:

- Success:
  - Status Code: 200
```
{
    "id": 14,
    "currency": {
        "id": 20,
        "base": "USD",
        "target": "IDR"
    },
    "weekly_average": [
        {
            "currency": 20,
            "rate__avg": 0.35714285714285715
        }
    ],
    "date": "2018-01-08",
    "rate": 0.4
}
```

### List Exchange Rate by Date
> Default URL: `forex/history/?date=<yyyy-mm-dd>/`

> Method: `GET`

> Response:

- Success:
  - Status Code: 200
```
[
    {
        "id": 1,
        "exchange_rate_history": [],
        "base": "GBP",
        "target": "IDR"
    },
    {
        "id": 20,
        "exchange_rate_history": [
            {
                "id": 14,
                "weekly_average": [
                    {
                        "currency": 20,
                        "rate__avg": 0.35714285714285715
                    }
                ],
                "date": "2018-01-08",
                "rate": 0.4
            }
        ],
        "base": "USD",
        "target": "IDR"
    }
]
```