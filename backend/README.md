# Backend(Python Server)

A python based server to fetch stock data based on Investment Strategies.

## Prerequisites

* Linux, Mac, or Windows machine
* Python
* Flask web framework


## API Details

```
POST /getData

```

Form data:

| Field          | Description                                                       | Optional   |
| -------------- | ----------------------------------------------------------------- | ---------- |
| `Strategies`   | One or two strategies as array ["Strategy 1","Strategy 2"]        | no         |
| `Amount`       | Investment Amount                                                 | no         |

