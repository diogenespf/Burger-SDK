# Order
(*order*)

## Overview

Operations related to orders

### Available Operations

* [list_orders](#list_orders) - List Orders
* [create_order](#create_order) - Create Order
* [read_order](#read_order) - Read Order
* [update_order](#update_order) - Update Order

## list_orders

List all orders

### Example Usage

```python
import apitizing_burgers

s = apitizing_burgers.APItizingBurgers()


res = s.order.list_orders()

if res.response_listorders is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.ListOrdersResponse](../../models/operations/listordersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_order

Create an order

### Example Usage

```python
import apitizing_burgers
from apitizing_burgers.models import components

s = apitizing_burgers.APItizingBurgers()


res = s.order.create_order(request=components.OrderCreate(
    burger_ids=[
        1,
        3,
    ],
    table=1,
    note='No onions',
))

if res.order_output is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [components.OrderCreate](../../models/components/ordercreate.md)    | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.CreateOrderResponse](../../models/operations/createorderresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## read_order

Read an order

### Example Usage

```python
import apitizing_burgers

s = apitizing_burgers.APItizingBurgers()


res = s.order.read_order(order_id=816257)

if res.order_output is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `order_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.ReadOrderResponse](../../models/operations/readorderresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ResponseMessage     | 404                        | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## update_order

Update an order

### Example Usage

```python
import apitizing_burgers
from apitizing_burgers.models import components

s = apitizing_burgers.APItizingBurgers()


res = s.order.update_order(order_id=928345, order_update=components.OrderUpdate(
    burger_ids=[
        1,
        2,
    ],
    table=1,
    status=components.OrderUpdateOrderStatus.READY,
    note='Extra ketchup',
))

if res.order_output is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `order_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `order_update`                                                      | [components.OrderUpdate](../../models/components/orderupdate.md)    | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.UpdateOrderResponse](../../models/operations/updateorderresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ResponseMessage     | 404                        | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |
