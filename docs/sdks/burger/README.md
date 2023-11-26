# Burger
(*burger*)

## Overview

Operations related to burgers

Burger external docs
<https://en.wikipedia.org/wiki/Hamburger>
### Available Operations

* [list_burgers](#list_burgers) - List Burgers
* [create_burger](#create_burger) - Create Burger
* [delete_burger](#delete_burger) - Delete Burger
* [read_burger](#read_burger) - Read Burger
* [update_burger](#update_burger) - Update Burger

## list_burgers

List all burgers

### Example Usage

```python
import apitizing_burgers

s = apitizing_burgers.APItizingBurgers()


res = s.burger.list_burgers()

if res.response_listburgers is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.ListBurgersResponse](../../models/operations/listburgersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_burger

Create a burger

### Example Usage

```python
import apitizing_burgers
from apitizing_burgers.models import components

s = apitizing_burgers.APItizingBurgers()

req = components.BurgerCreate(
    name='Cheeseburger',
    description='Veggie burger with avocado',
)

res = s.burger.create_burger(req)

if res.burger_output is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [components.BurgerCreate](../../models/components/burgercreate.md)  | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.CreateBurgerResponse](../../models/operations/createburgerresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## delete_burger

Delete a burger

### Example Usage

```python
import apitizing_burgers
from apitizing_burgers.models import operations

s = apitizing_burgers.APItizingBurgers()


res = s.burger.delete_burger(burger_id=199926)

if res.response_message is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `burger_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.DeleteBurgerResponse](../../models/operations/deleteburgerresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ResponseMessage     | 404                        | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## read_burger

Read a burger

### Example Usage

```python
import apitizing_burgers
from apitizing_burgers.models import operations

s = apitizing_burgers.APItizingBurgers()


res = s.burger.read_burger(burger_id=102880)

if res.burger_output is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `burger_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.ReadBurgerResponse](../../models/operations/readburgerresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ResponseMessage     | 404                        | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## update_burger

Update a burger

### Example Usage

```python
import apitizing_burgers
from apitizing_burgers.models import components, operations

s = apitizing_burgers.APItizingBurgers()


res = s.burger.update_burger(burger_id=566190, burger_update=components.BurgerUpdate(
    name='Hamburger',
    description='Veggie burger with avocado',
))

if res.burger_output is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `burger_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `burger_update`                                                     | [components.BurgerUpdate](../../models/components/burgerupdate.md)  | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.UpdateBurgerResponse](../../models/operations/updateburgerresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ResponseMessage     | 404                        | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |